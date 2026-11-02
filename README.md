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
## Today's games (2026-11-02)

### zip
```
+----+----+----+----+----+----+
|  1    7    6    2   ..   .. |
+                             +
| ..   ..   ..   ..    3   .. |
+                             +
| ..   ..    5   ..    4   .. |
+                             +
| ..    8   ..   ..   10   .. |
+                             +
| ..   ..    9   11   ..   .. |
+                             +
| ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | M | S | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . = . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | M |
+-=-+---+---+---+---+---+
| . | . | . | . | . | M |
+---+---+---+---+---+---+
| . | M | M | . | . | . |
+---+---+---+---+---+---+
| . | . | . | . = . | . |
+---+---+---+---+---+---+
```

### queens
```
🟩🟩🟫🟫🟫🟫🟥
🟩🟩🟦🟦🟫🟫🟫
🟫🟫🟦🟦🟪🟪🟫
🟫🟫🟫🟫🟪🟪🟫
🟫🟫🟫🟨🟨🟫🟫
🟧🟫🟫🟨🟨🟫🟫
🟧🟫🟫🟫🟫🟫🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │   │ 5 ┃ 4 │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │ 6 ┃ 5 │   │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │ 4 ┃ 6 │   │ 1 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 4 │   │ 2 ┃ 1 │   │ 6 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | |2 | |2 | .. | .. |
+----+----+----+----+----+----+
| .. | =  | .. | .. | |  | .. |
+----+----+----+----+----+----+
| .. | .. | .. | -2 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | -2 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | +2 | +2 | +2 | +2 | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| E | A | S | # | T |
+---+---+---+---+---+
| M | # | U | # | S |
+---+---+---+---+---+
| A | E | R | E | A |
+---+---+---+---+---+
| E | # | H | # | T |
+---+---+---+---+---+
| P | # | C | A | E |
+---+---+---+---+---+

Words:
  PEA
  EAST
  TEACH
  MEASURE
```

### pinpoint
```
  1. Body
  2. Greeting
  3. Address
  4. Signature
  5. P.S. (after the main text)

  answer: Parts of written correspondence (letter or email)!
```

### crossclimb
```
game      : crossclimb
number    : 916
date      : 2026-11-02
difficulty: None

Ladder (word : clue, top -> bottom):
  lead : The top + bottom rows = Two words for the most prominent actor in a play or film.
  leak : A broken pipe or faucet may have one
  beak : What a bird eats with
  bear : Animal whose name also means "to tolerate"
  boar : Type of wild pig
  soar : Fly high and majestically
  star : The top + bottom rows = Two words for the most prominent actor in a play or film.
```
<!-- DAILY-GAMES-END -->
