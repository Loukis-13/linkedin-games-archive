#!/usr/bin/env python3
"""zip renderer -- JSON to a monospace board."""
from games import common as _c


def _header(puz):
    return [
        f"game      : {puz['game']}",
        f"number    : {puz.get('number')}",
        f"date      : {puz.get('date')}",
        f"grid_size : {puz['grid_size']}  (cols x rows)",
        f"nodes     : {len(puz['nodes'])}",
        f"walls     : {len(puz['walls'])}",
        "",
        "Grid (numbers = nodes, | and - = walls, . = empty cell):",
    ]


def render(date_str, fmt="unicode"):
    puz = _c.load(date_str, "zip")
    if puz is None:
        return [f"(no zip.json for {date_str})"]
    n_cols, n_rows = puz["grid_size"]
    node_at = {(n["row"], n["col"]): n["id"] for n in puz["nodes"]}
    walls = {frozenset((tuple(w[0]), tuple(w[1]))) for w in puz["walls"]}

    def right_wall(r, c):
        return (frozenset(((r, c), (r, c + 1))) in walls) if c + 1 < n_cols else True

    def down_wall(r, c):
        return (frozenset(((r, c), (r + 1, c))) in walls) if r + 1 < n_rows else True

    lines = ["+" + "+".join(["----"] * n_cols) + "+"]
    for r in range(n_rows):
        row = "|"
        for c in range(n_cols):
            v = node_at.get((r, c))
            row += f" {v:>2d} " if v is not None else " .. "
            row += "|" if right_wall(r, c) else " "
        lines.append(row)
        hrow = "+"
        for c in range(n_cols):
            hrow += "----" if down_wall(r, c) else "    "
            hrow += "+" if right_wall(r, c) else " "
        lines.append(hrow)
    return lines
