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
## Today's games (2026-11-05)

### zip
```
+----+----+----+----+----+----+----+
|  1   ..   ..   ..   ..   ..   .. |
+          ---- ---- ----          +
| ..   ..   ..    6   ..   ..   .. |
+                                  +
| .. |  9   .. | .. | ..    4   .. |
+    +         +    +              +
|  7 | ..   .. | .. | ..   .. |  2 |
+    +         +    +         +    +
| ..    8   .. | .. | ..    3 | .. |
+              +    +         +    +
| ..   ..   ..    5   ..   ..   .. |
+          ---- ---- ----          +
| ..   ..   ..   ..   ..   ..   10 |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | S | M | . x . x . |
+---+---+---+---+-x-+---+
| . | S | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | . | . | . | . |
+---+---+---+---+-x-+---+
| S | M | M | . x . x . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟧🟧🟧🟧
🟥🟥🟨🟨🟨🟨🟨🟨🟧
🟥🟥🟥🟩🟨🟨🟦🟦🟦
🟪🟪🟥🟩🟨🟨🟦🟦🟦
🟪🟫🟥🟩⬛⬛⬛⬛⬛
🟪🟫🟥🟩⬛⬛⬛⬛⬛
⬜🟫🟥🟩⬛⬛⬛⬛⬛
⬜🟫🟫🟩⬛⬛⬛⬛⬛
⬜⬜⬜🟩⬛⬛⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 5 ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 6 │   │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │   │   ┃   │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 1 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| -6 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | -8 | .. | .. |
+----+----+----+----+----+----+
| +8 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +4 |
+----+----+----+----+----+----+
| .. | .. | -4 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | -6 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | T | H | # | # | # |
+---+---+---+---+---+---+
| # | B | G | J | O | U |
+---+---+---+---+---+---+
| # | U | I | M | N | R |
+---+---+---+---+---+---+
| Y | O | Y | L | A | # |
+---+---+---+---+---+---+
| A | N | C | D | O | # |
+---+---+---+---+---+---+
| # | # | # | D | S | # |
+---+---+---+---+---+---+

Words:
  ODDS
  MIGHT
  JOURNAL
  BUOYANCY
```

### pinpoint
```
  1. Cold
  2. Age
  3. Mason
  4. Henge
  5. ’s throw away

  answer: Terms that come after “stone”!
```

### crossclimb
```
game      : crossclimb
number    : 919
date      : 2026-11-05
difficulty: None

Ladder (word : clue, top -> bottom):
  gale : The top + bottom rows = Air movement, and a strong form of it. Keep in mind: The first word may be at the bottom.
  sale : Occasion when prices are lowered
  sane : Capable of thinking rationally
  sand : Grains plentiful in the Sahara
  hand : Human body part with knuckles
  hind : At the back, as two legs of many animals
  wind : The top + bottom rows = Air movement, and a strong form of it. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
