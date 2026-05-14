---
title: FAMBOX Component — Footer
type: design-system
layer: L4-Components
component: Footer
version: 0.2
status: confirmed
last_updated: 2026-04-28
owner: 宮川
deadline: 2026-05-29（OKR Task 2-1-a TOPページ DNA 反映）
source: Worksheet §19（2026-04-28 確定）+ 既存 Liquid 実測（fam-footer-v2 / fambox/sections/footer）
brand_alignment:
  - Continuity（連続）: Brand area + Nav + Social で関係継続を促す
  - Integrity（誠実）: Legal links（Privacy / Terms / 特商法）を必ず提示
  - Anti: Drive 色ベタ塗り / 動きアニメ / Hero 級画像 を禁止
related:
  - components/button.md
  - components/header.md
  - tokens/colors.md
extensible: true  # v0.3 以降でカスタム Variant 追加余地あり
---

# Footer — Component

## 概要

FAMBOX の全画面共通 Component。**3 Variants** で構成。
背景は Ink (`#1B1D1A`) 統一・White テキスト・SNS リンクと Legal links を最低限提示する誠実な設計。

## ブランド整合性

- **Continuity（連続）**: Brand area + Nav columns + Social でユーザー関係の継続を促す
- **Integrity（誠実）**: Legal links（Privacy / Terms / 特商法）を Bottom row で必ず提示
- **Co-driven**: 「お客様」表現を排し、SNS は対等な接点として配置
- **Anti 回避**: Drive 色ベタ塗り / SNS アイコンの Display サイズ化 / Bottom row 動きアニメ / Hero 級画像 を禁止

---

## Variants（3 種 / 拡張可）

| Variant | クラス | 構造 | 使用例 |
|---|---|---|---|
| **Standard** | `footer footer-standard` | Brand + Nav columns + Social + Bottom row | 通常ページ全般（fam-footer-v2 継承）|
| **Minimal** | `footer footer-minimal` | Brand + Bottom row のみ（Nav・Social 省略）| LP / チェックアウト |
| **Sitemap** | `footer footer-sitemap` | Standard + 詳細 Sitemap（多列カテゴリ）| 大規模サイト / 商品多時 / 将来用 |

### 拡張ルール（v0.3 以降）

新しい Footer Variant が必要な場合は以下を満たす:
1. **背景規律**: Ink (`--color-ink`) 単色で固定（Drive 色ベタ塗り禁止）
2. **Legal 必須**: Bottom row に Privacy / Terms / 特商法リンクを必ず含む
3. **SNS 規律**: SNS アイコンは 40px 上限（Display サイズ禁止）
4. **DNA Anti を踏まない**: 動きアニメ / Hero 級画像 / Drive 全面ベタ塗り 禁止
5. **命名**: `footer footer-{variant-name}`（kebab-case）

---

## 構造（Standard 全要素）

```
┌────────────────────────────────────────────────────┐
│ ┌─Brand Area──┐ ┌─Nav Columns─────────────────┐    │
│ │ [LOGO]      │ │ [Col 1] [Col 2] [Col 3]     │    │
│ │ tagline...  │ │  link    link    link       │    │
│ └─────────────┘ │  link    link    link       │    │
│                 └─────────────────────────────┘    │
│                                                    │
│ ┌─Social──────────────────────────────────────┐   │
│ │ [IG] [YT] [note] ...                        │   │
│ └─────────────────────────────────────────────┘   │
├────────────────────────────────────────────────────┤
│ Bottom Row                                         │
│ © 2026 FAMBOX     Privacy / Terms / 特商法         │
└────────────────────────────────────────────────────┘
```

---

## 背景・カラー（Q2 A 採択）

| 項目 | 値 |
|---|---|
| Footer 全体 background | `--color-ink` (`#1B1D1A`) |
| Brand text color | `--color-white` |
| Nav link color | `--color-white` |
| Nav link hover | `--color-drive` |
| Tagline color | `rgba(255, 255, 255, 0.7)` (Caption 級) |
| Bottom row background | `rgba(0, 0, 0, 0.3)` (Inkより少し濃い差別化) |
| Bottom row text color | `rgba(255, 255, 255, 0.6)` |
| Border (sections 区切り) | `rgba(255, 255, 255, 0.1)` |

---

## Logo 配置（Q3 A 採択 — 左固定）

Header と整合させて**左固定**。Brand area は Footer の左側 30-40% 幅で構成。

```css
.footer__brand {
  flex: 0 0 auto;
  max-width: 320px;
}
```

White ロゴ（透過 PNG 推奨）を `--color-ink` 背景に配置。

---

## Nav Columns（Standard / Sitemap）

| 項目 | 値 |
|---|---|
| Column 数 | PC 3-4 列 / Tablet 2 列 / SP 1 列（accordion 折り畳み推奨）|
| Column 見出し | `--font-en` `--fs-body` `--fw-semibold` `--color-white` |
| Link | `--font-ja` `--fs-body-sm`（14px）`--color-white` |
| Link gap | `--space-1`（8px）vertical |
| Link hover | `color: var(--color-drive)` `transition: color var(--duration-fast) var(--ease-out)` |

```css
.footer__nav {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-4);
}

@media (max-width: 1023px) {
  .footer__nav { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 767px) {
  .footer__nav { grid-template-columns: 1fr; }
}
```

---

## Social Links（Q4 A 採択 — 全 Variants 必須）

| 項目 | 値 |
|---|---|
| 対応サービス | Instagram / YouTube / note（最低限）/ X / TikTok（任意）|
| アイコンサイズ | **40×40px**（Display サイズ禁止 = Anti 違反）|
| アイコン配置 | 横並び・gap `--space-2`（16px）|
| 色 | アイコン内ロゴは White (透明背景版 SVG 推奨)|
| hover | アイコン background が Drive 色に切替（既存 fam-footer-v2 と整合）|

```css
.footer__social-list {
  display: flex;
  gap: var(--space-2);
  list-style: none;
  margin: 0;
  padding: 0;
}

.footer__social-list a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-pill);
  background: rgba(255, 255, 255, 0.1);
  transition: background var(--duration-fast) var(--ease-out);
}

.footer__social-list a:hover {
  background: var(--color-drive);
}

.footer__social-list a:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

---

## Bottom Row（Q5 A 採択 — Copyright + Legal links のみ）

| 要素 | 内容 |
|---|---|
| Copyright | `© 2026 FAMBOX. All rights reserved.` |
| Legal Links | Privacy Policy / Terms of Service / 特商法に基づく表記 |

**含めない**: Payment methods icons（v0.3 以降の B 案）/ 言語スイッチャー（v0.3 以降の C 案）/ メールマガジン登録（Q6 で不採用）

```html
<div class="footer__bottom">
  <div class="footer__bottom-inner">
    <p class="footer__copyright">© {{ 'now' | date: '%Y' }} FAMBOX. All rights reserved.</p>
    <ul class="footer__legal">
      <li><a href="/policies/privacy-policy">Privacy</a></li>
      <li><a href="/policies/terms-of-service">Terms</a></li>
      <li><a href="/policies/legal-notice">特商法に基づく表記</a></li>
    </ul>
  </div>
</div>
```

---

## CTA 配置（Q6 A 採択 — Footer に CTA 置かない）

Footer は **CTA を持たない**。Header / Hero / Section の文脈で CTA は十分提示済み、Footer での繰り返しは弱化を招く。

メールマガジン登録機能が必要な場合は、別 Component（`SubscribeBlock` 等）として **Footer の上のセクション**に配置する（Footer 内には組まない）。

---

## Liquid 実装例

### Standard（fam-footer-v2 継承）
```liquid
{% raw %}<footer class="footer footer-standard">
  <div class="footer__main">
    <div class="footer__inner">
      {%- comment -%} Brand Area（左）{%- endcomment -%}
      <div class="footer__brand">
        {% if section.settings.footer_logo %}
          <img class="footer__logo"
               src="{{ section.settings.footer_logo | image_url: width: 256 }}"
               alt="{{ shop.name }}"
               width="120" height="40" loading="lazy">
        {% endif %}
        {% if section.settings.footer_tagline != blank %}
          <p class="footer__tagline">{{ section.settings.footer_tagline }}</p>
        {% endif %}
      </div>

      {%- comment -%} Nav Columns（右）{%- endcomment -%}
      <nav class="footer__nav" aria-label="フッターナビゲーション">
        {% for block in section.blocks %}
          {% if block.type == 'menu_column' %}
            <div class="footer__nav-col" {{ block.shopify_attributes }}>
              <h3 class="footer__nav-heading">{{ block.settings.heading }}</h3>
              <ul class="footer__nav-list">
                {% for link in block.settings.menu.links %}
                  <li><a href="{{ link.url }}" class="footer__link">{{ link.title }}</a></li>
                {% endfor %}
              </ul>
            </div>
          {% endif %}
        {% endfor %}
      </nav>

      {%- comment -%} Social（必須）{%- endcomment -%}
      <div class="footer__social">
        <ul class="footer__social-list">
          {% if section.settings.sns_instagram != blank %}
            <li><a href="{{ section.settings.sns_instagram }}" target="_blank" rel="noopener" aria-label="Instagram">
              {%- render 'icon', name: 'social-instagram-white', size: 24 -%}
            </a></li>
          {% endif %}
          {% if section.settings.sns_youtube != blank %}
            <li><a href="{{ section.settings.sns_youtube }}" target="_blank" rel="noopener" aria-label="YouTube">
              {%- render 'icon', name: 'social-youtube-white', size: 24 -%}
            </a></li>
          {% endif %}
          {% if section.settings.sns_note != blank %}
            <li><a href="{{ section.settings.sns_note }}" target="_blank" rel="noopener" aria-label="note">
              {%- render 'icon', name: 'social-note-white', size: 24 -%}
            </a></li>
          {% endif %}
        </ul>
      </div>
    </div>
  </div>

  {%- comment -%} Bottom Row {%- endcomment -%}
  <div class="footer__bottom">
    <div class="footer__bottom-inner">
      <p class="footer__copyright">© {{ 'now' | date: '%Y' }} FAMBOX. All rights reserved.</p>
      <ul class="footer__legal">
        <li><a href="/policies/privacy-policy">Privacy</a></li>
        <li><a href="/policies/terms-of-service">Terms</a></li>
        <li><a href="/policies/legal-notice">特商法に基づく表記</a></li>
      </ul>
    </div>
  </div>
</footer>{% endraw %}
```

### Minimal（LP / チェックアウト）
```liquid
{% raw %}<footer class="footer footer-minimal">
  <div class="footer__main">
    <div class="footer__inner">
      <div class="footer__brand">
        <img class="footer__logo" src="{{ section.settings.footer_logo | image_url: width: 256 }}" alt="{{ shop.name }}" width="120" height="40">
      </div>
    </div>
  </div>

  <div class="footer__bottom">
    <div class="footer__bottom-inner">
      <p class="footer__copyright">© {{ 'now' | date: '%Y' }} FAMBOX. All rights reserved.</p>
      <ul class="footer__legal">
        <li><a href="/policies/privacy-policy">Privacy</a></li>
        <li><a href="/policies/terms-of-service">Terms</a></li>
        <li><a href="/policies/legal-notice">特商法に基づく表記</a></li>
      </ul>
    </div>
  </div>
</footer>{% endraw %}
```

### Sitemap（多列カテゴリ・将来用）
```liquid
{% raw %}<footer class="footer footer-sitemap">
  <div class="footer__main">
    <div class="footer__inner">
      <div class="footer__brand">
        <img class="footer__logo" src="{{ section.settings.footer_logo | image_url: width: 256 }}" alt="{{ shop.name }}">
        <p class="footer__tagline">{{ section.settings.footer_tagline }}</p>
      </div>

      <nav class="footer__nav footer__nav--sitemap" aria-label="サイトマップ">
        {% for block in section.blocks %}
          {% if block.type == 'sitemap_column' %}
            <div class="footer__nav-col">
              <h3 class="footer__nav-heading">{{ block.settings.heading }}</h3>
              <ul class="footer__nav-list">
                {% for link in block.settings.menu.links %}
                  <li><a href="{{ link.url }}" class="footer__link">{{ link.title }}</a></li>
                {% endfor %}
              </ul>
            </div>
          {% endif %}
        {% endfor %}
      </nav>

      <div class="footer__social">{%- comment -%}（Standard と同じ）{%- endcomment -%}</div>
    </div>
  </div>

  <div class="footer__bottom">{%- comment -%}（Standard と同じ）{%- endcomment -%}</div>
</footer>{% endraw %}
```

---

## CSS（v0.2 実装）

```css
/* === Footer 基本（全 Variants 共通）=== */
.footer {
  background: var(--color-ink);
  color: var(--color-white);
  isolation: isolate;
}

.footer__main {
  padding: var(--space-7) 0;  /* SP 96px */
}

@media (min-width: 1024px) {
  .footer__main {
    padding: var(--space-8) 0;  /* PC 160px */
  }
}

.footer__inner {
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 var(--space-3);
}

@media (min-width: 1024px) {
  .footer__inner {
    flex-direction: row;
    align-items: flex-start;
    gap: var(--space-6);
    padding: 0 var(--space-5);
  }
}

/* === Brand Area === */
.footer__brand {
  flex: 0 0 auto;
  max-width: 320px;
}

.footer__logo {
  height: 40px;
  width: auto;
}

.footer__tagline {
  margin-top: var(--space-2);
  font-family: var(--font-ja);
  font-size: var(--fs-body-sm);
  color: rgba(255, 255, 255, 0.7);
  line-height: var(--lh-body);
  letter-spacing: var(--ls-ja);
}

/* === Nav === */
.footer__nav {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-4);
}

@media (max-width: 1023px) {
  .footer__nav { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 767px) {
  .footer__nav { grid-template-columns: 1fr; }
}

.footer__nav-heading {
  font-family: var(--font-en);
  font-size: var(--fs-body);
  font-weight: var(--fw-semibold);
  color: var(--color-white);
  letter-spacing: var(--ls-en);
  margin-bottom: var(--space-2);
}

.footer__nav-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.footer__link {
  font-family: var(--font-ja);
  font-size: var(--fs-body-sm);
  color: var(--color-white);
  text-decoration: none;
  letter-spacing: var(--ls-ja);
  transition: color var(--duration-fast) var(--ease-out);
}

.footer__link:hover {
  color: var(--color-drive);
}

.footer__link:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}

/* === Social === */
.footer__social {
  flex: 0 0 auto;
}

.footer__social-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
}

.footer__social-list a {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-pill);
  background: rgba(255, 255, 255, 0.1);
  color: var(--color-white);
  transition: background var(--duration-fast) var(--ease-out);
}

.footer__social-list a:hover {
  background: var(--color-drive);
}

.footer__social-list a:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}

/* === Bottom Row === */
.footer__bottom {
  background: rgba(0, 0, 0, 0.3);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding: var(--space-3) 0;
}

.footer__bottom-inner {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 var(--space-3);
  font-size: var(--fs-caption);
  color: rgba(255, 255, 255, 0.6);
}

@media (min-width: 768px) {
  .footer__bottom-inner {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0 var(--space-5);
  }
}

.footer__copyright {
  margin: 0;
  font-family: var(--font-ja);
  letter-spacing: var(--ls-ja);
}

.footer__legal {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  gap: var(--space-3);
  flex-wrap: wrap;
}

.footer__legal a {
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-out);
}

.footer__legal a:hover {
  color: var(--color-white);
}

/* === Variant: Minimal === */
.footer-minimal .footer__nav,
.footer-minimal .footer__social {
  display: none;
}

/* === Variant: Sitemap === */
.footer-sitemap .footer__nav--sitemap {
  grid-template-columns: repeat(4, 1fr);
}

@media (max-width: 1023px) {
  .footer-sitemap .footer__nav--sitemap { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 767px) {
  .footer-sitemap .footer__nav--sitemap { grid-template-columns: 1fr; }
}
```

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| `<footer>` | セマンティック footer タグで囲む（landmark） |
| Nav | `<nav aria-label="フッターナビゲーション">` で囲む |
| Sitemap Nav | `<nav aria-label="サイトマップ">` |
| Social link | `aria-label` で SNS 名を明示（例: `aria-label="Instagram"`）+ `target="_blank" rel="noopener"` |
| Logo | `<img alt="...">` で店舗名を必ず指定 |
| Color contrast | White on Ink = 16.6:1（WCAG AAA 余裕クリア） |
| Caption text | `rgba(255,255,255,0.6)` でも 9:1 以上（AA クリア） |
| キーボード | Tab で全要素フォーカス可・順序は Brand → Nav → Social → Bottom |

---

## Do / Don't

### ✅ Do
- 背景は Ink (`--color-ink`) 単色固定
- SNS リンクは 40px 上限で控えめに
- Bottom row は Copyright + Legal の 2 要素のみ
- Legal links（Privacy / Terms / 特商法）を必ず提示
- White ロゴ（透明背景 SVG / PNG）を使用
- Link hover は `color 0.2s ease`（Header と整合）

### ✕ Don't（Q7 A 禁止リスト準拠）
- ❌ **Drive 色背景の全面ベタ塗り**（Anti / うるさい）
- ❌ **SNS アイコンを Display サイズ（64px+）にしない**（情報密度低下）
- ❌ **Bottom row に動きアニメ禁止**（落ち着き重視・Anti）
- ❌ **Footer 内に Hero 級画像を置かない**（Footer の役割逸脱）
- ❌ Footer 内に Primary CTA を置かない（Q6 A 採択）
- ❌ メール登録フォームを Footer 内に組み込まない（別 SubscribeBlock 推奨）
- ❌ Payment methods icons を Bottom row に並べない（v0.3 以降の B 案・現時点不採用）
- ❌ 言語スイッチャーを Footer に置かない（v0.3 以降の C 案・現時点不採用）

---

## Brand DNA Anti との照合

本コンポは以下の Anti を踏まない:
- 表面的／派手 → 背景単色 + 装飾最小限
- エセ高級 → グラデーション・ゴールドなし
- 媚びた広告 → CTA なし・SNS 控えめ・Legal 提示で誠実

---

## L4 派生関係

| 派生 Component | 継承する Variant | 追加要素 |
|---|---|---|
| Checkout Footer | Minimal | Trust badge / セキュリティロゴ |
| Email Footer（メール埋め込み）| Minimal | inline CSS / 画像ベース |
| Mobile App Footer（PWA）| Standard（compact）| App-specific links |

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `5. Components Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study`
- **Component Set ID**: `60:95` ✅（Audit #4 で既存確認、2026-05-12）
- **実装済 variants**: 3（`variant`: standard / minimal / sitemap）

## Liquid 実装

- **File**: `sections/fambox-footer.liquid`（665 行）
- **Schema**: 18 settings + 1 block type (`nav_column`) + 3 presets（Standard / Minimal / Sitemap）
- **Block**: `nav_column` は Shopify ナビ (`link_list`) 連携 + manual_links（"ラベル|URL" 改行区切り）の二段構え。fallback により presets で即配置可能
- **SNS**: Instagram / YouTube / note / X (Twitter) / TikTok の 5 種を inline SVG で対応（snippet 依存なし）
- **Legal**: Privacy / Terms / 特商法の URL は settings 化（条件分岐で空なら非表示）
- **Accessibility**: `<footer role="contentinfo">` + `<nav aria-label="...">` + SNS `aria-label` + `prefers-reduced-motion` 対応
- **既存資産**: `fam-footer-v2.liquid` (旧 LP 用) は **共存保持**。本ファイルが spec v0.2 準拠の新標準

## 既存 fam-footer-v2.liquid との関係

| 項目 | fam-footer-v2.liquid（旧）| fambox-footer.liquid（新）|
|---|---|---|
| 構造 | コーナー SVG 4 枚 + brand area + nav columns + SNS（独自レイアウト）| spec v0.2 準拠（Brand + Nav + Social + Bottom row）|
| Variant | 1 種（実質 Standard 系）| 3 種（standard / minimal / sitemap）切替可 |
| SNS | snippet 依存 / アイコン色独自管理 | inline SVG / 40×40 円形ボタン統一 |
| Legal | hard-coded URL | settings 化（URL 空なら非表示）|
| Bottom 背景 | コーナー SVG 重畳 | `rgba(0,0,0,0.3)` + 上罫線（spec 準拠）|
| 用途 | LP / プロモ（独自世界観）| **DS 標準 / 本番 TOP / Checkout / 全ページ共通**|

移行戦略: 新規ページは `fambox-footer.liquid` を採用。fam-footer-v2 は撤去せず**並存**（LP の世界観差別化として保持）。Week 5 QA で TOP 反映時に置換判断。

## Change Log
- v0.2-figma-layout (2026-05-14): Session #32 で variants の重なり (x=0, y=0) を解消。y 順に縦並べ（standard y=0 / minimal y=389 / sitemap y=675、gap 60px）。Set boundary を 1440×329 → **1440×1044** に明示 resize
- v0.2-liquid (2026-05-14): `fambox-footer.liquid` 三位一体達成。3 variants 内包 + `nav_column` block + 3 presets。SNS 5 種 inline SVG / Legal URL settings 化 / `fam-footer-v2.liquid` とは並存（後者は LP 用として保持）
- v0.2-figma (2026-05-12): Audit #4 で Component Set `60:95` を既存確認。3 variants 実装済（standard / minimal / sitemap）
- v0.2 (2026-04-28): Worksheet §19 確定（3 Variants / Ink 背景固定 / Logo 左 / SNS 必須 40px / Bottom = Copyright + Legal のみ / CTA なし / 4 禁止項目明示）。既存 Liquid（fam-footer-v2 / fambox/sections/footer）の実測抽出をベースに L4 Component 化

## Known TODOs（v0.3 候補）
- ⚠️ **Figma sitemap variant の 4 列化**: Liquid 側は `.footer-sitemap .footer__nav { grid-template-columns: repeat(4, 1fr); }` で 4 列差別化済だが、Figma 上の `variant=sitemap` (60:56) は中身が standard と同等（3 列）。v0.3 で 4 列に再構築して spec ↔ Figma ↔ Liquid の三位一体を完全化する
