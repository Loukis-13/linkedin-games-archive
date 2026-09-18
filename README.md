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
## Today's games (2026-09-18)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..    2   ..   .. |
+                             +
| ..   ..   ..   ..    5   .. |
+                             +
| ..   ..    8   ..    4   .. |
+                             +
| ..    6   ..    7   ..   .. |
+                             +
| ..    3   ..   ..   ..   .. |
+                             +
| ..   ..    1   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| S | . | S | . | . | . |
+---+---+---+---+---+---+
| M | S | S | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+-x-+---+---+
| . | . | . | . | . | . |
+---+---+---+-x-+---+-=-+
| . | . | . | . x . = . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟨🟨🟨🟨🟨🟨🟨
🟥🟨🟨🟨🟨🟨🟧🟧
🟥🟥🟨🟨🟨🟧🟧🟦
🟩🟥🟥🟥🟧🟧⬛🟦
🟩🟩🟪🟪🟪⬛⬛🟦
🟪🟪🟪🟫⬛⬛🟦🟦
🟫🟫🟫🟫⬛⬛🟦🟦
🟫🟫🟫🟫⬛⬛🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │   ┃ 2 │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 4 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 6 │   │ 5 ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 6 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +  | +4 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +4 | .. | .. | +  | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +8 | .. | .. | +  | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +  | +3 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| D | Y | H | C | H | N |
+---+---+---+---+---+---+
| R | # | A | E | # | O |
+---+---+---+---+---+---+
| A | T | T | T | O | L |
+---+---+---+---+---+---+
| E | E | T | T | G | Y |
+---+---+---+---+---+---+
| T | # | R | H | # | D |
+---+---+---+---+---+---+
| U | B | I | R | E | A |
+---+---+---+---+---+---+

Words:
  THREAD
  HYDRATE
  ATTRIBUTE
  TECHNOLOGY
```

### pinpoint
```
  1. Sandy Desert
  2. Salt Lake
  3. Rift Valley
  4. Barrier Reef
  5. Britain: England+Scotland+Wales

  answer: Geographic place names when preceded by “Great”!
```

### crossclimb
```
game      : crossclimb
number    : 871
date      : 2026-09-18
difficulty: None

Ladder (word : clue, top -> bottom):
  wind : The top + bottom rows = A two-word phrase for an easterly current considered mild and favorable. Keep in mind: The first word may be at the bottom.
  rind : Outer part of a lemon
  rend : Tear apart
  rent : Monthly apartment payment
  bent : Out of shape or crooked
  best : The tops, quality-wise
  west : The top + bottom rows = A two-word phrase for an easterly current considered mild and favorable. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
