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
## Today's games (2026-11-09)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+          ---- ----          +
| ..   ..   .. | ..   ..   .. |
+              +              +
| .. | .. |  3    6 | .. | .. |
+    +    +         +    +    +
| ..    4   ..   ..    5   .. |
+                             +
| ..   .. |  1 |  2 | ..   .. |
+         +    +    +         +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | . | . | . | . |
+---+---+-x-+---+---+---+
| M | . | . | . | . | . |
+---+---+---+---+---+---+
| S | S | . x . | . | . |
+---+---+---+---+---+---+
| . | . | M | M | . x . |
+---+---+---+---+---+---+
| . | . | . | S | . | . |
+---+---+---+---+---+-x-+
| . | . | . | S | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟨🟩🟫🟧🟧🟧🟧
🟨🟩🟫🟫🟧🟪🟧
🟨🟩🟫🟫🟧🟧🟧
🟨🟩🟩🟩🟩🟦🟧
🟨🟨🟨🟩🟩🟦🟦
🟨🟨🟨🟩🟩🟩🟩
🟨🟥🟥🟥🟥🟥🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 2 ┃ 3 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │ 2 │   ┃   │ 3 │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │ 4 │   ┃   │ 2 │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │ 5 ┃ 1 │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | =9 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |  |
+----+----+----+----+----+----+
| .. | =9 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | |  | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| A | # | R | E | C |
+---+---+---+---+---+
| C | P | T | # | E |
+---+---+---+---+---+
| C | E | T | P | I |
+---+---+---+---+---+
| D | # | T | P | A |
+---+---+---+---+---+
| N | E | R | # | Z |
+---+---+---+---+---+

Words:
  ZAP
  TREND
  ACCEPT
  RECEIPT
```

### pinpoint
```
  1. Temperature
  2. Humidity
  3. Atmospheric pressure
  4. Wind speed and direction
  5. Chance of precipitation

  answer: Parts of a weather forecast!
```

### crossclimb
```
game      : crossclimb
number    : 923
date      : 2026-11-09
difficulty: None

Ladder (word : clue, top -> bottom):
  dogs : The top + bottom rows = Two groups of animals commonly adopted as pets.
  dots : Polka ___ (fabric pattern)
  dote : Excessively bestow affection (on)
  date : Romantically involved couple's outing
  mate : Either half of a romantically involved couple
  mats : Soft platforms in a yoga studio
  cats : The top + bottom rows = Two groups of animals commonly adopted as pets.
```
<!-- DAILY-GAMES-END -->
