---
title: FAMBOX Primitive — Input
type: design-system
layer: L2-Primitives
component: Input
version: 0.2
status: confirmed
last_updated: 2026-04-20
owner: 宮川
source: FAM Brand DNA v0.5 L-1（継承）+ Worksheet §7（2026-04-20 確定）
brand_alignment:
  - Integrity（誠実）: 装飾を排除した素直な入力体験
  - Co-driven（対等）: 過度な圧迫感のない必須表記
related:
  - form-field.md
  - tokens/colors.md
---

# Input — Primitive Component

## 概要
FAMBOX で最も使用頻度の高い Primitive。**下線型 + 枠囲み型** のハイブリッド運用（v0.5確定）。

## ブランド整合性
- **Integrity**: 装飾過多を避け、素直な入力体験
- **Co-driven**: 「必須」バッジで対等な情報伝達（赤*等の威圧表現を回避）
- **Anti**: 「敷居高い」「お客様対応化」表現を避ける

---

## Variants

### 下線型（Underline）
**用途**: 単一入力 — 検索 / ニュースレター / メール / その他軽量UI

| プロパティ | 値 |
|---|---|
| border-top | none |
| border-right | none |
| border-bottom | `1px solid var(--border-base)` |
| border-left | none |
| padding | `12px 0` |
| background | transparent |
| font-family | `var(--font-ja)` |
| font-size | `var(--fs-body)`（16px） |
| color | `var(--color-ink)` |

#### Focus状態
```css
.input-underline:focus {
  outline: none;
  border-bottom: 2px solid var(--color-drive);
}
```

### 枠囲み型（Bordered）
**用途**: 複雑フォーム — 診断 / 問合せ / アカウント情報

| プロパティ | 値 |
|---|---|
| border | `1px solid var(--border-base)` |
| border-radius | `var(--radius-md)`（8px） |
| padding | `12px 16px` |
| background | `var(--bg-primary)` |
| font-family | `var(--font-ja)` |
| font-size | `var(--fs-body)`（16px） |
| color | `var(--color-ink)` |

#### Focus状態
```css
.input-bordered:focus {
  outline: none;
  border-color: var(--color-drive);
  border-width: 2px;
  padding: 11px 15px; /* border 2px増加分を相殺 */
}
```

### Textarea（複数行）
**Worksheet §7 Q2 確定: 枠囲み型を縦に伸ばす**

```css
.textarea {
  /* .input-bordered と同仕様 */
  border: 1px solid var(--border-base);
  border-radius: var(--radius-md);
  padding: 12px 16px;
  background: var(--bg-primary);
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-ink);
  /* Textarea固有 */
  min-height: calc(var(--space-3) * 4);  /* 約96px = 4行分 */
  resize: vertical;
  line-height: var(--lh-body);
}
```

---

## States（8状態）

| 状態 | 振る舞い |
|---|---|
| default | 基準スタイル |
| hover | border-color を `var(--border-base)` → 微暗（`#A0A0A0`相当）|
| focus | Drive色2pxボーダー（上記Variant参照） |
| active | focus と同等 |
| disabled | `background: var(--bg-tertiary)` / `color: var(--color-placeholder)` / `cursor: not-allowed` |
| empty | placeholder表示・薄色 |
| error | `border-color: var(--color-error-text)` `#F91A02` |
| success | `border-color: var(--color-success)` `#10B981`（任意・通常はFormField側で表示） |

---

## Validation

**Worksheet §7 Q3 確定: onBlur即時表示**（v0.5既定）

### 動作
- ユーザーがフィールドからフォーカスを外した瞬間に検証実行
- エラーがあれば即座に Error 状態へ遷移＋ErrorMessage 表示
- Submit時は再検証＋全フィールドのエラーを一覧表示

### 文字数カウンタ
**限定運用**: 自由記述フィールド（問合せ内容など）にのみ表示

```html
<div class="input-counter">
  <span class="current">0</span> / <span class="max">500</span>
</div>
```

```css
.input-counter {
  font-size: var(--fs-caption);
  color: var(--color-caption);
  text-align: right;
  margin-top: var(--space-1);
}
.input-counter.is-over {
  color: var(--color-error-text);
}
```

---

## Required Marker

**Worksheet §7 Q4 確定: 「必須」バッジをラベル横**

### マークアップ
```html
<label for="company">
  会社名・団体名
  <span class="badge-required">必須</span>
</label>
<input type="text" id="company" class="input-bordered" required>
```

### スタイル
```css
.badge-required {
  display: inline-block;
  padding: 2px 8px;
  margin-left: var(--space-1);
  border-radius: var(--radius-sm);
  background: var(--color-drive);
  color: var(--color-white);
  font-family: var(--font-ja);
  font-size: var(--fs-caption);  /* 12px */
  font-weight: var(--fw-semibold);
  letter-spacing: var(--ls-ja);
  vertical-align: middle;
}
```

### なぜ赤「*」ではなく日本語バッジか
- 赤「*」は**意味伝達が弱い**（特に高齢層・初訪問ユーザー）
- 視覚ノイズになりがち（複数フィールドで点だらけ）
- B2B フォームは Submit 完了率が事業数値に直結 → 明確な日本語ラベルで誤入力減
- Anti「敷居高い表現」回避＝「任意」逆指定はB2Bで体験を硬くしすぎる

---

## Liquid 実装例

### 下線型（メールサインアップ）
```liquid
{% raw %}<label for="newsletter-email" class="visually-hidden">メールアドレス</label>
<input type="email"
       id="newsletter-email"
       class="input-underline"
       placeholder="メールアドレスを入力"
       required>{% endraw %}
```

### 枠囲み型（問合せフォーム会社名）
```liquid
{% raw %}<div class="form-field">
  <label for="company">
    会社名・団体名
    <span class="badge-required">必須</span>
  </label>
  <input type="text"
         id="company"
         class="input-bordered"
         placeholder="例: ○○高校サッカー部"
         required>
</div>{% endraw %}
```

---

## Accessibility

- **Label 必須**: `<label for="...">` または `aria-label`
- **Required**: `required` 属性 + 視覚マーク両方（スクリーンリーダー対応）
- **Error**: `aria-invalid="true"` + `aria-describedby` で ErrorMessage に紐付け
- **Touch Target**: padding込みで最小44px高を確保
- **Focus Visible**: Drive色2pxボーダーは WCAG 2.1 AA 準拠

---

## Do / Don't

### ✅ Do
- 単一入力は **下線型**、複数項目フォームは **枠囲み型** で統一
- Required は「必須」バッジで明示
- Placeholder は「例: 〇〇」形式（入力例として）
- Validation は onBlur 即時表示

### ✕ Don't
- フォーム内で下線型と枠囲み型を混ぜない
- Required を `*` だけで示さない（バッジ必須）
- Placeholder に補足情報を入れない（入力時に消える）
- Disabled の文字色を可読性ギリギリまで薄くしない

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `3. Primitives`
- **Component Set ID**: `50:26` ✅ 自動生成済（2026-05-12）
- 生成スキル: `figma-component-from-spec` v0.1
- **実装済 variants**: 12（`variant` × `state`）
  - variant: underline / bordered / textarea
  - state: default / focus / disabled / error
- **未実装 states（v0.3 で追加予定）**: hover / active / empty / success
- フォント: Noto Sans JP（Hiragino Sans 代替）
- Variables バインド: color (bg/border/text) / radius (md) / font-size (body)

## Change Log
- v0.2 (2026-04-20): Worksheet §7 確定（下線型+枠囲み型ハイブリッド・onBlur検証・「必須」バッジ）
- v0.2-figma (2026-05-12): Figma Component Set 自動生成（12 variants）
