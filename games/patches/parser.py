#!/usr/bin/env python3
"""patches parser -- HTML to JSON. Number is date-math (local anchor)."""
from datetime import date
import re
from bs4 import BeautifulSoup
from games import common as _c

_ANCHOR_DATE = date(2026, 7, 13)
_ANCHOR_NUM = 118

# Locale-agnostic keyword sets (LinkedIn UI flips between PT-BR and EN).
COORD_RE = re.compile(r"(?:linha|Row)\s+(\d+),\s*(?:coluna|column)\s+(\d+)",
                      re.IGNORECASE)
FREE_RE = re.compile(r"(\d+)\s*(?:c[ée]lulas|cells)", re.IGNORECASE)


def number(d=None):
    d = d or date.today()
    return _ANCHOR_NUM + (d - _ANCHOR_DATE).days


def classify(al):
    low = al.lower()
    sm = FREE_RE.search(al)
    size = int(sm.group(1)) if sm else None
    if "quadrado" in low or "square" in low:
        return "square", size
    if "retângulo vertical" in low or "tall rectangle" in low:
        return "V_rect", size
    if "retângulo horizontal" in low or "wide rectangle" in low:
        return "H_rect", size
    if "forma livre" in low or "freeform" in low:
        return "free", size
    return None, None


def parse(date_str, html):
    soup = BeautifulSoup(html, "html.parser")
    board = soup.find("div", attrs={"data-testid": "patches-game-board"})
    if not board:
        raise SystemExit("no patches-game-board in HTML")
    grid = board.find(attrs={"data-testid": "interactive-grid"})
    cells = grid.find_all(attrs={"data-cell-idx": True})
    n = len(cells)
    cols = int(n ** 0.5 + 0.5)
    clues = []
    for c in cells:
        al = c.get("aria-label", "")
        if not re.search(r"pista|clue", al, re.IGNORECASE):
            continue
        m = COORD_RE.search(al)
        if not m:
            continue
        y = int(m.group(1)) - 1
        x = int(m.group(2)) - 1
        t, size = classify(al)
        if t is None:
            continue
        clues.append({"x": x, "y": y, "type": t, "size": size})
    data = {"game": "patches", "number": number(), "date": date_str,
            "grid_size": [cols, cols], "clues": clues}
    out = _c.write_json(date_str, "patches", data)
    print(f"wrote {out}")
    return data
