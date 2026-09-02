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
## Today's games (2026-09-02)

### zip
```
+----+----+----+----+----+----+
|  1   ..   ..   ..   ..    2 |
+                             +
| ..   ..    6   ..   ..   .. |
+                             +
| ..   ..   ..   ..    5   .. |
+                             +
| ..    4   ..   ..   ..   .. |
+                             +
| ..   ..   ..    7   ..   .. |
+                             +
|  8   ..   ..   ..   ..    3 |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | . x . = . | . |
+---+---+---+---+-=-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | M | S | M | S | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+-=-+---+---+---+---+
| . | . = . x . | M | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟧🟧
🟥🟩🟨🟨🟨🟧🟧
🟥🟩🟥🟥🟨🟨🟧
🟥🟥🟥🟦🟨🟧🟧
🟪🟥🟫🟫🟧🟧🟪
🟪🟫🟫🟫🟫🟫🟪
🟪🟪🟪🟪🟪🟪🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 3 ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 5 │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 6 │ 1 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 5 │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃ 3 │ 5 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | =  | -  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +5 | +6 |
+----+----+----+----+----+----+
| +3 | +6 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | |  | |  | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| N | O | # | P | O |
+---+---+---+---+---+
| S | S | S | S | S |
+---+---+---+---+---+
| E | S | # | E | S |
+---+---+---+---+---+
| E | E | E | E | E |
+---+---+---+---+---+
| N | L | # | R | I |
+---+---+---+---+---+

Words:
  SEEN
  EERIE
  LESSON
  POSSESS
```

### pinpoint
```
  1. Towels
  2. Napkins
  3. Large road maps
  4. Paper cranes
  5. Bad poker hands

  answer: Things that are folded!
```

### crossclimb
```
game      : crossclimb
number    : 855
date      : 2026-09-02
difficulty: None

Ladder (word : clue, top -> bottom):
  play : The top + bottom rows = A compound word for a part of a house that is filled with toys and games. Keep in mind: The first word may be at the bottom.
  slay : “___ the dragon” (conquer a difficult challenge)
  slam : Shut loudly, as a door
  seam : Line where two pieces of fabric are joined
  ream : Large quantity of paper
  roam : Wander somewhat aimlessly
  room : The top + bottom rows = A compound word for a part of a house that is filled with toys and games. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
