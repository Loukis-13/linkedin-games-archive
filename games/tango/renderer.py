#!/usr/bin/env python3
"""tango renderer -- JSON to a monospace board."""
from games import common as _c


def _header(puz):
    syms = puz.get("symbols", [])
    moons = sum(1 for s in syms if s[2] == "M")
    suns = sum(1 for s in syms if s[2] == "S")
    return [
        f"game      : {puz['game']}",
        f"number    : {puz.get('number')}",
        f"date      : {puz.get('date')}",
        f"grid_size : {puz['grid_size']}  (cols x rows)",
        f"symbols   : {len(syms)}  (Moon={moons}, Sun={suns})",
        f"divisors  : {len(puz.get('walls', []))} (= / x)",
        "",
        "Grid (M = given Moon, . = blank (fill Sun/Moon)):",
    ]


def render(date_str, fmt="unicode"):
    puz = _c.load(date_str, "tango")
    if puz is None:
        return [f"(no tango.json for {date_str})"]
    n_cols, n_rows = puz["grid_size"]
    sym = {(s[0], s[1]): s[2] for s in puz.get("symbols", [])}
    div = {}
    for w in puz.get("walls", []):
        a, b, sign = tuple(w[0]), tuple(w[1]), (w[2] if len(w) > 2 else "?")
        div[frozenset((a, b))] = sign

    def rsign(r, c):
        return div.get(frozenset(((r, c), (r, c + 1)))) if c + 1 < n_cols else None

    def dsign(r, c):
        return div.get(frozenset(((r, c), (r + 1, c)))) if r + 1 < n_rows else None

    lines = ["+" + "+".join(["---"] * n_cols) + "+"]
    for r in range(n_rows):
        row = "|"
        for c in range(n_cols):
            s = sym.get((r, c))
            row += f" {s} " if s else " . "
            rs = rsign(r, c)
            row += (rs if rs else "|") if c + 1 < n_cols else "|"
        lines.append(row)
        hrow = "+"
        for c in range(n_cols):
            ds = dsign(r, c)
            hrow += f"-{ds}-" if ds else "---"
            hrow += "+"
        lines.append(hrow)
    return lines
