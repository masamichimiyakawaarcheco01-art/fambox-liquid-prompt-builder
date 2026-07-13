---
title: FAMBOX Pattern — Mini Header
type: design-system
layer: L3-Patterns
component: MiniHeader
version: 0.3
status: confirmed
last_updated: 2026-05-08
owner: 宮川
source: 食事診断 Quiz画面実装からの抽出
brand_alignment:
  - Integrity: 必要最小限の情報のみ
  - Co-driven: 「戻る」を常に提供して操作の自由を保証
related:
  - components/header.md (既存 Site Header)
  - components/button.md
---

# Mini Header — Pattern Component

**Sticky な軽量ヘッダー**。フォーム・診断・チェックアウトなど、
「進行中タスク」の上部に配置する。

## ブランド整合性
- **Integrity**: ロゴ・ナビゲーションを排除、タスクに集中させる
- **Co-driven**: 戻るボタンで常に「やめる/やり直す」自由を保証

---

## 既存 Header との違い

| 項目 | Site Header（既存） | Mini Header |
|---|---|---|
| **用途** | 全ページ共通ナビゲーション | タスク進行中（Quiz / Form / Checkout） |
| **高さ** | 64-80px | **48-56px** |
| **要素** | ロゴ + メニュー + CTA | 戻る + Step表示（中央/右）|
| **Sticky** | 任意 | **必須** |
| **背景** | 不透明 | **半透明 + blur** |

---

## 構造

```html
<header class="mini-header">
  <button class="mini-header__back">
    <svg>...</svg>
    戻る
  </button>
  <span class="mini-header__step">STEP 3 / 5</span>
  <!-- オプション: 右側アクション -->
  <button class="mini-header__action">中断</button>
</header>
```

---

## 仕様

### Container
| 項目 | 値 |
|---|---|
| position | `sticky` / top: 0（または親の上端）|
| z-index | 50（モーダル未満・固定要素より上） |
| background | `rgba(255,255,255,0.92)` |
| backdrop-filter | `blur(8px)` |
| border-bottom | 1px solid `--border-light` |
| padding | 12px 24px |
| display | flex / align-items: center / gap: 16px |
| justify-content | space-between |

### Back Button
| 項目 | 値 |
|---|---|
| display | inline-flex / align-items: center / gap: 6px |
| padding | 8px 12px |
| font | Hiragino W5 14px |
| color | `--color-sub` |
| border-radius | `--radius-pill-cta` |
| icon | `nav-back.svg` 16×16 |
| hover | bg `rgba(27,29,26,0.05)` / color `--color-ink` |

#### 非表示状態（最初のステップ等）
```html
<button class="mini-header__back is-hidden">...</button>
```
```css
.mini-header__back.is-hidden { visibility: hidden; }
```
※ display:none ではなく visibility:hidden で**レイアウトを保つ**（Step表示の位置がずれない）

### Step Indicator
| 項目 | 値 |
|---|---|
| font | Poppins 12 Medium |
| letter-spacing | 0.16em |
| color | `--color-caption` |
| text-transform | uppercase |
| 例 | "STEP 3 / 5" |

---

## CSS（実装）

```css
.mini-header {
  position: sticky;
  top: 0;
  z-index: 50;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border-light);
  padding: 12px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.mini-header__back {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-ja);
  font-size: 14px;
  font-weight: var(--fw-medium);
  color: var(--color-sub);
  padding: 8px 12px;
  border-radius: var(--radius-pill-cta);
  transition: background var(--duration-fast) var(--ease-out);
}
.mini-header__back:hover {
  background: rgba(27, 29, 26, 0.05);
  color: var(--color-ink);
}
.mini-header__back.is-hidden { visibility: hidden; }

.mini-header__step {
  font-family: var(--font-en);
  font-size: 12px;
  font-weight: var(--fw-medium);
  letter-spacing: 0.16em;
  color: var(--color-caption);
  text-transform: uppercase;
}
```

---

## Variants（拡張余地）

| Variant | 用途 |
|---|---|
| `mini-header--default` ★ | 戻る + Step表示 |
| `mini-header--with-action` | 右側にアクションボタン（中断・スキップ等） |
| `mini-header--no-back` | 戻るボタン非表示（最初のステップ等） |

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| 戻るボタン | `aria-label="前のステップに戻る"` |
| Step | `aria-live="polite"` で進行通知 |
| Touch Target | 戻るボタンは min 44px |
| Keyboard | Tab で戻るボタンに focus 可能 |

---

## Do / Don't

### ✅ Do
- 半透明 + blur で**コンテンツとの分離感**を出す
- 戻るボタンは常に表示（最初のステップは visibility hidden で位置維持）
- Step は中央 or 右揃え（左の戻るボタンと対称）

### ✕ Don't
- ロゴやメニューを入れない（Site Header と差別化）
- 高さを 64px 以上にしない（Mini の意義喪失）
- background を不透明にしない（コンテンツとのつながり喪失）

---

## Change Log

- v0.3 (2026-05-08): Quiz画面実装から抽出して新規策定
