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
## Today's games (2026-10-29)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..    6   ..   .. |
+                             +
| ..    1    2    4   ..   .. |
+                             +
| ..   ..   ..   ..   ..   .. |
+                             +
| ..   ..   ..   ..   ..   .. |
+                             +
| ..   ..    3    8    5   .. |
+                             +
| ..   ..    7   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | M | S | M | . |
+---+---+---+---+---+---+
| . | S | . | . | M | . |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+-=-+-x-+---+---+
| . | . | . x . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟧🟧🟦🟦🟦
🟦🟦🟨🟧🟧🟩🟦🟦
🟦🟨🟨🟨🟩🟩🟥🟦
🟦🟪🟪🟪🟩🟥🟥🟦
🟦⬛🟪🟫🟫🟥🟦🟦
🟦⬛🟦🟫🟫🟦🟦🟦
⬛⬛🟦🟦🟦🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │ 3 ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃ 4 │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │   ┃   │ 2 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| |  | .. | +4 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | +3 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| +4 | .. | =  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +3 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | |  |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +2 | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| W | O | F | L | O | O |
+---+---+---+---+---+---+
| T | R | K | I | M | R |
+---+---+---+---+---+---+
| O | # | # | R | # | # |
+---+---+---+---+---+---+
| O | # | # | R | # | O |
+---+---+---+---+---+---+
| F | R | O | O | R | R |
+---+---+---+---+---+---+
| O | A | N | A | G | E |
+---+---+---+---+---+---+

Words:
  OAR
  FLOOR
  MIRROR
  OREGANO
  FOOTWORK
```

### pinpoint
```
  1. Jet
  2. Gulf
  3. Blood
  4. Live (on Twitch)
  5. Swimming up-

  answer: Words that come before “stream”!
```

### crossclimb
```
game      : crossclimb
number    : 912
date      : 2026-10-29
difficulty: None

Ladder (word : clue, top -> bottom):
  save : The top + bottom rows = Two verbs associated with computer files: one to store and one to retrieve. Keep in mind: The first word may be at the bottom.
  cave : Often explorable underground space
  cove : Small coastal area with a narrow entrance
  core : Center of an apple
  cord : Flexible accessory used for charging electronics
  lord : Someone who rules over a domain
  load : The top + bottom rows = Two verbs associated with computer files: one to store and one to retrieve. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
