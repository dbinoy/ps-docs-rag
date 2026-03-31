"""
Build a navigable HTML summary site from crawled PS documentation pages.

Structure:
  output/site/
  ├── index.html                        ← master overview + section cards
  ├── {section}/
  │   ├── index.html                    ← section summary + doc-group/page list
  │   └── {doc-group}/
  │       ├── index.html                ← doc-group summary + page list (large sections only)
  │       └── {page}.html               ← individual page summary
  └── assets/style.css

Usage:
    python -m summarizer.build_site run
    python -m summarizer.build_site run --no-api   # skip Claude, use body-text previews only
"""

from __future__ import annotations

import json
import os
import re
import textwrap
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

import anthropic
import typer
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

load_dotenv()
app = typer.Typer(help="Build navigable HTML summary site")
console = Console()

PAGES_DIR     = Path(os.getenv("PAGES_DIR",     "output/pages"))
SUMMARIES_DIR = Path(os.getenv("SUMMARIES_DIR", "output/summaries"))
SITE_DIR      = Path("output/site")
MODEL         = "claude-haiku-4-5-20251001"

# The 8 sections from the portal's left-hand navigation menu
MAIN_SECTIONS = [
    "Access and Administration",
    "AFT",
    "Bill Payments",
    "Central 1 Banking Services",
    "Clearing and Deposits",
    "Currency",
    "Data Hub",
    "Electronic Transactions",
]

SECTION_COLORS = {
    "Access and Administration":   "#2563eb",
    "AFT":                         "#7c3aed",
    "Bill Payments":               "#059669",
    "Central 1 Banking Services":  "#d97706",
    "Clearing and Deposits":       "#dc2626",
    "Currency":                    "#0891b2",
    "Data Hub":                    "#4f46e5",
    "Electronic Transactions":     "#be185d",
}

SECTION_ICONS = {
    "Access and Administration":   "🔐",
    "AFT":                         "💸",
    "Bill Payments":               "🧾",
    "Central 1 Banking Services":  "🏦",
    "Clearing and Deposits":       "📥",
    "Currency":                    "💱",
    "Data Hub":                    "📊",
    "Electronic Transactions":     "⚡",
}


# ── Data loading ──────────────────────────────────────────────────────────────

def load_pages() -> list[dict]:
    pages = []
    for f in sorted(PAGES_DIR.glob("*.json")):
        try:
            p = json.loads(f.read_text())
            if p.get("content_length", 0) >= 100:
                pages.append(p)
        except (json.JSONDecodeError, KeyError):
            pass
    return pages


def get_section(url: str) -> str:
    path = urlparse(url).path
    parts = [p.replace("%20", " ") for p in path.split("/") if p and p != "ps_manual"]
    if not parts:
        return ""
    sec = parts[0]
    return sec[:-5] if sec.endswith(".html") else sec


def get_doc_group(url: str) -> str:
    """Derive a document group from the filename, e.g. 'aft_settlement' from aft_settlement.6.03.html"""
    fname = urlparse(url).path.split("/")[-1]
    # Match base.chapter.section.html
    m = re.match(r"^(.+?)\.\d+\.\d+\.html$", fname)
    if m:
        return m.group(1).replace("_", " ").replace("%20", " ").title()
    # Fall back to filename without extension
    return re.sub(r"\.html$", "", fname).replace("_", " ").replace("%20", " ").title()


def load_page_summary(url: str) -> str:
    """Load a pre-generated page summary if it exists."""
    slug = url.replace("https://", "").replace("/", "_").replace(".", "_")[:80]
    summary_path = SUMMARIES_DIR / "pages" / f"{slug}.md"
    if summary_path.exists():
        text = summary_path.read_text().strip()
        if len(text) > 50 and not text.startswith("*Page appears empty"):
            return text
    return ""


def body_preview(body_text: str, chars: int = 400) -> str:
    """Return a clean preview of body text."""
    text = " ".join(body_text.split())
    return textwrap.shorten(text, width=chars, placeholder="…")


# ── Claude summarization ──────────────────────────────────────────────────────

def _client() -> anthropic.Anthropic:
    key = os.getenv("ANTHROPIC_API_KEY", "")
    if not key:
        raise RuntimeError("ANTHROPIC_API_KEY not set in .env")
    return anthropic.Anthropic(api_key=key)


ARCHITECT_CONTEXT = (
    "You are briefing a Solutions Architect joining the Payment Solutions team at Central 1 Credit Union. "
    "Be precise, technical, and focused on architecture-relevant information: data flows, "
    "integration points, key business rules, and design constraints."
)


def summarize_section(client: anthropic.Anthropic, section: str, pages: list[dict]) -> str:
    # Build a condensed digest of the section's pages
    digest_parts = []
    for p in pages[:40]:  # cap to avoid token overrun
        title = p.get("title", "")
        preview = body_preview(p.get("body_text", ""), 300)
        if preview:
            digest_parts.append(f"**{title}**\n{preview}")
    digest = "\n\n".join(digest_parts)

    prompt = f"""{ARCHITECT_CONTEXT}

Section: **{section}**
Number of pages: {len(pages)}

Below is a digest of the pages in this section:

{digest[:14000]}

Write a section overview (max 450 words) for a Solutions Architect. Use these headings:

## Purpose
What capability or business domain this section covers (2-3 sentences).

## Key Concepts
The 4-6 most important entities, processes, or rules an architect must understand.

## How It Works
A high-level description of the main flow or process (use numbered steps if sequential).

## Integration Points
What systems, APIs, or other PS sections this connects to.

## Architect Notes
Non-obvious constraints, compliance requirements, or design gotchas."""

    msg = client.messages.create(
        model=MODEL,
        max_tokens=900,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def summarize_doc_group(client: anthropic.Anthropic, group_name: str, pages: list[dict]) -> str:
    digest = "\n\n".join(
        f"**{p.get('title', '')}**\n{body_preview(p.get('body_text',''), 250)}"
        for p in pages
    )
    prompt = f"""{ARCHITECT_CONTEXT}

Document group: **{group_name}** ({len(pages)} pages)

{digest[:8000]}

Write a concise summary (max 200 words) covering:
- What this document group is about
- Key steps, rules, or data involved
- Anything an architect needs to know before designing enhancements"""

    msg = client.messages.create(
        model=MODEL,
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def summarize_master(client: anthropic.Anthropic, section_summaries: dict[str, str]) -> str:
    sections_text = "\n\n---\n\n".join(
        f"## {sec}\n{summary}" for sec, summary in section_summaries.items()
    )
    prompt = f"""{ARCHITECT_CONTEXT}

Below are summaries of all 8 sections of the Payment Solutions documentation portal.

{sections_text[:18000]}

Write a master overview (max 600 words) for a Solutions Architect onboarding to Payment Solutions. Use these headings:

## What is Payment Solutions?
A 3-4 sentence description of what the platform does and who uses it.

## Domain Map
A brief description of each of the 8 sections (1-2 lines each).

## Core End-to-End Flows
The 3-5 most important flows an architect must understand (e.g. AFT settlement, EFT processing, bill payment).

## Platform-Wide Integration Points
External systems, shared services, and standards that cut across sections.

## Architect Priorities
The top 3-4 things to understand first when joining an enhancement project."""

    msg = client.messages.create(
        model=MODEL,
        max_tokens=1200,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


# ── HTML generation ───────────────────────────────────────────────────────────

CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
       background: #f8fafc; color: #1e293b; line-height: 1.6; }
a { color: #2563eb; text-decoration: none; }
a:hover { text-decoration: underline; }
.topbar { background: #0f172a; color: #e2e8f0; padding: 12px 24px;
          display: flex; align-items: center; gap: 12px; font-size: 14px; }
.topbar a { color: #93c5fd; }
.topbar .sep { color: #475569; }
.container { max-width: 1000px; margin: 0 auto; padding: 32px 24px; }
h1 { font-size: 2rem; font-weight: 700; margin-bottom: 8px; }
h2 { font-size: 1.4rem; font-weight: 600; margin: 28px 0 12px; color: #0f172a; }
h3 { font-size: 1.1rem; font-weight: 600; margin: 20px 0 8px; color: #334155; }
p { margin-bottom: 12px; color: #334155; }
.subtitle { color: #64748b; font-size: 1.05rem; margin-bottom: 32px; }
.section-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
                gap: 16px; margin-top: 24px; }
.section-card { background: white; border-radius: 10px; padding: 20px 22px;
                border: 1px solid #e2e8f0; border-left: 5px solid var(--accent);
                transition: box-shadow .15s; }
.section-card:hover { box-shadow: 0 4px 16px rgba(0,0,0,.08); }
.section-card .icon { font-size: 1.6rem; margin-bottom: 8px; }
.section-card h3 { color: var(--accent); margin: 0 0 6px; font-size: 1rem; }
.section-card .count { font-size: .8rem; color: #94a3b8; margin-bottom: 8px; }
.section-card p { font-size: .875rem; color: #475569; margin: 0; }
.page-list { margin-top: 16px; }
.page-item { background: white; border: 1px solid #e2e8f0; border-radius: 8px;
             padding: 14px 18px; margin-bottom: 10px; display: flex;
             justify-content: space-between; align-items: flex-start; gap: 12px; }
.page-item:hover { border-color: #93c5fd; }
.page-item .page-title { font-weight: 600; font-size: .95rem; color: #1e293b; }
.page-item .page-title a { color: inherit; }
.page-item .page-meta { font-size: .78rem; color: #94a3b8; white-space: nowrap; }
.page-item .page-preview { font-size: .82rem; color: #64748b; margin-top: 4px; }
.group-card { background: white; border: 1px solid #e2e8f0; border-radius: 10px;
              padding: 18px 20px; margin-bottom: 14px; border-top: 4px solid var(--accent); }
.group-card h3 { color: var(--accent); margin-bottom: 6px; }
.group-card .group-count { font-size: .8rem; color: #94a3b8; margin-bottom: 10px; }
.group-card p { font-size: .875rem; color: #475569; margin-bottom: 10px; }
.summary-box { background: white; border: 1px solid #e2e8f0; border-radius: 10px;
               padding: 24px 28px; margin: 24px 0; }
.summary-box h2:first-child { margin-top: 0; }
.full-content { background: white; border: 1px solid #e2e8f0; border-radius: 10px;
                padding: 24px 28px; margin: 24px 0; white-space: pre-wrap;
                font-size: .875rem; color: #334155; line-height: 1.7; }
.badge { display: inline-block; font-size: .72rem; padding: 2px 8px; border-radius: 99px;
         background: var(--accent); color: white; font-weight: 600; margin-left: 6px; }
.back-btn { display: inline-block; margin-bottom: 20px; padding: 7px 16px;
            background: white; border: 1px solid #e2e8f0; border-radius: 6px;
            font-size: .875rem; color: #334155; }
.back-btn:hover { background: #f1f5f9; text-decoration: none; }
.ext-link { font-size: .78rem; color: #94a3b8; }
.md-content h2 { font-size: 1.1rem; margin: 20px 0 8px; }
.md-content h3 { font-size: 1rem; margin: 16px 0 6px; }
.md-content ul { margin: 8px 0 12px 20px; }
.md-content li { margin-bottom: 4px; font-size: .9rem; color: #334155; }
.md-content p { font-size: .9rem; }
.md-content strong { color: #0f172a; }
footer { margin-top: 48px; padding: 20px 0; border-top: 1px solid #e2e8f0;
         font-size: .8rem; color: #94a3b8; text-align: center; }
"""


def _md_to_html(md: str) -> str:
    """Minimal markdown → HTML (headings, bold, bullets, paragraphs)."""
    lines, out, in_ul = md.strip().split("\n"), [], False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            if in_ul: out.append("</ul>"); in_ul = False
            out.append(f"<h2>{stripped[3:]}</h2>")
        elif stripped.startswith("### "):
            if in_ul: out.append("</ul>"); in_ul = False
            out.append(f"<h3>{stripped[4:]}</h3>")
        elif stripped.startswith(("- ", "* ", "• ")):
            if not in_ul: out.append("<ul>"); in_ul = True
            content = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", stripped[2:])
            out.append(f"<li>{content}</li>")
        elif stripped:
            if in_ul: out.append("</ul>"); in_ul = False
            content = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", stripped)
            out.append(f"<p>{content}</p>")
        else:
            if in_ul: out.append("</ul>"); in_ul = False
    if in_ul: out.append("</ul>")
    return "\n".join(out)


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def _html_page(
    title: str,
    body: str,
    breadcrumbs: list[tuple[str, str]],  # [(label, href), ...]
    accent: str = "#2563eb",
    depth: int = 0,
) -> str:
    root = "../" * depth
    crumbs_html = " <span class='sep'>›</span> ".join(
        f"<a href='{root}{href}'>{label}</a>" if href else f"<span>{label}</span>"
        for label, href in breadcrumbs
    )
    css_link = f'<link rel="stylesheet" href="{root}assets/style.css">'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — PS Manual</title>
  {css_link}
  <style>:root {{ --accent: {accent}; }}</style>
</head>
<body>
  <div class="topbar">
    <span>📚 PS Manual</span>
    <span class="sep">›</span>
    {crumbs_html}
  </div>
  <div class="container">
    {body}
    <footer>Payment Solutions Documentation · Central 1 Credit Union</footer>
  </div>
</body>
</html>"""


# ── Site builders ─────────────────────────────────────────────────────────────

def build_page_html(page: dict, section: str, doc_group: str, summary: str, depth: int) -> str:
    accent = SECTION_COLORS.get(section, "#2563eb")
    title = page.get("title", "Untitled")
    url = page.get("url", "")

    if summary:
        content_html = f'<div class="summary-box md-content">{_md_to_html(summary)}</div>'
    else:
        preview = body_preview(page.get("body_text", ""), 1200)
        content_html = f'<div class="full-content">{preview}</div>'

    back_steps = "../" * 1
    body = f"""
    <a href="{back_steps}index.html" class="back-btn">← Back to {doc_group}</a>
    <h1>{title}</h1>
    <p class="subtitle">{section} › {doc_group}</p>
    {"<p class='ext-link'><a href='" + url + "' target='_blank'>↗ View in PS Manual</a></p>" if url else ""}
    {content_html}
"""
    crumbs = [
        ("index.html", "index.html"),
        (section, f"{_slug(section)}/index.html"),
        (doc_group, f"{_slug(section)}/{_slug(doc_group)}/index.html"),
        (title, ""),
    ]
    return _html_page(title, body, crumbs, accent, depth)


def build_group_html(
    section: str,
    doc_group: str,
    group_summary: str,
    pages: list[dict],
    existing_summaries: dict[str, str],
    depth: int,
) -> str:
    accent = SECTION_COLORS.get(section, "#2563eb")

    pages_html_parts = []
    for page in sorted(pages, key=lambda p: p.get("url", "")):
        title = page.get("title", "Untitled")
        page_slug = _slug(title) or _slug(page["url"].split("/")[-1])
        summary = existing_summaries.get(page["url"], "")
        if summary:
            lines = [l for l in summary.split("\n") if l.strip() and not l.startswith("#")]
            preview_text = " ".join(lines[:2])[:200]
        else:
            preview_text = body_preview(page.get("body_text", ""), 180)

        pages_html_parts.append(f"""
        <div class="page-item">
          <div>
            <div class="page-title"><a href="{page_slug}.html">{title}</a></div>
            <div class="page-preview">{preview_text}</div>
          </div>
          <span class="page-meta"><a href="{page['url']}" target="_blank" class="ext-link">↗ portal</a></span>
        </div>""")

    summary_html = f'<div class="summary-box md-content">{_md_to_html(group_summary)}</div>' if group_summary else ""

    body = f"""
    <a href="../index.html" class="back-btn">← Back to {section}</a>
    <h1>{SECTION_ICONS.get(section, "")} {doc_group}</h1>
    <p class="subtitle">{section} › {doc_group} <span class="badge" style="background:{accent}">{len(pages)} pages</span></p>
    {summary_html}
    <h2>Pages in this group</h2>
    <div class="page-list">{''.join(pages_html_parts)}</div>
"""
    crumbs = [
        ("index.html", "index.html"),
        (section, f"{_slug(section)}/index.html"),
        (doc_group, ""),
    ]
    return _html_page(doc_group, body, crumbs, accent, depth)


def build_section_html(
    section: str,
    section_summary: str,
    groups: dict[str, list[dict]],
    group_summaries: dict[str, str],
    depth: int,
) -> str:
    accent = SECTION_COLORS.get(section, "#2563eb")
    icon = SECTION_ICONS.get(section, "")
    total = sum(len(v) for v in groups.values())

    if len(groups) == 1:
        # Single group = flat page list (no sub-group level)
        only_group = next(iter(groups.values()))
        pages_html = []
        for page in sorted(only_group, key=lambda p: p.get("url", "")):
            title = page.get("title", "Untitled")
            page_slug = _slug(title) or _slug(page["url"].split("/")[-1])
            preview = body_preview(page.get("body_text", ""), 180)
            pages_html.append(f"""
            <div class="page-item">
              <div>
                <div class="page-title"><a href="{_slug(next(iter(groups)))}/{page_slug}.html">{title}</a></div>
                <div class="page-preview">{preview}</div>
              </div>
              <span class="page-meta"><a href="{page['url']}" target="_blank" class="ext-link">↗ portal</a></span>
            </div>""")
        groups_html = f'<div class="page-list">{"".join(pages_html)}</div>'
    else:
        group_cards = []
        for group_name, group_pages in sorted(groups.items(), key=lambda x: x[0]):
            g_summary = group_summaries.get(group_name, "")
            g_preview = textwrap.shorten(g_summary.replace("#", "").replace("*", ""), 220, placeholder="…") if g_summary else ""
            g_slug = _slug(group_name)
            group_cards.append(f"""
            <div class="group-card">
              <h3><a href="{g_slug}/index.html">{group_name}</a></h3>
              <div class="group-count">{len(group_pages)} pages</div>
              {"<p>" + g_preview + "</p>" if g_preview else ""}
              <a href="{g_slug}/index.html">View pages →</a>
            </div>""")
        groups_html = "".join(group_cards)

    summary_html = f'<div class="summary-box md-content">{_md_to_html(section_summary)}</div>' if section_summary else ""

    body = f"""
    <a href="../index.html" class="back-btn">← Back to overview</a>
    <h1>{icon} {section}</h1>
    <p class="subtitle"><span class="badge" style="background:{accent}">{total} pages</span></p>
    {summary_html}
    <h2>{"Document Groups" if len(groups) > 1 else "Pages"}</h2>
    {groups_html}
"""
    crumbs = [("index.html", "index.html"), (section, "")]
    return _html_page(section, body, crumbs, accent, depth)


def build_index_html(master_summary: str, section_data: dict) -> str:
    cards = []
    for section in MAIN_SECTIONS:
        info = section_data.get(section, {})
        count = info.get("count", 0)
        accent = SECTION_COLORS.get(section, "#2563eb")
        icon = SECTION_ICONS.get(section, "")
        teaser = textwrap.shorten(
            info.get("summary", "").replace("#", "").replace("*", ""),
            width=160, placeholder="…"
        )
        slug = _slug(section)
        cards.append(f"""
        <div class="section-card" style="--accent:{accent}">
          <div class="icon">{icon}</div>
          <h3><a href="{slug}/index.html">{section}</a></h3>
          <div class="count">{count} pages</div>
          <p>{teaser}</p>
        </div>""")

    summary_html = f'<div class="summary-box md-content">{_md_to_html(master_summary)}</div>' if master_summary else ""

    body = f"""
    <h1>Payment Solutions Manual</h1>
    <p class="subtitle">Central 1 Credit Union — Solutions Architect Reference</p>
    {summary_html}
    <h2>Sections</h2>
    <div class="section-grid">{''.join(cards)}</div>
"""
    return _html_page("Payment Solutions Manual", body, [("Overview", "")], depth=0)


# ── Main command ──────────────────────────────────────────────────────────────

@app.command()
def run(
    no_api: bool = typer.Option(False, "--no-api", help="Skip Claude API calls, use body-text previews only"),
    sections_only: list[str] = typer.Option([], "--section", help="Regenerate specific sections only"),
):
    """Build a navigable HTML summary site from crawled PS documentation pages."""
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "assets").mkdir(exist_ok=True)
    (SITE_DIR / "assets" / "style.css").write_text(CSS)

    client = None if no_api else _client()

    pages = load_pages()
    console.print(f"[green]Loaded {len(pages)} pages[/green]")

    # Group pages by section then by doc group
    by_section: dict[str, list[dict]] = defaultdict(list)
    for page in pages:
        sec = get_section(page["url"])
        if sec in MAIN_SECTIONS:
            by_section[sec].append(page)

    # Load all existing page summaries into a lookup {url: summary_text}
    existing_summaries: dict[str, str] = {}
    for page in pages:
        s = load_page_summary(page["url"])
        if s:
            existing_summaries[page["url"]] = s

    console.print(f"[dim]Using {len(existing_summaries)} existing page summaries[/dim]")

    target_sections = [s for s in MAIN_SECTIONS if not sections_only or s in sections_only]
    section_summaries: dict[str, str] = {}
    section_data: dict[str, dict] = {}

    with Progress(SpinnerColumn(), TextColumn("{task.description}"), console=console) as progress:
        for section in target_sections:
            sec_pages = by_section.get(section, [])
            if not sec_pages:
                continue

            progress.add_task(f"[cyan]Building: {section}[/cyan]")
            sec_slug = _slug(section)
            sec_dir = SITE_DIR / sec_slug
            sec_dir.mkdir(exist_ok=True)

            # Group pages by doc group
            groups: dict[str, list[dict]] = defaultdict(list)
            for page in sec_pages:
                groups[get_doc_group(page["url"])].append(page)

            # Generate group summaries
            group_summaries: dict[str, str] = {}
            for group_name, group_pages in groups.items():
                if client and len(groups) > 1:
                    try:
                        group_summaries[group_name] = summarize_doc_group(client, group_name, group_pages)
                    except Exception as e:
                        console.print(f"[yellow]  Group summary failed ({group_name}): {e}[/yellow]")
                        group_summaries[group_name] = body_preview(group_pages[0].get("body_text", ""), 300)
                else:
                    group_summaries[group_name] = body_preview(group_pages[0].get("body_text", ""), 300) if group_pages else ""

                # Build per-group subdir and page files
                g_slug = _slug(group_name)
                g_dir = sec_dir / g_slug
                g_dir.mkdir(exist_ok=True)

                # Write group index
                group_html = build_group_html(
                    section, group_name, group_summaries[group_name],
                    group_pages, existing_summaries, depth=2
                )
                (g_dir / "index.html").write_text(group_html, encoding="utf-8")

                # Write individual page files
                for page in group_pages:
                    title = page.get("title", "Untitled")
                    page_slug = _slug(title) or _slug(page["url"].split("/")[-1])
                    summary = existing_summaries.get(page["url"], "")
                    page_html = build_page_html(page, section, group_name, summary, depth=2)
                    (g_dir / f"{page_slug}.html").write_text(page_html, encoding="utf-8")

            # Generate section summary
            if client:
                try:
                    section_summaries[section] = summarize_section(client, section, sec_pages)
                except Exception as e:
                    console.print(f"[yellow]  Section summary failed ({section}): {e}[/yellow]")
                    section_summaries[section] = f"Section covering {len(sec_pages)} pages related to {section}."
            else:
                section_summaries[section] = f"Section covering {len(sec_pages)} pages related to {section}."

            # Write section index
            section_html = build_section_html(
                section, section_summaries[section], dict(groups), group_summaries, depth=1
            )
            (sec_dir / "index.html").write_text(section_html, encoding="utf-8")

            section_data[section] = {
                "count": len(sec_pages),
                "summary": section_summaries[section],
            }
            console.print(f"  [green]✓[/green] {section} ({len(sec_pages)} pages, {len(groups)} groups)")

    # Generate master overview
    master_summary = ""
    if client and section_summaries:
        console.print("[cyan]Generating master overview...[/cyan]")
        try:
            master_summary = summarize_master(client, section_summaries)
        except Exception as e:
            console.print(f"[yellow]Master summary failed: {e}[/yellow]")

    # Write master index
    index_html = build_index_html(master_summary, section_data)
    (SITE_DIR / "index.html").write_text(index_html, encoding="utf-8")

    total_files = sum(1 for _ in SITE_DIR.rglob("*.html"))
    console.print(f"\n[bold green]✓ Site built: {SITE_DIR}/[/bold green]")
    console.print(f"  {total_files} HTML files generated")
    console.print(f"\nOpen in browser:")
    console.print(f"  open {SITE_DIR.resolve()}/index.html")


if __name__ == "__main__":
    app()
