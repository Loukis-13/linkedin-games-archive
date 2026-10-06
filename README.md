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
## Today's games (2026-10-06)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..    5   ..    7 |
+                             +
| ..    6   ..   ..   ..   .. |
+                             +
| ..   ..   ..   ..   ..    8 |
+                             +
|  4   ..   ..   ..   ..   .. |
+                             +
| ..   ..   ..   ..    1   .. |
+                             +
|  2   ..    3   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | M | S | M | . |
+---+---+---+---+---+---+
| . | M | M | S | S | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+-=-+---+---+-x-+---+
| . | . | . x . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥
🟧🟧🟧🟥🟨🟨🟨
🟧🟩🟩🟥🟨🟥🟨
🟧🟧🟧🟥🟥🟥🟨
🟧🟦🟧🟪🟪🟥🟨
🟧🟧🟧🟪🟪🟥🟨
🟫🟫🟫🟫🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃   │ 2 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 6 │   │ 4 ┃ 3 │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 1 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +  | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | =4 | =9 | .. | .. |
+----+----+----+----+----+----+
| +3 | .. | .. | .. | .. | +5 |
+----+----+----+----+----+----+
| .. | .. | +3 | +3 | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| M | # | # | # | # | D |
+---+---+---+---+---+---+
| A | # | E | X | # | E |
+---+---+---+---+---+---+
| X | E | T | T | U | R |
+---+---+---+---+---+---+
| C | E | L | T | R | E |
+---+---+---+---+---+---+
| X | # | E | X | # | M |
+---+---+---+---+---+---+
| E | # | # | # | # | E |
+---+---+---+---+---+---+

Words:
  EXAM
  EXCEL
  EXTREME
  TEXTURED
```

### pinpoint
```
  1. Hamlet
  2. Conurbation
  3. Village
  4. Town
  5. City

  answer: Settlements of different size!
```

### crossclimb
```
game      : crossclimb
number    : 889
date      : 2026-10-06
difficulty: None

Ladder (word : clue, top -> bottom):
  cork : The top + bottom rows = A two-word term for the stopper in a bottle of Chardonnay or Chianti. Keep in mind: The first word may be at the bottom.
  core : Uneaten part of an apple
  care : Feel sympathy
  cave : Where to find stalactites
  wave : Arm gesture meaning "hello" or "goodbye"
  wane : Become less visible, like the moon
  wine : The top + bottom rows = A two-word term for the stopper in a bottle of Chardonnay or Chianti. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
