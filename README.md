# LinkedIn Games Extractor

Extract the daily LinkedIn Games puzzle definitions into per-day JSON files so
the puzzles can be replicated offline. Eight games are targeted; six are fully
implemented, two are deferred (see below).

## How it works

**One capture strategy: Termux Browser Pilot (tbp).** `src/tbp_capture.py`
drives the real Firefox daemon via the tbp Python client (`send_command`),
navigates to each game, clicks "Iniciar jogo"/"Start game" where needed, and
dumps the board HTML to `cache/<date>/<game>.html`. It also saves the daily
puzzle `number` to `cache/<date>/<game>_meta.json`.

Two URL forms are required (LinkedIn renders boards differently per game):
- **Grid games** (zip, tango, queens, minisudoku) embed the board inside an
  `<iframe src="/games/view/<slug>/desktop">`, so `tbp_capture.py` navigates
  straight to that URL — the board then sits in the top document.
- **wend, patches** render the board directly in the top document, but only
  after the start button is clicked (the click transition is flaky, so it
  retries in a loop).

> Note: the `browser_navigate` / `browser_snapshot` MCP tools are NOT usable on
> this platform (Termux arm64 — "Unsupported platform: android-arm64"). Use the
> `tbp` CLI / Python client. The old headless `--dump-dom` path
> (`scrape_games.py`) is kept only for extraction (it reads the cached HTML);
> HTML capture goes through tbp exclusively.

## Layout

    linkedin_games_extractor/
      src/
        tbp_capture.py     -- SINGLE HTML getter for all games (tbp browser)
        run_all.py         -- one-command daily pipeline (capture + extract)
        scrape_games.py    -- extractors for zip/tango/queens/minisudoku
                            -- (reads cached HTML; --force re-dumps headless)
        extract_zip.py      -- legacy screenshot-based Zip extractor (see note)
        build_legend.py     -- legacy Zip digit-template legend builder
        extract_wend.py     -- Wend extractor -> outputs/<date>/wend.json
        extract_patches.py  -- Patches extractor -> outputs/<date>/patches.json
        view_json.py        -- pretty-print any game's JSON in the terminal
      cache/<date>/<game>.html        -- raw captured board DOM (via tbp)
      cache/<date>/<game>_meta.json   -- puzzle number (tbp games only)
      outputs/<date>/<game>.json      -- extracted puzzle definition

## Usage

    # one command for the whole day (capture + extract all 6 games)
    python src/run_all.py
    python src/run_all.py --date 2026-07-15

    # or step by step:
    # capture ALL games' HTML for today via tbp (no args; today's date)
    python src/tbp_capture.py

    # extract the 4 grid games from the cached HTML (no re-dump)
    python src/scrape_games.py --date 2026-07-15 \
        --games zip,tango,queens,minisudoku

    # extract wend + patches
    python src/extract_wend.py    --date 2026-07-15 \
        --meta cache/2026-07-15/wend_meta.json
    python src/extract_patches.py --date 2026-07-15 \
        --meta cache/2026-07-15/patches_meta.json

    # inspect any extracted puzzle
    python src/view_json.py all --date 2026-07-15
    python src/view_json.py wend --date 2026-07-15

`--date` defaults to **today**; pass it explicitly to capture a specific day.
One JSON file is written per game per day under `outputs/<date>/`.

Wend's `words` key is only written when you pass `--words "ICY,OVAL,..."`
(the solution words are not in the board DOM); otherwise it is omitted.

## Output schema — every game

All files share the common fields `game`, `date`, and `grid_size`
(`[n_cols, n_rows]`).

### zip  (`outputs/<date>/zip.json`)
Numbered nodes on a lattice + wall barriers between cells.

    {
      "game": "zip",
      "date": "2026-07-13",
      "grid_size": [n_cols, n_rows],   # dynamic, recovered from the lattice
      "nodes": [                       # numbered cells (1-indexed id)
        {"id": <digit>, "row": <r>, "col": <c>}, ...
      ],
      "walls": [                       # each wall = the two adjacent cells it
        [[r1, c1], [r2, c2]], ...      # separates (blocks movement between)
      ]
    }

### tango  (`outputs/<date>/tango.json`)
Moon/Sun grid + equality/X divisors between adjacent cells.

    {
      "game": "tango",
      "date": "2026-07-13",
      "grid_size": [n_cols, n_rows],
      "symbols": [                     # given tiles only
        [<row>, <col>, "<M|S>"], ...  # M = Moon (given), S = Sun (given)
      ],
      "walls": [                       # divisors between two cells
        [[r1, c1], [r2, c2], "<=|x>"], ...   # = equality, x not-equal
      ]
    }

### queens  (`outputs/<date>/queens.json`)
Colored regions (region id per cell). Placed queens are intentionally ignored.

    {
      "game": "queens",
      "date": "2026-07-13",
      "grid_size": [n_cols, n_rows],
      "board": [                       # board[row][col] = region id
        [<region_id>, ...], ...
      ]
    }

### minisudoku  (`outputs/<date>/minisudoku.json`)
Prefilled 6x6 grid; `null` = blank.

    {
      "game": "minisudoku",
      "number": null,                    # NOT in the unauthenticated HTML
      "date": "2026-07-13",              # (fetched via a voyager API that 401s
      "grid_size": [n_cols, n_rows],     #  without a session) -> left null
      "cells": [ [<digit|null>, ...], ... ]
    }
      ]
    }

### wend  (`outputs/<date>/wend.json`)
5x5 letter grid with holes ("weave with words").

    {
      "game": "wend",
      "number": <int>,                 # daily puzzle number (from start screen)
      "date": "2026-07-13",
      "grid_size": [5, 5],
      "grid": [                        # '.' = hole, otherwise a letter tile
        ["N", "T", ".", "O", "V"], ...
      ],
      "words": [ "ICY", "OVAL", ... ]  # solution words (NOT in board DOM;
                                       # supply via --words after in-game reveal)
    }

### patches  (`outputs/<date>/patches.json`)
7x7 grid of patch clues. Coordinates are **0-indexed** (`x` = column,
`y` = row).

    {
      "game": "patches",
      "number": <int>,                 # daily puzzle number (from start screen)
      "date": "2026-07-13",
      "grid_size": [7, 7],
      "clues": [
        {"x": <col>, "y": <row>,       # 0-indexed
         "type": "square"|"free"|"V_rect"|"H_rect",
         "size": <int|null>},          # null for fixed shapes (square/V/H_rect);
                                       # N for "free" (tile length in cells)
        ...
      ]
    }
    # type counts for the daily puzzle: 2 square, 10 free, 1 V_rect, 1 H_rect

### pinpoint  (`outputs/<date>/pinpoint.json`) — DEFERRED
Word-association game. The board content (clue words) is fetched via LinkedIn's
voyager API after the game starts and only renders after interaction / reveal;
not captured by the current pipeline.

### crossclimb  (`outputs/<date>/crossclimb.json`) — DEFERRED
Ladder word game. Same limitation as Pinpoint: the letters load from voyager
after start and require the in-game reveal. Deferred.

## Conventions

- **Dates**: files are organised `outputs/<YYYY-MM-DD>/`. Daily puzzles change
  each day, so always capture the target date.
- **Coordinates**: Patches `x`/`y` are 0-indexed (x = column, y = row). Queens/
  miniSudoku use `board[row][col]` (0-indexed). Zip nodes use `row`/`col`
  (0-indexed). Wend uses a 2D `grid[row][col]`.
- **Puzzle number**: auto-captured for zip/tango/queens (from `NO.xxx` in the
  board-page launch footer), wend/patches (from the start screen). Mini-sudoku's
  number is served by a voyager API that 401s without a session, so it is left
  `null`. The number is saved to `cache/<date>/<game>_meta.json` by
  `tbp_capture.py` and read by the extractors.
- **Locale flips**: LinkedIn serves the UI in PT-BR or EN intermittently. The
  start button is "Iniciar jogo" / "Start game" and Patches clue aria-labels
  are "Dica de linha R, coluna C, pista ..." / "Row R, column C, ... clue".
  Both `tbp_capture.py` and `extract_patches.py` handle either language.

## Legacy

`extract_zip.py` / `build_legend.py` are the original screenshot-based Zip
extractor (digit templates from `zip_legend.json`). The current headless
`scrape_games.py` captures Zip from the live DOM instead; the screenshot path is
kept for reference.
