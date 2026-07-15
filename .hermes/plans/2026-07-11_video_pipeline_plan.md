# LinkedIn Games — Video Pipeline (backlog + daily)  Implementation Plan

> **For Hermes:** Use subagent-driven-development to implement task-by-task.

**Goal:** From a screen recording of a full LinkedIn games playthrough
(all 8 games: Zip, Tango, Queens, Pinpoint, Crossclimb, Mini Sudoku,
Patches, Wend), automatically locate EACH game's board in the frames,
extract its data, and write one JSON per game into a per-day folder.
Also produces a 1-FPS archive copy of the video for future re-checks.

**Architecture:** One daily driver `src/process_video.py <video.mp4>`:
1. Parse `<date>` from the filename (`Sreenrecorder-YYYY-MM-DD-...`).
2. **Extract-from-ORIGINAL first** → then ffmpeg the original down to 1 FPS
   for the archive (never extract from the shrunk copy).
3. Sample frames; for each game, vision-localize its board, crop it, and
   run the matching extractor.
4. Write `recordings_processed/<date>/{zip,tango,queens,pinpoint,
   crossclimb,minisudoku,patches,wend}.json`.

**Shared schema (identical to the webscraper plan):** each game JSON =
`{game, date, <game-fields>, raw}`. See that plan for the field list.
The video path and the scraper path MUST emit the same schema so downstream
consumers (solver, replay) don't care which produced the data.

**Tech Stack:** Python3 + numpy + Pillow (present). `ffmpeg` (apt install).
Vision via `hermes_tools.vision_analyze` (one read per game, cached).
No OCR/template path (dropped — unreliable). No solver (out of scope).

**Runs where:** this Termux device (everything here already works).

---

## Phase 0 — Recon / tooling

### Task 0.1: Install ffmpeg
- `apt install -y ffmpeg` (or `pkg install ffmpeg`). Verify `ffprobe --version`.
- Validation: `ffprobe inputs/Screenrecorder-2026-07-11-10-19-43-872.mp4`
  prints stream info (duration, resolution).

### Task 0.2: Frame-sampling helper
- `src/frames.py`: `extract_frames(video, out_dir, fps=1)` → writes
  `frame_0001.png ...` (1/sec is enough to catch each game's board).
- Validation: on the deposited video, count frames ≈ duration seconds; inspect
  one frame visually (vision) to confirm the games are visible & legible.

### Task 0.3: Confirm the 8 games' on-screen order/layout
- vision-scan ~5 sampled frames; note which games appear and roughly when
  (the playthrough is sequential: game1 finishes → game2 starts...).
  Save to `notes/video_layout.md`.
- This tells the localizer whether to scan the whole video or just look for
  "the next unseen game".

---

## Phase 1 — Board localizer (vision, once per game)

### Task 1.1: `localize_board(frame, game_name) -> bbox | None`
- vision prompt: "Does this frame show a {game_name} board (the grid/puzzle
  for that game)? If yes, return the pixel bounding box [x0,y0,x1,y1] of
  the board only. If no board is visible, answer 'NONE'."
- Try a handful of sampled frames per game; return the first bbox found.
- Validation: on the deposited video, for each of the 8 games, confirm we
  get a bbox from *some* frame (print the frame index + bbox).

### Task 1.2: Crop + persist
- `crop_board(video, bbox, frame_idx) -> inputs/<game>_<date>.png` (a clean
  still of just that board, same format the per-game extractors expect).
- Validation: visually confirm 2 cropped boards look clean (no UI chrome,
  board centered).

---

## Phase 2 — Per-game extractors (image → schema)

Reuse / adapt existing `src/extract_zip.py` for Zip; build the other 7
against vision-read boards the same way (positions auto-detected; node/id
values via cache-once vision). Each returns the normalized dict.

### Task 2.1: extract_zip  (already mostly done)
- Current `extract_zip.py` has solid grid/walls/positions + a vision
  `label_disks`. **Fix:** make labeling cache-once (see Task 2.0) and
  operate on the cropped board still instead of the full frame.
- Validation: `Zip_9` / `Zip_10` (already in inputs/) produce correct
  grid + all node ids (cross-check by one vision montage read, cached).

### Task 2.0: Cache-once vision labeling (cross-cutting, do before 2.1+)
- Replace the module-level `LABELED` dict with `src/disk_labels.json`
  (`{stem: [int,...]}`), loaded at startup, updated + saved when a fresh
  vision read happens. `extract_zip.py` uses it; re-runs on the same
  board = 0 vision calls, instant, offline.
- Validation: first run on a board does 1 vision call; second run does 0
  and matches.

### Task 2.2: extract_tango
### Task 2.3: extract_queens
### Task 2.4: extract_pinpoint
### Task 2.5: extract_crossclimb
### Task 2.6: extract_minisudoku
### Task 2.7: extract_patches
### Task 2.8: extract_wend

(Each: 2–5 min. Detect the board structure from the cropped still
(vision for values/labels, geometry for grid), normalize to schema, keep
`raw` = verbatim. Validate each against a sanity check — e.g. grid
dimensions non-empty, expected field counts.)

---

## Phase 3 — Daily driver + archiving

### Task 3.1: `src/process_video.py <video.mp4> [--date YYYY-MM-DD]`
- Parse date from filename (default) or `--date`.
- Extract frames to a temp dir. For each game: localize → crop → extract.
- Write `recordings_processed/<date>/<game>.json` (8 files).
- Validation: on the deposited video, `recordings_processed/2026-07-11/`
  has 8 valid JSONs matching the shared schema.

### Task 3.2: ffmpeg archive (AFTER extraction)
- `ffmpeg -i <orig> -vf fps=1 -c:v libx264 -crf 28 <archive>/<date>_1fps.mp4`
- Keep the ORIGINAL untouched until extraction succeeds; only then (or
  always, as a parallel archive step) produce the 1-FPS copy.
- Validation: archive file plays, ~1 frame/sec, much smaller.

### Task 3.3: Cleanup + idempotency
- Remove temp frames. If `recordings_processed/<date>/` already exists,
  skip/confirm (don't overwrite without asking).
- Validation: re-running on the same video is a no-op / safe.

---

## Risks / tradeoffs
- **Sequential playthrough assumption** (Task 0.3): if the user jumps
  around games, localizer scans all frames — fine, just slower.
- **Vision cost**: ≤1 read per game per video = ≤8 vision calls/video.
  Under the Nous subscription = no per-call billing. Backlog of ~365 videos
  = ~2920 calls total, spread over time, all cached after first.
- **Board stills vs full frames**: we crop to the board so extractors reuse
  the same code that works on screenshots today.
- **No solver**: explicitly out of scope per user; schema carries enough
  (`raw`) to build solvers later without re-processing video.

## Validation summary
- Phase 0: ffmpeg present; frames extractable; layout noted.
- Phase 1: each of 8 games localizes to a bbox in the deposited video.
- Phase 2: each extractor yields schema-correct JSON (Zip verified on
  Zip_9/Zip_10).
- Phase 3: one command turns the deposited (and any future) video into
  `recordings_processed/<date>/` with 8 JSONs + a 1-FPS archive.
