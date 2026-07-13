#!/usr/bin/env python3
"""白背景で生成したキャラ画像を、綺麗に切り抜く（Design Wheel 用）

Mac標準「背景を削除」の弱点（白フチ・カクカク輪郭）を回避する方式:
  1. 外周から繋がった"白っぽい領域"だけを背景として flood fill で特定
     （キャラ内部の白（スニーカー等）は保護される）
  2. 輪郭を1px erode して白フチの芯を除去
  3. アルファを軽くブラー → なめらかなエッジ（アンチエイリアス）
  4. 半透明画素の色から白の混入を数学的に除去（デフリンジ/unpremultiply）

使い方:
  python3 whitebg-cutout.py <入力.png> [出力.png]
  出力省略時は <入力>_cutout.png
"""
import sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

THRESH = 60          # flood fill の白判定のゆるさ（大きいほど影も背景扱い）
ERODE_PX = 3         # 輪郭を削る量（白フチの芯を除去）
FEATHER = 1.5        # エッジのぼかし半径（なめらかさ）

def cutout(src_path, dst_path):
    im = Image.open(src_path)
    if im.mode == 'RGBA':
        # 既に透過済み（Mac「背景を削除」後など）→ 一度白背景に戻してから
        # 処理し直す。焼き付いた白フチ・ギザギザもまとめて除去できる。
        base = Image.new('RGBA', im.size, (255, 255, 255, 255))
        im = Image.alpha_composite(base, im)
    im = im.convert('RGB')
    w, h = im.size

    # --- 1) 外周から flood fill で背景（白の連結領域）を特定 ---
    MARK = (255, 0, 255)
    ff = im.copy()
    seeds = [(0,0),(w-1,0),(0,h-1),(w-1,h-1),(w//2,0),(w//2,h-1),(0,h//2),(w-1,h//2)]
    for xy in seeds:
        if ff.getpixel(xy) != MARK:
            ImageDraw.floodfill(ff, xy, MARK, thresh=THRESH)
    arr = np.asarray(ff)
    bg = (arr[:,:,0]==255) & (arr[:,:,1]==0) & (arr[:,:,2]==255)
    alpha = np.where(bg, 0, 255).astype(np.uint8)

    a = Image.fromarray(alpha, 'L')
    # --- 2) erode（白フチの芯を落とす） ---
    for _ in range(ERODE_PX):
        a = a.filter(ImageFilter.MinFilter(3))
    hard = a  # ぼかし前の境界（これより外に広げない）
    # --- 3) エッジをなめらかに（※内側にだけ効かせる: 外側に滲むと白ハローが出る） ---
    soft = a.filter(ImageFilter.GaussianBlur(FEATHER))
    a = Image.fromarray(np.minimum(np.asarray(soft), np.asarray(hard)), 'L')

    # --- 4) デフリンジ: 半透明画素から白の混入を除去 ---
    rgb = np.asarray(im).astype(np.float32)
    af = np.asarray(a).astype(np.float32) / 255.0
    af3 = af[:,:,None]
    eps = 1e-4
    # C_observed = C_true*a + 255*(1-a)  →  C_true = (C - 255*(1-a)) / a
    edge = (af > 0.01) & (af < 0.999)
    unmix = (rgb - 255.0*(1.0-af3)) / np.maximum(af3, eps)
    out_rgb = np.where(edge[:,:,None], np.clip(unmix, 0, 255), rgb).astype(np.uint8)

    out = np.dstack([out_rgb, np.asarray(a)])
    Image.fromarray(out, 'RGBA').save(dst_path)
    kb = round(len(open(dst_path,'rb').read())/1024)
    print(f"saved: {dst_path} ({w}x{h}, {kb}KB)")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else src.rsplit('.',1)[0] + '_cutout.png'
    cutout(src, dst)
