#!/usr/bin/env python3
"""pinpoint renderer -- JSON to a monospace clue list + answer."""
from games import common as _c


def _header(puz):
    return [
        f"game      : {puz['game']}",
        f"number    : {puz.get('number')}",
        f"date      : {puz.get('date')}",
        f"clues    : {len(puz.get('clues', []))}",
        f"blanks   : {puz.get('blanks')}",
        f"answer   : {puz.get('answer')}",
        "",
        "Grid (clues lead to one shared category; answer = the revealed category phrase):",
    ]


def render(date_str, fmt="unicode"):
    puz = _c.load(date_str, "pinpoint")
    if puz is None:
        return [f"(no pinpoint.json for {date_str})"]
    clues = puz.get("clues", [])
    answer = puz.get("answer")
    blanks = puz.get("blanks")
    out = []
    for i, c in enumerate(clues, 1):
        out.append(f"  {i}. {c}")
    out.append("")
    if answer is not None:
        blanks_s = f" ({blanks} blanks)" if blanks else ""
        out.append(f"  answer{blanks_s}: {answer}")
    return out
