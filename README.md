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
## Today's games (2026-11-17)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
| ..    1    2   ..   ..   .. |
+                             +
| ..    8   .. | .. |  4   .. |
+     ----     +    +----     +
| ..    5 | .. | ..    3   .. |
+         +    +              +
| ..   ..   ..    7    6   .. |
+                             +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | S | . | . | . | . |
+---+---+---+---+-=-+---+
| M | S | M | . = . x . |
+---+---+---+---+---+---+
| . = . x . | S | M | S |
+---+-=-+---+---+---+---+
| . | . | . | . | S | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟧🟥🟨
🟦🟦🟦🟦🟩🟧🟥🟨
🟦🟦🟦🟪🟩🟧🟥🟨
🟦🟫⬛🟪🟩🟧🟥🟨
🟦🟫⬛🟪🟩🟧🟥🟨
🟦🟦⬛🟪🟩🟧🟥🟨
🟦🟦🟦🟦🟦🟦🟥🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 6 │ 2 ┃ 3 │ 5 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │ 3 ┃ 4 │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃ 5 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 5 ┃ 6 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | +3 | +6 | .. | .. | .. |
+----+----+----+----+----+----+
| +2 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |  |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | -  |
+----+----+----+----+----+----+
| .. | .. | .. | =  | -  | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| # | # | T | # | # |
+---+---+---+---+---+
| G | E | T | I | M |
+---+---+---+---+---+
| A | S | T | U | N |
+---+---+---+---+---+
| T | C | # | E | T |
+---+---+---+---+---+
| T | O | # | O | T |
+---+---+---+---+---+

Words:
  TOE
  MITT
  STUNT
  COTTAGE
```

### pinpoint
```
  1. Mandible
  2. Patella
  3. Coccyx
  4. Sternum
  5. Humerus ("the funny ___")

  answer: Names of bones!
```

### crossclimb
```
game      : crossclimb
number    : 931
date      : 2026-11-17
difficulty: None

Ladder (word : clue, top -> bottom):
  kite : The top + bottom rows = A flying toy, and a long part of it that provides decoration and stability. Keep in mind: The first word may be at the bottom.
  rite : ___ of passage (important life event)
  rile : Make angry or agitated
  tile : Square piece in many board games
  till : Cash drawer in a store
  tall : Having great height
  tail : The top + bottom rows = A flying toy, and a long part of it that provides decoration and stability. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
