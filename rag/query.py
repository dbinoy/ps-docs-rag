"""
RAG Query CLI — standalone Q&A against the ChromaDB collection.
Supports two LLM providers selectable via --provider:
  anthropic  — claude-sonnet-4-6             (requires ANTHROPIC_API_KEY in .env)
  github     — GPT-4o via GitHub Models API  (requires GITHUB_TOKEN in .env)

Retrieval modes (auto-detected):
  two-stage  — Stage 1: search ps_docs_summaries for relevant pages
               Stage 2: fetch + re-rank content chunks from those pages
  flat       — fallback: single collection query (ps_docs)

Usage:
    python -m rag.query ask "What is the EFT settlement process?"
    python -m rag.query ask "What are the card authorization rules?" --top-k 8
    python -m rag.query ask "What are the card authorization rules?" --provider github
    python -m rag.query search "settlement"            # raw semantic search, no LLM
    python -m rag.query interactive                    # REPL mode (default: anthropic)
    python -m rag.query interactive --provider github
"""

from __future__ import annotations

import os
from pathlib import Path

import anthropic
import chromadb
import typer
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt

from rag.embeddings import get_chroma_embeddings

load_dotenv()
app = typer.Typer(help="PS Docs RAG Query")
console = Console()

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "output/chroma_db")
COLLECTION_NAME = os.getenv("CHROMA_COLLECTION", "ps_docs")

# ── LLM provider constants ────────────────────────────────────────────────────
ANTHROPIC_MODEL        = "claude-sonnet-4-6"
# GITHUB_MODEL           = "Meta-Llama-3.1-405B-Instruct"   # best available on your GitHub plan
GITHUB_MODEL = "gpt-4o"
GITHUB_MODELS_ENDPOINT = "https://models.inference.ai.azure.com"

# typer enum for --provider option
PROVIDERS = ["anthropic", "github"]

COL_SUMMARIES = "ps_docs_summaries"
COL_CONTENT   = "ps_docs_content"

SYSTEM_PROMPT = """You are an expert assistant for the Payment Solutions platform documentation.
You answer questions based strictly on the provided documentation context.
If the context doesn't contain enough information to fully answer, say so clearly.
Always cite the relevant section or page title when referencing specific information.
Be precise and technical — your audience is a Solutions Architect."""


# ── ChromaDB helpers ──────────────────────────────────────────────────────────

def _chroma_client() -> chromadb.PersistentClient:
    if not Path(CHROMA_DB_PATH).exists():
        console.print(
            f"[red]ChromaDB not found at {CHROMA_DB_PATH}. Run ingestion first:[/red]\n"
            "  python -m rag.ingest run"
        )
        raise typer.Exit(1)
    return chromadb.PersistentClient(path=CHROMA_DB_PATH)


def _open_collection(client: chromadb.PersistentClient, name: str) -> chromadb.Collection:
    ef = get_chroma_embeddings()
    kwargs: dict = {"name": name}
    if ef:
        kwargs["embedding_function"] = ef
    return client.get_or_create_collection(**kwargs)


def _is_two_stage() -> bool:
    """Return True if both two-stage collections exist in ChromaDB."""
    try:
        client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
        existing = {c.name for c in client.list_collections()}
        return COL_SUMMARIES in existing and COL_CONTENT in existing
    except Exception:
        return False


# ── Retrieval ─────────────────────────────────────────────────────────────────

def _retrieve_flat(query: str, top_k: int) -> list[dict]:
    """Single-collection retrieval (legacy flat mode)."""
    client = _chroma_client()
    col = _open_collection(client, COLLECTION_NAME)
    results = col.query(
        query_texts=[query],
        n_results=min(top_k, col.count()),
        include=["documents", "metadatas", "distances"],
    )
    return [
        {"text": doc, "metadata": meta, "distance": dist, "relevance": round(1 - dist, 3)}
        for doc, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0],
        )
    ]


def _retrieve_two_stage(
    query: str,
    top_pages: int = 5,
    top_chunks: int = 8,
) -> tuple[list[dict], list[dict]]:
    """
    Two-stage retrieval.

    Stage 1 — query ps_docs_summaries → identify the most relevant pages.
    Stage 2 — query ps_docs_content filtered to those pages → best full-text chunks.

    Returns (matched_pages, content_chunks).
    """
    client = _chroma_client()
    summaries_col = _open_collection(client, COL_SUMMARIES)
    content_col   = _open_collection(client, COL_CONTENT)

    # ── Stage 1: find relevant pages via summary index ────────────────────────
    s1 = summaries_col.query(
        query_texts=[query],
        n_results=min(top_pages, summaries_col.count()),
        include=["documents", "metadatas", "distances"],
    )

    matched_pages: list[dict] = []
    matched_urls: list[str] = []
    for doc, meta, dist in zip(s1["documents"][0], s1["metadatas"][0], s1["distances"][0]):
        matched_pages.append({
            "text": doc,
            "metadata": meta,
            "distance": dist,
            "relevance": round(1 - dist, 3),
        })
        url = meta.get("url", "")
        if url:
            matched_urls.append(url)

    if not matched_urls:
        return matched_pages, []

    # ── Stage 2: fetch best content chunks from matched pages ─────────────────
    s2 = content_col.query(
        query_texts=[query],
        where={"url": {"$in": matched_urls}},
        n_results=min(top_chunks, content_col.count()),
        include=["documents", "metadatas", "distances"],
    )

    content_chunks: list[dict] = [
        {"text": doc, "metadata": meta, "distance": dist, "relevance": round(1 - dist, 3)}
        for doc, meta, dist in zip(
            s2["documents"][0],
            s2["metadatas"][0],
            s2["distances"][0],
        )
    ]

    return matched_pages, content_chunks


def _smart_retrieve(
    query: str,
    top_k: int = 6,
    top_pages: int = 5,
) -> tuple[list[dict], list[dict], bool]:
    """
    Auto-detect retrieval mode and return (matched_pages, content_chunks, is_two_stage).

    For flat mode, matched_pages is empty and content_chunks holds the results.
    """
    if _is_two_stage():
        pages, chunks = _retrieve_two_stage(query, top_pages=top_pages, top_chunks=top_k)
        return pages, chunks, True
    else:
        chunks = _retrieve_flat(query, top_k)
        return [], chunks, False


# ── LLM answer ────────────────────────────────────────────────────────────────

def _format_context(chunks: list[dict]) -> str:
    parts = []
    for i, chunk in enumerate(chunks, 1):
        meta = chunk["metadata"]
        source = meta.get("title") or meta.get("section_path") or meta.get("url") or "Unknown"
        parts.append(
            f"[Source {i}: {source}]\n"
            f"Section: {meta.get('section_path', 'N/A')}\n"
            f"{chunk['text']}"
        )
    return "\n\n---\n\n".join(parts)


def _answer(question: str, chunks: list[dict], provider: str = "anthropic") -> str:
    """Generate an answer using either Anthropic (Claude) or GitHub Models (Llama-3.1-405B)."""
    context = _format_context(chunks)
    user_content = (
        f"Based on the following Payment Solutions documentation excerpts, "
        f"answer this question:\n\n"
        f"**Question:** {question}\n\n"
        f"**Documentation Context:**\n{context}\n\n"
        f"Provide a thorough, accurate answer. "
        f"Cite sources by their [Source N] label when referencing specific details."
    )

    if provider == "github":
        api_key = os.getenv("GITHUB_TOKEN", "")
        if not api_key:
            return (
                "[red]GITHUB_TOKEN not set.[/red] Add it to your .env file:\n"
                "  GITHUB_TOKEN=ghp_your_token_here"
            )
        try:
            client = OpenAI(base_url=GITHUB_MODELS_ENDPOINT, api_key=api_key)
            response = client.chat.completions.create(
                model=GITHUB_MODEL,
                max_tokens=1500,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_content},
                ],
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            return f"[red]GitHub Models API error:[/red] {e}"

    else:  # provider == "anthropic"
        api_key = os.getenv("ANTHROPIC_API_KEY", "")
        if not api_key:
            return (
                "[red]ANTHROPIC_API_KEY not set.[/red] Add it to your .env file, "
                "or use [bold]--provider github[/bold] instead."
            )
        try:
            client = anthropic.Anthropic(api_key=api_key)
            msg = client.messages.create(
                model=ANTHROPIC_MODEL,
                max_tokens=1500,
                system=SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_content}],
            )
            return msg.content[0].text
        except anthropic.APIConnectionError as e:
            return (
                f"[red]Connection error reaching Anthropic API.[/red]\n"
                f"Your corporate network may be blocking api.anthropic.com.\n"
                f"Try [bold]--provider github[/bold] instead.\n\n[dim]{e}[/dim]"
            )
        except anthropic.AuthenticationError:
            return "[red]Invalid ANTHROPIC_API_KEY. Check your .env file.[/red]"
        except anthropic.APIStatusError as e:
            return f"[red]Anthropic API error {e.status_code}:[/red] {e.message}"


# ── CLI commands ──────────────────────────────────────────────────────────────

@app.command()
def ask(
    question: str = typer.Argument(..., help="Question to ask about the PS documentation"),
    top_k: int = typer.Option(8, "--top-k", "-k", help="Number of content chunks to retrieve"),
    top_pages: int = typer.Option(5, "--top-pages", help="Number of pages matched in Stage 1 (two-stage only)"),
    show_sources: bool = typer.Option(False, "--show-sources", help="Print retrieved source chunks"),
    provider: str = typer.Option("anthropic", "--provider", "-p", help="LLM provider: 'anthropic' (Claude, default) or 'github' (GPT-4o)"),
):
    """Ask a question and get an LLM-synthesized answer from the docs."""
    if provider not in PROVIDERS:
        console.print(f"[red]Invalid provider '{provider}'. Choose from: {PROVIDERS}[/red]")
        raise typer.Exit(1)

    provider_label = (
        f"[cyan]Llama-3.1-405B[/cyan] via GitHub Models" if provider == "github"
        else f"[cyan]claude-sonnet-4-6[/cyan] via Anthropic"
    )
    console.print(f"\n[bold cyan]Question:[/bold cyan] {question}")
    console.print(f"[dim]Provider: {provider_label}[/dim]\n")

    with console.status("Searching documentation..."):
        matched_pages, chunks, two_stage = _smart_retrieve(question, top_k=top_k, top_pages=top_pages)

    if two_stage:
        console.print(f"[dim]Two-stage retrieval — Stage 1: {len(matched_pages)} pages matched, Stage 2: {len(chunks)} chunks[/dim]")
        if matched_pages:
            console.print("[dim]Matched pages:[/dim]")
            for p in matched_pages:
                title = p["metadata"].get("title") or p["metadata"].get("section_path") or p["metadata"].get("url") or "—"
                console.print(f"  [dim]• [{p['relevance']:.2f}] {title[:80]}[/dim]")
    else:
        console.print(f"[dim]Flat retrieval — {len(chunks)} chunks[/dim]")

    if not chunks:
        console.print("[yellow]No relevant chunks found.[/yellow]")
        raise typer.Exit(1)

    if show_sources:
        console.print(Panel(
            "\n\n".join(
                f"[dim]{i+1}. [{c['relevance']:.2f}] {c['metadata'].get('title', c['metadata'].get('url', ''))[:80]}[/dim]\n{c['text'][:300]}..."
                for i, c in enumerate(chunks)
            ),
            title="Retrieved Sources",
            border_style="dim",
        ))

    with console.status("Generating answer..."):
        answer = _answer(question, chunks, provider=provider)

    console.print(Panel(Markdown(answer), title="[bold green]Answer[/bold green]", border_style="green"))


@app.command()
def search(
    query: str = typer.Argument(..., help="Semantic search query"),
    top_k: int = typer.Option(5, "--top-k", "-k"),
    top_pages: int = typer.Option(5, "--top-pages"),
):
    """Raw semantic search — returns chunks without LLM synthesis."""
    with console.status("Searching..."):
        matched_pages, chunks, two_stage = _smart_retrieve(query, top_k=top_k, top_pages=top_pages)

    if two_stage and matched_pages:
        console.print(f"\n[bold cyan]Stage 1 — Matched pages ({len(matched_pages)}):[/bold cyan]")
        for p in matched_pages:
            meta = p["metadata"]
            title = meta.get("title") or meta.get("section_path") or "Unknown"
            url = meta.get("url", "")
            console.print(f"  [{p['relevance']:.2f}] [bold]{title[:70]}[/bold]")
            if url:
                console.print(f"         [dim]{url}[/dim]")

        console.print(f"\n[bold cyan]Stage 2 — Content chunks ({len(chunks)}):[/bold cyan]")

    for i, chunk in enumerate(chunks, 1):
        meta = chunk["metadata"]
        title = meta.get("title") or meta.get("section_path") or "Unknown"
        console.print(Panel(
            f"[dim]URL: {meta.get('url', 'N/A')}[/dim]\n"
            f"[dim]Section: {meta.get('section_path', 'N/A')}[/dim]\n"
            f"[dim]Relevance: {chunk['relevance']:.3f}[/dim]\n\n"
            f"{chunk['text'][:600]}{'...' if len(chunk['text']) > 600 else ''}",
            title=f"[bold]{i}. {title[:70]}[/bold]",
            border_style="cyan",
        ))


@app.command()
def interactive(
    provider: str = typer.Option("anthropic", "--provider", "-p", help="LLM provider: 'anthropic' (Claude, default) or 'github' (GPT-4o)"),
):
    """Start an interactive Q&A REPL session."""
    if provider not in PROVIDERS:
        console.print(f"[red]Invalid provider '{provider}'. Choose from: {PROVIDERS}[/red]")
        raise typer.Exit(1)

    provider_label = (
        f"[cyan]Llama-3.1-405B[/cyan] via GitHub Models" if provider == "github"
        else f"[cyan]claude-sonnet-4-6[/cyan] via Anthropic"
    )
    mode_label = "two-stage" if _is_two_stage() else "flat"
    console.print(Panel(
        f"[bold]Payment Solutions Documentation Q&A[/bold]\n"
        f"Retrieval mode: [cyan]{mode_label}[/cyan]  |  Provider: {provider_label}\n"
        "Type your question and press Enter. Type [bold]quit[/bold] or [bold]exit[/bold] to stop.\n"
        "Prefix with [bold]/search [/bold] for raw retrieval without LLM.",
        border_style="cyan",
    ))

    while True:
        try:
            question = Prompt.ask("\n[bold cyan]You[/bold cyan]")
        except (KeyboardInterrupt, EOFError):
            console.print("\n[dim]Goodbye![/dim]")
            break

        if question.lower() in ("quit", "exit", "q"):
            break

        if not question.strip():
            continue

        if question.startswith("/search "):
            raw_query = question[8:].strip()
            matched_pages, chunks, two_stage = _smart_retrieve(raw_query, top_k=5)
            if two_stage and matched_pages:
                console.print(f"\n[dim]Stage 1 matched {len(matched_pages)} pages:[/dim]")
                for p in matched_pages:
                    console.print(f"  [dim]• [{p['relevance']:.2f}] {p['metadata'].get('title', 'Unknown')[:70]}[/dim]")
                console.print()
            for i, chunk in enumerate(chunks, 1):
                meta = chunk["metadata"]
                console.print(f"\n[dim]{i}. [{chunk['relevance']:.2f}] {meta.get('title', 'Unknown')[:70]}[/dim]")
                console.print(f"   {chunk['text'][:300]}...")
        else:
            matched_pages, chunks, two_stage = _smart_retrieve(question, top_k=8)
            if not chunks:
                console.print("[yellow]No relevant chunks found.[/yellow]")
                continue
            if two_stage:
                console.print(f"[dim]Matched {len(matched_pages)} pages → {len(chunks)} chunks[/dim]")
            answer = _answer(question, chunks, provider=provider)
            console.print(f"\n[bold green]Assistant:[/bold green]")
            console.print(Markdown(answer))


if __name__ == "__main__":
    app()
