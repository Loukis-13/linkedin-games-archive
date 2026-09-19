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
## Today's games (2026-09-19)

### zip
```
+----+----+----+----+----+----+----+
| ..   10   12   ..   ..   ..   .. |
+                                  +
|  9   ..   ..   ..   ..   ..   .. |
+                                  +
| ..   ..   11    2   .. | ..   .. |
+               ----     +         +
| ..    4   ..   ..   ..    1   .. |
+               ----               +
| ..   .. | ..    5    3   ..   .. |
+         +                        +
| ..   ..   ..   ..   ..   ..    6 |
+                                  +
| ..   ..   ..   ..    8    7   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | . | . | . | M |
+---+---+---+---+---+---+
| . | M | . | . | M | . |
+---+---+---+---+---+---+
| . | . | . x . | . | . |
+---+---+-=-+-x-+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| . | S | . | . | M | . |
+---+---+---+---+---+---+
| S | . | . | . | . | S |
+---+---+---+---+---+---+
```

### queens
```
⬛⬛⬛⬛🟥🟨🟨🟨🟨
⬛⬛⬛⬛🟥🟩🟩🟨🟨
⬛⬛🟥🟥🟥🟩🟧🟧🟨
⬛⬛🟥🟥🟥🟧🟧🟨🟨
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟦🟦🟫🟫🟥🟥🟥⬜⬜
🟦🟪🟪🟫🟥🟥🟥⬜⬜
🟦🟦🟪🟫🟥⬜⬜⬜⬜
🟦🟦🟦🟦🟥⬜⬜⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 5 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | -  | .. | .. | .. | .. | +4 | .. |
+----+----+----+----+----+----+----+----+
| -  | .. | |  | .. | .. | +4 | .. | +4 |
+----+----+----+----+----+----+----+----+
| .. | -  | .. | .. | .. | .. | +4 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | .. | +3 | .. |
+----+----+----+----+----+----+----+----+
| -  | .. | |  | .. | .. | +9 | .. | +4 |
+----+----+----+----+----+----+----+----+
| .. | -  | .. | .. | .. | .. | +5 | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| B | R | E | S | A | K | E |
+---+---+---+---+---+---+---+
| # | # | V | E | M | # | # |
+---+---+---+---+---+---+---+
| # | O | D | A | A | N | # |
+---+---+---+---+---+---+---+
| # | G | S | H | S | W | # |
+---+---+---+---+---+---+---+
| # | N | A | A | D | O | # |
+---+---+---+---+---+---+---+
| # | # | M | D | E | # | # |
+---+---+---+---+---+---+---+
| A | C | C | I | N | T | S |
+---+---+---+---+---+---+---+

Words:
  MANGO
  ADVERB
  SHADOWS
  NAMESAKE
  ACCIDENTS
```

### pinpoint
```
  1. Power
  2. Open
  3. Reliable
  4. Anonymous
  5. Go straight to the

  answer: Words that come before “source”!
```

### crossclimb
```
game      : crossclimb
number    : 872
date      : 2026-09-19
difficulty: None

Ladder (word : clue, top -> bottom):
  life : The top + bottom rows = A compound word for a rescue item on a ship. Keep in mind: The first word may be at the bottom.
  lift : Another word for what's called an elevator in North America
  list : You might make one for a shopping trip
  lust : One of the seven deadly sins
  bust : Sculpture of the upper part of the body
  busy : Having lots of things going on
  buoy : The top + bottom rows = A compound word for a rescue item on a ship. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
