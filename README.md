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
## Today's games (2026-09-16)

### zip
```
+----+----+----+----+----+----+
| ..   ..    1    2   ..    3 |
+                             +
|  4   ..   ..   ..   ..   .. |
+                             +
| ..   ..   ..   ..   ..    5 |
+                             +
|  6   ..   ..   ..   ..   .. |
+                             +
| ..   ..   ..   ..   ..    8 |
+                             +
|  7   ..   10    9   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+-x-+-x-+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | S | . | . | . |
+---+---+---+-x-+-x-+---+
| . | S | S | . | . | . |
+---+---+---+---+---+---+
| . | . | . | S | S | . |
+---+---+---+---+---+---+
| . | . | . | S | M | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟧🟧
🟥🟥🟧🟧🟧🟩🟩
🟥🟫🟧🟧🟦🟩🟩
🟪🟫🟧🟦🟦🟩🟨
🟪🟪🟧🟦🟦🟨🟨
🟧🟪🟧🟦🟨🟨🟨
🟧🟧🟧🟨🟨🟨🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 2 ┃ 3 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │   ┃   │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃ 1 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| -8 | .. | .. | .. | +  | .. | |4 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| +  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +16 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| =4 | .. | +  | .. | .. | .. | -2 |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| P | E | R | F | E | C | T |
+---+---+---+---+---+---+---+
| A | C | I | T | N | # | # |
+---+---+---+---+---+---+---+
| B | S | # | # | E | # | # |
+---+---+---+---+---+---+---+
| # | O | # | # | H | # | # |
+---+---+---+---+---+---+---+
| # | L | # | # | T | S | S |
+---+---+---+---+---+---+---+
| # | U | T | F | U | A | E |
+---+---+---+---+---+---+---+
| Y | L | E | L | A | W | L |
+---+---+---+---+---+---+---+

Words:
  PERFECT
  FLAWLESS
  AUTHENTIC
  ABSOLUTELY
```

### pinpoint
```
  1. Prescriptions
  2. Mechanical pencils
  3. Fuel tanks
  4. Empty water bottles
  5. Printers (with toner + paper)

  answer: Things that are refilled!
```

### crossclimb
```
game      : crossclimb
number    : 869
date      : 2026-09-16
difficulty: None

Ladder (word : clue, top -> bottom):
  chat : The top + bottom rows = A two-word phrase for an instant-messaging function in an online meeting app. Keep in mind: The first word may be at the bottom.
  coat : Garment to protect from chilly weather
  coal : Burnable form of carbon
  cool : Hip or trendy
  coos : Makes a sound like a dove
  zoos : Places where you can safely see lions
  zoom : The top + bottom rows = A two-word phrase for an instant-messaging function in an online meeting app. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
