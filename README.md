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
## Today's games (2026-08-25)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..    6   ..   .. |
+     ---- ----           ---- ----     +
| .. | ..   .. |  1    4 | ..   .. | .. |
+    +         +         +         +    +
| ..   .. | .. | ..   .. | .. | ..   .. |
+         +    +         +    +         +
| ..   ..   .. | ..   .. | ..   ..   .. |
+     ---- ----+         +---- ----     +
| .. | ..   ..   ..   ..   ..   .. | .. |
+    +                             +    +
| .. | .. | ..   ..   ..   .. | .. | .. |
+    +    +                   +    +    +
| .. | ..   .. |  2    5 | ..   .. | .. |
+    +---- ----+         +---- ----+    +
| ..   ..    3   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
| . | . x . x . = . | . |
+---+---+---+---+---+---+
| . | M | . | . | S | . |
+---+---+-=-+-x-+---+---+
| . | S | . | . | S | . |
+---+---+---+---+---+---+
| . | . = . x . = . | . |
+---+---+---+---+---+---+
| . | . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟧🟧🟧🟧🟧
🟥🟥🟨🟨🟨🟨🟨
🟩🟨🟨🟦🟦🟦🟨
🟩🟨🟪🟪🟦🟦🟨
🟩🟨🟪🟦🟦🟦🟨
🟩🟨🟨🟦🟦🟨🟨
🟩🟨🟨🟨🟨🟨🟫
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃ 2 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │ 1 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 1 │   │   ┃   │   │ 2 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 3 │   │   ┃   │   │ 5 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 1 │   ┃   │ 3 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 3 ┃ 4 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| +  | .. | .. | .. | +  | .. |
+----+----+----+----+----+----+
| .. | +6 | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | +4 | .. | .. |
+----+----+----+----+----+----+
| .. | .. | +9 | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | +8 | .. |
+----+----+----+----+----+----+
| .. | +  | .. | .. | .. | +  |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| # | # | F | Y | I |
+---+---+---+---+---+
| O | D | I | N | O |
+---+---+---+---+---+
| M | # | # | # | T |
+---+---+---+---+---+
| E | S | U | I | L |
+---+---+---+---+---+
| F | A | Q | # | # |
+---+---+---+---+---+

Words:
  ION
  SAFE
  QUILT
  MODIFY
```

### pinpoint
```
  1. Impact
  2. Courier
  3. Wingdings
  4. Lucida Handwriting
  5. Calibri or Aptos (in MS Office)

  answer: Names of fonts!
```

### crossclimb
```
game      : crossclimb
number    : 847
date      : 2026-08-25
difficulty: None

Ladder (word : clue, top -> bottom):
  read : The top + bottom rows = A hyphenated word describing someone who is highly educated through books. Keep in mind: The first word may be at the bottom.
  bead : Stone with a hole in it used in jewelry
  beat : Quality of a danceable song
  belt : It may hold up your jeans
  felt : Soft green material on a poker table
  fell : Plunged
  well : The top + bottom rows = A hyphenated word describing someone who is highly educated through books. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
