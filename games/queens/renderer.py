#!/usr/bin/env python3
"""queens renderer -- JSON to a board.

Two representations live here:
  * _unicode_grid -> emoji colour squares (default)
  * _ascii_grid   -> region-id ascii box
Only one is shown at a time; `render(..., fmt=...)` picks.
"""
from games import common as _c

PALETTE = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫", "⬛", "⬜"]


def _header(puz):
    regions = {v for row in puz["board"] for v in row}
    return [
        f"game      : {puz['game']}",
        f"number    : {puz.get('number')}",
        f"date      : {puz.get('date')}",
        f"grid_size : {puz['grid_size']}  (cols x rows)",
        f"regions   : {len(regions)}",
        "",
        "Grid (digit = region id):",
    ]


def _unicode_grid(puz):
    n_cols, n_rows = puz["grid_size"]
    board = puz["board"]
    return ["".join(
        PALETTE[board[r][c]] if 0 <= board[r][c] < len(PALETTE) else "❓"
        for c in range(n_cols)) for r in range(n_rows)]


def _ascii_grid(puz):
    n_cols, n_rows = puz["grid_size"]
    board = puz["board"]
    rows = ["|" + "|".join(f" {board[r][c]:>1} " for c in range(n_cols)) + "|"
            for r in range(n_rows)]
    head = "+" + "+".join(["---"] * n_cols) + "+"
    return [head] + sum(([ln, head] for ln in rows), [])


def render(date_str, fmt="unicode"):
    puz = _c.load(date_str, "queens")
    if puz is None:
        return [f"(no queens.json for {date_str})"]
    return _ascii_grid(puz) if fmt == "ascii" else _unicode_grid(puz)
