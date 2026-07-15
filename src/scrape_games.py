#!/usr/bin/env python3
"""
scrape_games.py -- extract LinkedIn Games puzzle data, NO login, NO Playwright.

Renders each game's board headless with Chromium --dump-dom, then parses with
BeautifulSoup. No voyager/GraphQL, no cookies.

Output: outputs/<date>/<game>.json  (see OUTPUT FORMAT below)
Cache:  cache/<date>/<game>.html    (rendered DOM, reprocess offline)

OUTPUT FORMAT (new spec)
------------------------
zip:        {game, number, date, grid_size:[cols,rows],
             nodes:[{id,row,col}], walls:[[[r,c],[r,c]]]}
tango:      {game, number, date, grid_size,
             symbols:[[row,col,"M"|"S"]],
             walls:[[[r,c],[r,c],"="|"x"]]}      # divisors
queens:     {game, number, date, grid_size, board:[[region ids]]}
minisudoku: {game, number, date, grid_size, cells:[[digit|null]]}
wend:       {game, number, date, ...}   # data-testid="wend-game-board"
patches:    {game, number, date, ...}   # data-testid="patches-game-board"

Grid games (zip/tango/queens/minisudoku) share the same DOM shape; only the
CSS class PREFIX differs. Board cells carry data-cell-idx="N" (row-major).
Wend/Patches are plain HTML inside a data-testid="*-game-board" div, BUT the
board only mounts for an authenticated session -- headless guest renders a
~16KB shell. Those extractors work when fed a DOM that actually contains the
board div (real browser session / authenticated cache).
"""
import os, re, json, argparse, subprocess, shutil
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT_ROOT = os.path.join(ROOT, "outputs")
CACHE_ROOT = os.path.join(ROOT, "cache")

GAMES = ["zip", "tango", "queens", "pinpoint", "crossclimb",
         "minisudoku", "patches", "wend"]
SLUG = {
    "zip": "zip", "tango": "tango", "queens": "queens",
    "pinpoint": "pinpoint", "crossclimb": "crossclimb",
    "minisudoku": "mini-sudoku",
    "patches": "patches", "wend": "wend",
}
# grid games: (css prefix, content-class, kind)
GRID = {
    "zip":        ("trail",  "trail-cell-content",  "numbered"),
    "tango":      ("lotka",  "lotka-cell-content",  "symbol"),
    "queens":     ("queens", None,                  "queens"),
    "minisudoku": ("sudoku", "sudoku-cell-content", "sudoku"),
}


def cache_path(date_str, game):
    return os.path.join(CACHE_ROOT, date_str, f"{game}.html")


def chromium():
    for cand in ("chromium-browser", "chromium", "google-chrome", "chrome"):
        p = shutil.which(cand)
        if p:
            return p
    import glob
    hits = glob.glob("/data/data/com.termux/files/usr/lib/chromium/chromium*")
    if hits:
        return hits[0]
    raise SystemExit("ERROR: chromium not found on PATH. Install it first.")


def dump_dom(game, date_str, timeout=45, force=False):
    """Render the board to HTML; cache under cache/<date>/<game>.html."""
    cp = cache_path(date_str, game)
    if not force and os.path.exists(cp):
        with open(cp, encoding="utf-8", errors="replace") as f:
            return f.read()
    # patches/wend use /games/<slug>; grid games use /games/view/<slug>/desktop
    if game in ("patches", "wend"):
        url = f"https://www.linkedin.com/games/{SLUG[game]}"
    else:
        url = f"https://www.linkedin.com/games/view/{SLUG[game]}/desktop"
    out = subprocess.run(
        [chromium(), "--headless", "--no-sandbox", "--disable-gpu",
         f"--virtual-time-budget={timeout*1000}", "--dump-dom", url],
        capture_output=True, text=True, timeout=timeout + 30)
    if out.returncode == 0 and out.stdout.strip():
        os.makedirs(os.path.dirname(cp), exist_ok=True)
        with open(cp, "w", encoding="utf-8") as f:
            f.write(out.stdout)
    return out.stdout


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _soup(dom):
    from bs4 import BeautifulSoup
    return BeautifulSoup(dom, "html.parser")


def grid_dims(grid, ncells):
    """Read --rows/--cols from style; fall back to sqrt(ncells)."""
    m = re.search(r"--rows:\s*(\d+).*?--cols:\s*(\d+)", grid.get("style", ""))
    if m:
        return int(m.group(1)), int(m.group(2))
    n = int(round(ncells ** 0.5))
    return n, n


def find_grid(soup, prefix):
    # match any grid container whose class starts with the prefix, e.g.
    # trail-grid, lotka-grid, sudoku-grid, queens-grid-no-gap
    g = soup.select_one(f'div[class*="{prefix}-grid"]')
    if g is None:
        # fall back: the parent of the data-cell-idx cells
        cell = soup.select_one("div[data-cell-idx]")
        g = cell.parent if cell is not None else None
    if g is None:
        raise ValueError(f"{prefix}: no {prefix}-grid in DOM "
                         f"(board likely not mounted / needs auth)")
    return g


def extract_number(soup):
    """Best-effort daily puzzle number.

    The number appears on the board page for zip/tango/queens as e.g.
    "NO.483" (launch-footer score text) and is captured into the cached HTML
    by tbp_capture.py. Mini-sudoku's number comes from a voyager API that 401s
    without a session, so it is absent here -> returns None.
    """
    for el in soup.find_all(string=re.compile(r"(No\.?|N[ºo]|#)\s*\d{2,4}", re.IGNORECASE)):
        m = re.search(r"(\d{2,4})", el)
        if m:
            return int(m.group(1))
    return None


# --------------------------------------------------------------------------
# grid extractors
# --------------------------------------------------------------------------
def extract_zip(soup):
    g = find_grid(soup, "trail")
    cells = g.select("div[data-cell-idx]")
    rows, cols = grid_dims(g, len(cells))
    nodes, walls = [], []
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        cont = c.select_one(".trail-cell-content")
        txt = cont.get_text(strip=True) if cont else ""
        if txt.isdigit():
            nodes.append({"id": int(txt), "row": r, "col": col})
        for w in c.select('div[class*="trail-cell-wall"]'):
            cls = " ".join(w.get("class", []))
            if "trail-cell-wall--right" in cls and col + 1 < cols:
                walls.append([[r, col], [r, col + 1]])
            if "trail-cell-wall--down" in cls and r + 1 < rows:
                walls.append([[r, col], [r + 1, col]])
    walls = _dedupe_walls(walls)
    return {"grid_size": [cols, rows], "nodes": nodes, "walls": walls}


def extract_tango(soup):
    g = find_grid(soup, "lotka")
    cells = g.select("div[data-cell-idx]")
    rows, cols = grid_dims(g, len(cells))
    symbols, walls = [], []
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        cont = c.select_one(".lotka-cell-content")
        svg = cont.find("svg") if cont else None
        al = (svg.get("aria-label") if svg else "") or ""
        al = al.strip().lower()
        if al == "moon":
            symbols.append([r, col, "M"])
        elif al == "sun":
            symbols.append([r, col, "S"])
        # divisor edges (=/x) belong to this cell (right/down)
        for e in c.select("div.lotka-cell-edge"):
            ecls = " ".join(e.get("class", []))
            esvg = e.find("svg")
            sign = (esvg.get("aria-label") if esvg else "") or ""
            sign = sign.strip().lower()
            sym = "=" if sign == "equal" else ("x" if sign in ("cross", "multiply") else None)
            if sym is None:
                continue
            if "lotka-cell-edge--right" in ecls and col + 1 < cols:
                walls.append([[r, col], [r, col + 1], sym])
            if "lotka-cell-edge--down" in ecls and r + 1 < rows:
                walls.append([[r, col], [r + 1, col], sym])
    return {"grid_size": [cols, rows], "symbols": symbols, "walls": walls}


def extract_queens(soup):
    g = find_grid(soup, "queens")
    cells = g.select("div[data-cell-idx]")
    n = len(cells)
    rows, cols = grid_dims(g, n)
    board = [[None] * cols for _ in range(rows)]
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        region = None
        for cl in c.get("class", []):
            m = re.match(r"cell-color-(\d+)", cl)
            if m:
                region = int(m.group(1))
        board[r][col] = region
    # already-placed queens are intentionally ignored (board regions only)
    return {"grid_size": [cols, rows], "board": board}


def extract_minisudoku(soup):
    g = find_grid(soup, "sudoku")
    cells = g.select("div[data-cell-idx]")
    rows, cols = grid_dims(g, len(cells))
    board = [[None] * cols for _ in range(rows)]
    for c in cells:
        idx = int(c["data-cell-idx"])
        r, col = divmod(idx, cols)
        cont = c.select_one(".sudoku-cell-content")
        txt = cont.get_text(strip=True) if cont else ""
        board[r][col] = int(txt) if txt.isdigit() else None
    return {"grid_size": [cols, rows], "cells": board}


def _dedupe_walls(walls):
    seen, out = set(), []
    for w in walls:
        a, b = w[0], w[1]
        key = tuple(sorted((tuple(a), tuple(b))))
        if key not in seen:
            seen.add(key)
            out.append(w)
    return out


# --------------------------------------------------------------------------
# wend / patches (plain HTML board, mounts only with a real session)
# --------------------------------------------------------------------------
def _require_board(soup, testid, game):
    board = soup.find(attrs={"data-testid": testid})
    if board is None:
        raise ValueError(
            f"{game}: '{testid}' not in DOM. Board did not mount -- "
            f"headless guest renders a shell. Feed an authenticated/"
            f"real-browser DOM to cache/<date>/{game}.html and re-run.")
    return board


def extract_wend(soup):
    board = _require_board(soup, "wend-game-board", "wend")
    # Wend: a chain of words; capture visible rows/tiles generically.
    rows = []
    for row in board.select("[class*=row], [data-row]"):
        letters = [t.get_text(strip=True)
                   for t in row.select("[class*=tile], [class*=cell], [class*=letter]")]
        letters = [x for x in letters if x]
        if letters:
            rows.append(letters)
    return {"board": rows, "raw_html_len": len(str(board))}


def extract_patches(soup):
    board = _require_board(soup, "patches-game-board", "patches")
    # Patches: grid of colored patches; capture cell colors/labels generically.
    cells = []
    for c in board.select("[data-cell-idx],[class*=cell],[class*=patch]"):
        cells.append({
            "idx": c.get("data-cell-idx"),
            "label": (c.get("aria-label") or "").strip() or None,
            "classes": c.get("class", []),
        })
    return {"cells": cells, "raw_html_len": len(str(board))}


EXTRACTORS = {
    "zip": extract_zip,
    "tango": extract_tango,
    "queens": extract_queens,
    "minisudoku": extract_minisudoku,
    "wend": extract_wend,
    "patches": extract_patches,
}


# --------------------------------------------------------------------------
def process_game(game, date_str, force=False):
    if game not in EXTRACTORS:
        print(f"  [skip] {game}: extractor not implemented "
              f"(needs authenticated session to reveal answers)")
        return None
    print(f"  rendering {game} ...", flush=True)
    dom = dump_dom(game, date_str, force=force)
    soup = _soup(dom)
    fields = EXTRACTORS[game](soup)
    number = extract_number(soup)
    out = {"game": game, "number": number, "date": date_str}
    out.update(fields)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=date.today().strftime("%Y-%m-%d"))
    ap.add_argument("--games", default=",".join(GAMES))
    ap.add_argument("--outdir", default=OUT_ROOT)
    ap.add_argument("--force", action="store_true",
                    help="re-render even if cache exists")
    args = ap.parse_args()
    games = [g.strip() for g in args.games.split(",") if g.strip()]
    out_dir = os.path.join(args.outdir, args.date)
    os.makedirs(out_dir, exist_ok=True)
    print(f"Scraping {len(games)} game(s) for {args.date} -> {out_dir}")
    for g in games:
        try:
            data = process_game(g, args.date, force=args.force)
        except Exception as e:
            print(f"  [ERROR] {g}: {e}")
            continue
        if data is None:
            continue
        path = os.path.join(out_dir, f"{g}.json")
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"  wrote {path}")


if __name__ == "__main__":
    main()
