# sporty — DS Bundle spec（Claude Design 登録用）

> このバンドルは `patterns/sporty/SYSTEM.md v0` の要点を
> Claude Design が参照できる HTML カード5枚＋サンプルLP1枚にまとめたもの。

## カード構成

| ファイル | group | name |
|---|---|---|
| 00-color.html | Foundations · sporty | Color |
| 01-type.html | Foundations · sporty | Type scale |
| 02-spacing.html | Foundations · sporty | Spacing & grid |
| 10-button.html | Components · sporty | Buttons & stat cards |
| 11-photo-depth.html | Components · sporty | Photo depth & rotation |
| _sample-stride-LP.html | — | サンプルLP（参考） |

## パターン一言定義

「計測・規格・精密」の digital に対して、sporty は**「運動量の説得」**。
アクション写真が主役。Display テキストを被写体と前後に重ねる「深度」と、
1ビビッドアクセント・色帯・統計数値で速度と熱量を作る。

## 凍結トークン（変更禁止）

- accent = #FF4D1F（energy orange）or #2E6BE6（court blue）/ 1作品1色のみ
- Display = 88px / w800 / uppercase / letter-spacing -.02em
- 余白比 = S16 / M32 / L64（等比 2x）
- 写真カード回転 = ±3〜6°

## sporty 固有の3技法（必ず使う）

1. **深度** — Display を写真・黒背景と前後に重ねる
2. **回転** — 写真カード ±3〜6°、hover で 0° 戻し
3. **デュオトーン** — accent × 写真（大面積 accent の唯一の例外）

## 昇格ステータス

- Figma 構築: STRIDE LP / 採点 11/12（減点=写真不在で「らしさ」-1）
- HTML 構築: stride-v1.html / 採点 **12/12**
- → **写真差込後に最終昇格判定**（運用方針: critique-log 記載）
