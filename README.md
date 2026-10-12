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
## Today's games (2026-10-12)

### zip
```
+----+----+----+----+----+----+
| ..   ..   10    1   ..   .. |
+                             +
| ..   12   ..   ..   11   .. |
+                             +
|  9   ..   ..   ..   ..    2 |
+                             +
|  8   ..   ..   ..   ..    3 |
+                             +
| ..    6   ..   ..    5   .. |
+                             +
| ..   ..    7    4   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . x . | . = . | . |
+-=-+---+---+---+---+-x-+
| . | M | S | . | S | . |
+---+---+---+---+---+---+
| . | . | . | . | M | . |
+-x-+---+---+---+---+-x-+
| . | S | . | . | . | . |
+---+---+---+---+---+---+
| . | M | . | S | S | . |
+-=-+---+---+---+---+-x-+
| . | . x . | . = . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟧🟧
🟨🟧🟧🟧🟧🟧🟧
🟨🟨🟨🟨🟨🟨🟩
🟦🟦🟩🟩🟩🟩🟩
🟦🟦🟦🟦🟪🟪🟪
🟫🟫🟫🟫🟫🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │ 5 ┃ 1 │   │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │ 4 ┃ 6 │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 3 ┃ 2 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 2 ┃ 5 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 4 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +6 | .. | .. | .. | =9 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| |4 | .. | +6 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +2 | .. | =4 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | -3 | .. | .. | .. | +2 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| Y | # | N | E | B |
+---+---+---+---+---+
| T | # | D | L | E |
+---+---+---+---+---+
| E | # | V | # | M |
+---+---+---+---+---+
| I | R | A | # | O |
+---+---+---+---+---+
| C | U | T | # | N |
+---+---+---+---+---+

Words:
  CUT
  BEND
  LEMON
  VARIETY
```

### pinpoint
```
  1. General
  2. Private
  3. Major
  4. Colonel
  5. Lieutenant

  answer: Military ranks!
```

### crossclimb
```
game      : crossclimb
number    : 895
date      : 2026-10-12
difficulty: None

Ladder (word : clue, top -> bottom):
  spin : The top + bottom rows = Two words meaning to rotate.
  shin : Part of the lower leg that might ache for a runner
  chin : Central part of a jawline
  coin : Metallic piece of currency
  corn : Vegetable that may be served on or off the cob
  torn : Ripped in half
  turn : The top + bottom rows = Two words meaning to rotate.
```
<!-- DAILY-GAMES-END -->
