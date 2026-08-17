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
## Today's games (2026-08-17)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
| ..   ..   10    5   ..   .. |
+                             +
| ..   ..   11    4   ..   .. |
+                             +
|  8    9   ..   ..    6    7 |
+                             +
|  1   12   ..   ..    3    2 |
+                             +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | S | . | . | . |
+---+---+---+---+---+---+
| . | S | S | M | . | . |
+---+---+---+---+---+---+
| . x . x . x . = . | . |
+---+---+---+---+---+---+
| . | . x . x . x . x . |
+---+---+---+---+---+---+
| . | . | M | S | M | . |
+---+---+---+---+---+---+
| . | . | . | M | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟫🟫🟫🟫🟫🟫🟫
🟫🟧🟪🟪🟪🟨🟫
🟫🟧🟧🟪🟨🟨🟫
🟫🟧🟩🟦🟩🟨🟫
🟫🟧🟩🟩🟩🟨🟫
🟫🟧🟥🟥🟩🟨🟥
🟫🟫🟫🟥🟥🟥🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 2 │ 3 │ 6 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │ 5 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │ 6 │ 3 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 1 │ 3 │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 6 │   │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 2 │ 5 │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| |3 | +4 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | =4 | +2 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +9 | |3 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +5 | |6 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| Y | # | # | # | J |
+---+---+---+---+---+
| R | O | W | A | I |
+---+---+---+---+---+
| C | T | # | S | G |
+---+---+---+---+---+
| I | E | T | O | U |
+---+---+---+---+---+
| V | # | # | # | Q |
+---+---+---+---+---+

Words:
  QUOTE
  JIGSAW
  VICTORY
```

### pinpoint
```
  1. Dram
  2. Krone
  3. Rupee
  4. Peso
  5. Euro (€)

  answer: Names of world currencies!
```

### crossclimb
```
game      : crossclimb
number    : 839
date      : 2026-08-17
difficulty: None

Ladder (word : clue, top -> bottom):
  miss : The top + bottom rows = Two words that complete the expression “___ the ___” meaning to lose out on an opportunity (i.e., the ship’s already left!). Keep in mind: The first word may be at the bottom.
  mass : Physical property measured in grams
  mast : Tall pole used to support a sail
  cast : Fiberglass bandage used to immobilize a broken bone
  cost : It’s listed on a price tag
  coat : Outerwear to protect from the cold and rain
  boat : The top + bottom rows = Two words that complete the expression “___ the ___” meaning to lose out on an opportunity (i.e., the ship’s already left!). Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
