---
title: FAMBOX Primitives — Progress / Spinner
type: design-system
layer: L2-Primitives
component: Progress
version: 0.2
status: confirmed
last_updated: 2026-04-20
owner: 宮川
source: Worksheet §11（2026-04-20 確定）
brand_alignment:
  - Continuity: 進行表現で「積み重ね」感を伝える
  - Integrity: 過剰な文言演出を避ける
related:
  - tokens/colors.md
  - tokens/motion.md
---

# Progress / Spinner — Primitive Components

待機・進行を伝える Primitive。**過剰演出を避け、必要最小限で誠実に**。

## ブランド整合性
- **Continuity**: Progress Bar は「達成への積み上げ」表現
- **Integrity**: 「もう少しです！」等の煽りは使わない
- **Anti**: 派手なローディングアニメは Brand DNA 違反

---

## Progress Bar

**🎯 確定: 両方採用（用途で使い分け）**

### 線形 (Linear)
**用途**: フォーム送信中・読み込み・連続的進行

| 仕様 | 値 |
|---|---|
| 高さ | 4px |
| 角丸 | `var(--radius-pill)` |
| 背景 | `var(--bg-tertiary)` `#F3F3F3` |
| 進行色 | `var(--color-drive)` |
| アニメ | `var(--ease-out)` 300ms |

```css
.progress-linear {
  width: 100%;
  height: 4px;
  background: var(--bg-tertiary);
  border-radius: var(--radius-pill);
  overflow: hidden;
}

.progress-linear__bar {
  height: 100%;
  background: var(--color-drive);
  border-radius: var(--radius-pill);
  transition: width var(--duration-base) var(--ease-out);
}
```

### 円形 (Circular)
**用途**: 食事診断（Step進行）・達成率表示

| 仕様 | 値 |
|---|---|
| サイズ | 48 / 64 / 96 / 128px（用途別）|
| ストローク | 4-6px（サイズ比例）|
| 背景円 | `var(--bg-tertiary)` |
| 進行円 | `var(--color-drive)` |
| 中央テキスト | `--fs-h2` Drive色 |

```html
<div class="progress-circular" style="--size: 96px; --progress: 75;">
  <svg viewBox="0 0 36 36">
    <circle class="bg" cx="18" cy="18" r="16"/>
    <circle class="bar" cx="18" cy="18" r="16"
            stroke-dasharray="100, 100"
            stroke-dashoffset="calc(100 - var(--progress))"/>
  </svg>
  <span class="value">75%</span>
</div>
```

```css
.progress-circular {
  position: relative;
  width: var(--size);
  height: var(--size);
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.progress-circular svg { transform: rotate(-90deg); }
.progress-circular .bg { fill: none; stroke: var(--bg-tertiary); stroke-width: 4; }
.progress-circular .bar {
  fill: none;
  stroke: var(--color-drive);
  stroke-width: 4;
  stroke-linecap: round;
  transition: stroke-dashoffset var(--duration-slow) var(--ease-out);
}
.progress-circular .value {
  position: absolute;
  font-family: var(--font-en);
  font-size: var(--fs-h2);
  font-weight: var(--fw-bold);
  color: var(--color-drive);
}
```

---

## Spinner

**🎯 確定: 円形回転・Drive色（標準）**

| 仕様 | 値 |
|---|---|
| サイズ | 24 / 32 / 48px |
| ストローク | 2-3px |
| 色 | `var(--color-drive)` |
| アニメ | 1秒で1回転 / linear / infinite |
| 一部欠け | 75%（円弧）|

```html
<span class="spinner spinner-md" aria-label="読み込み中"></span>
```

```css
.spinner {
  display: inline-block;
  border: 3px solid var(--bg-tertiary);
  border-top-color: var(--color-drive);
  border-radius: var(--radius-pill);
  animation: spin 1s linear infinite;
}

.spinner-sm { width: 24px; height: 24px; border-width: 2px; }
.spinner-md { width: 32px; height: 32px; border-width: 3px; }
.spinner-lg { width: 48px; height: 48px; border-width: 4px; }

@keyframes spin {
  to { transform: rotate(360deg); }
}

@media (prefers-reduced-motion: reduce) {
  .spinner { animation: none; }
}
```

---

## Loading テキスト

**🎯 確定: 文言なし（基本）+ 重要処理のみ「処理中です…」**

### 通常用途（軽い読み込み）
- スピナーのみ
- 文言なし

### 重要処理（送信中・決済中）
```html
<div class="loading-state">
  <span class="spinner spinner-md"></span>
  <p class="loading-text">処理中です…</p>
</div>
```

```css
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-2);
}

.loading-text {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-sub);
  letter-spacing: var(--ls-ja);
}
```

### NG文言（使用禁止）
- ❌ 「もう少しお待ちください！」(煽り感)
- ❌ 「がんばって読み込み中…」(擬人化過剰)
- ❌ 「Loading...」(英語直書き)
- ❌ 「ロード中」(略語)

---

## Accessibility
- ✅ Spinner は `aria-label="読み込み中"` または `<span class="visually-hidden">読み込み中</span>`
- ✅ Progress Bar は `role="progressbar"` + `aria-valuenow` / `aria-valuemin` / `aria-valuemax`
- ✅ `prefers-reduced-motion` でアニメ停止（`tokens.css` で対応済）
- ✅ Loading State は `aria-live="polite"` で SR 通知

---

## Do / Don't

### ✅ Do
- フォーム送信は **線形 Progress Bar**
- 食事診断・達成率は **円形 Progress**
- 軽い読み込みは **Spinner のみ**（文言なし）
- 重い処理だけ「処理中です…」を添える

### ✕ Don't
- ローディング演出に呼吸アニメ・派手なエフェクトを混ぜない
- 進捗 0% から始まる場合は最低 5% を表示（完全空は不安）
- スピナー色を Sky/Deep に変えない（Drive固定）
- 「Loading」「Wait」等の英語直書きしない

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `3. Primitives`
- **Progress Bar Component Set ID**: `55:11` ✅ 自動生成済（2026-05-12）
- **Spinner Component Set ID**: `55:21` ✅ 自動生成済（2026-05-12）
- 生成スキル: `figma-component-from-spec` v0.1
- **実装済**:
  - Progress Bar Linear: 5 variants（value=0/25/50/75/100）
  - Spinner: 3 variants（size=sm/md/lg）arcData による 75% 円弧
- **未実装（v0.3 で追加予定）**:
  - **Progress Circular**: vectorPath による正確な arc curve（現状の Spinner は pie 形状に近い）
  - Loading State pattern（Spinner + 「処理中です…」テキスト）
- Variables バインド: color (drive/bg-tertiary) / radius (pill)

## Change Log
- v0.3-audit-ok (2026-05-15): Session #42 で Step 0.5 詳細 Audit を実戦投入。Spinner Set `55:21` の 3 variants (sm 24 / md 32 / lg 48) は重なり / overflow なし、property `size` も spec 通り。**Progress Bar + Spinner は本 spec md に統合記載**であることを再確認 → current.md §7-C で Spinner が独立 spec md なしのため「1/2」と誤評価されていた **false-negative** を修正、L2 Primitive **6/6 完全制覇 🏆** へ
- v0.2 (2026-04-20): Worksheet §11 確定（線形+円形両用・Drive色固定・文言最小）
- v0.2-figma (2026-05-12): Linear + Spinner 自動生成（8 variants）。Circular は v0.3 で対応
