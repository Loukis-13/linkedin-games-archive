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
## Today's games (2026-08-31)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..    2 |
+               ---- ----     +
| .. | 10    1   ..    4 | .. |
+    +                   +    +
| .. | ..    5   ..   .. | .. |
+    +                   +    +
| .. | ..   ..    7   .. | .. |
+    +                   +    +
| .. |  6   ..    8    3 | .. |
+    +---- ----          +    +
|  9   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . | . x . | . = . |
+---+---+---+---+---+---+
| M | . | . | . | . | . |
+---+-=-+-=-+-x-+-x-+-x-+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | S |
+-=-+-=-+-x-+-=-+-x-+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
| . x . | . x . | . x . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟧🟥🟥🟥
🟨🟥🟧🟧🟧🟥🟥
🟨🟩🟧🟧🟧🟦🟥
🟨🟩🟧🟧🟧🟦🟥
🟨🟩🟩🟪🟪🟦🟥
🟨🟩🟫🟫🟦🟦🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 3 │ 4 │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 2 │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │ 1 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │ 2 │ 6 ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 6 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | -8 | .. | .. | +  | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | +  | .. | .. | |12 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| H | A | O | O | C |
+---+---+---+---+---+
| # | Z | Z | # | I |
+---+---+---+---+---+
| R | A | # | I | T |
+---+---+---+---+---+
| D | # | Z | Z | # |
+---+---+---+---+---+
| O | R | E | E | N |
+---+---+---+---+---+

Words:
  ZOO
  ZERO
  HAZARD
  CITIZEN
```

### pinpoint
```
  1. Risk
  2. Taboo
  3. Boggle
  4. Cluedo (Clue in N. America)
  5. Jenga

  answer: Games published by Hasbro!
```

### crossclimb
```
game      : crossclimb
number    : 853
date      : 2026-08-31
difficulty: None

Ladder (word : clue, top -> bottom):
  time : The top + bottom rows = A compound word for an organized list of what will happen and when, which may help to track a work project. Keep in mind: The first word may be at the bottom.
  tire : Grow weary from activity
  hire : Employ someone to join a work team
  hive : Home for bees
  five : Number of stars in many top ratings
  fine : Satisfactory, or amount paid as a penalty
  line : The top + bottom rows = A compound word for an organized list of what will happen and when, which may help to track a work project. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
