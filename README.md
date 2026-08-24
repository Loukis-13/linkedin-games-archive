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
## Today's games (2026-08-24)

### zip
```
+----+----+----+----+----+----+
|  2   ..   ..   ..   ..   .. |
+                             +
| .. | 10    1    8    9 | .. |
+    +     ---- ----     +    +
| .. | ..   ..   ..   .. | .. |
+    +                   +    +
| .. | ..   ..   ..   .. | .. |
+    +     ---- ----     +    +
| .. |  3    6    5    4 | .. |
+    +                   +    +
| ..   ..   ..   ..   ..    7 |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | M | S | . x . | . |
+---+---+---+---+---+-=-+
| M | . | M | . | . | . |
+---+---+---+-=-+---+---+
| S | . | M | . | . | . |
+---+---+---+---+---+-=-+
| M | S | S | . x . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟨🟨🟨🟨
🟥🟩🟩🟩🟩🟩🟩🟩🟨
🟦🟦🟦🟦🟦🟦🟦🟩🟨
🟦🟦🟪🟦🟦🟦🟪🟨🟨
🟦🟪🟪🟪🟦🟪🟪🟪🟨
🟦🟪🟪🟪🟪🟪🟪🟪🟫
🟦🟦🟪🟪⬛🟪🟪🟫🟫
🟦🟦🟦🟪🟪🟪🟫🟫🟫
🟦🟦⬜⬜🟪🟫🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃ 1 │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 4 │ 5 │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 2 │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │ 2 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │ 2 │ 5 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 6 │ 4 ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +2 | |12 | .. |
+----+----+----+----+----+----+
| .. | .. | |12 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | |4 | .. | .. |
+----+----+----+----+----+----+
| .. | =4 | +2 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| # | Y | O | R | Y |
+---+---+---+---+---+
| L | L | L | # | A |
+---+---+---+---+---+
| E | # | L | # | P |
+---+---+---+---+---+
| J | # | L | L | L |
+---+---+---+---+---+
| K | N | I | A | # |
+---+---+---+---+---+

Words:
  ALL
  LINK
  JELLY
  PAYROLL
```

### pinpoint
```
  1. Krait
  2. Copperhead
  3. Python
  4. Viper
  5. Boa constrictor

  answer: Types of snake!
```

### crossclimb
```
game      : crossclimb
number    : 846
date      : 2026-08-24
difficulty: None

Ladder (word : clue, top -> bottom):
  fish : The top + bottom rows = Two things found at the beach: one in the water, one on land. Keep in mind: The first word may be at the bottom.
  wish : A genie may grant one
  wise : Clever and experienced
  wine : Alcoholic drink made by fermenting grape juice
  wind : Weather measured on the Beaufort scale (8 means a gale, for example)
  wand : What a wizard wields
  sand : The top + bottom rows = Two things found at the beach: one in the water, one on land. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
