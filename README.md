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
## Today's games (2026-08-16)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..    4   ..   ..   ..   .. |
+                                       +
| ..    7   ..   ..   ..   ..    9   .. |
+                                       +
| ..   ..   ..   ..    5   ..   ..   .. |
+                                       +
| ..   ..    8   ..   ..   ..   ..    6 |
+                                       +
|  3   ..   ..   ..   ..   10   ..   .. |
+                                       +
| ..   ..   ..   11   ..   ..   ..   .. |
+                                       +
| ..    2   ..   ..   ..   ..   12   .. |
+                                       +
| ..   ..   ..   ..    1   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | S | . | . | . | . |
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . | . | . | . = . |
+---+---+---+---+---+---+
| S | S | . | . | . | . |
+---+---+---+---+---+-=-+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . x . |
+---+---+---+---+---+---+
```

### queens
```
🟨⬜⬜⬜⬜⬜⬜⬜⬜
🟨🟨⬜⬜🟧⬜⬜⬛⬛
🟨⬜⬜🟥🟧🟧⬜⬜⬛
⬜⬜🟥🟥🟦🟧🟩⬛⬛
⬜🟥🟥🟦🟦🟦🟩🟩⬛
⬜⬜🟥🟫🟦🟪🟩⬛⬛
⬜⬜🟥🟫🟫🟪🟪⬛⬛
⬜⬜🟫🟫🟪🟪🟪⬛⬛
⬜⬜⬜🟪🟪🟪⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃   │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │   ┃ 6 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 5 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | .. | =  | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | .. | |3 | .. |
+----+----+----+----+----+----+----+----+
| +2 | .. | +6 | .. | .. | -  | .. | |  |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| |  | .. | -  | .. | .. | +12 | .. | +2 |
+----+----+----+----+----+----+----+----+
| .. | -5 | .. | .. | .. | .. | +3 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | -  | .. | .. | +4 | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| O | N | A | D | E | N | O |
+---+---+---+---+---+---+---+
| I | Q | L | # | E | N | M |
+---+---+---+---+---+---+---+
| T | U | O | T | I | T | I |
+---+---+---+---+---+---+---+
| C | # | # | # | # | # | N |
+---+---+---+---+---+---+---+
| A | R | I | V | I | D | A |
+---+---+---+---+---+---+---+
| P | F | D | # | N | E | T |
+---+---+---+---+---+---+---+
| O | R | T | I | O | R | O |
+---+---+---+---+---+---+---+

Words:
  DIVIDE
  PORTION
  QUOTIENT
  FRACTIONAL
  DENOMINATOR
```

### pinpoint
```
  1. Freeze
  2. Time
  3. Bed
  4. Door
  5. Picture (🖼️)

  answer: Words that come before “frame”!
```

### crossclimb
```
game      : crossclimb
number    : 838
date      : 2026-08-16
difficulty: None

Ladder (word : clue, top -> bottom):
  fillet : The top + bottom rows = Two options at a seafood restaurant: one a type of shellfish, the other a cut of fish. Keep in mind: The first word may be at the bottom.
  filled : Like these blanks, when you're done with them
  milled : Fed through a grinding machine, as wheat
  misled : Gave false information to
  missed : Didn't hit the target
  mussed : Made untidy or disheveled, as someone's hair
  mussel : The top + bottom rows = Two options at a seafood restaurant: one a type of shellfish, the other a cut of fish. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
