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
## Today's games (2026-09-26)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..    2   ..   .. |
+                                  +
| ..    7   ..    6   ..   ..   .. |
+                                  +
|  1   ..   ..   ..   ..    3   .. |
+                                  +
| ..   ..   10   ..    5   ..   .. |
+                                  +
| ..   11   ..   ..   ..   ..    4 |
+                                  +
| ..   ..   ..   12   ..    8   .. |
+                                  +
| ..   ..    9   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | S | S | . = . | . |
+-x-+---+---+---+---+-x-+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | . | . | . | . | S |
+---+---+---+---+---+---+
| S | . | . | . | . | S |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+-x-+---+---+---+---+-=-+
| . | . x . | S | M | . |
+---+---+---+---+---+---+
```

### queens
```
🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟥🟥🟥🟦🟦🟩🟦🟦
🟦🟦🟥🟫🟫🟫🟩🟦🟦
🟦🟦🟥🟨🟫🟩🟩🟩🟦
🟧🟧🟧🟨🟨🟨⬛⬛🟦
⬛🟧🟪🟨⬜⬜⬜⬛🟦
⬛🟧🟪🟪🟪⬜⬛⬛🟦
⬛⬛🟪⬛⬛⬜⬛⬛🟦
⬛⬛⬛⬛⬛⬛⬛🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │ 2 ┃ 3 │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 2 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │ 1 ┃ 4 │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| =  | .. | .. | .. | =  | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | .. | .. | =  |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | +  | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | +  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| E | M | I | # | C | P | I |
+---+---+---+---+---+---+---+
| P | O | C | # | I | T | C |
+---+---+---+---+---+---+---+
| G | C | R | # | T | U | C |
+---+---+---+---+---+---+---+
| R | S | O | O | P | R | I |
+---+---+---+---+---+---+---+
| A | P | # | # | # | E | N |
+---+---+---+---+---+---+---+
| S | H | # | C | I | T | E |
+---+---+---+---+---+---+---+
| C | I | # | # | # | A | M |
+---+---+---+---+---+---+---+

Words:
  OPTIC
  PICTURE
  GRAPHICS
  CINEMATIC
  MICROSCOPE
```

### pinpoint
```
  1. Tip
  2. Dot
  3. Exact location
  4. Main idea
  5. Scoring unit in a game

  answer: Different definitions of “point”!
```

### crossclimb
```
game      : crossclimb
number    : 879
date      : 2026-09-26
difficulty: None

Ladder (word : clue, top -> bottom):
  sweep : The top + bottom rows = A two-word phrase for victory in every part of a competition. Keep in mind: The first word may be at the bottom.
  sheep : Animals often herded by dogs
  cheep : Little sound from a nest
  cheap : Crude and unimaginative, as a trick
  cheat : Peek at a classmate's test, say
  cleat : Spike in a World Cup player's footwear
  clean : The top + bottom rows = A two-word phrase for victory in every part of a competition. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
