# Pinpoint & Crossclimb Extractors — Implementation Plan

> **Status:** planning. Both games require *playing to completion* to reveal
> the data we need — unlike the grid games (zip/tango/queens/minisudoku) whose
> full board is server-rendered in the static DOM. Headless guest `--dump-dom`
> only yields a placeholder shell; the clues/letters/words arrive via async XHR
> after the user interacts. So these two need a **driven browser session**
> (real Chromium via CDP, or an authenticated cache), not just a DOM dump.

**Goal:** Emit `outputs/<date>/pinpoint.json` and `outputs/<date>/crossclimb.json`
in the project's standard format:
`{game, number, date, ...game-specific fields}`.

---

## Why the grid approach fails here

| Game | What static DOM has | What's missing | How to reveal |
|---|---|---|---|
| pinpoint | 5 empty clue-card slots (`Class` placeholder) | the 5 category clues + the answer | guess wrong 5× → game ends → all clues + answer revealed |
| crossclimb | empty ladder rows + shell | middle-row words, top/bottom words, per-row hints, correct order | fill every row via "Reveal line", then order rows, then reveal top+bottom |

Both fetch their real state via async XHR that only fires inside an interactive
(non-`--dump-dom`) browser. Use `render_cdp.py`-style CDP driving (Chrome
DevTools Protocol over websocket) — the scaffold already exists in `src/`.

---

## Target output schemas

### pinpoint.json
```json
{
  "game": "pinpoint",
  "number": 123,
  "date": "2026-07-12",
  "answer": "THINGS THAT ARE ROUND",
  "clues": [
    {"order": 1, "text": "Wheel"},
    {"order": 2, "text": "Coin"},
    {"order": 3, "text": "Pizza"},
    {"order": 4, "text": "Moon"},
    {"order": 5, "text": "Clock"}
  ]
}
```
- `clues` in the order Pinpoint reveals them (1 = hardest / first shown).
- `answer` = the category string revealed at the end.

### crossclimb.json
```json
{
  "game": "crossclimb",
  "number": 123,
  "date": "2026-07-12",
  "rows": [
    {"order": 1, "word": "COLD", "hint": "Not hot"},
    {"order": 2, "word": "GOLD", "hint": "Precious metal"},
    {"order": 3, "word": "GOLF", "hint": "..." }
  ],
  "top":    {"word": "WARM", "hint": "..."},
  "bottom": {"word": "FIRE", "hint": "..."}
}
```
- `rows` are the middle ladder rungs in their **correct final order**
  (each differs from its neighbour by one letter).
- `top` / `bottom` are the two capstone words revealed only after the middle
  rows are correctly filled AND ordered.

---

## Tasks

### Task 1 — Pinpoint auto-solver-to-reveal driver
1. Launch CDP-driven Chromium (reuse `render_cdp.py` websocket plumbing),
   navigate to `https://www.linkedin.com/games/pinpoint`, click "Start".
2. Wait for the guess input to mount. Submit 5 deliberately-wrong guesses
   (any junk string) to exhaust attempts and trigger the end screen.
   - Between guesses, wait for the next clue card to flip/reveal
     (poll for the clue text node to become non-placeholder).
3. On the end screen, scrape:
   - the 5 clue texts (in reveal order),
   - the category answer string.
4. Capture the puzzle `number` from the start/end screen if present
   (best-effort; may be null like the grid games).
5. Write `outputs/<date>/pinpoint.json`. Cache the final rendered DOM to
   `cache/<date>/pinpoint.html` for offline re-parsing.

**Pitfalls:** clue cards load async → never parse before the reveal animation
settles; use an explicit "text is non-empty and != placeholder" wait, not a
fixed sleep. The end-screen answer may live in a modal/toast, not the board.

### Task 2 — Crossclimb auto-reveal driver
1. CDP navigate to `https://www.linkedin.com/games/crossclimb`, click "Start".
2. For each middle ladder row: click **"Reveal line"** repeatedly until the
   row's correct word is filled. Scrape each row's `word` + its `hint`
   (the clue shown beside/above the active row).
3. **Ordering:** the rows come pre-scrambled; the win condition requires them
   sorted so each adjacent pair differs by exactly one letter. Two options:
   - (a) Read the game's own "correct order" if the reveal exposes it, OR
   - (b) Compute it ourselves: build a graph over the revealed words with an
     edge between words at Hamming distance 1 (same length), then find the
     Hamming path — that ordering is the solution. Drag/drop rows into that
     order via CDP to trigger the top/bottom reveal.
4. Once the middle is correct+ordered, the **top** and **bottom** words +
   hints unlock — scrape them.
5. Capture `number` best-effort. Write `outputs/<date>/crossclimb.json` and
   cache the DOM to `cache/<date>/crossclimb.html`.

**Pitfalls:** "Reveal line" only reveals the *active* row — must select each
row first. Drag/drop over CDP is fiddly; prefer computing the Hamming path and
issuing the minimum reorder moves. The one-letter-diff graph is a simple path
(each internal node has degree 2), so the path is unique up to reversal —
orient it using top/bottom hint semantics or accept either direction and let
the game confirm.

### Task 3 — Wire into scrape_games.py + view_json.py
1. Add `pinpoint` / `crossclimb` entries to `EXTRACTORS` that (when a
   populated cache exists) parse `cache/<date>/<game>.html` into the schemas
   above — so re-processing is offline and doesn't re-drive the browser.
2. Add renderers to `view_json.py`:
   - pinpoint: numbered clue list + answer line.
   - crossclimb: the ladder (top → middle rows → bottom) with hints.
3. Extend `KNOWN` in `view_json.py` so `all --date` includes them.

---

## Dependencies / environment
- `websocket-client` (already installed) for CDP.
- Real (non-headless-`--dump-dom`) Chromium session; `render_cdp.py` is flaky
  per project notes — budget time to stabilise navigation (old `--headless`,
  not `--headless=new`, was more reliable for pinpoint).
- No LinkedIn login strictly required for pinpoint/crossclimb guest play, but
  a session cookie makes the async fetches more reliable — supply `li_at` /
  `JSESSIONID`+`csrfToken` if guest play stalls.

## Definition of done
- `python3 src/scrape_games.py --games pinpoint,crossclimb --date <today>`
  produces both JSONs in the schemas above with real clue/word/hint data.
- `python3 src/view_json.py all --date <today>` renders all 6 games.
- Offline re-parse from `cache/<date>/*.html` reproduces identical JSON.
