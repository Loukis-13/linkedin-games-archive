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
## Today's games (2026-11-08)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
|  1 |  2   ..   10   ..   ..    9   .. |
+    +                                  +
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..    7   ..   ..    4   ..   ..    8 |
+                                       +
|  3   ..   ..    5   ..   ..   14   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..    6   ..   ..   12   ..   11 | 13 |
+                                  +    +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . | . | . | . | . |
+---+---+---+---+---+-=-+
| . | . x . | . | . | . |
+---+---+---+---+-=-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+-x-+---+---+---+---+
| . | . | . | M | M | . |
+-x-+---+---+---+---+---+
| . | . | . | . | S | S |
+---+---+---+---+---+---+
```

### queens
```
🟩🟩🟩🟩🟩🟩⬛⬛⬛
🟩🟦🟦🟦🟦🟩🟩🟩⬛
🟩🟦🟦🟥🟦🟩🟩🟩⬛
🟩🟦🟥🟥🟦🟪🟪🟪🟪
🟩🟦🟦🟦🟦🟦🟦🟦🟪
🟩🟩🟩🟩🟦🟦🟧🟦🟪
⬜🟩🟩🟨🟦🟧🟧🟦🟫
⬜🟩🟨🟨🟦🟦🟦🟦🟫
⬜⬜⬜🟨🟨🟨🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 2 ┃   │   │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃ 1 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │ 6 ┃ 5 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | =  | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | |  | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | =  | .. |
+----+----+----+----+----+----+----+----+
| -  | .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. | |8 |
+----+----+----+----+----+----+----+----+
| .. | -8 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | -8 | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |8 | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| # | H | I | D | E | # | # |
+---+---+---+---+---+---+---+
| T | C | N | G | S | I | U |
+---+---+---+---+---+---+---+
| E | F | E | C | I | S | G |
+---+---+---+---+---+---+---+
| # | # | A | N | D | # | # |
+---+---+---+---+---+---+---+
| C | H | L | O | F | S | N |
+---+---+---+---+---+---+---+
| R | A | E | C | L | A | E |
+---+---+---+---+---+---+---+
| # | # | S | E | E | K | # |
+---+---+---+---+---+---+---+

Words:
  FLEE
  SNEAK
  SEARCH
  CONCEAL
  FETCHING
  DISGUISED
```

### pinpoint
```
  1. Rules
  2. Control
  3. Water
  4. Floor
  5. -breaking (new and innovative)

  answer: Words that come after “ground”!
```

### crossclimb
```
game      : crossclimb
number    : 922
date      : 2026-11-08
difficulty: None

Ladder (word : clue, top -> bottom):
  port : The top + bottom rows = The opposite of "right," and what it's called on a ship. Keep in mind: The first word may be at the bottom.
  part : Distinct section of something
  wart : Skin blemish, or a small flaw
  waft : Float gently through the air, as an aroma might
  daft : ___ Punk (French electronic music duo)
  deft : Nimble and skilled
  left : The top + bottom rows = The opposite of "right," and what it's called on a ship. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
