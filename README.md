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
## Today's games (2026-10-21)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
| ..   ..    3    5   ..   .. |
+                             +
| ..   ..   ..    8    6   .. |
+                             +
| ..    2    7   ..   ..   .. |
+                             +
| ..   ..    1    4   ..   .. |
+                             +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | M | S | M | . |
+---+---+---+---+---+---+
| . | . | . | M | M | . |
+---+-x-+---+---+---+---+
| . | . = . | . | S | . |
+---+-=-+-=-+---+---+---+
| . | . = . x . | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟧🟧🟧🟧
🟥🟨🟨🟨🟧🟩🟧
🟥🟥🟥🟨🟧🟦🟧
🟥🟪🟥🟨🟧🟦🟧
🟪🟪🟪🟫🟧🟦🟧
🟫🟫🟫🟫🟧🟦🟧
🟫🟫🟫🟫🟧🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 2 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │   ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃   │   │ 2 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 4 │ 2 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | +8 | .. | .. | .. | +7 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | |6 | .. | |6 | .. | |8 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| +8 | .. | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| M | E | O | M | # |
+---+---+---+---+---+
| O | A | T | H | Y |
+---+---+---+---+---+
| I | S | # | R | B |
+---+---+---+---+---+
| B | C | D | I | P |
+---+---+---+---+---+
| # | I | S | Y | H |
+---+---+---+---+---+

Words:
  ATOM
  BIOME
  HYBRID
  PHYSICS
```

### pinpoint
```
  1. Gallery
  2. Bar
  3. Bench
  4. Witness box
  5. Judge’s chambers

  answer: Things seen at a court!
```

### crossclimb
```
game      : crossclimb
number    : 904
date      : 2026-10-21
difficulty: None

Ladder (word : clue, top -> bottom):
  fair : The top + bottom rows = A two-word phrase for a legitimate target for criticism, or an unbiased sporting competition. Keep in mind: The first word may be at the bottom.
  fail : Opposite of "succeed"
  fall : Tumble to the ground
  ball : What gets hit in golf or tennis
  bale : Bundle of hay or straw
  gale : Strong wind
  game : The top + bottom rows = A two-word phrase for a legitimate target for criticism, or an unbiased sporting competition. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
