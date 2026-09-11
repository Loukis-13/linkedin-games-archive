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
## Today's games (2026-09-11)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..    4   13   ..   ..   .. |
+                                       +
| ..   ..   ..    5   12   ..   ..   .. |
+          ----           ----          +
| ..   .. | ..   ..   ..   .. | ..   .. |
+         +                   +         +
|  3    6   ..    7   10   ..   11   14 |
+                                       +
|  2   19   ..    8    9   ..   18   15 |
+                                       +
| ..   .. | ..   ..   ..   .. | ..   .. |
+         +----           ----+         +
| ..   ..   ..   20   17   ..   ..   .. |
+                                       +
| ..   ..   ..    1   16   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | . | S | . | . |
+---+---+---+---+---+---+
| . | M | M | S | . | . |
+---+---+---+---+---+---+
| . | . | M | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+-x-+---+---+
| . | . | . x . = . | . |
+---+---+-x-+---+-=-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜🟥⬛⬛⬛⬛⬛⬜
⬜🟥🟥⬛⬛⬛🟧⬛⬜
⬜⬜🟥⬛⬛🟧🟧🟫⬜
⬜⬜🟥⬛⬛⬛🟧🟫⬜
🟪⬜🟥⬛⬛⬛🟧🟫🟫
🟪🟨🟨🟨🟦🟦🟧🟫🟫
🟪🟦🟦🟦🟦🟩🟩🟩🟫
🟪🟪🟪🟪🟦🟦🟦🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 4 ┃ 6 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃   │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 6 │   │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 5 │   ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 4 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | +5 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | +5 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| |  | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | |  | .. | .. | +5 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| H | S | E | A | R | T |
+---+---+---+---+---+---+
| C | # | R | L | # | N |
+---+---+---+---+---+---+
| I | L | F | # | C | E |
+---+---+---+---+---+---+
| U | B | # | S | K | I |
+---+---+---+---+---+---+
| P | # | R | G | # | N |
+---+---+---+---+---+---+
| S | S | E | O | R | P |
+---+---+---+---+---+---+

Words:
  SKIN
  FRESH
  PUBLIC
  CENTRAL
  PROGRESS
```

### pinpoint
```
  1. Traps
  2. Quads
  3. Lats
  4. Pecs
  5. Abs (short for abdominals)

  answer: Nicknames for different muscles!
```

### crossclimb
```
game      : crossclimb
number    : 864
date      : 2026-09-11
difficulty: None

Ladder (word : clue, top -> bottom):
  lego : The top + bottom rows = A two-word phrase for certain collections of toy bricks that can be assembled into intricate designs. Keep in mind: The first word may be at the bottom.
  logo : Graphic design used to represent a company
  logs : Cut sections of tree trunks that may be used as firewood
  jogs : Runs at a relaxed pace
  jots : Puts down on paper quickly
  jets : Vehicles like 747’s and 767’s
  sets : The top + bottom rows = A two-word phrase for certain collections of toy bricks that can be assembled into intricate designs. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
