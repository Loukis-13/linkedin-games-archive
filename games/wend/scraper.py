#!/usr/bin/env python3
"""wend scraper -- Playwright capture (Start game + reveal words)."""
from playwright.sync_api import Page
import re
from games import common as _c

_WORD_RE = re.compile(r"wend-word-list-slot-(\d+)-(\d+)")


def capture(page: Page, date_str, save_html=False):
    page.goto("https://www.linkedin.com/games/wend",
              wait_until="domcontentloaded")
    page.get_by_text(re.compile(r"Start game|Iniciar jogo")).first.click()
    page.wait_for_selector('div[data-testid="wend-game-board"]')
    # Reveal each word so the solution words mount in the DOM.
    words = page.locator("[data-testid^=wend-word-list-slot-]").all()
    for _ in range(len(words)):
        page.get_by_text(re.compile(r"Hint|Dica")).first.click()
    html = page.content()
    if save_html:
        _c.save_html(date_str, "wend", html)
    return html


def extract_words(html):
    """Read the solution words from the revealed word-list DOM. Returns the
    list of words, or None if the slots aren't present (board pre-reveal)."""
    from bs4 import BeautifulSoup
    s = BeautifulSoup(html, "html.parser")
    slots = {}
    for el in s.select('[data-testid^="wend-word-list-slot-"]'):
        m = _WORD_RE.match(el["data-testid"])
        if not m:
            continue
        w, l = int(m.group(1)), int(m.group(2))
        slots.setdefault(w, {})[l] = el.get_text(strip=True)
    if not slots:
        return None
    return ["".join(c[i] for i in sorted(c)) for w, c in sorted(slots.items())]
