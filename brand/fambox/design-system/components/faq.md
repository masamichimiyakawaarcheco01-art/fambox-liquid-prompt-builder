---
title: FAMBOX Component — FAQ
type: design-system
layer: L4-Components
component: FAQ
version: 0.2
status: confirmed
last_updated: 2026-05-12
owner: 宮川
source: 実装計画書 §7 並行作業（5/20 期限）+ preview-faq.html 一次実装 + Tier 3 `fambox-faq` (433 lines) 抽出
brand_alignment:
  - Editorial（読み物）: 32×2 黒線のキャラクターラインで Q/A を構造化
  - Scroll-driven（縦長煩雑を避ける）: 横スクロールで「読みたいだけ読む」設計
  - Co-driven（対等）: Avatar で「質問者」を可視化、上から目線の Q&A にしない
  - Integrity: 全 Q&A を畳まず露出、隠す Accordion を Default にしない
  - Anti: Accordion-only / FAQ にバッジ訴求 / Drive 色を質問文に使う 禁止
related:
  - components/card.md
  - components/avatar.md
  - tokens/typography.md
  - tokens/colors.md
extensible: true  # v0.3 以降で Accordion variant を追加可能
---

# FAQ — Component

## 概要

「よくあるご質問」を **カード型・横スクロール** で並べる L4 Component。
全 Q&A を畳まずに露出することで、ユーザーが「読みたい順」「気になる順」で水平に走査できる構造を維持する。Accordion を Default にしない理由は、本 DNA が **Editorial（読み物）×Scroll-driven** であり、情報を隠す Accordion はその逆を行くため。

**2 Variants**（v0.2 時点では Carousel のみ confirmed、Accordion は v0.3 以降）。

## ブランド整合性

- **Editorial**: `32px × 2px` の黒キャラクターラインで Q / A を視覚分離（直線・装飾なし）
- **Scroll-driven**: 縦の重みを増やさず、ユーザーが横にめくる主導権
- **Co-driven**: 40×40 Avatar が「質問者」役として残り、Q&A の「対等性」を示す
- **Integrity**: A は Drive `#FC5214` で強調するが、決して誇張せず短文で答える
- **Anti 回避**: Accordion-only / 「驚き！」「○○％ お得」等の煽り FAQ / 全部 Drive 色での Q 強調 を踏まない

---

## Variants（2 種 / 拡張可）

| Variant | クラス | 構造 | 使用例 |
|---|---|---|---|
| **Carousel** ✅ confirmed | `faq faq-carousel` | カード横スクロール（4-8 枚）| TOPページ 末尾 / LP 末尾 |
| **List Accordion** ⚠ v0.3 | `faq faq-list-accordion` | 縦リスト + 折りたたみ | `/pages/faq`（FAQ 専用ページ、20+ Q&A） |

### 拡張ルール（v0.3 以降）

新 Variant 追加時は以下を満たす:
1. **Q/A の対比構造**: 32×2 黒線（または Drive 線）で Q と A を分離すること
2. **Avatar 表示**: Q の上に 40×40 Avatar（または icon）を必須配置
3. **A 強調色**: 必ず `--color-drive` を使う（質問は Ink 黒）
4. **Anti**: Q を Drive 色で塗らない / 全 Q&A を Accordion で完全隠蔽しない
5. **命名**: `faq faq-{variant-name}`（kebab-case）

---

## サイズ仕様

### Carousel

| 要素 | PC（≥768px） | SP（<768px） |
|---|---|---|
| Section padding | `--space-7`（64px）上下 | `--space-7`（64px）上下 |
| Title 左 padding | `--space-7`（64px）/ max-width 1440 中央寄せ | `--space-3`（16px） |
| Scroll track 左 padding | `max(64px, (100% − 1440) / 2 + 64)` | `--space-3`（16px） |
| カード幅 | **320px 固定** | `calc(100vw − 80px)`（画面横一杯近く） |
| カード間 gap | `--space-5`（32px）| `--space-5`（32px）|
| Title → スクロール余白 | `--space-6`（56px）| `--space-6`（56px）|
| Scroll snap | なし（自由スクロール）| `scroll-snap-type: x mandatory` |

### Carousel — カード内部

| 要素 | 値 | Token |
|---|---|---|
| Avatar | 40 × 40 円 / `--bg-tertiary` placeholder | `--radius-pill` |
| Q 番号（Question 1）→ Avatar 余白 | 16px | `--space-2` |
| Q 番号 → 質問文 余白 | 24px | `--space-3` |
| 質問文 → 黒線 余白 | 24px | `--space-3` |
| 黒線 → 回答 余白 | 24px | `--space-3` |
| 回答 → ロゴ 余白 | 32px | `--space-5` |
| 黒線 | 32 × 2 / `--color-ink` | （直書き許容、char-line 専用）|
| ロゴ高さ | 32px | - |

---

## 共通 Props

| プロパティ | 値 |
|---|---|
| Section 背景 | `--bg-secondary`（#fafafa）|
| カード背景 | 透明（カード自体に塗りなし）|
| Q 番号 フォント | `--font-en`（Poppins）|
| Q 番号 サイズ | `--fs-h3`（24px）/ 600 |
| Q 番号 カラー | `--color-ink` |
| 質問文 フォント | `--font-ja` |
| 質問文 サイズ | `--fs-lg`（PC 18-20px）/ 600 / `line-height: 170%` |
| 質問文 カラー | `--color-ink` |
| 回答文 サイズ | `--fs-lg`（PC 18px、SP 16px）/ 500 / `line-height: 170%` |
| 回答文 カラー | **`--color-drive`**（`#FC5214`）— DNA で Drive 強調を許可する唯一の本文要素 |
| カラム数 | 4-8 枚推奨（少なすぎず多すぎず）|

---

## 構造（HTML）

```html
<section class="faq faq-carousel">
  <div class="faq__inner">

    <!-- Title -->
    <div class="faq__title-area">
      <h2 class="faq__title">よくあるご質問</h2>
    </div>

    <!-- Scroll area -->
    <div class="faq__scroll-area">
      <div class="faq__scroll-track">

        <article class="faq__card">
          <div class="faq__avatar" aria-hidden="true">
            <!-- Avatar v0.2: fallback / photo どちらも可 -->
          </div>
          <p class="faq__q-number">Question 1</p>
          <p class="faq__question">FAMBOX はどのような食事ですか？</p>
          <hr class="faq__line" aria-hidden="true" />
          <p class="faq__answer">FAMBOX はスポーツ栄養学に基づいた冷凍宅配食です。…</p>
          <div class="faq__logo">
            {%- render 'logo-fambox', size: 32 -%}
          </div>
        </article>

        <!-- 必要数繰り返し -->

      </div>
    </div>

  </div>
</section>
```

---

## CSS（v0.2 実装）

```css
/* === Section === */
.faq {
  width: 100%;
  background: var(--bg-secondary);
  position: relative;
}

.faq__inner {
  padding-block: var(--space-7);  /* 64px */
}

/* === Title === */
.faq__title-area {
  max-width: 1440px;
  margin-inline: auto;
  padding-inline: var(--space-7);  /* 64px */
}

.faq__title {
  font-family: var(--font-ja);
  font-weight: var(--fw-semibold);
  font-size: var(--fs-h2);  /* 32px */
  line-height: 1.8;
  color: var(--color-ink);
  letter-spacing: var(--ls-ja);
}

/* === Scroll area === */
.faq__scroll-area {
  width: 100%;
  margin-top: var(--space-6);  /* 56px */
  overflow-x: auto;
  overflow-y: hidden;
  scrollbar-width: none;
  -ms-overflow-style: none;
  -webkit-overflow-scrolling: touch;
}

.faq__scroll-area::-webkit-scrollbar { display: none; }

.faq__scroll-track {
  display: flex;
  gap: var(--space-5);  /* 32px */
  padding-left: max(var(--space-7), calc((100% - 1440px) / 2 + var(--space-7)));
  padding-right: max(0px, calc((100% - 1440px) / 2));
}

/* === Card === */
.faq__card {
  flex: 0 0 320px;
  width: 320px;
  display: flex;
  flex-direction: column;
}

.faq__avatar {
  width: 40px;
  height: 40px;
  border-radius: var(--radius-pill);
  background: var(--bg-tertiary);
}

.faq__q-number {
  font-family: var(--font-en);
  font-weight: var(--fw-semibold);
  font-size: var(--fs-h3);  /* 24px */
  color: var(--color-ink);
  margin-top: var(--space-2);  /* 16px */
}

.faq__question {
  font-family: var(--font-ja);
  font-weight: var(--fw-semibold);
  font-size: var(--fs-lg);  /* 18-20px */
  line-height: 1.7;
  color: var(--color-ink);
  margin-top: var(--space-3);  /* 24px */
}

.faq__line {
  width: 32px;
  height: 2px;
  background: var(--color-ink);
  border: 0;
  margin: var(--space-3) 0 0;  /* 24px top */
}

.faq__answer {
  font-family: var(--font-ja);
  font-weight: var(--fw-medium);
  font-size: var(--fs-lg);  /* 18px */
  line-height: 1.7;
  color: var(--color-drive);  /* #FC5214 — DNA 例外的に許容 */
  margin-top: var(--space-3);  /* 24px */
}

.faq__logo {
  margin-top: var(--space-5);  /* 32px */
  height: 32px;
  display: flex;
  align-items: center;
}

/* === SP === */
@media (max-width: 767px) {
  .faq__title-area { padding-inline: var(--space-3); }
  .faq__title { font-size: var(--fs-h3); }  /* 24px */

  .faq__scroll-area {
    scroll-snap-type: x mandatory;
    scroll-padding-left: var(--space-3);
  }
  .faq__scroll-track {
    padding-left: var(--space-3);
    padding-right: var(--space-3);
  }
  .faq__card {
    flex: 0 0 calc(100vw - 80px);
    width: calc(100vw - 80px);
    scroll-snap-align: start;
    scroll-snap-stop: always;
  }
  .faq__question,
  .faq__answer { font-size: var(--fs-body); }  /* 16px */
}

/* === reduced motion === */
@media (prefers-reduced-motion: reduce) {
  .faq__scroll-area { scroll-behavior: auto; }
}
```

---

## Liquid 実装例（Carousel）

```liquid
{% raw %}<section class="faq faq-carousel" data-gtag-section="faq">
  <div class="faq__inner">

    <div class="faq__title-area">
      <h2 class="faq__title">{{ section.settings.title | default: "よくあるご質問" }}</h2>
    </div>

    <div class="faq__scroll-area" tabindex="0" aria-label="FAQ カード一覧（横スクロール）">
      <div class="faq__scroll-track">
        {%- for block in section.blocks -%}
          {%- if block.type == 'faq_item' -%}
            <article class="faq__card" {{ block.shopify_attributes }}>
              <div class="faq__avatar" aria-hidden="true">
                {%- if block.settings.avatar_image != blank -%}
                  <img src="{{ block.settings.avatar_image | image_url: width: 80 }}"
                       width="40" height="40" alt="" loading="lazy">
                {%- endif -%}
              </div>
              <p class="faq__q-number">Question {{ forloop.index }}</p>
              <p class="faq__question">{{ block.settings.question }}</p>
              <hr class="faq__line" aria-hidden="true" />
              <p class="faq__answer">{{ block.settings.answer }}</p>
              <div class="faq__logo">
                {%- render 'logo-fambox', size: 32 -%}
              </div>
            </article>
          {%- endif -%}
        {%- endfor -%}
      </div>
    </div>

  </div>
</section>{% endraw %}
```

---

## Schema（参考）

```json
{
  "name": "FAQ",
  "tag": "section",
  "class": "faq faq-carousel",
  "settings": [
    { "type": "text", "id": "title", "label": "セクション見出し", "default": "よくあるご質問" }
  ],
  "blocks": [
    {
      "type": "faq_item",
      "name": "FAQ 項目",
      "limit": 12,
      "settings": [
        { "type": "image_picker", "id": "avatar_image", "label": "質問者アバター（任意）" },
        { "type": "text", "id": "question", "label": "質問", "default": "FAMBOX はどんな食事？" },
        { "type": "textarea", "id": "answer", "label": "回答", "default": "スポーツ栄養学に基づいた冷凍宅配食です。" }
      ]
    }
  ],
  "presets": [{ "name": "FAQ", "blocks": [{ "type": "faq_item" }, { "type": "faq_item" }, { "type": "faq_item" }, { "type": "faq_item" }] }]
}
```

---

## States

| State | クラス / 挙動 |
|---|---|
| default | 表示中（全カード視認可） |
| scrolling | ユーザー操作中。SP は `scroll-snap` で自動スナップ |
| focus（キーボード） | カード内最初のリンク／ボタンが focus 可視。scroll-area 自体にも `tabindex="0"` |
| hover（PC） | カード内テキストにアンダーラインや色変化を **付けない**（Editorial 維持） |

> ❗ Anti: hover で背景色を変えたり影を増やしたりしない。Editorial 紙面の読み心地を維持する。

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| `<section>` ランドマーク | `aria-labelledby` で `.faq__title` を参照（id 付与）|
| 横スクロール | `.faq__scroll-area` に `tabindex="0"` + 矢印キー横スクロール対応（ブラウザ標準）|
| Avatar | 装飾なら `aria-hidden="true"`、人物写真ありなら `alt=""`（質問者名は本文に書く）|
| 線（hr）| `aria-hidden="true"` で AT 読み上げ抑制 |
| Drive 色の回答 | コントラスト比 4.5:1 を `--bg-secondary` 上で確認（`#FC5214` on `#fafafa` ≈ 4.6:1 ✅）|
| ロゴ | `<svg>` 内で `aria-label="FAMBOX"` または隣接テキスト |
| SP 横スクロール | `scroll-snap` で 1 枚ずつ確実に止まる（動きが速すぎる Anti を回避）|
| `prefers-reduced-motion` | `scroll-behavior: auto` で滑らかスクロールを無効化 |

---

## Do / Don't

### ✅ Do
- カード幅 320px 固定 / gap 32px / 32×2 黒線 を厳守
- 回答（A）にだけ `--color-drive` を使い、質問（Q）は Ink 黒
- Avatar を「質問者」として残し、Co-driven の対等性を可視化
- SP は `scroll-snap-type: x mandatory` で 1 枚送り
- 全 Q&A を畳まず露出（Carousel 形式の本質）
- ロゴは各カード末尾に配置（FAMBOX が「回答者」であることを示す）

### ✕ Don't
- ❌ **Default を Accordion にする** — DNA: Editorial × Scroll-driven の真逆。Accordion は v0.3 で `/pages/faq` 専用のみ
- ❌ **質問（Q）を Drive 色で塗る** — 強調点が散る。Drive は A の専有
- ❌ **「驚き！」「○○％ お得」等の煽り FAQ** — Integrity 違反
- ❌ **カードに hover で色 / 影変化** — 紙面の読み心地を壊す
- ❌ **8 枚超のカード**（横スクロールが過剰に長い）— 8 枚を超える場合は別ページへ
- ❌ **黒線 32×2 を別寸法に変更** — このキャラクターラインは FAMBOX の Editorial 識別子の一つ

---

## Brand DNA Anti との照合

本コンポは以下の Anti を踏まない:
- 派手・煽り → Drive 色は A のみ、見出しと Q はモノトーン
- 隠す（Accordion）→ Default で全 Q&A 露出
- 媚びる → 質問者 Avatar の対等表示で「お客様」非対称構造を解消

---

## L4 派生関係

| 派生 | 継承する Variant | 追加要素 |
|---|---|---|
| `/pages/faq` 専用ページ | Accordion（v0.3）| 検索ボックス / カテゴリ Tab / `<details>` ベース |
| Spirit Carousel（既存 preview-spirit-carousel.html）| Carousel と兄弟関係 | 同じ scroll-track 機構 / カード中身が異なる |
| Voice Bento（fam-voices）| Carousel と分離 | Bento Grid 構造で別 L4 |

---

## 実装計画書との対応

- 計画書 §1 Tier 3: `fambox-faq` (433 lines) → 本 Spec の **Carousel Variant** へ書き換え
- 計画書 §7 並行作業: 「L4 FAQ Accordion」期限 5/20 → **L4 FAQ Component（Carousel + Accordion 拡張枠）として 2026-05-12 に Spec 化完了**
- Accordion variant は v0.3 で別途、`/pages/faq` の長文 FAQ 用に追加

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `5. Components Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study`
- **Component Set ID**: `93:90` ✅ 新規生成（2026-05-12 Session #6）
- 生成スキル: `figma-component-from-spec` + `figma-use`
- **実装済 variants**: 1（`variant`: carousel）/ Accordion は v0.3 拡張枠で保留
- **構造**:
  - Section bg: `bg/secondary` (#FAFAFA)、padding 64px (上下) × 64px (左右)
  - Title: 「よくあるご質問」Noto Sans JP Bold 32px Ink、margin-bottom 56px
  - Scroll track: 横並び 4 cards、gap 32px
  - 各 card 320 wide × auto height:
    - Avatar 40×40 円（`bg/tertiary` placeholder）
    - Question N（Poppins SemiBold 24 Ink）
    - 質問文（Noto Sans JP Bold 18 Ink、line-height 170%）
    - 黒線 32×2（`ink/ink` 直値）
    - 回答文（Noto Sans JP Regular 18 **Drive**、line-height 170%）
    - FAMBOX ロゴ placeholder（80×32 灰色 + テキスト）
- **未実装（v0.3 で追加予定）**:
  - Accordion variant（`/pages/faq` 長文 FAQ 専用）
  - SP layout（card 幅 calc(100vw - 80px) / scroll-snap）
  - Avatar に実画像 fill bind
  - hover state（spec で hover 動作はないが、focus-visible は要）

## Change Log
- v0.2-figma (2026-05-12): Figma Component Set `93:90` 新規生成（Carousel variant のみ）。4 card sample 構造で Q/A 対比、Drive 強調、黒線キャラクターラインを実装
- v0.2 (2026-05-12): preview-faq.html を一次資料に Carousel Variant を Spec 化。実装計画書の「Accordion」表記を DNA 整合のため Carousel が Default、Accordion は v0.3 拡張 と再定義
