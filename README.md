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
## Today's games (2026-10-23)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..    1    2   ..   ..    3   18   .. |
+                                       +
| ..    8    9   ..   ..   10   17   .. |
+                                       +
| ..   ..   ..   12   11   ..   ..   .. |
+                                       +
| ..   ..   ..   14   15   ..   ..   .. |
+                                       +
| ..    7   13   ..   ..   16   20   .. |
+                                       +
| ..    6    5   ..   ..    4   19   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | S | S |
+---+-x-+---+---+---+---+
| . x . x . | . | . | S |
+---+-x-+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+-x-+---+
| S | . | . | . x . x . |
+---+---+---+---+-=-+---+
| S | M | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟫🟫🟦🟦🟦⬛⬛⬛
🟫🟦🟦🟩🟩⬛⬛⬛
🟫🟦🟥🟥🟩🟩⬛⬛
🟫🟦🟥🟧🟧🟩⬛⬛
🟫🟫🟥🟧🟧🟩🟪⬛
🟫🟫🟨🟨🟨🟩🟪⬛
🟫🟫🟫🟨🟨🟪🟪⬛
🟫🟫🟫🟪🟪🟪⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │ 2 ┃   │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │ 5 ┃   │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃ 2 │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │   ┃ 4 │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | +6 | .. |
+----+----+----+----+----+----+
| .. | +4 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | -  | .. |
+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +8 | .. |
+----+----+----+----+----+----+
| .. | +6 | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | # | # | # | # | T |
+---+---+---+---+---+---+
| T | T | # | T | A | R |
+---+---+---+---+---+---+
| O | E | R | O | N | S |
+---+---+---+---+---+---+
| N | O | I | T | E | M |
+---+---+---+---+---+---+
| U | I | T | # | T | I |
+---+---+---+---+---+---+
| T | # | # | # | # | # |
+---+---+---+---+---+---+

Words:
  TOTE
  OTTER
  TUITION
  TRANSMIT
```

### pinpoint
```
  1. Yellow
  2. Ob
  3. Indus
  4. Tigris
  5. Yangtze (continent’s longest)

  answer: Rivers in Asia!
```

### crossclimb
```
game      : crossclimb
number    : 906
date      : 2026-10-23
difficulty: None

Ladder (word : clue, top -> bottom):
  fest : The top + bottom rows = A compound word for a gathering where people praise and appreciate each other. Keep in mind: The first word may be at the bottom.
  pest : Irritating child or insect
  post : Put online, like a LinkedIn update
  pose : Something a fashion model "strikes"
  dose : Amount of medicine
  dove : Peaceful bird on a United Nations postage stamp
  love : The top + bottom rows = A compound word for a gathering where people praise and appreciate each other. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
