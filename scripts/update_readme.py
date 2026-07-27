#!/usr/bin/env python3
"""Regenerate the daily-games section of README.md.

Replaces the content between the markers
    <!-- DAILY-GAMES-START -->
    <!-- DAILY-GAMES-END -->
with today's 8 game grids (no headers). Idempotent -- safe to run on every
CI run. Missing games render their "(no <game>.json ...)" placeholder so a
capture miss is visible instead of silently dropping the game.
"""
import argparse
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from games import GAMES, renderer as _renderer

_UNICODE_GAMES = {"queens", "minisudoku"}
_START = "<!-- DAILY-GAMES-START -->"
_END = "<!-- DAILY-GAMES-END -->"


def build_block(date_str):
    out = [f"## Today's games ({date_str})", ""]
    for g in GAMES:
        r = _renderer(g)
        fmt = "unicode" if g in _UNICODE_GAMES else "ascii"
        grid = r.render(date_str, fmt=fmt)  # grids only, no _header
        out.append(f"### {g}")
        out.append("```")
        out.extend(grid)
        out.append("```")
        out.append("")
    return "\n".join(out).rstrip("\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=date.today().strftime("%Y-%m-%d"),
                    help="date folder YYYY-MM-DD (default: today)")
    args = ap.parse_args()
    date_str = args.date

    block = build_block(date_str)
    replacement = f"{_START}\n{block}\n{_END}"

    readme_path = os.path.join(ROOT, "README.md")
    with open(readme_path, encoding="utf-8") as f:
        text = f.read()

    if _START in text and _END in text:
        new_text = re.sub(re.escape(_START) + r".*?" + re.escape(_END),
                          replacement, text, count=1, flags=re.S)
    else:
        new_text = text.rstrip() + "\n\n" + replacement + "\n"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"updated README daily games for {date_str}")


if __name__ == "__main__":
    main()
