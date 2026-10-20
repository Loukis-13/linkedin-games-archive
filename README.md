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
## Today's games (2026-10-20)

### zip
```
+----+----+----+----+----+----+
|  1   ..   ..   ..   ..    9 |
+                             +
| ..   ..    2   ..    4   .. |
+                             +
| ..    6   ..    8   ..   .. |
+                             +
| ..   ..    7   ..   ..   .. |
+                             +
| ..    5   ..   ..   ..   .. |
+                             +
|  3   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . = . | . | S |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+---+---+-=-+---+---+---+
| . | . | . | . | M | M |
+---+---+---+---+---+---+
| M | M | . | . | . | . |
+---+---+---+-=-+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . | . = . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟧🟥🟨
🟥🟥🟥🟥🟥🟧🟥🟨
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟩🟥🟦🟥🟥🟥🟥
🟥🟩🟥🟦🟥🟥🟥🟥
🟪🟪🟪🟪🟥🟥🟥🟥
🟪🟫🟫🟪🟥🟥🟥🟥
🟪🟪🟪🟪🟥⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃ 2 │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 1 ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃ 5 │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 2 ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │   ┃ 3 │   │ 1 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| +3 | .. | .. | .. | .. | +5 | .. |
+----+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +5 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +7 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +7 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | .. | +7 |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| E | D | I | S | T |
+---+---+---+---+---+
| E | N | T | O | U |
+---+---+---+---+---+
| # | # | R | # | # |
+---+---+---+---+---+
| C | N | A | O | F |
+---+---+---+---+---+
| E | E | C | I | F |
+---+---+---+---+---+

Words:
  OFFICE
  OUTSIDE
  ENTRANCE
```

### pinpoint
```
  1. Spelt
  2. Sorghum
  3. Millet
  4. Rye
  5. Rice

  answer: Types of grain!
```

### crossclimb
```
game      : crossclimb
number    : 903
date      : 2026-10-20
difficulty: None

Ladder (word : clue, top -> bottom):
  leak : The top + bottom rows = Two ways data might become public when it shouldn't be.
  lead : Be in the front of, as a race
  head : Where a hat usually sits
  herd : Collective noun for bison or elephants
  hard : Difficult
  hark : "___! The Herald Angels Sing"
  hack : The top + bottom rows = Two ways data might become public when it shouldn't be.
```
<!-- DAILY-GAMES-END -->
