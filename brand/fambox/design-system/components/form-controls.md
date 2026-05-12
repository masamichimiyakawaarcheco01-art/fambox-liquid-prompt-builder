---
title: FAMBOX Primitives — Form Controls (Checkbox / Radio / Toggle)
type: design-system
layer: L2-Primitives
component: FormControls
version: 0.2
status: confirmed
last_updated: 2026-04-20
owner: 宮川
source: Worksheet §10（2026-04-20 確定）
brand_alignment:
  - Co-driven: タッチ可能で対等な操作感
  - Integrity: 標準的UIで予測可能性を担保
related:
  - input.md
  - form-field.md
---

# Form Controls — Checkbox / Radio / Toggle

選択操作の3 Primitive。同意・複数選択・単一選択・設定切替に使用。

## ブランド整合性
- **Co-driven**: 全コントロールタッチターゲット 24px以上で対等な操作性
- **Integrity**: iOS/Android標準UIに近い形状でメンタルモデル一致
- **Anti**: 独自すぎる形状で操作迷子を防ぐ

---

## Checkbox

**🎯 確定: 角4px・Drive色チェック・24×24px**

| 状態 | 仕様 |
|---|---|
| サイズ | 24×24px |
| ボーダー | 1.5px solid `var(--border-base)` |
| 角丸 | `var(--radius-sm)` (4px) |
| 背景 | `var(--bg-primary)` (default) / `var(--color-drive)` (checked) |
| チェックマーク | 白 SVG（16px相当）|

```css
.checkbox {
  appearance: none;
  width: 24px;
  height: 24px;
  border: 1.5px solid var(--border-base);
  border-radius: var(--radius-sm);
  background: var(--bg-primary);
  cursor: pointer;
  transition: background var(--duration-fast) var(--ease-out),
              border-color var(--duration-fast) var(--ease-out);
}

.checkbox:checked {
  background: var(--color-drive);
  border-color: var(--color-drive);
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>');
  background-position: center;
  background-repeat: no-repeat;
}

.checkbox:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}

.checkbox:disabled {
  background: var(--bg-tertiary);
  border-color: var(--border-light);
  cursor: not-allowed;
}
```

### Liquid 例
```liquid
{% raw %}<label class="checkbox-label">
  <input type="checkbox" class="checkbox" name="agree" required>
  <span>プライバシーポリシーに同意する</span>
</label>{% endraw %}
```

---

## Radio

**🎯 確定: 円形・Drive色塗り潰し**

| 状態 | 仕様 |
|---|---|
| サイズ | 24×24px（外円） |
| 内側ドット | 12×12px（checked時のみ） |
| ボーダー | 1.5px solid `var(--border-base)` |
| 形状 | 完全円 |

```css
.radio {
  appearance: none;
  width: 24px;
  height: 24px;
  border: 1.5px solid var(--border-base);
  border-radius: var(--radius-pill);
  background: var(--bg-primary);
  cursor: pointer;
  position: relative;
  transition: border-color var(--duration-fast) var(--ease-out);
}

.radio:checked {
  border-color: var(--color-drive);
}

.radio:checked::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 12px;
  height: 12px;
  border-radius: var(--radius-pill);
  background: var(--color-drive);
}

.radio:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

### Liquid 例（問合せ種別）
```liquid
{% raw %}<fieldset class="radio-group">
  <legend>問合せ種別 <span class="badge-required">必須</span></legend>
  {% for option in inquiry_options %}
    <label class="radio-label">
      <input type="radio" class="radio" name="inquiry_type" value="{{ option.value }}" required>
      <span>{{ option.label }}</span>
    </label>
  {% endfor %}
</fieldset>{% endraw %}
```

---

## Toggle

**🎯 確定: Pill型・Drive色 ON / グレー OFF**

| 状態 | 仕様 |
|---|---|
| 全体 | 48×24px Pill |
| ノブ（◯） | 20×20px 白 |
| OFF背景 | `var(--border-base)` `#D0D0D0` |
| ON背景 | `var(--color-drive)` |
| アニメ | 200ms ease-out |

```css
.toggle {
  appearance: none;
  position: relative;
  width: 48px;
  height: 24px;
  border-radius: var(--radius-pill);
  background: var(--border-base);
  cursor: pointer;
  transition: background var(--duration-base) var(--ease-out);
}

.toggle::after {
  content: '';
  position: absolute;
  top: 2px;
  left: 2px;
  width: 20px;
  height: 20px;
  border-radius: var(--radius-pill);
  background: var(--color-white);
  box-shadow: var(--shadow-1);
  transition: transform var(--duration-base) var(--ease-out);
}

.toggle:checked {
  background: var(--color-drive);
}

.toggle:checked::after {
  transform: translateX(24px);
}

.toggle:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

### Liquid 例（設定画面）
```liquid
{% raw %}<label class="toggle-label">
  <input type="checkbox" class="toggle" name="newsletter">
  <span>お知らせメールを受け取る</span>
</label>{% endraw %}
```

---

## ラベル配置（共通）

```css
.checkbox-label,
.radio-label,
.toggle-label {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-ink);
  cursor: pointer;
  /* タッチターゲット 44px 最小確保 */
  min-height: 44px;
}
```

---

## 使用頻度の予測（Worksheet §10 Q4）

**🎯 確定: Checkbox 多い**

| Control | 主な使用場面 |
|---|---|
| **Checkbox** | プライバシー同意・複数選択（食物アレルギー/競技種目）・同意系 |
| Radio | 単一選択（問合せ種別・性別）|
| Toggle | 設定画面・通知ON/OFF・定期便スキップ |

---

## Accessibility
- ✅ 全コントロール `<label>` で囲む or `for` 紐付け
- ✅ `required` 属性 + 「必須」バッジ両方
- ✅ Touch target 44×44px 以上（label 全体で確保）
- ✅ Focus ring Drive 2px（WCAG 2.1 AA）
- ✅ Toggle は `role="switch"` を将来追加検討

---

## Do / Don't

### ✅ Do
- フォーム内では Checkbox/Radio を使い、設定画面では Toggle を使う
- ラベルクリックでも切り替わるように `<label>` で囲む
- Required はバッジで明示

### ✕ Don't
- Toggle で「保存」を意味させない（即時反映のみ）
- Checkbox を「単一選択」に使わない（Radio を使う）
- 独自形状のチェックマークを作らない（標準のtickで十分）

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `3. Primitives`
- **Component Set ID**: `54:16` ✅ 自動生成済（2026-05-12）
- 生成スキル: `figma-component-from-spec` v0.1
- **実装済 variants**: 9（`kind` × `state`）
  - kind: checkbox / radio / toggle
  - state (checkbox/radio): default / checked / disabled
  - state (toggle): off / on / disabled
- Checkbox checked: ✓ tick（Poppins Bold Unicode U+2713、white）
- Toggle knob: 20×20 white ellipse + drop shadow
- **未実装（v0.3 で追加予定）**: focus / hover state、`role="switch"` メタデータ
- Variables バインド: color (drive/bg-primary/bg-tertiary/border-base/border-light) / radius (sm/pill)

## Change Log
- v0.2 (2026-04-20): Worksheet §10 確定（標準形状3種・Drive色軸）
- v0.2-figma (2026-05-12): Figma Component Set 自動生成（9 variants）
