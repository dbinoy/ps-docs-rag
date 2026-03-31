"""
Payment Solutions Documentation Crawler
Crawls the authenticated PS manual portal and saves structured JSON output.

Usage:
    python -m crawler.crawl run
    python -m crawler.crawl run --start-url https://... --max-pages 500
"""

from __future__ import annotations

import json
import os
import re
import time
from collections import deque
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

import requests
import typer
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

from crawler.auth import get_authenticated_cookies, inject_cookies

load_dotenv()
app = typer.Typer(help="PS Documentation Crawler")
console = Console()

BASE_URL = os.getenv("PS_PORTAL_URL", "https://psmanual.secure.central1.com/ps_manual/index.html")
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", "output"))
PAGES_DIR = Path(os.getenv("PAGES_DIR", "output/pages"))
SITE_MAP_PATH = Path(os.getenv("SITE_MAP_PATH", "output/site_map.json"))


def _make_slug(url: str) -> str:
    """Convert a URL to a safe filename slug."""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    name = path.replace("/", "_").strip("_") or "index"
    # Append query params hash if present to avoid collisions
    if parsed.query:
        import hashlib
        name += "_" + hashlib.md5(parsed.query.encode()).hexdigest()[:6]
    return re.sub(r"[^a-zA-Z0-9_\-.]", "", name)


def _build_session() -> requests.Session:
    """Authenticate via ADFS (Playwright) and return a cookie-loaded requests.Session."""
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) PSDocsBot/1.0"})

    cookies = get_authenticated_cookies(headless=True)
    if cookies:
        inject_cookies(session, cookies)
    else:
        console.print("[yellow]Warning: Auth returned no cookies — pages may redirect to login[/yellow]")

    return session


def _get_page(session: requests.Session, url: str) -> requests.Response | None:
    """Fetch a URL with retry logic."""
    for attempt in range(3):
        try:
            resp = session.get(url, timeout=30, verify=True)
            if resp.status_code == 200:
                return resp
            elif resp.status_code == 401:
                console.print(f"[red]401 Unauthorized on {url}[/red]")
                return None
            elif resp.status_code == 404:
                return None
            else:
                console.print(f"[yellow]HTTP {resp.status_code} on {url}[/yellow]")
                return None
        except requests.RequestException as e:
            if attempt < 2:
                time.sleep(2 ** attempt)
            else:
                console.print(f"[red]Failed after 3 attempts: {url} — {e}[/red]")
    return None


def _extract_nav_links(soup: BeautifulSoup, base_url: str, domain: str) -> list[str]:
    """Extract navigation/TOC links from the page."""
    links = []
    # Common documentation nav patterns: left pane, nav, sidebar, toc, menu
    nav_candidates = soup.find_all(
        ["nav", "ul", "div", "frame", "frameset"],
        class_=re.compile(r"nav|toc|menu|sidebar|tree|contents", re.I),
    )
    # Also grab frame src attributes (many old doc portals use framesets)
    for frame in soup.find_all(["frame", "iframe"]):
        src = frame.get("src", "")
        if src and not src.startswith(("http://", "https://", "javascript:", "#")):
            full = urljoin(base_url, src)
            if urlparse(full).netloc == domain:
                links.append(full)

    if nav_candidates:
        for nav in nav_candidates:
            for a in nav.find_all("a", href=True):
                href = a["href"].split("#")[0]
                if href:
                    full = urljoin(base_url, href)
                    if urlparse(full).netloc == domain:
                        links.append(full)
    else:
        # Fall back: grab all links in the page body
        for a in soup.find_all("a", href=True):
            href = a["href"].split("#")[0]
            if href and not href.startswith(("mailto:", "javascript:")):
                full = urljoin(base_url, href)
                if urlparse(full).netloc == domain and full != base_url:
                    links.append(full)

    return list(dict.fromkeys(links))  # deduplicate while preserving order


def _extract_breadcrumb(soup: BeautifulSoup) -> list[str]:
    """Extract breadcrumb trail from page."""
    # Common breadcrumb patterns
    for selector in [
        {"class": re.compile(r"breadcrumb", re.I)},
        {"id": re.compile(r"breadcrumb", re.I)},
        {"aria-label": re.compile(r"breadcrumb", re.I)},
    ]:
        bc = soup.find(attrs=selector)
        if bc:
            return [a.get_text(strip=True) for a in bc.find_all("a")] + [
                bc.find_all(["span", "li"])[-1].get_text(strip=True)
                if bc.find_all(["span", "li"])
                else ""
            ]
    return []


def _extract_section_path(url: str, breadcrumb: list[str]) -> str:
    """Derive a section path like 'AFT > Settlement', skipping the 'ps_manual' portal prefix."""
    if breadcrumb:
        parts = [p for p in breadcrumb if p]
        return " > ".join(parts)
    # Derive from URL path segments, excluding the 'ps_manual' portal root
    parsed = urlparse(url)
    parts = [
        p.replace("%20", " ")
        for p in parsed.path.split("/")
        if p and p != "ps_manual" and not p.endswith(".html")
    ]
    return " > ".join(parts) if parts else "root"


def _extract_page_data(resp: requests.Response, url: str) -> dict:
    """Parse an HTML page into structured data."""
    soup = BeautifulSoup(resp.text, "lxml")

    # Remove script/style noise
    for tag in soup(["script", "style", "noscript", "header", "footer"]):
        tag.decompose()

    title = ""
    if soup.title:
        title = soup.title.get_text(strip=True)
    elif soup.find("h1"):
        title = soup.find("h1").get_text(strip=True)

    # Main content: look for common content containers
    content_el = (
        soup.find(id=re.compile(r"content|main|body", re.I))
        or soup.find(class_=re.compile(r"content|main|article|body-content", re.I))
        or soup.find("main")
        or soup.find("article")
        or soup.body
    )
    body_text = content_el.get_text(separator="\n", strip=True) if content_el else ""

    breadcrumb = _extract_breadcrumb(soup)
    section_path = _extract_section_path(url, breadcrumb)

    # Collect all in-domain links for BFS expansion
    domain = urlparse(url).netloc
    links = _extract_nav_links(soup, url, domain)

    return {
        "url": url,
        "title": title,
        "section_path": section_path,
        "breadcrumb": breadcrumb,
        "body_text": body_text,
        "links": links,
        "content_length": len(body_text),
    }


def _build_site_map(pages: list[dict]) -> dict:
    """Build a hierarchical site map from crawled pages."""
    site_map: dict = {"sections": {}, "total_pages": len(pages)}
    for page in pages:
        parts = page["section_path"].split(" > ")
        node = site_map["sections"]
        for part in parts[:-1]:
            node = node.setdefault(part, {"_pages": [], "_children": {}})["_children"]
        leaf = parts[-1] if parts else "root"
        node.setdefault(leaf, {"_pages": [], "_children": {}})["_pages"].append(
            {"url": page["url"], "title": page["title"]}
        )
    return site_map


@app.command()
def run(
    start_url: str = typer.Option(BASE_URL, "--start-url", help="Entry point URL"),
    max_pages: int = typer.Option(1000, "--max-pages", help="Max pages to crawl"),
    delay: float = typer.Option(0.5, "--delay", help="Seconds between requests"),
    output_dir: Path = typer.Option(PAGES_DIR, "--output-dir", help="Directory to save page JSON files"),
    site_map_path: Path = typer.Option(SITE_MAP_PATH, "--site-map", help="Path to save site_map.json"),
    fresh: bool = typer.Option(False, "--fresh", help="Re-crawl everything, ignoring already-saved pages"),
):
    """Crawl the PS documentation portal and save structured page data.

    By default, any page already saved in output-dir is skipped so re-runs
    are incremental. Use --fresh to force a full re-crawl.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    site_map_path.parent.mkdir(parents=True, exist_ok=True)

    session = _build_session()
    domain = urlparse(start_url).netloc

    # Always load already-saved pages to skip them, unless --fresh is set.
    # We read directly from the JSON files — no dependency on site_map.json.
    visited: set[str] = set()
    pages: list[dict] = []
    if not fresh:
        for f in sorted(output_dir.glob("*.json")):
            try:
                saved = json.loads(f.read_text())
                visited.add(saved["url"])
                pages.append(saved)
            except (json.JSONDecodeError, KeyError):
                pass
        if visited:
            console.print(f"[dim]Skipping {len(visited)} already-saved pages (use --fresh to re-crawl all)[/dim]")

    queue: deque[str] = deque([start_url])
    queued: set[str] = {start_url}

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Crawling...", total=max_pages)

        while queue and len(visited) < max_pages:
            url = queue.popleft()
            if url in visited:
                continue

            progress.update(task, description=f"[cyan]{url[-60:]}[/cyan]", advance=1)

            resp = _get_page(session, url)
            if not resp:
                visited.add(url)
                continue

            content_type = resp.headers.get("content-type", "")
            if "html" not in content_type:
                visited.add(url)
                continue

            page_data = _extract_page_data(resp, url)
            visited.add(url)
            pages.append(page_data)

            # Save page JSON
            slug = _make_slug(url)
            page_path = output_dir / f"{slug}.json"
            page_path.write_text(json.dumps(page_data, ensure_ascii=False, indent=2))

            # Enqueue new links
            for link in page_data["links"]:
                if link not in queued and link not in visited:
                    if urlparse(link).netloc == domain:
                        queue.append(link)
                        queued.add(link)

            time.sleep(delay)

    # Write site map
    site_map = _build_site_map(pages)
    site_map_path.write_text(json.dumps(site_map, ensure_ascii=False, indent=2))

    console.print(f"\n[green]✓ Crawled {len(pages)} pages[/green]")
    console.print(f"  Pages saved to: {output_dir}/")
    console.print(f"  Site map: {site_map_path}")


@app.command()
def inspect(url: str = typer.Argument(..., help="URL to test-fetch and inspect")):
    """Fetch a single URL and print extracted data (useful for debugging)."""
    session = _build_session()
    resp = _get_page(session, url)
    if not resp:
        console.print("[red]Failed to fetch URL[/red]")
        raise typer.Exit(1)
    data = _extract_page_data(resp, url)
    data.pop("body_text")  # too verbose for console display
    console.print_json(json.dumps(data, indent=2))
    console.print(f"\n[dim]Body text length: {data.get('content_length', 0)} chars[/dim]")


if __name__ == "__main__":
    app()
