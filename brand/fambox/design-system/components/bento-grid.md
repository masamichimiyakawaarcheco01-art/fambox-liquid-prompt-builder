---
title: FAMBOX Component — Bento Grid
type: design-system
layer: L4-Components
component: BentoGrid
version: 0.2
status: confirmed
last_updated: 2026-04-28
owner: 宮川
deadline: 2026-05-29（OKR Task 2-1-a TOPページ DNA 反映）
source: Worksheet §21（2026-04-28 確定）+ Brand DNA v0.5 C-Bento グリッド仕様継承
brand_alignment:
  - Editorial × Lab（DNA メタファー）: Bento Grid + 部分ガラス
  - 主構図: 左下→右上の対角線（Editorial Variant で強制）
  - 強弱の DNA: 主役タイル 2×2 以上を最低 1 個
related:
  - components/bento-tile.md
  - components/card.md
  - tokens/spacing.md
  - tokens/colors.md
extensible: true  # v0.3 以降でカスタム Variant 追加余地あり
---

# Bento Grid — Component

## 概要

FAMBOX TOPページ主役の **Bento Tile を配置するグリッドシステム**。
**3 Variants × 12 column system** で構成。DNA v0.5 の Bento グリッド仕様を体系化。

L3 Bento Tile（**bento-tile.md**）と一体運用。Tile は単体で存在せず、必ず Bento Grid 内に配置される。

## ブランド整合性

- **Editorial × Lab**: Bento Grid 全体で「強弱・対角線・部分ガラス」を構成
- **Aesthetic 軸 主構図**: 左下→右上の対角線（Editorial Variant で強制）
- **強弱の DNA**: 主役タイル 2×2 以上を最低 1 個含む
- **Anti 回避**: 同サイズタイル並列 / 主役タイルなし / Gap 16px 未満 / 12 タイル以上 を禁止

---

## Variants（3 種 / 拡張可）

| Variant | クラス | 構造 | 使用例 |
|---|---|---|---|
| **Standard** | `bento-grid bento-grid-standard` | PC 12 col / Tablet 6 col / SP 1 col + 自由配置 | TOP / 一般 LP / ブランド訴求エリア |
| **Editorial** | `bento-grid bento-grid-editorial` | Standard + **主構図ルール強制**（対角線・主役 2×2 最低 1 個必須） | TOP 主役エリア・Brand DNA 反映ページ |
| **Auto-fit** | `bento-grid bento-grid-autofit` | タイル数に応じて自動配置（`grid-auto-flow: dense`） | KPI ギャラリー / 商品一覧 / Stat ダッシュボード |

### 拡張ルール（v0.3 以降）

新しい Bento Grid Variant が必要な場合は以下を満たす:
1. **Column 規律**: PC 12 column system（DNA 既定）/ Tablet 6 column / SP 1 column 縦並び
2. **Gap 規律**: SP 16px / Tablet 24px / PC 32px（DNA 既定）/ 16px 未満禁止
3. **強弱規律**: 主役タイル（2×2 以上）を最低 1 個含むこと（推奨基準）
4. **Tile 数上限**: 1 Bento Grid に 12 タイル以上配置しない
5. **命名**: `bento-grid bento-grid-{variant-name}`（kebab-case）

---

## Grid System（DNA v0.5 既定）

### PC（≥1024px）
- **12 column system**
- gutter（カラム間 grid-gap）: 32px（`--space-4`）
- baseline grid: 8px（`--grid-baseline`）
- 最大幅: `--container-max`（1440px）

### Tablet（768-1023px）
- **6 column system**
- gutter: 24px（`--space-3`）
- 2x1 / 1x2 / 2x2 タイルは 6 col 内で再配置

### SP（<768px）
- **1 column 縦並び**
- gutter: 16px（`--space-2`）
- 全タイルが `grid-column: span 1` に縮退（DNA 既定）

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);  /* PC */
  grid-auto-rows: minmax(160px, auto);     /* タイル最小高さ */
  gap: var(--space-4);                      /* PC 32px */
  width: 100%;
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 var(--space-3);
}

@media (max-width: 1023px) {
  .bento-grid {
    grid-template-columns: repeat(6, 1fr);  /* Tablet */
    gap: var(--space-3);                     /* 24px */
  }
}

@media (max-width: 767px) {
  .bento-grid {
    grid-template-columns: 1fr;             /* SP */
    gap: var(--space-2);                     /* 16px */
  }
}
```

---

## Gap Modifier（DNA 既定の上書き）

通常は `--space-4`/`--space-3`/`--space-2` の自動切替で十分だが、用途に応じて gap modifier で上書き可。

| Modifier | gap（全画面共通）| 用途 |
|---|---|---|
| `bento-gap--sm` | `--space-2`（16px） | 情報密度高（KPI ギャラリー等）|
| `bento-gap--md` ★既定 | `--space-3`（24px） | 標準 |
| `bento-gap--lg` | `--space-4`（32px） | 余白重視（Brand 訴求）|

```css
.bento-gap--sm { gap: var(--space-2); }
.bento-gap--md { gap: var(--space-3); }
.bento-gap--lg { gap: var(--space-4); }
```

---

## Editorial Variant の主構図ルール（Q5 A 採択 — 強制）

`bento-grid-editorial` を使う場合、以下の構造ルールを **必須** として運用:

### 必須条件
1. **主役タイル 2×2 以上を最低 1 個**含む（2×2 / 3×2 のいずれか）
2. **対角線配置**: 主役タイルを左上または左下に置き、視線を右上または右下へ誘導
3. **タイル数 4-9 個**を推奨（少なすぎ/多すぎは禁止）

### 推奨構図パターン

```
パターン A: 左下→右上 対角線（DNA 既定）
┌────────┬────────┬─────┐
│ 1×1    │ 1×1    │ 2×2 │
├────────┴────────┤     │
│ 2×1             │     │
├────────┬────────┴─────┤
│ 2×2 ★主役       │ 1×1│
│                 ├────┤
│                 │ 1×1│
└─────────────────┴────┘

パターン B: 左上→右下 対角線
┌────────────┬──────┬──────┐
│ 2×2 ★主役  │ 1×1  │ 1×1  │
│            ├──────┴──────┤
│            │ 2×1          │
├────────────┴──────────────┤
│ 3×2 ★主役（メガタイル）   │
│                            │
└────────────────────────────┘
```

### Lint 検出（推奨）
将来の DS バリデーター（v0.5 想定）で `bento-grid-editorial` の子要素を解析し以下を検出:
- 主役タイルなし → エラー
- 1×1 のみで構成 → 警告（強弱なし）
- タイル 12 個以上 → 警告（情報過剰）

---

## Liquid 実装例

### Standard（TOP 一般エリア）
```liquid
{% raw %}<section class="bento-grid bento-grid-standard">
  {% for block in section.blocks %}
    {%- liquid
      assign size = block.settings.tile_size | default: 'tile-1x1'
      assign variant = block.settings.tile_variant | default: 'bento-standard'
    -%}
    <article class="bento-tile {{ variant }} {{ size }}" {{ block.shopify_attributes }}>
      <h3 class="bento-tile__title">{{ block.settings.title }}</h3>
      <p class="bento-tile__text">{{ block.settings.body }}</p>
    </article>
  {% endfor %}
</section>{% endraw %}
```

### Editorial（TOP 主役エリア・対角線）
```liquid
{% raw %}<section class="bento-grid bento-grid-editorial bento-gap--lg">
  {%- comment -%} 左上 主役（2×2）{%- endcomment -%}
  <article class="bento-tile bento-glass bento-glass--3 tile-2x2"
           style="background-image: url('{{ section.settings.hero_image | img_url: '1200x' }}');">
    <p class="bento-tile__eyebrow">CASE</p>
    <h3 class="bento-tile__title">{{ section.settings.hero_title }}</h3>
    <p class="bento-tile__text">{{ section.settings.hero_summary }}</p>
    <a href="{{ section.settings.hero_url }}" class="btn btn-link">詳細を見る →</a>
  </article>

  {%- comment -%} 右上 Stat（1×1）{%- endcomment -%}
  <div class="bento-tile bento-stat-focus tile-1x1">
    <p class="bento-stat-focus__value">-3.2<span class="bento-stat-focus__unit">kg</span></p>
    <p class="bento-stat-focus__label">3 ヶ月で平均減量</p>
  </div>

  {%- comment -%} 右上 Standard（1×1）{%- endcomment -%}
  <article class="bento-tile bento-standard tile-1x1">
    <h3 class="bento-tile__title">{{ section.settings.tile2_title }}</h3>
    <p class="bento-tile__text">{{ section.settings.tile2_body }}</p>
  </article>

  {%- comment -%} 中央 横長（2×1）{%- endcomment -%}
  <article class="bento-tile bento-image-fill tile-2x1">
    <img src="{{ section.settings.tile3_image | img_url: '1200x' }}"
         alt="{{ section.settings.tile3_alt }}"
         class="bento-tile__media" loading="lazy">
    <div class="bento-tile__overlay">
      <h3 class="bento-tile__title">{{ section.settings.tile3_title }}</h3>
    </div>
  </article>

  {%- comment -%} 右下 メガタイル（3×2 ・主役 2 番目）{%- endcomment -%}
  <article class="bento-tile bento-glass bento-glass--4 tile-3x2"
           style="background-image: url('{{ section.settings.feature_image | img_url: '1800x' }}');">
    <p class="bento-tile__eyebrow">FEATURE</p>
    <h3 class="bento-tile__title">{{ section.settings.feature_title }}</h3>
    <p class="bento-tile__text">{{ section.settings.feature_body }}</p>
  </article>
</section>{% endraw %}
```

### Auto-fit（KPI ギャラリー）
```liquid
{% raw %}<section class="bento-grid bento-grid-autofit bento-gap--sm">
  {% for stat in section.settings.stats %}
    <div class="bento-tile bento-stat-focus tile-1x1">
      <p class="bento-stat-focus__value">
        {{ stat.value }}<span class="bento-stat-focus__unit">{{ stat.unit }}</span>
      </p>
      <p class="bento-stat-focus__label">{{ stat.label }}</p>
    </div>
  {% endfor %}
</section>{% endraw %}
```

---

## CSS（v0.2 実装）

```css
/* === Bento Grid 基本 === */
.bento-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-auto-rows: minmax(160px, auto);
  gap: var(--space-4);
  width: 100%;
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 var(--space-3);
}

@media (max-width: 1023px) {
  .bento-grid {
    grid-template-columns: repeat(6, 1fr);
    gap: var(--space-3);
  }
}

@media (max-width: 767px) {
  .bento-grid {
    grid-template-columns: 1fr;
    gap: var(--space-2);
  }
}

/* === Gap Modifiers === */
.bento-gap--sm { gap: var(--space-2); }
.bento-gap--md { gap: var(--space-3); }
.bento-gap--lg { gap: var(--space-4); }

/* === Variant: Standard === */
.bento-grid-standard {
  /* 基本系統 — 自由配置 */
}

/* === Variant: Editorial === */
.bento-grid-editorial {
  /* 主構図ルール強制（CSS では実現不可・人間 + Lint で運用）*/
  /* タイル間隔をやや大きめに（余白思想 TNF 級）*/
  gap: var(--space-4);
}

@media (max-width: 1023px) {
  .bento-grid-editorial { gap: var(--space-3); }
}

/* === Variant: Auto-fit === */
.bento-grid-autofit {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-auto-flow: dense;  /* 隙間なく自動配置 */
}

@media (min-width: 1024px) {
  .bento-grid-autofit {
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  }
}
```

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| `<section>` | Bento Grid 全体を囲む（landmark） |
| 見出し | Section 冒頭に `<h2>` でブロックタイトル（任意・省略可） |
| Tile 順序 | DOM 順 = 視覚順を保つ（grid-area で順序逆転しない） |
| キーボード Tab | DOM 順に従う / 主役タイルが最初に focus される設計 |
| SP 縦並び | DOM 順で 1 列に縦並び（理解しやすい）|
| reduced motion | hover 時の transform translateY を無効化 |

```css
@media (prefers-reduced-motion: reduce) {
  .bento-grid .bento-tile:hover {
    transform: none;
  }
}
```

---

## Do / Don't

### ✅ Do
- 1 つの Bento Grid 内で **強弱を必ずつける**（主役 + 脇役）
- Editorial Variant では **主構図ルール厳守**（対角線 + 主役 2×2 最低 1 個）
- Tile 数 **4-9 個**を目安にする（少なすぎ・多すぎ禁止）
- Gap は DNA 既定（SP 16 / Tablet 24 / PC 32）を基本に、`bento-gap--{sm/md/lg}` で調整
- SP では DOM 順で縦並びになることを意識して順序設計

### ✕ Don't（Q6 A 禁止リスト準拠）
- ❌ **同じサイズタイルを単調並列**（強弱なし・DNA Anti）
- ❌ **主役タイルなし**（Editorial Variant 必須条件違反）
- ❌ **Gap 16px 未満**（密度過剰・読みづらさ）
- ❌ **1 Bento Grid に 12 タイル以上**（情報過剰・認知負荷）
- ❌ Tile を Bento Grid 外で単独配置しない（Card Pattern を使うべき）
- ❌ Tablet で col-12 を col-3 にしない（DNA 規律違反 / 6 col に縮退すべき）
- ❌ SP 横スクロールに切り替えない（DNA 既定の縦並びを維持）

---

## Brand DNA との整合

| DNA 要素 | Bento Grid での体現 |
|---|---|
| Editorial × Lab | Bento + 部分ガラス（Glass Variant 経由）で雑誌的紙面構成 |
| 主構図 軸1（対角線）| Editorial Variant で必須・対角線パターン推奨 |
| 強弱（DNA 美学）| 主役タイル 2×2 以上 + 脇役 1×1 の組合せ |
| 余白思想 TNF 級 | gap PC 32px / `bento-gap--lg` で余裕を持たせる |
| 情報密度 中〜密 | Tile 4-9 個範囲で密度コントロール |

---

## L4 派生関係

| 派生 | 継承する Variant | 追加要素 |
|---|---|---|
| Hero 内 Bento ブロック | bento-grid-editorial（compact）| Hero overlay と整合 |
| KPI Dashboard | bento-grid-autofit | Stat-focus tile 群 |
| Product Showcase Grid | bento-grid-standard | Image-fill tile 主体 |

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `5. Components Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study`
- **Component Set ID**: `91:107` ✅ 新規生成（2026-05-12）
- 生成スキル: `figma-component-from-spec` + `figma-use`
- **実装済 variants**: 3（`variant`: standard / editorial / autofit）
- **レイアウト demo の構成**（placeholder rect で grid pattern を示す）:
  - **Standard** (936×520): 自由配置 — 2×1 / 1×1 × 2 / 1×1 / 3×1（5 tiles）
  - **Editorial** (1160×968): 対角線配置 — 2×2 主役（右上 Drive 枠）+ 3×2 主役（左下 Drive 枠）+ 1×1 × 4 + 2×1 × 2（9 tiles）
  - **Autofit** (936×520): KPI ギャラリー — 1×1 × 8 均等
- **主役タイル識別**: `card-featured` と同じく `--color-drive` 2px ストロークで視認可能
- **未実装（v0.3 で追加予定）**:
  - 各 variant 内の placeholder rect を **Bento Tile (`87:26`) Component instance に置換**
  - Tablet（6 col）/ SP（1 col 縦並び）の responsive variants
  - `bento-gap--sm/md/lg` modifier の Figma 表現

## Change Log
- v0.2-figma (2026-05-12): Figma Component Set `91:107` 新規生成（3 variants × placeholder grid demo）。Editorial で対角線パターン A を視覚化、主役タイルを Drive 2px 枠で識別。Bento Tile instance への置換は v0.3
- v0.2 (2026-04-28): Worksheet §21 確定（3 Variants / DNA 12-6-1 col システム / Gap 16-24-32 既定 + modifier / Editorial 主構図強制 / 4 禁止項目明示）。Brand DNA v0.5 C-Bento グリッド仕様を体系化
