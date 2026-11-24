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
## Today's games (2026-11-24)

### zip
```
+----+----+----+----+----+----+
| ..    4   ..   .. | ..   .. |
+                   +         +
| ..    6   ..   .. | ..   .. |
+                   +         +
| .. | ..    5   ..   .. | .. |
+    +                   +    +
| .. | ..   ..    2   .. | .. |
+    +                   +    +
| ..   .. | ..   ..    3   .. |
+         +                   +
| ..   .. | ..   ..    1   .. |
+---- ----+---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | . | . | M | . |
+---+---+---+---+---+---+
| . | M | . | . | S | . |
+---+---+---+---+---+---+
| . | S | . = . | S | . |
+---+---+-=-+-x-+---+---+
| . | M | . x . | M | . |
+---+---+---+---+---+---+
| . | S | . | . | M | . |
+---+---+---+---+---+---+
| . | S | . | . | S | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥
🟥🟧🟧🟧🟥🟥🟥
🟥🟨🟦🟩🟩🟩🟩
🟥🟨🟦🟩🟩🟩🟩
🟥🟨🟨🟪🟪🟪🟩
🟥🟨🟨🟨🟫🟩🟩
🟨🟨🟨🟨🟫🟩🟩
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 3 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 3 ┃ 4 │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │ 5 ┃ 6 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 6 │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | |2 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| +2 | .. | =4 | .. | +4 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | +6 | .. | |6 | .. | +6 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | -6 | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| D | D | # | # | D |
+---+---+---+---+---+
| I | U | P | T | U |
+---+---+---+---+---+
| N | G | # | Y | B |
+---+---+---+---+---+
| I | T | R | E | U |
+---+---+---+---+---+
| F | # | # | F | F |
+---+---+---+---+---+

Words:
  FIT
  DUTY
  BUFFER
  PUDDING
```

### pinpoint
```
  1. Timon
  2. Cressida
  3. Cleopatra
  4. Othello
  5. Romeo and Juliet

  answer: Title characters from Shakespeare’s plays!
```

### crossclimb
```
game      : crossclimb
number    : 938
date      : 2026-11-24
difficulty: None

Ladder (word : clue, top -> bottom):
  page : The top + bottom rows = A compound word for the part of a website that many users see first. Keep in mind: The first word may be at the bottom.
  pale : Without much color
  pile : Disorderly stack
  pipe : Long object that water flows through
  pope : The current one is Leo XIV
  hope : Feeling that things could work out well
  home : The top + bottom rows = A compound word for the part of a website that many users see first. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
