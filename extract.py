#!/usr/bin/env python3
"""extract.py -- capture + parse every LinkedIn game for TODAY (no --date needed).

Launches one Chromium (locale en-US), drives each game's scraper to capture the
board, then runs each game's parser to write outputs/<today>/<game>.json.

Usage:
  python extract.py                          # all 8 games
  python extract.py --games zip,pinpoint,crossclimb
  python extract.py --headless              # no browser window
  python extract.py --save-html             # dump cache/<date>/<game>.html for debug

No scraping of stale HTML: the scraper hands its result straight to the parser
in memory.  --save-html only writes the HTML to cache/ for debugging.
"""
import argparse
import sys
import os

# allow `import games` from the repo root
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from games import GAMES, scraper as _scraper, parser as _parser
from games import common as _common


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", default=",".join(GAMES),
                    help="comma list; default = all")
    ap.add_argument("--headless", action="store_true",
                    help="run without a browser window")
    ap.add_argument("--save-html", action="store_true",
                    help="also dump cache/<date>/<game>.html for debugging")
    args = ap.parse_args()

    sel = [g.strip() for g in args.games.split(",") if g.strip()]
    sel = [g for g in sel if g in GAMES]
    date_str = _common.today_str()

    from playwright.sync_api import sync_playwright

    raw = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=args.headless)
        context = browser.new_context(locale="en-US")
        page = context.new_page()
        for g in sel:
            print(f"--- {g} (capture) ---", flush=True)
            try:
                raw[g] = _scraper(g).capture(page, date_str, args.save_html)
                print("  ok", flush=True)
            except Exception as e:
                print(f"  capture error: {e}", flush=True)
        browser.close()

    for g in sel:
        if g not in raw:
            continue
        print(f"--- {g} (parse) ---", flush=True)
        try:
            _parser(g).parse(date_str, raw[g])
        except Exception as e:
            print(f"  parse error: {e}", flush=True)


if __name__ == "__main__":
    main()
