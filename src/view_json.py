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
  * pinpoint     -- 5 clue words + revealed category (Pinpoint)
  * crossclimb   -- solved live in-browser via Playwright; answer saved as JSON (clues + 7-word ladder)

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
KNOWN = ("zip", "tango", "queens", "minisudoku", "wend", "patches", "pinpoint", "crossclimb")


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
    """New format: board=[[region_id]] (placed queens ignored).
    Shows an emoji-square view (region id -> colour) then the ASCII view."""
    n_cols, n_rows = puz["grid_size"]
    board = puz["board"]
    # palette indexed by region id (0..8) -> colour square
    PALETTE = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫", "⬛", "⬜"]
    # emoji grid
    emoji = []
    for r in range(n_rows):
        emoji.append("".join(
            PALETTE[board[r][c]] if 0 <= board[r][c] < len(PALETTE)
            else "❓" for c in range(n_cols)))
    # ascii grid (kept)
    ascii_rows = []
    for r in range(n_rows):
        row = [f" {board[r][c]:>1} " for c in range(n_cols)]
        ascii_rows.append("|" + "|".join(row) + "|")
    head = "+" + "+".join(["---"] * n_cols) + "+"
    ascii_block = [head] + sum(([ln, head] for ln in ascii_rows), [])
    return emoji + [""] + ascii_block


def render_minisudoku(puz):
    """New format: cells=[[digit|null]].
    Shows a unicode box-drawing view (thick lines on box borders) then ASCII."""
    n_cols, n_rows = puz["grid_size"]
    board = puz["cells"]
    # box dimensions (rows x cols per sub-box); 6x6 mini-sudoku = 2x3
    BOX = {6: (2, 3), 4: (2, 2), 9: (3, 3)}
    bh, bw = BOX.get(n_cols, (1, 1))

    def cell(r, c):
        v = board[r][c]
        return f" {v} " if v is not None else " . "

    def ucell(r, c):
        # unicode view leaves empty cells blank (no dots)
        v = board[r][c]
        return f" {v} " if v is not None else "   "

    # --- unicode box view ---
    def hline(left, boxsep, right, thick):
        seg = "━" if thick else "─"
        # intra-box separator: continuous on thick lines, ┼ on thin lines
        midcell = "━" if thick else "┼"
        parts = []
        for c in range(n_cols):
            parts.append(seg * 3)
            if c < n_cols - 1:
                parts.append(boxsep if (c + 1) % bw == 0 else midcell)
        return left + "".join(parts) + right

    uni = [hline("┏", "┳", "┓", True)]
    for r in range(n_rows):
        row = "┃"
        for c in range(n_cols):
            row += ucell(r, c)
            row += "┃" if (c + 1) % bw == 0 else "│"
        uni.append(row)
        if r < n_rows - 1:
            if (r + 1) % bh == 0:
                uni.append(hline("┣", "╋", "┫", True))
            else:
                uni.append(hline("┃", "┃", "┃", False))
    uni.append(hline("┗", "┻", "┛", True))

    # --- ascii view (kept) ---
    ascii_rows = []
    for r in range(n_rows):
        ascii_rows.append("|" + "|".join(cell(r, c) for c in range(n_cols)) + "|")
    head = "+" + "+".join(["---"] * n_cols) + "+"
    ascii_block = [head] + sum(([ln, head] for ln in ascii_rows), [])
    return uni + [""] + ascii_block


def render_wend(puz):
    """Wend: grid=[[letter|'.'(hole)]]. Holes shown as '#'.
    Solution words are listed below the grid when present (they only exist in
    reveal-captured JSON; tbp pre-reveal captures omit the key)."""
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
    out = [head] + sum(([ln, head] for ln in rows), [])
    words = puz.get("words")
    if words:
        out.append("")
        out.append("Words:")
        for w in words:
            out.append(f"  {w}")
    return out


def render_patches(puz):
    """Patches: clues=[{x=col, y=row, type, size}]. Each cell = 2 chars:
    shape glyph + size digit (space when size is null)."""
    GLYPH = {"free": "╋", "square": "◼", "H_rect": "▬", "V_rect": "▌"}
    n_cols, n_rows = puz["grid_size"]
    # cell -> (glyph, size-or-space)
    mark = {}
    for cl in puz.get("clues", []):
        c, r = cl["x"], cl["y"]          # 0-indexed x=col, y=row
        glyph = GLYPH.get(cl["type"], "?")
        size = cl.get("size")
        mark[(r, c)] = glyph + (str(size) if size is not None else " ")
    rows = []
    for r in range(n_rows):
        row = []
        for c in range(n_cols):
            v = mark.get((r, c), "..")
            row.append(f" {v} ")
        rows.append("|" + "|".join(row) + "|")
    head = "+" + "+".join(["----"] * n_cols) + "+"
    return [head] + sum(([ln, head] for ln in rows), [])


def render_pinpoint(puz):
    """Pinpoint: 5 clue words + the revealed category/answer phrase.

    No grid -- render the clues as an ordered list and the answer below.
    """
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


def render_crossclimb(puz):
    """Crossclimb: no grid — the answer is the solved 7-word ladder, top→bottom.
    The 5 middle clues are captured during the reveal (before the reorder), so
    they are NOT reliably aligned to a solved row; show them as a separate
    block alongside the shared top/bottom phrase (clue key 0)."""
    clues = {int(k): v for k, v in puz.get("clues", {}).items()}
    words = {int(k): v for k, v in puz.get("words", {}).items()}
    out = []
    # The ladder is the definitive answer — word per board row (1=top .. 7=bottom)
    for row in range(1, 8):
        out.append(f"  {words.get(row, '?'):<8}")
    # Clues: 1..5 are the middle rows (reveal-captured), 0 is the shared phrase
    middles = [clues[k] for k in sorted(clues) if k != 0]
    if middles:
        out.append("")
        out.append("Clues (middle rows):")
        for c in middles:
            out.append(f"  - {c}")
    if clues.get(0):
        out.append("")
        out.append(f"Phrase (top+bottom): {clues[0]}")
    return out


RENDERERS = {
    "zip": render_zip,
    "tango": render_tango,
    "queens": render_queens,
    "minisudoku": render_minisudoku,
    "wend": render_wend,
    "patches": render_patches,
    "pinpoint": render_pinpoint,
    "crossclimb": render_crossclimb,
}


def show(puz, path, verbose):
    g = puz["game"]
    print(f"=== {os.path.basename(path)} ===")
    print(f"game      : {g}")
    print(f"number    : {puz.get('number')}")
    print(f"date      : {puz.get('date')}")
    gs = puz.get("grid_size")
    print(f"grid_size : {gs}  (cols x rows)" if isinstance(gs, (list, tuple)) else "grid_size : — (no grid)")
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
        if puz.get("words"):
            print(f"words     : {len(puz['words'])}")
    elif g == "patches":
        types = {}
        for cl in puz.get("clues", []):
            types[cl["type"]] = types.get(cl["type"], 0) + 1
        print(f"clues    : {len(puz.get('clues', []))}  {types}")
    elif g == "pinpoint":
        print(f"clues    : {len(puz.get('clues', []))}")
        print(f"blanks   : {puz.get('blanks')}")
        print(f"answer   : {puz.get('answer')}")
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
            "patches": "cell = shape+size (space if null); ╋=free ◼=square ▬=H-rect ▌=V-rect, .. = empty",
            "pinpoint": "clues lead to one shared category; answer = the revealed category phrase",
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
