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
## Today's games (2026-10-14)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+     ----           ----     +
| ..    8   ..   ..   ..    7 |
+     ----           ----     +
| ..    6   ..   ..   ..    2 |
+     ----           ----     +
|  5   ..   ..   ..    1   .. |
+     ----           ----     +
|  4   ..   ..   ..    3   .. |
+     ----           ----     +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+-=-+---+---+
| . | . | M | . | . | . |
+---+---+---+---+---+---+
| . | . | M | . = . | . |
+---+-=-+---+---+---+---+
| M | . | S | S | . | . |
+---+---+---+---+---+---+
| S | . x . | . | . | . |
+---+---+---+---+---+---+
| M | M | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟪🟨🟨🟨
🟥🟥🟩🟪🟩🟨🟨
🟥🟥🟩🟩🟩🟨🟨
🟦🟦🟦🟩🟨🟨🟨
🟦🟦🟦🟧🟨🟨🟨
🟦🟫🟦🟧🟧🟨🟨
🟦🟫🟫🟫🟧🟧🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 1 │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │ 4 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 2 │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │ 1 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 3 │ 4 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | |2 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| |  | .. | =9 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | |4 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +2 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +6 | .. | +  |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +2 | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| # | T | # | T | T |
+---+---+---+---+---+
| E | U | O | A | I |
+---+---+---+---+---+
| G | C | G | D | R |
+---+---+---+---+---+
| A | A | E | U | E |
+---+---+---+---+---+
| B | B | # | B | # |
+---+---+---+---+---+

Words:
  OUT
  BUDGE
  ATTIRE
  CABBAGE
```

### pinpoint
```
  1. The dog
  2. The streets
  3. The line
  4. The plank
  5. A tightrope (take no false steps!)

  answer: Things you can “walk”!
```

### crossclimb
```
game      : crossclimb
number    : 897
date      : 2026-10-14
difficulty: None

Ladder (word : clue, top -> bottom):
  nine : The top + bottom rows = A hyphenated word describing a golf course that's half as long as usual. Keep in mind: The first word may be at the bottom.
  nice : Pleasant, or the name of a city in France
  mice : Computer peripherals used for clicking
  mace : Medieval club, often with spiky bits
  male : Like a bull or ram, but not a cow or ewe
  mole : Critter that digs tunnels
  hole : The top + bottom rows = A hyphenated word describing a golf course that's half as long as usual. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
