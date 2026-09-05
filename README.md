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
## Today's games (2026-09-05)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..    4   ..   ..    9   ..   .. |
+                                  +
| ..    7    5    3   12   ..   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+                                  +
| ..   ..    6    2   11   10   .. |
+                                  +
| ..   ..    8   ..   ..    1   .. |
+                                  +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | S | . = . |
+---+---+---+---+---+-x-+
| . | . | M | . | . | . |
+---+---+---+---+---+---+
| . | S | . | . | . | M |
+---+---+---+---+---+---+
| S | . | . | . | S | . |
+---+---+---+---+---+---+
| . | . | . | S | . | . |
+-x-+---+---+---+---+---+
| . x . | M | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟦🟦🟩🟩🟩⬜⬜⬜⬜
🟦🟨🟨🟨🟩⬜⬛⬛⬜
🟦🟨🟫🟫🟫⬜⬜⬛⬛
🟦🟨🟨🟨🟫🟪🟪🟪⬛
🟥🟥🟥🟨🟫🟪⬛⬛⬛
🟥🟨🟨🟨🟫🟪🟪🟪⬛
🟥🟥🟥🟫🟫🟫🟫🟪⬛
🟧🟧🟥🟫🟫🟪🟪🟪⬛
🟥🟥🟥⬛⬛⬛⬛⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │ 2 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │ 3 │   ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃   │ 2 │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 3 │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| +5 | .. | .. | .. | .. | +5 | .. |
+----+----+----+----+----+----+----+
| .. | +5 | .. | .. | .. | .. | |5 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |5 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | =  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| -  | .. | .. | .. | .. | +  | .. |
+----+----+----+----+----+----+----+
| .. | +  | .. | .. | .. | .. | +  |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| A | U | Q | L | O | O | S |
+---+---+---+---+---+---+---+
| R | # | A | # | # | H | C |
+---+---+---+---+---+---+---+
| I | # | # | # | # | # | H |
+---+---+---+---+---+---+---+
| U | # | S | # | # | I | S |
+---+---+---+---+---+---+---+
| M | L | L | W | A | F | L |
+---+---+---+---+---+---+---+
| G | I | S | H | T | A | E |
+---+---+---+---+---+---+---+
| F | R | E | R | E | N | G |
+---+---+---+---+---+---+---+

Words:
  GILLS
  SCHOOL
  AQUARIUM
  ANGELFISH
  FRESHWATER
```

### pinpoint
```
  1. Race
  2. Cable
  3. Muscle
  4. Rental
  5. Plug-in hybrid

  answer: Words that come before “car”!
```

### crossclimb
```
game      : crossclimb
number    : 858
date      : 2026-09-05
difficulty: None

Ladder (word : clue, top -> bottom):
  leia : The top + bottom rows = Two children of Darth Vader.
  leis : Flowery garlands used in hula dancing
  lets : Allows, or rents out a property
  lats : Muscles in the lower back, for short
  late : Not on time
  lute : Renaissance string instrument (adding an F to the start forms the name of a wind instrument)
  luke : The top + bottom rows = Two children of Darth Vader.
```
<!-- DAILY-GAMES-END -->
