#!/usr/bin/env python3
"""白系背景で生成したキャラ画像を、綺麗に切り抜く（Design Wheel 用）

方式（Mac標準「背景を削除」の白フチ・カクカク・穴の取り残しを回避）:
  0. 背景色を画像の外周からサンプリング（純白でも薄グレーでも対応）
  1. 外周から繋がった"背景色っぽい領域"を flood fill で特定
  2. 囲まれた背景色領域（バッグ取っ手の隙間・腕の隙間等の「穴」）も、
     背景色との近さ（純度）で判定して透過。白い靴・服・地図は陰影があるので残る
  3. 輪郭を erode して縁の混色を除去 → 内側限定のぼかしでなめらかに
  4. 半透明画素から背景色の混入を数学的に除去（デフリンジ/unpremultiply）

使い方:
  python3 whitebg-cutout.py <入力.png> [出力.png]
  出力省略時は <入力>_cutout.png
"""
import sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
from collections import deque

THRESH = 60          # 背景判定のゆるさ（背景色とのRGB差合計）
HOLE_PURITY = 0.70   # 囲まれた領域を「穴」と判定する背景色純度
HOLE_MIN = 30        # 穴とみなす最小画素数
ERODE_PX = 3         # 輪郭を削る量
FEATHER = 1.5        # エッジのぼかし半径
MIN_BG_BRIGHT = 200  # 背景とみなす明るさの下限（暗背景は対象外）

def cutout(src_path, dst_path):
    im = Image.open(src_path)
    if im.mode == 'RGBA':
        base = Image.new('RGBA', im.size, (255, 255, 255, 255))
        im = Image.alpha_composite(base, im)
    im = im.convert('RGB')
    w, h = im.size
    arr = np.asarray(im).astype(np.int32)

    # --- 0) 背景色を外周からサンプリング ---
    border = np.concatenate([arr[0], arr[-1], arr[:, 0], arr[:, -1]])
    bgc = np.median(border, axis=0)
    if bgc.min() < MIN_BG_BRIGHT:
        print(f"警告: 背景が白系でない（{bgc}）。白系背景の画像専用です。処理は続行。")
    diff = np.abs(arr - bgc).sum(axis=2)
    nearbg = diff <= THRESH
    pure = diff <= 14

    # --- 1) 外周から flood fill（背景の連結領域） ---
    bg = np.zeros((h, w), bool)
    dq = deque()
    for x in range(w):
        for y in (0, h - 1):
            if nearbg[y, x] and not bg[y, x]: bg[y, x] = True; dq.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if nearbg[y, x] and not bg[y, x]: bg[y, x] = True; dq.append((y, x))
    while dq:
        y, x = dq.popleft()
        for ny, nx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)):
            if 0 <= ny < h and 0 <= nx < w and nearbg[ny, nx] and not bg[ny, nx]:
                bg[ny, nx] = True; dq.append((ny, nx))

    # --- 2) 囲まれた背景色領域＝「穴」も背景化（純度で白い物体と見分ける） ---
    rest = nearbg & ~bg
    seen = np.zeros((h, w), bool)
    for y0 in range(h):
        for x0 in range(w):
            if rest[y0, x0] and not seen[y0, x0]:
                q = deque([(y0, x0)]); seen[y0, x0] = True; px = []
                while q:
                    cy, cx = q.popleft(); px.append((cy, cx))
                    for ny, nx in ((cy-1,cx),(cy+1,cx),(cy,cx-1),(cy,cx+1)):
                        if 0 <= ny < h and 0 <= nx < w and rest[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True; q.append((ny, nx))
                if len(px) >= HOLE_MIN and np.mean([pure[p] for p in px]) >= HOLE_PURITY:
                    for p in px: bg[p] = True

    alpha = np.where(bg, 0, 255).astype(np.uint8)
    a = Image.fromarray(alpha, 'L')
    # --- 3) erode → 内側限定ぼかし ---
    for _ in range(ERODE_PX):
        a = a.filter(ImageFilter.MinFilter(3))
    hard = a
    soft = a.filter(ImageFilter.GaussianBlur(FEATHER))
    a = Image.fromarray(np.minimum(np.asarray(soft), np.asarray(hard)), 'L')

    # --- 4) デフリンジ（背景色の混入を除去） ---
    rgb = arr.astype(np.float32)
    af = np.asarray(a).astype(np.float32) / 255.0
    af3 = af[:, :, None]
    eps = 1e-4
    edge = (af > 0.01) & (af < 0.999)
    unmix = (rgb - bgc[None, None, :] * (1.0 - af3)) / np.maximum(af3, eps)
    out_rgb = np.where(edge[:, :, None], np.clip(unmix, 0, 255), rgb).astype(np.uint8)

    out = np.dstack([out_rgb, np.asarray(a)])
    Image.fromarray(out, 'RGBA').save(dst_path)
    kb = round(len(open(dst_path, 'rb').read()) / 1024)
    print(f"saved: {dst_path} ({w}x{h}, {kb}KB, bg={tuple(int(v) for v in bgc)})")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else src.rsplit('.', 1)[0] + '_cutout.png'
    cutout(src, dst)
