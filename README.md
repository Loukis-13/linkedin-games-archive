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
## Today's games (2026-10-04)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| .. |  7   .. | .. |  8   ..   ..   .. |
+    +         +    +                   +
| ..   .. | ..   ..   ..   .. |  9   .. |
+         +     ---- ----     +         +
| ..    2   ..   ..   ..   ..    6   .. |
+          ----           ----          +
| ..    3   ..   ..   ..   ..    5   .. |
+               ---- ----               +
| ..   10 | ..   ..   ..   .. | ..   .. |
+         +                   +         +
| ..   ..   ..    1 | .. | ..    4 | .. |
+                   +    +         +    +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . x . | . | . x . |
+-=-+---+---+---+---+-x-+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+-=-+---+---+---+---+---+
| . x . | . | S | S | M |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟧🟥🟥🟥🟨🟨🟨🟥
🟥🟧🟧🟧🟧🟧🟨🟥🟥
🟥🟧🟩🟦🟦🟦🟨🟥🟦
🟩🟩🟩🟪🟦🟥🟥🟥🟦
🟫🟫🟩🟪🟦🟦🟦🟦🟦
🟫⬜🟪🟪🟪🟦🟦🟦⬛
🟫⬜⬜⬜🟦🟦🟦🟦⬛
🟫🟦🟦🟦🟦🟦🟦⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃ 1 │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 4 │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │ 6 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 6 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │ 5 ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| +6 | .. | .. | .. | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+----+
| .. | -6 | .. | .. | .. | .. | |2 | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +2 | .. | .. | +4 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +2 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | |6 | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | -6 | .. | .. | .. | .. | |6 | .. |
+----+----+----+----+----+----+----+----+
| +6 | .. | .. | .. | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| T | A | E | R | T | E | G |
+---+---+---+---+---+---+---+
| S | C | I | G | F | A | R |
+---+---+---+---+---+---+---+
| # | N | E | # | A | T | # |
+---+---+---+---+---+---+---+
| # | C | O | # | O | L | # |
+---+---+---+---+---+---+---+
| # | E | P | # | I | C | # |
+---+---+---+---+---+---+---+
| I | T | T | I | A | I | G |
+---+---+---+---+---+---+---+
| C | S | I | M | N | M | A |
+---+---+---+---+---+---+---+

Words:
  LOAF
  GREAT
  TARGET
  SCIENCE
  MAGICIAN
  OPTIMISTIC
```

### pinpoint
```
  1. George Lazenby
  2. Pierce Brosnan
  3. Roger Moore
  4. Daniel Craig
  5. Sean Connery (first in "Dr. No")

  answer: Actors who have played James Bond!
```

### crossclimb
```
game      : crossclimb
number    : 887
date      : 2026-10-04
difficulty: None

Ladder (word : clue, top -> bottom):
  lima : The top + bottom rows = Two consecutive letters in the NATO phonetic alphabet. Keep in mind: The first word may be at the bottom.
  lime : Green citrus fruit
  time : "___ flies when you're having fun"
  tile : Piece of material often used to cover a floor or wall
  tilt : Lean over a little
  kilt : Pleated garment associated with Scotland
  kilo : The top + bottom rows = Two consecutive letters in the NATO phonetic alphabet. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
