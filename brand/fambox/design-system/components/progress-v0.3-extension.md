---
title: FAMBOX Progress — v0.3 拡張案
type: design-system
layer: L2-Primitives
component: Progress
version: 0.3
status: extension-proposal
last_updated: 2026-05-08
owner: 宮川
source: Loading画面実装からの追加（Step-based progress）
note: 既存 components/progress.md（v0.2）への追記提案
---

# Progress v0.3 拡張案

既存 `components/progress.md`（v0.2）に**Step-based 進行表示**を追加する提案。
既存の Linear / Spinner はそのまま維持。

---

## 追記する Variant: Step Progress

**用途**: 多段階処理の進行状況可視化（Loading画面・複数ステップフォーム・チェックアウト）

### 構造
```html
<ol class="progress-steps">
  <li class="progress-step is-done">
    <span class="progress-step__indicator"></span>
    <span class="progress-step__label">体格データを評価中</span>
    <span class="progress-step__status-en">DONE</span>
  </li>
  <li class="progress-step is-active">
    <span class="progress-step__indicator"></span>
    <span class="progress-step__label">食事バランスをチェック中</span>
    <span class="progress-step__status-en">RUNNING</span>
  </li>
  <li class="progress-step">
    <span class="progress-step__indicator"></span>
    <span class="progress-step__label">最適なプランを算出中</span>
    <span class="progress-step__status-en">PENDING</span>
  </li>
</ol>
```

### 3 状態

| State | クラス | indicator | opacity | border | status-en |
|---|---|---|---|---|---|
| **pending** | （default） | 空円（border-base） | 0.4 | `--border-light` | "PENDING" gray |
| **active** ★ | `.is-active` | スピナー（Drive 2px ring rotating） | 1.0 | `--color-drive` | "RUNNING" Drive |
| **done** | `.is-done` | 塗りつぶし + 白チェック | 0.85 | `--color-success` | "DONE" Success |

### Indicator 仕様
| 項目 | 値 |
|---|---|
| size | 20×20 |
| border-width | 2px |
| border-radius | 50% |
| transition | all 300ms ease-out |

#### active のスピナー
```css
.progress-step.is-active .progress-step__indicator::after {
  content: '';
  position: absolute;
  inset: 3px;
  border-radius: 50%;
  border: 2px solid var(--color-drive);
  border-top-color: transparent;
  animation: spin 0.8s linear infinite;
}
```

#### done のチェックマーク
```css
.progress-step.is-done .progress-step__indicator {
  background: var(--color-success);
  border-color: var(--color-success);
}
.progress-step.is-done .progress-step__indicator::after {
  content: '';
  position: absolute;
  top: 2px;        /* ★ 2px が視覚的中心（Loading実装で検証済み） */
  left: 5px;
  width: 6px;
  height: 10px;
  border: solid white;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
  transform-origin: center;
}
```

### Container 仕様
```css
.progress-steps {
  display: flex;
  flex-direction: column;
  gap: 16px;
  list-style: none;
}
.progress-step {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 20px;
  background: var(--bg-primary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  opacity: 0.4;
  transition: opacity var(--duration-base) var(--ease-out),
              border-color var(--duration-base) var(--ease-out);
}
.progress-step.is-active {
  opacity: 1;
  border-color: var(--color-drive);
  background: rgba(251, 76, 21, 0.04);
}
.progress-step.is-done {
  opacity: 0.85;
  border-color: var(--color-success);
}
```

---

## 既存 Linear Progress の補強

実装で確認した **transition の数値**を既存 Linear に追記:

```css
.progress-linear__fill {
  transition: width 400ms cubic-bezier(0.4, 0, 0.2, 1);
  /* ↑ Quiz画面で使用、滑らかな進行表現 */
}
```

---

## Do / Don't

### ✅ Do
- pending / active / done の3状態を必ず視覚的に区別
- active は1つだけ（複数同時 active は混乱）
- done のチェックマークは `top: 2px` で視覚中心（4pxは下にズレる）

### ✕ Don't
- active を複数同時表示しない
- ステップ完了時に派手な祝祭演出を加えない（Brand Anti）
- pending の opacity を 0.2 以下にしない（読めなくなる）

---

## Change Log

- v0.3 拡張 (2026-05-08): Step-based progress を追加（Loading画面実装から抽出）
- v0.2 (2026-04-20): Linear / Spinner（既存）
