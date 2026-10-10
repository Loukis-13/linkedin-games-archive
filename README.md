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
## Today's games (2026-10-10)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..    7   ..   ..   ..   .. |
+                                  +
| ..   ..   .. |  8   ..    1   .. |
+          ----+----               +
| ..   ..   ..   ..   .. | ..   .. |
+                    ----+         +
| ..   .. |  3   ..    4 | ..   .. |
+         +----          +         +
| ..   .. | ..   ..   ..   ..   .. |
+         +     ---- ----          +
| ..    6   ..    5 | ..   ..   .. |
+                   +              +
| ..   ..   ..   ..    2   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | M | S | . | . | . |
+---+---+---+---+---+---+
| M | . | M | . | . = . |
+---+---+---+---+---+---+
| S | M | M | . | . | . |
+---+---+---+---+---+-=-+
| . | . | . | . | . | . |
+---+-x-+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+-x-+
| . | . x . | . x . | . |
+---+---+---+---+---+---+
```

### queens
```
🟧🟧🟧🟥🟫🟫🟫🟫🟫
🟧🟧🟥🟥🟥🟨🟫🟫🟫
🟧🟧🟩🟥🟨🟨🟨🟫🟫
🟧🟩🟩🟩🟦🟨🟫🟫🟫
🟧🟪🟩🟦🟦🟦🟫🟫🟫
🟪🟪🟪⬜🟦🟫🟫🟫⬛
🟫🟪⬜⬜⬜🟫🟫⬛⬛
🟫🟫🟫⬜🟫🟫⬛⬛⬛
🟫🟫🟫🟫🟫⬛⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │ 4 │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │   │   ┃   │ 4 │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 1 │ 5 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+----+
| .. | +6 | .. | +9 | .. | .. | .. | |  |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | -  | .. |
+----+----+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| -  | .. | .. | .. | +9 | .. | +4 | .. |
+----+----+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | +12 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+---+
| # | # | U | # | # | # | # | # |
+---+---+---+---+---+---+---+---+
| # | G | P | R | E | C | T | # |
+---+---+---+---+---+---+---+---+
| # | R | E | I | D | S | I | R |
+---+---+---+---+---+---+---+---+
| # | A | D | R | O | U | G | # |
+---+---+---+---+---+---+---+---+
| # | F | T | E | E | T | H | # |
+---+---+---+---+---+---+---+---+
| L | E | O | V | O | L | N | # |
+---+---+---+---+---+---+---+---+
| # | D | E | D | A | O | W | # |
+---+---+---+---+---+---+---+---+
| # | # | # | # | # | D | # | # |
+---+---+---+---+---+---+---+---+

Words:
  DIRECT
  UPGRADE
  LEFTOVER
  RIGHTEOUS
  DOWNLOADED
```

### pinpoint
```
  1. Hang
  2. Perfect
  3. Top
  4. Count to
  5. Nine times out of

  answer: Words that come before “ten”!
```

### crossclimb
```
game      : crossclimb
number    : 893
date      : 2026-10-10
difficulty: None

Ladder (word : clue, top -> bottom):
  lane : The top + bottom rows = The first and last name of Superman's main love interest. Keep in mind: The first name may be at the bottom.
  cane : Walking aid
  cans : Cylindrical containers
  cabs : Some hired rides, for short
  labs : Places for science experiments
  lobs : High shots, in tennis
  lois : The top + bottom rows = The first and last name of Superman's main love interest. Keep in mind: The first name may be at the bottom.
```
<!-- DAILY-GAMES-END -->
