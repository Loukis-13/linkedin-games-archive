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
## Today's games (2026-09-15)

### zip
```
+----+----+----+----+----+----+----+----+
| ..   ..   ..   ..   ..   ..   ..   .. |
+               ---- ----               +
| .. | ..   .. | ..   .. | ..    8 | .. |
+    +         +         +         +    +
| .. | ..   .. | ..   .. | ..    1 | .. |
+    +---- ----+         +---- ----+    +
| ..   ..   ..   ..    6    7   ..   .. |
+                                       +
| ..   ..    2    5   ..   ..   ..   .. |
+     ---- ----           ---- ----     +
| .. |  4   .. | ..   .. | ..   .. | .. |
+    +         +         +         +    +
| .. |  3   .. | ..   .. | ..   .. | .. |
+    +         +---- ----+         +    +
| ..   ..   ..   ..   ..   ..   ..   .. |
+---- ---- ---- ---- ---- ---- ---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . = . | . | . | . | . |
+-=-+---+---+---+---+---+
| . | . | S | . | . | . |
+---+---+---+---+---+---+
| . | M | . | S | . | . |
+---+---+---+---+---+---+
| . | . | S | . | S | . |
+---+---+---+---+---+---+
| . | . | . | M | . | . |
+---+---+---+---+---+-x-+
| . | . | . | . | . x . |
+---+---+---+---+---+---+
```

### queens
```
🟥🟥🟥🟥🟥🟥🟥
🟥🟧🟧🟧🟧🟧🟥
🟥🟥🟫🟫🟧🟩🟥
🟫🟫🟫🟦🟩🟩🟩
🟨🟫🟪🟩🟩🟩🟩
🟨🟪🟪🟪🟪🟪🟩
🟨🟨🟩🟩🟩🟩🟩
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 4 ┃   │ 5 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 3 │ 2 ┃   │ 6 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │   │   ┃   │ 3 │ 4 ┃
┃───┼───┼───┃───┼───┼───┃
┃ 1 │ 4 │   ┃   │   │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 6 │   ┃ 2 │ 1 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃ 5 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+
| .. | .. | +  | +  | .. | .. |
+----+----+----+----+----+----+
| +3 | .. | .. | .. | .. | +15 |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| .. | .. | .. | .. | .. | .. |
+----+----+----+----+----+----+
| +3 | .. | .. | .. | .. | +5 |
+----+----+----+----+----+----+
| .. | .. | +  | +3 | .. | .. |
+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+
| # | I | P | N | # |
+---+---+---+---+---+
| E | X | # | A | V |
+---+---+---+---+---+
| L | U | Q | U | E |
+---+---+---+---+---+
| B | O | # | D | T |
+---+---+---+---+---+
| # | G | R | I | # |
+---+---+---+---+---+

Words:
  VAN
  GRID
  PIXEL
  BOUQUET
```

### pinpoint
```
  1. Robusta
  2. Arabica
  3. Cold brew
  4. Instant
  5. Decaf

  answer: Words that come before “coffee”!
```

### crossclimb
```
game      : crossclimb
number    : 868
date      : 2026-09-15
difficulty: None

Ladder (word : clue, top -> bottom):
  back : The top + bottom rows = A compound word meaning to go on some adventurous travel with just a bag over your shoulders. Keep in mind: The first word may be at the bottom.
  bark : Outside covering of a tree
  lark : Songbird whose name completes the phrase “on a ___”, meaning to do something impulsively or just for fun
  lack : Shortage or absence of something
  lick : Short taste, as of a lollipop
  pick : Choose between a few options
  pack : The top + bottom rows = A compound word meaning to go on some adventurous travel with just a bag over your shoulders. Keep in mind: The first word may be at the bottom.
```
<!-- DAILY-GAMES-END -->
