#!/usr/bin/env python3
"""Shared plumbing for the per-game LinkedIn Games extractor.

Only cross-cutting concerns live here: paths, the optional HTML debug dump,
JSON output/read, and grid-parsing primitives shared by the board games
(zip / tango / queens / minisudoku). Game-specific display (the summary
header shown by `render.py --header`) lives in each game's renderer.
"""
import os
import re
import json
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))      # .../games
ROOT = os.path.dirname(HERE)                            # repo root
CACHE = os.path.join(ROOT, "cache")
OUT = os.path.join(ROOT, "outputs")


def today_str():
    return date.today().strftime("%Y-%m-%d")


def save_html(date_str, game, html):
    """Optionally dump a captured board DOM for debugging (--save-html)."""
    d = os.path.join(CACHE, date_str)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, f"{game}.html"), "w", encoding="utf-8") as f:
        f.write(html or "")


def write_json(date_str, game, data):
    out = os.path.join(OUT, date_str, f"{game}.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return out


def load(date_str, game):
    p = os.path.join(OUT, date_str, f"{game}.json")
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def start_game(page, gate):
    """Click 'Start game' (locale-tolerant) and wait for the board to mount.

    Used by games whose board only appears after the landing 'Start game'
    click. `gate` is the CSS selector for the mounted board (e.g. the grid div
    the parser expects). Without this click the board is never in the DOM and
    parse() raises "no <prefix>-grid in DOM (board likely not mounted)".
    """
    page.get_by_text(re.compile(r"Start game|Iniciar jogo")).first.click()
    page.wait_for_selector(gate)


# --------------------------------------------------------------------------
# Grid parsing primitives (zip / tango / queens / minisudoku share DOM shape)
# --------------------------------------------------------------------------
def find_grid(soup, prefix):
    g = soup.select_one(f'div[class*="{prefix}-grid"]')
    if g is None:
        cell = soup.select_one("div[data-cell-idx]")
        g = cell.parent if cell is not None else None
    if g is None:
        raise ValueError(f"{prefix}: no {prefix}-grid in DOM "
                         f"(board likely not mounted)")
    return g


def grid_dims(grid, ncells):
    m = re.search(r"--rows:\s*(\d+).*?--cols:\s*(\d+)", grid.get("style", ""))
    if m:
        return int(m.group(1)), int(m.group(2))
    n = int(round(ncells ** 0.5))
    return n, n


def dedupe_walls(walls):
    seen, out = set(), []
    for w in walls:
        a, b = w[0], w[1]
        key = tuple(sorted((tuple(a), tuple(b))))
        if key not in seen:
            seen.add(key)
            out.append(w)
    return out
