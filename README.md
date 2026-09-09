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
## Today's games (2026-09-09)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..    7   ..   .. |
+                             +
| .. | ..    8    1   .. | .. |
+    +                   +    +
| .. | ..   ..   ..    2 | .. |
+    +---- ---- ---- ----+    +
| .. |  5   ..   ..   .. | .. |
+    +                   +    +
| .. | ..    4    6   .. | .. |
+    +                   +    +
| ..   ..    3   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . = . | . = . | . |
+---+---+---+---+---+---+
| . | S | M | S | M | . |
+---+---+---+---+---+---+
| . | . = . | . x . | . |
+---+---+---+---+---+---+
| . | M | S | S | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟨🟨🟨🟨🟨
🟥🟨🟩🟩🟨🟨🟨🟦
🟥🟨🟨🟨🟨🟨🟪🟦
🟥🟨🟨🟨🟨🟨🟪🟦
🟥🟨🟨🟨🟨🟨🟪🟨
🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟫🟫🟫🟫🟨🟨
🟨🟨🟨⬛⬛⬛⬛🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 2 │   ┃ 5 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃   │ 6 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 5 ┃   │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃   │ 1 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +6 | .. | +12 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | |5 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +10 | .. | .. | .. | +4 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |4 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | .. | +4 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| # | # | A | R | # |
+---+---+---+---+---+
| S | A | B | C | Y |
+---+---+---+---+---+
| T | H | # | D | R |
+---+---+---+---+---+
| A | G | F | E | H |
+---+---+---+---+---+
| # | Y | T | # | # |
+---+---+---+---+---+

Words:
  DRY
  CRAB
  HEFTY
  AGHAST
```

### pinpoint
```
  1. Iron
  2. Golden
  3. Middle
  4. Voting
  5. Coming of

  answer: Words that come before “age”!
```

### crossclimb
```
game      : crossclimb
number    : 862
date      : 2026-09-09
difficulty: None

Ladder (word : clue, top -> bottom):
  meat : The top + bottom rows = A two-word phrase for tasty pastries for carnivores. Keep in mind: The first word may be at the bottom.
  neat : Clean and organized
  near : Close by
  pear : Fruit shaped like a teardrop
  peer : Colleague who is an equal to you in age, job, and/or social status
  pier : Raised walkway that extends from the shore over water
  pies : The top + bottom rows = A two-word phrase for tasty pastries for carnivores. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
