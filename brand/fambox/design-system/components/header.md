---
title: FAMBOX Component — Header
type: design-system
layer: L4-Components
component: Header
version: 0.2
status: confirmed
last_updated: 2026-04-28
owner: 宮川
deadline: 2026-05-29（OKR Task 2-1-a TOPページ DNA 反映）
source: Worksheet §18（2026-04-28 確定）+ 既存 Liquid 実測（fam/sections/header / fam-header-menu / fambox/sections/header）+ Brand DNA v0.5 ナビ仕様継承
brand_alignment:
  - Continuity（連続）: ページ間で sticky 維持し動線が途切れない
  - Co-driven（対等）: PC は中央揃え、SP はハンバーガー不採用で「隠さない」
  - Anti: ハンバーガー単独禁止 / Drive ベタ塗り禁止 / Logo の Drive 背景禁止
related:
  - components/button.md
  - components/card.md
  - tokens/colors.md
  - tokens/motion.md
extensible: true  # v0.3 以降でカスタム Variant 追加余地あり
---

# Header — Component

## 概要

FAMBOX の全ページ共通 Component。**3 Variants × 3 Heights × 3 Sticky Modes** で構成。
Brand DNA v0.5 の「**ハンバーガー不採用 / 横スクロールメニュー / Drive Pill CTA**」を体系化。

## ブランド整合性

- **Continuity（連続）**: `position: sticky` でスクロール中も動線維持
- **Co-driven（対等）**: PC 中央揃え / SP も「隠す UI（ハンバーガー）」を採用しない
- **Drive 推進**: 末尾 Primary CTA Pill で次アクションを明示
- **Anti 回避**: Drive 色ベタ塗り / Logo の Drive 背景配置 / Display サイズのメニュー文字は禁止

---

## Variants（3 種 / 拡張可）

| Variant | クラス | 構造 | 使用例 |
|---|---|---|---|
| **Standard** | `header header-standard` | Logo + Menu + CTA + Cart/Account | 通常ページ全般（TOP / 商品 / Blog 等） |
| **Minimal** | `header header-minimal` | Logo + CTA のみ（Menu 非表示） | LP / チェックアウト導線 |
| **Mega** | `header header-mega` | Standard + Mega Menu（hover でカテゴリ展開） | 商品カテゴリ多時 / 将来用 |

### 拡張ルール（v0.3 以降）

新しい Header Variant が必要な場合は以下を満たす:
1. **Sticky 規律**: 3 Sticky Modes のいずれかを必ず採用（独自スクロール挙動禁止）
2. **CTA 規律**: Primary 1 個（Q6 A 採択 / Drive Pill / btn-primary btn-md）
3. **Logo 配置**: 左固定（Q5 A 採択 / `logo--left`）
4. **DNA Anti 回避**: ハンバーガー単独 / Drive ベタ塗り / Display サイズメニュー文字 禁止
5. **命名**: `header header-{variant-name}`（kebab-case）

---

## Heights（3 段階・modifier 切替）

| Modifier | 高さ | 使用文脈 |
|---|---|---|
| `header--compact` | 64px | 情報密度優先（Blog 記事 / FAQ / モバイルアプリ風）|
| `header--default` ★既定 | 80px | 通常ページ全般 |
| `header--tall` | 96px | TOP / Hero と並列の主要 LP |

```css
.header { height: 80px; }                       /* 既定 = default */
.header--compact { height: 64px; }
.header--default { height: 80px; }
.header--tall    { height: 96px; }
```

### Height 選択フロー

```
このページの主役は何？
├─ Hero / 主要 LP → header--tall（96px・存在感）
├─ 通常ページ     → header--default（80px・標準）
└─ 情報密度優先   → header--compact（64px・小さく）
```

---

## Sticky Modes（3 種・modifier 切替・Q3 D 採択）

| Modifier | 挙動 | 使用文脈 |
|---|---|---|
| `header--sticky` ★既定 | 常時 sticky（スクロール中も上に固定）| 通常ページ全般（DNA 既定）|
| `header--scroll-up` | 下方向スクロール時に隠れ、上方向で再表示 | コンテンツ重視ページ（Blog 詳細 / Long LP）|
| `header--static` | sticky なし（スクロールで上に消える）| Hero と一体化させる演出（特殊）|

```css
/* 既定 = sticky */
.header,
.header--sticky {
  position: sticky;
  top: 0;
  z-index: var(--layer-4);  /* tokens.css: Sticky Header / Drawer */
}

.header--scroll-up {
  position: sticky;
  top: 0;
  z-index: var(--layer-4);
  transform: translateY(0);
  transition: transform var(--duration-base) var(--ease-out);
}

.header--scroll-up.is-hidden {
  transform: translateY(-100%);
}

.header--static {
  position: relative;
}
```

JS で `header--scroll-up` の `.is-hidden` 切替を制御（scrollY と prevY の差で判定）。

---

## Logo 配置（Q5 A 採択 — 左固定）

```css
.header__logo {
  display: flex;
  align-items: center;
  flex-shrink: 0;
  height: 100%;
  /* 高さに対して 50% を最大値とする */
  max-height: 50%;
}

.header__logo img {
  height: 100%;
  width: auto;
}
```

- 高さは Header 高さの 50% 上限（compact=32px / default=40px / tall=48px）
- `width: auto` で縦横比保持
- Drive 背景上には絶対に置かない（Anti）

---

## CTA 配置（Q6 A 採択 — Primary 1 個固定）

| 項目 | 値 |
|---|---|
| クラス | `btn btn-primary btn-md` |
| 配置 | Header 末尾（右端、Cart/Account の右） |
| 文言 | 暫定「話を聞いてみる」（cta-wording-proposal.md 連動）|
| 表示条件 | 全 Variants で 1 個必須（Minimal も同じ）|

PC / SP 共通で Primary 1 個を厳守。Header に複数 CTA を並べるのは Anti（階層崩壊）。

---

## SP 挙動（Q2 A 採択 — DNA 既定）

### 990px 以上（PC / Tablet 横）
- Logo + 横並びメニュー（中央）+ CTA（右）

### 990px 未満（SP / Tablet 縦）
- **横スクロールメニュー**（`overflow-x: auto`、スクロールバー非表示）
- ハンバーガー不採用 — DNA 違反のため絶対に作らない
- 補助として Shopify drawer を併用（既存 `header-drawer.liquid` 継承）

```css
@media (max-width: 989px) {
  .header__menu {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;  /* Firefox */
    white-space: nowrap;
  }
  .header__menu::-webkit-scrollbar {
    display: none;  /* Chrome/Safari */
  }
}
```

---

## States

### default
基準。`--bg-primary` 背景、`--color-ink` テキスト、border-bottom 1px `--border-light`。

### scroll-up Hidden（`.is-hidden` / `header--scroll-up` のみ）
下方向スクロール時。`transform: translateY(-100%)` で上にスライドアウト。

### menu hover（PC のみ）
メニュー項目 hover 時。`color: var(--color-drive)` + transition 0.2s ease。

### menu active（現在ページ）
メニュー項目に `aria-current="page"` または `.is-active` 付与時。
- 文字色 Drive
- 下線 2px Drive（offset 8px）

### CTA（btn-primary 継承）
button.md v0.3 の Primary State をそのまま継承（hover で translateY(-2px) + shadow-2 等）。

---

## 共通 Props

| プロパティ | 値 |
|---|---|
| background | `--bg-primary`（白） |
| color | `--color-ink` |
| border-bottom | `1px solid --border-light` |
| height | `--header--{compact/default/tall}`（64/80/96px） |
| padding | `0 --space-3`（24px・PC は --space-5 48px）|
| z-index | `--layer-4`（Sticky Header / Drawer 階層） |
| menu font-family | `--font-ja`（日本語ナビ）|
| menu font-size | `--fs-body`（16px）★Display サイズ禁止 |
| menu font-weight | `--fw-medium`（500） |
| menu hover transition | `color var(--duration-fast) var(--ease-out)` ★既存 0.2s 継承 |

---

## Liquid 実装例

### Standard（通常ページ TOP / 商品 / Blog）
```liquid
{% raw %}<header class="header header-standard header--default header--sticky">
  <div class="header__inner">
    {%- comment -%} Logo（左）{%- endcomment -%}
    <a href="{{ routes.root_url }}" class="header__logo" aria-label="{{ shop.name }}">
      {% if section.settings.logo %}
        {{ section.settings.logo | image_url: width: 256 | image_tag: loading: 'eager', alt: shop.name }}
      {% else %}
        <span class="header__logo-text">{{ shop.name }}</span>
      {% endif %}
    </a>

    {%- comment -%} Menu（中央 - PC 横並び / SP 横スクロール）{%- endcomment -%}
    <nav class="header__menu" aria-label="メインナビゲーション">
      <ul class="header__menu-list">
        {% for link in section.settings.menu.links %}
          <li class="header__menu-item">
            <a href="{{ link.url }}"
               class="header__menu-link {% if link.current %}is-active{% endif %}"
               {% if link.current %}aria-current="page"{% endif %}>
              {{ link.title }}
            </a>
          </li>
        {% endfor %}
      </ul>
    </nav>

    {%- comment -%} 右側ユーティリティ（Cart / Account / CTA）{%- endcomment -%}
    <div class="header__utilities">
      <a href="{{ routes.account_url }}" class="header__icon-link" aria-label="アカウント">
        {%- render 'icon', name: 'nav-user', size: 24 -%}
      </a>
      <a href="{{ routes.cart_url }}" class="header__icon-link" aria-label="カート">
        {%- render 'icon', name: 'nav-cart', size: 24 -%}
      </a>
      <a href="/contact" class="btn btn-primary btn-md" data-gtag-cta="header_main_cta">
        話を聞いてみる
      </a>
    </div>
  </div>
</header>{% endraw %}
```

### Minimal（LP / チェックアウト）
```liquid
{% raw %}<header class="header header-minimal header--default header--sticky">
  <div class="header__inner">
    <a href="{{ routes.root_url }}" class="header__logo">
      {{ section.settings.logo | image_url: width: 256 | image_tag: alt: shop.name }}
    </a>
    <a href="/contact" class="btn btn-primary btn-md">話を聞いてみる</a>
  </div>
</header>{% endraw %}
```

### Mega（カテゴリ展開・将来用）
```liquid
{% raw %}<header class="header header-mega header--default header--sticky">
  <div class="header__inner">
    <a href="{{ routes.root_url }}" class="header__logo">{{ section.settings.logo | image_url: width: 256 | image_tag: alt: shop.name }}</a>

    <nav class="header__menu" aria-label="メインナビゲーション">
      <ul class="header__menu-list">
        {% for link in section.settings.menu.links %}
          <li class="header__menu-item {% if link.links.size > 0 %}has-mega{% endif %}">
            <a href="{{ link.url }}" class="header__menu-link">{{ link.title }}</a>
            {% if link.links.size > 0 %}
              <div class="header__mega-panel" hidden>
                <ul class="header__mega-list">
                  {% for sublink in link.links %}
                    <li><a href="{{ sublink.url }}" class="header__mega-link">{{ sublink.title }}</a></li>
                  {% endfor %}
                </ul>
              </div>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    </nav>

    <div class="header__utilities">
      <a href="/contact" class="btn btn-primary btn-md">話を聞いてみる</a>
    </div>
  </div>
</header>{% endraw %}
```

---

## CSS（v0.2 実装）

```css
/* === Header 基本 === */
.header {
  position: sticky;
  top: 0;
  z-index: var(--layer-4);
  width: 100%;
  background: var(--bg-primary);
  color: var(--color-ink);
  border-bottom: 1px solid var(--border-light);
  height: 80px;  /* default */
}

.header__inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 var(--space-3);
}

@media (min-width: 1024px) {
  .header__inner {
    padding: 0 var(--space-5);
    gap: var(--space-3);
  }
}

/* === Heights === */
.header--compact { height: 64px; }
.header--default { height: 80px; }
.header--tall    { height: 96px; }

/* === Sticky Modes === */
.header--sticky {
  position: sticky;
  top: 0;
}

.header--scroll-up {
  position: sticky;
  top: 0;
  transform: translateY(0);
  transition: transform var(--duration-base) var(--ease-out);
}

.header--scroll-up.is-hidden {
  transform: translateY(-100%);
}

.header--static {
  position: relative;
}

/* === Logo === */
.header__logo {
  display: flex;
  align-items: center;
  flex-shrink: 0;
  height: 50%;
  text-decoration: none;
}

.header__logo img {
  height: 100%;
  width: auto;
}

.header__logo-text {
  font-family: var(--font-en);
  font-size: var(--fs-h3);
  font-weight: var(--fw-bold);
  color: var(--color-ink);
}

/* === Menu === */
.header__menu {
  flex: 1;
  display: flex;
  justify-content: center;
}

.header__menu-list {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  list-style: none;
  margin: 0;
  padding: 0;
}

.header__menu-link {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  font-weight: var(--fw-medium);
  color: var(--color-ink);
  text-decoration: none;
  letter-spacing: var(--ls-ja);
  white-space: nowrap;
  transition: color var(--duration-fast) var(--ease-out);
}

.header__menu-link:hover,
.header__menu-link:focus-visible {
  color: var(--color-drive);
}

.header__menu-link.is-active,
.header__menu-link[aria-current="page"] {
  color: var(--color-drive);
  text-decoration: underline;
  text-underline-offset: 8px;
  text-decoration-thickness: 2px;
}

/* === SP 横スクロールメニュー（DNA 既定）=== */
@media (max-width: 989px) {
  .header__menu {
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    white-space: nowrap;
  }
  .header__menu::-webkit-scrollbar { display: none; }

  .header__menu-list {
    gap: var(--space-2);
    padding: 0 var(--space-2);
  }
}

/* === Utilities（右側）=== */
.header__utilities {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-shrink: 0;
}

.header__icon-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  color: var(--color-ink);
  text-decoration: none;
  border-radius: var(--radius-pill);
  transition: background var(--duration-fast) var(--ease-out);
}

.header__icon-link:hover {
  background: rgba(27, 29, 26, 0.06);
}

.header__icon-link:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}

/* === Variant: Minimal === */
.header-minimal .header__menu,
.header-minimal .header__icon-link {
  display: none;
}

.header-minimal .header__inner {
  justify-content: space-between;
}

/* === Variant: Mega === */
.header-mega .header__menu-item.has-mega { position: relative; }

.header-mega .header__mega-panel {
  position: absolute;
  top: 100%;
  left: 0;
  background: var(--bg-primary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-3);
  padding: var(--space-3);
  min-width: 240px;
  z-index: var(--layer-4);
}

.header-mega .header__menu-item.has-mega:hover .header__mega-panel,
.header-mega .header__menu-item.has-mega:focus-within .header__mega-panel {
  display: block;
}

.header__mega-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.header__mega-link {
  display: block;
  padding: var(--space-1) 0;
  color: var(--color-ink);
  text-decoration: none;
  transition: color var(--duration-fast) var(--ease-out);
}

.header__mega-link:hover {
  color: var(--color-drive);
}
```

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| Logo | `<a>` でホームにリンク・`aria-label` 必須 |
| Menu | `<nav aria-label="メインナビゲーション">` で囲む |
| Active 状態 | `aria-current="page"` を必ず付与（`.is-active` と併用）|
| Icon link | `aria-label` で行先を明示（「カート」「アカウント」等） |
| Skip link | `<a class="skip-link">メインコンテンツへスキップ</a>` を Header 直前に推奨 |
| キーボード | Tab で全ての要素にフォーカス可・順序は Logo → Menu → Utilities |
| Mega Menu | `:focus-within` で展開、Esc で閉じる JS 推奨 |
| SP 横スクロール | スワイプ操作可・アクセシブル（ハンバーガーより SR フレンドリー） |

---

## Do / Don't

### ✅ Do
- 高さは `header--{compact/default/tall}` のいずれかを明示
- Sticky モードは `header--sticky / scroll-up / static` のいずれかを明示
- Logo は左固定
- CTA は Primary 1 個のみ（btn-primary btn-md）
- SP は横スクロールメニュー（DNA 既定）
- メニュー hover は `color 0.2s ease` で穏やかに

### ✕ Don't（Q7 A 禁止リスト準拠）
- ❌ **ハンバーガー単独運用**（DNA 違反 — 990px 未満は横スクロール + drawer 併用）
- ❌ **Header に Drive 色ベタ塗り**（うるさい / Anti）
- ❌ **Logo を Drive 色背景上に置かない**（視認性 / Anti）
- ❌ **メニューフォントを Display サイズ（48px+）にしない**（情報密度低下）
- ❌ Header 内に Primary CTA を 2 個並べない（階層崩壊）
- ❌ メニューにアイコンと文字を 2 段重ねしない（情報過剰）

---

## Brand DNA Anti との照合

本コンポは以下の Anti を踏まない:
- 表面的／派手 → border-bottom 1px / shadow なしで控えめ
- エセ高級 → グラデーション・ゴールドなし
- 媚びた広告 → 末尾 CTA のみ、Drive 推進感は維持しつつ静か

---

## L4 派生関係

| 派生 Component | 継承する Variant | 追加要素 |
|---|---|---|
| Article Header（Blog 記事冒頭）| Standard（compact）| Breadcrumb / カテゴリラベル |
| Checkout Header | Minimal（compact）| ステップ表示 |
| Sticky CTA Bar（Header 連動）| Minimal（compact）| 別 Component（layer-3）|

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `5. Components Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study`
- **Component Set ID**: `59:33` ✅（Audit #4 で既存確認、2026-05-12）
- **実装済 variants**: 3（`variant`: standard / minimal / mega）
- ⚠ Spec gap: spec の `height`（compact/default/tall）と `sticky-mode`（none/sticky/slide-down）は Figma 未実装。v0.3 で別 property として追加検討

## Change Log
- v0.2-figma (2026-05-12): Audit #4 で Component Set `59:33` を既存確認。3 variants 実装済、heights/sticky-mode は v0.3 で追加検討
- v0.2 (2026-04-28): Worksheet §18 確定（3 Variants / 3 Heights / 3 Sticky Modes / Logo 左固定 / Primary CTA 1 個 / SP 横スクロール DNA 既定 / 4 禁止項目明示）。既存 Liquid（fam/sections/header / fam-header-menu / fambox/sections/header）の実測抽出をベースに L4 Component 化
