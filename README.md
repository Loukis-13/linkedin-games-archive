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
## Today's games (2026-10-31)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+     ---- ----                    +
| .. | ..   ..   ..    2    1   .. |
+    +                             +
| .. | ..   12   11   ..    4   .. |
+    +                             +
| ..   ..    9   ..   10   ..   .. |
+                                  +
| ..    3   ..    8    7   .. | .. |
+                             +    +
| ..    5    6   ..   ..   .. | .. |
+                    ---- ----+    +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | . x . = . | . |
+---+---+---+---+-x-+---+
| . | . | . | . | . | . |
+---+-x-+---+---+-=-+---+
| . | . | . | . | . | . |
+---+-=-+---+---+---+---+
| . | . = . x . | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+---+---+---+---+---+---+
```

### queens
```
🟦🟦🟩🟩⬛⬛⬛⬛⬛
🟦🟦🟦🟩🟩⬜⬜⬜⬛
🟦🟦🟧🟧🟧🟧🟧⬜⬜
🟦🟧🟧🟫🟧🟧🟥🟧⬜
🟦🟧🟫🟫🟧🟥🟥🟧⬜
🟦🟧🟧🟧🟧🟧🟧🟧⬜
🟦🟧🟪🟪🟧🟪🟪🟧🟨
🟦🟧🟧🟪🟪🟪🟧🟧🟨
🟦🟦🟧🟧🟧🟧🟧🟨🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │ 1 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │   ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 4 │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 5 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | +15 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | =  |
+----+----+----+----+----+----+----+
| +3 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | +6 |
+----+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +12 | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| # | S | K | I | M | T | # |
+---+---+---+---+---+---+---+
| # | A | # | S | # | H | # |
+---+---+---+---+---+---+---+
| # | M | # | C | # | G | # |
+---+---+---+---+---+---+---+
| C | O | H | H | I | I | L |
+---+---+---+---+---+---+---+
| O | L | C | F | E | S | H |
+---+---+---+---+---+---+---+
| T | A | H | O | S | A | L |
+---+---+---+---+---+---+---+
| E | # | G | # | T | # | F |
+---+---+---+---+---+---+---+

Words:
  MASK
  GHOST
  MISCHIEF
  CHOCOLATE
  FLASHLIGHT
```

### pinpoint
```
  1. Books
  2. Cacti
  3. Sea urchins
  4. Vertebrates (by definition)
  5. Porcupines (they're sharp!)

  answer: Things with spines!
```

### crossclimb
```
game      : crossclimb
number    : 914
date      : 2026-10-31
difficulty: None

Ladder (word : clue, top -> bottom):
  poke : The top + bottom rows = A two-word phrase for a sphere for catching creatures in a massively popular game series. Keep in mind: The first word may be at the bottom.
  pole : What a gondolier uses for propulsion
  pile : Heap
  file : You might use it on your nails
  fill : ___-in-the-blank
  bill : What someone must pay before leaving the restaurant
  ball : The top + bottom rows = A two-word phrase for a sphere for catching creatures in a massively popular game series. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
