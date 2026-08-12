#!/usr/bin/env python3
"""crossclimb renderer -- JSON to a monospace ladder + clues block."""
from games import common as _c


def _header(puz):
    return [
        f"game      : {puz['game']}",
        f"number    : {puz['number']}",
        f"date      : {puz['date']}",
        f"difficulty: {puz.get('difficulty', '')}",
        "",
    ]


def render(date_str, fmt="unicode"):
    if puz := _c.load(date_str, "crossclimb"):
        rows = puz["words"]
        out = _header(puz)
        out.append("Ladder (word : clue, top -> bottom):")
        for word, clue in rows:
            out.append(f"  {word} : {clue}")
        return out
    return [f"(no crossclimb.json for {date_str})"]
