"""
ADFS Authentication via Playwright.

The PS portal uses Central 1's ADFS with a 2-step HRD flow:
  Step 1 (HRD page):   Enter plain username → redirects to sts3.secure.central1.com
  Step 2 (Forms auth): Set loginForm.UserName = 'extranetqa\\user', fill password, submit

Returns a dict of cookies that can be injected into a requests.Session.
"""

from __future__ import annotations

import os

import requests
from dotenv import load_dotenv
from playwright.sync_api import TimeoutError as PWTimeout
from playwright.sync_api import sync_playwright
from rich.console import Console

load_dotenv()
console = Console()

PORTAL_URL = os.getenv("PS_PORTAL_URL", "https://psmanual.secure.central1.com/ps_manual/index.html")
_raw = os.getenv("PS_PORTAL_USERNAME", "extranetqa\\psdoperator3")
PASSWORD = os.getenv("PS_PORTAL_PASSWORD", "Testing123#")


def _plain_user(username: str) -> str:
    """Return just the user part from DOMAIN\\user or user@domain."""
    if "\\" in username:
        return username.split("\\", 1)[1]
    if "@" in username:
        return username.split("@", 1)[0]
    return username


def _grab_error(page) -> str:  # noqa: ANN001
    try:
        el = page.query_selector("#errorText, .error, #error")
        return el.inner_text() if el else ""
    except PWTimeout:
        return ""


def get_authenticated_cookies(headless: bool = True) -> dict[str, str]:
    """
    Drive the ADFS login flow via Playwright and return session cookies
    as a plain dict suitable for injection into a requests.Session.
    """
    plain = _plain_user(_raw)
    full_username = f"extranetqa\\{plain}"
    console.print(f"[dim]Authenticating as '{full_username}' via ADFS...[/dim]")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        ctx = browser.new_context(ignore_https_errors=True)
        page = ctx.new_page()

        # ── Step 1: Navigate to portal → lands on ADFS HRD page ──────────
        page.goto(PORTAL_URL, timeout=30_000)
        page.wait_for_load_state("networkidle", timeout=20_000)

        # ── Step 2: HRD — enter plain username, click Next ────────────────
        try:
            page.wait_for_selector("#emailInput", timeout=10_000)
            page.fill("#emailInput", plain)
            page.click("input[name='HomeRealmByEmail']")
            page.wait_for_load_state("networkidle", timeout=20_000)
        except PWTimeout:
            pass  # May have skipped HRD and gone straight to forms auth

        # ── Step 3: Forms auth ─────────────────────────────────────────────
        # #userNameInput is the visible field; loginForm.UserName is submitted.
        # We set both: visible = plain user, submitted = full domain\\user.
        try:
            page.wait_for_selector("#userNameInput", timeout=15_000)
            page.fill("#userNameInput", plain)
            page.evaluate(
                "(u) => { var f = document.forms['loginForm']; if (f && f.UserName) f.UserName.value = u; }",
                full_username,
            )
            page.fill("#passwordInput", PASSWORD)
            page.click("#submitButton")
            page.wait_for_load_state("networkidle", timeout=30_000)
        except PWTimeout as exc:
            console.print(f"[red]Auth failed — forms auth page not found: {exc}[/red]")
            console.print(f"  Current URL: {page.url}")
            browser.close()
            return {}

        # ── Step 4: Verify redirect back to portal ─────────────────────────
        final_url = page.url
        if "psmanual.secure.central1.com" not in final_url and "adfs" in final_url.lower():
            err = _grab_error(page)
            console.print(f"[red]Auth failed. URL: {final_url}[/red]")
            if err:
                console.print(f"[red]ADFS error: {err}[/red]")
            browser.close()
            return {}

        console.print(f"[green]Auth successful → {final_url[:80]}[/green]")

        # ── Step 5: Extract session cookies ───────────────────────────────
        cookies = {c["name"]: c["value"] for c in ctx.cookies()}
        browser.close()
        console.print(f"[dim]Extracted {len(cookies)} session cookies[/dim]")
        return cookies


def inject_cookies(session: requests.Session, cookies: dict[str, str]) -> None:
    """Inject a cookie dict into a requests.Session."""
    for name, value in cookies.items():
        session.cookies.set(name, value)
