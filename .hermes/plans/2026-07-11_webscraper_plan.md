# LinkedIn Games Webscraper — Implementation Plan

> **For Hermes:** Use subagent-driven-development to implement task-by-task.

**Goal:** Extract the *authoritative game data* for all 8 LinkedIn games
(Zip, Tango, Queens, Pinpoint, Crossclimb, Mini Sudoku, Patches, Wend)
directly from LinkedIn's own game state, and write one JSON per game into a
per-day folder. This is the reliable, source-of-truth path for *future/daily*
extraction. The historical backlog (screen recordings) is handled by the
sibling **video pipeline** plan — both emit the SAME schema.

**Architecture:** A Playwright (or Browser-Use) driven browser logs into
linkedin.com/games, opens each game, and reads the game's underlying data
from either (a) the network XHR/JSON the page fetches, or (b) the DOM /
`window` game-state the client holds. No OCR/vision needed — we read the
real model. Results are normalized to a shared JSON schema and written to
`recordings_processed/<YYYY-MM-DD>/<game>.json`.

**Tech Stack:** Python3 + Playwright (Chromium). Termux-first attempt;
if Chromium won't run on-device, fall back to a Linux desktop. Optional:
Nous Browser-Use automation as an alternative host (no local Chromium).

**Runs where:** Termux device if Chromium installs; else the user's Linux box.
User authenticates to LinkedIn once (session cookie / manual login).

---

## Shared output schema (BOTH plans write this)

```
recordings_processed/<YYYY-MM-DD>/
  zip.json          {game:"zip", date, grid_size:[c,r], start:int,
                      nodes:[{id,row,col}], walls:[[r1,c1],[r2,c2]],
                      raw:<game-specific>}
  tango.json       {game:"tango", date, size:int, constraints:[...], raw:{}}
  queens.json      {game:"queens", date, size:int, regions:[...], raw:{}}
  pinpoint.json    {game:"pinpoint", date, clues:[...], raw:{}}
  crossclimb.json  {game:"crossclimb", date, puzzle:[...], raw:{}}
  minisudoku.json  {game:"minisudoku", date, grid:[9][9], raw:{}}
  patches.json     {game:"patches", date, board:[...], raw:{}}
  wend.json        {game:"wend", date, target:str, guesses:[...], raw:{}}
```
`date` = the day the game was PLAYED (for the scraper: today / the
auth'd session's current puzzle date; for the video plan: parsed from filename).
`raw` carries whatever game-specific fields we capture, so the schema can
grow without breaking consumers.

---

## Phase 0 — Recon (do FIRST, it de-risks everything)

### Task 0.1: Inspect how each game exposes its data
- Launch the browser against a logged-in LinkedIn games session.
- For EACH of the 8 games, open the game and capture:
  - the network requests (Playwright `page.on("response")`) — look for
    JSON endpoints like `*/games/graphql*` or `*/games-api/*`.
  - `page.evaluate(() => window.__GAME_STATE__ || window.game)` and any
    obvious global holding the puzzle model.
  - a trimmed DOM snapshot of the board container.
- Save findings to `notes/game_endpoints.md` (which game → which source).
- **Do not guess the schema** — derive it from what's actually there.
- Validation: `notes/game_endpoints.md` lists, per game, a concrete
  extraction path (XHR field OR DOM selector OR JS global).

### Task 0.2: Decide host & install
- Try `pip install playwright && playwright install chromium` on Termux.
- If Chromium fails to launch on-device: stop, tell user to run on Linux;
  the rest of the plan is host-agnostic (same code).
- Validation: a 3-line Playwright script opens `about:blank` and prints
  the browser version.

---

## Phase 1 — Scraper skeleton

### Task 1.1: Project layout + config
- Create: `src/scrape_games.py` (the runner).
- Create: `config/linkedin.json` = `{"games_base":"https://www.linkedin.com/games",
  "session_cookie":""}`. Cookie filled by user or by an interactive login
  step (Task 1.2).
- Create: `recordings_processed/` output root.
- Validation: `python3 src/scrape_games.py --help` prints usage.

### Task 1.2: Auth / session
- If `session_cookie` empty: launch a visible browser, navigate to
  LinkedIn, pause for manual login, then persist cookies to
  `config/cookies.json`.
- On later runs: load `config/cookies.json` and `context.add_cookies(...)`.
- Validation: after login, `page.goto(games_base)` shows the user's
  avatar / "Continue" — i.e. we are authenticated.

### Task 1.3: Per-game navigation + capture
- For each game in the 8: `page.goto(f"{games_base}/{slug}")`,
  wait for the board to render, then call the extraction for that game
  (Tasks 2.x). Wrap in try/except so one game failing doesn't abort all.
- Validation: running with `--dry-run` navigates all 8 and prints the
  captured raw model lengths, no file writes, no crashes.

---

## Phase 2 — Per-game extractors (one task each)

Each task: a function `extract_<game>(page, raw_capture) -> dict` returning
the normalized schema (with `raw` = the verbatim source). Ground the field
mapping in Task 0.1's findings — do NOT invent fields.

### Task 2.1: extract_zip
- Source: from Task 0.1 (XHR or DOM). Normalize to
  `grid_size, start, nodes[{id,row,col}], walls[[r1,c1],[r2,c2]]`.
- Validation: cross-check against the existing `extract_zip.py` image
  output for a known puzzle (same numbers).

### Task 2.2: extract_tango
### Task 2.3: extract_queens
### Task 2.4: extract_pinpoint
### Task 2.5: extract_crossclimb
### Task 2.6: extract_minisudoku
### Task 2.7: extract_patches
### Task 2.8: extract_wend

(Each: 2–5 min. Write the function from the real captured model;
validate that `normalize` produces a non-empty, schema-correct dict.)

---

## Phase 3 — Write + date

### Task 3.1: Output writer
- `write_day(date_str, game, data)`: `os.makedirs` the per-day folder,
  `json.dump` to `recordings_processed/<date>/<game>.json`.
- Validation: after a real run, `recordings_processed/<date>/` has 8 files,
  each valid JSON matching the schema.

### Task 3.2: CLI
- `python3 src/scrape_games.py [--date YYYY-MM-DD] [--games zip,tango,...]
  [--dry-run]`. Default date = today.
- Validation: `--dry-run --games zip` prints the zip model and writes nothing.

---

## Risks / tradeoffs
- **LinkedIn may require auth + anti-bot** — manual login (Task 1.2) is
  the pragmatic path; a full headless cookie farm is out of scope.
- **Game internals change** — Task 0.1 recon must be re-run if a game
  updates; `raw` field preserves verbatim data so re-parsing is possible
  without re-scraping.
- **Chromium on Termux is the main risk** — Phase 0.2 gates it; the
  Linux fallback keeps the plan viable.

## Validation summary
- Phase 0: `notes/game_endpoints.md` documents a real source per game.
- Phase 1: authenticated nav reaches all 8 boards.
- Phase 2: each extractor yields schema-correct JSON.
- Phase 3: a run populates `recordings_processed/<date>/` with 8 files
  matching the SHARED schema (consumable by the video plan too).
