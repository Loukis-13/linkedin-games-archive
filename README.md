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
## Today's games (2026-10-27)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
|  1   ..    6   ..   ..    2 |
+                             +
| ..   ..   ..   ..    4   .. |
+                             +
| ..    8   ..   ..   ..   .. |
+                             +
|  7   ..   ..    3   ..    5 |
+                             +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | . | . | . | . |
+---+---+-x-+---+---+---+
| . | M | . | . | . | . |
+---+---+---+---+---+---+
| . | S | . | M | . | . |
+---+---+-=-+---+-=-+---+
| . | M | . | S | . | . |
+---+---+---+---+---+---+
| . | . | . | S | . | . |
+---+---+---+---+-=-+---+
| . | . | . | M | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟧
🟥🟨🟩🟩🟦🟦🟧
🟥🟨🟩🟪🟪🟦🟧
🟥🟨🟪🟪🟪🟫🟧
🟥🟨🟨🟨🟫🟫🟧
🟥🟨🟨🟨🟨🟨🟧
🟥🟧🟧🟧🟧🟧🟧
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │ 3 ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 2 ┃ 3 │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │ 5 ┃ 6 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃ 2 │ 3 │ 1 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | -  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | =  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| +2 | .. | .. | .. | +15 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +12 | .. | .. | .. | +7 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | =  | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| E | E | R | T | I |
+---+---+---+---+---+
| P | # | # | # | E |
+---+---+---+---+---+
| F | O | R | M | E |
+---+---+---+---+---+
| I | # | # | # | K |
+---+---+---+---+---+
| N | U | A | L | I |
+---+---+---+---+---+

Words:
  TIE
  PEER
  ALIKE
  UNIFORM
```

### pinpoint
```
  1. Port
  2. Shiraz
  3. Merlot
  4. Chardonnay
  5. Pinot noir (from dark grapes)

  answer: Types of wine!
```

### crossclimb
```
game      : crossclimb
number    : 910
date      : 2026-10-27
difficulty: None

Ladder (word : clue, top -> bottom):
  bald : The top + bottom rows = Something often found on top of the head, and a word for someone who lacks it. Keep in mind: The first word may be at the bottom.
  band : Word that can follow "rubber" or "marching"
  sand : Beach surface
  said : Spoke aloud
  sail : Travel using wind power
  hail : Solid precipitation
  hair : The top + bottom rows = Something often found on top of the head, and a word for someone who lacks it. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
