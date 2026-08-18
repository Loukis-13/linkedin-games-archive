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
## Today's games (2026-08-18)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..    5   ..   ..   ..   .. |
+                    ---- ----     +
| ..    6   ..   ..   ..   .. | .. |
+     ---- ----               +    +
| ..   ..   .. | ..   ..    3 | .. |
+              +     ---- ----+    +
| ..   ..   .. | .. | ..   ..   .. |
+     ---- ----+    +              +
| .. |  2   ..   .. | ..   ..   .. |
+    +              +---- ----     +
| .. | ..   ..   ..   ..    1   .. |
+    +---- ----                    +
| ..   ..   ..   ..    4   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | M | . | . | M | M |
+---+---+---+---+---+---+
| M | . x . x . x . | S |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+-x-+---+---+-x-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . = . x . x . | M |
+---+---+---+---+---+---+
| M | S | . | . | M | S |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟧🟧🟧
🟥🟥🟨🟩🟩🟦🟦
🟥🟥🟨🟦🟦🟦🟦
🟪🟥🟫🟫🟫🟦🟦
🟪🟥🟥🟥🟫🟦🟦
🟪🟥🟫🟫🟫🟦🟦
🟪🟪🟪🟦🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │   ┃   │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │ 3 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 5 │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │ 2 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 3 │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃   │   │ 2 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| -3 | .. | .. | +2 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | +4 |
+----+----+----+----+----+----+
| +6 | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+
| .. | .. | +4 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +2 | .. | .. | -2 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| A | # | U | # | G |
+---+---+---+---+---+
| C | T | S | I | N |
+---+---+---+---+---+
| # | T | B | J | # |
+---+---+---+---+---+
| N | I | U | E | C |
+---+---+---+---+---+
| U | # | S | # | T |
+---+---+---+---+---+

Words:
  ACT
  UNIT
  USING
  SUBJECT
```

### pinpoint
```
  1. The Muppets
  2. Star Wars
  3. Marvel
  4. Pixar
  5. Mickey Mouse

  answer: Properties of The Walt Disney Company!
```

### crossclimb
```
game      : crossclimb
number    : 840
date      : 2026-08-18
difficulty: None

Ladder (word : clue, top -> bottom):
  fuel : The top + bottom rows = A two-word phrase for what may power an electric car by converting hydrogen into electricity. Keep in mind: The first word may be at the bottom.
  full : Stuffed
  bull : Animal that symbolizes a rising stock market
  bill : It may become a law
  will : Opposite of "won't"
  well : Source of drinking water
  cell : The top + bottom rows = A two-word phrase for what may power an electric car by converting hydrogen into electricity. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
