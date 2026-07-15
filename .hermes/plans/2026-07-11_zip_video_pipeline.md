# Zip Pipeline: video → board → extract → solve  (Implementation Plan)

> **For Hermes:** Use subagent-driven-development to implement task-by-task.

**Goal:** From a daily gameplay *video*, automatically (1) locate the Zip board inside the
video, (2) extract grid topology + node ids + walls, (3) solve the 1→K connect
path, and (4) emit the solution. Runs ~once/day; must be reliable and cheap.

**Architecture:** Two decoupled stages behind a thin daily driver.
- *Stage A — board acquisition:* sample video frames → use vision to localize the
  Zip grid in a frame → crop to a clean board image (same as today's screenshots).
- *Stage B — extract + solve:* reuse the existing `extract_zip.py` (grid/walls/
  positions already solid) but with **cache-once vision labeling** for node ids, then
  a new `solve_zip.py` that consumes the JSON.
Vision is called at most ONCE per game (results cached), so the per-day cost is one
vision read — effectively free under the Nous subscription (no per-call billing).

**Tech Stack:** Python3 + numpy + Pillow (already present). `ffmpeg` (or
python `imageio-ffmpeg`/`opencv`) for frame extraction — install step TBD.
Tesseract stays as an *offline fallback* for 1-digit disks only. Vision via
`hermes_tools.vision_analyze` (already used successfully for labeling).

---

## Phase 1 — Cache-once vision labeling (fix current code)
Current state: `extract_zip.py` calls `label_disks()` (vision) on EVERY run and also
keeps a stale `LABELED` dict. Fix so vision runs once per stem and the result is
persisted.

### Task 1.1: Persist vision labels to disk
- Modify: `src/extract_zip.py` — move `LABELED` out of the module into a JSON
  cache file `src/disk_labels.json` (`{stem: [int,...]}`), loaded at startup,
  updated when a fresh vision read happens, saved after.
- `main()`: if `stem` already in cache → use cached labels (NO vision, offline,
  instant). Else call `label_disks()`, store, save.
- Step: run on `Zip_9.jpg` and `Zip_10.jpg`; confirm each produces correct node
  count + ids (cross-check by re-pasting the montage once).
- Risk: cache must be keyed by stem and ordered exactly as
  `find_disk_cells` sorts (`round(cy//10), cx`) — already the contract.

### Task 1.2: Deprecate the OCR/template path
- `ocr_digit` + `zip_legend.json` + `build_legend.py` become fallback-only (or
  removed). Keep `ocr_digit` as offline fallback for 1-digit disks when a stem has
  no cache and vision is unavailable. Remove the INVOKED-every-run behavior.
- Validation: `extract_zip.py inputs/Zip_1.jpg` with cache present → 0 vision
  calls, instant, matches known output.

---

## Phase 2 — Video → board frame
Open question (see below) gates exact tooling, but the task shape is:

### Task 2.1: Frame extraction tooling
- Install `ffmpeg` via `apt install -y ffmpeg` (or `pip install imageio-ffmpeg`
  if apt is heavy). Verify with `ffprobe`.
- Write `src/video_frames.py`: given a video path, dump N evenly-spaced frames
  (e.g. 1/sec or 30 frames) to a temp dir as PNG.

### Task 2.2: Localize the Zip board in a frame
- For each candidate frame, call vision ONCE with a tight prompt: "Is there a numbered
  grid puzzle (cells with digits 1..N) in this image? If yes, return the pixel
  bounding box of the grid." Use the first frame that answers yes.
- Crop that bbox → save as `inputs/Zip_<date>.jpg` (the same format Stage B expects).
- Risk: LinkedIn UI chrome / ads / other games in the same video. Mitigation: prompt
  asks specifically for "numbered grid with connected nodes"; can scan multiple
  frames and pick the one with the clearest grid.

---

## Phase 3 — Solver (`src/solve_zip.py`)
Consumes `outputs/<stem>.json` (grid_size, start, nodes[{id,row,col}],
walls[[r1,c1],[r2,c2]]).

### Task 3.1: Build the cell graph
- Cells = grid_size[0]×grid_size[1], 0-indexed. Two cells are adjacent iff
  orthogonally neighboring AND the shared edge is NOT a wall.
- Validation: for `Zip_1.json`, assert adjacency count matches expectations.

### Task 3.2: Path search 1→2→…→K
- Sort nodes by id. For each consecutive pair (a→b), find a simple path on the
  graph from a to b. Constraint across the WHOLE solution: no cell may be visited
  twice (the drawn line can't cross itself). This is a sequential
  constraint-path problem → DFS backtracking per segment, carrying the set of used
  cells forward.
- Output: ordered list of cells (or edge moves) forming the full 1→K path.
- Validation: run on `Zip_1`..`Zip_10`; confirm each yields a valid,
  non-self-crossing, wall-respecting path that hits nodes 1..K in order. (Some
  LinkedIn Zip variants may allow revisits — confirm semantics; see questions.)

---

## Phase 4 — Daily one-shot driver
### Task 4.1: `src/solve_today.py <video-or-image>`
- If video: Phase 2 (frames → localize → crop). If image: use directly.
- Run `extract_zip.py` on the board (cache-once labeling).
- Run `solve_zip.py` on the JSON.
- Print / persist the solution path. Optional: emit an autoinput script to replay
  the path on-device (only if user wants auto-play).

---

## Open questions (block Phase 2/3 design)
1. **Video source/format** — is it a screen recording of the LinkedIn app
   (full-screen board) or a longer clip with the game embedded among other content?
   How is the file delivered (local path on this device)?
2. **Solver semantics** — confirm: connect nodes 1→2→…→K as ONE continuous
   path, no wall crossing, no cell reuse? Or is each segment independent?
3. **Output destination** — just print the solution, or actually auto-play it on
   the phone (tap/scroll simulation via autoinput)?

## Validation summary
- Phase 1: Zip_9/Zip_10 labeled correctly; cache makes re-runs free + instant.
- Phase 2: a board crop is produced from a sample video.
- Phase 3: all 10 JSONs solve to valid paths.
- Phase 4: one command turns a video into a solution.
