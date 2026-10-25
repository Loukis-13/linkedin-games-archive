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
## Today's games (2026-10-25)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..    7   ..   ..   .. |
+               ----               +
| .. |  2   ..   ..   ..    6 | .. |
+    +                        +    +
| .. | ..   ..    8   ..   ..   .. |
+    +                             +
| ..    1   ..   ..   ..    5   .. |
+                                  +
| ..   ..   ..    3   ..   .. | .. |
+                             +    +
| .. | 10   ..   ..   ..    9 | .. |
+    +          ----          +    +
| ..   ..   ..    4   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | M | . | . | . | . |
+---+---+---+---+---+---+
| M | . = . | . | . | . |
+---+-=-+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | S | . |
+---+---+---+---+---+---+
| . | . | . | S | M | . |
+---+---+---+---+---+-x-+
| . | . | . | . | . = . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟨🟨🟨🟨🟨🟨
🟥🟥🟧🟧🟧🟨🟩🟩🟨
🟥🟥🟫🟧🟩🟩🟩🟨🟨
🟥🟫🟫🟫🟪🟦🟦🟨🟨
🟥🟫🟥🟪🟪🟪🟦🟦🟨
🟥🟥🟥🟥🟪⬛🟦🟨🟨
🟥🟥🟥⬛⬛⬛🟨🟨🟨
🟥🟥🟥🟥⬛🟨🟨🟨🟨
🟥🟥⬜⬜⬜⬜⬜🟨🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │ 3 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │ 4 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃ 4 │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 1 │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +3 | .. | =4 |
+----+----+----+----+----+----+----+----+
| .. | =  | .. | -3 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +3 | .. | -  |
+----+----+----+----+----+----+----+----+
| .. | =  | .. | +5 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +6 | .. | -  | .. |
+----+----+----+----+----+----+----+----+
| |  | .. | +6 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -6 | .. | |  | .. |
+----+----+----+----+----+----+----+----+
| -2 | .. | +2 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| G | N | C | S | U | # | # |
+---+---+---+---+---+---+---+
| T | E | H | O | R | # | # |
+---+---+---+---+---+---+---+
| H | L | I | R | G | B | U |
+---+---+---+---+---+---+---+
| V | E | M | # | L | O | S |
+---+---+---+---+---+---+---+
| A | W | F | P | I | R | T |
+---+---+---+---+---+---+---+
| # | # | R | E | W | O | L |
+---+---+---+---+---+---+---+
| # | # | A | M | K | R | Y |
+---+---+---+---+---+---+---+

Words:
  CHORUS
  PILGRIM
  ROBUSTLY
  FRAMEWORK
  WAVELENGTH
```

### pinpoint
```
  1. Teeth
  2. Words
  3. Polynomial functions
  4. Family history
  5. Trees (below the ground)

  answer: Things with roots!
```

### crossclimb
```
game      : crossclimb
number    : 908
date      : 2026-10-25
difficulty: None

Ladder (word : clue, top -> bottom):
  palm : The top + bottom rows = A two-word phrase for a type of tree cultivated for its sweet fruit. Keep in mind: The first word may be at the bottom.
  pale : Lacking color
  sale : Transaction at a shop
  sake : Alcoholic drink made from rice
  rake : Tool in a Zen garden
  rate : Give a score from 1 to 10, say
  date : The top + bottom rows = A two-word phrase for a type of tree cultivated for its sweet fruit. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
