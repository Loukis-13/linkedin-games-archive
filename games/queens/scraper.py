#!/usr/bin/env python3
"""queens scraper -- Playwright capture."""
import re
from playwright.sync_api import Page
from games import common as _c


def capture(page: Page, date_str, save_html=False):
    page.goto("https://www.linkedin.com/games/view/queens/desktop",
              wait_until="domcontentloaded")
    # Board only mounts after the landing "Start game" click.
    page.get_by_text(re.compile(r"Start game|Iniciar jogo")).first.click()
    page.wait_for_selector('div[class*="queens-grid"]')
    html = page.content()
    if save_html:
        _c.save_html(date_str, "queens", html)
    return html
