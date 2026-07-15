#!/usr/bin/env python3
"""Build (or extend) the digit legend from real screenshots.

The Zip font varies slightly between puzzle instances, so a single-image
legend is not font-invariant.  This script crops each detected disk, labels it
with its CONFIRMED digit (read by vision and hard-coded in LABELED below), and
stores ONE OR MORE 32x32 normalised glyph templates per digit value.  The
recognizer matches a query against every template for a digit and keeps the
best, so multiple font variants of the same digit all match.

Run:
  python src/build_legend.py            # merge all LABELED images into src/zip_legend.json
  python src/build_legend.py --check    # just report current legend coverage
"""
import sys, os, json, argparse, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import extract_zip as E
from PIL import Image

OUT = E.LEGEND_PATH

# Each entry: image-stem -> {disk_index (sorted by row-band then col): digit}
# disk indices come from: disks = grid_disks(...); disks.sort(by row-band, col)
LABELED = {
    'Zip_2': {0: 10, 1: 5, 2: 4, 3: 1, 4: 2, 5: 11, 6: 3, 7: 12,
              8: 8, 9: 13, 10: 7, 11: 14, 12: 9, 13: 15, 14: 16, 15: 6},
    'Zip_3': {0: 8, 1: 3, 2: 7, 3: 2, 4: 6, 5: 5, 6: 1, 7: 4},
    'Zip_1': {0: 10, 1: 9, 2: 8, 3: 3, 4: 5, 5: 2, 6: 4, 7: 6, 8: 1, 9: 7},
    'Zip_4': {0: 5, 1: 4, 2: 7, 3: 1, 4: 3, 5: 6, 6: 2, 7: 8},
    'Zip_5': {0: 5, 1: 4, 2: 8, 3: 10, 4: 3, 5: 6, 6: 9, 7: 7, 8: 1, 9: 2},
    'Zip_6': {0: 3, 1: 4, 2: 6, 3: 5, 4: 1, 5: 2, 6: 7, 7: 8, 8: 9, 9: 10},
    'Zip_start': {0: 4, 1: 3, 2: 9, 3: 5, 4: 6, 5: 8, 6: 10, 7: 12,
                  8: 7, 9: 11, 10: 2, 11: 1},
    # Zip_7 -- 8x8, 12 disks. Order MUST follow disk_templates' sort, which is
    # (round(cy//10), cx). Cells in that order:
    # 0:(7,0)=12 1:(1,1)=1 2:(0,2)=9 3:(3,2)=2 4:(5,2)=10 5:(6,3)=11
    # 6:(1,4)=3 7:(2,5)=8 8:(4,5)=6 9:(7,5)=4 10:(6,6)=5 11:(0,7)=7
    'Zip_7': {0: 12, 1: 1, 2: 9, 3: 2, 4: 10, 5: 11, 6: 3, 7: 8,
               8: 6, 9: 4, 10: 5, 11: 7},
    # Zip_8 -- 7x7, 11 disks. Order = (round(cy//10), cx):
    # 0:(1,1)=5 1:(3,1)=1 2:(4,1)=3 3:(5,1)=8 4:(1,2)=4 5:(3,2)=2
    # 6:(5,2)=9 7:(1,3)=7 8:(2,3)=6 9:(3,3)=11 10:(5,3)=10
    'Zip_8': {0: 5, 1: 1, 2: 3, 3: 8, 4: 4, 5: 2, 6: 9, 7: 7,
               8: 6, 9: 11, 10: 10},
}


def disk_templates(img_path):
    img = Image.open(img_path).convert('L')
    gray = np.array(img).astype(np.float32)
    xlines = E.grid_lines(gray, 0)
    ylines = E.grid_lines(gray, 1)
    if len(xlines) < 2 or len(ylines) < 2:
        raise SystemExit(f"{os.path.basename(img_path)}: no grid lines")
    cells = E.find_disk_cells(gray, xlines, ylines)
    # sort row-band then column (mirrors Zip_1..6 ordering above)
    cells.sort(key=lambda t: (round(t[2] // 10), t[3]))
    return cells, gray


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()

    if args.check:
        raw = json.load(open(OUT)) if os.path.exists(OUT) else {}
        print('current legend digits:', sorted(int(k) for k in raw))
        return

    legend = {}   # digit -> list of 32x32 templates
    if os.path.exists(OUT):
        raw = json.load(open(OUT))
        for k, v in raw.items():
            legend.setdefault(int(k), []).append(np.array(v, np.uint8))

    root = E.PROJECT_ROOT
    for stem, labels in LABELED.items():
        path = os.path.join(root, 'inputs', stem + '.jpg')
        if not os.path.exists(path):
            print('skip', stem, '(no image)'); continue
        cells, gray = disk_templates(path)
        assert len(cells) == len(labels), \
            f"{stem}: {len(cells)} disks vs {len(labels)} labels"
        for i, (r, c, cx, cy) in enumerate(cells):
            R = 64
            d0 = max(0, int(cy) - R); d1 = min(gray.shape[0], int(cy) + R)
            e0 = max(0, int(cx) - R); e1 = min(gray.shape[1], int(cx) + R)
            inner = gray[d0:d1, e0:e1]
            bb = E.digit_mask(inner)
            if bb is None:
                print(f"  WARN {stem} disk {i}: no mask"); continue
            tm = E.norm32(bb)
            legend.setdefault(labels[i], []).append(tm)
            print(f"  {stem} disk {i} (r{r},c{c}) -> {labels[i]}  mask {bb.shape}")

    # serialise: digit -> list of 32x32 2D template arrays.  Sanity-check
    # every template is exactly 32x32 so a malformed (e.g. nested) entry
    # can never be written -- a bad template would crash the Recognizer.
    out = {}
    for k, tmpls in legend.items():
        clean = []
        for t in tmpls:
            t = np.array(t, np.uint8)
            if t.shape == (32, 32):
                clean.append(t.tolist())
            else:
                print(f"  WARN dropping digit {k} template with bad shape {t.shape}")
        if clean:
            out[str(k)] = clean
    with open(OUT, 'w') as f:
        json.dump(out, f)
    print(f"Saved {OUT} with digits: {sorted(legend)} "
          f"(variants: {', '.join(f'{k}x{len(v)}' for k, v in sorted(legend.items()))})")


if __name__ == '__main__':
    main()
