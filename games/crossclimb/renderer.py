#!/usr/bin/env python3
"""crossclimb renderer -- JSON to a monospace ladder + clues block."""
from games import common as _c


def _header(puz):
    return [
        f"game      : {puz['game']}",
        f"number    : {puz.get('number')}",
        f"date      : {puz.get('date')}",
        "",
        "Grid (word per board row (1 = top .. 7 = bottom)):",
    ]


def render(date_str, fmt="unicode"):
    puz = _c.load(date_str, "crossclimb")
    if puz is None:
        return [f"(no crossclimb.json for {date_str})"]
    clues = {int(k): v for k, v in puz.get("clues", {}).items()}
    words = {int(k): v for k, v in puz.get("words", {}).items()}
    out = []
    for row in range(1, 8):
        out.append(f"  {words.get(row, '?'):<8}")
    middles = [clues[k] for k in sorted(clues) if k != 0]
    if middles:
        out.append("")
        out.append("Clues (middle rows):")
        out += [f"  - {c}" for c in middles]
    if clues.get(0):
        out.append("")
        out.append(f"Phrase (top+bottom): {clues[0]}")
    return out
