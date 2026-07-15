#!/usr/bin/env python3
"""Single capture strategy for ALL LinkedIn Games: drive the real browser via
Termux Browser Pilot (tbp) and dump each game's board HTML to
cache/<today>/<game>.html.

This is the ONLY way we fetch HTML now -- the headless --dump-dom path
(src/scrape_games.py) is retired for capture (its extractors can still read
these cached HTMLs). Some games auto-mount their board on page load; others
need the "Iniciar jogo" start button clicked first (in a retry loop, because
the transition is flaky). The puzzle number is grabbed from the start screen.

Games handled:
  * zip, tango, queens, minisudoku  -- board auto-mounts (no click needed)
  * wend, patches                   -- click "Iniciar jogo" to mount board
  * pinpoint, crossclimb            -- DEFERRED (see note at bottom of file)

No CLI arguments: date = today, every game is captured, tries = 12.

Usage:
  python3 src/tbp_capture.py
"""
import os, sys, json, asyncio, re
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "..", "termux-browser-pilot"))
from src.client import send_command

# All eight games. Pinpoint/Crossclimb are kept here for documentation but are
# skipped at capture time (DEFERRED -- see bottom of file).
GAMES = ["zip", "tango", "queens", "minisudoku",
         "wend", "patches",
         # "pinpoint", "crossclimb",   # DEFERRED: need in-game reveal buttons
         ]

URL = {
    # Grid games render their board inside an <iframe src="/games/view/<slug>/desktop">,
    # so we navigate the browser straight to that URL (board ends up in the top
    # document, no iframe switching needed).
    "zip": "https://www.linkedin.com/games/view/zip/desktop",
    "tango": "https://www.linkedin.com/games/view/tango/desktop",
    "queens": "https://www.linkedin.com/games/view/queens/desktop",
    "minisudoku": "https://www.linkedin.com/games/view/minisudoku/desktop",
    # wend / patches render the board directly in the top document (after the
    # "Iniciar jogo" click).
    "wend": "https://www.linkedin.com/games/wend",
    "patches": "https://www.linkedin.com/games/patches",
    # "pinpoint": "https://www.linkedin.com/games/pinpoint",
    # "crossclimb": "https://www.linkedin.com/games/view/crossclimb/desktop",
}

START_TEXTS = ["Iniciar jogo", "Start game"]  # PT-BR or EN (locale varies)

# Board marker per game: a CSS selector that is only present once the board has
# mounted. All grid games use data-cell-idx; wend/patches use a data-testid.
BOARD_MARK = {
    "zip": 'div[data-cell-idx]',
    "tango": 'div[data-cell-idx]',
    "queens": 'div[data-cell-idx]',
    "minisudoku": 'div[data-cell-idx]',
    "wend": 'div[data-testid="wend-game-board"]',
    "patches": 'div[data-testid="patches-game-board"]',
    # "pinpoint": 'div.pinpoint__board',     # DEFERRED
    # "crossclimb": 'div.crossclimb__grid',  # DEFERRED
}

TRIES = 12


async def find_start_selector():
    """Return a CSS selector for the start button ("Iniciar jogo" / "Start game"),
    or None. Prefer the element whose own text is one of the start strings (the
    <a>/<button>), not an ancestor like <main id=workspace> that also matches.
    """
    candidates = []
    for text in START_TEXTS:
        res = await send_command("find", {"text": text})
        if not res.get("success"):
            continue
        data = res.get("data") or {}
        items = data.get("elements") if isinstance(data, dict) else None
        if not items:
            items = data if isinstance(data, list) else []
        for it in items:
            if not isinstance(it, dict):
                continue
            sel = it.get("selector")
            if not sel:
                continue
            txt = (it.get("text") or "").strip()
            tag = (it.get("tag") or "").lower()
            if txt in START_TEXTS and tag in ("a", "button"):
                return sel                       # exact match wins
            if any(s.lower() in txt.lower() for s in START_TEXTS) \
                    and tag in ("a", "button"):
                candidates.append(sel)
    return candidates[0] if candidates else None


async def board_present(game):
    mark = BOARD_MARK.get(game)
    if not mark:
        return None
    res = await send_command("eval", {
        "expression": f"!!document.querySelector({mark!r})"})
    return (res.get("data") or {}).get("result", False) if res.get("success") else None


async def capture(game, date_str):
    """Capture one game's board HTML + puzzle number into the cache."""
    out = os.path.join(ROOT, "cache", date_str, f"{game}.html")
    meta = os.path.join(ROOT, "cache", date_str, f"{game}_meta.json")
    await send_command("goto", {"url": URL[game]})
    await asyncio.sleep(2.5)

    # --- capture puzzle number (before clicking in, where applicable) ---
    # Sources differ per game:
    #   * wend / patches : "NO.36" / "Junte tudo 119" on the start screen text
    #   * zip / tango / queens : "NO.483" inside the launch-footer of the
    #     /games/view/<slug>/desktop board page (in innerHTML, not always text)
    #   * minisudoku : number is fetched via a voyager API that 401s without a
    #     session -> NOT in the unauthenticated HTML -> left as null
    txt = await send_command("eval", {"expression": "document.body.innerText"})
    t = (txt.get("data") or {}).get("result", "") if txt.get("success") else ""
    html = await send_command("eval", {"expression": "document.body.innerHTML"})
    h = (html.get("data") or {}).get("result", "") if html.get("success") else ""
    hay = f"{t}\n{h}"
    number = None
    if game == "minisudoku":
        # Mini-sudoku's number is served by a voyager API that 401s without a
        # session, so it is never in the unauthenticated HTML -> always null.
        pass
    else:
        m = re.search(r"(?:Junte tudo|n[º°]|NO\.)\s*(\d+)", hay, re.IGNORECASE)
        if m:
            number = int(m.group(1))
        else:
            lines = [l.strip() for l in (t or "").splitlines() if l.strip()]
            for st in START_TEXTS:           # start button precedes the number
                if st in lines:
                    i = lines.index(st)
                    if i > 0 and lines[i - 1].isdigit():
                        number = int(lines[i - 1])
                        break
    # always write the meta (number may legitimately be null, e.g. minisudoku)
    os.makedirs(os.path.dirname(meta), exist_ok=True)
    json.dump({"number": number}, open(meta, "w"))

    # --- mount the board (auto-mount games pass on the first check) ---
    for i in range(TRIES):
        if await board_present(game):
            html = await send_command("eval",
                                      {"expression": "document.body.innerHTML"})
            h = (html.get("data") or {}).get("result", "")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w", encoding="utf-8").write(h)
            return {"game": game, "mounted_on_try": i, "bytes": len(h)}
        sel = await find_start_selector()
        if sel:
            await send_command("click", {"target": sel})
        await asyncio.sleep(3)
    return {"game": game, "failed": True, "tries": TRIES}


async def main():
    date_str = date.today().strftime("%Y-%m-%d")
    for g in GAMES:
        r = await capture(g, date_str)
        print(json.dumps(r), flush=True)


if __name__ == "__main__":
    asyncio.run(main())


# ============================================================================
# DEFERRED: pinpoint and crossclimb
# ----------------------------------------------------------------------------
# These two games fetch their board content from LinkedIn's voyager API after
# the game starts, and the content only renders after using the in-game
# "reveal" buttons -- a plain "Iniciar jogo" click is not enough. They are left
# in GAMES/URL/BOARD_MARK above (commented) so the wiring is ready; to enable
# them, uncomment the three lines for each and add a reveal-button step inside
# capture() (click each reveal control, then dump). Not implemented yet.
# ============================================================================
