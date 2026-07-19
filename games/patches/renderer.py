#!/usr/bin/env python3
"""patches renderer -- JSON to a monospace board of shape+size cells."""
from games import common as _c

GLYPH = {"free": "+", "square": "=", "H_rect": "-", "V_rect": "|"}


def _header(puz):
    types = {}
    for cl in puz.get("clues", []):
        types[cl["type"]] = types.get(cl["type"], 0) + 1
    return [
        f"game      : {puz['game']}",
        f"number    : {puz.get('number')}",
        f"date      : {puz.get('date')}",
        f"grid_size : {puz['grid_size']}  (cols x rows)",
        f"clues    : {len(puz.get('clues', []))}  {types}",
        "",
        "Grid (cell = shape+size (space if null); "
        "+=free =square -=H-rect |=V-rect, .. = empty):",
    ]


def render(date_str, fmt="unicode"):
    puz = _c.load(date_str, "patches")
    if puz is None:
        return [f"(no patches.json for {date_str})"]
    n_cols, n_rows = puz["grid_size"]
    mark = {}
    for cl in puz.get("clues", []):
        c, r = cl["x"], cl["y"]
        glyph = GLYPH.get(cl["type"], "?")
        size = cl.get("size")
        mark[(r, c)] = glyph + (str(size) if size is not None else " ")
    rows = []
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            v = mark.get((r, c), "..")
            row.append(f" {v} ")
        rows.append("|" + "|".join(row) + "|")
    head = "+" + "+".join(["----"] * n_cols) + "+"
    return [head] + sum(([ln, head] for ln in rows), [])
