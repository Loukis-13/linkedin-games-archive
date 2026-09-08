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
## Today's games (2026-09-08)

### zip
```
+----+----+----+----+----+----+----+
|  4   ..   ..   ..   ..   ..    5 |
+          ---- ----               +
| ..   .. | ..   ..   .. | ..   .. |
+         +     ----     +         +
|  1   .. | ..   ..   .. | ..    6 |
+         +     ----     +         +
| ..   .. | ..   ..   .. | ..   .. |
+         +     ----     +         +
|  2   .. | ..   ..   .. | ..    7 |
+         +     ----     +         +
| ..   .. | ..   ..   .. | ..   .. |
+         +     ---- ----+         +
|  3   ..   ..   ..   ..   ..    8 |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . x . | S | S | . |
+---+-x-+---+---+---+---+
| . | . | . | . | S | . |
+---+---+---+---+---+---+
| . | M | . = . | M | . |
+---+---+---+---+---+---+
| . | S | . | . | . | . |
+---+---+---+---+-x-+---+
| . | M | M | . x . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟧🟨🟨🟨
🟥🟥🟧🟧🟧🟨🟨
🟥🟥🟥🟧🟧🟧🟨
🟥🟥🟥🟥🟪🟦🟦
🟥🟥🟥🟪🟪🟫🟦
🟥🟥🟩🟩🟩🟫🟦
🟥🟩🟩🟩🟩🟫🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 2 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │ 4 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │ 6 │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 1 │ 5 │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 2 │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 3 │ 4 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | |6 | +  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | =4 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +8 |
+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| |2 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +  | =4 | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| H | T | C | A | S |
+---+---+---+---+---+
| E | J | # | # | C |
+---+---+---+---+---+
| O | E | T | D | A |
+---+---+---+---+---+
| R | # | # | E | S |
+---+---+---+---+---+
| Y | T | A | U | Q |
+---+---+---+---+---+

Words:
  JET
  SQUAT
  THEORY
  CASCADE
```

### pinpoint
```
  1. Crust
  2. Mantle
  3. Core (mostly iron and nickel)
  4. Tectonic plates
  5. Magnetic poles (North+South)

  answer: Parts of the Earth!
```

### crossclimb
```
game      : crossclimb
number    : 861
date      : 2026-09-08
difficulty: None

Ladder (word : clue, top -> bottom):
  rule : The top + bottom rows = A two-word phrase for something that comes with a complex boardgame to explain how to play. Keep in mind: The first word may be at the bottom.
  role : Part to play in a project or organization
  hole : One of eighteen on a typical golf course
  hold : “Please ___” (don’t hang up the phone)
  hood : Feature of a raincoat that covers the head
  hook : Captain ___ (Peter Pan character, whose name is also something attached to his arm)
  book : The top + bottom rows = A two-word phrase for something that comes with a complex boardgame to explain how to play. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
