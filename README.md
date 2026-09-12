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
## Today's games (2026-09-12)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..    1 |
+                                  +
| ..    4   ..   ..   ..    6 | .. |
+                         ----+    +
| ..   ..    3   ..   .. | ..   .. |
+                        +         +
| ..   ..   ..    5   ..   ..   .. |
+                                  +
| ..   .. | ..   ..    2   ..   .. |
+     ----+                        +
| .. |  9   ..   ..   ..    8   .. |
+    +                             +
|  7   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | M | S | M | . | . |
+---+---+---+---+---+---+
| M | . | . | M | . | . |
+---+---+---+---+---+---+
| M | . | . | S | . | . |
+---+---+---+---+---+---+
| S | M | M | S | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . x . |
+---+---+---+---+-x-+-=-+
| . | . | . | . | . = . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟦🟦🟦🟦🟦🟦
🟥🟦🟥🟦🟩🟩🟨🟦🟦
🟫🟦🟦🟦🟩🟦🟨🟨🟦
🟫🟦🟧🟧🟧🟦🟦🟨🟦
🟫🟦🟧🟦🟦🟦🟦🟨🟦
🟪🟦⬜🟦🟦🟦🟦⬛🟦
🟪🟦⬜⬜🟦⬛⬛⬛🟦
🟪🟦🟦⬜🟦⬛🟦🟦🟦
🟪🟪🟪⬜🟦🟦🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 6 ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │   │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 3 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| +3 | .. | .. | .. | -4 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +9 | .. | .. | .. | |6 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | +2 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| |3 | .. | .. | .. | +12 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | -3 | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| # | A | # | A | # | A | # |
+---+---+---+---+---+---+---+
| N | D | D | T | T | C | C |
+---+---+---+---+---+---+---+
| E | # | E | # | E | # | E |
+---+---+---+---+---+---+---+
| G | C | T | P | M | T | N |
+---+---+---+---+---+---+---+
| A | U | # | O | # | U | A |
+---+---+---+---+---+---+---+
| T | L | L | R | R | L | T |
+---+---+---+---+---+---+---+
| U | R | A | D | E | Y | E |
+---+---+---+---+---+---+---+

Words:
  AGENDA
  ORDERLY
  CULTURAL
  ATTEMPTED
  ACCENTUATE
```

### pinpoint
```
  1. Rain
  2. Tear
  3. Name
  4. Mic
  5. Drag and

  answer: Words that come before “drop”!
```

### crossclimb
```
game      : crossclimb
number    : 865
date      : 2026-09-12
difficulty: None

Ladder (word : clue, top -> bottom):
  ware : The top + bottom rows = A compound word for decorative items given as presents, such as fancy silver for a wedding couple. Keep in mind: The first word may be at the bottom.
  wane : Wax and ___
  want : Desire
  rant : ___ and rave
  raft : Boat that's simply logs lashed together
  rift : Fissure, as in nature or a tense relationship
  gift : The top + bottom rows = A compound word for decorative items given as presents, such as fancy silver for a wedding couple. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
