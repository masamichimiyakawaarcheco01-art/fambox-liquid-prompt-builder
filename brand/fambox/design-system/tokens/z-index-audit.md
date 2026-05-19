---
title: z-index Existing Usage Audit & Layer Stack Proposal
type: design-system-reference
layer: L1-Tokens-Zindex
status: active
last_updated: 2026-04-20
owner: 宮川
purpose: 既存Shopifyテーマでの z-index 使用状況を可視化し、ZOZO Layer Stack 方式で FAMBOX DS の階層を再設計する
reference:
  - https://zenn.dev/zozotech/articles/7609d2c7af30df#layer-stack-のルール
---

# z-index — 既存監査 × Layer Stack 設計

Worksheet §4 への統合回答。**ZOZO Layer Stack 方式を採用**し、単純な数値＋`isolation: isolate` で衝突を根絶する方針に改訂。

---

## 1. 既存テーマの使用状況（監査）

### 使用分布

| z-index | 件数 | 主な用途 | 代表ファイル |
|---|---|---|---|
| -1 | 1 | 背景埋め込み | fam-solution |
| 0 | 34 | 基礎レイヤー | fam-voices, fambox-easy-cooking |
| **1** | **142** | **コンテンツ持ち上げ（最多）** | fam-item, fam-voices, fam-achievement |
| 2 | 53 | 写真・画像 | fam-item, fam-voices |
| 3 | 36 | タイトル画像 / ヘッダー推定 | fam-item, fam-corp-hero |
| 4 | 23 | CTAボタン / ヘッダー推定 | fam-item, fam-corp-hero |
| 5 | 27 | Hero文字 | fambox-hero, fambox-spirit |
| 6-10 | 34 | 複合演出 | fambox-hero |
| 15-20 | 6 | Hero動画重ね | fambox-hero-v17-video |
| **9990** | **2** | **Sticky CTA** | fam-sticky-cta |

### 発見事項（宮川さん指摘反映）

1. **実質 0〜10 で完結（95%以上）**。例外は `fam-sticky-cta` の 9990
2. **`fam-sticky-cta: 9990` の意図**: CTA上の最上位レイヤーとしてスティッキー表示を保持するため（宮川さん注記: 2026-04-20）
3. **🔑 重要制約**: **ヘッダー / ヘッダーメニューは sticky-cta より上に配置すること**（宮川さん指定）
4. **theme.liquid 側ヘッダーが z-index: 3-4** — これでは sticky-cta 9990 の下に埋もれている（設計ミス）
5. **統一規則がない**: セクションごとに場当たり的 → **Layer Stack 導入で根絶する**

---

## 2. ZOZO Layer Stack 方式の採用

### 核となる3原則（記事より）

1. **単純な小さな値で済ませる**: 1, 2, 3, 4... の連番で十分（1000/9999 不要）
2. **CSS 変数で一元管理**: `--layer-*` を tokens.css に集約、直書き禁止
3. **`isolation: isolate` で衝突回避**: セクションルートに付与してスタッキングコンテキストを作る → 内側の z-index が外に漏れない

### FAMBOX 採用版：6層スケール

**宮川さん制約（ヘッダー > sticky-cta）を満たしつつ ZOZO の思想を継承**。

```css
:root {
  /* Layer Stack（6階層・DS標準）*/
  --layer-base: 0;      /* 通常フロー（ほぼ使わない）*/
  --layer-1: 1;         /* 持ち上げ：バッジ・カード・ホバー浮上 */
  --layer-2: 2;         /* 浮遊要素：Tooltip・Popover・Accordion展開 */
  --layer-3: 3;         /* Sticky CTA（モバイル下部固定CTA）*/
  --layer-4: 4;         /* Sticky Header / Drawer（全体ナビ）*/
  --layer-5: 5;         /* Modal / Overlay（ヘッダーも覆う）*/
  --layer-6: 6;         /* Toast / Critical Alert（最前面）*/

  /* Legacy 互換枠（段階移行用・新規では使用禁止）*/
  --z-legacy-sticky-cta: 9990;  /* ⚠️ fam-sticky-cta のみ。v0.5で廃止予定 */
}
```

### 階層の意味

| Layer | 役割 | 具体例 | 上下関係の意図 |
|---|---|---|---|
| base (0) | 通常フロー | 普通のテキスト・画像 | z-index不要 |
| 1 | 持ち上げ | バッジ、Card影、ホバー浮上 | 通常より少し上 |
| 2 | 浮遊 | Tooltip, Popover, Dropdown | 内容より上・UI操作補助 |
| **3** | **Sticky CTA** | モバイル下部「話を聞く」バー | 内容より上・常駐操作 |
| **4** | **Sticky Header / Drawer** | グローバルナビ・ハンバーガー展開 | **Sticky CTA より上** ✅ |
| 5 | Modal / Overlay | 画面中央モーダル・確認ダイアログ | ヘッダーも暗転する |
| 6 | Toast / Critical | 成功・エラーのトースト通知 | 最前面（モーダル上）|

### `isolation: isolate` の運用ルール

**原則**: セクションルート（`<section>` タグ）には必ず `isolation: isolate` を付ける。

```css
/* 全 section に適用するベーススタイル */
.section-root {
  isolation: isolate;
}
```

**効果**: セクション内部で `z-index: 1-5` を使っても、外部の他セクションに影響しない。

**例**:
```liquid
{% raw %}<section class="section-root">
  <div class="hero-bg" style="z-index: 1;"></div>
  <div class="hero-text" style="z-index: 2;"></div>
  {# ↑ これらは他セクションの z-index と干渉しない #}
</section>{% endraw %}
```

---

## 3. 宮川さんの判断反映

### 論点1: ヘッダー vs sticky-cta
**確定**: ヘッダーは sticky-cta より上。→ Layer 4 に配置、sticky-cta は Layer 3 に配置。
- 既存 theme.liquid ヘッダー z-index 3-4 → Layer Stack 移行時に `var(--layer-4)` で統一
- 既存 fam-sticky-cta z-index 9990 → Layer Stack 移行時に `var(--layer-3)` へ刷新

### 論点2: fam-sticky-cta 9990
**確定**: レガシー互換枠 `--z-legacy-sticky-cta: 9990` として一時保持。v0.5 までに `var(--layer-3)` へ完全移行。

### 論点3: Announcement Bar / Chat Widget
- **Announcement Bar**: ヘッダーよりは下、Sticky CTA より上 → 既存Layerでは **Layer 3** で良い（sticky-cta と同レイヤー・ただし画面上/下で別位置）
- **Chat Widget (Shopify inbox 等)**: Sticky CTA 相当 → **Layer 3** で良い

→ 新規Alias追加は不要。**意味参照はコンポーネント側の命名で担保**（例: `.announcement-bar { z-index: var(--layer-3); }`）

---

## 4. 採用する tokens.css 改訂（v0.3向け）

```css
/* ============================================================
 * Z-INDEX — Layer Stack 方式（ZOZO 準拠）
 * 原則: セクションルートに isolation: isolate を必ず付与
 *       直書き z-index は禁止、必ず --layer-* を使う
 * ============================================================ */
--layer-base: 0;
--layer-1: 1;
--layer-2: 2;
--layer-3: 3;      /* Sticky CTA */
--layer-4: 4;      /* Sticky Header / Drawer */
--layer-5: 5;      /* Modal / Overlay */
--layer-6: 6;      /* Toast */

/* Legacy 互換（v0.5で廃止予定）*/
--z-legacy-sticky-cta: 9990;
```

---

## 5. 移行計画

| Phase | 期限 | 作業 |
|---|---|---|
| **v0.3** | 2026-05-15 | tokens.css に Layer Stack 追加、`isolation: isolate` 運用ルール策定 |
| **v0.4** | 2026-06-30 | 新規セクション（DS Phase B以降）はすべて Layer Stack 使用 |
| **v0.5** | 2026-09-30 | 既存 fam-sticky-cta を Layer 3 へ刷新、theme.liquid ヘッダーを Layer 4 へ刷新 |
| **v1.0** | 2026-12 | Legacy 互換枠削除、Layer Stack のみで統一 |

---

## 6. コンポーネント別 Layer 対応表

| コンポーネント | Layer | CSS例 |
|---|---|---|
| バッジ | 1 | `z-index: var(--layer-1)` |
| カード影・浮上 | 1 | `z-index: var(--layer-1)` |
| Tooltip / Popover | 2 | `z-index: var(--layer-2)` |
| Accordion 展開部 | 2 | `z-index: var(--layer-2)` |
| Sticky CTA（下部固定）| 3 | `z-index: var(--layer-3)` |
| Announcement Bar（上部）| 3 | `z-index: var(--layer-3)` |
| Chat Widget | 3 | `z-index: var(--layer-3)` |
| **Sticky Header** | **4** | `z-index: var(--layer-4)` |
| **Drawer（SP Menu）** | **4** | `z-index: var(--layer-4)` |
| Modal / Dialog | 5 | `z-index: var(--layer-5)` |
| Full-screen Overlay | 5 | `z-index: var(--layer-5)` |
| Toast Notification | 6 | `z-index: var(--layer-6)` |
| Critical Alert | 6 | `z-index: var(--layer-6)` |

---

## 7. 宮川さんの確認項目

- [x] 論点1: ヘッダー > Sticky CTA → **確定**（Layer 4 vs Layer 3 で実現）
- [x] 論点2: fam-sticky-cta 9990 → **確定**（Legacy枠で一時保持、v0.5で Layer 3 へ刷新）
- [x] 論点3: Announcement Bar / Chat Widget → **新Alias不要**（Layer 3 に統合）
- [ ] Layer Stack 6層案（1-6）の採用確認: [ 回答: 採用 / 微調整 / 別案 ]
- [ ] `isolation: isolate` をセクションルートに強制するルール採用: [ 回答: ]

---

## 8. 参考

- ZOZO Tech Blog — [Layer Stack のルール](https://zenn.dev/zozotech/articles/7609d2c7af30df#layer-stack-のルール)
  - 本記事の4層構造（1-4）を6層に拡張して採用
  - `isolation: isolate` によるスタッキングコンテキスト生成の手法を全面採用
