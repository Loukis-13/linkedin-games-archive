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
## Today's games (2026-08-12)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..    3 |
+                             +
| ..   12   11    5    4   .. |
+                             +
| ..   ..   .. | ..    6   .. |
+          ----+----          +
| ..   10   .. | ..   ..   .. |
+              +              +
| ..    1    9    7    8   .. |
+                             +
|  2   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | . = . | M | . |
+---+---+---+---+---+---+
| . | . | M | S | . | . |
+---+-x-+---+---+-x-+---+
| . | . | M | M | . | . |
+---+---+---+---+---+---+
| . | S | . x . | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟧🟧🟨
🟥🟧🟧🟧🟧🟧🟧🟨
🟥🟧🟧🟧🟧🟧🟨🟨
🟩🟧🟧🟧🟧🟦🟦🟦
🟩🟩🟩🟧🟧🟧🟧🟦
🟪🟫🟫🟫🟧🟧🟧⬛
🟪🟧🟧🟫🟧🟧🟧⬛
🟪🟪🟧🟧🟧🟧⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │   ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │ 4 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 5 │ 6 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 3 │ 5 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 1 │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃   │   │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| +  | .. | +  | .. | +  | .. | +  |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +7 | .. | +10 | .. | +5 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| +3 | .. | +5 | .. | +3 | .. | +3 |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| J | U | N | A | J |
+---+---+---+---+---+
| R | A | G | L | A |
+---+---+---+---+---+
| T | F | # | E | R |
+---+---+---+---+---+
| I | F | A | S | I |
+---+---+---+---+---+
| C | # | B | # | C |
+---+---+---+---+---+

Words:
  AJAR
  BASIC
  JUNGLE
  TRAFFIC
```

### pinpoint
```
  1. Electric current
  2. Personal pronoun
  3. Square root of -1
  4. Iodine
  5. Roman numeral for 1

  answer: Different meanings of the letter “I”!
```

### crossclimb
```
game      : crossclimb
number    : 834
date      : 2026-08-12
difficulty: None
Ladder (word : clue, top -> bottom):
  back : The top + bottom rows = A two-word phrase for what you might do after you get a telephone message. Keep in mind: The first word may be at the bottom.
  bask : Loll in the sun
  base : Something used to neutralize an acid
  bale : Bundle of straw or hay
  tale : Something Hans Christian Andersen wrote
  tall : Having above-average height
  call : The top + bottom rows = A two-word phrase for what you might do after you get a telephone message. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
