#!/bin/bash
# FAMBOX バナー HTML → PNG 書き出し（Chrome ヘッドレス・Retina ×2・インストール不要）
# 使い方: ./capture.sh            → 5サイズすべて
#         ./capture.sh 1x1        → 指定サイズのみ
set -e
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DIR="$(cd "$(dirname "$0")" && pwd)"
HTML="file://$DIR/banner-export.html"
OUT="$DIR/out"; mkdir -p "$OUT"

size_of(){ case "$1" in
  1x1) echo "1080,1080";; 4x5) echo "1080,1350";; 9x16) echo "1080,1920";;
  16x9) echo "1280,720";; 191x1) echo "1200,630";; *) echo "1080,1080";; esac; }
TARGETS=${1:+$1}; TARGETS=${TARGETS:-"1x1 4x5 9x16 16x9 191x1"}

for ar in $TARGETS; do
  wh=$(size_of "$ar")
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --window-size="$wh" --default-background-color=00000000 \
    --virtual-time-budget=2500 \
    --screenshot="$OUT/banner-$ar@2x.png" "$HTML?ar=$ar" >/dev/null 2>&1
  echo "✓ $OUT/banner-$ar@2x.png ($wh ×2)"
done
