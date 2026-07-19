#!/usr/bin/env python3
"""crossclimb scraper -- Playwright capture + live solve + drag reorder.

capture() returns a DICT (not html): the solved 7-word ladder and the clues,
read live from the browser via page.input_value() (Ember-set DOM *property*,
which page.content() / BeautifulSoup cannot see). The board HTML is only saved
when --save-html is set, for debugging.
"""
from itertools import permutations
import re
from playwright.sync_api import Page
from games import common as _c


def capture(page: Page, date_str, save_html=False):
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
        h, d = source.locator(".crossclimb__guess-dragger__left").bounding_box(), \
               target.bounding_box()
        sx, sy = h["x"] + h["width"] / 2, h["y"] + h["height"] / 2
        tx, ty = d["x"] + d["width"] / 2, d["y"] + d["height"] / 2
        page.mouse.move(sx, sy)
        page.mouse.down()
        page.mouse.move(sx, sy + 6)               # nudge past drag-start threshold
        page.wait_for_timeout(120)
        over = ty + (ty - sy) / abs(ty - sy) * d["height"] * 0.4 if ty != sy else ty
        for s in range(1, 21):                    # paced steps; overshoot midpoint
            page.mouse.move(sx + (tx - sx) * s / 20, sy + (over - sy) * s / 20)
            page.wait_for_timeout(20)
        page.wait_for_timeout(120)
        page.mouse.up()
        page.wait_for_timeout(200)

    def reorder(target_order, max_passes=6):
        """Drag the middle rows into `target_order`. A single insert can land
        one slot off, so re-read, fix the first wrong slot, repeat until correct.
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

    page.goto("https://www.linkedin.com/games/view/crossclimb/desktop",
              wait_until="domcontentloaded")
    page.get_by_text("Start game").first.click()
    page.get_by_label("Dismiss").click()
    page.wait_for_selector("div.crossclimb__grid")
    for i in range(1, 6):
        game["clues"][i] = page.locator(f"#crossclimb-clue-section-{i}").inner_text()
        page.get_by_text("Reveal row").first.click()

    game["words"] = read_words()

    for perm in permutations(game["words"].values()):
        if all(sum(x != y for x, y in zip(perm[i], perm[i + 1])) == 1
               for i in range(len(perm) - 1)):
            reorder(list(perm))

    page.wait_for_timeout(2000)

    # the last two rows (top + bottom) unlock once the ladder is correct;
    # their clue is a single shared two-word-phrase clue (id 0)
    game["clues"][0] = page.locator("#crossclimb-clue-section-0").inner_text()
    for _ in range(2):
        page.get_by_text("Reveal row").first.click()

    game["words"] = read_words()

    # Capture the board HTML for debugging only.
    if save_html:
        _c.save_html(date_str, "crossclimb", page.content())

    return game
