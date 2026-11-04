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
## Today's games (2026-11-04)

### zip
```
+----+----+----+----+----+----+----+
|  1   ..   ..    7   ..   ..    9 |
+                                  +
| .. | .. | ..   ..   .. | .. | .. |
+    +    +              +    +    +
| .. | ..    6   ..   ..    8 | .. |
+    +     ---- ---- ----     +    +
| .. | ..   ..   ..   ..   .. | .. |
+    +---- ---- ---- ----     +    +
| ..    4   ..   ..    5 | .. | .. |
+                        +    +    +
| ..   ..   ..   ..   .. | .. | .. |
+                        +    +    +
|  2   ..   ..    3   ..   ..   10 |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | M | S | S | M | S |
+---+---+---+---+---+---+
| M | S | S | M | S | M |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . = . | . = . | . x . |
+---+---+---+---+---+---+
| . = . | . x . | . = . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟧🟧🟧
🟥🟥🟥🟨🟩🟩🟧
🟥🟥🟦🟨🟩🟩🟩
🟥🟪🟦🟨🟨🟩🟩
🟫🟪🟦🟦🟩🟩🟩
🟫🟪🟪🟩🟩🟩🟩
🟫🟫🟩🟩🟩🟩🟩
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 3 ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃ 4 │   │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │ 2 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │ 4 ┃   │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 1 │   ┃ 3 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +3 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | -6 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +  | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | -3 | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| R | E | E | L | B |
+---+---+---+---+---+
| A | G | # | N | O |
+---+---+---+---+---+
| E | # | # | # | L |
+---+---+---+---+---+
| R | A | # | Y | O |
+---+---+---+---+---+
| B | V | E | A | L |
+---+---+---+---+---+

Words:
  NOBLE
  EAGER
  LOYAL
  BRAVE
```

### pinpoint
```
  1. Haddock
  2. Sparrow
  3. Hook
  4. Nemo
  5. Ahab (from Moby-Dick)

  answer: Fictional sea captains!
```

### crossclimb
```
game      : crossclimb
number    : 918
date      : 2026-11-04
difficulty: None

Ladder (word : clue, top -> bottom):
  tank : The top + bottom rows = A two-word phrase for a container that an engine draws from in order to run. Keep in mind: The first word may be at the bottom.
  bank : Place to deposit or withdraw money
  balk : Show reluctance about an idea
  ball : Formal dance, like the one Cinderella attended
  fall : Opposite of "rise," as a noun or a verb
  full : Half-___ (like an optimist's water glass)
  fuel : The top + bottom rows = A two-word phrase for a container that an engine draws from in order to run. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
