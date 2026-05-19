---
title: FAMBOX Component — Profile
type: design-system
layer: L4-Components
component: Profile
version: 0.2
status: confirmed
last_updated: 2026-05-12
owner: 宮川
source: 実装計画書 §7 並行作業（5/22 期限）+ preview-profile.html 一次実装 + Tier 3 `fambox-profile` (380 lines) 抽出
brand_alignment:
  - Drive Hero（推進）: セクション全面 Drive 塗りで「監修者・推薦者」の存在を最大主張
  - Editorial: 284×2 細線 + Poppins 英タイトル「Profile」+ 単色塗りで読み物的構造
  - Co-driven: 名前を 40px と最大級にし、肩書を抑制（本人主役）
  - Integrity: 経歴は単段落で誇張せず、実績数字も中立トーン
  - Anti: Card Pattern v0.2 の `card-flat-drive` 派生禁止 / Section レベルでのみ Drive 全面塗りを許可
related:
  - components/card.md
  - components/header.md
  - tokens/colors.md
  - tokens/typography.md
extensible: true  # v0.3 で Card variant 追加可能
---

# Profile — Component

## 概要

監修者・推薦者・主要メンバーを紹介する L4 Section。
**セクション全面を Drive Orange `#FB4C15` で塗り**、白テキストと細い Drive Light 線で読み物的な構造を作る。Hero / Profile / 特定の主役 Section のみが許される「Drive 全面塗り」演出を担う。

**2 Variants**（v0.2 時点では Section のみ confirmed、Card は v0.3 以降）。

## ブランド整合性

- **Drive Hero**: セクション背景に Drive を一面に置くのは FAMBOX 全体で **Hero と Profile のみ許容**。他セクションでこれを真似ない
- **Editorial**: タイトルボックスの 72×72 アイコン枠 + 2px Drive Light ボーダー + Poppins 英文字「Profile」、本文と境界線を一貫した縦リズムで配置
- **Co-driven**: 名前は **40px**（本文比 2.8x）と最大級。肩書は 14px と抑制し、本人を主役に
- **Integrity**: 経歴は 1 段落で完結、賞歴ラッシュや「✨ 業界 No.1」等の煽り表現は禁止
- **Anti 回避**: `card-flat-drive` 派生（Card Pattern を Drive 塗りで使う）禁止、Section レベルでのみ可

---

## Variants（2 種 / 拡張可）

| Variant | クラス | 構造 | 使用例 |
|---|---|---|---|
| **Section** ✅ confirmed | `profile profile-section` | Drive 全面塗りのセクション / 1-3 名並列 | TOP「監修者紹介」/ LP「推薦者」 |
| **Card** ⚠ v0.3 | `profile profile-card` | Card Pattern `card-horizontal` 継承 + Avatar | About ページの団体メンバー一覧 / 連名形式 |

### 拡張ルール（v0.3 以降）

新 Variant 追加時は以下を満たす:
1. **名前 ≥ 32px / 肩書 ≤ 16px**（コントラスト比 2.0x 以上を維持）
2. **区切り線必須**: 名前と bio の間に直線 1 本（width は文字数に合わせる）
3. **Section 全面 Drive 塗りは 1-3 名まで**（4 名以上は Card variant か別 L5 Template へ）
4. **Anti**: ゴールド枠 / 影付き肖像 / SNS リンクラッシュ 禁止
5. **命名**: `profile profile-{variant-name}`（kebab-case）

---

## サイズ仕様

### Section

| 要素 | PC（≥768px） | SP（<768px） |
|---|---|---|
| Section 最大幅 | 1440px / 上下 margin `--space-6` | 100% |
| Section 内側 padding | `--space-7` × 4辺（64px） | 64px 上下 / 24px 左右 |
| Title box 高 | 72px / 幅は inner 100% | 同左 |
| Title icon 枠 | **72×72**（右に `2px solid` Drive Light 罫線） | 同左 |
| Title icon glyph | 40×40 中央 | 同左 |
| Title text 左 padding | `--space-3`（24px、icon 枠から） | 同左 |
| Title font-size | `--fs-h2`（32px / Poppins 400 / white） | `--fs-h3`（24px） |
| Profiles gap | 64px / `flex-direction: row` | 32px / `column` |
| Profile box | **624 × auto**（最低 517 想定） | 100% 幅 / auto |
| Profile bg 画像 | `absolute inset:0 / object-fit: cover` | テキスト下に `relative` 配置 180px |
| Profile content 幅 | 284px / 上寄せ左配置 / `z-index: 1` | 100% |

### Section — テキスト内寸

| 要素 | サイズ | weight | line-height | margin-top |
|---|---|---|---|---|
| Name | `40px`（直値、Display 級） | 500 | 1.3 | — |
| Title（肩書）| `--fs-body-sm`（14px）| 500 | 1.8 | `--space-1`（8px）|
| Line（区切り）| 284 × 2px / Drive Light | — | — | `--space-5`（32px）|
| Bio | `--fs-body-sm`（14px）| 400 | 1.8 | `--space-5`（32px）|

---

## 共通 Props

| プロパティ | 値 |
|---|---|
| Section 背景 | `--color-drive`（`#FB4C15`） |
| Title border / icon-枠 border | `2px solid --color-drive-light` |
| Title font | `--font-en`（Poppins 400）|
| Body / Name font | `--font-ja` |
| Line / Border 強調色 | `--color-drive-light`（`#FC825B`） |
| テキストカラー | `--color-white` 単一（全て白）|
| Profile box border-radius | **0**（角丸禁止 — Editorial を保つ） |
| 影 | **なし**（Drive 塗り単色で完結）|
| z-index | content `1` / 背景画像 `0` |

> ⚠ Note: preview-profile.html では Title border に `#FF7A51` を使用しているが、Spec として **`--color-drive-light` (`#FC825B`) に統一**。色相差は約 1° で視覚上同等、トークン整合性を優先。

---

## 構造（HTML）

```html
<section class="profile profile-section">
  <div class="profile__inner">

    <!-- Title -->
    <header class="profile__title-box">
      <span class="profile__title-icon" aria-hidden="true">
        {%- render 'icon', name: 'profile', size: 40 -%}
      </span>
      <h2 class="profile__title">Profile</h2>
    </header>

    <!-- Profiles -->
    <div class="profile__list">

      <article class="profile__box">
        <div class="profile__bg profile__bg--pc">
          <img src="..." width="624" height="517" alt="" loading="lazy">
        </div>
        <div class="profile__content">
          <p class="profile__name">大前 恵</p>
          <p class="profile__title-sub">FAM スポーツ栄養アドバイザー<br>管理栄養士</p>
          <hr class="profile__line" aria-hidden="true" />
          <p class="profile__bio">プロ野球選手をはじめ、トップアスリートの栄養管理を 15 年以上担当。…</p>
          <div class="profile__sp-image">
            <img src="..." width="343" height="180" alt="" loading="lazy">
          </div>
        </div>
      </article>

      <!-- 必要数（1-3 名まで）繰り返し -->

    </div>

  </div>
</section>
```

---

## CSS（v0.2 実装）

```css
/* === Section === */
.profile {
  max-width: 1440px;
  margin-inline: auto;
  margin-block: var(--space-6);
  background: var(--color-drive);
  position: relative;
}

.profile__inner {
  padding: var(--space-7);
}

/* === Title === */
.profile__title-box {
  width: 100%;
  height: 72px;
  border: 2px solid var(--color-drive-light);
  display: flex;
  align-items: center;
}

.profile__title-icon {
  width: 72px;
  height: 72px;
  border-right: 2px solid var(--color-drive-light);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.profile__title-icon > svg,
.profile__title-icon > img {
  width: 40px;
  height: 40px;
}

.profile__title {
  font-family: var(--font-en);
  font-weight: 400;
  font-size: var(--fs-h2);  /* 32px */
  color: var(--color-white);
  padding-left: var(--space-3);  /* 24px */
  line-height: 1;
}

/* === List === */
.profile__list {
  display: flex;
  gap: 64px;
  margin-top: var(--space-6);  /* 56px */
}

/* === Box === */
.profile__box {
  width: 624px;
  position: relative;
  overflow: hidden;
  border-radius: 0;  /* 角丸禁止 */
}

.profile__bg {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.profile__bg > img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.profile__content {
  position: relative;
  z-index: 1;
  width: 284px;
}

.profile__name {
  font-family: var(--font-ja);
  font-weight: var(--fw-medium);
  font-size: 40px;  /* Display 級・直値で確定 */
  color: var(--color-white);
  line-height: 1.3;
}

.profile__title-sub {
  font-family: var(--font-ja);
  font-weight: var(--fw-medium);
  font-size: var(--fs-body-sm);  /* 14px */
  color: var(--color-white);
  line-height: 1.8;
  margin-top: var(--space-1);  /* 8px */
}

.profile__line {
  width: 284px;
  height: 2px;
  background: var(--color-drive-light);
  border: 0;
  margin: var(--space-5) 0 0;  /* 32px */
}

.profile__bio {
  font-family: var(--font-ja);
  font-weight: var(--fw-regular);
  font-size: var(--fs-body-sm);  /* 14px */
  color: var(--color-white);
  line-height: 1.8;
  margin-top: var(--space-5);  /* 32px */
}

/* === SP === */
@media (max-width: 767px) {
  .profile__inner { padding: 64px var(--space-3); }
  .profile__title { font-size: var(--fs-h3); }  /* 24px */
  .profile__title-box { width: 100%; }

  .profile__list {
    flex-direction: column;
    gap: var(--space-5);  /* 32px */
  }

  .profile__box { width: 100%; height: auto; }
  .profile__content { width: 100%; position: relative; }
  .profile__line { width: 100%; }

  /* PC 背景を非表示にし、テキスト下に画像を配置 */
  .profile__bg--pc { display: none; }

  .profile__sp-image {
    display: block;
    width: 100%;
    height: 180px;
    margin-top: var(--space-3);  /* 24px */
    overflow: hidden;
  }

  .profile__sp-image > img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
}

@media (min-width: 768px) {
  .profile__sp-image { display: none; }
}

/* === reduced motion === */
@media (prefers-reduced-motion: reduce) {
  /* Profile はアニメ未使用、no-op */
}
```

---

## Liquid 実装例（Section）

```liquid
{% raw %}<section class="profile profile-section" data-gtag-section="profile">
  <div class="profile__inner">

    <header class="profile__title-box">
      <span class="profile__title-icon" aria-hidden="true">
        {%- render 'icon', name: 'profile', size: 40 -%}
      </span>
      <h2 class="profile__title">{{ section.settings.title | default: "Profile" }}</h2>
    </header>

    <div class="profile__list">
      {%- for block in section.blocks -%}
        {%- if block.type == 'person' -%}
          <article class="profile__box" {{ block.shopify_attributes }}>
            {%- if block.settings.image != blank -%}
              <div class="profile__bg profile__bg--pc">
                <img src="{{ block.settings.image | image_url: width: 1248 }}"
                     width="624" height="517"
                     alt="{{ block.settings.name | escape }}"
                     loading="lazy">
              </div>
            {%- endif -%}
            <div class="profile__content">
              <p class="profile__name">{{ block.settings.name }}</p>
              <p class="profile__title-sub">{{ block.settings.title_sub }}</p>
              <hr class="profile__line" aria-hidden="true" />
              <p class="profile__bio">{{ block.settings.bio }}</p>
              {%- if block.settings.image != blank -%}
                <div class="profile__sp-image">
                  <img src="{{ block.settings.image | image_url: width: 686 }}"
                       width="343" height="180"
                       alt=""
                       loading="lazy">
                </div>
              {%- endif -%}
            </div>
          </article>
        {%- endif -%}
      {%- endfor -%}
    </div>

  </div>
</section>{% endraw %}
```

---

## Schema（参考）

```json
{
  "name": "Profile",
  "tag": "section",
  "class": "profile profile-section",
  "settings": [
    { "type": "text", "id": "title", "label": "セクション見出し（英）", "default": "Profile" }
  ],
  "blocks": [
    {
      "type": "person",
      "name": "プロフィール",
      "limit": 3,
      "settings": [
        { "type": "image_picker", "id": "image", "label": "肖像（推奨 1248×1034 以上）" },
        { "type": "text", "id": "name", "label": "氏名", "default": "大前 恵" },
        { "type": "textarea", "id": "title_sub", "label": "肩書（改行可）", "default": "FAM スポーツ栄養アドバイザー\n管理栄養士" },
        { "type": "textarea", "id": "bio", "label": "経歴（1 段落）", "default": "プロ野球選手をはじめ…" }
      ]
    }
  ],
  "presets": [{ "name": "Profile", "blocks": [{ "type": "person" }, { "type": "person" }] }]
}
```

---

## States

Profile Section は静的表示。状態遷移は持たない（hover / active 等）。

| State | クラス / 挙動 |
|---|---|
| default | 表示中（全 Profile 視認可） |
| focus（キーボード） | 肖像 `<img>` への focus 矩形は適用しない（装飾画像のため `alt=""` 推奨）。リンク化する場合のみ focus ring を出す |
| hover | **何もしない**（Editorial 紙面の読み心地を維持。色変化 / 浮き上がりは Anti） |

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| `<section>` ランドマーク | `aria-labelledby` で `.profile__title` を参照（id 付与）|
| Title icon | `aria-hidden="true"`、隣接する `<h2>` で意味は伝わる |
| 肖像画像 | 装飾なら `alt=""`、本人情報を補強するなら `alt="大前 恵"`（氏名のみ） |
| 区切り線 hr | `aria-hidden="true"` で AT 読み上げ抑制 |
| コントラスト | `#FFFFFF` on `#FB4C15` ≈ 3.4:1（**WCAG AA Large テキストのみクリア / 14px 本文は要注意**） |
| 本文最低 16px 確保 | 本コンポは設計上 14px が DNA 整合。WCAG AAA を要求される場面では **bio 16px に拡張可**（v0.3 で対応） |
| `prefers-reduced-motion` | 該当アニメなし |

### コントラスト注意点

`#FFFFFF` を `#FB4C15` に重ねた本コンポは、Large テキスト（40px name など）は AA を超えるが、**14px の bio / 肩書は AA 大文字 (4.5:1) を満たさない**。これは DNA の演出優先設計だが、**bio は短文（80 字以内）に絞り**、視覚負荷を最小化する。WCAG AAA を満たすには `bio` を 16px / weight 500 に上げる必要があり、v0.3 で代替トークンを検討。

---

## Do / Don't

### ✅ Do
- セクション全面に Drive `#FB4C15` を塗る（Profile 専用の表現として許可）
- 名前を 40px と最大級にし、肩書（14px）と明確なジャンプ率を作る
- 区切り線 `284×2px` を必ず Drive Light で引く（Editorial キャラクターライン）
- 1-3 名までに絞る（4 名以上は別 L5 Template を検討）
- PC は背景画像が全面、SP はテキスト下 180px の画像配置（明確に役割を分離）
- Poppins 英文字「Profile」をタイトルに使用（読み物的トーン）

### ✕ Don't
- ❌ **Card Pattern を Drive 全面塗りで使う**（`card-flat-drive` 派生は Anti） — Section レベルでのみ可
- ❌ **角丸を付ける** — Editorial の単色塗りに角丸は不協和音
- ❌ **影 / Glow を付ける** — Drive 塗り単色で完結させる
- ❌ **「✨ 業界 No.1」「驚異の」等の煽り経歴** — Integrity 違反
- ❌ **SNS アイコンラッシュ / 賞歴ロゴ集合** — 本人不在の権威主義は Co-driven 違反
- ❌ **4 名以上を 1 セクションに詰める** — Drive 塗りの強さで認知過負荷
- ❌ **`#FF7A51` を直書き** — `--color-drive-light` に統一

---

## Brand DNA Anti との照合

本コンポは以下の Anti を踏まない:
- 派手・煽り → Drive 塗りはあるが、テキストは中立トーン
- 媚びる → 名前 40px が主役、肩書も控えめ
- 過剰演出 → 影なし / 角丸なし / アニメなし

ただし **Drive 全面塗りは強い表現**のため、本コンポを使うのは Hero / Profile / 主役 Section に限定し、TOPページ内でも 1 箇所のみ使用する。

---

## L4 派生関係

| 派生 | 継承する Variant | 追加要素 |
|---|---|---|
| About ページ メンバー一覧（4-10 名）| Card variant (v0.3) | `card-horizontal` + Avatar v0.2 / Drive 塗りなし |
| Testimonial / Case Study 主役 | 既存 case-study.md（L4 別 Component） | 顔写真 + 引用文 |
| 推薦者（Endorsement）| Card variant (v0.3) | Profile + 引用文 + Drive 線 |

---

## 実装計画書との対応

- 計画書 §1 Tier 3: `fambox-profile` (380 lines) → 本 Spec の **Section Variant** へ書き換え
- 計画書 §1 Tier 3 で「Card Pattern v0.2 `card-horizontal` + Avatar v0.2」と指定されていた案 → **Card Variant (v0.3) として保留**。preview-profile.html の Drive 塗り Section が DNA 整合的に正
- 計画書 §7 並行作業: 「L4 Profile Card」期限 5/22 → **L4 Profile Component（Section + Card 拡張枠）として 2026-05-12 に Spec 化完了**

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `5. Components Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study`
- **Component Set ID**: `96:79` ✅ 新規生成（2026-05-12 Session #6）
- 生成スキル: `figma-component-from-spec` + `figma-use`
- **実装済 variants**: 1（`variant`: section）/ Card variant は v0.3 拡張枠で保留
- **構造**:
  - Section bg: `color/brand/drive` (#FB4C15) 全面、padding 64px × 4 辺
  - **Title box**: 1312 × 72 / 2px solid `drive-light` 枠
    - Icon box 72×72 / 右に 2px drive-light 縦罫線 (`individualStrokeWeights.right = 2`)
    - Icon glyph: 40×40 drive-light 半透明 placeholder
    - "Profile" Poppins Regular 32px white（左 padding 24px）
  - Title → Profile list: 56px
  - **Profile list**: HORIZONTAL / gap 64 / 2 boxes 並列
  - 各 **Profile box** 624 × 517 / `layoutMode: 'NONE'` / `clipsContent: true`:
    - 背景 placeholder: 全面 dark gray rect（実画像は production で fill）
    - Content frame 284 wide / 上寄せ左配置:
      - Name 40px Bold White line 130%
      - 肩書 14px Medium White line 180%
      - Spacer 24（line top margin = itemSpacing 8 + spacer 24 = 32）
      - 区切り線 284 × 2 `drive-light`
      - Spacer 24（line bottom margin = 32）
      - Bio 14px Regular White line 180%
- **未実装（v0.3 で追加予定）**:
  - **Card variant**（About ページ・メンバー一覧用）
  - 背景画像の Image Fill バインド（現状 dark placeholder）
  - SP layout（テキスト下に画像 180px、Card box の縦積み）
  - WCAG 注: 14px 白 on Drive は AA 大文字非達成、bio を 16px に昇格する spec 改訂候補

## Change Log
- v0.2-figma (2026-05-12): Figma Component Set `96:79` 新規生成（Section variant）。Drive 全面塗り + Editorial キャラクターライン（2px drive-light 罫線）+ 2 名並列構造を実装。Title box の Icon 枠は `individualStrokeWeights.right = 2` で実現
- v0.2 (2026-05-12): preview-profile.html を一次資料に Section Variant を Spec 化。Title border の直書き `#FF7A51` を `--color-drive-light` (#FC825B) に統一。Card variant は v0.3 拡張枠で保留（About ページ・メンバー一覧用）
