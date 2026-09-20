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
## Today's games (2026-09-20)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+     ---- ----           ---- ----     +
| .. |  3   .. | ..    5 | ..   .. | .. |
+    +         +         +         +    +
| ..   ..    2   ..   ..    6   ..   .. |
+          ----           ----          +
| ..   .. | ..   ..    7   .. | 10   .. |
+         +                   +         +
| ..    4 | ..    1   ..   .. | ..   .. |
+         +----           ----+         +
| ..   ..    9   ..   ..   11   ..   .. |
+                                       +
| .. | ..   .. |  8   .. | ..   12 | .. |
+    +---- ----+         +---- ----+    +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . x . | . | . | M |
+---+---+---+---+---+---+
| M | S | . | . | . | M |
+---+---+---+---+-x-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | S | . | . | . | . |
+---+---+---+---+---+---+
| . | S | . | . | . x . |
+-x-+---+---+---+---+---+
| . | . | . | M | S | . |
+---+---+---+---+---+---+
```

### queens
```
⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬛🟦🟦🟪🟪🟪🟪⬜⬜
⬛🟥🟦🟦🟦🟨🟪⬜⬜
⬛🟥🟥🟩🟨🟨🟪⬜⬜
⬛🟧🟥🟩🟨🟨🟪⬜⬜
⬛🟧🟥🟩🟩🟨🟨⬜⬜
⬛🟧🟧🟧🟩🟨🟨⬜⬜
⬛⬛🟫🟫🟫🟫🟫⬜⬜
⬛⬛🟫🟫🟫🟫🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │ 2 ┃   │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 3 │ 4 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 5 │ 4 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃ 4 │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | +3 | .. |
+----+----+----+----+----+----+----+
| +3 | .. | -3 | .. | |3 | .. | +3 |
+----+----+----+----+----+----+----+
| .. | .. | .. | +3 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | .. | .. |
+----+----+----+----+----+----+----+
| |  | .. | |  | .. | =  | .. | |  |
+----+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | -  | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| T | W | S | # | # | # | # |
+---+---+---+---+---+---+---+
| E | E | I | N | G | R | A |
+---+---+---+---+---+---+---+
| A | B | C | D | E | F | G |
+---+---+---+---+---+---+---+
| R | # | N | # | N | # | R |
+---+---+---+---+---+---+---+
| G | F | E | D | C | B | A |
+---+---+---+---+---+---+---+
| A | I | N | E | O | E | N |
+---+---+---+---+---+---+---+
| # | # | # | # | B | W | T |
+---+---+---+---+---+---+---+

Words:
  DEN
  SWEET
  COBWEB
  FENCING
  FRAGRANT
  BARGAINED
```

### pinpoint
```
  1. Cargo ships
  2. Wrestling matches
  3. Climbing walls
  4. Bank accounts (after big deposits)
  5. Phone calls (“please wait!”)

  answer: Things with holds!
```

### crossclimb
```
game      : crossclimb
number    : 873
date      : 2026-09-20
difficulty: None

Ladder (word : clue, top -> bottom):
  foster : The top + bottom rows = A two-word phrase for a male family member who's not in your bloodline. Keep in mind: The first word may be at the bottom.
  poster : Large notice or picture hung on a wall
  pester : Irritate or bother
  fester : Become more irritating, like a problem you are ignoring
  faster : At a higher speed
  fatter : Stouter
  father : The top + bottom rows = A two-word phrase for a male family member who's not in your bloodline. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
