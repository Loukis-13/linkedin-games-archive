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
## Today's games (2026-10-11)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   14   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   ..    5   18   ..   ..   17   15 |
+                                       +
| 13   ..   ..   ..   ..   16   ..   .. |
+                                       +
| ..    6    8   ..   ..   ..   ..   .. |
+                                       +
| ..   ..   ..   ..   ..    1    2   .. |
+                                       +
| ..   ..    7   ..   ..   ..   ..    3 |
+                                       +
| 12   11   ..   ..    9   10   ..   .. |
+                                       +
| ..   ..   ..   ..   ..   ..    4   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| . | S | . x . | S | . |
+---+---+---+---+---+---+
| S | . | . | . | . | M |
+---+---+---+---+---+---+
| . | . | . x . | . | . |
+---+---+---+---+---+---+
| . | S | . x . | M | . |
+---+---+---+---+---+---+
| S | . | . | . | . | S |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟧🟧🟧🟧🟧
🟥🟨🟨🟥🟧🟥🟥🟥🟧
🟥🟨🟥🟥🟥🟥🟥🟥🟧
🟥🟨🟩🟩🟦🟦🟦🟥🟧
🟨🟨🟩🟦🟦🟪🟦🟥🟥
🟨🟫🟩🟩🟩🟪🟦⬛⬛
🟨🟫🟫🟫🟫🟪🟪🟪⬛
⬛⬛⬛⬛🟫🟫🟫🟪⬛
⬛⬜⬜⬛⬛⬛⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃ 6 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │   ┃   │   │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 5 ┃   │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 5 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | |3 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| |6 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -3 | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| A | N | O | N | Y | U | M |
+---+---+---+---+---+---+---+
| L | Y | # | Y | # | Y | M |
+---+---+---+---+---+---+---+
| L | M | # | S | # | O | N |
+---+---+---+---+---+---+---+
| E | Y | Y | # | R | E | Y |
+---+---+---+---+---+---+---+
| P | W | A | # | D | T | X |
+---+---+---+---+---+---+---+
| S | H | O | Y | A | S | E |
+---+---+---+---+---+---+---+
| Y | C | L | O | G | Y | Y |
+---+---+---+---+---+---+---+

Words:
  ONYX
  YUMMY
  SYNONYM
  ALLEYWAY
  YESTERDAY
  PSYCHOLOGY
```

### pinpoint
```
  1. Books
  2. Plates
  3. Firewood
  4. Chairs after a banquet
  5. Poker chips (in tall columns)

  answer: Things that are stacked!
```

### crossclimb
```
game      : crossclimb
number    : 894
date      : 2026-10-11
difficulty: None

Ladder (word : clue, top -> bottom):
  file : The top + bottom rows = A row and a column of a chessboard, or non-managing workers as in the phrase "___ and ___." Keep in mind: The first word may be at the bottom.
  fill : Pack until nothing else will fit
  fall : Plunge
  tall : Like prominent buildings
  talk : Pep ___ (motivational speech)
  tank : Where to keep pet fish
  rank : The top + bottom rows = A row and a column of a chessboard, or non-managing workers as in the phrase "___ and ___." Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
