#!/usr/bin/env python3
"""crossclimb parser -- solved-game dict to JSON. Number is date-math (local anchor)."""
from datetime import date
from games import common as _c

_ANCHOR_DATE = date(2026, 7, 17)
_ANCHOR_NUM = 808


def number(d=None):
    d = d or date.today()
    return _ANCHOR_NUM + (d - _ANCHOR_DATE).days


def parse(date_str, game):
    # `game` is the dict returned by the scraper (words + clues), NOT html.
    data = {
        "game": "crossclimb",
        "number": number(),
        "date": date_str,
        "clues": {int(k): v for k, v in game.get("clues", {}).items()},
        "words": {int(k): v for k, v in game.get("words", {}).items()},
    }
    out = _c.write_json(date_str, "crossclimb", data)
    print(f"wrote {out}")
    return data
