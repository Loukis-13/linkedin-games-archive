#!/usr/bin/env python3
"""wend renderer -- JSON to a monospace board + words list."""
from games import common as _c


def _header(puz):
    holes = sum(1 for row in puz["grid"] for v in row if v == ".")
    lines = [
        f"game      : {puz['game']}",
        f"number    : {puz.get('number')}",
        f"date      : {puz.get('date')}",
        f"grid_size : {puz['grid_size']}  (cols x rows)",
        f"holes     : {holes}",
    ]
    if puz.get("words"):
        lines.append(f"words     : {len(puz['words'])}")
    lines += ["", "Grid (# = hole, letter = tile (rendered as space)):"]
    return lines


def render(date_str, fmt="unicode"):
    puz = _c.load(date_str, "wend")
    if puz is None:
        return [f"(no wend.json for {date_str})"]
    n_cols, n_rows = puz["grid_size"]
    grid = puz["grid"]
    rows = []
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            v = grid[r][c]
            row.append(" # " if v == "." else f" {v:>1} ")
        rows.append("|" + "|".join(row) + "|")
    head = "+" + "+".join(["---"] * n_cols) + "+"
    out = [head] + sum(([ln, head] for ln in rows), [])
    words = puz.get("words")
    if words:
        out += ["", "Words:"]
        out += [f"  {w}" for w in words]
    return out
