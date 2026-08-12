#!/usr/bin/env python3
"""pinpoint renderer -- JSON to a monospace clue list + answer."""
from games import common as _c


def _header(puz):
    return [
        f"game     : {puz['game']}",
        f"number   : {puz.get('number')}",
        f"date     : {puz.get('date')}",
        f"clues    : {len(puz.get('clues', []))}",
        "",
        "Grid (clues lead to one shared category; answer = the revealed category phrase):",
    ]


def render(date_str, fmt="unicode"):
    if puz := _c.load(date_str, "pinpoint"):
        return [
            *(f"  {i}. {c}" for i, c in enumerate(puz['clues'], 1)),
            "",
            f"  answer: {puz['answer']}",
        ]
    return [f"(no pinpoint.json for {date_str})"]
