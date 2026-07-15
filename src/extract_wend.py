#!/usr/bin/env python3
"""Extract the Wend board from a captured HTML and write outputs/<date>/wend.json.

Format (matches the hand-authored reference):
  {
    "game": "wend",
    "number": <int|null>,
    "date": "YYYY-MM-DD",
    "grid_size": [5, 5],
    "grid": [ ["N","T",".","O","V"], ... ],   # '.' = hole
    "words": [ "ICY", "OVAL", ... ]           # solution words (not in board DOM)
  }

The grid (letters + holes) IS in the board DOM. The puzzle number and the
solution words are NOT in the initial board DOM (they appear only after
in-game reveal/solve), so they must be supplied: --number / --words (or a
_meta.json from tbp_capture for the number).

Usage:
  python3 src/extract_wend.py [cache/2026-07-13/wend.html] [--date ...]
                              [--number N] [--words ICY,OVAL,QUICK,LANTERN]
                              [--meta cache/.../wend_meta.json]
"""
import os, sys, json, argparse
from datetime import date
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def extract(path, number=None, words=None):
    dom = open(path, encoding="utf-8", errors="replace").read()
    s = BeautifulSoup(dom, "html.parser")
    board = s.find("div", attrs={"data-testid": "wend-game-board"})
    if not board:
        raise SystemExit(f"no wend-game-board in {path}")
    cells = board.find_all(attrs={"data-cell-idx": True})
    n = len(cells)
    cols = int(n ** 0.5 + 0.5)
    grid = [["" for _ in range(cols)] for _ in range(cols)]
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        is_hole = c.get("data-cell-is-hole") == "true"
        letter = c.get_text(strip=True)
        grid[r][col] = "." if is_hole else letter
    data = {"game": "wend", "number": number, "grid_size": [cols, cols],
            "grid": grid}
    # Only include "words" when the user actually supplies them (they are NOT
    # in the board DOM). No placeholder is written when omitted.
    if words is not None:
        data["words"] = words
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=None)
    ap.add_argument("--date", default=date.today().strftime("%Y-%m-%d"))
    ap.add_argument("--number", type=int, default=None)
    ap.add_argument("--words", default=None,
                    help="comma-separated solution words (not in board DOM)")
    ap.add_argument("--meta", default=None,
                    help="path to a *_meta.json with {\"number\": N} from tbp_capture")
    args = ap.parse_args()
    path = args.path or os.path.join(ROOT, "cache", args.date, "wend.html")
    number = args.number
    words = args.words.split(",") if args.words else None
    if number is None and args.meta and os.path.exists(args.meta):
        try:
            number = json.load(open(args.meta)).get("number")
        except Exception:
            pass
    data = extract(path, number, words)
    data["date"] = args.date
    out = os.path.join(ROOT, "outputs", args.date, "wend.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(data, open(out, "w"), indent=2, ensure_ascii=False)
    print(f"wrote {out}")
    print(f"grid={data['grid_size']} number={data['number']} "
          f"words={data['words'] if 'words' in data else '<omitted>'}")


if __name__ == "__main__":
    main()
