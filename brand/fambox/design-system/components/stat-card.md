---
title: FAMBOX Pattern — Stat Card
type: design-system
layer: L3-Patterns
component: StatCard
version: 0.2
status: confirmed
last_updated: 2026-04-28
owner: 宮川
source: Worksheet §23（2026-04-28 確定）+ Card Pattern Flat / Bento Tile Stat-focus からの抽出
brand_alignment:
  - Drive（推進）: 数字 Drive 色固定で達成感を訴求
  - Integrity（誠実）: アニメなし・煽りなし・誠実な数値提示
  - Anti: カウントアップアニメ禁止 / 単位ラベル同サイズ禁止
related:
  - components/card.md
  - components/bento-tile.md
  - tokens/colors.md
extensible: true  # v0.3 以降でカスタム Variant 追加余地あり
---

# Stat Card — Pattern Component

## 概要

数字訴求専用の L3 Pattern。**3 Sizes × 2 Layouts** で構成。
Card Pattern Flat と Bento Tile Stat-focus を統合し、**汎用 Stat 表現**として独立させた基盤。

### 関係整理（v0.2 確定）
```
L3 Stat Card（本 Pattern）= 汎用・独立配置可能
    ↑ 派生
├── Card Pattern Flat: Stat Card を内部に持つ汎用フラット Card
└── Bento Tile Stat-focus: Bento Grid 内での Stat Card 配置
```

汎用配置（Hero 内 / Card 一覧 / Bento 内 / 単独セクション）すべてで使用可能。

## ブランド整合性

- **Drive**: 数字部分は Drive 色固定で「推進・達成」を体現
- **Integrity**: アニメ・煽りを排し、数字そのものの誠実な提示
- **Anti**: カウントアップ等の派手演出 / 単位を Label と同サイズで表示 / 複数数字並列 禁止

---

## Sizes（3 段階・modifier 切替）

| Modifier | 数字 font-size | 用途 |
|---|---|---|
| `stat-card--compact` | `--fs-h2`（32px） | Card 内の補助 Stat / 一覧密度高 |
| `stat-card--default` ★既定 | `--fs-display`（56px） | 標準（Bento Grid 内 / Card 主要 Stat）|
| `stat-card--large` | `--fs-mega`（96px） | Hero 級訴求 / 単独セクションの主役 |

```css
.stat-card--compact .stat-card__value { font-size: var(--fs-h2); }
.stat-card--default .stat-card__value { font-size: var(--fs-display); }
.stat-card--large   .stat-card__value { font-size: var(--fs-mega); }
```

---

## Layouts（2 種・modifier 切替）

| Modifier | 配置 | 用途 |
|---|---|---|
| `stat-card--vertical` ★既定 | 数字 → Unit → Label 縦並び | 標準（多くの場面）|
| `stat-card--horizontal` | 数字 + Unit が左、Label が右 横並び | 一覧密度高・Compact size と相性 |

```
Vertical（既定）          Horizontal
┌──────────────┐         ┌──────────────────────┐
│   -3.2 kg    │         │  -3.2 kg │ 3 ヶ月平均 │
│              │         │          │ 減量      │
│  3 ヶ月平均  │         │          │ 2026 Q1   │
│   減量       │         └──────────────────────┘
│              │
│   2026 Q1    │
└──────────────┘
```

---

## 構造（4 要素）

| 要素 | 必須/任意 | 内容 |
|---|---|---|
| **Value**（数字本体）| **必須** | 主な数値（例: -3.2 / 84% / 2026）|
| **Unit**（単位）| 任意 | kg / % / 件 等。Value の 0.4em で表示（Anti 違反防止）|
| **Label**（補足）| **必須** | Value の意味（例: 「3 ヶ月で平均減量」）|
| **Period**（期間）| 任意 | 集計期間（例: 「2026 Q1」「12 ヶ月継続」）|

---

## カラー仕様（Q2 A 採択 — Drive 固定）

| 要素 | color | 理由 |
|---|---|---|
| Value | `--color-drive` 固定 | 推進感・FAMBOX らしさ・Hero / Bento と整合 |
| Unit | `--color-sub`（控えめ）| Value より弱化（情報階層）|
| Label | `--color-ink` | 本文と同階層 |
| Period | `--color-caption` | 補助情報・最弱 |

将来的に色切替が必要な場合は v0.3 以降で `stat-card--success`（緑）/ `stat-card--warning`（オレンジ別陰影）/ `stat-card--error`（赤）等を拡張。

```css
.stat-card__value  { color: var(--color-drive); }
.stat-card__unit   { color: var(--color-sub); font-size: 0.4em; }
.stat-card__label  { color: var(--color-ink); }
.stat-card__period { color: var(--color-caption); }
```

---

## 共通 Props

| プロパティ | 値 |
|---|---|
| display | `inline-flex`（vertical: column / horizontal: row）|
| gap | `--space-1`（8px）|
| Value font-family | `--font-en`（Poppins）|
| Value font-weight | `--fw-bold`（700）|
| Value line-height | `1` |
| Value letter-spacing | `--ls-en` |
| Unit font-size | `0.4em`（Value に対する相対値）|
| Label font-family | `--font-ja` |
| Label font-size | `--fs-body`（16px）|
| Period font-size | `--fs-caption`（12px）|

---

## Liquid 実装例

### Default size / Vertical（標準）
```liquid
{% raw %}<div class="stat-card stat-card--default stat-card--vertical">
  <p class="stat-card__value">-3.2<span class="stat-card__unit">kg</span></p>
  <p class="stat-card__label">3 ヶ月で平均減量</p>
  <p class="stat-card__period">2026 Q1</p>
</div>{% endraw %}
```

### Large size（Hero 級）
```liquid
{% raw %}<div class="stat-card stat-card--large stat-card--vertical">
  <p class="stat-card__value">84<span class="stat-card__unit">%</span></p>
  <p class="stat-card__label">継続率（12 ヶ月）</p>
</div>{% endraw %}
```

### Compact / Horizontal（一覧）
```liquid
{% raw %}<div class="stat-card stat-card--compact stat-card--horizontal">
  <p class="stat-card__value">12<span class="stat-card__unit">チーム</span></p>
  <div>
    <p class="stat-card__label">導入実績</p>
    <p class="stat-card__period">2026/4 時点</p>
  </div>
</div>{% endraw %}
```

### Bento Tile 内 (`bento-stat-focus` の代替)
```liquid
{% raw %}<div class="bento-tile tile-1x1">
  <div class="stat-card stat-card--default stat-card--vertical">
    <p class="stat-card__value">-3.2<span class="stat-card__unit">kg</span></p>
    <p class="stat-card__label">3 ヶ月で平均減量</p>
  </div>
</div>{% endraw %}
```

### Card Flat 内
```liquid
{% raw %}<article class="card card-flat">
  <div class="stat-card stat-card--large">
    <p class="stat-card__value">84<span class="stat-card__unit">%</span></p>
    <p class="stat-card__label">継続率</p>
  </div>
  <a href="/case-studies" class="btn btn-link">事例を見る →</a>
</article>{% endraw %}
```

---

## CSS（v0.2 実装）

```css
/* === Stat Card 基本 === */
.stat-card {
  display: inline-flex;
  flex-direction: column;
  gap: var(--space-1);
  align-items: flex-start;
}

.stat-card__value {
  font-family: var(--font-en);
  font-weight: var(--fw-bold);
  line-height: 1;
  letter-spacing: var(--ls-en);
  color: var(--color-drive);
  margin: 0;
}

.stat-card__unit {
  font-size: 0.4em;
  color: var(--color-sub);
  margin-left: var(--space-1);
  font-weight: var(--fw-medium);
}

.stat-card__label {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-ink);
  letter-spacing: var(--ls-ja);
  margin: 0;
}

.stat-card__period {
  font-family: var(--font-en);
  font-size: var(--fs-caption);
  color: var(--color-caption);
  letter-spacing: var(--ls-en);
  margin: 0;
}

/* === Sizes === */
.stat-card--compact .stat-card__value { font-size: var(--fs-h2);      /* 32px */ }
.stat-card--default .stat-card__value { font-size: var(--fs-display); /* 56px */ }
.stat-card--large   .stat-card__value { font-size: var(--fs-mega);    /* 96px */ }

/* SP では large を hero 64px に縮退 */
@media (max-width: 767px) {
  .stat-card--large .stat-card__value { font-size: var(--fs-hero); /* 64px */ }
}

/* === Layouts === */
.stat-card--vertical {
  flex-direction: column;
  align-items: flex-start;
}

.stat-card--horizontal {
  flex-direction: row;
  align-items: baseline;
  gap: var(--space-2);
}

.stat-card--horizontal .stat-card__value {
  flex-shrink: 0;
}

.stat-card--horizontal > div {
  display: flex;
  flex-direction: column;
  gap: 0;
}
```

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| 数字読み上げ | SR 用に `<span class="visually-hidden">マイナス</span>` 等の補助テキストを推奨 |
| 単位省略警告 | Unit が記号（%, kg）の場合、SR が読み飛ばさないよう `<abbr title="キログラム">kg</abbr>` 推奨 |
| Color contrast | Drive on White = 4.0:1 / 数字は太字のため AA クリア |
| Animation | カウントアップ等のアニメは禁止（Anti / `prefers-reduced-motion` 対応の必要なし）|

---

## Do / Don't

### ✅ Do
- 数字色は Drive 固定（FAMBOX らしさ・推進感）
- Unit は Value の 0.4em で表示（情報階層）
- Label は必須・Value の意味を必ず明示
- Period は集計期間が明確な場合のみ追加（曖昧な期間は書かない方が誠実）
- Card Pattern Flat / Bento Tile / Hero 内など、**汎用配置で再利用**

### ✕ Don't（Q4 A 禁止リスト準拠）
- ❌ **数字部分にアニメ（カウントアップ等）**禁止 — 派手・煽り・Anti
- ❌ **単位（kg / %）を Label と同じサイズで表示**禁止 — 情報階層崩壊
- ❌ **大型 Stat Card（large）に背景画像**禁止 — Stat Card は数字主役の Pattern
- ❌ **1 つの Stat Card に 2 つ以上の数字を並べない** — 複数 Stat なら Bento Grid Auto-fit + 複数 Stat Card 配置
- ❌ Drive 以外の色（Sky / Deep / Ink 等）を Value にしない（v0.2 では）
- ❌ アイコンを Value 横に並べない（数字単独で勝負）

---

## Brand DNA Anti との照合

本コンポは以下の Anti を踏まない:
- 派手・煽り → アニメ禁止・装飾なし
- エセ高級 → 単純な Drive 色 + 数字のみ
- 過剰演出 → カウントアップ禁止・静的提示

---

## L4 派生関係

| 派生 | 継承する設定 | 追加要素 |
|---|---|---|
| Bento Tile Stat-focus | default size / vertical | Bento Grid 配置・タイル枠 |
| Card Flat 内 Stat | large size / vertical | Card padding + CTA |
| Hero 内 Stat（Image Editorial）| large size / vertical | Hero overlay color（white）|
| Dashboard Stat Grid | compact size / horizontal | KPI ギャラリー（Bento Grid Auto-fit）|

---

## v0.2 でのトリプル運用整理

```
シンプル単独配置 → Stat Card を直接 HTML
Card 一覧の Stat → card-flat 内に Stat Card
Bento Grid 内    → bento-stat-focus（内部は Stat Card と同じ CSS）
```

将来 v0.3 で `bento-stat-focus` を Stat Card の薄い wrapper にリファクタリング予定。

---

## Change Log
- v0.2 (2026-04-28): Worksheet §23 確定（3 Sizes / 2 Layouts / Drive 固定 / 4 禁止項目明示）。Card Flat と Bento Tile Stat-focus を統合し汎用 L3 Pattern として独立化
