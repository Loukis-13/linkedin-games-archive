# LinkedIn Games Extractor
Capture the daily **LinkedIn Games** puzzles into per-day JSON files so they
can be inspected or replicated offline. All **eight** games are implemented and
captured with **Playwright**.
- Games: `zip`, `tango`, `queens`, `minisudoku`, `patches`, `wend`,
  `pinpoint`, `crossclimb`
- Output: `outputs/<YYYY-MM-DD>/<game>.json`, one file per game per day.

## Usage
```bash
# capture + parse today's games (writes outputs/<today>/<game>.json)
python extract.py
python extract.py --games zip,pinpoint,crossclimb
python extract.py --headless
python extract.py --save-html        # also dump debug HTML to cache/

# inspect extracted puzzles (reads outputs/, not the browser)
python render.py 2026-07-19                 # every game that day
python render.py 2026-07-19 crossclimb      # one game
python render.py 2026-07-19 --header        # with per-game summary
python render.py 2026-07-19 --format ascii  # force ascii
```

## Developer docs
See [`AGENTS.md`](./AGENTS.md) for the full architecture, the CI pipeline, the
local Telegram-posting cron, conventions, and how to add a new game.
