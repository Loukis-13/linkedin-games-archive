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
## Today's games (2026-08-23)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   13   ..   12   ..   10   ..   .. |
+                                       +
| ..    3    4   ..   11   ..    9   .. |
+     ----      ----           ----     +
| ..   ..   ..   ..   ..   ..   ..   .. |
+----      ----           ----      ----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+     ----           ----      ----     +
| ..    1   ..    5   ..    8   14   .. |
+                                       +
| ..   ..    2   ..    7   ..    6   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | . x . = . x . | . |
+---+---+---+---+-=-+---+
| . | . | . | . | . | . |
+-x-+---+---+---+-x-+---+
| . | . | . | . | . | . |
+-x-+---+---+---+-=-+---+
| . | . | . | . | . | . |
+-=-+---+---+---+-x-+---+
| . x . x . x . = . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟩🟩🟩🟨🟨🟨🟧🟧🟧
🟩🟩🟩🟩🟩🟨🟨🟨🟧
🟩🟦⬛⬛⬛⬛🟨🟧🟧
🟩🟦⬛⬛🟫⬛⬛🟧🟥
🟩🟦⬛🟫🟫🟫⬛🟥🟥
🟩🟩⬛⬛🟫⬛⬛🟥⬜
🟩🟩🟩⬛⬛⬛⬛🟥⬜
🟩🟩🟩🟩❓❓❓🟥⬜
❓❓❓❓❓⬜⬜⬜⬜
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 2 │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 1 ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃ 4 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 6 │   │ 5 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | +8 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | -6 | .. |
+----+----+----+----+----+----+----+----+
| .. | +4 | .. | .. | -5 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | +7 |
+----+----+----+----+----+----+----+----+
| +5 | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | -12 | .. | .. | +4 | .. |
+----+----+----+----+----+----+----+----+
| .. | -6 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +7 | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| E | # | # | T | Y | P | E |
+---+---+---+---+---+---+---+
| Q | U | I | T | E | T | W |
+---+---+---+---+---+---+---+
| R | P | R | Y | R | I | R |
+---+---+---+---+---+---+---+
| O | Y | E | P | R | I | U |
+---+---+---+---+---+---+---+
| T | T | W | O | E | P | Q |
+---+---+---+---+---+---+---+
| O | I | R | O | I | R | E |
+---+---+---+---+---+---+---+
| T | Y | P | E | # | # | R |
+---+---+---+---+---+---+---+

Words:
  POWER
  EQUITY
  REQUIRE
  PRIORITY
  PROTOTYPE
  TYPEWRITER
```

### pinpoint
```
  1. Tank
  2. Piece
  3. Twice
  4. Out loud
  5. Outside the box

  answer: Words that come after “think”!
```

### crossclimb
```
game      : crossclimb
number    : 845
date      : 2026-08-23
difficulty: None

Ladder (word : clue, top -> bottom):
  buses : The top + bottom rows = Two plural nouns for types of vehicles you could pay to go across town.
  ruses : Deceptive tricks
  runes : Letters a Norse god might use
  tunes : Catchy ditties
  tuxes : Men's formalwear options, for short
  taxes : Charges added at the end of a sales receipt
  taxis : The top + bottom rows = Two plural nouns for types of vehicles you could pay to go across town.
```
<!-- DAILY-GAMES-END -->
