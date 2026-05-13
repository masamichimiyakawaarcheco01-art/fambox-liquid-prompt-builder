---
title: FAMBOX Pattern — Bento Tile
type: design-system
layer: L3-Patterns
component: BentoTile
version: 0.2
status: confirmed
last_updated: 2026-04-28
owner: 宮川
deadline: 2026-05-29（OKR Task 2-1-a TOPページ DNA 反映 / Bento Grid と一体）
source: Worksheet §20（2026-04-28 確定）+ Brand DNA v0.5 C-Bento タイル仕様継承
brand_alignment:
  - Editorial × Lab（DNA メタファー）: Bento Grid + 部分ガラス
  - Aesthetic 軸 主構図: 左下→右上の対角線（強弱でコントラスト）
  - Anti: 同サイズ並列単調禁止 / Drive 全タイル背景化禁止
related:
  - components/card.md
  - components/bento-grid.md
  - tokens/colors.md
  - tokens/spacing.md
extensible: true  # v0.3 以降でカスタム Variant 追加余地あり
---

# Bento Tile — Pattern Component

## 概要

FAMBOX TOPページの主役 Pattern。**4 Variants × 5 Sizes**（DNA v0.5 確定）で構成。
Card Pattern を継承しつつ、Bento Grid 内での「強弱 × Editorial」表現を担う。

L4 Bento Grid と一体運用（**bento-grid.md** 参照）。

## ブランド整合性

- **Editorial × Lab**: 写真 / Stat / タイポを Bento 内で重ねて Editorial 表現
- **強弱の DNA**: 主役タイル（2×2 以上）と脇役タイル（1×1 等）の対比でリズム
- **対角線構図**: 左下→右上の主構図（タイル配置で実現）
- **Anti 回避**: 同サイズ単調並列 / Drive 全タイル背景 / タイル間隔 16px 未満 / Glass + Hero級画像 mix-blend を image-fill 専用 など禁止

---

## Variants（4 種 / 拡張可）

| Variant | クラス | 構造 | 使用例 |
|---|---|---|---|
| **Standard** | `bento-tile bento-standard` | Card Standard 継承（タイトル + 本文 + 任意 CTA） | 一般タイル / Quote / 小情報 |
| **Glass** | `bento-tile bento-glass` | 部分ガラス効果（背景画像 + Glass 1-5 opacity オーバーレイ） | ヒーロー級・Editorial 表現 |
| **Image-fill** | `bento-tile bento-image-fill` | 画像が全面を埋める + テキスト下部オーバーレイ | 写真主役（Case / Product 訴求）|
| **Stat-focus** | `bento-tile bento-stat-focus` | 大型数字（`--fs-display` 56px）+ ラベル | KPI 訴求 / Case Study 数値 |

### 拡張ルール（v0.3 以降）

新しい Bento Tile Variant が必要な場合は以下を満たす:
1. **Sizes 厳守**: DNA 5 sizes（1×1 / 2×1 / 1×2 / 2×2 / 3×2）のいずれかに対応
2. **強弱規律**: タイルが Bento Grid 内で「主役 / 脇役」階層に配置できる
3. **Glass 規律**: Glass 効果は **Glass Variant 専用**（他 Variants に適用しない）
4. **DNA Anti を踏まない**: Drive 色全タイル背景 / 同サイズ単調並列 / タイル間隔 16px 未満 禁止
5. **命名**: `bento-tile bento-{variant-name}`（kebab-case）

---

## Sizes（5 種・DNA v0.5 既定）

| Size | クラス | grid-column × grid-row | aspect-ratio | 想定用途 |
|---|---|---|---|---|
| **1×1** | `tile-1x1` | 1 × 1 | 1:1 | 小タイル / Icon / Quote |
| **2×1** | `tile-2x1` | 2 × 1 | 2:1 | 横長タイル / Stat 横並び |
| **1×2** | `tile-1x2` | 1 × 2 | 1:2 | 縦長タイル / 動画 |
| **2×2** | `tile-2x2` | 2 × 2 | 1:1 (large) | **主役タイル**（Bento 1 グリッドに最低 1 個推奨）|
| **3×2** | `tile-3x2` | 3 × 2 | 3:2 | メガタイル / Hero 内 / Editorial 級 |

### 強弱の規律（Anti 回避）

```
✅ Do  : 主役 2×2 + 脇役 1×1 × 2 + 横長 2×1 で対角線リズム
❌ Don't: 1×1 を 6 個並列（単調・DNA Anti）
❌ Don't: 全部 2×2 で並列（強弱なし・DNA Anti）
```

---

## Glass 効果（Glass Variant 専用 / Q3 A 採択）

DNA v0.5 の Glass 5 階調から選択。`bento-glass` Variant にのみ適用。

| Modifier | opacity | 用途 |
|---|---|---|
| `bento-glass--1` | 0.05 | 超薄オーバーレイ（写真ほぼ素のまま）|
| `bento-glass--2` | 0.1 | ガラスタイル薄（背景の質感を残す）|
| `bento-glass--3` ★既定 | 0.3 | ガラス中（テキスト可読性とのバランス）|
| `bento-glass--4` | 0.6 | モーダル暗化レベル（読みやすさ優先）|
| `bento-glass--5` | 0.8 | 強オーバーレイ（背景はほぼ消える）|

```css
.bento-glass {
  position: relative;
  background-size: cover;
  background-position: center;
  isolation: isolate;
}

.bento-glass::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, var(--glass-opacity, 0.3));
  z-index: var(--layer-base);
}

.bento-glass--1 { --glass-opacity: 0.05; }
.bento-glass--2 { --glass-opacity: 0.1; }
.bento-glass--3 { --glass-opacity: 0.3; }
.bento-glass--4 { --glass-opacity: 0.6; }
.bento-glass--5 { --glass-opacity: 0.8; }

.bento-glass > * {
  position: relative;
  z-index: var(--layer-1);
  color: var(--color-white);
}
```

---

## Stat-focus の数字仕様（Q4 B 採択）

| 項目 | 値 |
|---|---|
| 数字 font-size | `--fs-display`（**56px**）固定 |
| 数字 font-family | `--font-en` Poppins |
| 数字 font-weight | `--fw-bold`（700） |
| 数字 color | `--color-drive`（既定）/ `--color-ink`（落ち着き）|
| ラベル font-size | `--fs-body`（16px） |
| ラベル color | `--color-sub` |

**理由**: `--fs-mega`（96px）は Hero 専用、Bento グリッド内では情報密度を保つため `--fs-display`（56px）を採用。Bento Grid のリズムを壊さず、Hero との階層が成立。

```css
.bento-stat-focus__value {
  font-family: var(--font-en);
  font-size: var(--fs-display);  /* 56px */
  font-weight: var(--fw-bold);
  line-height: 1;
  letter-spacing: var(--ls-en);
  color: var(--color-drive);
}

.bento-stat-focus__unit {
  font-size: 0.4em;  /* 約 22px */
  color: var(--color-sub);
}

.bento-stat-focus__label {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-sub);
  letter-spacing: var(--ls-ja);
  margin-top: var(--space-1);
}
```

---

## 共通 Props（全 Variants）

| プロパティ | 値 |
|---|---|
| background | Standard: `--bg-primary` / Glass: 画像 + opacity overlay / Image-fill: 画像 cover / Stat-focus: `--bg-primary` |
| border | `1px solid --border-light` 既定（Glass / Image-fill は枠なし） |
| border-radius | `--radius-md`（8px）固定 — Pill / 矩形禁止 |
| padding | Standard / Stat-focus: `--space-3`（24px）/ Glass / Image-fill: `--space-3`（テキスト周辺）|
| shadow | `--shadow-1` 既定 / hover で `--shadow-3` |
| transition | `box-shadow / transform var(--duration-base) var(--ease-out)` |

---

## Liquid 実装例

### Standard（1×1 小タイル）
```liquid
{% raw %}<article class="bento-tile bento-standard tile-1x1">
  <h3 class="bento-tile__title">{{ tile.title }}</h3>
  <p class="bento-tile__text">{{ tile.body }}</p>
</article>{% endraw %}
```

### Glass（2×2 主役・写真背景）
```liquid
{% raw %}<article class="bento-tile bento-glass bento-glass--3 tile-2x2"
         style="background-image: url('{{ tile.image | img_url: '1200x' }}');">
  <p class="bento-tile__eyebrow">CASE</p>
  <h3 class="bento-tile__title">{{ tile.title }}</h3>
  <p class="bento-tile__text">{{ tile.summary }}</p>
  <a href="{{ tile.url }}" class="btn btn-link">詳細を見る →</a>
</article>{% endraw %}
```

### Image-fill（3×2 メガ・写真主役）
```liquid
{% raw %}<a href="{{ tile.url }}" class="bento-tile bento-image-fill tile-3x2">
  <img src="{{ tile.image | img_url: '1800x' }}" alt="{{ tile.alt }}"
       class="bento-tile__media" loading="lazy">
  <div class="bento-tile__overlay">
    <h3 class="bento-tile__title">{{ tile.title }}</h3>
    <p class="bento-tile__text">{{ tile.body }}</p>
  </div>
</a>{% endraw %}
```

### Stat-focus（1×1 KPI）
```liquid
{% raw %}<div class="bento-tile bento-stat-focus tile-1x1">
  <p class="bento-stat-focus__value">
    -3.2<span class="bento-stat-focus__unit">kg</span>
  </p>
  <p class="bento-stat-focus__label">3 ヶ月で平均減量</p>
</div>{% endraw %}
```

---

## CSS（v0.2 実装）

```css
/* === Bento Tile 基本 === */
.bento-tile {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  background: var(--bg-primary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--space-3);
  box-shadow: var(--shadow-1);
  overflow: hidden;
  transition: box-shadow var(--duration-base) var(--ease-out),
              transform var(--duration-base) var(--ease-out);
  text-decoration: none;
  color: inherit;
}

.bento-tile:hover {
  box-shadow: var(--shadow-3);
  transform: translateY(-2px);
}

.bento-tile:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}

/* === Sizes（grid-column / row）=== */
.tile-1x1 { grid-column: span 1; grid-row: span 1; }
.tile-2x1 { grid-column: span 2; grid-row: span 1; }
.tile-1x2 { grid-column: span 1; grid-row: span 2; }
.tile-2x2 { grid-column: span 2; grid-row: span 2; }
.tile-3x2 { grid-column: span 3; grid-row: span 2; }

/* SP（< 768px）では強制縮退 */
@media (max-width: 767px) {
  .tile-2x1, .tile-2x2, .tile-3x2 { grid-column: span 1; }
  .tile-1x2, .tile-2x2 { grid-row: span 1; }
}

/* === 内部要素 === */
.bento-tile__title {
  font-family: var(--font-ja);
  font-size: var(--fs-h3);
  font-weight: var(--fw-bold);
  color: var(--color-ink);
  letter-spacing: var(--ls-ja);
  line-height: var(--lh-heading);
}

.bento-tile__text {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-sub);
  line-height: var(--lh-body);
  letter-spacing: var(--ls-ja);
}

.bento-tile__eyebrow {
  font-family: var(--font-en);
  font-size: var(--fs-caption);
  font-weight: var(--fw-semibold);
  color: var(--color-drive);
  letter-spacing: var(--ls-en);
  text-transform: uppercase;
}

/* === Variant: Glass === */
.bento-glass {
  position: relative;
  background-size: cover;
  background-position: center;
  border: none;
  isolation: isolate;
}

.bento-glass::before {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, var(--glass-opacity, 0.3));
  z-index: var(--layer-base);
}

.bento-glass > * {
  position: relative;
  z-index: var(--layer-1);
  color: var(--color-white);
}

.bento-glass .bento-tile__title,
.bento-glass .bento-tile__text {
  color: var(--color-white);
}

.bento-glass--1 { --glass-opacity: 0.05; }
.bento-glass--2 { --glass-opacity: 0.1; }
.bento-glass--3 { --glass-opacity: 0.3; }
.bento-glass--4 { --glass-opacity: 0.6; }
.bento-glass--5 { --glass-opacity: 0.8; }

/* === Variant: Image-fill === */
.bento-image-fill {
  position: relative;
  padding: 0;
  border: none;
}

.bento-image-fill .bento-tile__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: var(--layer-base);
}

.bento-image-fill .bento-tile__overlay {
  position: relative;
  margin-top: auto;
  padding: var(--space-3);
  background: linear-gradient(
    180deg,
    transparent 0%,
    rgba(0, 0, 0, 0.7) 100%
  );
  z-index: var(--layer-1);
}

.bento-image-fill .bento-tile__title,
.bento-image-fill .bento-tile__text {
  color: var(--color-white);
}

/* === Variant: Stat-focus === */
.bento-stat-focus {
  align-items: flex-start;
  justify-content: center;
}

.bento-stat-focus__value {
  font-family: var(--font-en);
  font-size: var(--fs-display);  /* 56px */
  font-weight: var(--fw-bold);
  line-height: 1;
  letter-spacing: var(--ls-en);
  color: var(--color-drive);
}

.bento-stat-focus__unit {
  font-size: 0.4em;
  color: var(--color-sub);
  margin-left: var(--space-1);
}

.bento-stat-focus__label {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-sub);
  letter-spacing: var(--ls-ja);
  margin-top: var(--space-1);
}
```

---

## Accessibility

- **タイル全体がリンク**: `<a class="bento-tile">` で囲む（リンクネスト禁止）
- **複数アクション**: `<article>` + 内部 `<a>`/`<button>`
- **画像 alt**: Image-fill / Glass 背景の意味ある画像には alt 必須
- **見出し階層**: `bento-tile__title` は文脈に応じて h2/h3/h4 を選ぶ
- **対比**: Glass 3 (0.3) 以下では背景画像との contrast を撮影／素材選定で担保
- **focus-visible**: キーボード操作時の outline 必須

---

## Do / Don't

### ✅ Do
- 1 つの Bento Grid 内で **強弱を必ずつける**（主役 2×2 + 脇役 1×1）
- 主構図は **左下→右上の対角線**（DNA Aesthetic 軸）
- Glass effect は Glass Variant 専用（他に適用しない）
- 数字訴求は Stat-focus Variant で `--fs-display` 56px 固定
- 画像主役は Image-fill Variant でテキストを下部オーバーレイ

### ✕ Don't（Q6 A 禁止リスト準拠）
- ❌ **同じサイズタイルを単調並列**（強弱なし・DNA Anti）
- ❌ **Drive 色を全タイル背景に使う**（うるさい・面で使うのは Anti）
- ❌ **Glass + Hero級画像 mix-blend を Glass Variant 以外で使う**（image-fill 専用）
- ❌ **タイル間隔を 16px 未満にしない**（密度過剰・読みづらさ）
- ❌ Pill radius を Bento Tile に使わない（Card と同じく `--radius-md` 固定）
- ❌ shadow-4/5 を使わない（Anti）

---

## L4 Bento Grid との関係

Bento Tile は **Bento Grid 内に配置される**。Grid 側は:
- 12 column system / gutter 24px / 8px baseline
- タイル間隔: SP 16px / Tablet 24px / PC 32px
- 主役タイル（2×2 以上）を最低 1 個含む

詳細は [bento-grid.md](bento-grid.md) を参照。

---

## L4 派生関係

| 派生 | 継承する Variant | 追加要素 |
|---|---|---|
| Hero 内 Bento ブロック | tile-3x2 + Glass | Hero overlay と整合 |
| Product Highlight Tile | tile-2x1 + Image-fill | 商品名 / 価格 |
| Article Featured Tile | tile-2x2 + Glass | カテゴリラベル / 公開日 |

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `4. Patterns FormField / Card / Tooltip / Alert`
- **Component Set ID**: `87:26`（2026-05-12 生成 + Session #10 で 20 variants 完備 + Session #13 で featured property 拡張）
- 生成スキル: `figma-component-from-spec` v0.3
- **実装済 variants**: **40**（`variant` × `size` × `featured`）
  - variant: standard / glass / image-fill / stat-focus（4）
  - size: 1×1 / 2×1 / 1×2 / 2×2 / 3×2（5）
  - **featured: false / true（2）**★ Session #13 で追加（Issue 8 解消）
- **配置**: 2 ブロック × 4 列 × 5 行（左 featured=false / 右 featured=true）/ Set 全体 4900 × 2000
- **featured 仕様**:
  - `featured=false` (既定): 既存 stroke 維持（standard / stat-focus は border-light 1px、glass / image-fill は枠なし）
  - `featured=true`: 全 variant に **Drive `#FB4C15` 2px stroke** を適用（individual stroke weights を 2/2/2/2 で均一化）
  - 用途: Bento Grid editorial パターンでの主役識別、Subscription Plan の推奨プラン等
- **size 別寸法**:
  - 1×1: 160 × 160（小タイル、Quote / Icon / 単一 KPI）
  - 2×1: 360 × 160（横長、Stat 横並び / 横長告知）
  - 1×2: 160 × 360（縦長、動画 / 連続情報）
  - 2×2: 360 × 360（**主役タイル**、Bento 1 グリッドに最低 1 個推奨）
  - 3×2: 560 × 360（メガタイル、Hero 内 / Editorial 級）
- **Variable バインド**:
  - fills: `bg/primary`（standard, stat-focus）/ 直値 dark base（glass, image-fill）
  - strokes: `border/light` 1px（standard, stat-focus）/ なし（glass, image-fill）
  - effects: `FAMBOX/shadow/1`（standard, stat-focus）/ なし（glass, image-fill）
- **各 variant の構造（全 size 共通）**:
  - standard: Eyebrow（Drive `CASE`）+ Title（Bold 24）+ Body（Regular 16）
  - glass: dark base + Glass overlay rect (opacity 0.3) + 下寄せ白文字
  - image-fill: 画像 placeholder + bottom gradient overlay + 下寄せ白文字
  - stat-focus: 大型数字 `-3.2 kg`（56px Drive Bold、`kg` 部分 22px sub）+ ラベル
- **未実装（v0.4 で追加予定）**:
  - **size 別のコンテンツ最適化**: 1×1 でテキスト切れの問題、各 size 専用のコンテンツ密度調整
  - state property: hover（shadow-3 + translateY -2px）/ focus-visible / disabled
  - Glass の 5 階調 modifier（glass--1 〜 glass--5）
  - 画像 placeholder の Image Fill バインド
  - **Bento Grid editorial の主役 instances を `featured=true` に切替**（Issue 8 解消の Phase 3 実装、次セッション）

## Change Log
- v0.3-figma+featured (2026-05-12): Session #13 で **featured boolean variant property を追加**（20 → 40 variants）。featured=true で Drive 2px stroke 適用、Bento Grid editorial の主役識別を Tile 側で表現可能に（Issue 8 解消の準備）。SKILL v0.3 Phase 2 の実証実験 1 回目
- v0.3-figma (2026-05-12): Session #10 で 残 4 sizes を追加し **20 variants 完備**（4 variant × 5 size）。size property が認識され、Bento 5 sizes 体系が Figma 上で完全に表現可能に
- v0.2-figma (2026-05-12): Figma Component Set `87:26` 新規生成（4 variants × default size 2×2 のみ）。残 4 sizes と state は v0.3 で順次追加
- v0.2 (2026-04-28): Worksheet §20 確定（4 Variants / DNA 5 sizes 厳守 / Glass Variant 専用 / Stat-focus は --fs-display 56px / Glass 5 階調 / 4 禁止項目明示）。Brand DNA v0.5 C-Bento タイル仕様を体系化
