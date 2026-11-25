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
## Today's games (2026-11-25)

### zip
```
+----+----+----+----+----+----+----+
| ..   11   ..   ..   ..   ..   .. |
+                                  +
| 10   ..   14   ..   ..   ..   .. |
+                                  +
|  9   ..   ..    4   ..   12   .. |
+                                  +
| ..   15   ..    3   ..   13   .. |
+                                  +
| ..    5   ..    2   ..   ..    1 |
+                                  +
| ..   ..   ..   ..    6   ..    7 |
+                                  +
| ..   ..   ..   ..   ..    8   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | S | . | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+-=-+---+-=-+---+-x-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+-x-+---+-=-+---+-x-+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | . | M | . | M |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟧🟧🟧🟧
🟥🟧🟨🟩🟦🟧🟧
🟥🟨🟨🟨🟦🟦🟧
🟥🟨🟪🟦🟦🟫🟧
🟥🟪🟪🟫🟫🟫🟧
🟥🟥🟪🟪🟫🟧🟧
🟥🟥🟥🟥🟥🟥🟥
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 3 │ 4 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 5 │   ┃   │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 6 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │   ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 3 │ 1 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | -  | .. |
+----+----+----+----+----+----+----+
| .. | +4 | =  | .. | .. | +6 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | -  | .. | .. | =  | +6 | .. |
+----+----+----+----+----+----+----+
| .. | +4 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| N | O | B | P | I |
+---+---+---+---+---+
| B | # | R | A | H |
+---+---+---+---+---+
| L | U | # | C | S |
+---+---+---+---+---+
| P | R | A | # | R |
+---+---+---+---+---+
| O | L | K | W | O |
+---+---+---+---+---+

Words:
  BLUR
  POLKA
  CARBON
  WORSHIP
```

### pinpoint
```
  1. Chain
  2. Cuff
  3. Missing
  4. Weakest
  5. Click the (online call to action)

  answer: Words that come before “link”!
```

### crossclimb
```
game      : crossclimb
number    : 939
date      : 2026-11-25
difficulty: None

Ladder (word : clue, top -> bottom):
  yarn : The top + bottom rows = Two words for a story to be told.
  yard : Imperial measurement that's just short of a meter
  bard : Renaissance Faire entertainer
  bald : Without hair on the head
  balk : Stop or hesitate when doing something
  talk : Have a conversation
  tale : The top + bottom rows = Two words for a story to be told.
```
<!-- DAILY-GAMES-END -->
