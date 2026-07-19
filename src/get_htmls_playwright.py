#!/usr/bin/env python3
"""LinkedIn Games capture via Playwright (PC; DEBUG TARGET).

Plain, synchronous Playwright -- no tbp, no GetGame wrapper, no asyncio, no
login, no sleeps, no explicit timeouts. Playwright's locators auto-wait, so we
just navigate / click / wait_for_selector and read page.content().

One explicit function per game; game-specific logic stays local to each
function (no generic loop). The puzzle number is date-math (GAME_NUMBER_ANCHOR
+ game_number) -- never scraped.

The page locale is forced to English, so the start button is always
"Start game" (no PT/EN branching).

Run on your PC:
    pip install playwright && playwright install chromium
    python3 src/get_htmls_playwright.py                  # all games
    python3 src/get_htmls_playwright.py --games zip,pinpoint,crossclimb
    python3 src/get_htmls_playwright.py --headless       # no window
"""
import os
import re
import json
import argparse
from datetime import date
from itertools import permutations

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACHE = os.path.join(ROOT, "cache")


def save_html(game, html):
    today = date.today().strftime("%Y-%m-%d")
    os.makedirs(os.path.join(CACHE, today), exist_ok=True)
    print(os.path.join(CACHE, today, f"{game}.html"))
    with open(os.path.join(CACHE, today, f"{game}.html"), "w", encoding="utf-8") as f:
        f.write(html or "")


def save_json(game, data):
    """Write a puzzle's extracted answer to outputs/<date>/<game>.json.
    Used by games that have no HTML page to cache (e.g. crossclimb, which is
    solved live in-browser). Shape mirrors what view_json.py's show() expects:
    game, number, date, plus game-specific fields."""
    today = date.today().strftime("%Y-%m-%d")
    os.makedirs(os.path.join(ROOT, "outputs", today), exist_ok=True)
    out = os.path.join(ROOT, "outputs", today, f"{game}.json")
    print(out)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Per-game capture (kept explicit on purpose -- game-specific logic stays here)
# ---------------------------------------------------------------------------

def _zip(page):
    page.goto("https://www.linkedin.com/games/view/zip/desktop", wait_until="domcontentloaded")
    save_html("zip", page.content())


def tango(page):
    page.goto("https://www.linkedin.com/games/view/tango/desktop", wait_until="domcontentloaded")
    # page.wait_for_selector("div[data-cell-idx]")
    save_html("tango", page.content())


def queens(page):
    page.goto("https://www.linkedin.com/games/view/queens/desktop", wait_until="domcontentloaded")
    # page.wait_for_selector("div[data-cell-idx]")
    save_html("queens", page.content())


def mini_sudoku(page):
    page.goto("https://www.linkedin.com/games/view/mini-sudoku/desktop", wait_until="domcontentloaded")
    # page.wait_for_selector("div[data-cell-idx]")
    save_html("mini-sudoku", page.content())


def patches(page):
    page.goto("https://www.linkedin.com/games/patches", wait_until="domcontentloaded")
    page.get_by_text("Start game").first.click()
    page.wait_for_selector('div[data-testid="patches-game-board"]')
    save_html("patches", page.content())


def wend(page):
    page.goto("https://www.linkedin.com/games/wend", wait_until="domcontentloaded")
    page.get_by_text(re.compile(r"Start game|Iniciar jogo")).first.click()
    page.wait_for_selector('div[data-testid="wend-game-board"]')
    words = page.locator("[data-testid^=wend-word-list-slot-]").all()
    for _ in range(len(words)):
        page.get_by_text(re.compile(r"Hint|Dica")).first.click()
    save_html("wend", page.content())


def pinpoint(page):
    page.goto("https://www.linkedin.com/games/view/pinpoint/desktop", wait_until="domcontentloaded")
    page.get_by_text("Start game").first.click()
    page.wait_for_selector("div.pinpoint__board")
    for _ in range(5):
        page.fill(".pinpoint__input", "_")
        page.press(".pinpoint__input", "Enter")
    page.wait_for_selector(".pinpoint__card__answer_text")
    save_html("pinpoint", page.content())


def crossclimb(page):
    def read_words():
        letters = {}
        for e in page.locator("input[data-crossclimb-guess-input-idx]").all():
            row = int(re.search(r"row (\d+)", e.get_attribute("aria-label"))[1])
            idx = int(e.get_attribute("data-crossclimb-guess-input-idx"))
            letters.setdefault(row, {})[idx] = e.input_value()
        return {r: "".join(c[i] for i in sorted(c)) for r, c in letters.items()}

    def middle_rows():
        return [(r, "".join(c.input_value() for c in
                r.locator("input[data-crossclimb-guess-input-idx]").all()))
                for r in page.locator(".crossclimb__guess--middle").all()]

    def drag(source, target):
        h, d = source.locator(".crossclimb__guess-dragger__left").bounding_box(), target.bounding_box()
        sx, sy = h["x"] + h["width"] / 2, h["y"] + h["height"] / 2
        tx, ty = d["x"] + d["width"] / 2, d["y"] + d["height"] / 2
        page.mouse.move(sx, sy)
        page.mouse.down()
        page.mouse.move(sx, sy + 6)               # nudge past the drag-start threshold
        page.wait_for_timeout(120)
        over = ty + (ty - sy) / abs(ty - sy) * d["height"] * 0.4 if ty != sy else ty
        for s in range(1, 21):                    # paced steps; overshoot the midpoint
            page.mouse.move(sx + (tx - sx) * s / 20, sy + (over - sy) * s / 20)
            page.wait_for_timeout(20)
        page.wait_for_timeout(120)
        page.mouse.up()
        page.wait_for_timeout(200)

    def reorder(target_order, max_passes=6):
        """Drag the middle rows into `target_order`. A single insert can land one
        slot off, so re-read, fix the first wrong slot, repeat until correct.
        Raises if still wrong (don't reveal a wrong board)."""
        for _ in range(max_passes):
            rows = middle_rows()
            words = [w for _, w in rows]
            if words == target_order or words == target_order[::-1]:
                return
            want = next(w for slot, w in enumerate(target_order) if words[slot] != w)
            src = next(r for r, w in rows if w == want)
            tgt = rows[next(i for i, w in enumerate(words) if w != target_order[i])][0]
            drag(src, tgt)
        words = [w for _, w in middle_rows()]
        if words != target_order:
            raise RuntimeError(f"reorder failed: got {words}, wanted {target_order}")

    game = {"clues": {}, "words": {}}

    page.goto("https://www.linkedin.com/games/view/crossclimb/desktop", wait_until="domcontentloaded")
    page.get_by_text("Start game").first.click()
    page.get_by_label("Dismiss").click()
    page.wait_for_selector("div.crossclimb__grid")
    for i in range(1, 6):
        game["clues"][i] = page.locator(f"#crossclimb-clue-section-{i}").inner_text()
        page.get_by_text("Reveal row").first.click()

    game["words"] = read_words()

    for perm in permutations(game["words"].values()):
        if all(sum(x != y for x, y in zip(perm[i], perm[i + 1])) == 1 for i in range(len(perm) - 1)):
            reorder(list(perm))

    page.wait_for_timeout(2000)

    # the last two rows (top + bottom) unlock once the ladder is correct;
    # their clue is a single shared two-word-phrase clue (id 0)
    game["clues"][0] = page.locator("#crossclimb-clue-section-0").inner_text()
    for _ in range(2):
        page.get_by_text("Reveal row").first.click()

    game["words"] = read_words()
    game["game"] = "crossclimb"
    game["number"] = game_number("crossclimb")
    game["date"] = date.today().strftime("%Y-%m-%d")
    save_json("crossclimb", game)


# ---------------------------------------------------------------------------
# dispatch
# ---------------------------------------------------------------------------
CAPTURE = {
    "zip": _zip,
    "tango": tango,
    "queens": queens,
    "mini-sudoku": mini_sudoku,
    "patches": patches,
    "wend": wend,
    "pinpoint": pinpoint,
    "crossclimb": crossclimb,
}


def main(games, headless=False):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(locale="en-US")
        page = context.new_page()
        for g in games:
            print(f"--- {g} ---", flush=True)
            try:
                CAPTURE[g](page)
                print("  ok", flush=True)
            except Exception as e:
                print(f"  error: {e}", flush=True)
        browser.close()


# ---------------------------------------------------------------------------
# daily puzzle number (date math -- NOT scraped; matches get_htmls.py)
# ---------------------------------------------------------------------------
GAME_NUMBER_ANCHOR = {
    "zip": (date(2026, 7, 13), 483),
    "tango": (date(2026, 7, 13), 644),
    "queens": (date(2026, 7, 13), 804),
    "wend": (date(2026, 7, 13), 35),
    "patches": (date(2026, 7, 13), 118),
    "mini-sudoku": (date(2026, 7, 15), 338),
    "pinpoint": (date(2026, 7, 17), 487),   # verified from 2026-07-17 capture
    "crossclimb": (date(2026, 7, 17), 808),  # added by user
}


def game_number(game, d=None):
    """Daily puzzle number = anchor_number + days since the anchor date."""
    anchor = GAME_NUMBER_ANCHOR.get(game)
    if not anchor:
        return None
    base_date, base_num = anchor
    d = d or date.today()
    return base_num + (d - base_date).days


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--games", default=",".join(CAPTURE.keys()),
                        help="comma list; default = all")
    parser.add_argument("--headless", action="store_true",
                        help="run without a browser window")
    args = parser.parse_args()
    sel = [g.strip() for g in args.games.split(",") if g.strip()]
    sel = [g for g in sel if g in CAPTURE]
    main(sel, headless=args.headless)
