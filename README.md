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
## Today's games (2026-11-18)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+                             +
| ..    7   ..   ..    3   .. |
+                             +
| ..   ..    6    8   ..   .. |
+                             +
| ..   ..    4    1   ..   .. |
+                             +
| ..    5   ..   ..    2   .. |
+                             +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . | . | . | . | . |
+-=-+-=-+---+---+---+---+
| . = . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . = . | . | . |
+---+---+-=-+-=-+---+---+
| . | . | . = . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | M | M |
+---+---+---+---+---+---+
| . | . | . | . | S | M |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟨🟨🟩🟩🟩
🟥🟧🟨🟨🟩🟦🟦
🟥🟧🟨🟨🟨🟦🟪
🟥🟧🟨🟨🟨🟪🟪
🟥🟧🟧🟫🟫🟫🟫
🟥🟧🟧🟫🟫🟫🟫
🟥🟥🟥🟥🟥🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 5 │ 1 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │ 5 │ 6 ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 2 ┃ 6 │ 3 │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 1 │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| -6 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | -  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | -6 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | |  |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| N | E | # | U | N |
+---+---+---+---+---+
| E | W | L | A | C |
+---+---+---+---+---+
| M | A | # | T | H |
+---+---+---+---+---+
| # | G | # | O | # |
+---+---+---+---+---+
| # | Y | A | D | # |
+---+---+---+---+---+

Words:
  NEW
  GAME
  LAUNCH
  TODAY
```

### pinpoint
```
  1. 500
  2. 21
  3. Uno
  4. Crazy Eights
  5. 52 Pickup (using a scattered deck)

  answer: Names of card games!
```

### crossclimb
```
game      : crossclimb
number    : 932
date      : 2026-11-18
difficulty: None

Ladder (word : clue, top -> bottom):
  soap : The top + bottom rows = Two items you use when washing your hands.
  soak : Spend a long time in a bath
  sock : Item between a shoe and a foot
  suck : What young children might do on their thumbs
  sulk : Pout and be resentful
  silk : Smooth material often used to make neckties
  sink : The top + bottom rows = Two items you use when washing your hands.
```
<!-- DAILY-GAMES-END -->
