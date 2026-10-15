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
## Today's games (2026-10-15)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+     ---- ----                    +
| .. |  2   ..   ..    6    7   .. |
+    +                             +
| .. | ..   ..   ..    1    8   .. |
+    +---- ----                    +
| ..   ..   ..   ..   ..   ..   .. |
+                    ---- ----     +
| ..    9    4   ..   ..   .. | .. |
+                             +    +
| ..   10    3   ..   ..    5 | .. |
+                    ---- ----+    +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | M | . | . | . |
+---+---+---+---+---+---+
| . | S | M | . | . | . |
+---+---+---+---+---+---+
| . | M | . | . | . | . |
+---+---+---+-x-+---+---+
| . | S | . | . | . | . |
+---+---+---+-=-+---+---+
| . | . | . | . | . | . |
+---+---+---+-x-+---+---+
| . | . | . | . = . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟧🟧🟧🟨🟨🟨🟥
🟥🟧🟧🟧🟩🟩🟩🟥
🟥🟧🟧🟥🟥🟥🟥🟥
🟥🟥🟥🟥🟥🟦🟦🟥
🟪🟫🟫🟫🟦🟦🟦🟥
🟪🟫⬛⬛🟦🟦🟦🟥
🟪🟪🟪🟪🟪🟥🟥🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │ 4 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 3 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 5 │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +5 | .. | +3 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +4 | .. | .. | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | -5 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| +6 | .. | |5 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |5 | .. | +4 |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | |5 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | .. | +6 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +3 | .. | +5 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | # | # | M | U | M |
+---+---+---+---+---+---+
| M | A | X | I | L | E |
+---+---+---+---+---+---+
| # | # | E | T | S | A |
+---+---+---+---+---+---+
| A | G | L | B | # | # |
+---+---+---+---+---+---+
| N | I | G | M | I | N |
+---+---+---+---+---+---+
| T | I | C | # | # | # |
+---+---+---+---+---+---+

Words:
  LEAST
  NIMBLE
  MAXIMUM
  GIGANTIC
```

### pinpoint
```
  1. Drum
  2. Bass
  3. Sole
  4. Perch
  5. Flounder

  answer: Types of fish!
```

### crossclimb
```
game      : crossclimb
number    : 898
date      : 2026-10-15
difficulty: None

Ladder (word : clue, top -> bottom):
  folk : The top + bottom rows = A two-word phrase for a music genre that often features acoustic guitars and socially conscious lyrics. Keep in mind: The first word may be at the bottom.
  fold : Drop out of a poker hand
  food : What many farms generate
  hood : Robin ___ (legendary outlaw)
  hook : It's at the end of a fishing line
  rook : Game piece that moves up and down and side to side, but not diagonally
  rock : The top + bottom rows = A two-word phrase for a music genre that often features acoustic guitars and socially conscious lyrics. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
