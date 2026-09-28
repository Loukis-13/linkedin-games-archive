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
## Today's games (2026-09-28)

### zip
```
+----+----+----+----+----+----+
| ..    2   ..   ..   ..    1 |
+                             +
|  3   ..   ..   ..    4   .. |
+                             +
| 10   ..   ..   ..    6   .. |
+                             +
| ..   12   ..   ..   ..    5 |
+                             +
| ..   11   ..   ..   ..    7 |
+                             +
|  9   ..   ..   ..    8   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | M | M | . | . |
+-=-+---+---+---+---+-=-+
| . | . | M | S | . | . |
+-x-+-=-+---+---+-x-+-x-+
| . | . | S | S | . | . |
+-=-+---+---+---+---+-=-+
| . | . | M | M | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟧🟧🟧🟧
🟥🟧🟧🟧🟨🟨🟧
🟧🟧🟧🟨🟨🟨🟨
🟧🟧🟧🟩🟨🟨🟦
🟪🟪🟪🟩🟩🟦🟦
🟪🟪🟪🟩🟩🟦🟦
🟪🟪🟪🟪🟩🟦🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 6 │ 2 │   ┃   │ 3 │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 5 │ 6 │   ┃   │ 4 │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 4 ┃ 5 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| |  | +  | +  | =  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +12 | +  | +  | +6 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
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
  1. Subway
  2. Domino’s
  3. Jollibee
  4. KFC
  5. McDonald’s

  answer: Restaurant chains!
```

### crossclimb
```
game      : crossclimb
number    : 881
date      : 2026-09-28
difficulty: None

Ladder (word : clue, top -> bottom):
  toes : The top + bottom rows = The uppermost and lowermost body parts, as in "from my ___ to my ___." Keep in mind: The first word may be at the bottom.
  tees : Casual shirts named for the 20th letter of the alphabet
  bees : Creatures who live in hives
  beer : Stout, porter, or pale ale
  bear : Word following "brown," "black," or "polar"
  bead : Necklace part, or drop of sweat
  head : The top + bottom rows = The uppermost and lowermost body parts, as in "from my ___ to my ___." Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
