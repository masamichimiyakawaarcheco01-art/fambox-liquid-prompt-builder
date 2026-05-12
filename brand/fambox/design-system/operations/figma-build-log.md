---
title: FAMBOX Design System — Figma Build Log
type: operations
last_updated: 2026-05-12
purpose: Markdown仕様→Figma Component の自動生成履歴。スキル「figma-component-from-spec」で実施した各セッションの記録。
---

# Figma Build Log

`figma-component-from-spec` スキル経由で行った Markdown → Figma 自動生成の履歴。
発生した問題・修復内容も記録（再発防止のナレッジ蓄積）。

---

## Session 2026-05-12 — L2 Primitives 一括構築

**契機**: Marc-Antoine（外部デザイナー）の Smart City Kit 制作プロセスを学習。
Marc流4層スタック（L1 Transport / L2 Skill / L3 Tokens / L4 CLAUDE.md / L5 Audit-first）を
FAMBOX に翻訳・適用した最初のセッション。

### 成果

| Component | Variants | Component Set ID | Page | Notes |
|---|---|---|---|---|
| Button | 15 (5 variant × 3 size) | `46:32` | 3. Primitives | default state only。hover/disabled/loading/icon は v0.3 で追加 |
| Input | 12 (3 variant × 4 state) | `50:26` | 3. Primitives | underline / bordered / textarea × default/focus/disabled/error |
| Avatar | 20 (2 type × 2 state × 5 size) | `53:32` | 3. Primitives | fallback("F") / photo(gray placeholder) × default/featured × xs..xl |
| Form Controls | 9 (3 kind × 3 state) | `54:16` | 3. Primitives | checkbox / radio / toggle × default/checked-or-on/disabled |
| Progress Bar | 5 (5 value) | `55:11` | 3. Primitives | value=0/25/50/75/100 |
| Spinner | 3 (3 size) | `55:21` | 3. Primitives | sm/md/lg。arcData による 75% 円弧 |

**合計**: 64 variants、推定 280+ Variable バインド、約 60 分。

### 発生問題と修復

#### 🐛 Issue 1: alias Variables 12 個が純白に固まっていた（最大発見）
- **症状**: Button Link variant のテキスト色が drive オレンジにならず白に
- **原因**: Tokens Studio から `{color.brand.drive}` 等の alias 参照が import 時に解決失敗、
  全 alias 系 Variables が静的 `{r:1, g:1, b:1, a:1}` に固定化
- **影響範囲**: `cta` / `focus-ring` / `link-on-light` / `link-on-dark` / `link-on-drive` /
  `link-hover` / `data/primary` / `data/secondary` / `data/tertiary` /
  `data/zone-good` / `data/zone-caution` / `data/zone-danger`
- **修復**: `setValueForMode` で正しい VARIABLE_ALIAS に再接続（12 件）
- **再発防止**: `figma-component-from-spec` SKILL の Step 1 に alias 健全化スクリプトを必須化

#### 🐛 Issue 2: Textarea の placeholder テキストが縦書きで wrap
- **症状**: 1 文字ずつ縦に並んで描画
- **原因**: `figma.createText()` の初期 width が極小、`textAutoResize='HEIGHT'` で固定された
- **修復**: `appendChild` 後に `resize(innerWidth, height) → textAutoResize='HEIGHT' →
  layoutSizingHorizontal='FILL'` の順で再設定
- **再発防止**: 多行テキストは作成順序が重要、SKILL ドキュメントに明記

### Known TODOs

- **Button v0.3**: hover / disabled / loading state + Icon variants（with-icon / icon-only）
- **Input v0.3**: hover / active state、必須バッジ表示
- **Avatar v0.3**: focus ring（WCAG 2.1 AA）、写真フィル実装
- **Form Controls v0.3**: focus / hover state、Toggle 影の量感調整
- **Progress Circular**: arc 描画（vectorPath による SVG path）— Circular Progress 全体が未着手
- **Spinner v0.3**: 円弧の見た目を CSS 仕様に近づける（pie ではなく純粋な arc curve）

### 使用した Variables（主要）

```
FAMBOX/color/brand/drive          (Primary CTA)
FAMBOX/color/brand/deep           (Avatar fallback bg)
FAMBOX/color/ink/ink              (本文)
FAMBOX/color/ink/white            (反転テキスト)
FAMBOX/color/ink/placeholder      (Disabled / Empty)
FAMBOX/color/bg/primary           (Input bg)
FAMBOX/color/bg/tertiary          (Disabled bg / Photo placeholder)
FAMBOX/color/border/base          (Input default border)
FAMBOX/color/border/light         (Disabled border)
FAMBOX/color/semantic/error       (Input error border)
FAMBOX/color/alias/link-on-light  (Link text — 修復後)
FAMBOX/radius/sm                  (Checkbox 4px)
FAMBOX/radius/md                  (Input bordered 8px)
FAMBOX/radius/pill                (Avatar / Toggle / Spinner)
FAMBOX/radius/pill-cta            (Button)
FAMBOX/border-width/thin          (Input 1px)
FAMBOX/border-width/thick         (Button outline / Featured Avatar 2px)
FAMBOX/typography/font-size/body-sm   (Button sm 14px)
FAMBOX/typography/font-size/body      (Button md / Input 16px)
FAMBOX/typography/font-size/lg        (Button lg 20px)
```

### 学んだこと

1. **Audit-first protocol は実効性が高い**: Step 0 で既存資産を確認することで重複生成と
   隠れバグ（alias 破損）を早期発見。Marc流ノウハウの即時実証。

2. **テキスト描画は順序依存が大きい**: `loadFontAsync → createText → characters →
   appendChild → layoutSizing` の順序を守らないと描画ミスする。

3. **MVP→拡張 が正解**: 状態×サイズ×バリアントを 30 超で一気に作るより、
   default state のみで先に variant 構造を確立してから state を追加するほうが
   失敗コストが低い。

4. **Hiragino Sans は Figma に無い**: `Noto Sans JP` で代替。CSS と完全一致は
   できないが、visual fidelity は実用範囲。

---

## 次回セッション着手候補

優先順:
1. **Button v0.3 拡張**: hover/disabled/Icon variants で完全体化
2. **Patterns L3** に進む: `form-field.md` `card.md` の組合せ系
3. **Header / Footer**: ナビゲーション系 Component
4. **Hero Section**: LP 主役 Template
