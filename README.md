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
## Today's games (2026-09-17)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                    ----     +
| ..   ..   .. |  1   .. | .. |
+          ----+         +    +
| .. |  4   ..    6 | ..   .. |
+    +              +         +
| ..   .. |  5   ..    2 | .. |
+         +     ----     +    +
| .. | ..    3 | ..   ..   .. |
+    +----     +              +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | M | S | . | . | . |
+---+---+---+---+---+---+
| M | . | M | . | . | . |
+---+---+---+---+---+---+
| S | M | S | . x . = . |
+---+---+---+-=-+---+-=-+
| M | . | . | . | . | . |
+---+---+---+-x-+---+-x-+
| . | . | . | . = . x . |
+---+---+---+-=-+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟧🟧🟧
🟧🟨🟩🟩🟧🟧🟧🟧
🟧🟨🟨🟨🟦🟦🟧🟧
🟧🟨🟨🟨🟨🟨🟪🟧
🟧🟧🟨🟨🟨🟨🟪🟧
🟧🟧🟨🟨🟫🟫🟧🟧
🟧🟧⬛⬛🟧🟧🟧🟧
🟧🟧🟧🟧🟧🟧🟧🟧
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │   ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 3 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | |  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | -  | .. | |  | +  |
+----+----+----+----+----+----+
| +  | |  | .. | -  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | -  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| A | C | T | I | T | Y |
+---+---+---+---+---+---+
| # | # | I | V | T | Y |
+---+---+---+---+---+---+
| A | L | L | I | S | # |
+---+---+---+---+---+---+
| # | T | A | N | E | Z |
+---+---+---+---+---+---+
| B | I | V | E | # | # |
+---+---+---+---+---+---+
| B | A | R | N | O | Z |
+---+---+---+---+---+---+

Words:
  ZONE
  ZESTY
  RABBIT
  VANILLA
  ACTIVITY
```

### pinpoint
```
  1. Nuts
  2. Bananas
  3. Cold turkey
  4. Viral
  5. The extra mile

  answer: Words that come after “go” in common sayings!
```

### crossclimb
```
game      : crossclimb
number    : 870
date      : 2026-09-17
difficulty: None

Ladder (word : clue, top -> bottom):
  fast : The top + bottom rows = Two words that complete the idiom “a ___ and ___ rule” meaning something that is fixed and cannot easily be changed. Keep in mind: The first word may be at the bottom.
  fest : Gathering or celebration (often used as a suffix, as after Oktober)
  feat : Impressive achievement requiring a fair amount of skill
  heat : Make warm
  head : “Hit the nail on the ___”
  herd : Group of cattle
  hard : The top + bottom rows = Two words that complete the idiom “a ___ and ___ rule” meaning something that is fixed and cannot easily be changed. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
