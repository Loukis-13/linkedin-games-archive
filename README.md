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
## Today's games (2026-11-27)

### zip
```
+----+----+----+----+----+----+----+
| ..   ..    8    7    6   ..   .. |
+                                  +
| ..   11   ..   ..   ..    3   .. |
+                                  +
| ..   12   ..    2   ..    4   .. |
+                                  +
| ..   13   ..   ..   ..    5   .. |
+                                  +
| ..   ..    9   10    1   ..   .. |
+                                  +
| ..   .. | ..   ..   .. | ..   .. |
+         +     ----     +         +
| ..   .. | ..   ..   .. | ..   .. |
+---- ----+---- ---- ----+---- ----+
```

### tango
```
+---+---+---+---+---+---+
| . | . | . | . | . = . |
+---+---+---+---+-=-+-=-+
| . | . | . | . | . = . |
+---+---+---+---+---+---+
| . | . | S | M | . | . |
+---+---+---+---+---+---+
| . | . | S | S | . | . |
+---+---+---+---+---+---+
| . = . | . | . | . | . |
+-x-+-x-+---+---+---+---+
| . = . | . | . | . | . |
+---+---+---+---+---+---+
```

### queens
```
🟫🟫🟫🟫🟫🟫🟫🟫🟫
🟫🟫🟫🟫🟦🟫🟫🟫🟫
🟫🟫🟫🟫🟦⬜⬜⬜⬜
🟫🟪🟪🟦🟦🟦⬜⬜⬜
🟫🟪🟦🟦🟥🟦🟦⬛⬜
🟪🟪🟦🟥🟥🟥🟦⬛⬜
🟪🟩🟦🟥🟧🟥🟦⬛⬛
🟩🟩🟦🟧🟧🟧🟦🟨⬛
🟩🟩🟩🟩🟨🟨🟨🟨⬛
```

### minisudoku
```
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   │   │ 1 ┃   │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │ 2 │   ┃   │ 3 │   ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃ 3 │   │   ┃ 4 │   │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │ 5 ┃   │   │ 6 ┃
┣━━━━━━━━━━━╋━━━━━━━━━━━┫
┃   │ 6 │   ┃   │ 2 │   ┃
┃───┼───┼───┃───┼───┼───┃
┃   │   │   ┃ 1 │   │   ┃
┗━━━━━━━━━━━┻━━━━━━━━━━━┛
```

### patches
```
+----+----+----+----+----+----+----+----+
| |  | .. | .. | .. | .. | .. | .. | +8 |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | =  | +2 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | -  | .. | .. | +6 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | -  | .. | .. | +2 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | -  | +4 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | -  | .. | .. | +4 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | |  | .. | .. | +4 | .. | .. |
+----+----+----+----+----+----+----+----+
| .. | .. | .. | |  | +2 | .. | .. | .. |
+----+----+----+----+----+----+----+----+
```

### wend
```
+---+---+---+---+---+---+
| # | U | N | T | A | # |
+---+---+---+---+---+---+
| M | O | E | C | I | N |
+---+---+---+---+---+---+
| # | M | O | I | N | # |
+---+---+---+---+---+---+
| M | E | R | Y | O | N |
+---+---+---+---+---+---+
| # | C | H | T | R | # |
+---+---+---+---+---+---+
| M | S | A | U | E | N |
+---+---+---+---+---+---+

Words:
  NICE
  CHASM
  MEMORY
  NEUTRON
  MOUNTAIN
```

### pinpoint
```
  1. Try
  2. Goal
  3. Ace
  4. Home run
  5. Free throw (worth 1 if made)

  answer: Different ways to score points in sports!
```

### crossclimb
```
game      : crossclimb
number    : 941
date      : 2026-11-27
difficulty: None

Ladder (word : clue, top -> bottom):
  nerd : The top + bottom rows = Two words for someone who is very enthusiastic and knowledgeable about a particular subject.
  need : Requirement
  feed : Provide with sustenance
  feel : Experience, as an emotion
  peel : Outer part of some fruit
  peek : Quick look (not to be confused with a mountain)
  geek : The top + bottom rows = Two words for someone who is very enthusiastic and knowledgeable about a particular subject.
```
<!-- DAILY-GAMES-END -->
