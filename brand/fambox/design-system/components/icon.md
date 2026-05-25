---
title: FAMBOX System — Icon
type: design-system
layer: L1-Tokens-Iconography
component: Icon
version: 0.3
status: confirmed
last_updated: 2026-05-08
owner: 宮川
source: Intro/Quiz/Loading 画面実装からの統一規約
brand_alignment:
  - Integrity: 統一規格・命名で一貫性を保証
  - Co-driven: 全UIパーツで同じアイコンが再利用可能
related:
  - tokens/colors.md
  - components/selection-card.md
---

# Icon System

FAMBOX 全画面で**アイコンを差替え可能・命名規則統一**で運用する規約。

---

## サイズスケール（5段階）

| Size | px | 用途 |
|---|---|---|
| `icon-xs` | 16 | インライン補助・ボタン内アイコン |
| `icon-sm` | 20 | コンパクトUI（Grid Multi 等）/ 状態インジケータ |
| `icon-md` | 24 | 標準（Trust list / インライン強調）|
| `icon-lg` | 36 | Card内アイコン（Selection Card 等）|
| `icon-xl` | 48 | 強調表示（Gender select / Feature 等）|
| `icon-2xl` | 64 | Hero級訴求（拡張余地）|

### CSS Variable
```css
:root {
  --icon-xs: 16px;
  --icon-sm: 20px;
  --icon-md: 24px;
  --icon-lg: 36px;
  --icon-xl: 48px;
  --icon-2xl: 64px;
}
```

---

## 命名規約

### パス
```
assets/icons/{category}-{value}.svg
```

### Category（カテゴリ）

| Category | 用途 | 例 |
|---|---|---|
| `goal-` | 診断目標 | `goal-muscle-gain.svg` |
| `symptom-` | 症状 | `symptom-fatigue.svg` |
| `gender-` | 性別 | `gender-male.svg` |
| `trust-` | Trust list | `trust-savas.svg` |
| `nav-` | ナビゲーション | `nav-back.svg` `nav-forward.svg` `nav-close.svg` |
| `action-` | アクション | `action-share.svg` `action-download.svg` `action-retry.svg` |
| `state-` | 状態 | `state-check.svg` `state-error.svg` |
| `plan-` | プラン | `plan-athlete-plus-60.jpg`（画像別途） |

### Value（個別名）
- 英小文字 + ハイフン区切り
- データ値（diagnosis.js の value）と一致させる
- 例: `goal-muscle-gain` （Q_GOAL の value: `muscle_gain` を ハイフン化）

---

## SVG 仕様

### 推奨設定
| 項目 | 値 |
|---|---|
| **viewBox** | `0 0 24 24` 統一 |
| **stroke** | `currentColor` |
| **fill** | `none` または `currentColor` |
| **stroke-width** | 1.5 〜 2px |
| **stroke-linecap** | `round` |
| **stroke-linejoin** | `round` |
| **width / height 属性** | **書き出し時に削除**（CSS で 100% 制御）|

### currentColor の使い方
SVG 内で `stroke="currentColor"` または `fill="currentColor"` を使うと、
**CSS の `color` プロパティでアイコン色を制御**できる:

```css
.select-card.is-selected .select-card__icon { color: var(--color-drive); }
.select-card .select-card__icon { color: var(--color-ink); }
```

これにより、状態に応じてアイコンの色が自動連動する。

---

## 差替えパターン（emoji フォールバック）

実画像未配置時に emoji を表示するパターン:

### 構造
```html
<span class="*__icon">
  <img src="assets/icons/{category}-{value}.svg" alt=""
       width="36" height="36"
       onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
  <span class="icon-fallback">😀</span>
</span>
```

### コンテナ CSS
```css
/* 親要素は flex container として使う */
.*__icon {
  width: var(--icon-lg);    /* サイズ別 */
  height: var(--icon-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.*__icon img,
.*__icon svg {
  width: 100%;
  height: 100%;
  object-fit: contain;
  display: block;
}
.icon-fallback {
  display: none;
  font-size: var(--icon-lg);
  line-height: 1;
}
```

---

## 適用ガイドライン

### Selection Card
| Variant | アイコンサイズ |
|---|---|
| `select-card` | `--icon-lg`（36px） |
| `select-list` | （アイコンなし or `--icon-md`） |
| `select-grid` | `--icon-sm`（20px） |

### Trust list
- `--icon-md`（24px）
- 左寄せ・テキストの縦中央揃え

### Gender select
- `--icon-xl`（48px）
- 中央配置・テキスト上部

### Loading Step Indicator
- `--icon-sm`（20px）の円
- 内部スピナー / チェックマーク

---

## アクセシビリティ

| 項目 | 仕様 |
|---|---|
| 装飾的アイコン | `alt=""` + `aria-hidden="true"` |
| 意味のあるアイコン | `alt="代替テキスト"` 必須 |
| インタラクティブ | `aria-label` を親要素に |
| カラーコントラスト | アイコンのみで状態を表現しない（必ずテキストと併用）|

---

## Do / Don't

### ✅ Do
- SVG は `currentColor` で書き出し → CSS で色制御
- カテゴリプレフィックスで命名（goal- / symptom- / nav-）
- 差替えパターン（img + onerror fallback）で堅牢化
- viewBox `0 0 24 24` を統一

### ✕ Don't
- 16px と 20px 等を「ほぼ同じ」と妥協しない（スケールに従う）
- 同じ意味のアイコンを複数バージョン作らない
- アイコンの色を SVG ファイル内に直書きしない（CSS で制御）

---

## Change Log

- v0.3 (2026-05-08): Intro/Quiz/Loading 画面実装から抽出して新規策定
