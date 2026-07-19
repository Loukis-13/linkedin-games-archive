#!/usr/bin/env python3
"""tango parser -- HTML to JSON. Number is date-math (local anchor)."""
from datetime import date
from bs4 import BeautifulSoup
from games import common as _c

_ANCHOR_DATE = date(2026, 7, 13)
_ANCHOR_NUM = 644


def number(d=None):
    d = d or date.today()
    return _ANCHOR_NUM + (d - _ANCHOR_DATE).days


def parse(date_str, html):
    soup = BeautifulSoup(html, "html.parser")
    g = _c.find_grid(soup, "lotka")
    cells = g.select("div[data-cell-idx]")
    rows, cols = _c.grid_dims(g, len(cells))
    symbols, walls = [], []
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        cont = c.select_one(".lotka-cell-content")
        svg = cont.find("svg") if cont else None
        al = (svg.get("aria-label") if svg else "") or ""
        al = al.strip().lower()
        if al == "moon":
            symbols.append([r, col, "M"])
        elif al == "sun":
            symbols.append([r, col, "S"])
        for e in c.select("div.lotka-cell-edge"):
            ecls = " ".join(e.get("class", []))
            esvg = e.find("svg")
            sign = (esvg.get("aria-label") if esvg else "") or ""
            sign = sign.strip().lower()
            sym = "=" if sign == "equal" else ("x" if sign in ("cross", "multiply") else None)
            if sym is None:
                continue
            if "lotka-cell-edge--right" in ecls and col + 1 < cols:
                walls.append([[r, col], [r, col + 1], sym])
            if "lotka-cell-edge--down" in ecls and r + 1 < rows:
                walls.append([[r, col], [r + 1, col], sym])
    data = {"game": "tango", "number": number(), "date": date_str,
            "grid_size": [cols, rows], "symbols": symbols, "walls": walls}
    out = _c.write_json(date_str, "tango", data)
    print(f"wrote {out}")
    return data
