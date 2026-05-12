---
title: FAMBOX Pattern — FormField
type: design-system
layer: L3-Patterns
component: FormField
version: 0.2
status: confirmed
last_updated: 2026-04-20
owner: 宮川
source: Worksheet §8（2026-04-20 確定）
brand_alignment:
  - Integrity（誠実）: 入力に必要な情報を最も読みやすい位置に配置
  - Co-driven（対等）: エラー時もユーザーを責めない位置・トーン
related:
  - input.md
  - tokens/colors.md
---

# FormField — Pattern Component

## 概要
**FormField = Label + Input + HelperText + ErrorMessage** の標準構造。Form 内の全入力単位で使用。

## ブランド整合性
- **Integrity**: 補助情報を「常時表示」して誤入力を減らす（誠実な情報提供）
- **Co-driven**: ラベルが上配置でフィールドと対等な情報階層

---

## 構造

```
┌─────────────────────────────────────────┐
│ ラベル [必須]                            │ ← Label（上配置）
├─────────────────────────────────────────┤
│ ┌─────────────────────────────────────┐ │
│ │ 入力欄                              │ │ ← Input
│ └─────────────────────────────────────┘ │
│ 例: ○○○ で記入してください            │ ← HelperText（Input下・薄色）
│ ⚠ 入力に誤りがあります                 │ ← ErrorMessage（Input下・赤）
└─────────────────────────────────────────┘
```

---

## 各要素の配置（Worksheet §8 確定）

### Label の位置
**🎯 確定: 上配置（標準）**

#### 理由
- モバイル含め最も読みやすい
- スクリーンリーダー親和性◎（DOM順とビジュアル順が一致）
- 国際標準（FormField の de facto standard）

```html
<label for="company" class="form-label">
  会社名・団体名
  <span class="badge-required">必須</span>
</label>
```

```css
.form-label {
  display: block;
  margin-bottom: var(--space-1);  /* 8px */
  font-family: var(--font-ja);
  font-size: var(--fs-body-sm);   /* 14px */
  font-weight: var(--fw-semibold);
  color: var(--color-ink);
  letter-spacing: var(--ls-ja);
}
```

### HelperText の位置
**🎯 確定: Input下・薄色（`--color-sub`）**

#### 理由
- 入力前は読まれにくくても問題ない補足情報
- 上配置はラベルと本文の階層を壊す
- 入力中も常時表示で参照可能（Placeholderとの差別化）

```html
<p class="form-helper">例: ○○高校サッカー部、○○大学体育会野球部 等</p>
```

```css
.form-helper {
  margin-top: var(--space-1);  /* 8px */
  font-family: var(--font-ja);
  font-size: var(--fs-caption);  /* 12px */
  color: var(--color-sub);       /* #545655 */
  line-height: var(--lh-caption);
  letter-spacing: var(--ls-ja);
}
```

### ErrorMessage の位置
**🎯 確定: Input下・赤（`--color-error-text` `#F91A02`）**

#### 理由
- フィールドとの紐付けが最も明確
- Toast だと文脈が分離して原因特定が遅れる
- HelperText と同じ位置 → エラー時に置き換え or 併記

```html
<p class="form-error" role="alert">
  <span class="icon-error">⚠</span>
  入力に誤りがあります。例の形式でご入力ください。
</p>
```

```css
.form-error {
  margin-top: var(--space-1);
  font-family: var(--font-ja);
  font-size: var(--fs-caption);
  color: var(--color-error-text);  /* #F91A02 */
  line-height: var(--lh-caption);
  display: flex;
  align-items: center;
  gap: var(--space-1);
}
```

### 入力例（「例: ○○」）の表示位置
**🎯 確定: HelperText に書く**

#### 理由
- Placeholder に書くと**入力時に消えて参照不可**になる致命的問題
- HelperText は常時表示で入力中も参照可能
- スクリーンリーダーが label と紐付けて読み上げる

#### NG例（Placeholder方式）
```html
<input placeholder="例: ○○高校サッカー部">
<!-- ↑ 入力始めると消える / SR読まない場合あり -->
```

#### OK例（HelperText方式）
```html
<input id="company" placeholder="">
<p class="form-helper" id="company-help">例: ○○高校サッカー部</p>
```

---

## 完全なマークアップ例

```html
<div class="form-field">
  <label for="company" class="form-label">
    会社名・団体名
    <span class="badge-required">必須</span>
  </label>
  <input type="text"
         id="company"
         name="company"
         class="input-bordered"
         aria-describedby="company-help"
         required>
  <p class="form-helper" id="company-help">
    例: ○○高校サッカー部、○○大学体育会野球部 等
  </p>
  <!-- エラー時のみ表示 -->
  <p class="form-error" id="company-error" role="alert" hidden>
    <span class="icon-error">⚠</span>
    会社名・団体名を入力してください
  </p>
</div>
```

---

## CSS（FormField 全体）

```css
.form-field {
  display: flex;
  flex-direction: column;
  margin-bottom: var(--space-3);  /* 24px FormField 間ゆとり */
}

.form-field:last-child {
  margin-bottom: 0;
}

/* error 状態時 input にも色を反映 */
.form-field.is-error .input-bordered,
.form-field.is-error .input-underline {
  border-color: var(--color-error-text);
}

/* helper を error が出ている時に隠す（任意） */
.form-field.is-error .form-helper {
  display: none;
}
```

---

## State 遷移

| 状態 | Label | Input | HelperText | ErrorMessage |
|---|---|---|---|---|
| default | 表示 | default | 表示 | 非表示 |
| focus | 表示 | focus(Drive 2px) | 表示 | 非表示 |
| typing | 表示 | active | 表示（or counter） | 非表示 |
| error (onBlur) | 表示 | error(赤2px) | **非表示** | 表示 |
| success | 表示 | success（任意・通常はdefault） | 表示 | 非表示 |
| disabled | 表示・グレー | disabled | 表示・グレー | 非表示 |

---

## Liquid Snippet 例（再利用可能化）

`snippets/form-field.liquid`:
```liquid
{% raw %}{% comment %}
  Usage:
    {% render 'form-field',
       id: 'company',
       label: '会社名・団体名',
       required: true,
       type: 'text',
       placeholder: '',
       helper: '例: ○○高校サッカー部'
    %}
{% endcomment %}

<div class="form-field">
  <label for="{{ id }}" class="form-label">
    {{ label }}
    {% if required %}<span class="badge-required">必須</span>{% endif %}
  </label>
  <input type="{{ type | default: 'text' }}"
         id="{{ id }}"
         name="{{ id }}"
         class="input-bordered"
         placeholder="{{ placeholder | default: '' }}"
         {% if helper %}aria-describedby="{{ id }}-help"{% endif %}
         {% if required %}required{% endif %}>
  {% if helper %}
    <p class="form-helper" id="{{ id }}-help">{{ helper }}</p>
  {% endif %}
  <p class="form-error" id="{{ id }}-error" role="alert" hidden></p>
</div>{% endraw %}
```

---

## Accessibility

- ✅ `<label for="">` で Input と必ず紐付け
- ✅ HelperText は `aria-describedby` で参照
- ✅ ErrorMessage は `role="alert"` でSR読み上げ
- ✅ `aria-invalid="true"` を error 時に Input に付与
- ✅ Required は `required` 属性 + バッジ両方
- ✅ Tab 順序が DOM 順と一致

---

## Do / Don't

### ✅ Do
- Label を上配置で揃える（左配置はB2Bフォームでは古臭い印象）
- HelperText は常時表示で「例: 〜」形式
- ErrorMessage は具体的に「何が問題で、どうすれば直るか」を書く

### ✕ Don't
- Placeholder に補足情報を入れない（消える＋SR非対応）
- ErrorMessage を Toast でだけ出さない（フィールド紐付け不可）
- Label を Input 下に置かない（DOM順と視覚順がズレる）
- 「不正な入力です」等の曖昧なエラー文言を書かない

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `4. Patterns FormField / Card / Tooltip / Alert`
- **Component Set ID**: `56:34` ✅（Audit #4 で既存確認、2026-05-12）
- **実装済 variants**: 4（`state`: default / focus / error / disabled）
- ⚠ Spec ↔ Figma 整合: v0.3 で詳細レビュー必要（spec md は §8 のみ、Figma 実装の詳細項目未整合）

## Change Log
- v0.2-figma (2026-05-12): Audit #4 で Component Set `56:34` を既存確認。4 state variants 実装済、内部構造の spec 整合は v0.3 でレビュー
- v0.2 (2026-04-20): Worksheet §8 確定（Label上・Helper下薄色・Error下赤・例はHelperに）
