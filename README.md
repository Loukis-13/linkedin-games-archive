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
## Today's games (2026-09-06)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   16   ..   15   ..    5   ..   .. |
+                                       +
| ..   17   ..   18   ..   14   ..   .. |
+                                       +
| ..    2   ..    1   ..   12   ..   .. |
+                                       +
| ..   ..   10   ..   11   ..   13   .. |
+                                       +
| ..   ..    9   ..    8   ..    6   .. |
+                                       +
| ..   ..    3   ..    4   ..    7   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . = . | . |
+-=-+---+---+---+---+-x-+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . = . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . x . |
+---+---+---+---+---+---+
| M | . | . | . | . | . |
+---+---+---+---+---+-=-+
| S | M | M | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜🟥🟥⬜⬜⬜🟧🟧⬜
⬜🟥🟥🟥🟨🟧🟧🟧⬜
⬛🟥🟥🟥🟨🟧🟧⬜⬜
⬛⬛⬛⬛🟨🟪🟪⬜⬜
⬛🟩⬛🟨🟨🟫🟫🟦⬜
⬛🟩🟩🟫🟫🟫🟦🟦⬜
⬛⬛🟩🟩🟦🟦🟦⬛⬜
⬛⬛⬛⬛⬛⬛⬛⬛⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │ 3 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │ 4 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 2 │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 3 │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 6 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -6 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | |6 | .. | .. | .. | .. | |6 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | -  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | =  |
+----+----+----+----+----+----+----+----+
| -6 | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |6 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | |6 | .. | .. | .. | .. | |6 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | |6 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| E | M | E | R | C | E | X |
+---+---+---+---+---+---+---+
| N | # | I | # | N | # | E |
+---+---+---+---+---+---+---+
| T | T | T | # | I | U | C |
+---+---+---+---+---+---+---+
| E | E | H | P | S | T | I |
+---+---+---+---+---+---+---+
| E | G | G | A | I | O | V |
+---+---+---+---+---+---+---+
| T | U | A | C | T | N | E |
+---+---+---+---+---+---+---+
| N | A | R | E | J | B | O |
+---+---+---+---+---+---+---+

Words:
  EXECUTIVE
  INCREMENT
  SPAGHETTI
  GUARANTEE
  OBJECTION
```

### pinpoint
```
  1. Cardboard
  2. Leaves
  3. Banana peels
  4. Eggshells and egg cartons
  5. Grass clippings and twigs

  answer: Things that are composted!
```

### crossclimb
```
game      : crossclimb
number    : 859
date      : 2026-09-06
difficulty: None

Ladder (word : clue, top -> bottom):
  poker : The top + bottom rows = A two-word phrase for expressions that don't give any indication of intent. Keep in mind: The first word may be at the bottom.
  pokes : Gives a hello on Facebook (using an icon like this: 👈)
  poles : People from Warsaw
  pales : “That ___ in comparison”
  pares : Cuts the peel off a potato with a special knife
  fares : Costs paid to ride buses
  faces : The top + bottom rows = A two-word phrase for expressions that don't give any indication of intent. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
