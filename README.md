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
## Today's games (2026-11-01)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   11   .. |
+                                       +
| ..    4    5   ..   ..   ..   12   .. |
+                                       +
| ..   ..   ..   ..    6   ..   ..   .. |
+                                       +
|  7    1   ..   ..    3   ..   ..   .. |
+                                       +
| ..   ..   ..   16   ..   ..   13   10 |
+                                       +
| ..   ..   ..    9   ..   ..   ..   .. |
+                                       +
| ..    2   ..   ..   ..   15   14   .. |
+                                       +
| ..    8   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | M | S | . | . x . |
+---+---+---+---+---+-x-+
| M | . | . | . | . | . |
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+-=-+
| . | . | . | . | . | . |
+-=-+---+---+---+---+-x-+
| . x . | . | . = . x . |
+---+---+---+---+---+---+
```

### queens
```
⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜🟥🟫⬛⬛⬛⬜⬜⬜
🟥🟥🟫⬛🟧⬛⬜⬜⬜
🟪🟥🟫🟧🟧⬛⬛🟨⬜
🟪🟥🟫🟫🟧⬛🟨🟨⬜
🟥🟥🟥🟫🟧⬛⬛🟨⬜
🟩🟩🟩🟧🟧🟧⬛🟨⬜
🟦🟦🟩🟩🟩🟩🟨🟨🟨
🟦🟦🟦🟦🟦🟩🟩🟩🟩
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃   │ 2 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃ 5 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃ 4 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │ 1 ┃ 3 │ 4 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | .. | .. | -  |
+----+----+----+----+----+----+----+----+
| .. | |4 | .. | .. | .. | .. | +  | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | .. | +3 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | =4 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +4 | .. | .. | .. | +5 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +  | .. | .. | .. | .. | -6 | .. |
+----+----+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. | .. | +7 |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| N | O | V | N | V | O | N |
+---+---+---+---+---+---+---+
| N | # | A | O | E | # | R |
+---+---+---+---+---+---+---+
| I | V | T | I | R | S | U |
+---+---+---+---+---+---+---+
| L | O | N | O | V | U | T |
+---+---+---+---+---+---+---+
| C | N | O | L | E | P | E |
+---+---+---+---+---+---+---+
| A | # | I | S | A | # | R |
+---+---+---+---+---+---+---+
| N | O | V | I | V | O | N |
+---+---+---+---+---+---+---+

Words:
  NOVEL
  VISION
  VOLCANO
  TURNOVER
  SUPERNOVA
  INNOVATION
```

### pinpoint
```
  1. Hard
  2. Digital
  3. Advance
  4. Backup
  5. Carbon (the second c of cc)

  answer: Words that come before “copy”!
```

### crossclimb
```
game      : crossclimb
number    : 915
date      : 2026-11-01
difficulty: None

Ladder (word : clue, top -> bottom):
  fall : The top + bottom rows = A two-word phrase for what some people do when Daylight Saving Time ends. Keep in mind: The first word may be at the bottom.
  call : ___ and response
  cull : Remove, as the least useful part
  bull : Male elephant
  bulk : Majority portion
  buck : Attempt to throw a rider off
  back : The top + bottom rows = A two-word phrase for what some people do when Daylight Saving Time ends. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
