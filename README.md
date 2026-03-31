# PS Docs RAG

Automated pipeline to crawl, summarize, and build a RAG Q&A system over the
Payment Solutions documentation portal at `psmanual.secure.central1.com`.

Built as an onboarding accelerator for a Solutions Architect joining
Payment Solutions enhancement projects at Central 1 Credit Union.

---

## What This Does

```
Portal (ADFS/SSO authenticated via Playwright)
  → Crawler       → 725 pages saved as structured JSON     (output/pages/)
  → Summarizer    → 3-tier markdown summaries              (output/summaries/)
  → HTML Site     → navigable web site with drill-down     (output/site/)
  → Ingest        → ChromaDB vector store                  (output/chroma_db/)
  → Web Server    → FastAPI serving site + /api/ask        (http://localhost:8000)
  → MCP Server    → Claude Code tools: search_docs, ask_docs, get_section_summary
```

**Once the pipeline has run, you can:**
- Browse a navigable HTML site with an in-page Q&A chat widget: `python -m web_server.server`
- Ask Q&A questions from the CLI: `python -m rag.query ask "How does AFT settlement work?"`
- Query documentation mid-conversation in Claude Code via the MCP server

---

## Extraction Quality — Current State

The crawler ran on **31 March 2026** and produced the following results.

### Coverage Summary

| Metric | Value |
|--------|-------|
| Total pages saved | **725** |
| Substantive pages (500+ chars) | **684** (94%) |
| Thin pages (100–500 chars) | 38 |
| Near-empty pages (<100 chars) | 3 |
| Sections discovered | **8 main + Releases + misc** |
| Chapter groups | **42** |
| Linked URLs not saved (missed pages) | **0** |
| Sequential page number gaps | **0** |

### Section Breakdown

| Section | Pages |
|---------|------:|
| Releases (release notes, one per release) | 290 |
| Clearing and Deposits | 123 |
| Electronic Transactions | 89 |
| AFT | 53 |
| Bill Payments | 47 |
| Access and Administration | 40 |
| Central 1 Banking Services | 31 |
| Currency | 28 |
| Data Hub | 8 |
| How to Use this Manual + misc | 5 |

### Coverage Confidence

The portal uses a **JavaScript-rendered left-panel navigation**, so the sidebar
TOC links are absent from raw HTML. Coverage is still complete because:

1. Each section has a static index page (e.g., `Electronic Transactions.html`)
   containing all `<a href>` links to the numbered content pages within it.
2. Zero linked-but-unsaved URLs found after cross-referencing all 725 saved files.
3. All numbered page sequences (e.g., `wires.3.01.html` → `wires.3.06.html`) are
   contiguous — no chapter gaps across all 42 chapter groups.

---

## Setup

### Prerequisites

- Python 3.11 — virtual env already created at `Central1/psend/`
- Anthropic API key

### Activate the virtual environment

```bash
source /Users/binoydas/Documents/Code/Central1/psend/bin/activate
cd /Users/binoydas/Documents/Code/Central1/ps-docs-rag
```

### Configure credentials

```bash
cp .env.template .env
# Edit .env and fill in:
#   ANTHROPIC_API_KEY=sk-ant-...        ← for default provider (claude-sonnet-4-6)
#   GITHUB_TOKEN=ghp_...               ← for --provider github fallback (gpt-4o)
#   Portal credentials are pre-filled in .env.template
```

---

## Running the Pipeline

### Full pipeline (first run)

```bash
# 1. Crawl the portal
python -m crawler.crawl run

# 2. Generate markdown summaries (for RAG ingestion)
python -m summarizer.summarize run

# 3. Build the vector store
python -m rag.ingest run

# 4. Start the web server (builds site automatically, then opens browser)
python -m web_server.server                        # Anthropic provider (default)
python -m web_server.server --provider github      # GPT-4o via GitHub Models

# Alternative: CLI Q&A without the web server
python -m rag.query ask "What is the EFT settlement process?"
python -m rag.query ask "What is the EFT settlement process?" --provider github
```

### Incremental re-run (after portal updates)

```bash
# Crawl only fetches new/missing pages by default
python -m crawler.crawl run

# Summarizer skips pages that already have summaries
python -m summarizer.summarize run --resume

# Re-ingest (upserts — existing chunks are updated, not duplicated)
python -m rag.ingest run

# Restart the server — it rebuilds the site incrementally on startup
python -m web_server.server
```

---

## Component Reference

### Crawler (`crawler/crawl.py` + `crawler/auth.py`)

The portal uses **Central 1's ADFS federated SSO** — `requests`-based Basic or
NTLM auth does not work. The crawler authenticates via a two-step ADFS flow
driven by Playwright:

1. **HRD page** (`sts1.secure.central1.com`): submit plain username → redirects
   to Central 1's own ADFS at `sts3.secure.central1.com`
2. **Forms auth page**: set `loginForm.UserName = extranetqa\psdoperator3`,
   fill password, submit → redirected back to the portal
3. Session cookies are extracted and injected into a `requests.Session` for
   efficient bulk page fetching

```bash
# Incremental crawl (default) — skips pages already in output/pages/
python -m crawler.crawl run

# Force full re-crawl from scratch
python -m crawler.crawl run --fresh

# Test auth + inspect a single URL
python -m crawler.crawl inspect https://psmanual.secure.central1.com/ps_manual/index.html

# Throttle requests (default delay is 0.5s)
python -m crawler.crawl run --delay 1.0
```

**Output per page** (`output/pages/<slug>.json`):
```json
{
  "url": "https://psmanual.secure.central1.com/ps_manual/AFT/aft_settlement.6.01.html",
  "title": "1 Introduction to AFT Settlement",
  "section_path": "AFT",
  "breadcrumb": [],
  "body_text": "...",
  "links": ["..."],
  "content_length": 3241
}
```

**Note on `section_path`:** Pages crawled before 31 March 2026 have
`section_path: "ps_manual > AFT"` (with the portal root prefix). Pages crawled
after the fix have `section_path: "AFT"` (clean). The summarizer and site builder
both handle either format transparently via URL-decoding and prefix-stripping.

**Also produces:** `output/site_map.json` — full hierarchical section tree.

---

### Summarizer (`summarizer/summarize.py`)

Generates markdown summaries used by the RAG pipeline. Uses `claude-haiku-4-5-20251001`.

| Tier | Scope | Output location | Use for |
|------|-------|-----------------|---------|
| Page | Single page | `output/summaries/pages/` | RAG retrieval context |
| Section | One section (e.g., AFT) | `output/summaries/sections/` | RAG + site builder |
| Master | Entire portal | `output/summaries/master_summary.md` | Onboarding overview |

```bash
# Generate all tiers
python -m summarizer.summarize run

# Resume an interrupted run (skips already-generated summaries)
python -m summarizer.summarize run --resume

# Generate only one tier
python -m summarizer.summarize run --tier page
python -m summarizer.summarize run --tier section
python -m summarizer.summarize run --tier master

# Print master summary to terminal
python -m summarizer.summarize show-master
```

**Cost estimate:** ~$5–10 USD for all 725 pages using `claude-haiku-4-5-20251001`.

**Known fix applied:** The `_group_by_section` function previously grouped all
pages under `"ps_manual"` (the URL root segment) instead of by actual section
name. This is now fixed — section summaries are correctly named `AFT.md`,
`Electronic Transactions.md`, etc.

---

### HTML Site Builder (`summarizer/build_site.py`)

Builds a fully navigable, self-contained HTML site for human reading. Uses the
existing page summaries from `output/summaries/pages/` where available, falls
back to body-text previews for pages without summaries. Section and master
summaries are loaded from `output/summaries/` (generated by `summarizer.summarize`)
and are never regenerated unless those files are absent.

**Site structure:**
```
output/site/
├── index.html                          ← PS overview + 8 colour-coded section cards
├── {section}/
│   ├── index.html                      ← section summary + doc-group list
│   └── {doc-group}/
│       ├── index.html                  ← group summary + page list
│       └── {page}.html                 ← individual page with AI summary
└── assets/
    ├── style.css
    └── qa.js                           ← Q&A widget (auto-injected into every page)
```

Every page has:
- **Breadcrumb navigation** (PS Manual › Section › Group › Page)
- **Back button** to the parent level
- **"↗ View in PS Manual"** link to the original portal page
- **💬 Q&A chat widget** (bottom-right floating button — see Web Server section)

```bash
# Incremental build — skips page files that already exist (fast, default)
python -m summarizer.build_site

# Force full rebuild of every page
python -m summarizer.build_site --force

# Skip all Claude API calls (uses stored summaries + body-text previews)
python -m summarizer.build_site --no-api

# Skip API calls AND force full rebuild
python -m summarizer.build_site --no-api --force

# Rebuild a specific section only
python -m summarizer.build_site --section "AFT" --section "Electronic Transactions"
```

**Note on command syntax:** `build_site` is a single-command Typer app —
call it directly without a subcommand (unlike `crawl run` or `summarize run`).

---

### Web Server (`web_server/server.py`)

A FastAPI server that:
1. Runs an incremental `build_site` before starting (so the site is always up-to-date)
2. Serves the static HTML site at `http://localhost:8000`
3. Exposes `POST /api/ask` — the RAG Q&A endpoint used by the in-page widget
4. Opens the browser automatically on startup

```bash
# Start server (incremental site build + open browser)
python -m web_server.server

# Use GitHub Models (GPT-4o) as the default provider
python -m web_server.server --provider github

# Force a full site rebuild before starting
python -m web_server.server --rebuild

# Force rebuild with a custom port
python -m web_server.server --rebuild --port 8080

# Bind to all interfaces (e.g. to access from another machine)
python -m web_server.server --host 0.0.0.0
```

Or via the installed script:
```bash
ps-serve
ps-serve --provider github
ps-serve --rebuild
```

#### Q&A Chat Widget

Every page in the site includes a floating **💬** button (bottom-right corner)
that opens a chat panel backed by the `/api/ask` endpoint.

**Features:**

| Feature | Description |
|---------|-------------|
| **Provider selector** | Switch between Anthropic (Claude) and GitHub (GPT-4o) per query |
| **Chunks dropdown** | Control how many document chunks are sent to the LLM (4 / 6 / 8 / 10 / 12 / 16) |
| **Formatted answers** | Responses rendered as HTML (headings, lists, code blocks, bold/italic) |
| **Source links** | Each answer shows the matched documentation pages with relevance scores |
| **Session persistence** | Chat history survives page navigation — restored automatically on every page |
| **Query recovery** | If you navigate away mid-query, the request is automatically re-issued on the next page |
| **Cancel** | While a query is in-flight the Send button turns red — click to cancel |
| **Clear history** | 🗑 button in the widget header wipes the chat and localStorage history |
| **Resizable panel** | Drag the left border of the panel to resize; width is saved across sessions |
| **Content reflow** | Page content shifts left as the panel widens (no overlap) |
| **Persist open/closed** | Panel state (open/closed, width) is remembered across page navigations |

**Provider defaults:** The widget reads `GET /api/config` on load and pre-selects
whichever `--provider` was passed at server startup.

---

### Ingestion (`rag/ingest.py`)

Chunks all page content and summaries, embeds them, and stores in ChromaDB.
Uses ChromaDB's built-in ONNX `all-MiniLM-L6-v2` embeddings — local, no API
key or GPU required.

**Two-stage mode (default)** creates two separate collections for Multi-Representation
Indexing — summaries as retrieval keys, full-text chunks as the answer context:

| Collection | Contents | Role |
|------------|----------|------|
| `ps_docs_summaries` | One entry per page (AI summary or 500-char body preview) | Stage 1: find relevant pages |
| `ps_docs_content` | Chunked body_text (800 tok / 100 overlap) | Stage 2: fetch detailed context |

```bash
python -m rag.ingest run                     # two-stage (recommended)
python -m rag.ingest run --mode flat         # single ps_docs collection (legacy)
python -m rag.ingest run --reset             # wipe collections first, then ingest
python -m rag.ingest stats                   # show chunk counts for all collections
python -m rag.ingest reset                   # wipe all collections
```

**Chunking:** 800-token chunks, 100-token overlap. Metadata per chunk:
`{url, title, section_path, type}`.

**Embedding backend** (set `EMBEDDING_MODEL` in `.env`):

| Value | Description |
|-------|-------------|
| `claude` (default) | ChromaDB ONNX embeddings — local, fast, no API key |
| `ollama` | Ollama local inference (`llama3.2` installed) |

---

### Query CLI (`rag/query.py`)

Retrieval mode is **auto-detected**: if `ps_docs_summaries` and `ps_docs_content` both
exist, two-stage retrieval is used automatically. Otherwise falls back to the flat
`ps_docs` collection.

**Two-stage flow:**
1. Stage 1 — embed query → search `ps_docs_summaries` → identify top-N most relevant pages
2. Stage 2 — search `ps_docs_content` filtered to those pages → return best full-text chunks

#### LLM Providers

The CLI supports two answer-generation backends, selectable via `--provider` / `-p`:

| Provider | Flag | Model | Key Required | When to use |
|----------|------|-------|-------------|-------------|
| **`anthropic`** ⬅ default | *(omit flag)* | `claude-sonnet-4-6` | `ANTHROPIC_API_KEY` in `.env` | Best answer quality — use when not on a restricted network |
| `github` | `--provider github` | `gpt-4o` via GitHub Models API | `GITHUB_TOKEN` in `.env` | Fallback when `api.anthropic.com` is blocked (e.g. corporate network) |

> **Corporate network note:** Cognizant-issued laptops typically block direct
> access to `api.anthropic.com`. Use `--provider github` in that case — the
> GitHub Models endpoint (`models.inference.ai.azure.com`) is generally permitted.
> See [GitHub → Settings → Developer Settings → Personal Access Tokens](https://github.com/settings/tokens)
> to generate a classic PAT (no scopes required).

#### Commands

```bash
# ── Default provider: Anthropic / claude-sonnet-4-6 ─────────────────────────

# Single question (uses Anthropic by default)
python -m rag.query ask "How does AFT batch settlement work?"
python -m rag.query ask "What are EFT reject codes?" --top-k 8 --show-sources

# Interactive REPL (uses Anthropic by default)
python -m rag.query interactive
# In REPL: prefix with /search for raw retrieval without LLM synthesis

# ── GitHub Models fallback: gpt-4o ──────────────────────────────────────────

# Single question via GitHub
python -m rag.query ask "How does AFT batch settlement work?" --provider github
python -m rag.query ask "How does AFT batch settlement work?" -p github

# Interactive REPL via GitHub
python -m rag.query interactive --provider github

# ── Raw semantic search (no LLM, provider flag not applicable) ───────────────

# Shows Stage 1 matched pages + Stage 2 content chunks
python -m rag.query search "wire transfer cut-off times"
```

---

### MCP Server (`mcp_server/server.py`)

Exposes the RAG system as tools inside Claude Code conversations.

#### Register in Claude Code

Add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "ps-docs": {
      "command": "/Users/binoydas/Documents/Code/Central1/psend/bin/python",
      "args": ["/Users/binoydas/Documents/Code/Central1/ps-docs-rag/mcp_server/server.py"],
      "env": {
        "ANTHROPIC_API_KEY": "sk-ant-...",
        "CHROMA_DB_PATH": "/Users/binoydas/Documents/Code/Central1/ps-docs-rag/output/chroma_db",
        "SUMMARIES_DIR": "/Users/binoydas/Documents/Code/Central1/ps-docs-rag/output/summaries",
        "SITE_MAP_PATH": "/Users/binoydas/Documents/Code/Central1/ps-docs-rag/output/site_map.json",
        "CHROMA_COLLECTION": "ps_docs"
      }
    }
  }
}
```

Restart Claude Code after adding. Run `/mcp` in Claude Code to verify the server is connected.

#### Available Tools

| Tool | Description |
|------|-------------|
| `search_docs(query, top_k)` | Semantic search — returns ranked chunks with source metadata |
| `ask_docs(question, top_k)` | Full RAG answer synthesized by Claude |
| `get_section_summary(section)` | Returns the pre-built markdown summary for a section |
| `get_master_summary()` | Returns the top-level architecture guide |
| `list_sections()` | Lists all available section names |

**Important:** Use the full venv Python path in `settings.json`
(`psend/bin/python`), not just `python` — system Python lacks the dependencies.

---

## Project Structure

```
ps-docs-rag/
├── .env                        # credentials — gitignored, copy from .env.template
├── .env.template               # all configurable variables
├── pyproject.toml
├── crawler/
│   ├── auth.py                 # Playwright ADFS authentication (2-step HRD flow)
│   └── crawl.py                # incremental web crawler (requests + BeautifulSoup)
├── summarizer/
│   ├── summarize.py            # 3-tier Claude markdown summarization (page/section/master)
│   └── build_site.py           # navigable HTML site builder + Q&A widget (qa.js)
├── rag/
│   ├── embeddings.py           # pluggable embedding backends (ONNX / Ollama)
│   ├── ingest.py               # ChromaDB chunking + ingestion (two-stage mode)
│   └── query.py                # CLI Q&A (ask / search / interactive); Anthropic + GitHub providers
├── mcp_server/
│   └── server.py               # MCP server exposing RAG tools to Claude Code
├── web_server/
│   └── server.py               # FastAPI: serves site + /api/ask RAG endpoint
└── output/                     # gitignored — generated data
    ├── site_map.json           # hierarchical section tree
    ├── pages/                  # 725 crawled page JSON files
    ├── summaries/
    │   ├── master_summary.md
    │   ├── sections/           # one .md per section (AFT.md, etc.)
    │   └── pages/              # one .md per crawled page
    ├── site/                   # navigable HTML site (served by web_server)
    │   ├── index.html
    │   ├── assets/style.css
    │   ├── assets/qa.js        # Q&A widget — auto-built by build_site.py
    │   ├── {section}/index.html
    │   └── {section}/{group}/{page}.html
    └── chroma_db/              # ChromaDB vector store (persistent)
```

---

## Bugs Fixed

| Bug | Symptom | Fix |
|-----|---------|-----|
| **ADFS auth** | Crawler landed on SSO login page; `requests` NTLM/Basic auth rejected | Switched to Playwright-driven 2-step ADFS flow in `crawler/auth.py` |
| **`section_path` URL encoding** | Saved pages had `"ps_manual > Clearing%20and%20Deposits"` | `_extract_section_path` in `crawl.py` now decodes `%20` and strips `ps_manual` prefix |
| **Section grouping** | Summarizer grouped all 725 pages under `"ps_manual"`, producing one summary file | `_group_by_section` in `summarize.py` now strips `ps_manual` prefix and URL-decodes before grouping |
| **Model not found** | `summarize run` failed with 404 on `claude-3-5-haiku-20241022` | Updated to `claude-haiku-4-5-20251001` |

---

## Troubleshooting

**Auth fails / crawler saves login page content:**
The portal uses ADFS SSO — not Basic/NTLM. Playwright handles this.
Ensure `playwright install chromium` has been run inside the `psend` venv.

**`build_site` command not recognised:**
`build_site` is a single-command Typer app. Call without subcommand:
```bash
python -m summarizer.build_site          # correct
python -m summarizer.build_site run      # wrong — "run" is not a subcommand here
```

**Site summaries missing after `build_site` re-run:**
Section and master summaries are loaded from `output/summaries/` (written by
`summarizer.summarize`). If those files exist they are always used — no API call
is made. Only run `python -m summarizer.build_site` with no flags to trigger
live Claude API calls for sections/groups that have no stored summary file.

**Widget Q&A not updating after code changes:**
`build_site` writes `qa.js` on every run. After changing `build_site.py`, run:
```bash
python -m summarizer.build_site --no-api   # fast, skips unchanged pages
```
Or just restart the server with `--rebuild` which does this automatically.

**`summarize` / `crawl` commands need subcommand:**
These are multi-command apps and do need the subcommand:
```bash
python -m summarizer.summarize run       # correct
python -m crawler.crawl run             # correct
```

**MCP server uses wrong Python / missing packages:**
Use the full venv path: `/Users/binoydas/Documents/Code/Central1/psend/bin/python`

**ChromaDB ONNX model download on first ingest:**
The `all-MiniLM-L6-v2` model (~90MB) downloads automatically from HuggingFace
on first run. Requires internet access once; cached locally thereafter.

**Summarizer interrupted mid-run:**
Use `--resume` — it skips pages that already have a summary file:
```bash
python -m summarizer.summarize run --resume
```
