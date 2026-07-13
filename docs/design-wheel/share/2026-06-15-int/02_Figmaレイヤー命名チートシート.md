# Figma レイヤー命名チートシート（1枚版）

> 「Group 1216122894」「IMG_8563」「Mask group」のままだと、**人も AI も後から触れません**。
> 名前を整えるだけで、レイヤーが「読める・直せる・使い回せる資産」になります。
> （フル版ルール：`docs/design-wheel/LAYER-NAMING.md`）

---

## 基本形

```
役割 / 用途 / バリエーション
```
英語小文字・`/` 区切り。例：`section/hero` ／ `card/stat-members` ／ `text/display`

---

## 役割プレフィックス（これだけ覚えればOK）

| 役割 | 何に使う | 例 |
|---|---|---|
| `page/` | 一番外のフレーム | `page/corporate-flowops` |
| `section/` | 大きな区画 | `section/hero` `section/features` |
| `group/` | 行・列のまとまり | `group/stats-row` |
| `card/` | カード1枚 | `card/feature-01` |
| `text/` | 文字 | `text/display` `text/body` |
| `button/` | ボタン | `button/pill-primary` |
| `image/` | 画像・写真枠 | `image/photo-athlete` |
| `shape/` | 装飾図形（帯・線・下地） | `shape/band-accent` |
| `icon/` | アイコン | `icon/arrow-ne` |

---

## Before → After

```
❌ Before（触れない）        ✅ After（資産になる）
Frame 123                    page/sporty-stride
├ Group 1216122894          ├ section/hero
│ ├ Rectangle 12            │ ├ image/placeholder-runner
│ ├ Mask group             │ ├ shape/band-accent
│ └ IMG_8563               │ └ text/display
└ Ellipse 1048              └ section/content
                              └ group/stats-row → card/stat-members
```

---

## やってはいけない 3つ

1. **デフォルト名のまま放置**（`Frame 123` `Ellipse 1048` `Group 1216…`）
2. **取り込みファイル名のまま**（`IMG_8563` `AdobeStock_…` `スクショ…`）→ `image/photo-内容` に改名
3. **`Mask group` のまま** → `image/masked-用途` に改名

---

## おまけ：なぜ効くか

レイヤー名を **HTML のクラス名と1対1**で揃えると（`section/hero` ⇔ `<section class="hero">`）、
**Figma ⇄ HTML を機械的に変換**できます。AI に作らせた後の編集・流用がぐっと楽になります。
命名のコストは実質ゼロ（作る時に名前を付けるだけ）です。
