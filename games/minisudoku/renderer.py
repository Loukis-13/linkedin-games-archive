#!/usr/bin/env python3
"""minisudoku renderer -- JSON to a board.

Two representations live here:
  * _unicode_grid -> unicode box-drawing grid + thick box separators (default)
  * _ascii_grid   -> +-|- ascii grid
Only one is shown at a time; `render(..., fmt=...)` picks.
"""
from games import common as _c

BOX = {6: (2, 3), 4: (2, 2), 9: (3, 3)}


def _header(puz):
    filled = sum(1 for row in puz["cells"] for v in row if v is not None)
    return [
        f"game      : {puz['game']}",
        f"number    : {puz.get('number')}",
        f"date      : {puz.get('date')}",
        f"grid_size : {puz['grid_size']}  (cols x rows)",
        f"givens    : {filled}",
        "",
        "Grid (digit = given, . = blank):",
    ]


def _unicode_grid(puz):
    n_cols, n_rows = puz["grid_size"]
    board = puz["cells"]
    bh, bw = BOX.get(n_cols, (1, 1))

    def ucell(r, c):
        v = board[r][c]
        return f" {v} " if v is not None else "   "

    def hline(left, boxsep, right, thick):
        seg = "━" if thick else "─"
        mid = "━" if thick else "┼"
        parts = []
        for c in range(n_cols):
            parts.append(seg * 3)
            if c < n_cols - 1:
                parts.append(boxsep if (c + 1) % bw == 0 else mid)
        return left + "".join(parts) + right

    out = [hline("┏", "┳", "┓", True)]
    for r in range(n_rows):
        row = "┃"
        for c in range(n_cols):
            row += ucell(r, c)
            row += "┃" if (c + 1) % bw == 0 else "│"
        out.append(row)
        if r < n_rows - 1:
            if (r + 1) % bh == 0:
                out.append(hline("┣", "╋", "┫", True))
            else:
                out.append(hline("┃", "┃", "┃", False))
    out.append(hline("┗", "┻", "┛", True))
    return out


def _ascii_grid(puz):
    n_cols, n_rows = puz["grid_size"]
    board = puz["cells"]

    def cell(r, c):
        v = board[r][c]
        return f" {v} " if v is not None else " . "

    rows = ["|" + "|".join(cell(r, c) for c in range(n_cols)) + "|"
            for r in range(n_rows)]
    head = "+" + "+".join(["---"] * n_cols) + "+"
    return [head] + sum(([ln, head] for ln in rows), [])


def render(date_str, fmt="unicode"):
    puz = _c.load(date_str, "minisudoku")
    if puz is None:
        return [f"(no minisudoku.json for {date_str})"]
    return _ascii_grid(puz) if fmt == "ascii" else _unicode_grid(puz)
