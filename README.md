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
## Today's games (2026-11-22)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| .. | ..   10    9    6    1   .. | .. |
+    +     ----           ----     +    +
| ..   ..   11    8    7    2   ..   .. |
+                                       +
| ..   ..   ..   ..   ..   ..   ..   .. |
+----      ----           ----      ----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+                                       +
| ..   ..   12   15   16    3   ..   .. |
+          ----           ----          +
| .. | ..   13   14    5    4   .. | .. |
+    +                             +    +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| M | . | . | . = . x . |
+---+---+---+---+---+-=-+
| . | M | . | . | . | . |
+---+---+---+---+---+-x-+
| . | . | M | . | . | . |
+---+---+---+---+---+---+
| . | . | . | M | . | . |
+-=-+---+---+---+---+---+
| . | . | . | . | S | . |
+-x-+---+---+---+---+---+
| . = . x . | . | . | S |
+---+---+---+---+---+---+
```

### queens
```
🟥🟧🟧🟨🟨🟨🟦🟦
🟥🟥🟧🟧🟧🟨🟨🟦
⬛🟥⬛⬛⬛🟩🟦🟦
⬛🟥⬛🟫🟪🟩🟩🟦
⬛⬛⬛🟫🟪🟪🟩🟦
⬛⬛⬛🟫🟫🟪🟩🟦
⬛⬛⬛⬛🟫🟪🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │   ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃ 4 │   │ 6 ┃   │   │ 3 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 4 │   ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 6 │   ┃   │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 2 │   │   ┃ 5 │   │ 1 ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃   │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | .. | +4 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | =  | .. | .. | .. | .. | .. | +5 |
+----+----+----+----+----+----+----+----+
| +4 | .. | .. | .. | |  | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. | -  | .. |
+----+----+----+----+----+----+----+----+
| .. | |  | .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | =  | .. | .. | .. | +4 |
+----+----+----+----+----+----+----+----+
| +3 | .. | .. | .. | .. | .. | |  | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | +4 | .. | .. | +2 | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+---+
| T | O | # | D | # | E | H |
+---+---+---+---+---+---+---+
| # | P | W | O | T | A | # |
+---+---+---+---+---+---+---+
| L | P | N | A | N | V | D |
+---+---+---+---+---+---+---+
| E | E | H | D | N | Y | E |
+---+---+---+---+---+---+---+
| N | C | I | L | E | C | S |
+---+---+---+---+---+---+---+
| A | L | A | L | N | D | I |
+---+---+---+---+---+---+---+
| I | M | B | L | A | G | N |
+---+---+---+---+---+---+---+

Words:
  HEAVY
  TOPPLE
  LANDING
  DOWNHILL
  IMBALANCE
  DESCENDANT
```

### pinpoint
```
  1. Contest
  2. Peer
  3. Fire starter
  4. Double (as funds to charity)
  5. Visual pairing (as of socks)

  answer: Different definitions of “match”!
```

### crossclimb
```
game      : crossclimb
number    : 936
date      : 2026-11-22
difficulty: None

Ladder (word : clue, top -> bottom):
  moves : The top + bottom rows = A two-word phrase for aggressive tactics in business. Keep in mind: The first word may be at the bottom.
  doves : White birds that represent peace
  dover : British town known for its white cliffs
  lover : Romantic partner
  loser : Someone who is defeated
  poser : Difficult question, or an insincere person
  power : The top + bottom rows = A two-word phrase for aggressive tactics in business. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
