# AGENTS.md — LinkedIn Games Extractor (developer guide)

This file is the full source of truth for **developing and operating** this
project: architecture, conventions, the CI + local-posting pipeline, and every
pitfall hit during the build. The user-facing blurb lives in `README.md` — keep
that file short; put everything detailed here.

---

## 1. What the project is

A set of scripts that capture the **daily LinkedIn Games** puzzles into
per-day JSON so they can be inspected or replicated offline. All **eight**
games are implemented and captured with **Playwright** (runs on PC / CI, not on
Termux — see §7).

Games: `zip`, `tango`, `queens`, `minisudoku`, `patches`, `wend`, `pinpoint`,
`crossclimb`.

LinkedIn Games are **guest-launched** — no login, no session, no credentials.

---

## 2. Architecture

Per-game split. Each game is its own package under `games/<game>/`, with three
modules and **no shared game logic beyond `games/common.py`**:

```
games/<game>/
  scraper.py   # capture(page, date_str, save_html=False) -> raw
  parser.py    # parse(date_str, raw) -> dict  (writes outputs/<date>/<game>.json)
  renderer.py  # render(date_str, fmt="ascii"|"unicode") -> list[str]
```

- **scraper** drives the *real* browser (navigate, click "Start game", reveal,
  read live DOM/state) and returns **raw** board data. For 7/8 games `raw` is
  the page HTML **string**; for **crossclimb** it is a **dict**
  (`{words, clues}`) because the solved 7-word ladder is read live from the
  browser via `page.input_value()` after a real-mouse drag — it is not in the
  saved HTML.
- **parser** turns `raw` into the JSON dict and writes the file. The daily
  puzzle **number** is computed here by date-math (§5), never scraped.
- **renderer** reads the JSON (via `common.load`) and returns a **monospace
  block** as a `list[str]`. Each renderer also has an optional `_header(puz)`
  used when `--header` is passed to `render.py`.

### Dispatch (`games/__init__.py`)

No hard imports of the 8 games at module load — they're pulled on demand with
`importlib`, so `extract.py`/`render.py` stay light and a broken single game
doesn't break the others:

```python
GAMES = ("zip", "tango", "queens", "minisudoku",
         "patches", "wend", "pinpoint", "crossclimb")

def scraper(game):  return importlib.import_module(f"games.{game}.scraper")
def parser(game):   return importlib.import_module(f"games.{game}.parser")
def renderer(game): return importlib.import_module(f"games.{game}.renderer")
```

### `games/common.py` (shared helpers — NOT `_common`)

Renamed from `_common.py` to `common.py` on purpose (no leading underscore).
Every `games/**/*.py` imports it as `from games import common as _c`. It owns:
`today_str()`, `load(date_str, game)`, `save(date_str, game, data)`,
`save_html(date_str, game, html)`, path helpers (`OUT_DIR`, `CACHE_DIR`), and
the grid-parsing utilities. It has **no header logic** (that lives in each
renderer's `_header`).

> There are no `__init__.py` files inside `games/<game>/` — the packages are
> implicit namespace packages; only `games/__init__.py` exists (the dispatch
> table).

### Root entry points

- **`extract.py`** — capture + parse for **today only**. Launches one Chromium
  (locale `en-US`), runs every selected scraper, then every parser. Flags:
  - `--games zip,pinpoint,crossclimb` (default: all)
  - `--headless` (no browser window)
  - `--save-html` (also dump `cache/<date>/<game>.html` for debugging)
  - **No `--date`** — it always captures the current day. This is intentional.
- **`render.py <date> [<game>] [--header] [--format ascii|unicode]`** —
  reads `outputs/`, never the browser. `--header` adds the per-game summary;
  `--format` defaults to `unicode` for `queens`/`minisudoku`, else `ascii`.
  When more than one game is rendered, it prints a `### <game> #...` separator
  line before each (single game: no separator).

`extract.py` and `render.py` both inject the repo root onto `sys.path` so
`import games` works from anywhere.

---

## 3. Data flow (no HTML caching by default)

```
extract.py
  └─ for each game: scraper.capture(page, date, save_html)
        raw (html str | crossclimb dict)  ──in memory──▶  parser.parse(date, raw)
                                                        └─ writes outputs/<date>/<game>.json
```
`--save-html` is the *only* thing that writes `cache/`; the parser never reads
`cache/`. The 7 HTML-string scrapers hand their HTML straight to the parser;
the parser uses `BeautifulSoup` to read the board.

---

## 4. Capture strategy — one Playwright path, no login

- Plain **synchronous** Playwright (`playwright.sync_api`), `from playwright.sync_api import Page`.
- **No** `async`/`await`/`asyncio`, **no** `Capture`/`GetGame` wrapper classes,
  **no** `send_command`, **no** `storage_state`/`li_state`, **no** `input()`
  login prompts, **no** explicit `sleep`.
- Locale forced to English: `browser.new_context(locale="en-US")` — so all
  selectors / button text are English.
- Rely on Playwright auto-waiting; `wait_for_selector` is used only as a mount
  gate. The single deliberate exception: `page.wait_for_timeout(2000)` after the
  crossclimb drag (lets the reorder settle).
- **Board-mount rule**: some games only render their board **after** the
  landing button click — the grid is absent from the DOM on first load, so
  parsing fails with `no <prefix>-grid in DOM (board likely not mounted)`.
  Each affected scraper clicks its own landing button (locale-tolerant regex)
  and `wait_for_selector`s its grid *before* reading HTML, inlined in the
  scraper (no shared helper). Button text differs by game:
  - zip / tango / queens / patches / wend / pinpoint / crossclimb:
    "Start game" / "Iniciar jogo"
  - **minisudoku**: "Solve now" / "Resolver agora" (different label!)
  When adding a game, check the actual landing-button label; if the board
  isn't in the pre-click DOM, click that button then wait for the grid.
- **crossclimb** is the only game needing real interaction: a solver + real-mouse
  drag (`page.mouse`) + convergent reorder, all inlined in
  `games/crossclimb/scraper.py`. The 7-word ladder is read via
  `page.input_value()` after the drag, not from HTML.
- **pinpoint** needs a 5-guess "reveal" in the browser before the answer phrase
  is readable.

---

## 5. Daily number — per-game date-math anchors

Each `parser.py` computes the puzzle number itself from a local anchor
(`_ANCHOR_DATE` / `_ANCHOR_NUM`); there is **no** central `GAME_NUMBER_ANCHOR`.
Formula: `_ANCHOR_NUM + (date - _ANCHOR_DATE).days`. Never scraped.

| game        | `_ANCHOR_DATE` | `_ANCHOR_NUM` |
|-------------|----------------|---------------|
| zip         | 2026-07-13     | 483           |
| tango       | 2026-07-13     | 644           |
| queens      | 2026-07-13     | 804           |
| wend        | 2026-07-13     | 35            |
| patches     | 2026-07-13     | 118           |
| minisudoku  | 2026-07-15     | 338           |
| pinpoint    | 2026-07-17     | 487           |
| crossclimb  | 2026-07-17     | 808           |

Verified for 2026-07-19: zip 489, tango 650, queens 810, wend 41, patches 124,
minisudoku 342, pinpoint 489, crossclimb 810.

> If LinkedIn changes a game's numbering, only that one `parser.py` anchor
> changes — nothing else.

---

## 6. Output schema

`outputs/<YYYY-MM-DD>/<game>.json`. Every file shares:
`game`, `number` (date-math), `date`, `grid_size` (`[cols, rows]`).
Game-specific fields live in each `parser.py` (e.g. zip `nodes`/`walls`,
queens `regions`, wend `words`, pinpoint `clues`/`answer`, crossclimb
`ladder`/`clues`/`phrase`). `cache/` is gitignored; `outputs/` is committed by
CI (§8).

---

## 7. Environment limits & validation

- **Playwright cannot run on Termux** (no Chromium binary). All local validation
  is `py_compile` + import checks + `render.py` on already-captured JSON. The
  actual browser capture runs on PC or in CI.
- Python 3.13+ (CI uses 3.13). `pyproject.toml` pins `requires-python = ">=3.13"`.
- Dependencies: `playwright` **and** `beautifulsoup4` (bs4 is imported by the
  HTML parsers — easy to forget). `pyproject.toml` sets
  `[tool.setuptools] packages = ["games"]` — **required**, because setuptools'
  auto package-discovery chokes on the flat layout (`games` *and* `outputs`
  both look like top-level packages and it aborts the editable install).

---

## 8. CI — `.github/workflows/daily-games.yml`

Daily headless capture that **commits** the day's `outputs/`.

- **Trigger**: `cron: "17 5 * * *"` (05:17 UTC, after LinkedIn refreshes) +
  `workflow_dispatch` (manual run button).
- **Runner**: `ubuntu-latest`, Python 3.13.
- **Setup**: `pip install -e .` (pulls playwright + beautifulsoup4), then
  `playwright install --with-deps chromium`. The `ms-playwright` browser cache
  is restored from `actions/cache` keyed on `pyproject.toml`, so the ~150 MB
  download only re-runs when deps change.
- **Extract**: `python extract.py --headless` → writes `outputs/<today>/`.
- **Commit**: if `outputs/` changed, commits + pushes (needs
  `permissions: contents: write`; uses the built-in `GITHUB_TOKEN`).

First runs surfaced two real bugs that are now fixed:
1. `pip install -e .` failed on setuptools auto-discovery → `packages = ["games"]`.
2. `extract.py` still imported the old `games._common` after the rename to
   `common` → fixed to `from games import common as _common`.

---

## 9. Local daily posting — `daily_render.sh` + Hermes cron

CI commits; a **local Hermes cron** pulls and posts to Telegram.

- **Script**: `~/.hermes/scripts/daily_render.sh` (lives in the Hermes home,
  *not* in this repo). It: `cd` to the repo → `git pull --ff-only` → for each
  game renders `render.py <date> <game> --header` and posts it as its **own**
  Telegram message, wrapped in a **``` code block** for monospace.
- **Cron**: Hermes job `fa548c937b18` ("daily-games-8am"),
  `schedule: "0 8 * * *"`, `no_agent: true`, `deliver: local` (the script does
  its own sending). `script: daily_render.sh`.
- **Target**: `telegram:-1004403987384:3` (the games forum topic).
- **Sending**: via `hermes send --to <target>` — reuses the gateway's Telegram
  credentials, **no bot token in the script**. `hermes send` emits MarkdownV2
  and **protects fenced code blocks**, so the ``` wrapper renders as a clean
  monospace block (grid `#`/`=`/`-`/`|` chars are literal inside the fence).
- **Failure policy (explicit, never silent)**:
  - missing `outputs/<date>/<game>.json` → posts
    `ERROR: ... is MISSING -- the daily CI extract likely failed for <game>.`
  - `render.py` crash → posts the error + captured output.
  - `git pull` failure → posts `ERROR: git pull failed...`.
  - any failure → script exits `1` so the cron shows non-ok.

> Earlier design "skipped missing games with a `[skip]` note" — **rejected**;
> the user wants a visible error to investigate.

---

## 10. Git layout & conventions

- **Branches**: `master` = this Playwright-only flow (current, pushed to
  `origin`). `termux-pilot-browser` = the legacy Termux Browser Pilot (tbp)
  capture flow, preserved untouched for reference. Don't merge tbp back.
- **Remote**: `origin` = `Loukis-13/linkedin-games-archive`.
- **Commits**: `outputs/` is committed by CI; `cache/` is gitignored.
- **NEVER `git commit`/`git push` without explicit user approval** — even for
  obvious fixes or a clean tree. Present the diff/plan and wait for a go-ahead.
- **Dates** in file paths: `outputs/<YYYY-MM-DD>/`. Daily puzzles change each
  day; always capture the target day (today via `extract.py`).
- **Coordinates**: Patches `x`/`y` are 0-indexed (x = column, y = row). Queens /
  miniSudoku use `board[row][col]`. Zip nodes use `row`/`col`. Wend uses
  `grid[row][col]`.
- **Locale**: forced `en-US` in the Playwright context.

---

## 11. Adding a new game

1. `mkdir games/<newgame>`; add `scraper.py`, `parser.py`, `renderer.py`.
2. `scraper.capture(page, date_str, save_html=False)` → return `raw`
   (HTML str, or a dict if the data isn't in HTML).
3. `parser.parse(date_str, raw)` → compute number from a local
   `_ANCHOR_DATE`/`_ANCHOR_NUM`, build the dict, `common.save(date_str, game, d)`.
4. `renderer.render(date_str, fmt=...)` → `list[str]` monospace block; add
   `_header(puz)` if it has a summary.
5. Add `<newgame>` to `GAMES` in `games/__init__.py`.
6. Validate locally: `python -m py_compile games/<newgame>/*.py` and
   `python render.py <date> <newgame> --header` against a captured JSON.
7. Capture for real on PC/CI (`extract.py --games <newgame>`).

---

## 12. Quick command reference

```bash
# capture + parse today (writes outputs/<today>/<game>.json)
python extract.py
python extract.py --games zip,pinpoint,crossclimb
python extract.py --headless
python extract.py --save-html

# inspect (reads outputs/, not the browser)
python render.py 2026-07-19                 # every game that day
python render.py 2026-07-19 crossclimb      # one game
python render.py 2026-07-19 --header        # with per-game summary
python render.py 2026-07-19 --format ascii  # force ascii

# local daily posting (run by the Hermes cron, not by hand normally)
bash ~/.hermes/scripts/daily_render.sh
```
