#!/usr/bin/env python3
"""queens parser -- HTML to JSON. Number is date-math (local anchor).
Placed queens are intentionally ignored; only the region board is kept."""
from datetime import date
import re
from bs4 import BeautifulSoup
from games import common as _c

_ANCHOR_DATE = date(2026, 7, 13)
_ANCHOR_NUM = 804


def number(d=None):
    d = d or date.today()
    return _ANCHOR_NUM + (d - _ANCHOR_DATE).days


def parse(date_str, html):
    soup = BeautifulSoup(html, "html.parser")
    g = _c.find_grid(soup, "queens")
    cells = g.select("div[data-cell-idx]")
    n = len(cells)
    rows, cols = _c.grid_dims(g, n)
    board = [[None] * cols for _ in range(rows)]
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        region = None
        for cl in c.get("class", []):
            m = re.match(r"cell-color-(\d+)", cl)
            if m:
                region = int(m.group(1))
        board[r][col] = region
    data = {"game": "queens", "number": number(), "date": date_str,
            "grid_size": [cols, rows], "board": board}
    out = _c.write_json(date_str, "queens", data)
    print(f"wrote {out}")
    return data
