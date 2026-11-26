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
## Today's games (2026-11-26)

### zip
```
+----+----+----+----+----+----+
|  2   ..   ..   ..   ..   .. |
+                             +
| ..   ..   ..    5   ..   .. |
+     ----                    +
| ..   ..   ..   ..   ..    3 |
+          ---- ----          +
|  1   ..   ..   ..   ..   .. |
+                    ----     +
| ..   ..    4   ..   ..   .. |
+                             +
| ..   ..   ..   ..   ..    6 |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . = . | . = . | S |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+-x-+-x-+---+---+-=-+-x-+
| . | . | . x . | . | . |
+---+---+---+---+---+---+
| M | . x . | . x . | S |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟧🟧🟧🟧🟧🟥🟥
🟥🟧🟨🟨🟩🟧🟦🟪
🟥🟧🟨🟨🟩🟩🟦🟪
🟥🟧🟫🟫⬛⬛🟦🟪
🟥🟧🟫🟦⬛⬛🟦🟪
🟧🟧🟪🟦🟦🟦🟦🟪
🟪🟪🟪🟪🟪🟪🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │ 2 ┃ 3 │   │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │   │   ┃   │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │ 1 ┃ 5 │   │ 2 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | -  | .. |
+----+----+----+----+----+----+
| .. | .. | .. | -  | .. | +5 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +5 | .. |
+----+----+----+----+----+----+
| .. | +2 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| +5 | .. | |  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| E | T | A | I | C | E | R |
+---+---+---+---+---+---+---+
| # | # | # | R | G | P | P |
+---+---+---+---+---+---+---+
| S | # | T | A | # | A | # |
+---+---+---+---+---+---+---+
| K | # | E | L | # | # | # |
+---+---+---+---+---+---+---+
| N | # | F | U | T | # | E |
+---+---+---+---+---+---+---+
| A | H | T | S | R | # | T |
+---+---+---+---+---+---+---+
| B | L | E | S | I | B | U |
+---+---+---+---+---+---+---+

Words:
  BLESS
  THANKS
  TRIBUTE
  GRATEFUL
  APPRECIATE
```

### pinpoint
```
  1. Pillows
  2. Teddy bears
  3. Holiday turkey
  4. You, after eating too much
  5. Ravioli (w/ meat or cheese)

  answer: Things that are stuffed!
```

### crossclimb
```
game      : crossclimb
number    : 940
date      : 2026-11-26
difficulty: None

Ladder (word : clue, top -> bottom):
  road : The top + bottom rows = A two-word phrase for a journey taken in a car. Keep in mind: The first word may be at the bottom.
  read : What many people do to relax before going to sleep
  ream : Bundle of printer paper
  team : "There's no I in ___"
  tram : Streetcar (or, spelled backwards, a store)
  trap : Pitfall
  trip : The top + bottom rows = A two-word phrase for a journey taken in a car. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
