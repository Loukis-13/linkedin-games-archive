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
## Today's games (2026-09-04)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..    4   ..    3   ..   ..   ..   .. |
+                                       +
| ..    5   ..    6 | .. | .. | .. | .. |
+                   +    +    +    +    +
| ..    1   10    7 | .. | .. | .. | .. |
+                   +    +    +    +    +
| ..   ..   ..    8 | ..   ..   .. | .. |
+                   +---- ----     +    +
| ..   ..   ..    9   ..   .. | .. | .. |
+                             +    +    +
| ..   ..   ..    2   ..   .. | .. | .. |
+                             +    +    +
| ..   ..   ..   ..   ..   .. | ..   .. |
+---- ---- ---- ---- ---- ----+---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+-x-+---+-x-+---+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+-=-+---+---+---+---+---+
| . | . | M | . | M | . |
+---+---+---+---+---+---+
| . | . | M | . | M | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟧🟧🟧🟧
🟥🟨🟨🟨🟥🟩🟩🟩🟧
🟨🟨🟨🟨🟥🟨🟨🟩🟩
🟨🟨🟨🟨🟨🟨🟨🟨🟩
🟨🟨🟨🟨🟦🟩🟩🟩🟩
🟪🟦🟦🟦🟦🟦🟦🟦🟫
🟪🟪🟦🟦🟦🟦🟦⬛🟫
🟪🟪🟪🟦🟦🟦⬛⬛🟫
🟪⬜⬜⬜🟦⬛⬛🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 5 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 6 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │ 4 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. | -  |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +2 | +2 | +4 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | +2 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +3 | +3 | +6 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| -  | .. | .. | .. | .. | .. | |  |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| A | T | H | R | H | S |
+---+---+---+---+---+---+
| E | R | E | I | N | E |
+---+---+---+---+---+---+
| F | # | # | # | K | U |
+---+---+---+---+---+---+
| O | J | # | # | # | Q |
+---+---+---+---+---+---+
| R | A | M | E | T | I |
+---+---+---+---+---+---+
| I | T | Y | C | H | N |
+---+---+---+---+---+---+

Words:
  SHRINK
  FEATHER
  MAJORITY
  TECHNIQUE
```

### pinpoint
```
  1. Trains
  2. Music albums
  3. Adjustable ceiling lights
  4. Olympic stadiums for running
  5. Mud after animals walk in it

  answer: Things associated with tracks!
```

### crossclimb
```
game      : crossclimb
number    : 857
date      : 2026-09-04
difficulty: None

Ladder (word : clue, top -> bottom):
  drop : The top + bottom rows = A two-word phrase for a tennis stroke that lands the ball near the net. Keep in mind: The first word may be at the bottom.
  crop : Plant grown for human consumption
  coop : Where chickens live
  loop : Section of a roller coaster that may be particularly exciting or scary to ride around
  loot : Treasure found in a dungeon
  soot : Black powder in a chimney
  shot : The top + bottom rows = A two-word phrase for a tennis stroke that lands the ball near the net. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
