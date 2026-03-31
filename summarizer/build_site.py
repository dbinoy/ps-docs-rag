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


def load_section_summary(section: str) -> str:
    """Load a pre-generated section summary if it exists."""
    path = SUMMARIES_DIR / "sections" / f"{section}.md"
    if path.exists():
        text = path.read_text().strip()
        if len(text) > 50:
            return text
    return ""


def load_master_summary() -> str:
    """Load the pre-generated master summary if it exists."""
    path = SUMMARIES_DIR / "master_summary.md"
    if path.exists():
        text = path.read_text().strip()
        if len(text) > 50:
            return text
    return ""


def _grp_slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def load_group_summary(section: str, group_name: str) -> str:
    """Load a cached group summary from disk if it exists."""
    path = SUMMARIES_DIR / "groups" / _grp_slug(section) / f"{_grp_slug(group_name)}.md"
    if path.exists():
        text = path.read_text().strip()
        if len(text) > 30:
            return text
    return ""


def save_group_summary(section: str, group_name: str, text: str) -> None:
    """Persist a group summary to disk for reuse on future builds."""
    d = SUMMARIES_DIR / "groups" / _grp_slug(section)
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{_grp_slug(group_name)}.md").write_text(text, encoding="utf-8")


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


QA_JS = r"""
(function () {
  'use strict';

  /* ── Inject widget CSS ─────────────────────────────────── */
  var style = document.createElement('style');
  style.textContent = [
    '#qa-fab{position:fixed;bottom:24px;right:24px;z-index:9998;width:52px;height:52px;',
    'border-radius:50%;background:#2563eb;color:#fff;border:none;cursor:pointer;',
    'font-size:22px;box-shadow:0 4px 14px rgba(0,0,0,.25);display:flex;',
    'align-items:center;justify-content:center;transition:background .2s,transform .15s}',
    '#qa-fab:hover{background:#1d4ed8;transform:scale(1.08)}',
    'body{transition:margin-right .25s cubic-bezier(.4,0,.2,1)}',
    '#qa-resize{position:absolute;left:0;top:0;bottom:0;width:6px;cursor:col-resize;z-index:1}',
    '#qa-resize:hover{background:rgba(37,99,235,.15)}',
    '#qa-panel{position:fixed;top:0;right:0;bottom:0;width:380px;max-width:100vw;',
    'background:#fff;border-left:1px solid #e2e8f0;box-shadow:-4px 0 24px rgba(0,0,0,.12);',
    'display:flex;flex-direction:column;z-index:9999;',
    'transform:translateX(100%);transition:transform .25s cubic-bezier(.4,0,.2,1)}',
    '#qa-panel.qa-open{transform:translateX(0)}',
    '#qa-header{background:#0f172a;color:#e2e8f0;padding:14px 18px;display:flex;',
    'align-items:center;justify-content:space-between;font-size:14px;font-weight:600;flex-shrink:0}',
    '#qa-close,#qa-clear{background:none;border:none;color:#94a3b8;font-size:18px;cursor:pointer;',
    'line-height:1;padding:2px 6px;border-radius:4px}',
    '#qa-close:hover,#qa-clear:hover{color:#e2e8f0;background:rgba(255,255,255,.1)}',
    '#qa-controls{padding:10px 14px;border-bottom:1px solid #e2e8f0;flex-shrink:0;background:#f8fafc;',
    'display:flex;align-items:center;gap:12px;font-size:12px;color:#64748b;flex-wrap:wrap}',
    '#qa-provider,#qa-topk{font-size:12px;padding:3px 8px;border-radius:4px;border:1px solid #cbd5e1;',
    'background:#fff;color:#334155;cursor:pointer}',
    '#qa-messages{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:12px}',
    '.qa-msg{border-radius:8px;padding:10px 13px;font-size:13.5px;line-height:1.55;max-width:95%}',
    '.qa-msg-user{background:#2563eb;color:#fff;align-self:flex-end;border-bottom-right-radius:2px}',
    '.qa-msg-bot{background:#f1f5f9;color:#1e293b;align-self:flex-start;',
    'border-bottom-left-radius:2px}',
    '.qa-msg-bot h2{font-size:14px;font-weight:700;margin:10px 0 4px}',
    '.qa-msg-bot h3{font-size:13px;font-weight:700;margin:8px 0 3px}',
    '.qa-msg-bot p{margin:4px 0}',
    '.qa-msg-bot ul,.qa-msg-bot ol{margin:4px 0;padding-left:18px}',
    '.qa-msg-bot li{margin:2px 0}',
    '.qa-msg-bot code{background:#e2e8f0;border-radius:3px;padding:1px 4px;font-size:12px;font-family:monospace}',
    '.qa-msg-bot pre{background:#1e293b;color:#e2e8f0;border-radius:6px;padding:10px;',
    'overflow-x:auto;font-size:12px;margin:6px 0}',
    '.qa-msg-bot pre code{background:none;padding:0;color:inherit}',
    '.qa-msg-bot strong{font-weight:700}',
    '.qa-msg-bot em{font-style:italic}',
    '.qa-msg-bot a{color:#2563eb;text-decoration:none}',
    '.qa-msg-bot a:hover{text-decoration:underline}',
    '.qa-msg-err{background:#fef2f2;color:#991b1b;align-self:flex-start;border:1px solid #fecaca}',
    '.qa-sources{font-size:11.5px;color:#64748b;margin-top:8px;padding-top:8px;',
    'border-top:1px solid #e2e8f0}',
    '.qa-sources a{color:#2563eb;text-decoration:none}',
    '.qa-sources a:hover{text-decoration:underline}',
    '.qa-spin-wrap{display:flex;align-items:center;gap:8px;font-size:13px;color:#64748b;padding:8px 4px}',
    '.qa-spinner{width:16px;height:16px;border-radius:50%;border:2px solid #e2e8f0;',
    'border-top-color:#2563eb;animation:qa-spin .7s linear infinite;flex-shrink:0}',
    '@keyframes qa-spin{to{transform:rotate(360deg)}}',
    '#qa-empty{color:#94a3b8;font-size:13px;text-align:center;margin-top:40px;',
    'line-height:1.7;padding:0 16px}',
    '#qa-input-row{padding:12px 14px;border-top:1px solid #e2e8f0;',
    'display:flex;gap:8px;flex-shrink:0;background:#fff}',
    '#qa-input{flex:1;font-size:13.5px;padding:8px 11px;border:1px solid #cbd5e1;',
    'border-radius:6px;outline:none;resize:none;font-family:inherit;line-height:1.4;',
    'max-height:100px;overflow-y:auto}',
    '#qa-input:focus{border-color:#2563eb;box-shadow:0 0 0 2px rgba(37,99,235,.15)}',
    '#qa-send{background:#2563eb;color:#fff;border:none;border-radius:6px;',
    'padding:0 14px;cursor:pointer;font-size:13px;font-weight:600;flex-shrink:0;',
    'transition:background .15s}',
    '#qa-send:hover:not(:disabled){background:#1d4ed8}',
    '#qa-send:disabled{background:#93c5fd;cursor:not-allowed}',
    '#qa-send.qa-cancelling{background:#dc2626!important}',
    '#qa-send.qa-cancelling:hover:not(:disabled){background:#b91c1c!important}'
  ].join('');
  document.head.appendChild(style);

  /* ── Build DOM ─────────────────────────────────────────── */
  var fab = document.createElement('button');
  fab.id = 'qa-fab'; fab.title = 'Ask a question'; fab.textContent = '\uD83D\uDCAC';

  var panel = document.createElement('div');
  panel.id = 'qa-panel';
  panel.innerHTML =
    '<div id="qa-resize"></div>' +
    '<div id="qa-header">' +
      '<span>\uD83D\uDCAC\u2002PS Docs Q&amp;A</span>' +
      '<div style="display:flex;gap:4px">' +
        '<button id="qa-clear" title="Clear chat history">\uD83D\uDDD1</button>' +
        '<button id="qa-close" title="Close">\u2715</button>' +
      '</div>' +
    '</div>' +
    '<div id="qa-controls">' +
      '<label for="qa-provider">Provider:</label>' +
      '<select id="qa-provider">' +
        '<option value="anthropic">Anthropic (Claude)</option>' +
        '<option value="github">GitHub (GPT-4o)</option>' +
      '</select>' +
      '<label for="qa-topk" title="Number of document chunks passed to the LLM">Chunks:</label>' +
      '<select id="qa-topk">' +
        '<option value="4">4</option>' +
        '<option value="6">6</option>' +
        '<option value="8" selected>8</option>' +
        '<option value="10">10</option>' +
        '<option value="12">12</option>' +
        '<option value="16">16</option>' +
      '</select>' +
    '</div>' +
    '<div id="qa-messages">' +
      '<div id="qa-empty">Ask any question about the<br>Payment Solutions documentation.</div>' +
    '</div>' +
    '<div id="qa-input-row">' +
      '<textarea id="qa-input" placeholder="Ask a question\u2026" rows="1"></textarea>' +
      '<button id="qa-send">Send</button>' +
    '</div>';

  document.body.appendChild(fab);
  document.body.appendChild(panel);

  /* ── Refs & state ──────────────────────────────────────── */
  var msgs     = panel.querySelector('#qa-messages');
  var inputEl  = panel.querySelector('#qa-input');
  var sendBtn  = panel.querySelector('#qa-send');
  var closeBtn  = panel.querySelector('#qa-close');
  var clearBtn  = panel.querySelector('#qa-clear');
  var resizeEl  = panel.querySelector('#qa-resize');
  var provEl    = panel.querySelector('#qa-provider');
  var topkEl   = panel.querySelector('#qa-topk');
  var emptyEl  = panel.querySelector('#qa-empty');
  var loading    = false;
  var DEFAULT_W  = 380;
  var _history   = [];   // [{cls, html, sourcesHtml}] — persisted across navigations
  var _abortCtrl = null;

  /* ── Helpers ───────────────────────────────────────────── */
  function open() {
    var w = parseInt(localStorage.getItem('qa_width'), 10) || DEFAULT_W;
    panel.style.width = w + 'px';
    panel.classList.add('qa-open');
    document.body.style.marginRight = w + 'px';
    fab.style.display = 'none';
    localStorage.setItem('qa_open', '1');
    inputEl.focus();
  }
  function close() {
    panel.classList.remove('qa-open');
    document.body.style.marginRight = '';
    fab.style.display = '';
    localStorage.removeItem('qa_open');
  }

  function setLoading(on) {
    loading = on; inputEl.disabled = on;
    if (on) {
      sendBtn.textContent = 'Cancel';
      sendBtn.classList.add('qa-cancelling');
      sendBtn.disabled = false;
    } else {
      sendBtn.textContent = 'Send';
      sendBtn.classList.remove('qa-cancelling');
      sendBtn.disabled = false;
    }
    var ind = document.getElementById('qa-loading');
    if (on && !ind) {
      var d = document.createElement('div');
      d.id = 'qa-loading'; d.className = 'qa-spin-wrap';
      d.innerHTML = '<div class="qa-spinner"></div><span>Searching\u2026</span>';
      msgs.appendChild(d); msgs.scrollTop = msgs.scrollHeight;
    } else if (!on && ind) { ind.remove(); }
  }

  /* ── Persistence helpers ───────────────────────────────── */
  function escapeHtml(s) {
    return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  }
  function saveHistory() {
    if (_history.length > 100) _history = _history.slice(-100);
    try { localStorage.setItem('qa_history', JSON.stringify(_history)); } catch(e) {}
  }
  function loadHistory() {
    try { return JSON.parse(localStorage.getItem('qa_history') || '[]'); } catch(e) { return []; }
  }
  function savePending(q, prov, topk) {
    try { localStorage.setItem('qa_pending', JSON.stringify({q:q, prov:prov, topk:topk, t:Date.now()})); } catch(e) {}
  }
  function clearPending() { localStorage.removeItem('qa_pending'); }
  function loadPending() {
    try {
      var p = JSON.parse(localStorage.getItem('qa_pending') || 'null');
      if (p && (Date.now() - p.t) < 90000) return p;
    } catch(e) {}
    clearPending(); return null;
  }

  /* ── Minimal markdown → HTML ───────────────────────────── */
  function mdToHtml(md) {
    var lines = md.split('\n'), out = [], inPre = false, inUl = false, inOl = false;
    function closeLists() {
      if (inUl) { out.push('</ul>'); inUl = false; }
      if (inOl) { out.push('</ol>'); inOl = false; }
    }
    function inline(s) {
      // code spans first to avoid processing their contents
      s = s.replace(/`([^`]+)`/g, '<code>$1</code>');
      s = s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
      s = s.replace(/\*(.+?)\*/g, '<em>$1</em>');
      s = s.replace(/_(.+?)_/g, '<em>$1</em>');
      s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>');
      return s;
    }
    for (var i = 0; i < lines.length; i++) {
      var l = lines[i];
      if (/^```/.test(l)) {
        if (!inPre) { closeLists(); out.push('<pre><code>'); inPre = true; }
        else { out.push('</code></pre>'); inPre = false; }
        continue;
      }
      if (inPre) { out.push(l.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')); continue; }
      if (/^## /.test(l))  { closeLists(); out.push('<h2>' + inline(l.slice(3)) + '</h2>'); continue; }
      if (/^### /.test(l)) { closeLists(); out.push('<h3>' + inline(l.slice(4)) + '</h3>'); continue; }
      if (/^#### /.test(l)){ closeLists(); out.push('<h4>' + inline(l.slice(5)) + '</h4>'); continue; }
      if (/^[-*] /.test(l)) {
        if (inOl) { out.push('</ol>'); inOl = false; }
        if (!inUl) { out.push('<ul>'); inUl = true; }
        out.push('<li>' + inline(l.slice(2)) + '</li>'); continue;
      }
      if (/^\d+\. /.test(l)) {
        if (inUl) { out.push('</ul>'); inUl = false; }
        if (!inOl) { out.push('<ol>'); inOl = true; }
        out.push('<li>' + inline(l.replace(/^\d+\. /, '')) + '</li>'); continue;
      }
      if (l.trim() === '') { closeLists(); out.push(''); continue; }
      closeLists();
      out.push('<p>' + inline(l) + '</p>');
    }
    if (inPre) out.push('</code></pre>');
    closeLists();
    return out.join('\n');
  }

  function _renderMsg(cls, html, sourcesHtml) {
    if (emptyEl) { emptyEl.style.display = 'none'; }
    var d = document.createElement('div');
    d.className = 'qa-msg ' + cls;
    d.innerHTML = html;
    if (sourcesHtml) {
      var s = document.createElement('div');
      s.className = 'qa-sources'; s.innerHTML = sourcesHtml; d.appendChild(s);
    }
    msgs.appendChild(d); msgs.scrollTop = msgs.scrollHeight;
  }
  function addMsg(text, cls, sourcesHtml) {
    var html = cls === 'qa-msg-bot' ? mdToHtml(text) : escapeHtml(text);
    _history.push({cls: cls, html: html, sourcesHtml: sourcesHtml || ''});
    saveHistory();
    _renderMsg(cls, html, sourcesHtml);
  }

  function sources(pages) {
    if (!pages || !pages.length) return '';
    var links = pages.filter(function(p){return p.url||p.title;}).map(function(p){
      var label = p.title || p.url;
      var pct   = p.relevance ? ' (' + Math.round(p.relevance * 100) + '%)' : '';
      return '<a href="' + (p.url||'#') + '" target="_blank">' + label + '</a>' + pct;
    });
    return links.length ? '<strong>Sources:</strong> ' + links.join(' \u00B7 ') : '';
  }

  /* ── Send & cancel ─────────────────────────────────────── */
  function _doFetch(q, prov, topk) {
    savePending(q, prov, topk);
    setLoading(true);
    _abortCtrl = typeof AbortController !== 'undefined' ? new AbortController() : null;
    var opts = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({question: q, provider: prov, top_k: topk})
    };
    if (_abortCtrl) opts.signal = _abortCtrl.signal;
    fetch('/api/ask', opts)
    .then(function(r) {
      if (!r.ok) return r.json().then(function(b){ throw new Error(b.detail||('Error '+r.status)); });
      return r.json();
    })
    .then(function(d) {
      clearPending(); setLoading(false);
      addMsg(d.answer, 'qa-msg-bot', sources(d.matched_pages));
    })
    .catch(function(e) {
      if (e.name === 'AbortError') { clearPending(); setLoading(false); return; }
      clearPending(); setLoading(false);
      addMsg('Error: ' + e.message, 'qa-msg-err', null);
    });
  }
  function send() {
    var q = inputEl.value.trim();
    if (!q || loading) return;
    addMsg(q, 'qa-msg-user', null);
    inputEl.value = ''; inputEl.style.height = '';
    _doFetch(q, provEl.value, Math.max(1, Math.min(20, parseInt(topkEl.value, 10) || 8)));
  }
  function cancel() {
    if (_abortCtrl) { _abortCtrl.abort(); _abortCtrl = null; }
    clearPending(); setLoading(false);
  }
  function clearHistory() {
    if (loading) cancel();
    _history = [];
    try { localStorage.removeItem('qa_history'); } catch(e) {}
    while (msgs.firstChild) msgs.removeChild(msgs.firstChild);
    var emp = document.createElement('div');
    emp.id = 'qa-empty';
    emp.innerHTML = 'Ask any question about the<br>Payment Solutions documentation.';
    msgs.appendChild(emp);
    emptyEl = emp;
  }

  /* ── Events ────────────────────────────────────────────── */
  fab.addEventListener('click', open);
  closeBtn.addEventListener('click', close);
  clearBtn.addEventListener('click', clearHistory);
  sendBtn.addEventListener('click', function() { if (loading) cancel(); else send(); });
  document.addEventListener('keydown', function(e){ if (e.key==='Escape') close(); });
  inputEl.addEventListener('keydown', function(e){
    if (e.key==='Enter' && !e.shiftKey) { e.preventDefault(); send(); }
  });
  inputEl.addEventListener('input', function(){
    this.style.height = ''; this.style.height = Math.min(this.scrollHeight, 100) + 'px';
  });

  /* ── Drag-to-resize ────────────────────────────────────── */
  var _drag = false, _dragX = 0, _dragW = 0;
  resizeEl.addEventListener('mousedown', function(e) {
    _drag = true; _dragX = e.clientX; _dragW = panel.offsetWidth;
    document.body.style.userSelect = 'none';
    e.preventDefault();
  });
  document.addEventListener('mousemove', function(e) {
    if (!_drag) return;
    var w = Math.max(280, Math.min(Math.round(window.innerWidth * 0.8), _dragW + (_dragX - e.clientX)));
    panel.style.width = w + 'px';
    document.body.style.marginRight = w + 'px';
  });
  document.addEventListener('mouseup', function() {
    if (!_drag) return;
    _drag = false;
    document.body.style.userSelect = '';
    localStorage.setItem('qa_width', panel.offsetWidth);
  });

  /* ── Restore session from previous page ────────────────── */
  (function initSession() {
    var hist = loadHistory();
    if (hist.length) {
      _history = hist;
      hist.forEach(function(item) { _renderMsg(item.cls, item.html, item.sourcesHtml || ''); });
      msgs.scrollTop = msgs.scrollHeight;
    }
    var pending = loadPending();
    if (pending) {
      if (pending.prov && provEl) provEl.value = pending.prov;
      _doFetch(pending.q, pending.prov, pending.topk);
    }
  })();

  if (localStorage.getItem('qa_open') === '1') open();

  /* ── Load default provider from server config ──────────── */
  fetch('/api/config').then(function(r){ return r.json(); }).then(function(c){
    if (c && c.provider) provEl.value = c.provider;
  }).catch(function(){});
}());
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
  <script src="{root}assets/qa.js"></script>
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
    force: bool = typer.Option(False, "--force", "-f", help="Rebuild all pages even if they already exist"),
    sections_only: list[str] = typer.Option([], "--section", help="Regenerate specific sections only"),
):
    """Build a navigable HTML summary site from crawled PS documentation pages."""
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    (SITE_DIR / "assets").mkdir(exist_ok=True)
    (SITE_DIR / "assets" / "style.css").write_text(CSS)
    (SITE_DIR / "assets" / "qa.js").write_text(QA_JS)

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
    skipped_pages = 0

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

            # Generate group summaries (load from disk cache unless --force)
            group_summaries: dict[str, str] = {}
            for group_name, group_pages in groups.items():
                cached = "" if force else load_group_summary(section, group_name)
                if cached:
                    group_summaries[group_name] = cached
                elif client and len(groups) > 1:
                    try:
                        summary = summarize_doc_group(client, group_name, group_pages)
                        group_summaries[group_name] = summary
                        save_group_summary(section, group_name, summary)
                    except Exception as e:
                        console.print(f"[yellow]  Group summary failed ({group_name}): {e}[/yellow]")
                        group_summaries[group_name] = body_preview(group_pages[0].get("body_text", ""), 300)
                else:
                    group_summaries[group_name] = body_preview(group_pages[0].get("body_text", ""), 300) if group_pages else ""

                # Build per-group subdir and page files
                g_slug = _slug(group_name)
                g_dir = sec_dir / g_slug
                g_dir.mkdir(exist_ok=True)

                # Write group index (skip if exists and not forcing)
                group_index = g_dir / "index.html"
                if force or not group_index.exists():
                    group_html = build_group_html(
                        section, group_name, group_summaries[group_name],
                        group_pages, existing_summaries, depth=2
                    )
                    group_index.write_text(group_html, encoding="utf-8")

                # Write individual page files
                for page in group_pages:
                    title = page.get("title", "Untitled")
                    page_slug = _slug(title) or _slug(page["url"].split("/")[-1])
                    page_path = g_dir / f"{page_slug}.html"
                    if not force and page_path.exists():
                        skipped_pages += 1
                        continue
                    summary = existing_summaries.get(page["url"], "")
                    page_html = build_page_html(page, section, group_name, summary, depth=2)
                    page_path.write_text(page_html, encoding="utf-8")

            # Generate section summary (use stored file if available)
            stored_sec = load_section_summary(section)
            if stored_sec:
                section_summaries[section] = stored_sec
            elif client:
                try:
                    section_summaries[section] = summarize_section(client, section, sec_pages)
                except Exception as e:
                    console.print(f"[yellow]  Section summary failed ({section}): {e}[/yellow]")
                    section_summaries[section] = f"Section covering {len(sec_pages)} pages related to {section}."
            else:
                section_summaries[section] = f"Section covering {len(sec_pages)} pages related to {section}."

            # Write section index (skip if exists and not forcing)
            sec_index = sec_dir / "index.html"
            if force or not sec_index.exists():
                section_html = build_section_html(
                    section, section_summaries[section], dict(groups), group_summaries, depth=1
                )
                sec_index.write_text(section_html, encoding="utf-8")

            section_data[section] = {
                "count": len(sec_pages),
                "summary": section_summaries[section],
            }
            console.print(f"  [green]✓[/green] {section} ({len(sec_pages)} pages, {len(groups)} groups)")

    # Generate master overview (use stored file if available)
    master_summary = load_master_summary()
    if not master_summary and client and section_summaries:
        console.print("[cyan]Generating master overview...[/cyan]")
        try:
            master_summary = summarize_master(client, section_summaries)
        except Exception as e:
            console.print(f"[yellow]Master summary failed: {e}[/yellow]")

    # Write master index (skip if exists and not forcing)
    master_index = SITE_DIR / "index.html"
    if force or not master_index.exists():
        index_html = build_index_html(master_summary, section_data)
        master_index.write_text(index_html, encoding="utf-8")

    total_files = sum(1 for _ in SITE_DIR.rglob("*.html"))
    console.print(f"\n[bold green]✓ Site built: {SITE_DIR}/[/bold green]")
    console.print(f"  {total_files} HTML files total" + (f"  ({skipped_pages} page files unchanged, skipped)" if skipped_pages else ""))
    console.print(f"\nOpen in browser:")
    console.print(f"  open {SITE_DIR.resolve()}/index.html")


if __name__ == "__main__":
    app()
