"""
Payment Solutions Docs MCP Server

Exposes the RAG system as MCP tools that Claude Code can call directly
during conversations, enabling in-context Q&A against the PS documentation.

Tools exposed:
  - search_docs(query, top_k)     — semantic search, returns chunks
  - ask_docs(question, top_k)     — full RAG answer via Claude
  - get_section_summary(section)  — retrieve a pre-built section summary
  - get_master_summary()          — retrieve the top-level architecture guide
  - list_sections()               — list all available sections

Registration in Claude Code (~/.claude/settings.json):
  {
    "mcpServers": {
      "ps-docs": {
        "command": "python",
        "args": ["/Users/binoydas/Documents/Code/Central1/ps-docs-rag/mcp_server/server.py"],
        "env": {
          "ANTHROPIC_API_KEY": "<your-key>",
          "CHROMA_DB_PATH": "/Users/binoydas/Documents/Code/Central1/ps-docs-rag/output/chroma_db",
          "SUMMARIES_DIR": "/Users/binoydas/Documents/Code/Central1/ps-docs-rag/output/summaries",
          "SITE_MAP_PATH": "/Users/binoydas/Documents/Code/Central1/ps-docs-rag/output/site_map.json"
        }
      }
    }
  }
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# Add project root to path so imports work when invoked by MCP
sys.path.insert(0, str(Path(__file__).parent.parent))

import anthropic
import chromadb
from dotenv import load_dotenv
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

load_dotenv()

CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH", "output/chroma_db")
COLLECTION_NAME = os.getenv("CHROMA_COLLECTION", "ps_docs")
SUMMARIES_DIR = Path(os.getenv("SUMMARIES_DIR", "output/summaries"))
SITE_MAP_PATH = Path(os.getenv("SITE_MAP_PATH", "output/site_map.json"))
ANSWER_MODEL = "claude-sonnet-4-6"

COL_SUMMARIES = "ps_docs_summaries"
COL_CONTENT   = "ps_docs_content"

_chroma_client_cache: chromadb.PersistentClient | None = None


def _client() -> chromadb.PersistentClient | None:
    global _chroma_client_cache
    if _chroma_client_cache is not None:
        return _chroma_client_cache
    db_path = Path(CHROMA_DB_PATH)
    if not db_path.exists():
        return None
    try:
        _chroma_client_cache = chromadb.PersistentClient(path=str(db_path))
        return _chroma_client_cache
    except Exception:
        return None


def _open_col(client: chromadb.PersistentClient, name: str) -> chromadb.Collection:
    from rag.embeddings import get_chroma_embeddings
    ef = get_chroma_embeddings()
    kwargs: dict = {"name": name}
    if ef:
        kwargs["embedding_function"] = ef
    return client.get_or_create_collection(**kwargs)


def _is_two_stage() -> bool:
    c = _client()
    if not c:
        return False
    try:
        existing = {col.name for col in c.list_collections()}
        return COL_SUMMARIES in existing and COL_CONTENT in existing
    except Exception:
        return False


def _retrieve(query: str, top_k: int = 6) -> tuple[list[dict], list[dict]]:
    """
    Return (matched_pages, content_chunks).

    Two-stage mode: Stage 1 matches pages via summary index, Stage 2 fetches content chunks.
    Flat mode: matched_pages is empty, content_chunks holds flat results.
    """
    c = _client()
    if not c:
        return [], []

    if _is_two_stage():
        try:
            summaries_col = _open_col(c, COL_SUMMARIES)
            content_col   = _open_col(c, COL_CONTENT)

            top_pages = max(5, top_k)
            s1 = summaries_col.query(
                query_texts=[query],
                n_results=min(top_pages, summaries_col.count()),
                include=["documents", "metadatas", "distances"],
            )
            matched_pages = [
                {"text": doc, "metadata": meta, "relevance": round(1 - dist, 3)}
                for doc, meta, dist in zip(
                    s1["documents"][0], s1["metadatas"][0], s1["distances"][0]
                )
            ]
            matched_urls = [p["metadata"].get("url", "") for p in matched_pages if p["metadata"].get("url")]

            if not matched_urls:
                return matched_pages, []

            s2 = content_col.query(
                query_texts=[query],
                where={"url": {"$in": matched_urls}},
                n_results=min(top_k, content_col.count()),
                include=["documents", "metadatas", "distances"],
            )
            content_chunks = [
                {"text": doc, "metadata": meta, "relevance": round(1 - dist, 3)}
                for doc, meta, dist in zip(
                    s2["documents"][0], s2["metadatas"][0], s2["distances"][0]
                )
            ]
            return matched_pages, content_chunks
        except Exception:
            pass  # fall through to flat

    # Flat fallback
    try:
        col = _open_col(c, COLLECTION_NAME)
        if col.count() == 0:
            return [], []
        results = col.query(
            query_texts=[query],
            n_results=min(top_k, col.count()),
            include=["documents", "metadatas", "distances"],
        )
        chunks = [
            {"text": doc, "metadata": meta, "relevance": round(1 - dist, 3)}
            for doc, meta, dist in zip(
                results["documents"][0], results["metadatas"][0], results["distances"][0]
            )
        ]
        return [], chunks
    except Exception:
        return [], []


def _format_chunks_for_output(matched_pages: list[dict], chunks: list[dict]) -> str:
    if not chunks and not matched_pages:
        return "No relevant documentation found for this query."

    parts = []

    if matched_pages:
        page_lines = []
        for p in matched_pages:
            meta = p["metadata"]
            title = meta.get("title") or meta.get("section_path") or "Unknown"
            url = meta.get("url", "")
            page_lines.append(f"- [{p['relevance']:.2f}] **{title}**" + (f"  \n  {url}" if url else ""))
        parts.append("### Stage 1 — Matched pages\n\n" + "\n".join(page_lines))

    for i, chunk in enumerate(chunks, 1):
        meta = chunk["metadata"]
        source = meta.get("title") or meta.get("section_path") or meta.get("url") or "Unknown"
        parts.append(
            f"## Source {i}: {source}\n"
            f"**Section:** {meta.get('section_path', 'N/A')}\n"
            f"**Relevance:** {chunk['relevance']:.3f}\n"
            f"**URL:** {meta.get('url', 'N/A')}\n\n"
            f"{chunk['text']}"
        )
    return "\n\n---\n\n".join(parts)


def _llm_answer(question: str, chunks: list[dict]) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key:
        return "ANTHROPIC_API_KEY not set. Cannot generate LLM answer."
    if not chunks:
        return "No relevant documentation found to answer this question."

    client = anthropic.Anthropic(api_key=api_key)
    context_parts = []
    for i, chunk in enumerate(chunks, 1):
        meta = chunk["metadata"]
        source = meta.get("title") or meta.get("section_path") or "Unknown"
        context_parts.append(f"[Source {i}: {source}]\n{chunk['text']}")
    context = "\n\n---\n\n".join(context_parts)

    msg = client.messages.create(
        model=ANSWER_MODEL,
        max_tokens=1500,
        system=(
            "You are an expert assistant for the Payment Solutions platform documentation. "
            "Answer questions based strictly on the provided documentation context. "
            "Cite sources using [Source N] notation. Be precise and technical."
        ),
        messages=[{
            "role": "user",
            "content": (
                f"Based on the following Payment Solutions documentation, answer this question:\n\n"
                f"**Question:** {question}\n\n"
                f"**Documentation Context:**\n{context}"
            ),
        }],
    )
    return msg.content[0].text


def _get_section_names() -> list[str]:
    sections_dir = SUMMARIES_DIR / "sections"
    if not sections_dir.exists():
        return []
    return sorted(f.stem for f in sections_dir.glob("*.md"))


# ── MCP Server setup ─────────────────────────────────────────────────────────

server = Server("ps-docs")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="search_docs",
            description=(
                "Semantically search the Payment Solutions documentation. "
                "Returns the most relevant documentation chunks for a query. "
                "Use this to find specific information about PS features, processes, or APIs."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query (e.g., 'EFT settlement process', 'card authorization rules')",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Number of results to return (default 6, max 20)",
                        "default": 6,
                    },
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="ask_docs",
            description=(
                "Ask a question about the Payment Solutions documentation and get a synthesized answer. "
                "This performs RAG (retrieval-augmented generation): retrieves relevant docs, "
                "then uses Claude to compose a comprehensive answer. "
                "Prefer this over search_docs when you need a complete, synthesized response."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "The question to answer (e.g., 'How does EFT batch settlement work?')",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Number of context chunks to retrieve (default 6)",
                        "default": 6,
                    },
                },
                "required": ["question"],
            },
        ),
        Tool(
            name="get_section_summary",
            description=(
                "Retrieve the pre-generated summary for a specific documentation section. "
                "Use list_sections first to find available section names."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "section": {
                        "type": "string",
                        "description": "Section name (as returned by list_sections)",
                    },
                },
                "required": ["section"],
            },
        ),
        Tool(
            name="get_master_summary",
            description=(
                "Retrieve the master architecture guide — a top-level overview of the entire "
                "Payment Solutions documentation. Good starting point for onboarding."
            ),
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        Tool(
            name="list_sections",
            description=(
                "List all available sections in the Payment Solutions documentation. "
                "Returns section names that can be used with get_section_summary."
            ),
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "search_docs":
        query = arguments["query"]
        top_k = min(int(arguments.get("top_k", 6)), 20)
        matched_pages, chunks = _retrieve(query, top_k)
        result = _format_chunks_for_output(matched_pages, chunks)
        return [TextContent(type="text", text=result)]

    elif name == "ask_docs":
        question = arguments["question"]
        top_k = min(int(arguments.get("top_k", 6)), 12)
        _, chunks = _retrieve(question, top_k)
        answer = _llm_answer(question, chunks)
        return [TextContent(type="text", text=answer)]

    elif name == "get_section_summary":
        section = arguments["section"]
        summary_path = SUMMARIES_DIR / "sections" / f"{section}.md"
        if summary_path.exists():
            return [TextContent(type="text", text=summary_path.read_text())]
        # Try fuzzy match
        available = _get_section_names()
        matches = [s for s in available if section.lower() in s.lower()]
        if matches:
            summary_path = SUMMARIES_DIR / "sections" / f"{matches[0]}.md"
            return [TextContent(type="text", text=summary_path.read_text())]
        return [TextContent(
            type="text",
            text=f"Section '{section}' not found. Available sections: {', '.join(available)}",
        )]

    elif name == "get_master_summary":
        master_path = SUMMARIES_DIR / "master_summary.md"
        if master_path.exists():
            return [TextContent(type="text", text=master_path.read_text())]
        return [TextContent(
            type="text",
            text="Master summary not yet generated. Run: python -m summarizer.summarize run",
        )]

    elif name == "list_sections":
        sections = _get_section_names()
        site_map_info = ""
        if SITE_MAP_PATH.exists():
            try:
                site_map = json.loads(SITE_MAP_PATH.read_text())
                total = site_map.get("total_pages", "unknown")
                site_map_info = f"\n\nTotal pages crawled: {total}"
            except Exception:
                pass

        if sections:
            result = "Available documentation sections:\n\n" + "\n".join(f"- {s}" for s in sections) + site_map_info
        else:
            result = (
                "No section summaries found. "
                "Run: python -m summarizer.summarize run\n\n"
                "Or check if ChromaDB has data: python -m rag.ingest stats"
            )
        return [TextContent(type="text", text=result)]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
