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
## Today's games (2026-08-28)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..    8 |
+                             +
| ..    6   ..    3   ..   .. |
+                             +
| ..   ..   ..   ..    4   .. |
+                             +
| ..    7   ..   ..   ..   .. |
+                             +
| ..   ..    1   ..    5   .. |
+                             +
|  2   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | M | . | . | M |
+---+-x-+---+---+---+---+
| . | . | . | . | . x . |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+---+---+---+---+---+---+
| M | . | . | . | . | . |
+---+---+---+---+---+---+
| . = . | . | . | . | . |
+---+---+---+---+-x-+---+
| S | . | . | S | . | S |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥🟧🟧
🟥🟥🟥🟥🟨🟥🟥🟥🟧
🟥🟥🟩🟥🟨🟥🟥🟥🟥
🟩🟩🟩🟨🟨🟨🟦🟦🟦
🟩🟨🟨🟨🟪🟨🟨🟨🟦
🟩🟩🟩🟨🟪🟨🟦🟦🟦
🟩🟫🟫🟪🟪🟪⬛⬛🟦
🟩🟫🟪🟪🟪🟪🟪⬜🟦
🟩⬜⬜⬜⬜⬜⬜⬜🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │   ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃ 5 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │   ┃ 6 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃   │   │ 2 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 2 ┃   │   │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃   │   │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | .. | +5 |
+----+----+----+----+----+----+----+
| .. | .. | .. | +3 | .. | .. | .. |
+----+----+----+----+----+----+----+
| +6 | .. | -4 | .. | .. | |4 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | |6 | .. | .. | =4 | .. | +5 |
+----+----+----+----+----+----+----+
| .. | .. | .. | +3 | .. | .. | .. |
+----+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | -  | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| W | A | Y | U | A | N |
+---+---+---+---+---+---+
| A | # | I | G | # | A |
+---+---+---+---+---+---+
| V | A | Y | T | A | N |
+---+---+---+---+---+---+
| A | # | M | O | # | A |
+---+---+---+---+---+---+
| I | A | C | R | A | C |
+---+---+---+---+---+---+
| L | # | C | U | # | Y |
+---+---+---+---+---+---+

Words:
  AWAY
  AVAIL
  IGUANA
  ANATOMY
  ACCURACY
```

### pinpoint
```
  1. Will
  2. Trade
  3. Rein
  4. Speech
  5. As a bird

  answer: Words that come after “free”!
```

### crossclimb
```
game      : crossclimb
number    : 850
date      : 2026-08-28
difficulty: None

Ladder (word : clue, top -> bottom):
  jack : The top + bottom rows = A compound word for what is paid out by slot machines (also known as fruit machines or poker machines). Keep in mind: The first word may be at the bottom.
  back : Returned from a trip abroad
  bach : Johann Sebastian ___ (German composer)
  bath : Alternative to a shower
  path : Route from one place to another
  pats : Gently touches, as a pet dog
  pots : The top + bottom rows = A compound word for what is paid out by slot machines (also known as fruit machines or poker machines). Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
