#!/usr/bin/env python3
"""zip scraper -- Playwright capture."""
from playwright.sync_api import Page
from games import common as _c


def capture(page: Page, date_str, save_html=False):
    page.goto("https://www.linkedin.com/games/view/zip/desktop",
              wait_until="domcontentloaded")
    _c.start_game(page, 'div[class*="trail-grid"]')
    html = page.content()
    if save_html:
        _c.save_html(date_str, "zip", html)
    return html
