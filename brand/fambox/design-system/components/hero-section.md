---
title: FAMBOX Component — Hero Section
type: design-system
layer: L4-Components
component: HeroSection
version: 0.2
status: confirmed
last_updated: 2026-04-28
owner: 宮川
deadline: 2026-05-29（OKR Task 2-1-a TOPページ DNA 反映）
source: Worksheet §17（2026-04-28 確定）+ 既存 Liquid 実測（fam-corp-hero / fambox-hero-v17-video / fam-blog-hero）
brand_alignment:
  - Editorial × Lab（DNA メタファー）: NBA HOOP 型タイポ重ねで Editorial 表現
  - Integrity（誠実）: Drive 色ベタ塗り禁止・派手フィルタ禁止
  - 余白思想 TNF 級: padding `--space-7`〜`--space-8`
related:
  - components/button.md
  - components/card.md
  - tokens/colors.md
  - tokens/motion.md
extensible: true  # v0.3 以降でカスタム Variant 追加余地あり
---

# Hero Section — Component

## 概要

FAMBOX の各画面冒頭に配置する主役 Component。**4 Variants × 3 Heights** で構成。
NBA HOOP 型タイポ重ね（任意）/ 余白 TNF 級 / パララックス対応 を Brand DNA v0.5 から継承。

## ブランド整合性

- **Editorial × Lab**: 写真 / 動画 + タイポの重ね合わせで Editorial 表現（NBA HOOP 型・任意）
- **TNF 級余白**: PC `--space-8`（160px）/ SP `--space-7`（96px）を vertical padding の最低基準
- **Integrity**: Drive 色を背景全面に使わない、派手フィルタ・装飾過多禁止
- **Anti**: 動画 + 派手フィルタ重ね / Pill 以外の CTA / Primary 2 個並列 を禁止

---

## Variants（4 種 / 拡張可）

| Variant | クラス | 構造 | 使用例 |
|---|---|---|---|
| **Video Fullscreen** | `hero hero-video-fullscreen` | 全画面動画背景 + Logo + Title + Text + CTA | TOP / Blog Top（fam-corp-hero / fam-blog-hero 継承）|
| **Video Split** | `hero hero-video-split` | 左右分割動画 + 4 Corner Icons + 中央テキスト | キャンペーン LP（fambox-hero-v17 継承）|
| **Image Editorial** | `hero hero-image-editorial` | 静止画 + タイポ Editorial 配置（NBA HOOP モード ON/OFF 可） | 食事診断 / Subscription LP / About |
| **Minimal Text** | `hero hero-minimal-text` | 装飾なし・大型タイポ + サブ + CTA（任意） | 社内ページ / 告知 / FAQ |

### 拡張ルール（v0.3 以降）

新しい Hero Variant が必要な場合は以下を満たす:
1. **TNF 級余白**: vertical padding 最低 PC 96px / SP 64px（`--space-7` 以上）
2. **CTA 規律**: Primary は 1 個まで（Q6 A 禁止リスト準拠）
3. **DNA Anti を踏まない**: Drive 色全面ベタ塗り / 派手フィルタ / Pill 以外の CTA 禁止
4. **命名**: `hero hero-{variant-name}`（kebab-case）

---

## Heights（3 段階・modifier クラスで切替）

| Modifier | min-height | 使用文脈 |
|---|---|---|
| `hero--full` ★既定 | 100vh | TOP / 主要 LP |
| `hero--tall` | 70vh | カテゴリページ / 中継ぎ Hero |
| `hero--compact` | 40vh | FAQ / 規約 / 社内ページ |

```css
.hero { min-height: 100vh; }     /* 既定 = full */
.hero--full { min-height: 100vh; }
.hero--tall { min-height: 70vh; }
.hero--compact { min-height: 40vh; }
```

### Height 選択フロー

```
このページは UX 上「主役級」？
├─ Yes（TOP / 主要 LP）→ hero--full（100vh）
└─ No → コンテンツ密度は？
        ├─ 中（カテゴリ / 中継ぎ）→ hero--tall（70vh）
        └─ 低（情報ページ）       → hero--compact（40vh）
```

---

## CTA 運用（0〜2・Q3 C 採択）

CTA 個数は **0 / 1 / 2** から文脈で選択。

| 個数 | 使用例 | 配置 |
|---|---|---|
| **0** | FAQ Hero / 告知 / About 冒頭 | テキストのみ |
| **1** | TOP / 主要 LP（Primary 1 個）| Title 下に Primary |
| **2** | Subscription LP（Primary + Secondary）| 横並び（PC）/ 縦積み（SP） |

### Anti-pattern（Q6 A 禁止リスト）

| 禁止事項 | 理由 |
|---|---|
| ❌ **動画 + 派手フィルタ重ね**（彩度を意図的に上げる、color burn 等のブレンド多用）| Brand DNA Anti「派手・エセ高級」違反 |
| ❌ **Drive 色背景での全画面ベタ塗り**（`background: var(--color-drive)` 全面）| Drive は CTA 専用、面で使うとうるさい |
| ❌ **Hero 内 CTA を Primary 2 個以上**（Primary は 1 個のみ）| 階層崩壊・迷い増加 |
| ❌ **Pill 形状以外の CTA**（角張りボタン / Underline-only 大型ボタン等）| Button v0.3 規律違反 |

---

## NBA HOOP モード（Q4 B 採択 — 任意 ON/OFF）

`hero-image-editorial` および互換 Variant で **modifier `is-hoop`** を付けるとタイポが画像と重なる Editorial 表現になる。

### `is-hoop` ON（Editorial 重ね）
```
   ┌──────────────────┐
   │ ASTHLETE         │  ← Title 上端が画像上端と重なる（部分はみ出し）
   │ ┌──────────────┐ │
   │ │   [写真]     │ │
   │ │              │ │
   │ │              │ │
   │ └──────────────┘ │
   │       NUTRITION  │  ← Title 下端が画像下端と重なる
   └──────────────────┘
```

### `is-hoop` OFF（既定 / 上下分離）
```
   ┌──────────────────┐
   │   ATHLETE        │
   │   NUTRITION      │
   │   ┌────────────┐ │
   │   │  [写真]    │ │
   │   └────────────┘ │
   └──────────────────┘
```

```css
.hero-image-editorial.is-hoop .hero__title {
  position: relative;
  z-index: var(--layer-2);
  margin-bottom: -2em;  /* 画像と重ねる */
  mix-blend-mode: difference;  /* 写真を見つつ可読性確保 */
}

.hero-image-editorial.is-hoop .hero__title-bottom {
  margin-top: -2em;  /* 画像下端と重ねる */
  z-index: var(--layer-2);
}
```

**注意**: `mix-blend-mode: difference` は背景色が複雑な画像で読みにくくなる場合あり。撮影／素材選定で「タイポと干渉しない余白がある写真」を優先。

---

## パララックス運用（Q5 B 採択 — 動画にも適用可）

DNA v0.5 既定では「ヒーロー**背景画像のみ** slow parallax 任意」だが、本 Spec では **動画にも適用可能** に拡張。

```css
/* 静止画 / 動画 共通 */
.hero__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  will-change: transform;
}

.hero.is-parallax .hero__media {
  transform: translateY(0);
  transition: transform var(--duration-slow) var(--ease-out);
}

/* JS で scrollY に応じて transform: translateY(-N px) を更新 */
```

### 適用ガイドライン

- **slow** のみ採用（fast 系の派手 parallax は禁止）
- スクロール量の **15% 以下** の transform（過度な追従禁止）
- `prefers-reduced-motion: reduce` で必ず無効化（既存 tokens.css 対応）

```css
@media (prefers-reduced-motion: reduce) {
  .hero.is-parallax .hero__media {
    transform: none !important;
    transition: none !important;
  }
}
```

---

## 共通 Props（全 Variants）

| プロパティ | 値 |
|---|---|
| max-width | `--container-max`（1440px・PC ロック） |
| padding (vertical) | PC `--space-8` (160px) / SP `--space-7` (96px) |
| padding (horizontal) | PC `--space-5` (48px) / SP `--space-3` (24px) |
| min-height | `hero--full`=100vh / `hero--tall`=70vh / `hero--compact`=40vh |
| 内部 gap | `--space-3`（24px）— Logo / Label / Title / Text / CTA 間 |
| Title font-size | PC `--fs-mega` (96px) / SP `--fs-hero` (64px) |
| Title font-weight | `--fw-bold`（700） |
| Title line-height | `--lh-heading`（1.2） |
| Text font-size | PC `--fs-lead` 想定 / SP `--fs-body` |

---

## States

### default
基準。動画/画像が読み込まれ次第表示。

### loading（動画読み込み中）
動画が読み込まれるまでローダー表示（既存 fam-corp-hero の `loader` 構造を継承）。

```html
<div class="hero__loader" aria-hidden="true"></div>
```

### scroll-cue（任意・既存 fam-blog-hero 継承）
Hero 末尾に「SCROLL ↓」のスクロール促進 cue。`hero--full` 推奨、`hero--compact` では非表示。

```html
<div class="hero__scroll" aria-hidden="true">
  <span>SCROLL</span>
</div>
```

### parallax-active（`.is-parallax`）
JS で scrollY に応じて `--media-translate-y` を更新。既存 tokens の `prefers-reduced-motion` 対応継承。

---

## Liquid 実装例

### Variant 1: Video Fullscreen（TOP）
```liquid
{% raw %}<section class="hero hero-video-fullscreen hero--full is-parallax" id="hero-{{ section.id }}">
  <video class="hero__media hero__media--pc" autoplay muted loop playsinline>
    <source src="{{ section.settings.video_pc_url }}" type="video/mp4">
  </video>
  <video class="hero__media hero__media--sp" autoplay muted loop playsinline>
    <source src="{{ section.settings.video_sp_url }}" type="video/mp4">
  </video>
  <div class="hero__loader" aria-hidden="true"></div>

  <div class="hero__overlay">
    <div class="hero__inner">
      {% if section.settings.logo %}
        <div class="hero__logo">
          {{ section.settings.logo | image_url: width: 256 | image_tag: alt: section.settings.logo_alt }}
        </div>
      {% endif %}

      <h1 class="hero__title">{{ section.settings.title | newline_to_br }}</h1>
      <p class="hero__text">{{ section.settings.text | newline_to_br }}</p>

      {% if section.settings.cta_text != blank %}
        <div class="hero__cta-wrap">
          <a href="{{ section.settings.cta_url }}"
             class="btn btn-primary btn-lg"
             data-gtag-cta="hero_main_cta">
            {{ section.settings.cta_text }}
          </a>
        </div>
      {% endif %}
    </div>

    <div class="hero__scroll" aria-hidden="true">
      <span>SCROLL</span>
    </div>
  </div>
</section>{% endraw %}
```

### Variant 2: Video Split（キャンペーン LP）
```liquid
{% raw %}<section class="hero hero-video-split hero--full">
  <div class="hero__bg" aria-hidden="true">
    <video class="hero__media hero__media--left" autoplay muted loop playsinline>
      <source src="{{ section.settings.video_left }}" type="video/mp4">
    </video>
    <video class="hero__media hero__media--right" autoplay muted loop playsinline>
      <source src="{{ section.settings.video_right }}" type="video/mp4">
    </video>
  </div>

  {% for corner in 'tl,tr,bl,br' | split: ',' %}
    <span class="hero__corner hero__corner--{{ corner }}" aria-hidden="true">
      {{ section.settings.corner_icon | image_url: width: 128 | image_tag: alt: '' }}
    </span>
  {% endfor %}

  <div class="hero__inner hero__inner--center">
    <h1 class="hero__title">
      {{ section.settings.h1_line1 }}<br>{{ section.settings.h1_line2 }}
    </h1>
    <p class="hero__text">{{ section.settings.sub_text | newline_to_br }}</p>
    {% if section.settings.cta_text != blank %}
      <a href="{{ section.settings.cta_url }}" class="btn btn-primary btn-lg">
        {{ section.settings.cta_text }}
      </a>
    {% endif %}
  </div>
</section>{% endraw %}
```

### Variant 3: Image Editorial（NBA HOOP モード）
```liquid
{% raw %}<section class="hero hero-image-editorial hero--full {% if section.settings.hoop_mode %}is-hoop{% endif %}">
  {% if section.settings.image %}
    <img class="hero__media"
         src="{{ section.settings.image | image_url: width: 2400 }}"
         alt="{{ section.settings.image_alt }}"
         width="2400" height="1600" loading="eager">
  {% endif %}

  <div class="hero__inner hero__inner--editorial">
    <h1 class="hero__title hero__title--top">{{ section.settings.title_top }}</h1>
    <h1 class="hero__title hero__title--bottom">{{ section.settings.title_bottom }}</h1>
    <p class="hero__text">{{ section.settings.text }}</p>
    {% if section.settings.cta_text != blank %}
      <a href="{{ section.settings.cta_url }}" class="btn btn-primary btn-lg">
        {{ section.settings.cta_text }}
      </a>
    {% endif %}
  </div>
</section>{% endraw %}
```

### Variant 4: Minimal Text（FAQ / 告知）
```liquid
{% raw %}<section class="hero hero-minimal-text hero--compact">
  <div class="hero__inner hero__inner--center">
    {% if section.settings.eyebrow != blank %}
      <p class="hero__eyebrow">{{ section.settings.eyebrow }}</p>
    {% endif %}
    <h1 class="hero__title">{{ section.settings.title }}</h1>
    {% if section.settings.subtitle != blank %}
      <p class="hero__subtitle">{{ section.settings.subtitle }}</p>
    {% endif %}
    {% comment %} CTA は任意（0個でも成立）{% endcomment %}
    {% if section.settings.cta_text != blank %}
      <a href="{{ section.settings.cta_url }}" class="btn btn-secondary-ink btn-md">
        {{ section.settings.cta_text }}
      </a>
    {% endif %}
  </div>
</section>{% endraw %}
```

---

## CSS（v0.2 実装）

```css
/* === Hero 基本 === */
.hero {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  max-width: var(--container-max);
  margin: 0 auto;
  padding: var(--space-7) var(--space-3);
  overflow: hidden;
  isolation: isolate;
}

@media (min-width: 1024px) {
  .hero {
    padding: var(--space-8) var(--space-5);
  }
}

/* === Heights === */
.hero--full    { min-height: 100vh; }
.hero--tall    { min-height: 70vh; }
.hero--compact { min-height: 40vh; }

/* === 共通 inner / overlay === */
.hero__overlay {
  position: relative;
  z-index: var(--layer-1);
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: var(--space-3);
}

.hero__inner {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  max-width: 720px;
  text-align: center;
}

.hero__inner--editorial {
  max-width: 1200px;  /* Editorial は広め */
}

/* === Title / Text === */
.hero__title {
  font-family: var(--font-en);
  font-size: var(--fs-hero);   /* SP 64px */
  font-weight: var(--fw-bold);
  line-height: var(--lh-heading);
  letter-spacing: var(--ls-en);
  color: var(--color-white);
}

@media (min-width: 1024px) {
  .hero__title {
    font-size: var(--fs-mega);  /* PC 96px */
  }
}

.hero__text {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  line-height: var(--lh-body);
  letter-spacing: var(--ls-ja);
  color: var(--color-white);
}

@media (min-width: 1024px) {
  .hero__text {
    font-size: var(--fs-lg);  /* PC 20px */
  }
}

.hero__eyebrow {
  font-family: var(--font-en);
  font-size: var(--fs-caption);
  font-weight: var(--fw-semibold);
  letter-spacing: var(--ls-en);
  color: var(--color-drive);
  text-transform: uppercase;
}

/* === Media（動画/画像）=== */
.hero__media {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: var(--layer-base);
}

.hero__media--pc { display: none; }
.hero__media--sp { display: block; }

@media (min-width: 768px) {
  .hero__media--pc { display: block; }
  .hero__media--sp { display: none; }
}

/* === Variant: Video Fullscreen === */
.hero-video-fullscreen::after {
  /* テキスト可読性確保のオーバーレイ */
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.2) 0%,
    rgba(0, 0, 0, 0.5) 100%
  );
  z-index: var(--layer-base);
  pointer-events: none;
}

/* === Variant: Video Split === */
.hero-video-split .hero__bg {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  z-index: var(--layer-base);
}

.hero-video-split .hero__media--left,
.hero-video-split .hero__media--right {
  position: relative;
  width: 100%;
  height: 100%;
}

.hero-video-split .hero__corner {
  position: absolute;
  width: 64px;
  height: 64px;
  z-index: var(--layer-2);
}

.hero-video-split .hero__corner--tl { top: var(--space-3); left: var(--space-3); }
.hero-video-split .hero__corner--tr { top: var(--space-3); right: var(--space-3); }
.hero-video-split .hero__corner--bl { bottom: var(--space-3); left: var(--space-3); }
.hero-video-split .hero__corner--br { bottom: var(--space-3); right: var(--space-3); }

/* === Variant: Image Editorial === */
.hero-image-editorial.is-hoop .hero__title--top {
  position: relative;
  z-index: var(--layer-2);
  margin-bottom: -2em;
  mix-blend-mode: difference;
}

.hero-image-editorial.is-hoop .hero__title--bottom {
  position: relative;
  z-index: var(--layer-2);
  margin-top: -2em;
  mix-blend-mode: difference;
}

/* === Variant: Minimal Text === */
.hero-minimal-text {
  background: var(--bg-primary);
}

.hero-minimal-text .hero__title {
  color: var(--color-ink);
}

.hero-minimal-text .hero__text,
.hero-minimal-text .hero__subtitle {
  color: var(--color-sub);
}

/* === Loader === */
.hero__loader {
  position: absolute;
  inset: 0;
  background: var(--color-ink);
  z-index: var(--layer-3);
  opacity: 1;
  transition: opacity var(--duration-slow) var(--ease-out);
}

.hero.is-loaded .hero__loader {
  opacity: 0;
  pointer-events: none;
}

/* === Scroll Cue === */
.hero__scroll {
  position: absolute;
  bottom: var(--space-3);
  left: 50%;
  transform: translateX(-50%);
  font-family: var(--font-en);
  font-size: var(--fs-caption);
  font-weight: var(--fw-semibold);
  letter-spacing: 0.2em;
  color: var(--color-white);
  text-transform: uppercase;
  z-index: var(--layer-1);
  animation: hero-scroll-bounce var(--duration-breath) var(--ease-inout) infinite;
}

@keyframes hero-scroll-bounce {
  0%, 100% { transform: translate(-50%, 0); opacity: 0.6; }
  50%      { transform: translate(-50%, 8px); opacity: 1; }
}

@media (prefers-reduced-motion: reduce) {
  .hero__scroll { animation: none; }
}

/* === Parallax === */
.hero.is-parallax .hero__media {
  will-change: transform;
  transition: transform var(--duration-slow) var(--ease-out);
}

@media (prefers-reduced-motion: reduce) {
  .hero.is-parallax .hero__media {
    transform: none !important;
    transition: none !important;
  }
}

/* === CTA 配置 === */
.hero__cta-wrap {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  align-items: center;
  margin-top: var(--space-3);
}

@media (min-width: 768px) {
  .hero__cta-wrap {
    flex-direction: row;  /* PC は横並び（CTA 2 個時）*/
  }
}
```

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| Title | 必ず `<h1>` で1ページ1個 |
| 動画 | `autoplay muted loop playsinline` 必須・`<source>` で MP4 / WebM |
| 動画代替 | `prefers-reduced-motion` 検出で静止画にフォールバック推奨 |
| 装飾画像 | `aria-hidden="true"` または空 alt（4 Corner Icon 等） |
| Loader | `aria-hidden="true"` |
| Scroll cue | `aria-hidden="true"` |
| Parallax | `prefers-reduced-motion: reduce` で必ず無効化 |
| Color contrast | 動画上テキストは linear-gradient overlay で WCAG AA を担保 |
| CTA | 既存 Button v0.3 の a11y 規律を継承 |

---

## Do / Don't

### ✅ Do
- TNF 級余白（PC 160px / SP 96px）を厳守
- Title は `<h1>` 1個、ページ階層を尊重
- 動画は PC/SP で別ファイル（モバイル軽量化）
- `is-loaded` クラスで loader をクロスフェード
- CTA は Primary 1 個 OR Primary + Secondary（即決派/相談派 両対応）
- NBA HOOP モードは画像と干渉しない素材で運用

### ✕ Don't（Q6 A 禁止リスト準拠）
- ❌ 動画 + 派手フィルタ重ね（彩度上げ・color burn 等のブレンド多用）
- ❌ Drive 色背景の全画面ベタ塗り
- ❌ Hero 内 CTA を Primary 2 個以上
- ❌ Pill 形状以外の CTA（Button v0.3 規律違反）
- ❌ Parallax を fast 系で動かす（slow + 15% 以下のみ）
- ❌ Title フォントサイズを `--fs-mega`/`--fs-hero` 以下に下げる（迫力消失）
- ❌ `<h1>` 以外で Hero 見出しを書く

---

## L4 Component への継承関係

| 派生 Component | 継承する Variant | 追加要素 |
|---|---|---|
| Bento Tile（Hero 内ブロック）| Image Editorial / Standard Card 派生 | グリッド配置 / カテゴリラベル |
| Section Hero（中継ぎ）| Image Editorial（hero--tall）| Eyebrow / 大型タイポ |
| Page Header（記事冒頭）| Minimal Text（hero--compact）| Breadcrumb |

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `5. Components Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study`
- **Component Set ID**: `67:73` ✅（Audit #4 で既存確認、2026-05-12）
- **実装済 variants**: **3**（`variant`: video-fullscreen / image-editorial / minimal-text）
- ⚠ **重要 Spec gap**: spec は **4 variants × 3 heights = 12 variants** を想定していたが、Figma 実装は **3 variants のみ**（spec 1 variant 欠落 + heights 別 property 化が未実装）
- v0.3 アクション候補:
  - 不足 variant（spec §17 で確定済の 4 つ目）を Figma に追加
  - `height`（compact/default/tall）を別 property として 12 variants に展開
  - または「heights は別 Container Frame で表現」と spec を縮小

## Change Log
- v0.2-figma (2026-05-12): Audit #4 で Component Set `67:73` を既存確認。実装は 3 variants で spec の 12 variants（4×3）から欠落、v0.3 で要整合
- v0.2 (2026-04-28): Worksheet §17 確定（4 Variants / 3 Heights / CTA 0〜2 / NBA HOOP モード任意 / 動画パララックス対応 / 4禁止項目明示）。既存 Liquid（fam-corp-hero / fambox-hero-v17-video / fam-blog-hero）の実測抽出をベースに L4 Component 化
