---
title: FAMBOX Pattern — Section Header
type: design-system
layer: L3-Patterns
component: SectionHeader
version: 0.3
status: confirmed
last_updated: 2026-05-08
owner: 宮川
source: 食事診断 Result/Intro 画面実装からの抽出（2026-05-08）
brand_alignment:
  - Editorial × Lab: 英字Eyebrow + 日本語タイトルの2行階層
  - Integrity: 装飾なし、サイズと余白で階層を作る
  - Drive: タイプ色がEyebrowの一部に乗ることがある（Result画面等）
related:
  - tokens/typography.md
  - tokens/spacing.md
---

# Section Header — Pattern Component

## 概要

セクション冒頭の **Eyebrow英字 + 日本語タイトル** の2行構成。FAMBOX全画面で統一使用する基本パターン。

```
DAILY MEAL MODEL              ← Eyebrow（Poppins 14 Medium）
                              ← 16px 余白
あなたにおすすめの1日の食事モデル ← Section Title（Hiragino W5 32px）
```

---

## ブランド整合性

- **Editorial**: 英字を上、日本語を下に置く読み物ヘッダー構成
- **Lab**: Eyebrow英字でカテゴリ性・科学性を示唆
- **Drive 連動**: 文脈によりEyebrowをタイプ色に変更可

---

## Variants（3 サイズ）

| Variant | Eyebrow | Title | 用途 |
|---|---|---|---|
| **Hero** ★最大訴求 | Poppins 14M | Hiragino W5 48px | LP Hero級 |
| **Standard** ★既定 | Poppins 14M | Hiragino W5 32px | 通常セクション |
| **Compact** | Poppins 12M | Hiragino W5 24px | カード内見出し・密なUI |

---

## 構造（HTML）

```html
<header class="section-header section-header--standard">
  <span class="section-header__eyebrow">DAILY MEAL MODEL</span>
  <h2 class="section-header__title">あなたにおすすめの1日の食事モデル</h2>
</header>
```

---

## CSS

```css
.section-header__eyebrow {
  display: block;
  font-family: var(--font-en);
  font-size: 14px;
  font-weight: var(--fw-medium);
  letter-spacing: 0.04em;
  color: var(--color-ink);
  margin-bottom: 16px;
}

.section-header__title {
  font-family: var(--font-ja);
  font-size: 32px;          /* Standard 既定 */
  font-weight: var(--fw-medium);  /* W5 */
  line-height: 1.5;
  letter-spacing: var(--ls-ja);
  color: var(--color-ink);
  margin: 0 0 48px;
}

/* Hero */
.section-header--hero .section-header__title { font-size: 48px; }

/* Compact */
.section-header--compact .section-header__eyebrow { font-size: 12px; }
.section-header--compact .section-header__title { font-size: 24px; margin-bottom: 32px; }

/* Eyebrow をタイプ色に切替（Result画面等） */
.section-header--type-accent .section-header__eyebrow {
  color: var(--type-current, var(--color-drive));
}

/* SP 調整 */
@media (max-width: 767px) {
  .section-header__title { font-size: 26px; }
  .section-header--hero .section-header__title { font-size: 36px; }
}
```

---

## Do / Don't

### ✅ Do
- Eyebrow は必ず英字、Titleは必ず日本語（Editorial × Lab 構成の維持）
- Eyebrow→Title間の余白は **16px** 厳守
- Title→次コンテンツ間の余白は Standard で **48px**
- Eyebrow は短く（最大3単語）、Titleは1行に収まる長さ

### ✕ Don't
- Eyebrow を Title より下に置かない
- Eyebrow を Bold にしない（Medium で抑制）
- Title を Bold(700) にしない（W5 で軽やかさを維持）
- Eyebrow と Title 間に装飾線・アイコンを入れない（Integrity違反）

---

## 適用例（実装済）

| 画面 | セクション | Variant |
|---|---|---|
| Result | あなたに推奨されるPFCバランス | Standard |
| Result | あなたの食事改善 3つのポイント | Standard |
| Result | あなたにおすすめの1日の食事モデル | Standard |
| Result | あなたにおすすめのFAM BOXプラン | Standard |
| Intro | 診断でわかる3つのこと | Standard |

---

## Change Log

- v0.3 (2026-05-08): 食事診断 Result 画面実装から抽出して新規策定（Hero / Standard / Compact 3 Variant）
