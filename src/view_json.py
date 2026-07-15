#!/usr/bin/env python3
"""view_json.py -- render a generated LinkedIn Games puzzle JSON for
human inspection in the terminal.

Supports all eight games:
  * zip         -- numbered nodes + walls (Zip)
  * tango       -- Moon/Sun grid (Tango)
  * queens      -- colored regions + placed queens (Queens)
  * minisudoku  -- prefilled 6x6 grid (Mini Sudoku)
  * wend        -- 5x5 letter grid + holes (Wend)
  * patches      -- 7x7 initial grid + clue tile lengths (Patches)
  * pinpoint / crossclimb -- captured via tbp browser; extractors TBD

Usage:
  python src/view_json.py                       # latest date, zip
  python src/view_json.py tango                 # game stem in latest date
  python src/view_json.py outputs/2026-07-12/queens.json
  python src/view_json.py minisudoku --date 2026-07-11
  python src/view_json.py all --date 2026-07-12 # render every game that day
"""
import sys, os, json, argparse
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "outputs")

# game names this viewer knows how to draw
KNOWN = ("zip", "tango", "queens", "minisudoku", "wend", "patches")


def latest_date():
    if not os.path.isdir(OUT):
        return None
    ds = [d for d in os.listdir(OUT)
          if os.path.isdir(os.path.join(OUT, d)) and d[0].isdigit()]
    return max(ds) if ds else None


def resolve(target, date_str):
    """Return a path to a JSON file given a stem/path + optional date."""
    target = target or "zip"
    if target.endswith(".json") and os.path.exists(target):
        return target
    if os.sep in target or target.startswith("output"):
        # looks like a path
        cand = os.path.join(ROOT, target)
        if os.path.exists(cand):
            return cand
    d = date_str or latest_date()
    if not d:
        return None
    return os.path.join(OUT, d, target + ".json")


def load(path):
    with open(path) as f:
        return json.load(f), path


# ---------------------------------------------------------------- renderers

def render_zip(puz):
    n_cols, n_rows = puz["grid_size"]
    node_at = {(n["row"], n["col"]): n["id"] for n in puz["nodes"]}
    walls = {frozenset((tuple(w[0]), tuple(w[1]))) for w in puz["walls"]}

    def right_wall(r, c):
        return frozenset(((r, c), (r, c + 1))) in walls if c + 1 < n_cols else True

    def down_wall(r, c):
        return frozenset(((r, c), (r + 1, c))) in walls if r + 1 < n_rows else True

    lines = ["+" + "+".join(["----"] * n_cols) + "+"]
    for r in range(n_rows):
        row = "|"
        for c in range(n_cols):
            v = node_at.get((r, c))
            row += f" {v:>2d} " if v is not None else " .. "
            row += "|" if right_wall(r, c) else " "
        lines.append(row)
        hrow = "+"
        for c in range(n_cols):
            hrow += "----" if down_wall(r, c) else "    "
            hrow += "+" if right_wall(r, c) else " "
        lines.append(hrow)
    return lines


def render_tango(puz):
    """New format: symbols=[[row,col,'M'|'S']], walls=[[[r,c],[r,c],'='|'x']]."""
    n_cols, n_rows = puz["grid_size"]
    sym = {(s[0], s[1]): s[2] for s in puz.get("symbols", [])}
    # divisor between two cells -> sign
    div = {}
    for w in puz.get("walls", []):
        a, b, sign = tuple(w[0]), tuple(w[1]), (w[2] if len(w) > 2 else "?")
        div[frozenset((a, b))] = sign

    def rsign(r, c):  # sign on right edge
        return div.get(frozenset(((r, c), (r, c + 1)))) if c + 1 < n_cols else None

    def dsign(r, c):  # sign on down edge
        return div.get(frozenset(((r, c), (r + 1, c)))) if r + 1 < n_rows else None

    lines = ["+" + "+".join(["---"] * n_cols) + "+"]
    for r in range(n_rows):
        row = "|"
        for c in range(n_cols):
            s = sym.get((r, c))
            row += f" {s} " if s else " . "
            rs = rsign(r, c)
            row += (rs if rs else "|") if c + 1 < n_cols else "|"
        lines.append(row)
        hrow = "+"
        for c in range(n_cols):
            ds = dsign(r, c)
            hrow += f"-{ds}-" if ds else "---"
            hrow += "+"
        lines.append(hrow)
    return lines


def render_queens(puz):
    """New format: board=[[region_id]] (placed queens ignored)."""
    n_cols, n_rows = puz["grid_size"]
    board = puz["board"]
    rows = []
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            row.append(f" {board[r][c]:>1} ")
        rows.append("|" + "|".join(row) + "|")
    head = "+" + "+".join(["---"] * n_cols) + "+"
    return [head] + sum(([ln, head] for ln in rows), [])


def render_minisudoku(puz):
    """New format: cells=[[digit|null]]."""
    n_cols, n_rows = puz["grid_size"]
    board = puz["cells"]
    rows = []
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            v = board[r][c]
            row.append(f" {v:>1} " if v is not None else " . ")
        rows.append("|" + "|".join(row) + "|")
    head = "+" + "+".join(["---"] * n_cols) + "+"
    return [head] + sum(([ln, head] for ln in rows), [])


def render_wend(puz):
    """Wend: grid=[[letter|'.'(hole)]]. Holes shown as '#'."""
    n_cols, n_rows = puz["grid_size"]
    grid = puz["grid"]
    rows = []
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            v = grid[r][c]
            row.append(" # " if v == "." else f" {v:>1} ")
        rows.append("|" + "|".join(row) + "|")
    head = "+" + "+".join(["---"] * n_cols) + "+"
    return [head] + sum(([ln, head] for ln in rows), [])


def render_patches(puz):
    """Patches: clues=[{x=col, y=row, type, size}]. Mark clue cells."""
    n_cols, n_rows = puz["grid_size"]
    # cell -> short label: size for free, letter for fixed shapes
    mark = {}
    for cl in puz.get("clues", []):
        x, y = cl["x"], cl["y"]          # 0-indexed
        c, r = x, y
        if cl["type"] == "free":
            mark[(r, c)] = str(cl["size"])
        elif cl["type"] == "square":
            mark[(r, c)] = "SQ"
        elif cl["type"] == "V_rect":
            mark[(r, c)] = "VR"
        elif cl["type"] == "H_rect":
            mark[(r, c)] = "HR"
    rows = []
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            v = mark.get((r, c))
            row.append(f" {v:>1} " if v else " . ")
        rows.append("|" + "|".join(row) + "|")
    head = "+" + "+".join(["---"] * n_cols) + "+"
    return [head] + sum(([ln, head] for ln in rows), [])


RENDERERS = {
    "zip": render_zip,
    "tango": render_tango,
    "queens": render_queens,
    "minisudoku": render_minisudoku,
    "wend": render_wend,
    "patches": render_patches,
}


def show(puz, path, verbose):
    g = puz["game"]
    print(f"=== {os.path.basename(path)} ===")
    print(f"game      : {g}")
    print(f"number    : {puz.get('number')}")
    print(f"date      : {puz.get('date')}")
    print(f"grid_size : {puz['grid_size']}  (cols x rows)")
    if g == "zip":
        print(f"nodes     : {len(puz['nodes'])}")
        print(f"walls     : {len(puz['walls'])}")
    elif g == "tango":
        syms = puz.get("symbols", [])
        moons = sum(1 for s in syms if s[2] == "M")
        suns = sum(1 for s in syms if s[2] == "S")
        print(f"symbols   : {len(syms)}  (Moon={moons}, Sun={suns})")
        print(f"divisors  : {len(puz.get('walls', []))} (= / x)")
    elif g == "queens":
        regions = {v for row in puz["board"] for v in row}
        print(f"regions   : {len(regions)}")
    elif g == "minisudoku":
        filled = sum(1 for row in puz["cells"] for v in row if v is not None)
        print(f"givens    : {filled}")
    elif g == "wend":
        holes = sum(1 for row in puz["grid"] for v in row if v == ".")
        print(f"holes     : {holes}")
    elif g == "patches":
        types = {}
        for cl in puz.get("clues", []):
            types[cl["type"]] = types.get(cl["type"], 0) + 1
        print(f"clues    : {len(puz.get('clues', []))}  {types}")
    print()
    fn = RENDERERS.get(g)
    if not fn:
        print(f"(no renderer for '{g}' yet)")
    else:
        legend = {
            "zip": "numbers = nodes, | and - = walls, . = empty cell",
            "tango": "M = given Moon, . = blank (fill Sun/Moon)",
            "queens": "digit = region id",
            "minisudoku": "digit = given, . = blank",
            "wend": "# = hole, letter = tile",
            "patches": "digit = free-tile size, SQ=square, VR=V-rect, HR=H-rect, . = empty",
        }.get(g, "")
        print(f"Grid ({legend}):")
        for ln in fn(puz):
            print(ln)
    if verbose and g == "zip":
        print()
        print("Nodes (1-indexed number -> row,col):")
        for n in sorted(puz["nodes"], key=lambda n: n["id"]):
            print(f"  {n['id']:>2}: ({n['row']},{n['col']})")
        print()
        print("Walls (blocked edge between two cells):")
        for w in puz["walls"]:
            print(f"  {w[0]} -- {w[1]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", nargs="?", default=None,
                    help="game stem (zip/tango/queens/minisudoku), 'all', "
                         "or a path to a .json file")
    ap.add_argument("--date", default=None, help="date folder YYYY-MM-DD")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    if args.target == "all":
        d = args.date or latest_date()
        if not d:
            print("no date folder found"); return
        for g in KNOWN:
            p = resolve(g, d)
            if p and os.path.exists(p):
                puz, path = load(p)
                show(puz, path, args.verbose)
                print()
        return

    p = resolve(args.target, args.date)
    if not p or not os.path.exists(p):
        print(f"cannot find puzzle for {args.target!r} "
              f"(date={args.date or latest_date()})")
        return
    puz, path = load(p)
    show(puz, path, args.verbose)


if __name__ == "__main__":
    main()
