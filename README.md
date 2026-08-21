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
## Today's games (2026-08-21)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+     ----           ---- ----     +
| ..    2   .. |  7   ..    9 | .. |
+              +              +    +
| .. | ..   ..   ..   ..   .. | .. |
+    +     ----               +    +
| ..    5   ..    1   ..    8   .. |
+                    ----          +
| .. | ..   ..   ..   ..   .. | .. |
+    +                        +    +
| .. |  4   ..    3 | ..    6   .. |
+    +---- ----     +     ----     +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+---+---+---+---+---+
| S | . | . | . | . | . |
+---+-=-+---+---+---+---+
| . | . x . | S | . | . |
+---+---+---+---+---+---+
| . | . | S | . = . | . |
+---+---+---+---+-=-+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟧🟨🟨
🟩🟥🟧🟧🟧🟧🟨🟨
🟩🟥🟦🟧🟧🟨🟨🟨
🟩🟩🟦🟦🟧🟨🟨🟨
🟩🟩🟩🟦🟦🟨🟨🟨
🟩🟪🟩🟩🟩🟫🟫🟫
⬛🟪🟪🟩🟩🟫🟫🟫
⬛🟪🟪🟪🟩🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 2 ┃ 3 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 5 │ 3 ┃ 2 │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | =4 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | .. | |  | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | .. | .. | +3 |
+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | +4 | .. | .. |
+----+----+----+----+----+----+----+
| +5 | .. | .. | +4 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | -  | .. | .. | +4 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | -4 | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| N | D | E | A | S | T |
+---+---+---+---+---+---+
| A | E | R | C | # | # |
+---+---+---+---+---+---+
| Y | M | # | D | A | T |
+---+---+---+---+---+---+
| G | E | T | # | O | C |
+---+---+---+---+---+---+
| # | # | A | B | R | A |
+---+---+---+---+---+---+
| S | T | R | I | M | P |
+---+---+---+---+---+---+

Words:
  IMPACT
  MEANDER
  STRATEGY
  BROADCAST
```

### pinpoint
```
  1. A video
  2. A glance
  3. The messenger
  4. Fish in a barrel
  5. Oneself in the foot

  answer: Things you might “shoot”!
```

### crossclimb
```
game      : crossclimb
number    : 843
date      : 2026-08-21
difficulty: None

Ladder (word : clue, top -> bottom):
  fire : The top + bottom rows = A two-word phrase for a retail event in which everything must go, no matter the price. Keep in mind: The first word may be at the bottom.
  five : What a V stood for, in ancient Rome
  dive : Emulate an Olympian who starts on a board
  dime : American currency that is roughly equivalent to a ten-pence coin
  dame : Title bestowed on a woman in Britain
  same : Identical
  sale : The top + bottom rows = A two-word phrase for a retail event in which everything must go, no matter the price. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
