# LinkedIn Games Extractor

Extract the daily LinkedIn Games puzzle definitions into per-day JSON files so
the puzzles can be replicated offline. All **eight** games are implemented and
captured with **Playwright** (PC / CI).

> The legacy Termux Browser Pilot (tbp) capture flow lives on the
> `termux-pilot-browser` branch (kept for reference). This `master` branch is
> the Playwright-only flow.

## How it works

**One capture strategy: Playwright.** `extract.py` launches a single Chromium
(locale `en-US`) and, for each game, calls that game's `scraper.capture(page)`
to drive the real browser (navigate, click "Start game", reveal, read live
state) and get the board data. It then hands that data straight to the game's
`parser.parse(date, raw)` which writes `outputs/<date>/<game>.json`. No HTML is
cached by default — the scraper result flows to the parser **in memory**. The
`--save-html` flag additionally dumps `cache/<date>/<game>.html` for debugging.

The daily puzzle **number** is computed by each game's parser from a date anchor
(`_ANCHOR_DATE` / `_ANCHOR_NUM` in `games/<game>/parser.py`) — never scraped.

LinkedIn Games are guest-launched, so no login / session / credentials.

## Layout

```
linkedin_games_extractor/
  extract.py              # ROOT: capture + parse all games (today only)
  render.py               # ROOT: render outputs/<date>[/<game>] for inspection
  games/
    _common.py            # shared helpers (paths, grid parsing, render header)
    __init__.py           # dispatch: scraper()/parser()/renderer() per game
    <game>/               # one dir per game, each with:
      scraper.py          #   capture(page, date, save_html=False) -> raw
      parser.py           #   parse(date, raw) -> dict (writes the JSON)
      renderer.py         #   render(date) -> list[str] (monospace block)
  cache/<date>/<game>.html   # optional debug dump (gitignored)
  outputs/<date>/<game>.json # extracted puzzle (committed by CI)
```

`raw` is the HTML string for 7/8 games; for **crossclimb** it is a dict
(`{words, clues}`) because the solved 7-word ladder is read live from the
browser via `page.input_value()` after a real-mouse drag — it isn't in the
saved HTML.

## Usage

```
# capture + parse today's games (writes outputs/<today>/<game>.json)
python extract.py
python extract.py --games zip,pinpoint,crossclimb
python extract.py --headless        # no browser window
python extract.py --save-html       # also dump cache/<date>/<game>.html

# inspect extracted puzzles (reads outputs/, not the browser)
python render.py 2026-07-19              # every game that day
python render.py 2026-07-19 crossclimb   # one game
```

`extract.py` has **no `--date`** — it always captures the current day.

## Output schema — every game

All files share `game`, `number` (date-math), `date`, and `grid_size`
(`[cols, rows]`). See `games/<game>/parser.py` for the exact fields.

## Conventions

- **Dates**: files are organised `outputs/<YYYY-MM-DD>/`. Daily puzzles change
  each day, so always capture the target date (today, via `extract.py`).
- **Coordinates**: Patches `x`/`y` are 0-indexed (x = column, y = row). Queens /
  miniSudoku use `board[row][col]`. Zip nodes use `row`/`col`. Wend uses
  `grid[row][col]`.
- **Puzzle number**: date-math in each `parser.py` (`_ANCHOR_DATE` +
  days since anchor) — always present, never scraped.
- **Locale**: forced to `en-US` in the Playwright context, so all selectors /
  button text are English.
