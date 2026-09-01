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
## Today's games (2026-09-01)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   .. |
+               ---- ----     +
|  4   ..   .. | ..   .. | .. |
+              +         +    +
|  3    5   .. | ..   .. | .. |
+              +         +    +
| .. | ..   .. | ..    1    6 |
+    +         +              +
| .. | ..   .. | ..   ..    2 |
+    +---- ----+              +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+-=-+---+---+-x-+---+
| . | . | S | . | . | . |
+---+-x-+---+---+-x-+---+
| . | . | S | . | . | . |
+---+-x-+---+---+-x-+---+
| . | . | . | M | . | . |
+---+-x-+---+---+-=-+---+
| . | . | . | S | . | . |
+---+-=-+---+---+-x-+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟨🟨🟨🟨
🟥🟧🟧🟦🟨🟨🟨
🟫🟫🟦🟦🟦🟨🟨
🟨🟫🟦🟪🟪🟪🟨
🟨🟨🟦🟪🟪🟩🟨
🟨🟨🟨🟪🟩🟩🟨
🟨🟨🟨🟨🟨🟨🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │ 2 │ 3 ┃ 4 │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 6 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 2 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 5 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 5 │ 2 ┃ 1 │ 3 │ 4 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| =4 | .. | -6 | .. | .. | .. |
+----+----+----+----+----+----+
| |2 | |2 | -2 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +  | .. | +  |
+----+----+----+----+----+----+
| .. | .. | .. | +  | +  | +  |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| B | U | U | T | N |
+---+---+---+---+---+
| K | L | M | # | A |
+---+---+---+---+---+
| Y | # | N | # | U |
+---+---+---+---+---+
| L | # | O | P | Q |
+---+---+---+---+---+
| A | M | R | U | C |
+---+---+---+---+---+

Words:
  CUP
  BULKY
  NORMAL
  QUANTUM
```

### pinpoint
```
  1. Espresso
  2. Renaissance art
  3. Vespa scooters
  4. Fashion houses (Gucci, Prada, …)
  5. Pizza and pasta

  answer: Things associated with Italy (🇮🇹)!
```

### crossclimb
```
game      : crossclimb
number    : 854
date      : 2026-09-01
difficulty: None

Ladder (word : clue, top -> bottom):
  good : The top + bottom rows = A two-word phrase for information you hope to hear. Keep in mind: The first word may be at the bottom.
  wood : Lumber
  woos : Tries to win someone’s affection
  wows : Really impresses with a performance
  sows : Female pigs
  sews : Uses a needle and thread
  news : The top + bottom rows = A two-word phrase for information you hope to hear. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
