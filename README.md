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
## Today's games (2026-09-29)

### zip
```
+----+----+----+----+----+----+----+
|  2   ..   ..   ..   ..   ..    9 |
+                                  +
| .. |  1   .. |  7 | ..   .. | .. |
+    +         +    +         +    +
| .. | ..   .. | .. | ..    8 | .. |
+    +         +    +         +    +
| .. | ..   .. | .. | ..   .. | .. |
+    +---- ----+    +---- ----+    +
| ..    4   .. | ..   ..   .. | .. |
+              +              +    +
| ..   ..   .. |  6   ..    5 | .. |
+              +              +    +
|  3   ..   ..   ..   ..   ..   10 |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | S | . | . | . | . |
+---+---+---+---+---+---+
| . | S | S | . | . | . |
+---+---+---+---+---+---+
| . | M | S | . | . | . |
+---+---+---+---+-=-+---+
| . | M | . | . x . | . |
+---+---+---+---+---+---+
| . | . | . | . = . | . |
+---+---+---+---+-x-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟧🟧🟧
🟥🟥🟥🟧🟧🟧🟧🟧
🟥🟥🟥🟧🟧🟧🟨🟨
🟥🟥🟥🟧🟧🟩🟨🟨
🟥🟥🟥🟦🟩🟩🟩🟨
🟥🟪🟦🟦🟦🟩🟨🟨
🟪🟪🟪🟦🟫🟫🟨🟨
⬛🟪🟫🟫🟫🟫🟨🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 2 │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 2 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │ 4 ┃ 5 │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │ 6 ┃ 1 │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 5 ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 1 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | -10 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| +15 | .. | .. | .. | .. | .. | +10 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | -14 | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| E | E | R | T | I |
+---+---+---+---+---+
| P | # | # | # | E |
+---+---+---+---+---+
| F | O | R | M | E |
+---+---+---+---+---+
| I | # | # | # | K |
+---+---+---+---+---+
| N | U | A | L | I |
+---+---+---+---+---+

Words:
  TIE
  PEER
  ALIKE
  UNIFORM
```

### pinpoint
```
  1. Help
  2. View
  3. Window
  4. File
  5. Edit (where you can copy and paste)

  answer: Software menus!
```

### crossclimb
```
game      : crossclimb
number    : 882
date      : 2026-09-29
difficulty: None

Ladder (word : clue, top -> bottom):
  flip : The top + bottom rows = A hyphenated word for an open-toed item of footwear. Keep in mind: The first word may be at the bottom.
  slip : Lose one's footing
  slit : Extremely narrow opening
  slot : Narrow opening
  slow : Lacking speed
  flow : Movement of water or air
  flop : The top + bottom rows = A hyphenated word for an open-toed item of footwear. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
