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
## Today's games (2026-08-22)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..    4    3    8   ..   ..    9   .. |
+                                       +
| ..    5    6   ..   ..    7   ..   .. |
+                                       +
| ..    1   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   ..   ..   ..   ..   ..    2   .. |
+                                       +
| ..   ..   12   ..   ..   13   10   .. |
+                                       +
| ..   16   ..   ..   15   14   11   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . x . | M | M | . = . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . x . = . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | M | S | S |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | S | . x . | M | S |
+---+---+---+---+---+---+
```

### queens
```
🟪🟪🟪🟪🟦🟦⬛⬛🟦
🟪🟪🟪🟪🟦🟫🟫🟦🟦
🟪🟪🟪🟪🟦🟫🟫🟦🟦
🟪🟪🟪🟪🟦🟦🟦🟦🟦
🟦🟥🟥🟩🟩🟦🟦🟦🟦
🟦🟥🟥🟩🟩🟦🟧🟧🟦
🟦🟦🟨🟨🟦🟦🟧🟧🟦
🟦🟦🟨🟨🟦🟦🟦⬜⬜
🟦🟦🟦🟦🟦🟦🟦⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 6 │   ┃   │ 5 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃ 5 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | +2 | +2 | +2 | .. | .. |
+----+----+----+----+----+----+----+
| .. | +6 | .. | .. | .. | +4 | .. |
+----+----+----+----+----+----+----+
| |6 | .. | .. | .. | .. | .. | |6 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +3 | +3 | +3 | .. | .. |
+----+----+----+----+----+----+----+
| .. | +2 | .. | .. | .. | +6 | .. |
+----+----+----+----+----+----+----+
| +2 | .. | .. | .. | .. | .. | +2 |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| U | M | N | G | R | Y | T |
+---+---+---+---+---+---+---+
| L | Y | R | # | A | V | I |
+---+---+---+---+---+---+---+
| O | C | R | # | S | A | R |
+---+---+---+---+---+---+---+
| # | # | E | B | P | # | # |
+---+---+---+---+---+---+---+
| N | A | R | # | I | O | L |
+---+---+---+---+---+---+---+
| T | A | D | # | V | A | E |
+---+---+---+---+---+---+---+
| Q | U | U | L | T | R | T |
+---+---+---+---+---+---+---+

Words:
  COLUMN
  GRAVITY
  QUADRANT
  RASPBERRY
  ULTRAVIOLET
```

### pinpoint
```
  1. Crushing ice
  2. Removing nails
  3. Tenderizing meat
  4. Shaping metal (over an anvil)
  5. Chiseling stone (hit with this)

  answer: Different ways to use a hammer (besides the most common one)!
```

### crossclimb
```
game      : crossclimb
number    : 844
date      : 2026-08-22
difficulty: None

Ladder (word : clue, top -> bottom):
  sword : The top + bottom rows = A medieval weapon, and an adjective describing it. Keep in mind: The first word may be at the bottom.
  sworn : Like some testimony and enemies
  scorn : Open disrespect
  score : Total of how many goals each team has
  scare : Frightening moment
  share : Pass along to your followers, as a social media post
  sharp : The top + bottom rows = A medieval weapon, and an adjective describing it. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
