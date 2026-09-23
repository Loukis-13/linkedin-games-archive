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
## Today's games (2026-09-23)

### zip
```
+----+----+----+----+----+----+
| ..   ..   ..    3   ..   .. |
+     ----      ----          +
| .. |  2   ..   .. | ..   .. |
+    +              +         +
| .. | ..   ..   .. | ..   .. |
+    +----          +----     +
| ..   .. | ..   ..   .. | .. |
+         +              +    +
| ..   .. | ..   ..    1 | .. |
+         +----      ----+    +
| ..   ..    4   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . x . | . | M | M | S |
+---+---+-x-+---+---+---+
| . | . | . | M | . | . |
+---+---+-x-+---+---+---+
| . | . | . | S | . | . |
+---+---+---+---+---+---+
| . | . | S | . | . | . |
+---+---+---+-x-+---+---+
| . | . | M | . | . | . |
+---+---+---+-=-+---+---+
| S | S | M | . | . = . |
+---+---+---+---+---+---+
```

### queens
```
🟩🟩🟩🟧🟧🟧🟦
🟩🟩🟥🟧🟨🟧🟦
🟩🟥🟥🟥🟨🟨🟦
🟩🟩🟥🟥🟥🟪🟪
🟫🟥🟥🟥🟥🟥🟪
🟫🟫🟥🟫🟥🟪🟪
🟫🟫🟫🟫🟫🟫🟪
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │ 4 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │ 1 │ 2 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │   ┃ 3 │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 5 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +  | +2 | -  | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | +  | +2 | +2 | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | +2 | +3 | +  | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | =  | +2 | +  | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| V | A | R | C | H |
+---+---+---+---+---+
| I | R | O | # | K |
+---+---+---+---+---+
| A | S | C | I | C |
+---+---+---+---+---+
| B | # | T | H | O |
+---+---+---+---+---+
| L | E | N | E | P |
+---+---+---+---+---+

Words:
  OPEN
  THICK
  SCORCH
  VARIABLE
```

### pinpoint
```
  1. Delta
  2. Doritos
  3. “Give way” or “Yield” sign
  4. Rack (for 8-Ball or Snooker)
  5. Pennant (like this one: 🚩)

  answer: Things shaped like triangles!
```

### crossclimb
```
game      : crossclimb
number    : 876
date      : 2026-09-23
difficulty: None

Ladder (word : clue, top -> bottom):
  hand : The top + bottom rows = Compound word that describes drawing without the help of mechanical devices. Keep in mind: The first word may be at the bottom.
  band : Musical group
  bend : Flex, like an elbow or knee
  fend : ___ for yourself (get what you need without help)
  feed : Serve a meal to
  fred : Cartoon Flintstone who said "Yabba-dabba-doo!"
  free : The top + bottom rows = Compound word that describes drawing without the help of mechanical devices. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
