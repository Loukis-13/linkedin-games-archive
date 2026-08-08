#!/usr/bin/env python3
"""minisudoku parser -- HTML to JSON. Number is date-math (local anchor)."""
import re
from datetime import date
from bs4 import BeautifulSoup
from games import common as _c

_ANCHOR_DATE = date(2026, 7, 15)
_ANCHOR_NUM = 338


def number(d=None):
    d = d or date.today()
    return _ANCHOR_NUM + (d - _ANCHOR_DATE).days


def parse(date_str, html):
    soup = BeautifulSoup(html, "html.parser")
    g = _c.find_grid(soup, "sudoku")
    cells = g.select("div[data-cell-idx]")
    rows, cols = _c.grid_dims(g, len(cells))
    board = [[None] * cols for _ in range(rows)]
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        cont = c.select_one(".sudoku-cell-content")
        txt = cont.get_text(strip=True) if cont else ""
        board[r][col] = int(txt) if txt.isdigit() else None
    data = {"game": "minisudoku",
            "date": date_str,
            "grid_size": [cols, rows],
            "cells": board}
    # Daily puzzle number + title + difficulty live in the
    # `pr-game-overboard-label pr-game-overboard-label__sudoku` node.
    # Example: "#361  Domino Set\n (Hard)"
    if title_el := soup.select_one('div[class*="pr-game-overboard-label__sudoku"]'):
        raw = title_el.get_text(" ", strip=True)
        if m := re.match(r"#(?P<number>\d+)\s*(?P<title>[^\n]*)(\s*\((?P<difficulty>.+)\))?$", raw, re.DOTALL):
            data["number"] = m["number"]
            data["title"] = m["title"]
            data["difficulty"] = m["difficulty"]
    out = _c.write_json(date_str, "minisudoku", data)
    print(f"wrote {out}")
    return data
