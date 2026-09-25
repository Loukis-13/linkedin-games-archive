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
## Today's games (2026-09-25)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+     ----                         +
| .. |  5   ..    4    9   ..   .. |
+    +          ---- ----          +
| ..   ..   ..   ..    7 | ..   .. |
+                        +         +
| ..    1 | ..   ..   .. | 10   .. |
+         +              +         +
| ..   .. |  6   ..   ..   ..   .. |
+         +---- ----               +
| ..   ..    2    3   ..    8 | .. |
+                         ----+    +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . x . | M | . | . | . |
+---+-x-+---+-x-+---+---+
| . | . | M | . x . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . = . | S | . | . |
+---+---+-x-+---+-x-+---+
| . | . | . | S | . = . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟧🟨🟨🟨🟨
🟥🟧🟧🟧🟨🟩🟩🟨
🟥🟧🟧🟧🟦🟩🟧🟧
🟥🟧🟧🟦🟦🟧🟧🟧
🟧🟧🟪🟪🟧🟧🟫🟫
🟧🟧🟪🟧🟧🟧🟫🟫
🟧🟧🟧🟧🟧🟧🟧🟧
🟧🟧⬛⬛⬛⬛🟧🟧
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 2 ┃ 3 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │ 2 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │ 3 ┃ 2 │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| +14 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | |  | .. | +9 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +6 | .. | =  | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | +5 |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| W | E | # | # | # | N | D |
+---+---+---+---+---+---+---+
| # | A | V | E | D | E | # |
+---+---+---+---+---+---+---+
| # | N | T | O | I | V | # |
+---+---+---+---+---+---+---+
| # | E | I | R | Y | I | # |
+---+---+---+---+---+---+---+
| # | V | N | O | S | D | # |
+---+---+---+---+---+---+---+
| # | I | N | C | T | U | # |
+---+---+---+---+---+---+---+
| G | A | # | # | # | M | E |
+---+---+---+---+---+---+---+

Words:
  GAIN
  WEAVE
  COSTUME
  DIVIDEND
  INVENTORY
```

### pinpoint
```
  1. Media
  2. Bag
  3. Blessing
  4. Metaphor
  5. Messages (contradictory ideas)

  answer: Words that come after “mixed”!
```

### crossclimb
```
game      : crossclimb
number    : 878
date      : 2026-09-25
difficulty: None

Ladder (word : clue, top -> bottom):
  beds : The top + bottom rows = A two-word phrase for pieces of furniture that fold out for sleeping. Keep in mind: The first word may be at the bottom.
  bods : Physiques, colloquially
  bode : Be an omen
  code : Do a programmer's job
  coda : Element at the end of a song
  soda : Carbonated water
  sofa : The top + bottom rows = A two-word phrase for pieces of furniture that fold out for sleeping. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
