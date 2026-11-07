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
## Today's games (2026-11-07)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   10    8   ..   ..   ..   ..   .. |
+                                       +
| ..   ..   12   13   ..   14    7   .. |
+                                       +
| ..   ..   ..   ..    2   15   ..   .. |
+                                       +
| ..   ..   11    3   ..   ..   ..   .. |
+                                       +
| ..    9    4   ..    1   16   ..   .. |
+                                       +
| ..   ..   ..   ..   ..    5    6   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | . x . = . | . |
+---+-=-+-x-+---+---+---+
| . = . | . | . | . | . |
+---+---+---+---+---+---+
| . = . | S | . | . | . |
+-=-+---+---+---+---+---+
| . | . | . | M | . | . |
+-x-+---+---+---+---+---+
| . | . | . | . | S | . |
+---+---+---+---+---+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟨🟨🟧🟧
⬜⬜⬜🟩🟥🟦🟦🟦🟧
⬜⬜🟩🟩🟥🟥🟦🟦🟧
⬜🟩🟩🟩🟥🟥🟥🟦🟧
⬜⬜⬜🟫🟫🟥🟥🟥🟧
⬜⬛⬜⬜🟫🟪🟪🟪🟫
⬜⬛⬛🟫🟫🟪🟪🟫🟫
⬜⬛⬛⬛🟫🟪🟫🟫🟫
⬜⬜⬜⬜🟫🟫🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │ 4 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │ 1 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 1 │ 2 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 2 │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 5 │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| +3 | .. | .. | +3 | +3 | .. | .. | +  |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | +3 | .. |
+----+----+----+----+----+----+----+----+
| .. | |3 | .. | .. | .. | .. | +3 | .. |
+----+----+----+----+----+----+----+----+
| +3 | .. | +3 | .. | -3 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | =4 | .. | +4 | .. | +4 |
+----+----+----+----+----+----+----+----+
| .. | +4 | .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+----+
| .. | +  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| +4 | .. | .. | +4 | +  | .. | .. | +4 |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| J | R | # | R | O | N | Z |
+---+---+---+---+---+---+---+
| E | E | T | B | # | C | E |
+---+---+---+---+---+---+---+
| C | # | N | I | S | I | # |
+---+---+---+---+---+---+---+
| T | A | L | # | S | T | N |
+---+---+---+---+---+---+---+
| # | S | C | L | A | # | E |
+---+---+---+---+---+---+---+
| E | R | # | U | B | S | U |
+---+---+---+---+---+---+---+
| V | E | R | S | # | E | Q |
+---+---+---+---+---+---+---+

Words:
  BRONZE
  CLASSIC
  REVERSAL
  INTERJECT
  SUBSEQUENT
```

### pinpoint
```
  1. Guide
  2. Carriage
  3. Handbag brand
  4. Airplane section
  5. Sports team leader

  answer: Different definitions of "coach"!
```

### crossclimb
```
game      : crossclimb
number    : 921
date      : 2026-11-07
difficulty: None

Ladder (word : clue, top -> bottom):
  good : The top + bottom rows = A two-word phrase in the name of a cape on the coast of South Africa. Keep in mind: The first word may be at the bottom.
  gold : Metal for a first-place medal
  sold : Gave away in exchange for money
  sole : Bottom of a person's foot
  some : Vaguely defined amount between none and all
  home : Where many people go after work
  hope : The top + bottom rows = A two-word phrase in the name of a cape on the coast of South Africa. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
