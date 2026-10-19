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
## Today's games (2026-10-19)

### zip
```
+----+----+----+----+----+----+
|  1   ..   ..   ..   ..    4 |
+                             +
| ..   ..   ..   ..    6   .. |
+                             +
| ..   ..   ..    8   ..   .. |
+                             +
| ..   ..    7   ..   ..   .. |
+                             +
| ..    5   ..   ..   ..   .. |
+                             +
|  2   ..   ..   ..   ..    3 |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . = . | . |
+---+---+---+-=-+---+---+
| . | . | . = . | . | . |
+---+---+-x-+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| M | M | . | S | M | . |
+---+---+---+---+---+---+
| M | S | . | M | M | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟫🟫🟧🟧🟧🟦🟦
🟫🟫🟧🟥🟧🟦🟦
🟫🟫🟧🟧🟧🟦🟦
🟫🟪🟪🟧🟨🟨🟦
🟫🟪🟧🟧🟧🟨🟦
🟫🟪🟪🟧🟨🟨🟩
🟫🟪🟪🟧🟩🟩🟩
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 2 ┃ 3 │ 4 │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │   │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │   ┃ 2 │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │ 5 ┃   │ 6 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │ 4 ┃ 1 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | +6 | +2 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +4 | .. | .. | +9 | .. | .. |
+----+----+----+----+----+----+----+
| .. | +8 | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | |  | |  | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | |2 | -8 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| T | # | E | # | A |
+---+---+---+---+---+
| S | E | L | I | G |
+---+---+---+---+---+
| # | T | E | E | # |
+---+---+---+---+---+
| O | N | S | S | O |
+---+---+---+---+---+
| C | # | U | # | P |
+---+---+---+---+---+

Words:
  USE
  POSE
  AGILE
  CONTEST
```

### pinpoint
```
  1. Acrobat
  2. Clown
  3. Ringmaster
  4. Sword swallower
  5. Lion tamer

  answer: Professions seen at the circus!
```

### crossclimb
```
game      : crossclimb
number    : 902
date      : 2026-10-19
difficulty: None

Ladder (word : clue, top -> bottom):
  dice : The top + bottom rows = Objects rolled during some board games, and a common shape for them. Keep in mind: The first word may be at the bottom.
  dire : Desperate, as a situation or a need
  dare : Be boldly courageous
  pare : Peel the skin off of, as fruit
  pure : ___ and simple (no more, no less)
  cure : Completely get rid of, as an illness
  cube : The top + bottom rows = Objects rolled during some board games, and a common shape for them. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
