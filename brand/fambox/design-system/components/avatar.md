---
title: FAMBOX Primitive — Avatar
type: design-system
layer: L2-Primitives
component: Avatar
version: 0.2
status: confirmed
last_updated: 2026-04-20
owner: 宮川
source: Worksheet §9（2026-04-20 確定）
brand_alignment:
  - Co-driven（対等）: 装飾なしで人物を主役に
  - Integrity: フォールバックで信頼感（Deep Blue）
related:
  - tokens/colors.md
  - tokens/spacing.md
---

# Avatar — Primitive Component

アスリート・栄養士・監督・コーチのプロフィール表示用 Primitive。

## ブランド整合性
- **Co-driven**: 円形＋装飾なしで「対等な人物表現」を実現
- **Integrity**: 写真なし時もブランド色（Deep Blue）で信頼感維持
- **Anti**: ボーダー多用や装飾過多を避ける

---

## サイズ（5段階）

| Size | 値 | CSS Variable | 主な用途 |
|---|---|---|---|
| XS | 24×24px | `--avatar-xs` | コメント・小ラベル |
| SM | 32×32px | `--avatar-sm` | リスト・テーブル行 |
| MD | 48×48px | `--avatar-md` | Card内・標準 |
| LG | 64×64px | `--avatar-lg` | Profile セクション |
| XL | 96×96px | `--avatar-xl` | Hero・Featured |

すべて 8の倍数で `--space-*` と整合。

---

## 形状

**🎯 確定: 円形（standard）**

```css
.avatar {
  border-radius: var(--radius-pill);  /* 9999px = 完全円 */
  overflow: hidden;
}
```

---

## フォールバック（画像なし時）

**🎯 確定: イニシャル（背景 Deep Blue / 文字 White）**

| 仕様 | 値 |
|---|---|
| 背景色 | `var(--color-deep)` `#0F2A5C` |
| 文字色 | `var(--color-white)` |
| フォント | `var(--font-en)` Poppins |
| ウェイト | `var(--fw-semibold)` 600 |
| 文字サイズ | Avatar サイズの 40%（例: MD 48px → 約20px）|
| 文字数 | 1文字（姓のローマ字頭文字 推奨）|

### 例
- 「大前」→ `O`
- 「Yamada」→ `Y`
- 「FAMBOX」→ `F`

---

## ボーダー / 枠

**🎯 確定: 装飾なし（デフォルト）+ Drive 2pxボーダー（Featured/選択時のみ）**

```css
/* default */
.avatar { /* no border */ }

/* featured / selected */
.avatar.is-featured {
  border: 2px solid var(--color-drive);
  /* 内側にborderが入らないよう注意 */
  box-sizing: content-box;
}

/* focus */
.avatar:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

---

## Liquid 実装例

### 写真あり
```liquid
{% raw %}<img src="{{ user.image | img_url: '96x96', crop: 'center' }}"
     alt="{{ user.name }}"
     class="avatar avatar-xl"
     width="96" height="96"
     loading="lazy">{% endraw %}
```

### フォールバック
```liquid
{% raw %}<span class="avatar avatar-md avatar-fallback" aria-label="{{ user.name }}">
  {{ user.name | slice: 0, 1 | upcase }}
</span>{% endraw %}
```

```css
.avatar-fallback {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: var(--color-deep);
  color: var(--color-white);
  font-family: var(--font-en);
  font-weight: var(--fw-semibold);
}

.avatar-xs { width: 24px; height: 24px; font-size: 10px; }
.avatar-sm { width: 32px; height: 32px; font-size: 13px; }
.avatar-md { width: 48px; height: 48px; font-size: 20px; }
.avatar-lg { width: 64px; height: 64px; font-size: 26px; }
.avatar-xl { width: 96px; height: 96px; font-size: 38px; }
```

---

## Accessibility
- ✅ `alt` 属性に氏名を入れる（写真）
- ✅ Fallback は `aria-label` で氏名を補足
- ✅ Focus ring は WCAG 2.1 AA 準拠（Drive 2px）

---

## Do / Don't

### ✅ Do
- 写真がある場合は 1:1 トリミング後に使用（顔中央）
- Fallback は **1文字** で十分（読みやすさ優先）
- Featured / 選択時にのみ Drive ボーダー

### ✕ Don't
- 装飾的な背景色（Sky色/Drive色背景フォールバック）にしない
- ボーダーをデフォルトでつけない
- 異なるAvatarサイズを並べない（リスト内は統一）

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `3. Primitives`
- **Component Set ID**: `53:32` ✅ 自動生成済（2026-05-12）
- 生成スキル: `figma-component-from-spec` v0.1
- **実装済 variants**: 20（`type` × `state` × `size`）
  - type: fallback (Deep + "F" initial) / photo (gray placeholder)
  - state: default / featured (Drive 2px outer border)
  - size: xs / sm / md / lg / xl
- **未実装（v0.3 で追加予定）**: focus ring、実写真フィル
- Variables バインド: color (deep/white/drive/bg-tertiary) / radius (pill) / border-width (thick)

## Change Log
- v0.2 (2026-04-20): Worksheet §9 確定
- v0.2-figma (2026-05-12): Figma Component Set 自動生成（20 variants）
