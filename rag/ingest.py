"""
RAG Ingestion — chunks crawled pages and loads them into ChromaDB.

Modes:
  two-stage (default)  — two collections:
      ps_docs_summaries  one entry per page (summary text or body preview)
      ps_docs_content    chunked body_text (raw, no summaries mixed in)

  flat                 — original behaviour: single ps_docs collection,
                         page chunks + summary chunks mixed together

Usage:
    python -m rag.ingest run                     # two-stage (recommended)
    python -m rag.ingest run --mode flat         # original flat collection
    python -m rag.ingest run --reset             # wipe collections then ingest
    python -m rag.ingest stats                   # show collection stats
    python -m rag.ingest reset                   # wipe collections
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from urllib.parse import unquote

import chromadb
import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import BarColumn, Progress, SpinnerColumn, TaskProgressColumn, TextColumn
from rich.table import Table

from rag.embeddings import get_chroma_embeddings

load_dotenv()


# ── Minimal text splitter (avoids langchain/sentence_transformers dependency) ──

class _RecursiveTextSplitter:
    """Recursive character text splitter — same logic as LangChain's implementation."""

    def __init__(self, chunk_size: int, chunk_overlap: int, separators: list[str]):
        self._chunk_size = chunk_size
        self._chunk_overlap = chunk_overlap
        self._separators = separators

    def split_text(self, text: str) -> list[str]:
        chunks = self._split(text, self._separators)
        return self._apply_overlap(chunks)

    def _split(self, text: str, seps: list[str]) -> list[str]:
        if len(text) <= self._chunk_size:
            return [text] if text.strip() else []
        # Find the first separator that appears in the text
        sep, remaining = "", []
        for i, s in enumerate(seps):
            if s == "" or s in text:
                sep, remaining = s, seps[i + 1:]
                break
        pieces = text.split(sep) if sep else list(text)
        # Merge pieces greedily up to chunk_size
        result: list[str] = []
        current = ""
        for piece in pieces:
            joined = (current + sep + piece) if current else piece
            if len(joined) <= self._chunk_size:
                current = joined
            else:
                if current:
                    result.append(current)
                if len(piece) > self._chunk_size and remaining:
                    result.extend(self._split(piece, remaining))
                    current = ""
                else:
                    current = piece
        if current:
            result.append(current)
        return result

    def _apply_overlap(self, chunks: list[str]) -> list[str]:
        if self._chunk_overlap <= 0 or len(chunks) <= 1:
            return chunks
        out = [chunks[0]]
        for chunk in chunks[1:]:
            tail = out[-1][-self._chunk_overlap:]
            out.append(tail + chunk)
        return out
app = typer.Typer(help="PS Docs RAG Ingestion")
console = Console()

PAGES_DIR    = Path(os.getenv("PAGES_DIR",     "output/pages"))
SUMMARIES_DIR = Path(os.getenv("SUMMARIES_DIR", "output/summaries"))
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH",   "output/chroma_db")

# Collection names
COL_FLAT      = os.getenv("CHROMA_COLLECTION", "ps_docs")          # legacy flat
COL_SUMMARIES = "ps_docs_summaries"                                  # two-stage stage-1
COL_CONTENT   = "ps_docs_content"                                    # two-stage stage-2


# ── ChromaDB helpers ──────────────────────────────────────────────────────────

def _chroma_client() -> chromadb.PersistentClient:
    Path(CHROMA_DB_PATH).mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=CHROMA_DB_PATH)


def _get_collection(name: str, reset: bool = False) -> chromadb.Collection:
    client = _chroma_client()
    ef = get_chroma_embeddings()
    if reset:
        try:
            client.delete_collection(name)
            console.print(f"[yellow]Deleted collection '{name}'[/yellow]")
        except Exception:
            pass
    kwargs: dict = {"name": name}
    if ef:
        kwargs["embedding_function"] = ef
    return client.get_or_create_collection(**kwargs)


def _batch_upsert(
    collection: chromadb.Collection,
    texts: list[str],
    metadatas: list[dict],
    ids: list[str],
    label: str = "Embedding and storing",
    batch_size: int = 100,
) -> None:
    with Progress(
        SpinnerColumn(), TextColumn("{task.description}"),
        BarColumn(), TaskProgressColumn(), console=console,
    ) as progress:
        task = progress.add_task(f"{label}...", total=len(texts))
        for start in range(0, len(texts), batch_size):
            end = min(start + batch_size, len(texts))
            collection.upsert(
                documents=texts[start:end],
                metadatas=metadatas[start:end],
                ids=ids[start:end],
            )
            progress.advance(task, end - start)


# ── Data helpers ──────────────────────────────────────────────────────────────

def _load_pages() -> list[dict]:
    pages = []
    for f in sorted(PAGES_DIR.glob("*.json")):
        try:
            pages.append(json.loads(f.read_text()))
        except json.JSONDecodeError:
            pass
    return pages


def _page_summary_text(page: dict) -> str:
    """
    Return the best available summary text for a page:
      1. Pre-generated markdown summary from output/summaries/pages/
      2. First 500 chars of body_text as a pseudo-summary
    """
    url = page.get("url", "")
    slug = url.replace("https://", "").replace("/", "_").replace(".", "_")[:80]
    summary_path = SUMMARIES_DIR / "pages" / f"{slug}.md"
    if summary_path.exists():
        text = summary_path.read_text().strip()
        if len(text) > 80 and not text.startswith("*Page appears empty"):
            return text
    # Fallback: clean body preview
    body = page.get("body_text", "").strip()
    return " ".join(body.split())[:500]


def _clean_section_path(raw: str) -> str:
    """Strip 'ps_manual' prefix and URL-decode section_path."""
    decoded = unquote(raw)
    parts = [p.strip() for p in decoded.split(" > ") if p.strip() and p.strip() != "ps_manual"]
    return " > ".join(parts) or "root"


def _chunk_pages(
    pages: list[dict],
    chunk_size: int,
    chunk_overlap: int,
) -> tuple[list[str], list[dict], list[str]]:
    """Split page body_text into chunks. Returns (texts, metadatas, ids)."""
    splitter = _RecursiveTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    texts, metadatas, ids = [], [], []
    for page in pages:
        body = page.get("body_text", "").strip()
        if len(body) < 50:
            continue
        chunks = splitter.split_text(body)
        for i, chunk in enumerate(chunks):
            texts.append(chunk)
            metadatas.append({
                "url": page.get("url", ""),
                "title": page.get("title", ""),
                "section_path": _clean_section_path(page.get("section_path", "")),
                "chunk_index": i,
                "total_chunks": len(chunks),
                "type": "page_content",
            })
            ids.append(f"content_{hash(page['url'])}_{i}")
    return texts, metadatas, ids


def _build_summary_docs(pages: list[dict]) -> tuple[list[str], list[dict], list[str]]:
    """
    Build one summary document per page for the summaries collection.
    Uses pre-generated markdown summaries where available, falls back to body preview.
    Also adds section-level summaries.
    """
    texts, metadatas, ids = [], [], []

    for i, page in enumerate(pages):
        summary = _page_summary_text(page)
        if not summary:
            continue
        texts.append(summary)
        metadatas.append({
            "url": page.get("url", ""),
            "title": page.get("title", ""),
            "section_path": _clean_section_path(page.get("section_path", "")),
            "type": "page_summary",
        })
        ids.append(f"summary_page_{i}")

    # Add section-level summaries
    sections_dir = SUMMARIES_DIR / "sections"
    if sections_dir.exists():
        for j, f in enumerate(sorted(sections_dir.glob("*.md"))):
            text = f.read_text().strip()
            if text:
                texts.append(text)
                metadatas.append({
                    "url": "",
                    "title": f"Section: {f.stem}",
                    "section_path": f.stem,
                    "type": "section_summary",
                })
                ids.append(f"summary_section_{j}")

    return texts, metadatas, ids


def _load_flat_summaries() -> list[dict]:
    """Load summaries in the old flat format (for --mode flat)."""
    summaries = []
    master_path = SUMMARIES_DIR / "master_summary.md"
    if master_path.exists():
        summaries.append({
            "text": master_path.read_text(),
            "metadata": {"type": "master_summary", "section_path": "root", "title": "Master Architecture Guide", "url": ""},
        })
    sections_dir = SUMMARIES_DIR / "sections"
    for f in sorted(sections_dir.glob("*.md")) if sections_dir.exists() else []:
        summaries.append({
            "text": f.read_text(),
            "metadata": {"type": "section_summary", "section_path": f.stem, "title": f"Section: {f.stem}", "url": ""},
        })
    pages_dir = SUMMARIES_DIR / "pages"
    for f in sorted(pages_dir.glob("*.md")) if pages_dir.exists() else []:
        summaries.append({
            "text": f.read_text(),
            "metadata": {"type": "page_summary", "section_path": "", "title": f.stem, "url": ""},
        })
    return summaries


def _chunk_flat_summaries(summaries: list[dict], chunk_size: int, chunk_overlap: int):
    splitter = _RecursiveTextSplitter(chunk_size=chunk_size * 2, chunk_overlap=chunk_overlap, separators=["\n\n", "\n", ". ", " ", ""])
    texts, metadatas, ids = [], [], []
    for i, s in enumerate(summaries):
        for j, chunk in enumerate(splitter.split_text(s["text"])):
            texts.append(chunk)
            metadatas.append({**s["metadata"], "chunk_index": j})
            ids.append(f"summary_{i}_{j}")
    return texts, metadatas, ids


# ── Commands ──────────────────────────────────────────────────────────────────

@app.command()
def run(
    mode: str = typer.Option("two-stage", "--mode", help="'two-stage' (recommended) or 'flat'"),
    chunk_size: int = typer.Option(800, "--chunk-size"),
    chunk_overlap: int = typer.Option(100, "--chunk-overlap"),
    reset: bool = typer.Option(False, "--reset", help="Wipe collections before ingesting"),
    pages_dir: Path = typer.Option(PAGES_DIR, "--pages-dir"),
):
    """Ingest crawled pages into ChromaDB.

    two-stage mode (default): creates ps_docs_summaries + ps_docs_content.
    flat mode: creates single ps_docs collection (original behaviour).
    """
    pages = _load_pages()
    if not pages:
        console.print(f"[red]No pages found in {pages_dir}. Run the crawler first.[/red]")
        raise typer.Exit(1)
    console.print(f"[green]Loaded {len(pages)} pages[/green]")

    if mode == "two-stage":
        _run_two_stage(pages, chunk_size, chunk_overlap, reset)
    elif mode == "flat":
        _run_flat(pages, chunk_size, chunk_overlap, reset)
    else:
        console.print(f"[red]Unknown mode '{mode}'. Use 'two-stage' or 'flat'.[/red]")
        raise typer.Exit(1)


def _run_two_stage(pages: list[dict], chunk_size: int, chunk_overlap: int, reset: bool) -> None:
    console.print("\n[bold]Two-stage mode[/bold]: building summary index + content index\n")

    # ── Stage 1 collection: one summary doc per page ──────────────────────────
    console.print("[bold cyan]Stage 1 collection: ps_docs_summaries[/bold cyan]")
    sum_texts, sum_metas, sum_ids = _build_summary_docs(pages)
    with_summary = sum(1 for m in sum_metas if m["type"] == "page_summary" and m["url"])
    with_fallback = len([m for m in sum_metas if m["type"] == "page_summary"]) - with_summary
    section_count = sum(1 for m in sum_metas if m["type"] == "section_summary")
    console.print(f"  {with_summary} pages with AI summaries")
    console.print(f"  {with_fallback} pages using body-text preview fallback")
    console.print(f"  {section_count} section summaries")
    console.print(f"  → {len(sum_texts)} total entries")

    col_summaries = _get_collection(COL_SUMMARIES, reset=reset)
    _batch_upsert(col_summaries, sum_texts, sum_metas, sum_ids, label="Indexing summaries")

    # ── Stage 2 collection: chunked body_text ────────────────────────────────
    console.print("\n[bold cyan]Stage 2 collection: ps_docs_content[/bold cyan]")
    con_texts, con_metas, con_ids = _chunk_pages(pages, chunk_size, chunk_overlap)
    console.print(f"  → {len(con_texts)} chunks from page body_text")

    col_content = _get_collection(COL_CONTENT, reset=reset)
    _batch_upsert(col_content, con_texts, con_metas, con_ids, label="Indexing content")

    console.print(f"\n[green]✓ ps_docs_summaries: {col_summaries.count()} entries[/green]")
    console.print(f"[green]✓ ps_docs_content:   {col_content.count()} chunks[/green]")
    console.print(f"  Persisted to: {CHROMA_DB_PATH}")


def _run_flat(pages: list[dict], chunk_size: int, chunk_overlap: int, reset: bool) -> None:
    console.print("\n[bold]Flat mode[/bold]: building single mixed collection (ps_docs)\n")
    col = _get_collection(COL_FLAT, reset=reset)

    texts, metadatas, ids = _chunk_pages(pages, chunk_size, chunk_overlap)
    console.print(f"  → {len(texts)} chunks from page content")

    summaries = _load_flat_summaries()
    if summaries:
        s_texts, s_meta, s_ids = _chunk_flat_summaries(summaries, chunk_size, chunk_overlap)
        texts += s_texts
        metadatas += s_meta
        ids += s_ids
        console.print(f"  → {len(s_texts)} chunks from summaries")

    console.print(f"\n[bold]Upserting {len(texts)} total chunks...[/bold]")
    _batch_upsert(col, texts, metadatas, ids)
    console.print(f"\n[green]✓ Collection '{COL_FLAT}' now has {col.count()} chunks[/green]")


@app.command()
def stats():
    """Show statistics for all ChromaDB collections."""
    client = _chroma_client()
    existing = {c.name for c in client.list_collections()}

    table = Table(title="ChromaDB Collections")
    table.add_column("Collection", style="cyan")
    table.add_column("Chunks", style="green")
    table.add_column("Mode", style="dim")

    for name, mode_label in [
        (COL_SUMMARIES, "two-stage stage-1"),
        (COL_CONTENT,   "two-stage stage-2"),
        (COL_FLAT,      "flat (legacy)"),
    ]:
        if name in existing:
            ef = get_chroma_embeddings()
            kwargs: dict = {"name": name}
            if ef:
                kwargs["embedding_function"] = ef
            col = client.get_or_create_collection(**kwargs)
            table.add_row(name, str(col.count()), mode_label)
        else:
            table.add_row(name, "—", f"{mode_label} (not built)")

    table.add_row("persist path", CHROMA_DB_PATH, "", end_section=False)
    console.print(table)


@app.command()
def reset():
    """Wipe all ChromaDB collections."""
    client = _chroma_client()
    for name in [COL_SUMMARIES, COL_CONTENT, COL_FLAT]:
        try:
            client.delete_collection(name)
            console.print(f"[yellow]Deleted '{name}'[/yellow]")
        except Exception:
            pass
    console.print("[green]✓ All collections reset[/green]")


if __name__ == "__main__":
    app()
