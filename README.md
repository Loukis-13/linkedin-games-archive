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
## Today's games (2026-10-09)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..    7   ..   ..   ..   .. |
+                         ----     +
| ..    4   ..    6   ..   ..   .. |
+                         ----     +
| ..   ..    8   ..   ..   ..   .. |
+                    ----          +
| ..   ..   ..   ..   ..   ..   .. |
+          ----                    +
| ..   ..   ..   ..    1   ..   .. |
+     ----                         +
| ..   ..   ..    2   ..    3   .. |
+     ----                         +
| ..   ..   ..   ..    5   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | M | . | . | . |
+---+-=-+---+---+---+---+
| M | . | S | . | . | . |
+---+-x-+---+---+---+---+
| S | . | M | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | S | . |
+---+---+---+-=-+---+-=-+
| . | . | . | . | M | . |
+---+---+---+-x-+---+-x-+
| . | . | . | . | M | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟧🟧🟧
🟥🟧🟧🟧🟧🟨🟨🟨
🟩🟩🟩🟩🟧🟧🟧🟨
🟩🟦🟦🟦🟪🟪🟪🟪
🟦🟦🟦🟦🟦🟦🟦🟪
🟦🟦🟦🟦🟦🟫🟫🟫
⬛⬛⬛🟦🟦🟦🟦🟫
⬛🟦🟦🟦🟦🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 6 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 6 │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 6 ┃ 5 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃ 3 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | -  |
+----+----+----+----+----+----+----+
| .. | +9 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +9 | .. | .. |
+----+----+----+----+----+----+----+
| +  | .. | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+
| .. | .. | +9 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +9 | .. |
+----+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | B | N | A | # | # |
+---+---+---+---+---+---+
| N | A | G | R | E | M |
+---+---+---+---+---+---+
| G | L | E | P | C | O |
+---+---+---+---+---+---+
| U | Z | P | O | O | O |
+---+---+---+---+---+---+
| B | Z | W | D | R | B |
+---+---+---+---+---+---+
| # | # | O | R | N | # |
+---+---+---+---+---+---+

Words:
  BANGLE
  POPCORN
  BUZZWORD
  BOOMERANG
```

### pinpoint
```
  1. Blue
  2. Right
  3. Bowhead
  4. Humpback
  5. Orca (aka “Killer”)

  answer: Types of whales!
```

### crossclimb
```
game      : crossclimb
number    : 892
date      : 2026-10-09
difficulty: None

Ladder (word : clue, top -> bottom):
  half : The top + bottom rows = A two-word phrase for something that lasts for two beats in a piece of music in 4/4 time. Keep in mind: The first word may be at the bottom.
  hale : ___ and hearty (in good physical condition)
  hare : Long-eared animal related to the rabbit
  dare : Challenge to do something risky
  date : 10/10/26, for example
  dote : Lavish affection (on)
  note : The top + bottom rows = A two-word phrase for something that lasts for two beats in a piece of music in 4/4 time. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
