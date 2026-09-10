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
## Today's games (2026-09-10)

### zip
```
+----+----+----+----+----+----+
| ..    1   ..   ..   ..   .. |
+               ---- ----     +
| ..    8   .. | ..   ..   .. |
+              +              +
|  2    5   ..   ..   ..   .. |
+                             +
| ..   ..   ..   ..    6    7 |
+                             +
| ..   ..   .. | ..    4   .. |
+     ---- ----+              +
| ..   ..   ..   ..    3   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| S | . = . | S | S | M |
+---+---+---+---+---+---+
| S | . | . | . | . | M |
+---+---+---+---+---+---+
| . | . | . | . | . | S |
+-=-+---+---+---+---+---+
| . | . | . | . | . | M |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+-x-+---+---+---+---+-=-+
| . | . x . | M | S | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟨🟨🟨🟨🟨🟨
🟥🟧🟨🟨🟨🟩🟨🟨
🟥🟧🟨🟨🟩🟩🟩🟨
🟦🟦🟦🟨🟨🟩🟨🟨
🟨🟨🟨🟨🟨🟨🟪🟨
🟨🟨🟨🟨🟨🟨🟪🟨
🟨🟨🟨🟨🟫🟫⬛⬛
🟨🟨🟨🟨🟫🟫⬛⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ 1 │   │ 4 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │ 6 ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │ 4 │ 5 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 3 │ 4 │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 1 │   │ 3 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 4 │   │ 2 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +4 | .. | .. | .. | .. | +6 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| +10 | .. | .. | .. | .. | +8 |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| W | G | D | I | R | W |
+---+---+---+---+---+---+
| O | E | # | # | B | O |
+---+---+---+---+---+---+
| R | # | C | S | # | B |
+---+---+---+---+---+---+
| B | # | E | E | # | N |
+---+---+---+---+---+---+
| C | T | N | R | C | I |
+---+---+---+---+---+---+
| U | R | V | E | R | A |
+---+---+---+---+---+---+

Words:
  BROW
  CURVE
  BRIDGE
  RAINBOW
  CRESCENT
```

### pinpoint
```
  1. Ten
  2. Timing
  3. Stranger
  4. Storm
  5. Example (no way to show better)

  answer: Words that come after “perfect”!
```

### crossclimb
```
game      : crossclimb
number    : 863
date      : 2026-09-10
difficulty: None

Ladder (word : clue, top -> bottom):
  rose : The top + bottom rows = A type of flower and what you might put it in. Keep in mind: The first word may be at the bottom.
  rope : What you use to tie up a boat at a pier
  ripe : Ready to eat, like fruit
  wipe : Clean with a rag, as a pane of glass
  wise : “A word to the ___” (helpful hint)
  vise : Gripping tool with two jaws
  vase : The top + bottom rows = A type of flower and what you might put it in. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
