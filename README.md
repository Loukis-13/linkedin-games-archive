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
## Today's games (2026-11-11)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+               ----          +
| ..   ..   .. | ..   ..   .. |
+          ----+              +
| ..   .. | ..   ..   ..   .. |
+         +                   +
| ..    3   ..   ..    6    4 |
+                             +
| ..    1   ..   ..    7   .. |
+                             +
| ..   ..    2    5   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | M | . | . | . |
+---+---+---+---+-=-+---+
| . | . | M | . | . | . |
+---+---+---+---+---+---+
| . | . | S | M | . | . |
+---+-=-+---+---+-x-+---+
| . | . | M | S | . | . |
+---+---+---+---+---+---+
| . | . | . | S | . | . |
+---+-=-+---+---+---+---+
| . | . | . | M | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟨🟨🟨
🟥🟧🟧🟩🟧🟧🟧🟨
🟥🟧🟧🟩🟩🟩🟧🟧
🟦🟦🟦🟧🟧🟧🟧🟧
🟧🟧🟦🟧🟪🟧🟧🟫
🟧🟧🟧🟧🟪🟧🟧🟫
⬛🟧🟧🟧🟪🟪🟫🟫
⬛🟧🟧🟧🟧🟧🟧🟧
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │ 1 │ 4 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 1 │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 5 │ 2 │ 3 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | +6 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +8 | +  | .. | .. |
+----+----+----+----+----+----+----+
| +3 | +2 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| =4 | .. | .. | .. | .. | .. | -3 |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +2 | +2 |
+----+----+----+----+----+----+----+
| .. | .. | +  | +3 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +4 | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| Q | # | # | # | A |
+---+---+---+---+---+
| U | E | C | E | U |
+---+---+---+---+---+
| T | S | C | S | T |
+---+---+---+---+---+
| H | S | U | S | H |
+---+---+---+---+---+
| O | R | N | R | O |
+---+---+---+---+---+

Words:
  HORN
  QUEST
  AUTHOR
  SUCCESS
```

### pinpoint
```
  1. {1, 2, 3, ...}
  2. Knight (in chess)
  3. Newton (SI unit of force)
  4. North
  5. No (if Yes = Y)

  answer: Things represented by the letter "N"!
```

### crossclimb
```
game      : crossclimb
number    : 925
date      : 2026-11-11
difficulty: None

Ladder (word : clue, top -> bottom):
  back : The top + bottom rows = A two-word phrase for the second half of a golf course. Keep in mind: The first word may be at the bottom.
  lack : Inadequate amount
  lick : Enjoy, as a lollipop
  link : Word following "missing" or "cuff"
  mink : Animal related to the weasel
  mine : Not yours
  nine : The top + bottom rows = A two-word phrase for the second half of a golf course. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
