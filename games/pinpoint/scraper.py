#!/usr/bin/env python3
"""pinpoint scraper -- Playwright capture (guess 5 times to reveal category)."""
from playwright.sync_api import Page
from games import common as _c


def capture(page: Page, date_str, save_html=False):
    page.goto("https://www.linkedin.com/games/view/pinpoint/desktop",
              wait_until="domcontentloaded")
    page.get_by_text("Start game").first.click()
    page.wait_for_selector("div.pinpoint__board")
    for _ in range(5):
        page.fill(".pinpoint__input", "_")
        page.press(".pinpoint__input", "Enter")
    page.wait_for_selector(".pinpoint__card__answer_text")
    html = page.content()
    if save_html:
        _c.save_html(date_str, "pinpoint", html)
    return html
