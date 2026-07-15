#!/usr/bin/env python3
"""Extract the Patches initial state from a captured board HTML and write
outputs/<date>/patches.json.

Format (matches the hand-authored reference):
  {
    "game": "patches",
    "number": <int|null>,
    "date": "YYYY-MM-DD",
    "grid_size": [7, 7],
    "clues": [ {"x": col(1-indexed), "y": row(1-indexed),
                "type": "square"|"free"|"V_rect"|"H_rect",
                "size": <int|null>} , ... ]
  }

Each clue cell carries an aria-label like:
  "Dica de linha 2, coluna 2, pista quadrado"
  "Linha 2, coluna 3, pista forma livre, 2 células"
We parse that directly -> coords + type + size.

Usage:
  python3 src/extract_patches.py [cache/2026-07-13/patches.html] [--date ...]
                                [--number N] [--meta cache/.../patches_meta.json]
"""
import os, sys, json, argparse, re
from datetime import date
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# Locale-agnostic keyword sets (LinkedIn UI flips between PT-BR and EN).
# Coordinates: "linha R, coluna C" (PT) or "Row R, column C" (EN)
# Types:       square / tall rectangle (V_rect) / wide rectangle (H_rect) / free
COORD_RE = re.compile(
    r"(?:linha|Row)\s+(\d+),\s*(?:coluna|column)\s+(\d+)", re.IGNORECASE)
FREE_RE = re.compile(r"(\d+)\s*(?:c[ée]lulas|cells)", re.IGNORECASE)


def classify(al):
    """Return (type, size) from an aria-label, handling PT and EN."""
    low = al.lower()
    if "quadrado" in low or "square" in low:
        return "square", None
    if "retângulo vertical" in low or "tall rectangle" in low:
        return "V_rect", None
    if "retângulo horizontal" in low or "wide rectangle" in low:
        return "H_rect", None
    if "forma livre" in low or "freeform" in low:
        sm = FREE_RE.search(al)
        return "free", int(sm.group(1)) if sm else None
    return None, None


def extract(path, number=None):
    dom = open(path, encoding="utf-8", errors="replace").read()
    s = BeautifulSoup(dom, "html.parser")
    board = s.find("div", attrs={"data-testid": "patches-game-board"})
    if not board:
        raise SystemExit(f"no patches-game-board in {path}")
    grid = board.find(attrs={"data-testid": "interactive-grid"})
    cells = grid.find_all(attrs={"data-cell-idx": True})
    n = len(cells)
    cols = int(n ** 0.5 + 0.5)

    clues = []
    for c in cells:
        al = c.get("aria-label", "")
        # clue cells carry a "pista"/"clue" marker (PT/EN)
        if not re.search(r"pista|clue", al, re.IGNORECASE):
            continue
        m = COORD_RE.search(al)
        if not m:
            continue
        y = int(m.group(1)) - 1      # row (0-indexed)
        x = int(m.group(2)) - 1      # column (0-indexed)
        t, size = classify(al)
        if t is None:
            continue
        clues.append({"x": x, "y": y, "type": t, "size": size})
    return {"game": "patches", "number": number,
            "grid_size": [cols, cols], "clues": clues}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?", default=None)
    ap.add_argument("--date", default=date.today().strftime("%Y-%m-%d"))
    ap.add_argument("--number", type=int, default=None,
                    help="puzzle number (not in board DOM; from start screen)")
    ap.add_argument("--meta", default=None,
                    help="path to a *_meta.json with {\"number\": N} saved by tbp_capture")
    args = ap.parse_args()
    path = args.path or os.path.join(ROOT, "cache", args.date, "patches.html")
    number = args.number
    if number is None and args.meta and os.path.exists(args.meta):
        try:
            number = json.load(open(args.meta)).get("number")
        except Exception:
            pass
    data = extract(path, number)
    data["date"] = args.date
    out = os.path.join(ROOT, "outputs", args.date, "patches.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump(data, open(out, "w"), indent=2, ensure_ascii=False)
    print(f"wrote {out}")
    print(f"clues={len(data['clues'])} grid={data['grid_size']} number={data['number']}")


if __name__ == "__main__":
    main()
