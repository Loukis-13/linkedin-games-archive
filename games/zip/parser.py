#!/usr/bin/env python3
"""zip parser -- HTML to JSON. Number is date-math (local anchor)."""
from datetime import date
from bs4 import BeautifulSoup
from games import common as _c

# Daily puzzle number = anchor_number + days since anchor date.
_ANCHOR_DATE = date(2026, 7, 13)
_ANCHOR_NUM = 483


def number(d=None):
    d = d or date.today()
    return _ANCHOR_NUM + (d - _ANCHOR_DATE).days


def parse(date_str, html):
    soup = BeautifulSoup(html, "html.parser")
    g = _c.find_grid(soup, "trail")
    cells = g.select("div[data-cell-idx]")
    rows, cols = _c.grid_dims(g, len(cells))
    nodes, walls = [], []
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        cont = c.select_one(".trail-cell-content")
        txt = cont.get_text(strip=True) if cont else ""
        if txt.isdigit():
            nodes.append({"id": int(txt), "row": r, "col": col})
        for w in c.select('div[class*="trail-cell-wall"]'):
            cls = " ".join(w.get("class", []))
            if "trail-cell-wall--right" in cls and col + 1 < cols:
                walls.append([[r, col], [r, col + 1]])
            if "trail-cell-wall--down" in cls and r + 1 < rows:
                walls.append([[r, col], [r + 1, col]])
    data = {"game": "zip", "number": number(), "date": date_str,
            "grid_size": [cols, rows],
            "nodes": nodes, "walls": _c.dedupe_walls(walls)}
    out = _c.write_json(date_str, "zip", data)
    print(f"wrote {out}")
    return data
