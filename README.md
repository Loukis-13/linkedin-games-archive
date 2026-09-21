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
## Today's games (2026-09-21)

### zip
```
+----+----+----+----+----+----+
| 10   ..   ..   ..   ..    3 |
+                             +
| ..   ..    1 | ..   ..   .. |
+              +              +
| ..    2   .. |  4   ..   .. |
+     ---- ----+---- ----     +
| ..   ..    8 | ..    5   .. |
+              +              +
| ..   ..   .. |  6   ..   .. |
+              +              +
|  9   ..   ..   ..   ..    7 |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | S | . | . | . | . |
+---+---+---+---+---+---+
| . = . | . | . | . = . |
+---+---+---+---+---+---+
| S | S | . | . | M | M |
+---+---+---+---+---+---+
| . = . | . | . | . = . |
+---+---+---+---+---+---+
| S | M | . | . | M | M |
+---+---+---+---+---+---+
| . | . | . | . | . = . |
+---+---+---+---+---+---+
```

### queens
```
🟦🟦🟦🟧🟧🟦🟦🟨
🟦🟩🟦🟧🟧🟦🟥🟨
🟦🟦🟦🟧🟧🟦🟥🟨
🟦🟦🟦🟦🟦🟦🟨🟨
🟦🟪🟪🟦🟦🟦🟨🟨
🟦🟪🟪🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟫🟫🟫🟦
🟦⬛⬛⬛⬛⬛🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │   ┃   │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │ 4 │   ┃   │ 6 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │   ┃   │ 4 │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃   │ 1 │ 2 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | +6 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | |  | +5 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | |  | +8 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | -  | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| T | C | B | O | J |
+---+---+---+---+---+
| J | E | P | M | # |
+---+---+---+---+---+
| E | D | A | U | # |
+---+---+---+---+---+
| U | J | # | J | # |
+---+---+---+---+---+
| S | T | # | # | # |
+---+---+---+---+---+

Words:
  JOB
  JUMP
  EJECT
  ADJUST
```

### pinpoint
```
  1. Pole
  2. Kiwi
  3. Dane
  4. Thai
  5. Chilean

  answer: Common national demonyms (i.e., names for people from a specific country)!
```

### crossclimb
```
game      : crossclimb
number    : 874
date      : 2026-09-21
difficulty: None

Ladder (word : clue, top -> bottom):
  rope : The top + bottom rows = Two things attached to a boat's mast.
  role : ___-playing game
  roll : Do a somersault
  toll : Cost to drive on some roadways
  toil : Work very hard
  tail : Wagging appendage
  sail : The top + bottom rows = Two things attached to a boat's mast.
```
<!-- DAILY-GAMES-END -->
