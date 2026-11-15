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
## Today's games (2026-11-15)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..    5 |
+                                       +
| ..   ..   ..   ..   .. |  8   ..   .. |
+                    ----+----          +
| ..    7 | ..   ..   .. | ..   ..   .. |
+     ----+----          +              +
| ..   .. |  2   ..   ..   ..   ..   .. |
+         +                             +
| ..   ..   ..   ..   ..    6 | ..   .. |
+                         ----+----     +
| ..   ..   .. | ..   ..   .. |  1   .. |
+          ----+----          +         +
| ..   ..    4 | ..   ..   ..   ..   .. |
+              +                        +
|  3   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | M | S | . | . | . |
+---+---+---+---+---+---+
| M | M | S | . | . | . |
+---+---+---+---+---+---+
| M | S | M | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . = . x . |
+---+---+---+---+---+---+
| . | . | . | . x . = . |
+---+---+---+---+---+---+
| . | . | . | . = . x . |
+---+---+---+---+---+---+
```

### queens
```
🟩🟩⬛⬛⬛⬛🟨🟨🟨
🟩⬛⬛⬜⬛⬛⬛⬛🟨
⬛⬛⬛⬜⬜⬛⬛⬛🟨
⬛⬛🟦🟦⬜🟦🟦🟦🟦
⬛⬛🟦🟦🟥🟧🟧🟧🟦
⬛🟦🟦🟦🟥🟦🟦🟦🟦
🟪🟦🟦🟦🟥🟦🟦🟦🟦
🟪🟦🟦🟦🟥🟦🟦🟦🟫
🟪🟪🟪🟦🟦🟦🟦🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │   ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 5 ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 6 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | .. | .. | .. | +  |
+----+----+----+----+----+----+----+----+
| .. | +6 | .. | .. | +3 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+----+
| .. | +3 | -  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | -  | +4 | .. |
+----+----+----+----+----+----+----+----+
| .. | -  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | +6 | .. | .. | +9 | .. |
+----+----+----+----+----+----+----+----+
| +  | .. | .. | .. | +3 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| # | Y | R | E | L | N | # |
+---+---+---+---+---+---+---+
| S | R | U | L | A | O | I |
+---+---+---+---+---+---+---+
| S | U | X | # | X | A | T |
+---+---+---+---+---+---+---+
| E | R | # | # | # | L | I |
+---+---+---+---+---+---+---+
| K | P | X | # | X | I | A |
+---+---+---+---+---+---+---+
| O | O | E | A | U | Y | R |
+---+---+---+---+---+---+---+
| # | B | T | X | E | T | # |
+---+---+---+---+---+---+---+

Words:
  LUXURY
  EXPRESS
  TEXTBOOK
  AUXILIARY
  RELAXATION
```

### pinpoint
```
  1. Doors
  2. Canals
  3. Hair
  4. Wrestling (e.g., arm or head)
  5. Safes (open with the right #s)

  answer: Things with locks!
```

### crossclimb
```
game      : crossclimb
number    : 929
date      : 2026-11-15
difficulty: None

Ladder (word : clue, top -> bottom):
  flats : The top + bottom rows = Musical notes that are a half-step lower than naturals, and a word describing their opposite. Keep in mind: The first word may be at the bottom.
  slats : Parts of Venetian blinds
  stats : Data used in analysis of athletes, for short
  state : Express clearly, as a case in court
  stare : Look without blinking
  share : Don't keep all to yourself
  sharp : The top + bottom rows = Musical notes that are a half-step lower than naturals, and a word describing their opposite. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
