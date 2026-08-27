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
## Today's games (2026-08-27)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+     ---- ---- ---- ----     +
| ..   ..    1   ..    4   .. |
+                             +
| ..    5   ..   ..    8   .. |
+                             +
| ..    6   ..   ..    3   .. |
+                             +
| ..    7   ..    2   ..   .. |
+     ---- ---- ---- ----     +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| . | . | M | S | . | . |
+---+---+---+---+---+---+
| . | M | . | . | M | . |
+-=-+---+---+---+---+-=-+
| . | S | . | . | M | . |
+---+---+---+---+---+---+
| . | . | M | S | . | . |
+---+---+---+---+---+---+
| . | . | . x . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟨🟨⬛⬛
🟥🟥🟧🟥🟥🟩⬛⬛
🟥🟧🟧🟧🟩🟩🟩⬛
🟥🟥🟧🟦🟦🟩🟥⬛
🟥🟥🟪🟦🟦🟫🟥🟥
🟥🟪🟪🟪🟫🟫🟫🟥
🟥🟥🟪🟥🟥🟫🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │ 4 ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 6 │   ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 5 │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │ 5 ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 4 │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | +3 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | |4 | .. | .. |
+----+----+----+----+----+----+
| -  | .. | .. | .. | +5 | .. |
+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | |  |
+----+----+----+----+----+----+
| .. | .. | -4 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +5 | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| L | I | C | O | R | # |
+---+---+---+---+---+---+
| I | S | P | # | N | N |
+---+---+---+---+---+---+
| C | P | O | # | # | O |
+---+---+---+---+---+---+
| O | # | # | A | T | I |
+---+---+---+---+---+---+
| N | R | # | T | S | E |
+---+---+---+---+---+---+
| # | E | L | I | E | V |
+---+---+---+---+---+---+

Words:
  SILICON
  POPCORN
  RELIEVE
  STATION
```

### pinpoint
```
  1. Octopuses
  2. Arctic hares (twice a year)
  3. Mood rings
  4. Leaves (in autumn)
  5. Chameleons

  answer: Things that change colors!
```

### crossclimb
```
game      : crossclimb
number    : 849
date      : 2026-08-27
difficulty: None

Ladder (word : clue, top -> bottom):
  said : The top + bottom words = Two words that complete the idiom “Easier ___ than ___.” Keep in mind: The first word may be at the bottom.
  laid : Produced an egg, as a hen
  land : Country, or the end of several country names
  lane : Playing area used for ten-pin bowling
  cane : Walking aid held in one hand
  cone : Geometric shape with a circular base that rises to a single vertex
  done : The top + bottom words = Two words that complete the idiom “Easier ___ than ___.” Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
