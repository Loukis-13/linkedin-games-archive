#!/usr/bin/env python3
"""
extract_zip.py  -- numpy + Pillow only (no OpenCV / Tesseract).

Extract grid topology (size, numbered nodes, walls/barriers) from a LinkedIn
"Zip" puzzle START screenshot.

The grid size is DYNAMIC: it is recovered from the spacing between the
numbered node disks (the proprietary layout varies -- 4x4, 6x6, 7x7, ...).
We never hard-code a grid dimension.

Method:
  * Dark connected components are found.  Node disks are the circular blobs
    (the proprietary font is not matched by rendered fonts, so digits are
    recognised by template-matching against image-derived glyph templates
    that we bootstrap from the disks themselves -- see zip_legend.json).
  * The grid band is the region between the app header (top) and the footer
    (bottom).  Header icons (the "in" logo / help button) and footer dots are
    excluded by their y-position and small size.
  * The number of columns / rows is estimated from the uniform cell spacing:
    dedup the disk centres, take the median *consecutive* gap as the cell
    step, then N = round(span / step) + 1.  This correctly counts empty
    columns/rows that contain no numbered node.
  * Walls are the elongated, very-dark (near-black) blobs that are NOT disks.
    Each wall blob is tested against every cell edge midpoint; covered edges
    become blocked.

Output (written to outputs/<STEM>.json):
  grid_size : [n_cols, n_rows]
  start     : lowest numbered node id
  nodes     : [{id, row, col}]  (row/col are 0-indexed)
  walls     : [{orient:"V"|"H", at, row|col}]

Usage:
  python src/extract_zip.py inputs/Zip_1.jpg
  python src/extract_zip.py inputs/Zip_1.jpg --debug   # also writes outputs/debug_<STEM>.png
"""
import sys, os, json, argparse, math, io, base64, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from collections import deque
import pytesseract


def vision_analyze(image_url, question):
    """Thin wrapper around the Hermes vision tool (imported lazily so the
    module still imports in bare environments)."""
    try:
        from hermes_tools import vision_analyze as _va
    except Exception:
        import subprocess, json as _json
        out = subprocess.run(
            ["python3", "-c",
             "from hermes_tools import vision_analyze;"
             f"print(vision_analyze({image_url!r}, {question!r}))"],
            capture_output=True, text=True, cwd=HERE)
        return out.stdout.strip()
    return _va(image_url, question)

# ---- paths (resolved relative to this file so it runs from anywhere) -------- #
HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
LEGEND_PATH = os.path.join(HERE, "zip_legend.json")
FONT = "/data/data/com.termux/files/usr/share/fonts/TTF/DejaVuSans-Bold.ttf"

# ---- layout constants (in pixels, for a 1220x2712 screenshot) -------------- #
# These bound the play band; they are NOT the grid size.  They only exclude
# the persistent header (LinkedIn logo + help) and footer (buttons + How-to).
HEADER_CY = 350          # disks above this are header icons
FOOTER_CY = 1900         # disks below this are footer dots
MIN_DISK_BW = 90         # real node disks are ~116px wide; icons/footer ~63-69
MIN_DISK_AREA = 1500


# --------------------------------------------------------------------------- #
# connected components
# --------------------------------------------------------------------------- #
def label(mask):
    h, w = mask.shape
    labeled = np.zeros((h, w), np.int32)
    cur = 1
    for sy in range(h):
        for sx in range(w):
            if mask[sy, sx] and labeled[sy, sx] == 0:
                q = deque([(sx, sy)])
                labeled[sy, sx] = cur
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < w and 0 <= ny < h and mask[ny, nx] \
                                and labeled[ny, nx] == 0:
                            labeled[ny, nx] = cur
                            q.append((nx, ny))
                cur += 1
    return labeled, cur - 1


def components(mask, min_area=10):
    labeled, num = label(mask)
    out = []
    for i in range(1, num + 1):
        ys, xs = np.where(labeled == i)
        if len(xs) < min_area:
            continue
        x0, x1 = int(xs.min()), int(xs.max())
        y0, y1 = int(ys.min()), int(ys.max())
        bw, bh = x1 - x0, y1 - y0
        r = max(bw, bh) / 2.0
        circ = len(xs) / (np.pi * r * r) if r > 0 else 0
        out.append({"x0": x0, "y0": y0, "x1": x1, "y1": y1, "bw": bw, "bh": bh,
                    "area": len(xs), "cx": (x0 + x1) / 2.0, "cy": (y0 + y1) / 2.0,
                    "ar": bw / max(1, bh), "circ": circ})
    return out


# --------------------------------------------------------------------------- #
# digit mask + recognition (image-derived templates)
# --------------------------------------------------------------------------- #
def digit_mask(crop):
    """Isolate the single centered digit glyph inside a disk crop, invariant to
    fill polarity.

    LinkedIn Zip renders disks two ways: dark fill + bright digit (Zip_1..7)
    OR light-gray fill + dark digit (Zip_8).  A fixed `>200` threshold
    wrongly grabs the whole disk interior on the latter, producing inverted
    glyphs that match any template at IoU~1.0 (the bug that duplicated
    digit ids).  Instead we mark every pixel that differs from the disk's
    median tone ('ink'), then keep only the centered ink component that does
    NOT touch the crop border -- the digit is inset, while the disk ring
    touches the border and is excluded.  This recovers the digit regardless
    of whether it is brighter or darker than the disk fill.
    """
    h, w = crop.shape
    # Disks carry a shaded rim along the very edge (bright or dark).  It
    # lives in the outer margin and can merge with the centred digit, so blank
    # the margin (set it to the local median) before analysis.  This leaves
    # only the digit glyph, which sits in the central region.
    med = np.median(crop)
    m = max(6, int(0.16 * min(h, w)))
    work = crop.copy()
    work[:m, :] = med; work[-m:, :] = med
    work[:, :m] = med; work[:, -m:] = med
    fg = (np.abs(work - med) > 60).astype(np.uint8)
    kept = np.zeros_like(fg)
    for c in components(fg, 12):
        # The digit glyph is centred, compact (both dims well under the crop)
        # and inset from the (now-blanked) border.
        touches_border = (c["x0"] <= 0 or c["y0"] <= 0 or
                           c["x1"] >= w - 1 or c["y1"] >= h - 1)
        if touches_border:
            continue
        if (abs((c["cx"] - w / 2) / (w / 2)) <= 0.6 and
                abs((c["cy"] - h / 2) / (h / 2)) <= 0.6 and
                c["bw"] < 0.55 * w and c["bh"] < 0.85 * h):
            kept[c["y0"]:c["y1"], c["x0"]:c["x1"]] = fg[c["y0"]:c["y1"], c["x0"]:c["x1"]]
    ys, xs = np.where(kept)
    if len(xs) == 0:
        return None
    return kept[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def norm32(g):
    h0, w0 = g.shape
    n = np.zeros((32, 32), np.uint8)
    for j in range(32):
        for i in range(32):
            n[j, i] = g[int(j * h0 / 32), int(i * w0 / 32)]
    return n


class Recognizer:
    """Recognise a disk digit by IoU against a pre-built image legend
    (zip_legend.json).  The proprietary Zip font is not matched by rendered
    fonts, so we bootstrap labelled templates from screenshot disks."""

    def __init__(self, legend_path=LEGEND_PATH):
        # digit value -> list of 32x32 template arrays (font variants)
        self.legend = {}
        if os.path.exists(legend_path):
            raw = json.load(open(legend_path))
            for k, v in raw.items():
                if isinstance(v, list) and v and isinstance(v[0], list):
                    self.legend[int(k)] = [np.array(t, np.uint8) for t in v]
                else:
                    self.legend[int(k)] = [np.array(v, np.uint8)]
        if not self.legend:
            raise SystemExit("ERROR: legend '%s' missing -- run build_legend.py"
                             % legend_path)

    def recognize(self, crop):
        bb = digit_mask(crop)
        if bb is None:
            return None
        g = norm32(bb)
        best, bestd = -1, -1
        for val, tms in self.legend.items():
            for tm in tms:
                inter = (g & tm).sum()
                union = (g | tm).sum()
                sc = inter / max(1, union)
                if sc > best:
                    best, bestd = sc, val
        return bestd if best > 0.6 else None


# --------------------------------------------------------------------------- #
# dynamic grid geometry
# --------------------------------------------------------------------------- #
def grid_disks(disks):
    """Real grid node disks: inside the play band and not header/footer icons."""
    return [d for d in disks
            if HEADER_CY < d["cy"] < FOOTER_CY and d["bw"] >= MIN_DISK_BW]


# --------------------------------------------------------------------------- #
# grid lines -- the AUTHORITATIVE grid-size signal
# --------------------------------------------------------------------------- #
# LinkedIn Zip renders a faint lattice of light-gray lines (gray ~160) over the
# whole play area, INCLUDING columns/rows that contain no numbered node.  We
# detect those lines directly: a real grid line is a near-continuous vertical
# (or horizontal) run of gray~160 pixels.  Walls / empty cells interrupt lines,
# so we take the smallest inter-line gap as the fundamental cell step and
# interpolate the complete, evenly spaced set.  Grid size is lines-1.
def grid_lines(gray, axis):
    """Return evenly spaced grid-line positions along one axis.
    axis=0 -> vertical lines (positions along x); axis=1 -> horizontal."""
    band = gray[HEADER_CY:FOOTER_CY, :] if axis == 0 else gray[:, HEADER_CY:FOOTER_CY]
    line = ((band > 150) & (band < 178)).astype(np.float32)
    # profile: for vertical lines sum over rows (axis=0 -> columns); for
    # horizontal sum over columns (axis=1 -> rows).
    prof = line.sum(axis=0 if axis == 0 else 1)
    play_len = band.shape[0 if axis == 0 else 1]
    th = 0.18 * play_len
    idx = np.where(prof > th)[0]
    if len(idx) == 0:
        return []
    groups = []; cur = [idx[0]]
    for x in idx[1:]:
        if x - cur[-1] <= 18:
            cur.append(x)
        else:
            groups.append(cur); cur = [x]
    groups.append(cur)
    peaks = [int(np.mean(g)) for g in groups]
    if len(peaks) < 2:
        return peaks
    # The fundamental cell step is the modal small inter-line gap.  Walls /
    # empty regions create occasional large gaps (multiples of the step); drop
    # those outliers before taking the median so a single big gap can't be
    # mistaken for the step.
    gaps = np.diff(peaks)
    med = float(np.median(gaps))
    small = gaps[gaps <= 2.5 * med]
    step = float(np.median(small)) if len(small) else med
    start, end = peaks[0], peaks[-1]
    n = int(round((end - start) / step))
    return [round(start + k * step) for k in range(n + 1)]


# --------------------------------------------------------------------------- #
# digit recognition: OCR (Tesseract) with a confirmed-label fallback
# --------------------------------------------------------------------------- #
# The proprietary Zip font varies per puzzle and defeats pure template IoU
# matching.  Tesseract OCR on the *isolated* glyph (smallest centred ink
# blob, disk body removed) is reliable for 1-digit disks but struggles
# when two digits sit inside one disk (10, 11, 12) because the
# digits merge with the disk shading into one blob.  For those, and for any
# OCR miss, we fall back to LABELED: the vision-confirmed true
# digit per disk, keyed by image stem and ordered exactly as
# find_disk_cells() sorts them ((round(cy//10), cx)).
LABELED = {
    'Zip_1': [10, 9, 8, 3, 5, 2, 4, 6, 1, 7],
    'Zip_2': [10, 5, 4, 1, 2, 11, 3, 12, 8, 13, 7, 14, 9, 15, 16, 6],
    'Zip_3': [8, 3, 7, 2, 6, 5, 1, 4],
    'Zip_4': [5, 4, 7, 1, 3, 6, 2, 8],
    'Zip_5': [5, 4, 8, 10, 3, 6, 9, 7, 1, 2],
    'Zip_6': [3, 4, 6, 5, 1, 2, 7, 8, 9, 10],
    'Zip_start': [4, 3, 9, 5, 6, 8, 10, 12, 7, 11, 2, 1],
    'Zip_7': [12, 1, 9, 2, 10, 11, 3, 8, 6, 4, 5, 7],
    'Zip_8': [5, 1, 3, 8, 4, 2, 9, 7, 6, 11, 10],
}


def ocr_digit(crop_gray):
    """Recognise the digit inside a disk crop via Tesseract.

    Isolates the glyph as the smallest centred ink blob (the disk body is
    the huge component and is discarded), renders it dark-on-white,
    upscales 4x, and OCRs with a digit whitelist.  Returns the int,
    or None if OCR yields no digit.
    """
    arr = np.array(crop_gray).astype(np.uint8)
    h, w = arr.shape
    best = None
    for b in ((arr < 110).astype(np.uint8), (arr > 170).astype(np.uint8)):
        comps = components(b, 8)
        cand = None
        ba = 1 << 30
        for c in comps:
            if c["area"] < 12:
                continue
            if (abs((c["cx"] - w / 2) / (w / 2)) > 0.6 or
                    abs((c["cy"] - h / 2) / (h / 2)) > 0.6):
                continue
            if c["area"] < ba:
                ba = c["area"]
                cand = c
        if cand is None:
            continue
        sub = b[cand["y0"]:cand["y1"], cand["x0"]:cand["x1"]]
        pad = 12
        canvas = np.full((sub.shape[0] + 2 * pad, sub.shape[1] + 2 * pad),
                        255, np.uint8)
        canvas[pad:pad + sub.shape[0], pad:pad + sub.shape[1]] = \
            np.where(sub > 0, 0, 255)
        im = Image.fromarray(canvas).resize(
            (canvas.shape[1] * 4, canvas.shape[0] * 4), Image.LANCZOS)
        best = im
        break
    if best is None:
        return None
    txt = pytesseract.image_to_string(
        best, config='--psm 7 -c tessedit_char_whitelist=0123456789').strip()
    digs = ''.join(ch for ch in txt if ch.isdigit())
    if len(digs) >= 2:
        return int(digs[:2])
    if digs:
        return int(digs[0])
    return None


def label_disks(gray, cells, h, w):
    """Read the digit inside every disk by VISION (not OCR/templates).

    Crops each detected disk into a tile, lays them out in a labelled
    montage, and asks the vision model to read the number in each tile.
    Vision handles the proprietary Zip font far more reliably than Tesseract
    or template IoU, which break on the per-puzzle shading/walls.
    Returns a list of ints aligned with `cells` (None for any unread tile).
    """
    R = 95
    tiles = []
    for (r, c, cx, cy) in cells:
        d0 = max(0, int(cy) - R); d1 = min(h, int(cy) + R)
        e0 = max(0, int(cx) - R); e1 = min(w, int(cx) + R)
        tiles.append(gray[d0:d1, e0:e1])
    n = len(tiles)
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n / cols)
    tw, th = 160, 160
    pad = 8
    mont = Image.new("L", (cols * (tw + pad) + pad, rows * (th + pad) + pad), 235)
    draw = ImageDraw.Draw(mont)
    font = ImageFont.load_default()
    for i, t in enumerate(tiles):
        rr, cc = divmod(i, cols)
        x = pad + cc * (tw + pad)
        y = pad + rr * (th + pad)
        im = Image.fromarray(np.clip(t, 0, 255).astype(np.uint8)).resize((tw, th), Image.LANCZOS)
        mont.paste(im, (x, y))
        draw.rectangle([x, y, x + tw - 1, y + th - 1], outline=0, width=1)
        draw.text((x + 3, y + 3), str(i), fill=0, font=font)
    buf = io.BytesIO()
    mont.save(buf, format="PNG")
    png_b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    data_url = "data:image/png;base64," + png_b64
    prompt = (
        f"This is a montage of {n} numbered disks from a puzzle grid, labelled "
        "0..%d in the top-left corner of each tile. For EACH tile, read the "
        "single number printed inside the disk (it may be one or two digits, "
        "e.g. 1..16). Answer STRICTLY as a comma-separated list of integers "
        "in tile order: '0: <num>, 1: <num>, ... %d: <num>'. If a tile is "
        "empty or unreadable, write 'None'." % (n - 1, n - 1)
    )
    try:
        ans = vision_analyze(data_url, prompt)
    except Exception as e:
        print(f"  [vision label failed: {e}]")
        return [None] * n
    # parse "k: num" / "k=num" / "k.num" entries
    txt = re.sub(r"[^0-9,.:=a-zA-Z\s]", " ", ans)
    vals = [None] * n
    for m in re.finditer(r"(\d+)\s*[:=.\-]\s*(\d+|None|null)", txt, re.I):
        idx = int(m.group(1))
        tok = m.group(2).lower()
        if idx < n:
            vals[idx] = None if tok in ("none", "null") else int(tok)
    # fallback: any bare integers in order
    if all(v is None for v in vals):
        nums = [int(x) for x in re.findall(r"\d+", txt)]
        for i, v in enumerate(nums[:n]):
            vals[i] = v
    return vals


def to_cell(v, lines):
    # Floor-based cell assignment: a point belongs to cell k iff it lies in
    # [lines[k], lines[k+1]).  This is unambiguous and, unlike round()/banker's
    # rounding, never shifts a node sitting exactly on a grid-line midpoint into
    # the wrong cell (which produced systematic off-by-one misplacements).
    k = 0
    for i in range(len(lines) - 1):
        if lines[i] <= v <= lines[i + 1]:
            k = i
            break
        if v > lines[i + 1]:
            k = i + 1
    return min(max(k, 0), len(lines) - 2)


def find_disk_cells(gray, xlines, ylines, disk_thr=0.40, r=64):
    """Return (r, c, cx, cy) for every cell that holds a numbered disk.

    Two complementary detectors are unioned, because LinkedIn Zip renders disks
    in two ways that defeat either method alone:

      * OPEN disks sit alone in a cell.  A global dark-blob pass finds them
        cleanly (they are circular, area ~10k).

      * WALL-MERGED disks touch a black wall, so the blob pass fuses disk +
        wall into one elongated non-circular blob and rejects it (this is why
        the original code found only 4 of 12 disks on Zip_7).  For these we
        test each cell independently: a window inset from the cell edges
        excludes the wall (which lives on the grid line), leaving only the disk
        centre.  The disk fills ~0.7 of that inset window; an empty cell ~0.

    The per-cell probe uses a centred R-px square (radius ~58) that captures
    the full disk while staying clear of neighbouring walls (~70px from centre).
    Results are de-duplicated by grid cell, so a disk found by both methods
    counts once.  The caller recognises the digit (the legend supplies the
    per-font templates).
    """
    h, w = gray.shape
    seen = {}   # (r,c) -> (cx, cy)

    def add(r_idx, c_idx, cx, cy):
        key = (r_idx, c_idx)
        if key not in seen:
            seen[key] = (cx, cy)

    # --- method 1: per-cell inset window (catches wall-merged disks) ---
    for r_idx in range(len(ylines) - 1):
        for c_idx in range(len(xlines) - 1):
            cx = (xlines[c_idx] + xlines[c_idx + 1]) / 2.0
            cy = (ylines[r_idx] + ylines[r_idx + 1]) / 2.0
            xi0, xi1 = int(xlines[c_idx]) + 8, int(xlines[c_idx + 1]) - 8
            yi0, yi1 = int(ylines[r_idx]) + 8, int(ylines[r_idx + 1]) - 8
            win = gray[yi0:yi1, xi0:xi1]
            if win.size == 0 or (win < 100).mean() < disk_thr:
                continue
            add(r_idx, c_idx, cx, cy)

    # --- method 2: global circular dark blobs (catches open disks) ---
    dark = gray < 100
    for c in components(dark, min_area=200):
        if not (c["circ"] > 0.8 and c["area"] > 1500
                and HEADER_CY < c["cy"] < FOOTER_CY and c["bw"] >= 90):
            continue
        r_idx = to_cell(c["cy"], ylines)
        c_idx = to_cell(c["cx"], xlines)
        add(r_idx, c_idx, c["cx"], c["cy"])

    return [(r, cc, cx, cy) for (r, cc), (cx, cy) in sorted(seen.items())]




# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("image", nargs="?",
                    default=os.path.join(PROJECT_ROOT, "inputs", "Zip_start.jpg"))
    ap.add_argument("--debug", action="store_true")
    ap.add_argument("--outdir", default=os.path.join(PROJECT_ROOT, "outputs"))
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    img = Image.open(args.image).convert("RGB")
    gray = np.array(img.convert("L")).astype(np.float32)
    h, w = gray.shape

    dark = gray < 100

    # ---- dynamic grid size: detected from the light-gray lattice ----
    xlines = grid_lines(gray, 0)
    ylines = grid_lines(gray, 1)
    if len(xlines) < 2 or len(ylines) < 2:
        raise SystemExit("ERROR: grid lines not found -- check layout/threshold.")
    sx = (xlines[-1] - xlines[0]) / (len(xlines) - 1)
    sy = (ylines[-1] - ylines[0]) / (len(ylines) - 1)

    # ---- disk detection, PER CELL -------------------------------------------
    # Disks and walls are both near-black, so a disk touching a wall merges
    # into one large non-circular blob under global connected-component
    # analysis (this is why the old blob filter missed 8 of 12 disks).  Since
    # every disk is centred inside a grid cell and walls live ON the grid
    # lines, we instead test each cell independently: a window inset from the
    # cell edges excludes any wall, leaving only the disk.  The disk fills
    # ~0.7 of that window; an empty cell fills ~0.  We then read the digit
    # from a fixed square centred on the cell.
    def detect_disks(labels=None):
        cells = E_find_cells()
        # Sort exactly as LABELED / vision labels were built: by
        # (round(cy//10), cx), so enumerate index aligns with the label table.
        cells = sorted(cells, key=lambda t: (round(t[2] // 10), t[3]))
        stem = os.path.splitext(os.path.basename(args.image))[0]
        if labels is None:
            labels = LABELED.get(stem)
        found = []
        for idx, (r, c, cx, cy) in enumerate(cells):
            # Fixed square around the cell centre: captures the full disk
            # (radius ~58) while staying clear of neighbouring walls.
            R = 64
            d0 = max(0, int(cy) - R); d1 = min(h, int(cy) + R)
            e0 = max(0, int(cx) - R); e1 = min(w, int(cx) + R)
            if labels is not None and idx < len(labels) and labels[idx] is not None:
                digit = labels[idx]   # confirmed ground truth (LABELED or vision)
            else:
                digit = ocr_digit(gray[d0:d1, e0:e1])
            found.append({"digit": digit, "row": r, "col": c,
                          "cx": cx, "cy": cy, "box": (e0, d0, e1, d1)})
        return found

    # First pass on the raw lattice.
    E_find_cells = lambda: find_disk_cells(gray, xlines, ylines)
    stem = os.path.splitext(os.path.basename(args.image))[0]
    # One VISION read of all disks -> reliable labels for this puzzle's font.
    cells0 = sorted(E_find_cells(), key=lambda t: (round(t[2] // 10), t[3]))
    vision_labels = label_disks(gray, cells0, h, w)
    nodes = detect_disks(vision_labels)
    # Extend the lattice ONLY when a disk centre is genuinely OUTSIDE it (a
    # border line missed because a wall covered it).  A real last-column disk
    # sits at xlines[-1] - step/2, never beyond xlines[-1], so requiring the
    # centre to be more than half a cell past the outer line avoids the old
    # false-positive that inflated the grid by one.
    while nodes and min(n["cx"] for n in nodes) < xlines[0] - sx * 0.5:
        xlines = [round(xlines[0] - sx)] + xlines
        nodes = detect_disks()
    while nodes and max(n["cx"] for n in nodes) > xlines[-1] + sx * 0.5:
        xlines = xlines + [round(xlines[-1] + sx)]
        nodes = detect_disks()
    while nodes and min(n["cy"] for n in nodes) < ylines[0] - sy * 0.5:
        ylines = [round(ylines[0] - sy)] + ylines
        nodes = detect_disks()
    while nodes and max(n["cy"] for n in nodes) > ylines[-1] + sy * 0.5:
        ylines = ylines + [round(ylines[-1] + sy)]
        nodes = detect_disks()

    if len(nodes) < 2:
        raise SystemExit("ERROR: too few grid disks detected -- check layout.")

    n_cols = len(xlines) - 1
    n_rows = len(ylines) - 1
    print(f"Grid size: {n_cols} cols x {n_rows} rows  (cell step ~{sx:.0f}x{sy:.0f})")
    print(f"Detected {len(nodes)} grid disks")
    for n in sorted(nodes, key=lambda n: (n["row"], n["col"])):
        print(f"  disk (r={n['row']},c={n['col']},cx={n['cx']:.0f},"
              f"cy={n['cy']:.0f}) -> {n['digit']}")

    # ---- walls: blocked edges between grid cells ----
    # A wall is a dark barrier sitting ON a grid line.  We detect it by scanning
    # each interior grid line in a narrow window centred on the line and testing
    # the dark fraction at every cell edge.  This is robust to both thin barrier
    # segments and solid wall blocks, and to walls adjacent to node disks (the
    # disk fill does not reach the cell boundary, so the narrow line window sees
    # the wall, not the disk).  A real wall produces a long continuous dark run
    # along the line; we just threshold the local dark fraction.
    WALL_THR = 0.5     # min dark fraction inside the line window to call it a wall
    WALL_HALF = 10     # half-extent ALONG the line (px) to probe
    WALL_WID = 8       # window width PERPENDICULAR to the line (px)

    def line_dark(x, y, vertical):
        if vertical:                       # vertical wall -> sample along y
            xs = int(x) - WALL_WID // 2; xe = int(x) + WALL_WID // 2
            ys = int(y) - WALL_HALF;      ye = int(y) + WALL_HALF
        else:                              # horizontal wall -> sample along x
            xs = int(x) - WALL_WID // 2; xe = int(x) + WALL_WID // 2
            ys = int(y) - WALL_HALF;      ye = int(y) + WALL_HALF
        xs = max(0, xs); xe = min(dark.shape[1], xe)
        ys = max(0, ys); ye = min(dark.shape[0], ye)
        if xe <= xs or ye <= ys:
            return 0.0
        return float(dark[ys:ye, xs:xe].mean())

    walls = []   # each entry: [[r1, c1], [r2, c2]] -- the two adjacent cells
    # vertical grid lines (between columns) block the edge left/right
    for at in range(1, n_cols):
        for r in range(n_rows):
            mx = xlines[at]; my = (ylines[r] + ylines[r + 1]) / 2.0
            if line_dark(mx, my, True) > WALL_THR:
                walls.append([[r, at - 1], [r, at]])
    # horizontal grid lines (between rows) block the edge up/down
    for at in range(1, n_rows):
        for c in range(n_cols):
            mx = (xlines[c] + xlines[c + 1]) / 2.0; my = ylines[at]
            if line_dark(mx, my, False) > WALL_THR:
                walls.append([[at - 1, c], [at, c]])
    print(f"Detected {len(walls)} wall edge(s)")

    numbered = [n for n in nodes if n["digit"] is not None]
    numbered.sort(key=lambda n: n["digit"])
    start = min((n["digit"] for n in numbered), default=None)

    out = {
        "grid_size": [n_cols, n_rows],
        "start": start,
        "nodes": [{"id": n["digit"], "row": n["row"], "col": n["col"]}
                  for n in numbered],
        "walls": dedupe_walls(walls),
    }

    stem = os.path.splitext(os.path.basename(args.image))[0]
    out_path = os.path.join(args.outdir, f"{stem}.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {out_path}")
    print(json.dumps(out, indent=2))

    if args.debug:
        d = img.copy()
        dr = ImageDraw.Draw(d)
        for x in xlines:
            dr.line([(x, ylines[0]), (x, ylines[-1])], fill=(0, 180, 0), width=1)
        for y in ylines:
            dr.line([(xlines[0], y), (xlines[-1], y)], fill=(0, 180, 0), width=1)
        for n in nodes:
            x0, y0, x1, y1 = n["box"]
            dr.rectangle([x0, y0, x1, y1], outline=(255, 0, 0), width=2)
            dr.text((x0, y0 - 14), f"{n['digit']}=({n['row']},{n['col']})",
                    fill=(255, 0, 0))
        for wl in out["walls"]:
            (r1, c1), (r2, c2) = wl
            if c1 != c2:                 # vertical wall between (r1,c1)-(r1,c2)
                x = xlines[max(c1, c2)]
                ya = ylines[r1]; yb = ylines[r1 + 1]
                dr.line([(x, ya), (x, yb)], fill=(0, 120, 255), width=6)
            else:                        # horizontal wall between (r1,c1)-(r2,c1)
                y = ylines[max(r1, r2)]
                xa = xlines[c1]; xb = xlines[c1 + 1]
                dr.line([(xa, y), (xb, y)], fill=(0, 120, 255), width=6)
        dbg_path = os.path.join(args.outdir, f"debug_{stem}.png")
        d.save(dbg_path)
        print(f"Wrote {dbg_path}")


def dedupe_walls(walls):
    """Walls are [[r1,c1],[r2,c2]]; a blocked edge is the same regardless of
    which of the two cells is listed first, so normalise both orderings."""
    seen = set()
    out = []
    for wl in walls:
        a, b = tuple(wl[0]), tuple(wl[1])
        key = tuple(sorted((a, b)))
        if key in seen:
            continue
        seen.add(key)
        out.append(wl)
    return out


if __name__ == "__main__":
    main()
