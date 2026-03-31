"""
Payment Solutions Documentation Summarizer
Generates 3-tier hierarchical summaries using the Claude API.

Tiers:
  1. Page-level  — bullet-point summary per crawled page
  2. Section     — synthesis of all pages in a section
  3. Master      — top-level architect's guide across all sections

Usage:
    python -m summarizer.summarize run
    python -m summarizer.summarize run --tier page   # only page summaries
    python -m summarizer.summarize run --tier all    # all tiers (default)
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Literal

import anthropic
import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

load_dotenv()
app = typer.Typer(help="PS Documentation Summarizer")
console = Console()

PAGES_DIR = Path(os.getenv("PAGES_DIR", "output/pages"))
SUMMARIES_DIR = Path(os.getenv("SUMMARIES_DIR", "output/summaries"))
SITE_MAP_PATH = Path(os.getenv("SITE_MAP_PATH", "output/site_map.json"))
MODEL = "claude-haiku-4-5-20251001"  # fast + cheap for bulk summarization
ARCHITECT_CONTEXT = (
    "You are briefing a Solutions Architect who is joining a Payment Solutions team. "
    "Use precise technical language. Focus on: key concepts, data flows, integration points, "
    "constraints, and anything an architect needs to understand before designing enhancements."
)


def _claude_client() -> anthropic.Anthropic:
    key = os.getenv("ANTHROPIC_API_KEY", "")
    if not key:
        console.print("[red]ANTHROPIC_API_KEY not set in .env[/red]")
        raise typer.Exit(1)
    return anthropic.Anthropic(api_key=key)


def _summarize_page(client: anthropic.Anthropic, page: dict) -> str:
    """Generate a bullet-point summary of a single page."""
    body = page.get("body_text", "")
    if len(body) < 100:
        return f"*Page appears empty or very short.*\n\nURL: {page['url']}"

    # Truncate very long pages to fit context (keep first 12k chars)
    body_excerpt = body[:12000] + ("\n\n[content truncated...]" if len(body) > 12000 else "")

    prompt = f"""You are summarizing a page from the Payment Solutions documentation portal.

Page title: {page.get('title', 'Unknown')}
Section path: {page.get('section_path', 'Unknown')}
URL: {page.get('url', '')}

--- PAGE CONTENT ---
{body_excerpt}
--- END ---

{ARCHITECT_CONTEXT}

Write a concise summary (5-8 bullet points) covering:
- What this page is about (one sentence)
- Key concepts, processes, or rules defined
- Any important data structures, fields, or codes mentioned
- Integration points or dependencies on other systems
- Anything an architect must know

Format as markdown bullet points. Be specific, not generic."""

    msg = client.messages.create(
        model=MODEL,
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def _summarize_section(client: anthropic.Anthropic, section_name: str, page_summaries: list[dict]) -> str:
    """Generate a section-level synthesis from individual page summaries."""
    summaries_text = "\n\n".join(
        f"### {ps['title']} ({ps['url']})\n{ps['summary']}"
        for ps in page_summaries
    )
    if not summaries_text.strip():
        return f"*No pages found in section: {section_name}*"

    prompt = f"""You are synthesizing documentation for a Solutions Architect.

Section: {section_name}
Number of pages: {len(page_summaries)}

--- PAGE SUMMARIES ---
{summaries_text[:15000]}
--- END ---

{ARCHITECT_CONTEXT}

Write a section overview (max 400 words) covering:
1. **Purpose of this section** — what capability or domain it covers
2. **Key concepts** — 3-5 most important ideas/entities
3. **How it works** — high-level flow or process
4. **Integration points** — what this connects to
5. **Architect notes** — gotchas, constraints, or design implications

Use clear markdown headings."""

    msg = client.messages.create(
        model=MODEL,
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def _summarize_master(client: anthropic.Anthropic, section_summaries: list[dict]) -> str:
    """Generate the top-level master overview across all sections."""
    sections_text = "\n\n".join(
        f"## {ss['section']}\n{ss['summary']}"
        for ss in section_summaries
    )

    prompt = f"""You are creating an onboarding document for a Solutions Architect joining a Payment Solutions team.

The following section summaries cover the entire Payment Solutions documentation portal.

--- SECTION SUMMARIES ---
{sections_text[:20000]}
--- END ---

{ARCHITECT_CONTEXT}

Create a comprehensive but scannable Master Architecture Guide (max 800 words) with:

## 1. System Overview
Brief description of what this Payment Solutions platform does.

## 2. Domain Map
Table or bullet list of all sections and what each covers (2 lines max per section).

## 3. Core Flows
The 3-5 most important end-to-end flows an architect must understand (e.g., payment auth, settlement, EFT).

## 4. Key Integration Points
External systems, APIs, protocols that the platform depends on or exposes.

## 5. Critical Design Constraints
Rules, limits, compliance requirements, or non-negotiables that will shape any enhancement project.

## 6. Where to Start Reading
Recommended reading order for a new architect — which sections are foundational vs. reference."""

    msg = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def _load_pages() -> list[dict]:
    """Load all crawled page JSON files."""
    pages = []
    for f in sorted(PAGES_DIR.glob("*.json")):
        try:
            pages.append(json.loads(f.read_text()))
        except json.JSONDecodeError:
            console.print(f"[yellow]Skipping malformed JSON: {f.name}[/yellow]")
    return pages


def _group_by_section(pages: list[dict]) -> dict[str, list[dict]]:
    """Group pages by their top-level section, skipping the 'ps_manual' portal prefix."""
    from urllib.parse import unquote
    groups: dict[str, list[dict]] = {}
    for page in pages:
        path = unquote(page.get("section_path", "root"))
        parts = [p.strip() for p in path.split(" > ") if p.strip() and p.strip() != "ps_manual"]
        top_section = parts[0] if parts else "root"
        groups.setdefault(top_section, []).append(page)
    return groups


@app.command()
def run(
    tier: str = typer.Option("all", "--tier", help="Which tier to generate: page, section, master, all"),
    resume: bool = typer.Option(False, "--resume", help="Skip pages that already have summaries"),
    pages_dir: Path = typer.Option(PAGES_DIR, "--pages-dir"),
    summaries_dir: Path = typer.Option(SUMMARIES_DIR, "--summaries-dir"),
):
    """Generate hierarchical summaries from crawled pages."""
    summaries_dir.mkdir(parents=True, exist_ok=True)
    (summaries_dir / "pages").mkdir(exist_ok=True)
    (summaries_dir / "sections").mkdir(exist_ok=True)

    pages = _load_pages()
    if not pages:
        console.print(f"[red]No pages found in {pages_dir}. Run the crawler first.[/red]")
        raise typer.Exit(1)

    console.print(f"[green]Loaded {len(pages)} crawled pages[/green]")
    client = _claude_client()

    # ── Tier 1: Page summaries ──────────────────────────────────────────────
    page_summaries: list[dict] = []
    if tier in ("page", "all"):
        console.print("\n[bold]Tier 1: Page summaries[/bold]")
        with Progress(SpinnerColumn(), TextColumn("{task.description}"), console=console) as progress:
            task = progress.add_task("Summarizing pages...", total=len(pages))
            for page in pages:
                slug = page["url"].replace("https://", "").replace("/", "_").replace(".", "_")[:80]
                out_path = summaries_dir / "pages" / f"{slug}.md"

                if resume and out_path.exists():
                    progress.advance(task)
                    summary_text = out_path.read_text()
                else:
                    progress.update(task, description=f"[cyan]{page.get('title', page['url'])[-50:]}[/cyan]")
                    summary_text = _summarize_page(client, page)
                    out_path.write_text(summary_text)
                    progress.advance(task)

                page_summaries.append({
                    "url": page["url"],
                    "title": page.get("title", ""),
                    "section_path": page.get("section_path", ""),
                    "summary": summary_text,
                })

        console.print(f"[green]✓ {len(page_summaries)} page summaries saved to {summaries_dir}/pages/[/green]")
    else:
        # Load existing page summaries for higher tiers
        for f in sorted((summaries_dir / "pages").glob("*.md")):
            page_summaries.append({"url": "", "title": f.stem, "section_path": "", "summary": f.read_text()})

    # ── Tier 2: Section summaries ───────────────────────────────────────────
    section_summaries: list[dict] = []
    if tier in ("section", "all"):
        console.print("\n[bold]Tier 2: Section summaries[/bold]")
        # Re-group using original page section paths
        groups = _group_by_section(pages)

        with Progress(SpinnerColumn(), TextColumn("{task.description}"), console=console) as progress:
            task = progress.add_task("Summarizing sections...", total=len(groups))
            for section_name, section_pages in groups.items():
                out_path = summaries_dir / "sections" / f"{section_name[:60]}.md"
                progress.update(task, description=f"[cyan]{section_name}[/cyan]")

                # Get page summaries for this section
                section_page_summaries = [
                    ps for ps in page_summaries
                    if ps.get("section_path", "").startswith(section_name)
                ] or [{"title": p.get("title", ""), "url": p["url"], "summary": ""} for p in section_pages]

                if resume and out_path.exists():
                    summary_text = out_path.read_text()
                else:
                    summary_text = _summarize_section(client, section_name, section_page_summaries)
                    out_path.write_text(summary_text)

                progress.advance(task)
                section_summaries.append({"section": section_name, "summary": summary_text})

        console.print(f"[green]✓ {len(section_summaries)} section summaries saved to {summaries_dir}/sections/[/green]")
    else:
        for f in sorted((summaries_dir / "sections").glob("*.md")):
            section_summaries.append({"section": f.stem, "summary": f.read_text()})

    # ── Tier 3: Master summary ──────────────────────────────────────────────
    if tier in ("master", "all") and section_summaries:
        console.print("\n[bold]Tier 3: Master summary[/bold]")
        with Progress(SpinnerColumn(), TextColumn("{task.description}"), console=console) as progress:
            progress.add_task("Generating master architecture guide...")
            master_text = _summarize_master(client, section_summaries)

        master_path = summaries_dir / "master_summary.md"
        master_path.write_text(master_text)
        console.print(f"[green]✓ Master summary saved to {master_path}[/green]")
        console.print("\n[bold yellow]Master Summary Preview:[/bold yellow]")
        console.print(master_text[:1000] + "\n[dim]...(truncated, see master_summary.md)[/dim]")


@app.command()
def show_master():
    """Print the master summary to console."""
    master_path = SUMMARIES_DIR / "master_summary.md"
    if not master_path.exists():
        console.print("[red]No master summary found. Run: python -m summarizer.summarize run[/red]")
        raise typer.Exit(1)
    console.print(master_path.read_text())


if __name__ == "__main__":
    app()
