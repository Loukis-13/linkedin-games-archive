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
## Today's games (2026-09-14)

### zip
```
+----+----+----+----+----+----+
| 14    6   ..   ..   ..    7 |
+                             +
| 13   ..    5   ..   ..   .. |
+                             +
| ..    1   ..    2   ..   .. |
+                             +
| ..   ..   11   ..    4   .. |
+                             +
| ..   ..   ..    3   ..    8 |
+                             +
| 12   ..   ..   ..   10    9 |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | S | . | . | . |
+---+---+---+---+---+---+
| . | S | . | . | . | . |
+---+---+-=-+---+---+---+
| S | . = . | S | . | . |
+---+---+---+---+---+---+
| . | . | S | S | . | . |
+---+---+---+---+-=-+---+
| . | . | . | . = . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | S |
+---+---+---+---+---+---+
```

### queens
```
🟦🟦🟦🟨🟨🟫🟫
🟦🟦🟦🟦🟨🟨🟫
🟩🟨🟨🟨🟨🟨🟨
🟩🟥🟥🟨🟨🟨🟨
🟪🟪🟪🟨🟨🟧🟨
🟪🟪🟪🟨🟨🟨🟨
🟪🟪🟨🟨🟨🟨🟨
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │ 5 │   ┃   │ 1 │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │ 6 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │   │ 5 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │   ┃   │ 2 │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃ 4 │ 3 │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │ 4 │   ┃   │   │ 2 ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | +3 | .. | .. | +3 | .. |
+----+----+----+----+----+----+
| .. | +  | .. | .. | -6 | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | =9 | .. | .. | +  | .. |
+----+----+----+----+----+----+
| .. | +2 | .. | .. | +4 | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| U | B | E | I | G |
+---+---+---+---+---+
| H | # | H | # | H |
+---+---+---+---+---+
| O | # | # | # | T |
+---+---+---+---+---+
| H | # | H | # | H |
+---+---+---+---+---+
| C | E | C | T | A |
+---+---+---+---+---+

Words:
  HUB
  ECHO
  HATCH
  HEIGHT
```

### pinpoint
```
  1. Tweety Bird
  2. Pac-Man
  3. SpongeBob SquarePants
  4. Bart Simpson
  5. The Minions (rhymes with Bello!)

  answer: Fictional characters that are yellow!
```

### crossclimb
```
game      : crossclimb
number    : 867
date      : 2026-09-14
difficulty: None

Ladder (word : clue, top -> bottom):
  kind : The top + bottom rows = Two synonyms of the word "variety."
  mind : “Make up your ___” (come to a decision)
  mine : Dig in the earth for precious metals
  mire : Swampy land
  more : Opposite of less
  sore : Aching a bit, as after a run
  sort : The top + bottom rows = Two synonyms of the word "variety."
```
<!-- DAILY-GAMES-END -->
