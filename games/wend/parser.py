#!/usr/bin/env python3
"""wend parser -- HTML to JSON. Number is date-math (local anchor).
The grid (letters + holes) is in the DOM; the solution words are revealed by
the scraper and returned alongside the HTML, so no manual --words needed."""
from datetime import date
from bs4 import BeautifulSoup
from games import common as _c

_ANCHOR_DATE = date(2026, 7, 13)
_ANCHOR_NUM = 35


def number(d=None):
    d = d or date.today()
    return _ANCHOR_NUM + (d - _ANCHOR_DATE).days


def parse(date_str, html):
    soup = BeautifulSoup(html, "html.parser")
    board = soup.find("div", attrs={"data-testid": "wend-game-board"})
    if not board:
        raise SystemExit("no wend-game-board in HTML")
    cells = board.find_all(attrs={"data-cell-idx": True})
    n = len(cells)
    cols = int(n ** 0.5 + 0.5)
    grid = [["" for _ in range(cols)] for _ in range(cols)]
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        is_hole = c.get("data-cell-is-hole") == "true"
        letter = c.get_text(strip=True)
        grid[r][col] = "." if is_hole else letter
    data = {"game": "wend", "number": number(), "date": date_str,
            "grid_size": [cols, cols], "grid": grid}
    words = extract_words_inline(html)
    if words is not None:
        data["words"] = words
    out = _c.write_json(date_str, "wend", data)
    print(f"wrote {out}")
    return data


def extract_words_inline(html):
    from games.wend.scraper import extract_words
    return extract_words(html)
