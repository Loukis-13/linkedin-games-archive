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
## Today's games (2026-10-05)

### zip
```
+----+----+----+----+----+----+
|  5   ..   ..   ..   ..   .. |
+               ---- ----     +
| ..   ..   .. |  1    2    3 |
+              +              +
| ..   ..   .. |  9   ..   .. |
+              +---- ----     +
| ..   ..   ..   ..    4 | .. |
+                        +    +
| ..   ..   ..   ..   .. |  8 |
+               ---- ----+    +
| ..   ..   ..    6    7   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | M | . | . |
+---+---+---+---+---+---+
| . | . | M | . | M | . |
+---+---+---+-x-+---+---+
| . | M | . | . | . | M |
+---+---+---+---+---+---+
| M | . | . | . | S | . |
+---+---+-x-+---+---+---+
| . | S | . | M | . | . |
+---+---+---+---+---+---+
| . | . | S | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟧🟧
🟧🟧🟧🟨🟧🟧🟧
🟧🟧🟨🟨🟧🟧🟧
🟧🟧🟧🟨🟩🟩🟧
🟧🟦🟦🟨🟩🟫🟪
🟦🟦🟨🟨🟨🟫🟪
🟦🟦🟦🟪🟪🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 2 ┃ 3 │ 4 │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │ 3 ┃ 4 │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 6 │   ┃   │   │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃ 6 │ 1 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| |5 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +6 | +3 | +3 |
+----+----+----+----+----+----+
| .. | .. | .. | +3 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | -5 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | -5 |
+----+----+----+----+----+----+
| .. | .. | .. | +4 | +2 | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| D | E | L | G | I |
+---+---+---+---+---+
| O | # | # | # | D |
+---+---+---+---+---+
| M | # | C | # | M |
+---+---+---+---+---+
| R | # | R | # | E |
+---+---+---+---+---+
| E | T | A | I | T |
+---+---+---+---+---+

Words:
  DIG
  ITEM
  MODEL
  CRATER
```

### pinpoint
```
  1. Recorder
  2. Whistle
  3. Piccolo
  4. Flute
  5. Clarinet

  answer: Wind instruments!
```

### crossclimb
```
game      : crossclimb
number    : 888
date      : 2026-10-05
difficulty: None

Ladder (word : clue, top -> bottom):
  work : The top + bottom rows = A compound word for how an organization might accomplish a challenging task. Keep in mind: The first word may be at the bottom.
  worm : “The early bird catches the ___”
  form : Something you might fill out with your name and address
  foam : Type of cushioning or rubber
  roam : Travel without a plan
  ream : Package of 500 sheets of paper
  team : The top + bottom rows = A compound word for how an organization might accomplish a challenging task. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
