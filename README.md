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
## Today's games (2026-08-15)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| 12   11   ..   ..   ..   ..   13   14 |
+               ---- ----               +
| ..    7   10   ..   ..    9    8   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   15    2   ..   ..    3    4   .. |
+               ---- ----               +
|  6   16   ..   ..   ..   ..    1    5 |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+-=-+-x-+---+---+
| . | M | . | . | M | . |
+---+---+---+---+---+---+
| . = . | . | M | . x . |
+---+---+---+---+---+---+
| . x . | M | . | . x . |
+---+---+---+---+---+---+
| . | M | . | . | M | . |
+---+---+-x-+-x-+---+---+
| . | . | . x . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟫🟫🟦🟦🟦🟦🟥🟥🟥
🟫🟦🟦🟪🟪🟪🟪🟪🟥
🟧🟧🟧⬜⬜⬜⬜🟪🟥
🟨🟨🟧⬜⬜⬜🟥🟥🟥
🟨🟨🟧⬜⬜⬜🟥🟩🟩
🟧🟧🟧⬜⬜⬜🟥🟩🟩
🟧⬜⬜⬜⬜⬜🟥🟥🟥
🟧⬜⬜⬜⬜⬜⬛⬛⬛
🟧🟧🟧⬛⬛⬛⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 4 │   ┃ 1 │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │   ┃   │   │ 2 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │   ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 5 ┃   │ 2 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | +  | +  | .. | .. | .. | |  |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | -  | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +  | .. | .. | +  | .. | +  | +  |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| +2 | +2 | .. | +2 | .. | .. | +2 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | |2 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| -2 | .. | .. | .. | +2 | +2 | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| I | M | A | T | R | U | G |
+---+---+---+---+---+---+---+
| T | L | M | U | U | L | A |
+---+---+---+---+---+---+---+
| # | U | # | U | M | S | U |
+---+---+---+---+---+---+---+
| # | # | # | U | # | U | # |
+---+---+---+---+---+---+---+
| L | A | A | C | # | # | # |
+---+---+---+---+---+---+---+
| C | C | V | U | R | A | N |
+---+---+---+---+---+---+---+
| U | L | U | S | M | U | I |
+---+---+---+---+---+---+---+

Words:
  GURU
  USUAL
  VACUUM
  URANIUM
  CALCULUS
  ULTIMATUM
```

### pinpoint
```
  1. A speech
  2. The daily newspaper
  3. The mail
  4. A knockout blow
  5. Restaurant food brought to you

  answer: Things that are delivered!
```

### crossclimb
```
game      : crossclimb
number    : 837
date      : 2026-08-15
difficulty: None

Ladder (word : clue, top -> bottom):
  step : The top + bottom rows = A compound word meaning to go beyond one's authority or boundaries. Keep in mind: The first word may be at the bottom.
  stem : Part of a plant, or an acronym for four evidence-based fields of study
  seem : Appear (to be)
  seen : Perceived
  sven : Common Swedish boy's name that means "young man"
  oven : Appliance for roasting a turkey
  over : The top + bottom rows = A compound word meaning to go beyond one's authority or boundaries. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
