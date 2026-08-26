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
## Today's games (2026-08-26)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   13    1    3   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..   14   ..    9   ..    2   .. |
+                                  +
| ..   15   ..    8   ..    6   .. |
+                                  +
| ..   12   ..    7   ..    5   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..   11   10    4   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| . | . | M | M | . | . |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| . | S | M | S | S | . |
+---+---+---+---+---+---+
| . = . x . | . x . x . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥
🟧🟧🟧🟧🟧🟨🟥
🟧🟩🟩🟨🟨🟨🟥
🟩🟩🟩🟨🟦🟦🟥
🟪🟪🟪🟦🟦🟥🟥
🟫🟫🟪🟦🟥🟥🟥
🟪🟪🟪🟥🟥🟥🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 2 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │ 5 ┃ 6 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 6 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 6 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 1 ┃ 2 │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 6 ┃ 5 │ 1 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+
| .. | |6 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | |3 | .. | .. | |  |
+----+----+----+----+----+----+
| |  | .. | .. | |3 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | |3 | .. |
+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| E | T | # | E | R |
+---+---+---+---+---+
| L | S | I | S | E |
+---+---+---+---+---+
| T | S | S | S | L |
+---+---+---+---+---+
| # | I | I | I | # |
+---+---+---+---+---+
| W | H | G | H | T |
+---+---+---+---+---+

Words:
  ISLE
  SIGHT
  RESIST
  WHISTLE
```

### pinpoint
```
  1. Twist
  2. Floss
  3. Robot
  4. Moonwalk
  5. Macarena

  answer: Names of dance crazes (with "The")!
```

### crossclimb
```
game      : crossclimb
number    : 848
date      : 2026-08-26
difficulty: None

Ladder (word : clue, top -> bottom):
  load : The top + bottom rows = A compound word for transferring data from an online source to a local computer. Keep in mind: The first word may be at the bottom.
  lord : “The ___ of the Rings” (fantasy epic published in three parts)
  cord : Word after power, spinal, or vocal
  corn : Vegetable that can be eaten “on the cob”
  torn : Ripped apart, as scraps of paper
  town : Human residential area smaller than a city
  down : The top + bottom rows = A compound word for transferring data from an online source to a local computer. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
