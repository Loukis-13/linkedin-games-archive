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
## Today's games (2026-11-19)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..    3   ..   ..   .. |
+     ----                ----     +
| .. | ..   ..    1   ..   .. | .. |
+    +                        +    +
| ..   ..   ..    4   ..   ..   .. |
+                                  +
| ..    7   10   11    5    2   .. |
+                                  +
| ..   ..   ..    9   ..   ..   .. |
+                                  +
| .. | ..   ..    8   ..   .. | .. |
+    +----                ----+    +
| ..   ..   ..    6   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | M | S | M | . |
+---+---+---+---+---+---+
| M | . | . | . | . | M |
+---+---+---+---+---+---+
| M | . | . x . | . | M |
+---+---+-=-+-=-+---+---+
| S | . | . x . | . | S |
+---+---+---+---+---+---+
| S | . | . | . | . | M |
+---+---+---+---+---+---+
| . | M | S | M | S | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟧🟧🟧🟧🟧
🟨🟩🟩🟦🟧🟧🟧🟧
🟨🟩🟦🟦🟦🟪🟧🟧
🟨🟩🟫⬛⬛🟪🟪🟧
🟨🟫🟫⬛⬛🟪🟧🟧
🟨🟨🟫⬛⬛⬛🟧🟧
🟨🟨🟨🟨⬛🟧🟧🟧
🟨🟨🟨🟧🟧🟧🟧🟧
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 3 │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │   │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 5 │ 6 ┃ 1 │   │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | +3 | .. | +3 | .. |
+----+----+----+----+----+----+
| .. | =  | .. | +3 | .. | +3 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| +4 | .. | +4 | .. | =  | .. |
+----+----+----+----+----+----+
| .. | +4 | .. | +4 | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| M | B | I | T | E | R |
+---+---+---+---+---+---+
| O | # | N | # | N | # |
+---+---+---+---+---+---+
| C | Y | A | D | O | G |
+---+---+---+---+---+---+
| # | E | # | E | # | A |
+---+---+---+---+---+---+
| O | N | S | N | E | X |
+---+---+---+---+---+---+
| H | # | E | # | H | # |
+---+---+---+---+---+---+

Words:
  DENSE
  RETINA
  HEXAGON
  HONEYCOMB
```

### pinpoint
```
  1. House
  2. Mind
  3. Secret
  4. Mic
  5. Sesame (it’s a magical phrase)

  answer: Words that come after “open”!
```

### crossclimb
```
game      : crossclimb
number    : 933
date      : 2026-11-19
difficulty: None

Ladder (word : clue, top -> bottom):
  care : The top + bottom rows = A hyphenated word for looking after your own well-being. Keep in mind: The first word may be at the bottom.
  cure : Medicine to eliminate a disease
  curl : Lock of hair that isn't straight
  cull : Gather, as from a larger set
  cell : One box in a spreadsheet
  sell : Opposite of "buy"
  self : The top + bottom rows = A hyphenated word for looking after your own well-being. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
