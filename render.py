#!/usr/bin/env python3
"""render.py -- render extracted puzzle JSON for inspection.

Usage:
  python render.py <date>                  # render every game from that day
  python render.py <date> <game>           # render one game
  python render.py <date> all              # same as: render every game
  python render.py <date> --header         # also print the summary header
  python render.py <date> --format ascii   # force ascii
  python render.py <date> --format unicode # force unicode

The <date> is required (no guessing "latest"). Output is a monospace block,
one game at a time, printed to stdout. The summary header is OFF by default;
pass --header to include it. --format defaults to "unicode" for games that have
a unicode representation (queens, minisudoku), otherwise "ascii".
"""
import argparse
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from games import GAMES, renderer as _renderer
from games import common as _c

# Games that have a dedicated unicode rendering; default to it.
_UNICODE_GAMES = {"queens", "minisudoku"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date", help="date folder YYYY-MM-DD")
    ap.add_argument("game", nargs="?", default="all",
                    help="game stem (zip/tango/...), or 'all' (default)")
    ap.add_argument("--header", action="store_true",
                    help="also print the per-game summary header")
    ap.add_argument("--format", choices=("ascii", "unicode"), default=None,
                    help="board format (default: unicode for games that have "
                         "it, else ascii)")
    args = ap.parse_args()

    date_str = args.date
    if args.game in (None, "all"):
        games = list(GAMES)
    else:
        games = [args.game]
        if args.game not in GAMES:
            print(f"unknown game {args.game!r}; choose from: {', '.join(GAMES)}")
            return

    multi = len(games) > 1
    for g in games:
        renderer = _renderer(g)
        fmt = args.format or ("unicode" if g in _UNICODE_GAMES else "ascii")
        puz = _c.load(date_str, g)
        lines = renderer.render(date_str, fmt=fmt)
        if args.header:
            if puz is None:
                hdr = [f"(no {g}.json for {date_str})"]
            elif hasattr(renderer, "_header"):
                hdr = renderer._header(puz)
            else:
                hdr = []
            lines = hdr + lines
        if multi:
            # visual separator: "### <game> ##################"
            width = 60
            lead = f"### {g} "
            sep = lead + "#" * max(0, width - len(lead))
            print(sep)
        for ln in lines:
            print(ln)
        print()


if __name__ == "__main__":
    main()
