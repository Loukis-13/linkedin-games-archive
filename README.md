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
## Today's games (2026-10-01)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   .. |
+     ---- ----                    +
| ..    5   ..   ..   ..    1   .. |
+          ---- ----               +
|  7   ..   ..   ..   ..   ..   .. |
+               ---- ----          +
| ..    8   ..   ..   ..    2   .. |
+          ---- ----               +
| ..   ..   ..   ..   ..   ..    6 |
+               ---- ----          +
| ..    4   ..   ..   ..    3   .. |
+                    ---- ----     +
| ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+-=-+---+
| . | . | . | . | . x . |
+---+---+---+-=-+---+---+
| . | . | . | . = . | . |
+---+---+---+---+---+---+
| . | S | S | . | . | . |
+---+---+---+---+---+---+
| S | S | M | . | . | . |
+---+---+---+---+---+---+
| . | M | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟧🟨🟥🟥🟥🟥🟨🟨
🟧🟨🟨🟥🟥🟨🟨🟩
🟧🟧🟨🟨🟨🟨🟩🟩
🟨🟨🟨🟨🟨🟨🟩🟨
🟨🟨🟨🟦🟦🟨🟨🟨
🟨🟨🟪🟦🟦🟫🟨🟨
🟨🟪🟪⬛🟦🟫🟫🟨
🟪🟪⬛⬛🟦🟦🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 2 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 2 │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 6 │   │   ┃   │   │ 4 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │   ┃   │ 6 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃ 3 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +4 | .. | +2 | .. | +4 | .. |
+----+----+----+----+----+----+----+
| .. | .. | |3 | .. | +3 | .. | .. |
+----+----+----+----+----+----+----+
| .. | +4 | .. | |2 | .. | +6 | .. |
+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | |2 | .. | .. |
+----+----+----+----+----+----+----+
| .. | +6 | .. | +3 | .. | +6 | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | C | O | R | H | C |
+---+---+---+---+---+---+
| # | K | E | # | # | A |
+---+---+---+---+---+---+
| C | I | T | # | O | M |
+---+---+---+---+---+---+
| O | G | # | D | T | S |
+---+---+---+---+---+---+
| L | # | # | O | O | # |
+---+---+---+---+---+---+
| B | O | N | K | R | # |
+---+---+---+---+---+---+

Words:
  LOGIC
  ROCKET
  STOMACH
  DOORKNOB
```

### pinpoint
```
  1. Ossicles
  2. Cochlea
  3. Semicircular canals
  4. Tympanic membrane
  5. Auditory nerve

  answer: Parts of the ear!
```

### crossclimb
```
game      : crossclimb
number    : 884
date      : 2026-10-01
difficulty: None

Ladder (word : clue, top -> bottom):
  well : The top + bottom rows = A two-word compliment meaning "You expressed that perfectly." Keep in mind: The first word may be at the bottom.
  bell : Loud ringer at many churches
  ball : Fancy party, or a sphere
  bald : Lacking hair
  band : Word following "rubber" or "rock"
  sand : Substance found on a beach or in an hourglass
  said : The top + bottom rows = A two-word compliment meaning "You expressed that perfectly." Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
