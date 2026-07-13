---
title: FAMBOX Pattern — Selection Card
type: design-system
layer: L3-Patterns
component: SelectionCard
version: 0.3
status: confirmed
last_updated: 2026-05-08
owner: 宮川
source: 食事診断 Quiz画面実装からの抽出（Q_GOAL / Q1 / Q5 / Q11 / Q2 等）
brand_alignment:
  - Co-driven: 押しつけでない選択肢提示
  - Drive: 選択時の Drive Orange 強調
  - Integrity: 過剰装飾なし、状態は枠線とグローで表現
related:
  - components/button.md
  - components/form-controls.md
  - tokens/colors.md
---

# Selection Card — Pattern Component

ユーザーが**選択肢から選ぶ UI**を統一するパターン。
Quiz / Form / Onboarding / Settings 全般で再利用可能。

## ブランド整合性
- **Co-driven**: 全選択肢を均等に提示、強制感を排除
- **Drive**: 選択時のみ Drive Orange を使い「決断」を示唆
- **Integrity**: ハートマーク・グラデなどの装飾を排除、状態変化は枠線/グロー/チェックバッジで表現

---

## Variants（3 種）

| Variant | クラス | 用途 |
|---|---|---|
| **Card**（縦型） | `select-card` | 選択肢が4つ程度でアイコン+説明を見せたい時（Q_GOAL, Q1） |
| **List**（横型ラジオ） | `select-list` | 選択肢が5〜10程度でラベル中心の単選択（Q5, Q6） |
| **Grid**（コンパクト） | `select-grid` | 複数選択・最大3〜6個（Q11） |

### Variant 選択フロー
```
選択肢の数は？
├─ 〜4個 + アイコン+説明あり → Card
├─ 5〜10個 + ラベル中心 → List
└─ 複数選択 + コンパクト → Grid
```

---

## States（4 状態）

| State | 仕様 |
|---|---|
| **default** | 1.5px `--border-light` border / `--bg-primary` bg |
| **hover** | border `--color-drive-light` / Card は translateY(-2px) + shadow-2 |
| **selected** ★ | border `--color-drive` / bg `rgba(251,76,21,0.04)` / 4px `--color-drive-glow` outer / 右上に 24×24 Drive 円 + 白チェック |
| **disabled** | opacity 0.5 / pointer-events: none / hover effects 無効 |

### selected 状態の共通仕様
```css
.is-selected {
  border-color: var(--color-drive);
  background: var(--state-selected-bg);
  box-shadow: var(--state-selected-glow);
}
.is-selected::after {
  content: '';
  position: absolute;
  top: 16px;
  right: 16px;
  width: 24px;
  height: 24px;
  background: var(--color-drive);
  border-radius: 50%;
  background-image: url("data:image/svg+xml,...checkmark...");
}
```

---

## Card Variant（縦型）

### 構造
```html
<button class="select-card is-selected" data-value="muscle_gain">
  <span class="select-card__icon"><img src="..." alt=""></span>
  <span class="select-card__body">
    <span class="select-card__label">筋肉量で体重を増やしたい</span>
    <span class="select-card__desc">筋肉量を増やして体重を増やしたい</span>
  </span>
</button>
```

### 仕様
| 項目 | 値 |
|---|---|
| padding | 24px |
| border-radius | `--radius-lg`（12px）|
| icon size | 36×36 |
| label | Hiragino W5 16px |
| desc | Hiragino 13px sub |
| layout | flex column / gap 16px |
| grid | `repeat(2, 1fr)` PC / `1fr` SP |

---

## List Variant（横型ラジオ）

### 構造
```html
<button class="select-list is-selected">
  <span class="select-list__radio"></span>
  <span class="select-list__body">
    <span class="select-list__label">部活・クラブチーム所属で大会出場</span>
    <span class="select-list__sub">競技者</span>
  </span>
</button>
```

### 仕様
| 項目 | 値 |
|---|---|
| padding | 20px 24px |
| border-radius | `--radius-md`（8px）|
| radio size | 22×22 / 4px inner dot when selected |
| label | Hiragino W5 15px |
| sub | Hiragino 12px caption |
| hover | translateX(+4px) |

---

## Grid Variant（コンパクト・複数選択）

### 構造
```html
<div class="select-grid-info">
  <span class="select-grid-info__count"><strong>2</strong> 件選択中</span>
  <span class="select-grid-info__max">最大3つ</span>
</div>
<div class="select-grid">
  <button class="select-grid-item is-selected">
    <span class="select-grid-item__check"></span>
    <span class="select-grid-item__icon"><img src="..."></span>
    <span class="select-grid-item__label">疲れが取れにくい・回復が遅い</span>
  </button>
  ...
</div>
```

### 仕様
| 項目 | 値 |
|---|---|
| padding | 16px 20px |
| border-radius | `--radius-md` |
| checkbox | 22×22 / Drive 塗りつぶし + 白✓ when selected |
| icon size | 20×20 |
| label | Hiragino W5 14px |
| grid | `repeat(2, 1fr)` PC / `1fr` SP |

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| 操作 | `<button>` で実装。Enter / Space で選択 |
| Touch Target | 全 Variant で min 44px |
| Focus | `:focus-visible` で Drive 2px outline |
| ARIA | 単選択は `role="radio"` + `aria-checked`、複数選択は `role="checkbox"` |
| グループ | `role="radiogroup"` / `role="group"` で囲む |

---

## Do / Don't

### ✅ Do
- 1画面1選択 = 単選択 / 複数選択を明確に区別
- selected 時の表現は border + bg + glow + ✓バッジ の4点セット
- アイコンは 36 / 20 / 48 のサイズスケールで統一

### ✕ Don't
- selected を文字色だけで表現しない（コントラスト不足）
- カード内に選択肢以外の情報を混ぜない
- グラデーション・派手シャドウを使わない（Brand Anti）

---

## Change Log

- v0.3 (2026-05-08): Quiz画面実装から抽出して新規策定（Card / List / Grid 3 Variant）
