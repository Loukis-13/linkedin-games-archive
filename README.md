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
## Today's games (2026-11-12)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..   12    5   ..   ..   .. |
+                                  +
| ..   13   ..   ..    4   ..   .. |
+                                  +
| ..   ..    8   ..   ..    3   .. |
+                                  +
| ..   ..   ..    2   ..   ..   .. |
+                                  +
| ..    9   ..   ..    7   ..   .. |
+                                  +
| ..   ..   10   ..   ..    1   .. |
+                                  +
| ..   ..   ..   11    6   ..   .. |
+---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . x . |
+---+---+---+---+---+---+
| . | . | . | . | M | S |
+---+---+---+-x-+---+---+
| . x . | . | . | M | M |
+---+---+---+---+---+---+
| S | M | . | . | . x . |
+---+---+-x-+---+---+---+
| M | S | . | . | . | . |
+---+---+---+---+---+---+
| . x . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟨🟨🟨🟦🟦
🟥🟨🟨🟨🟨🟦🟦🟩
🟥🟨🟥🟨🟦🟦🟩🟩
🟥🟥🟥🟦🟦🟩🟩🟩
🟥🟥🟦🟦🟧🟩🟩🟩
🟥🟦🟦🟪🟧🟧🟫🟩
🟦🟦⬛🟪🟪🟧🟫🟫
🟦⬛⬛⬛🟪🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 1 │ 2 ┃ 3 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │ 5 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 2 │   │   ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 4 │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 1 ┃ 6 │ 3 │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+
| .. | +8 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +5 | .. |
+----+----+----+----+----+----+----+
| +6 | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | |6 | +  | |3 | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | +5 |
+----+----+----+----+----+----+----+
| .. | +6 | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | +7 | .. |
+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| L | I | C | O | E | N |
+---+---+---+---+---+---+
| A | C | # | # | L | C |
+---+---+---+---+---+---+
| R | # | H | C | C | H |
+---+---+---+---+---+---+
| U | # | A | N | C | E |
+---+---+---+---+---+---+
| C | C | # | # | R | I |
+---+---+---+---+---+---+
| N | O | S | U | C | C |
+---+---+---+---+---+---+

Words:
  CALICO
  CHANCE
  CLENCH
  CONCUR
  CIRCUS
```

### pinpoint
```
  1. Red
  2. Stars
  3. The light
  4. The big picture
  5. Eye to eye (agree fully)

  answer: Words that come after “see” in common idioms!
```

### crossclimb
```
game      : crossclimb
number    : 926
date      : 2026-11-12
difficulty: None

Ladder (word : clue, top -> bottom):
  book : The top + bottom rows = A compound word for a collection of instructions and strategies for a business. Keep in mind: The first word may be at the bottom.
  cook : Prepare a hot meal
  coop : Place for chickens on a farm
  clop : Sound from a trotting horse's hoof
  clap : Noisily put your hands together
  clay : Moldable material in an art class
  play : The top + bottom rows = A compound word for a collection of instructions and strategies for a business. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
