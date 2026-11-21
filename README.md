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
## Today's games (2026-11-21)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   .. | ..   ..   ..   .. |
+              +     ---- ----     +
| ..    6   ..   ..   ..    5 | .. |
+               ----          +    +
| .. | ..   ..   .. | ..   .. | .. |
+    +              +         +    +
| .. |  2   .. | .. | ..    4 | .. |
+    +         +    +         +    +
| .. | ..   .. | ..   ..   .. | .. |
+    +         +----          +    +
| .. |  1   ..   ..   ..    3   .. |
+    +---- ----                    +
| ..   ..   ..   .. | ..   ..   .. |
+---- ---- ---- ----+---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
| . = . x . = . x . | M |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . = . x . x . x . |
+---+---+---+---+---+---+
| M | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟪🟪🟪🟩🟩🟩
⬜🟥🟫🟪🟨🟪🟩🟦🟩
⬜🟥🟫🟪🟨🟪🟩🟩🟩
⬜🟥🟫🟪🟨🟪🟩🟧⬜
⬜🟥🟫🟪🟪🟪🟩🟧⬜
⬜🟫🟫🟧🟧🟧🟧🟧⬜
⬜🟫⬛⬛⬛🟧🟧🟧⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃   │ 2 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 5 │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 6 │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| -3 | .. | .. | .. | .. | .. | .. | +7 |
+----+----+----+----+----+----+----+----+
| .. | -3 | .. | .. | .. | .. | +  | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +3 | .. | .. | =  | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +3 | .. | .. | -  | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | -3 | .. | .. | .. | .. | +  | .. |
+----+----+----+----+----+----+----+----+
| |3 | .. | .. | .. | .. | .. | .. | +7 |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | Z | I | N | G | R |
+---+---+---+---+---+---+
| T | E | E | # | # | E |
+---+---+---+---+---+---+
| N | E | R | F | I | D |
+---+---+---+---+---+---+
| D | I | B | R | V | I |
+---+---+---+---+---+---+
| E | # | # | I | E | D |
+---+---+---+---+---+---+
| R | G | N | I | F | # |
+---+---+---+---+---+---+

Words:
  BRIEF
  DIVIDER
  FREEZING
  INGREDIENT
```

### pinpoint
```
  1. Full
  2. Blue
  3. Harvest
  4. Crescent
  5. Dark side of the

  answer: Words that come before "moon"!
```

### crossclimb
```
game      : crossclimb
number    : 935
date      : 2026-11-21
difficulty: None

Ladder (word : clue, top -> bottom):
  scot : The top + bottom rows = A hyphenated word meaning "without being punished." Keep in mind: The first word may be at the bottom.
  slot : Small opening for a coin
  slow : Not quick
  flow : Move freely, like water
  floe : Sheet of ice on the water's surface
  flee : Run far away from
  free : The top + bottom rows = A hyphenated word meaning "without being punished." Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
