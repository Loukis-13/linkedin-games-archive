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
## Today's games (2026-11-14)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   11 | 10   .. | ..   .. | ..   .. |
+         +         +         +         +
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   ..    3 |  1   .. | ..   ..    9 |
+              +         +          ----+
| ..   ..   ..   ..   ..   ..   ..    8 |
+          ----           ----          +
| 12   ..   ..   ..   ..   ..   ..   .. |
+----                                   +
|  4   ..   .. | ..    2 |  6   ..   .. |
+              +         +              +
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   .. | ..   .. | ..    5 |  7   .. |
+---- ----+---- ----+---- ----+---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . | M | M | . | . |
+-=-+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . | . | . | . | M |
+---+---+---+---+---+---+
| S | . | . | . | . | S |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+-x-+
| . | . | M | S | . x . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥⬜⬜⬜⬜⬜⬜
🟦🟥🟧🟧🟧⬜⬜⬜⬜
🟥🟥🟥🟧🟨🟨🟨⬜⬜
⬛⬛🟧🟧🟧🟨⬜⬜⬜
⬛⬛⬛⬛🟨🟨🟨⬜⬜
🟫🟪🟪🟪🟫🟩🟩🟩⬜
🟫🟫🟪🟫🟫🟫🟩⬜⬜
🟫🟪🟪🟪🟫🟩🟩🟩⬜
🟫🟫🟫🟫🟫🟫🟫⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 6 │   ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 5 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │   │   ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃   │ 1 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | -8 |
+----+----+----+----+----+----+----+----+
| .. | -4 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | -8 | .. |
+----+----+----+----+----+----+----+----+
| |6 | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | +8 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | +8 |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| P | O | R | O | P | I | E |
+---+---+---+---+---+---+---+
| S | # | D | C | E | T | R |
+---+---+---+---+---+---+---+
| S | # | N | # | H | A | C |
+---+---+---+---+---+---+---+
| S | # | I | # | C | # | I |
+---+---+---+---+---+---+---+
| E | N | A | # | T | # | L |
+---+---+---+---+---+---+---+
| K | E | R | R | A | # | P |
+---+---+---+---+---+---+---+
| I | L | S | C | T | R | I |
+---+---+---+---+---+---+---+

Words:
  COPIER
  SCRATCH
  LIKENESS
  RAINDROPS
  TRIPLICATE
```

### pinpoint
```
  1. Story
  2. Cut
  3. List
  4. Circuit
  5. And sweet (to the point)

  answer: Words that can follow “short”!
```

### crossclimb
```
game      : crossclimb
number    : 928
date      : 2026-11-14
difficulty: None

Ladder (word : clue, top -> bottom):
  case : The top + bottom rows = A compound word for something you pack for a trip. Keep in mind: The first word may be at the bottom.
  cast : Performers in a play, collectively
  fast : Like a Formula 1 car, when racing
  fait : ___ accompli (something already done)
  flit : Move swiftly, like a bee or butterfly
  slit : Long, very thin opening
  suit : The top + bottom rows = A compound word for something you pack for a trip. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
