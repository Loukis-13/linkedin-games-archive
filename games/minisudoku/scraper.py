#!/usr/bin/env python3
"""minisudoku scraper -- Playwright capture."""
from playwright.sync_api import Page
from games import common as _c


def capture(page: Page, date_str, save_html=False):
    page.goto("https://www.linkedin.com/games/view/mini-sudoku/desktop",
              wait_until="domcontentloaded")
    html = page.content()
    if save_html:
        _c.save_html(date_str, "minisudoku", html)
    return html
