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
## Today's games (2026-10-16)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..    2   14   ..   .. |
+                                  +
| ..   ..    4   ..   ..    1   .. |
+                                  +
| ..    3   ..   ..   ..   ..   13 |
+                                  +
|  7   ..   ..   ..   ..   ..   12 |
+                                  +
|  8   ..   ..   ..   ..    5   .. |
+                                  +
| ..   10   ..   ..    6   ..   .. |
+                                  +
| ..   ..    9   11   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| S | . | M | . | M | . |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+-=-+---+---+---+---+
| M | . | S | . | M | . |
+---+---+---+-x-+---+---+
| . | . x . | . | . | . |
+---+---+---+---+---+---+
| M | . | M | . | S | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟧🟧
🟥🟥🟥🟨🟩🟥🟥🟧
🟥🟥🟨🟨🟩🟩🟥🟧
🟥🟥🟨🟦🟦🟩🟥🟪
🟥🟥🟥🟦🟦🟥🟥🟪
🟫🟥⬛⬛⬛⬛🟥🟥
🟫🟫⬛⬛⬛⬛🟥🟥
🟫🟫🟫⬛⬛🟥🟥🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 4 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 2 ┃ 5 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 2 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 4 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │ 4 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | +3 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +6 | .. | =  | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | |  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |  | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | +12 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +3 | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | S | E | L | A | C |
+---+---+---+---+---+---+
| T | I | H | T | T | I |
+---+---+---+---+---+---+
| E | S | # | # | C | A |
+---+---+---+---+---+---+
| K | N | # | # | S | R |
+---+---+---+---+---+---+
| O | A | L | B | C | P |
+---+---+---+---+---+---+
| I | R | A | N | E | # |
+---+---+---+---+---+---+

Words:
  THESIS
  BLANKET
  SCENARIO
  PRACTICAL
```

### pinpoint
```
  1. Off
  2. Cord
  3. Tide
  4. To pieces
  5. -Roaring success

  answer: Words that come after “rip”!
```

### crossclimb
```
game      : crossclimb
number    : 899
date      : 2026-10-16
difficulty: None

Ladder (word : clue, top -> bottom):
  sled : The top + bottom rows = A two-word phrase for animals that may work in snowy conditions. Keep in mind: The first word may be at the bottom.
  seed : A tree may grow from it
  feed : Give a supply of nutrients
  fees : Charges for professional services
  foes : Opposing forces
  fogs : Weather patterns that may be described as "pea soup"
  dogs : The top + bottom rows = A two-word phrase for animals that may work in snowy conditions. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
