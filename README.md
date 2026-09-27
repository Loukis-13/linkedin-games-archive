# LinkedIn Games Extractor
Capture the daily **LinkedIn Games** puzzles into per-day JSON files so they
can be inspected or replicated offline. All **eight** games are implemented and
captured with **Playwright**.
- Games: `zip`, `tango`, `queens`, `minisudoku`, `patches`, `wend`,
  `pinpoint`, `crossclimb`
- Output: `outputs/<YYYY-MM-DD>/<game>.json`, one file per game per day.

## Developer docs
See [`AGENTS.md`](./AGENTS.md) for the full architecture, the CI pipeline, the
local Telegram-posting cron, conventions, how to use, and how to add a new game.

<!-- DAILY-GAMES-START -->
## Today's games (2026-09-27)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   10    7   ..   ..   .. |
+                                       +
| ..   ..    9   ..   ..    4   ..   .. |
+               ----                    +
| ..   11   ..   ..   .. | ..    5   .. |
+          ----          +              +
| 12   ..   ..   ..   ..   .. | ..    6 |
+                             +         +
| 14   .. | ..   ..   ..   ..   ..    3 |
+         +               ----          +
| ..   13   .. | ..   ..   ..    2   .. |
+              +     ----               +
| ..   ..   15   ..   ..    8   ..   .. |
+                                       +
| ..   ..   ..   16    1   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+-x-+---+---+---+
| . = . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+-=-+---+---+---+---+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
| . | . | . | S | M | M |
+---+---+---+---+---+---+
| . | . | . | S | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟦🟦🟦🟦🟫🟩🟩🟩🟩
🟪🟦🟦🟫🟫🟫🟨🟨🟩
🟪🟪🟫🟫🟫🟫🟫🟨🟨
🟪🟫🟫🟫🟫🟫🟫🟫🟨
🟥🟥🟥🟧🟫⬜⬜⬜🟨
🟥🟧🟧🟧🟫⬜⬜⬜⬜
🟥🟧🟧🟧🟫⬜⬜⬜⬜
🟥🟧⬛⬛🟫⬛⬛⬜⬜
🟧🟧⬛⬛⬛⬛⬛⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 6 │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 5 │   ┃ 6 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| +  | .. | .. | .. | .. | .. | +2 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | |3 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | =4 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -3 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | |4 | .. | .. | .. | +5 | .. |
+----+----+----+----+----+----+----+----+
| +  | .. | .. | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +6 | .. | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| # | I | R | M | R | H | # |
+---+---+---+---+---+---+---+
| Q | U | E | M | O | C | O |
+---+---+---+---+---+---+---+
| S | U | M | # | M | O | N |
+---+---+---+---+---+---+---+
| I | M | # | # | # | M | E |
+---+---+---+---+---+---+---+
| X | A | M | # | M | E | N |
+---+---+---+---+---+---+---+
| Y | T | U | M | B | R | A |
+---+---+---+---+---+---+---+
| # | I | N | M | O | C | # |
+---+---+---+---+---+---+---+

Words:
  SQUIRM
  MAXIMUM
  MEMBRANE
  COMMUNITY
  MONOCHROME
```

### pinpoint
```
  1. Fair
  2. Market
  3. Mind
  4. Earnings per
  5. The lion’s (the largest part)

  answer: Words that come before “share”!
```

### crossclimb
```
game      : crossclimb
number    : 880
date      : 2026-09-27
difficulty: None

Ladder (word : clue, top -> bottom):
  ships : The top + bottom rows = Ocean vessels, and a word for a group of them. Keep in mind: The first word may be at the bottom.
  chips : Small squares containing circuits
  clips : Short segments from longer videos
  flips : Turns over, as a playing card
  flies : Plays with, as a kite
  flees : Runs away from danger
  fleet : The top + bottom rows = Ocean vessels, and a word for a group of them. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
