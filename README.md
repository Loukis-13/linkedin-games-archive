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
## Today's games (2026-10-24)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..    3    9   10   ..   ..   .. |
+                                  +
| ..    4   ..   ..   12   ..   .. |
+                                  +
| ..    7   ..   ..   11   ..   .. |
+                                  +
| ..   ..    6    5    8   ..   .. |
+                                  +
| ..   ..   ..   ..   ..    1   .. |
+                                  +
| ..   ..   ..   ..   ..   ..    2 |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | M | . | . | . | . |
+---+---+-=-+---+---+---+
| . | . | . | . | . | . |
+-=-+---+---+-=-+---+---+
| . | . | . | . | . | . |
+---+-=-+---+---+-x-+---+
| . | . | . | . | . | . |
+---+---+-x-+---+---+-x-+
| . | . | . | . | . | . |
+---+---+---+-x-+---+---+
| . | . | . | . | S | M |
+---+---+---+---+---+---+
```

### queens
```
⬛⬛⬛⬛⬛⬛⬛⬛⬛
🟥🟥🟥⬛⬛🟫🟫⬛⬛
🟧🟧🟥🟩⬛🟩🟫🟫⬛
🟥🟥🟥🟩⬛🟩🟦⬛⬛
🟥🟨🟨🟩🟩🟩🟦⬛⬛
🟥🟥🟥🟪🟪🟩🟦🟦🟦
⬜⬜⬜⬜🟪🟩🟦🟪🟦
⬜⬜⬜⬜🟪🟪🟦🟪🟦
⬜⬜⬜⬜⬜🟪🟪🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 5 │   ┃   │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃   │   │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 6 ┃ 4 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │   ┃   │   │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | -  | =  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |  | =4 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| +2 | .. | .. | .. | .. | .. | .. | -  |
+----+----+----+----+----+----+----+----+
| =  | .. | .. | .. | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | -2 | =  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -  | |  | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| E | O | R | E | O | R | E |
+---+---+---+---+---+---+---+
| H | # | I | T | L | # | S |
+---+---+---+---+---+---+---+
| T | # | C | A | P | # | C |
+---+---+---+---+---+---+---+
| S | T | E | L | X | E | O |
+---+---+---+---+---+---+---+
| A | # | R | G | I | # | R |
+---+---+---+---+---+---+---+
| C | # | O | N | S | # | E |
+---+---+---+---+---+---+---+
| E | R | O | F | S | E | L |
+---+---+---+---+---+---+---+

Words:
  IGNORE
  EXPLORE
  FORECAST
  SCORELESS
  THEORETICAL
```

### pinpoint
```
  1. Friends
  2. Quarters
  3. Attention
  4. To home
  5. Call / shave (near miss)

  answer: Words that come after “close”!
```

### crossclimb
```
game      : crossclimb
number    : 907
date      : 2026-10-24
difficulty: None

Ladder (word : clue, top -> bottom):
  menu : The top + bottom rows = Something you read at a restaurant, and what you choose from it. Keep in mind: The first word may be at the bottom.
  mend : On the ___ (recovering from an injury)
  bend : Make curved or angled, as a straight object
  bond : Join together permanently
  bold : Word-processing option that makes the letters thicker
  fold : Verb often seen in origami instructions
  food : The top + bottom rows = Something you read at a restaurant, and what you choose from it. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
