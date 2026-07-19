#!/usr/bin/env python3
"""patches scraper -- Playwright capture (needs Start game click)."""
from playwright.sync_api import Page
from games import common as _c


def capture(page: Page, date_str, save_html=False):
    page.goto("https://www.linkedin.com/games/patches",
              wait_until="domcontentloaded")
    page.get_by_text("Start game").first.click()
    page.wait_for_selector('div[data-testid="patches-game-board"]')
    html = page.content()
    if save_html:
        _c.save_html(date_str, "patches", html)
    return html
