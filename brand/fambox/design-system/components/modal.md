---
title: FAMBOX Component — Modal
type: design-system
layer: L4-Components
component: Modal
version: 0.2
status: confirmed
last_updated: 2026-04-28
owner: 宮川
source: Worksheet §22（2026-04-28 確定）+ 既存実装サンプル（Shopify product-media-modal / collage video modal / product-popup-modal）
brand_alignment:
  - Integrity（誠実）: Confirmation で煽り英語ボタン禁止・日本語の「OK」「キャンセル」のみ
  - Co-driven（対等）: 「お客様」表現を排し、対等トーンで確認
  - Anti: ネスト禁止 / Detail 90% 超禁止 / Sheet を PC で使わない
related:
  - components/button.md
  - tokens/colors.md
  - tokens/motion.md
extensible: true  # v0.3 以降でカスタム Variant 追加余地あり
---

# Modal — Component

## 概要

確認・詳細・Bottom Sheet の3形態を扱う Component。**3 Variants** で構成。
DNA Anti（煽り・派手）を踏まないシンプルな確認 UI。

## ブランド整合性

- **Integrity**: 「キャンセル」「OK」「送信する」等の日本語動詞ベース
- **Co-driven**: 「お客様」表現排除・対等トーンで意図確認
- **Anti**: Modal 内 Modal（ネスト）/ 過剰 sized Detail / PC での Sheet 使用 禁止

---

## Variants（3 種 / 拡張可）

| Variant | クラス | 構造 | 使用例 |
|---|---|---|---|
| **Confirmation** | `modal modal-confirmation` | Title + Body + Cancel/OK 2 ボタン | 削除確認 / Plan 変更 / Contact Form 送信前 |
| **Detail** | `modal modal-detail` | Header + Body（スクロール可）+ Close × | 商品詳細 / Case Study 詳細 / Plan 比較 |
| **Sheet** | `modal modal-sheet` | 下から slide-in（SP 専用）| SP の Variant 選択 / フィルタ / アクションシート |

### 拡張ルール（v0.3 以降）

新しい Modal Variant が必要な場合は以下を満たす:
1. **Backdrop**: opacity 0.6（Glass 4）固定 / 動画 backdrop 等の派手化禁止
2. **Close 3 方法**: × ボタン + ESC + Backdrop クリック を全 Variants で実装
3. **DNA Anti**: ネスト / 90% 超 / PC での Sheet 使用 禁止
4. **z-index**: `--layer-5`（tokens.css の Modal / Overlay 階層）
5. **命名**: `modal modal-{variant-name}`（kebab-case）

---

## サイズ仕様

| Variant | 最大幅 | 最大高さ | 配置 |
|---|---|---|---|
| Confirmation | 400px | auto（content-driven）| 画面中央 |
| Detail | 800px | **画面高 90% 上限**（90% 超は Anti 違反） | 画面中央 |
| Sheet | 100% | auto / max 80%（SP のみ） | 画面下端から slide-in |

```css
.modal-confirmation { max-width: 400px; }
.modal-detail       { max-width: 800px; max-height: 90vh; }
.modal-sheet        { max-width: 100%; max-height: 80vh; bottom: 0; }
```

---

## Backdrop（Q2 A 採択 — Glass 4 固定）

DNA v0.5 Glass 4（opacity 0.6）固定。背景を確実に暗化し Modal 本体に集中させる。

```css
.modal__backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);  /* Glass 4 */
  z-index: var(--layer-5);
  opacity: 0;
  transition: opacity var(--duration-base) var(--ease-out);
}

.modal.is-open .modal__backdrop {
  opacity: 1;
}
```

---

## Close 動作（Q3 A 採択 — 3 方法すべて）

全 Variants で以下 3 方法すべてを実装:

| 方法 | 実装 |
|---|---|
| **× ボタン**（右上 / Confirmation は省略可）| `<button class="modal__close" aria-label="閉じる">` |
| **ESC キー** | `keydown` イベントで `event.key === 'Escape'` 検知 |
| **Backdrop クリック** | `.modal__backdrop` の click イベントで close |

```js
// 例: keydown ESC
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && modal.classList.contains('is-open')) {
    closeModal();
  }
});

// 例: backdrop クリック（modal 本体のクリックは伝播停止）
modal.addEventListener('click', (e) => {
  if (e.target === modal) closeModal();
});
```

---

## States

### default（閉じている）
DOM に存在するが `display: none` または `aria-hidden="true"`。

### opening（フェードイン）
- Backdrop opacity 0 → 1（duration-base）
- Modal body opacity 0 → 1 + scale(0.95) → scale(1)（duration-base + ease-out）

### open
完全表示。focus を Modal 内の最初のフォーカス可能要素にトラップ。

### closing（フェードアウト）
- 逆順で opacity 1 → 0
- 完了後に `display: none`

### Sheet 専用 slide
- 下端から `transform: translateY(100%) → translateY(0)`（duration-slow + ease-out）

---

## 共通 Props

| プロパティ | 値 |
|---|---|
| z-index | `--layer-5` |
| backdrop | `rgba(0, 0, 0, 0.6)` |
| modal background | `--bg-primary` |
| modal border-radius | `--radius-md`（8px / Sheet は上端のみ）|
| modal padding | `--space-4`（32px） |
| modal shadow | `--shadow-4`（強・浮き上がり強調）|
| transition | `--duration-base` `--ease-out` |
| max-width | Confirmation 400 / Detail 800 / Sheet 100% |

---

## Liquid 実装例

### Confirmation（Plan 変更確認）
```liquid
{% raw %}<div class="modal modal-confirmation" id="plan-change-modal" role="dialog" aria-modal="true" aria-labelledby="plan-change-title" hidden>
  <div class="modal__backdrop" data-modal-close></div>
  <div class="modal__body">
    <h2 class="modal__title" id="plan-change-title">プランを変更しますか？</h2>
    <p class="modal__text">変更後のプランは次回お届け分から適用されます。</p>
    <div class="modal__actions">
      <button type="button" class="btn btn-ghost btn-md" data-modal-close>キャンセル</button>
      <button type="submit" class="btn btn-primary btn-md" data-modal-confirm>変更する</button>
    </div>
  </div>
</div>{% endraw %}
```

### Detail（Case Study 詳細）
```liquid
{% raw %}<div class="modal modal-detail" id="case-detail-modal" role="dialog" aria-modal="true" aria-labelledby="case-title" hidden>
  <div class="modal__backdrop" data-modal-close></div>
  <div class="modal__body">
    <header class="modal__header">
      <h2 class="modal__title" id="case-title">{{ case.title }}</h2>
      <button type="button" class="btn btn-icon-only btn-md modal__close" aria-label="閉じる" data-modal-close>
        {%- render 'icon', name: 'nav-close', size: 24 -%}
      </button>
    </header>
    <div class="modal__content">
      {{ case.full_content }}
    </div>
  </div>
</div>{% endraw %}
```

### Sheet（SP フィルタ）
```liquid
{% raw %}<div class="modal modal-sheet" id="filter-sheet" role="dialog" aria-modal="true" aria-labelledby="filter-title" hidden>
  <div class="modal__backdrop" data-modal-close></div>
  <div class="modal__body">
    <header class="modal__header">
      <h2 class="modal__title" id="filter-title">絞り込み</h2>
      <button type="button" class="btn btn-icon-only btn-sm modal__close" aria-label="閉じる" data-modal-close>
        {%- render 'icon', name: 'nav-close', size: 24 -%}
      </button>
    </header>
    <div class="modal__content">
      {%- render 'filter-form' -%}
    </div>
    <footer class="modal__actions">
      <button type="button" class="btn btn-ghost btn-md" data-modal-close>クリア</button>
      <button type="submit" class="btn btn-primary btn-md">適用する</button>
    </footer>
  </div>
</div>{% endraw %}
```

---

## CSS（v0.2 実装）

```css
/* === Modal 基本 === */
.modal {
  position: fixed;
  inset: 0;
  z-index: var(--layer-5);
  display: none;
  align-items: center;
  justify-content: center;
  padding: var(--space-3);
}

.modal.is-open {
  display: flex;
}

.modal[hidden] {
  display: none !important;
}

/* === Backdrop === */
.modal__backdrop {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  opacity: 0;
  transition: opacity var(--duration-base) var(--ease-out);
}

.modal.is-open .modal__backdrop {
  opacity: 1;
}

/* === Modal Body 共通 === */
.modal__body {
  position: relative;
  background: var(--bg-primary);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  box-shadow: var(--shadow-4);
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  opacity: 0;
  transform: scale(0.95);
  transition: opacity var(--duration-base) var(--ease-out),
              transform var(--duration-base) var(--ease-out);
}

.modal.is-open .modal__body {
  opacity: 1;
  transform: scale(1);
}

/* === Header === */
.modal__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-3);
  padding-bottom: var(--space-2);
  border-bottom: 1px solid var(--border-light);
}

.modal__title {
  font-family: var(--font-ja);
  font-size: var(--fs-h3);
  font-weight: var(--fw-bold);
  color: var(--color-ink);
  letter-spacing: var(--ls-ja);
}

.modal__text {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-sub);
  line-height: var(--lh-body);
}

/* === Content === */
.modal__content {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-ink);
  line-height: var(--lh-body);
}

/* === Actions === */
.modal__actions {
  display: flex;
  gap: var(--space-2);
  justify-content: flex-end;
  margin-top: var(--space-4);
  padding-top: var(--space-3);
  border-top: 1px solid var(--border-light);
}

@media (max-width: 480px) {
  .modal__actions {
    flex-direction: column-reverse;  /* SP は Primary を上に */
  }
}

/* === Close button === */
.modal__close {
  flex-shrink: 0;
}

/* === Variant: Confirmation === */
.modal-confirmation .modal__body {
  max-width: 400px;
}

/* === Variant: Detail === */
.modal-detail .modal__body {
  max-width: 800px;
  max-height: 90vh;
}

/* === Variant: Sheet（SP 専用）=== */
.modal-sheet {
  align-items: flex-end;
  padding: 0;
}

.modal-sheet .modal__body {
  max-width: 100%;
  max-height: 80vh;
  border-radius: var(--radius-md) var(--radius-md) 0 0;
  transform: translateY(100%);
  transition: transform var(--duration-slow) var(--ease-out);
}

.modal-sheet.is-open .modal__body {
  transform: translateY(0);
}

/* PC では Sheet を Confirmation 風に動作させる（Anti 回避）*/
@media (min-width: 768px) {
  .modal-sheet {
    align-items: center;
    padding: var(--space-3);
  }
  .modal-sheet .modal__body {
    max-width: 400px;
    max-height: 90vh;
    border-radius: var(--radius-md);
    transform: scale(0.95);
  }
  .modal-sheet.is-open .modal__body {
    transform: scale(1);
  }
}

/* === reduced motion === */
@media (prefers-reduced-motion: reduce) {
  .modal__backdrop,
  .modal__body {
    transition: none;
  }
  .modal__body {
    transform: none;
  }
}
```

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| `role="dialog"` + `aria-modal="true"` | 必須 |
| `aria-labelledby` | Title 要素の id を必ず参照 |
| `aria-describedby` | 補足テキストがある場合に追加（任意） |
| Focus trap | Modal 内の Tab 移動を内部に制限（JS 必須） |
| 初期 focus | 最初のフォーカス可能要素（Cancel ボタン等）に自動フォーカス |
| ESC キー | 必ず close 動作（Q3 A 採択） |
| body スクロールロック | Modal 表示中は `<body>` の overflow: hidden |
| Close 後の focus 復元 | trigger 要素にフォーカスを戻す |
| `prefers-reduced-motion` | アニメ無効化（既存 tokens.css 対応） |

```js
// Focus trap 実装例
const focusable = modal.querySelectorAll('a, button, input, [tabindex]:not([tabindex="-1"])');
const first = focusable[0];
const last = focusable[focusable.length - 1];

modal.addEventListener('keydown', (e) => {
  if (e.key !== 'Tab') return;
  if (e.shiftKey && document.activeElement === first) {
    e.preventDefault();
    last.focus();
  } else if (!e.shiftKey && document.activeElement === last) {
    e.preventDefault();
    first.focus();
  }
});
```

---

## Do / Don't

### ✅ Do
- 全 Variants で × / ESC / Backdrop クリックの 3 方法を実装
- Confirmation のボタン文言は **日本語動詞ベース**（「キャンセル」「変更する」「送信する」）
- Detail Modal は最大高さ 90vh を厳守（スクロールは Modal 内で）
- Focus trap を JS で実装し、Modal 内に Tab 移動を閉じ込める
- Close 後は trigger 要素に focus を戻す
- body スクロールロック（Modal 表示中）

### ✕ Don't（Q4 A 禁止リスト準拠）
- ❌ **Modal 内 Modal**（ネスト）禁止 — 認知負荷が極端に高い・実装で z-index 管理が破綻
- ❌ **Confirmation で「OK」「Cancel」等の英語ボタン**禁止 — 日本語動詞で意図明示
- ❌ **Detail Modal の高さを画面の 90% 超えて作らない** — フルスクリーンに近くなり Modal の意味消失
- ❌ **Sheet を PC で使わない** — PC では Confirmation 風に挙動切替（CSS で対応済）
- ❌ Backdrop に動画や画像を使わない（DNA Anti / 派手）
- ❌ Modal 内に Hero 級画像を置かない（Modal の役割逸脱）

---

## Brand DNA Anti との照合

本コンポは以下の Anti を踏まない:
- 派手・煽り → Backdrop は Glass 4 固定の単色暗化
- 媚びた表現 → 「キャンセル」「変更する」等の動詞ベース日本語
- 過剰演出 → reduced-motion 対応・スケール 0.95→1.0 の控えめなアニメ

---

## L4 派生関係

| 派生 | 継承する Variant | 追加要素 |
|---|---|---|
| Image Lightbox | Detail（max-width 90vw / max-height 90vh）| 前後ナビ矢印 / カウンター |
| Video Modal | Detail | 動画埋込 / Player controls |
| Filter Sheet | Sheet（SP）/ Sidebar（PC）| Form Controls 群 |
| Toast（区別: Modal とは別 Component）| - | 一時通知・Modal 階層と分離 |

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `5. Components Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study`
- **Component Set ID**: `62:33` ✅（Audit #4 で既存確認、2026-05-12）
- **実装済 variants**: 3（`variant`: confirmation / detail / sheet）

## Liquid 実装

- **File**: `sections/fambox-modal.liquid`（672 行）
- **Schema**: 14 settings + 3 presets（Confirmation / Detail / Sheet）
- **JS API**: `window.FAMBoxModal[modalId].open() / .close()` + `data-modal-trigger="<modalId>"` + CustomEvent `fambox-modal:confirm`
- **Close 3 方法**: × ボタン / ESC キー / Backdrop クリック（全て実装）
- **Accessibility**: `role="dialog"` + `aria-modal="true"` + `aria-labelledby` + Focus trap + body scroll lock + `prefers-reduced-motion` 対応

## Change Log
- v0.2-audit-ok (2026-05-14): Session #32 で再 Audit。Set 62:33 の 3 variants（confirmation 400×219 / detail 800×236 / sheet 800×345）配置は x=0, 500, 1400 で問題なし、property `variant` も spec と完全整合。**修正不要**。Set boundary 2200×345 も適切
- v0.2-liquid (2026-05-14): `fambox-modal.liquid` 三位一体達成。3 variants 内包 + 3 presets。spec の Liquid 実装例（Confirmation / Detail / Sheet）を 1 section に統合。JS で Focus trap / ESC / Backdrop / body scroll lock を実装
- v0.2-figma (2026-05-12): Audit #4 で Component Set `62:33` を既存確認。3 variants 実装済
- v0.2 (2026-04-28): Worksheet §22 確定（3 Variants / Backdrop Glass 4 固定 / Close 3 方法 / 4 禁止項目明示）。既存 Shopify product-media-modal 等の実装サンプルから一般化した L4 Modal Component
