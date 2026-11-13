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
## Today's games (2026-11-13)

### zip
```
+----+----+----+----+----+----+----+
| ..    9   ..    8   ..    3   .. |
+                                  +
| ..   10   ..    7   ..    1   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+     ----           ----          +
| ..   ..   ..   ..   ..   ..   .. |
+          ----           ----     +
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..   12   ..    2   ..    4   .. |
+                                  +
| ..   11   ..    6   ..    5   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | M | S | M | . |
+---+---+---+---+---+---+
| . | . = . x . = . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | S | M | S | . |
+---+---+---+---+---+---+
| . | . x . = . x . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥⬛⬛⬛⬛⬛
🟥🟦🟦🟦⬛⬛⬛⬛
🟥🟥🟪🟦🟪⬛⬛⬛
🟥🟧🟪🟦🟪⬛⬛⬛
🟧🟧🟪🟦🟪🟨🟨🟨
🟧🟧🟪🟪🟪🟨🟩🟨
🟧🟧🟧🟧🟧🟨🟩🟨
🟫🟫🟧🟧🟧🟨🟩🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 3 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │ 4 │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │ 2 │   ┃   │ 6 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 5 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | -  |
+----+----+----+----+----+----+
| .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+
| .. | .. | .. | |  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | =  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | .. |
+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| A | B | C | # | # | # |
+---+---+---+---+---+---+
| Z | U | R | Y | P | C |
+---+---+---+---+---+---+
| Z | E | N | T | T | I |
+---+---+---+---+---+---+
| M | U | Q | E | R | L |
+---+---+---+---+---+---+
| A | T | R | I | F | A |
+---+---+---+---+---+---+
| # | # | # | X | Y | Z |
+---+---+---+---+---+---+

Words:
  LAZY
  ABUZZ
  MATRIX
  CRYPTIC
  FREQUENT
```

### pinpoint
```
  1. Cook
  2. Canary
  3. Marshall
  4. Falkland
  5. Galápagos

  answer: Names of island groups / archipelagoes (when followed by “Islands”)!
```

### crossclimb
```
game      : crossclimb
number    : 927
date      : 2026-11-13
difficulty: None

Ladder (word : clue, top -> bottom):
  duck : The top + bottom rows = A certain waterfowl, and a body of water where you might see one. Keep in mind: The first word may be at the bottom.
  puck : Rubber disc used in ice hockey
  punk : ___ rock (brash music subgenre)
  puns : Wordplay jokes often met with groans
  pens : Writing implements that may dry out if left uncapped
  pend : Be unresolved
  pond : The top + bottom rows = A certain waterfowl, and a body of water where you might see one. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
