"""
FastAPI web server — serves the static HTML site and exposes a RAG Q&A endpoint.

Usage:
    python -m web_server.server                        # port 8000, Anthropic provider
    python -m web_server.server --port 8080
    python -m web_server.server --provider github      # GPT-4o via GitHub Models

Endpoints:
    GET  /              → serves output/site/index.html
    GET  /{path}        → serves any static file from output/site/
    POST /api/ask       → RAG Q&A, returns JSON {answer, matched_pages, chunks_count}
"""

from __future__ import annotations

import asyncio
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import typer
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

# Project root on sys.path so rag.* imports work when invoked as a module
sys.path.insert(0, str(Path(__file__).parent.parent))

from rag.query import _answer, _smart_retrieve  # noqa: E402

load_dotenv()

SITE_DIR  = Path(os.getenv("SITE_DIR", "output/site"))
PROVIDERS = {"anthropic", "github"}

# Blocking RAG calls run in this thread pool so the async event loop is never blocked
_executor = ThreadPoolExecutor(max_workers=2)

_RICH_TAG = re.compile(r"\[/?[^\]]+\]")


def _strip_rich(text: str) -> str:
    """Remove Rich markup tags (e.g. [red]...[/red]) from answer strings."""
    return _RICH_TAG.sub("", text)


# ── Pydantic models ───────────────────────────────────────────────────────────

class AskRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)
    provider: str = Field(default="anthropic")
    top_k: int = Field(default=8, ge=1, le=20)


class PageMatch(BaseModel):
    title: str
    url: str
    relevance: float


class AskResponse(BaseModel):
    answer: str
    matched_pages: list[PageMatch]
    chunks_count: int


# ── App factory ───────────────────────────────────────────────────────────────

def create_app(default_provider: str = "anthropic") -> FastAPI:
    app = FastAPI(
        title="PS Docs",
        description="Payment Solutions documentation Q&A server",
        docs_url=None,
        redoc_url=None,
    )

    @app.get("/api/config")
    async def config():
        return {"provider": default_provider}

    @app.post("/api/ask", response_model=AskResponse)
    async def ask(req: AskRequest):
        if req.provider not in PROVIDERS:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid provider '{req.provider}'. Choose: {sorted(PROVIDERS)}",
            )

        loop = asyncio.get_event_loop()

        try:
            matched_pages_raw, chunks, _ = await loop.run_in_executor(
                _executor,
                lambda: _smart_retrieve(req.question, top_k=req.top_k),
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Retrieval error: {exc}") from exc

        if not chunks and not matched_pages_raw:
            return AskResponse(
                answer="No relevant documentation found for this question.",
                matched_pages=[],
                chunks_count=0,
            )

        try:
            raw_answer = await loop.run_in_executor(
                _executor,
                lambda: _answer(req.question, chunks, provider=req.provider),
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"LLM error: {exc}") from exc

        matched = [
            PageMatch(
                title=p["metadata"].get("title") or p["metadata"].get("section_path") or "Unknown",
                url=p["metadata"].get("url", ""),
                relevance=p.get("relevance", 0.0),
            )
            for p in matched_pages_raw
        ]

        return AskResponse(
            answer=_strip_rich(raw_answer),
            matched_pages=matched,
            chunks_count=len(chunks),
        )

    @app.get("/")
    async def root():
        index = SITE_DIR / "index.html"
        if index.exists():
            return FileResponse(str(index))
        raise HTTPException(
            status_code=503,
            detail="Site not yet built. Run: python -m summarizer.build_site",
        )

    @app.get("/{full_path:path}")
    async def serve_static(full_path: str):
        # Don't intercept API routes (shouldn't reach here, but defensive)
        if full_path.startswith("api/"):
            raise HTTPException(status_code=404)
        candidate = SITE_DIR / full_path
        if candidate.is_file():
            return FileResponse(str(candidate))
        index = candidate / "index.html"
        if index.exists():
            return FileResponse(str(index))
        raise HTTPException(status_code=404, detail=f"Not found: {full_path}")

    return app


# ── CLI ───────────────────────────────────────────────────────────────────────

cli = typer.Typer(help="PS Docs web server", invoke_without_command=True)


@cli.command()
def serve(
    port: int = typer.Option(8000, "--port", "-p", help="Port to listen on"),
    host: str = typer.Option("127.0.0.1", "--host", help="Host to bind to"),
    provider: str = typer.Option(
        "anthropic", "--provider", help="Default LLM provider (anthropic|github)"
    ),
    rebuild: bool = typer.Option(
        False, "--rebuild", "-r",
        help="Force a full site rebuild before starting (default: incremental)",
    ),
):
    """Start the PS Docs web server, building the site first if needed."""
    import threading
    import webbrowser

    if provider not in PROVIDERS:
        typer.echo(f"Invalid provider '{provider}'. Choose from: {sorted(PROVIDERS)}", err=True)
        raise typer.Exit(1)

    # ── Build site before serving ──────────────────────────────────────────────
    project_root = Path(__file__).parent.parent
    build_cmd = [sys.executable, "-m", "summarizer.build_site", "--no-api"]
    if rebuild:
        build_cmd.append("--force")
        typer.echo("Rebuilding documentation site (force)...")
    else:
        typer.echo("Building documentation site (incremental)...")

    proc = subprocess.run(build_cmd, cwd=str(project_root))
    if proc.returncode != 0:
        typer.echo("Warning: site build had errors. Starting server anyway.", err=True)

    url = f"http://{host}:{port}"
    typer.echo(f"PS Docs server → {url}")
    typer.echo(f"  API:      POST {url}/api/ask")
    typer.echo(f"  Provider: {provider}")

    # Open browser after a short delay to let the server start
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()

    app = create_app(default_provider=provider)
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    cli()
