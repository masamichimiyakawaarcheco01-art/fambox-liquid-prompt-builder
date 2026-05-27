---
title: FAMBOX DS — Naming Convention & Governance
type: design-system-operations
layer: L7-Operations
version: 0.2
status: confirmed
last_updated: 2026-04-28
owner: 宮川
purpose: DS の SSoT 宣言・命名規則・バージョニング・Contribution / Deprecate フローを統合した運用ルール。v0.2 完成基準として全 Spec ファイルが参照する基盤。
---

# FAMBOX DS — Naming Convention & Governance

## 0. SSoT（Single Source of Truth）宣言

### 各レイヤーの SSoT

| レイヤー | SSoT | 補足 |
|---|---|---|
| **Spec（設計の正）** | `brand/fambox/design-system/` 配下の `.md` ファイル | components / tokens / operations / current.md |
| **Tokens（変数の正）** | `brand/fambox/design-system/tokens/tokens.css` | Figma Variables / 各 .md の値はここから派生 |
| **Figma Library** | Figma File `QsiBrc2v20BYw76YHI9x3e` | Spec を視覚化したもの。差分は Spec 側を正とする |
| **Liquid 実装** | `projects/fam/sections/` `projects/fambox/sections/` `snippets/` | Spec を実装したもの。差分は Spec 側を正とする |

### 競合時のルール

```
.md Spec  ━━━━ master ━━━━━━┓
                              ↓
tokens.css ←─ 同期する ─────→ Figma Variables
                              ↓
                          Liquid 実装

差分発生時:
1. 必ず .md Spec を先に更新
2. tokens.css を Spec に合わせて更新
3. Figma Variables を tokens.css に合わせて更新
4. Liquid 実装を Spec に合わせて改修
```

---

## 1. 命名規則

### 1-A. CSS クラス命名

#### 基本形式
**`{component-name}` または `{component-name} {component-name}-{variant}`**

```css
.btn                            /* base class */
.btn.btn-primary                /* base + variant */
.btn.btn-primary.btn-md         /* base + variant + size */
.btn.btn-primary.btn-md.is-loading  /* base + variant + size + state */
```

#### Component 命名規則

| パターン | 例 | 用途 |
|---|---|---|
| `{name}` | `.btn` `.card` `.modal` | Base class（必須）|
| `{name}-{variant}` | `.btn-primary` `.card-featured` `.modal-confirmation` | Variant 修飾 |
| `{name}-{variant}-{sub}` | `.btn-secondary-ink` `.btn-secondary-drive` | サブ Variant（2語以上）|
| `{name}--{modifier}` | `.card--featured` `.hero--full` | Modifier（状態以外の調整）|
| `.is-{state}` | `.is-loading` `.is-active` `.is-selected` `.is-open` | 状態（State）|
| `.has-{property}` | `.has-icon` `.has-badge` | 構造的プロパティ |

#### 命名禁止事項

- ❌ camelCase（`btnPrimary`）
- ❌ snake_case（`btn_primary`）
- ❌ PascalCase（`BtnPrimary`）
- ❌ 番号サフィックス（`.btn-1`、`.btn-v2`）— 例外: Bento Tile sizes（`tile-1x1` 等）
- ❌ ブランド名直書き（`.fambox-btn`）— DS は中立に保つ

#### 内部要素命名（BEM ライト）

```css
.card                  /* Block */
.card__title           /* Element（Block の子）*/
.card__media           /* Element */
.card__body            /* Element */
.card.is-selected      /* Modifier（State）*/
```

`__` は Element、`--` は Modifier。Component を超えた粒度では使わない。

### 1-B. Token 命名（CSS Variables）

#### 基本形式
**`--{category}-{name}` または `--{category}-{name}-{variant}`**

```css
--color-drive                   /* category: color, name: drive */
--color-drive-light             /* category: color, name: drive, variant: light */
--space-3                       /* category: space, name: 3 (sequential) */
--fs-body                       /* category: fs (font-size), name: body */
--fw-bold                       /* category: fw (font-weight), name: bold */
--radius-md                     /* category: radius, name: md */
--shadow-1                      /* category: shadow, name: 1 (sequential) */
--layer-3                       /* category: layer, name: 3 (sequential) */
--duration-base                 /* category: duration, name: base */
--ease-out                      /* category: ease, name: out */
```

#### Category prefix 表

| Prefix | 意味 | 例 |
|---|---|---|
| `color-` | カラー（meaning ベース）| `--color-drive` `--color-ink` `--color-success` |
| `bg-` | 背景 | `--bg-primary` `--bg-secondary` `--bg-tertiary` |
| `border-` | ボーダー色 | `--border-base` `--border-light` |
| `space-` | スペーシング（数値順）| `--space-1` 〜 `--space-8` |
| `fs-` | font-size | `--fs-body` `--fs-h1` `--fs-display` |
| `fw-` | font-weight | `--fw-regular` `--fw-bold` |
| `lh-` | line-height | `--lh-body` `--lh-heading` |
| `ls-` | letter-spacing | `--ls-en` `--ls-ja` |
| `radius-` | border-radius | `--radius-md` `--radius-pill` |
| `shadow-` | box-shadow（数値順）| `--shadow-1` 〜 `--shadow-5` |
| `layer-` | z-index（数値順）| `--layer-base` 〜 `--layer-6` |
| `duration-` | アニメ duration | `--duration-fast` `--duration-base` `--duration-slow` |
| `ease-` | easing | `--ease-in` `--ease-out` `--ease-inout` |
| `bw-` | border-width | `--bw-thin` `--bw-thick` |
| `font-` | font-family | `--font-en` `--font-ja` |

#### Token 命名禁止事項

- ❌ Hex 値の直接埋込（`--color-FB4C15`）— meaning ベースにする
- ❌ Component 固有の命名（`--card-padding`）— Component 内では `var(--space-3)` のように汎用 Token を使う
- ❌ ブランド名 prefix（`--fambox-color`）

### 1-C. Liquid Snippet 命名

#### 基本形式
**`{kebab-case-name}.liquid`**

```
snippets/icon.liquid
snippets/form-field.liquid
snippets/card-product.liquid
snippets/header-drawer.liquid
```

- 全小文字、ハイフン区切り
- Component 名と一致が原則
- Shopify 標準（`card-product` 等）はそのまま継承

### 1-D. Section / Liquid Section 命名

| 範囲 | プレフィックス | 例 |
|---|---|---|
| FAM 共通 | `fam-` | `fam-header.liquid` `fam-corp-hero.liquid` |
| FAMBOX 専用 | `fambox-` | `fambox-hero-v17.liquid` `fambox-faq.liquid` |
| Shopify 標準 | プレフィックスなし | `header.liquid` `footer.liquid` `main-product.liquid` |

### 1-E. Figma 内 Component 命名

#### 基本形式
**`{category}/{name}-{variant}` または `{component}/{variant}/{size}`**

スラッシュ階層化で Figma Assets パネルの自動フォルダ化を活用。

```
icon/nav/close-ink
icon/action/download-drive
icon/domain/athlete-white

button/primary/md
button/secondary-ink/lg

card/standard/default
card/featured/default

bento-tile/glass/2x2
bento-grid/editorial/default
```

### 1-F. Figma Variables 命名

CSS Token と完全一致させる（`--` プレフィックスを除く）:

```
color/drive
color/drive-light
space/3
fs/body
radius/md
```

---

## 2. Versioning Policy

### 2-A. DS 全体のバージョニング

[Semantic Versioning 2.0.0](https://semver.org/) に準拠:

```
v{MAJOR}.{MINOR}.{PATCH}
   |       |        |
   |       |        └── バグ修正・微調整（互換性あり）
   |       └─────────── 機能追加・新 Variant（互換性あり）
   └─────────────────── 破壊的変更・命名変更（互換性なし）
```

#### 例
- v0.1 → v0.2: MINOR up（新 Component 追加・互換性あり）
- v0.2.1: PATCH up（typo 修正・微調整）
- v1.0.0 → v2.0.0: MAJOR up（破壊的変更）

### 2-B. Component 個別のバージョニング

Spec ファイルの frontmatter に `version` を記載:

```yaml
---
version: 0.3
status: confirmed
---
```

| 状態 | 意味 |
|---|---|
| `seed` | 初期 draft / 検証中 |
| `confirmed` | v0.X として確定（実装可能） |
| `stable` | 本番運用中 / 後方互換あり |
| `deprecated` | 廃止予告中（次の MAJOR で削除） |

### 2-C. リリースサイクル

| サイクル | 頻度 | 内容 |
|---|---|---|
| **PATCH リリース** | 随時 | バグ修正・typo・軽微な値調整 |
| **MINOR リリース** | 月次目安 | 新 Component / Variant 追加 |
| **MAJOR リリース** | 四半期 / 半年 | 破壊的変更・命名規則の大幅改定 |

### 2-D. v0.2 → v0.5 → v1.0 の予定（current.md と連動）

- **v0.2**（2026-04-27 達成）: Worksheet §1-§14 + 拡張 §15-§23 / Tokens + 主要 Components 確定
- **v0.5**（2026-06-30 予定）: Brand DNA v1.0 連動 / L0 Foundation 翻訳表確定 / Figma Library Publish
- **v1.0**（2026-09-30 予定）: 主要画面適用率 100% / 運用ルール完全版（Contribution Process / Deprecate Rule 含む）

---

## 3. Contribution Process（v0.2 暫定版）

### 3-A. 新 Component を追加する手順

```
[1] Worksheet § 追加（質問形式）
      ↓
[2] チャットで Q&A 確定
      ↓
[3] components/{name}.md（v0.2 confirmed）作成
      ↓
[4] tokens.css / 既存 Spec への影響確認・更新
      ↓
[5] Worksheet ✅ マーク同期 + session_log 追記
      ↓
[6] CHANGELOG.md にエントリ追加
      ↓
[7] current.md milestone 行追記
      ↓
[8] git commit（feat(ds): add ... 形式のメッセージ）
      ↓
[9] Figma Library に反映（別セッション・別ブロック）
      ↓
[10] Liquid 実装（必要時・Critical Path に応じて）
```

### 3-B. 既存 Component を改訂する手順

```
[1] 改訂理由を CHANGELOG.md に明記
      ↓
[2] components/{name}.md の version を bump（PATCH or MINOR）
      ↓
[3] frontmatter の last_updated 更新
      ↓
[4] Change Log セクションに変更内容追記
      ↓
[5] 影響範囲の Liquid を grep で洗い出し
      ↓
[6] 必要なら Worksheet § も更新（決定変更の場合）
      ↓
[7] git commit
      ↓
[8] Figma / Liquid 反映
```

### 3-C. 命名変更（破壊的変更）の手順

MAJOR バージョン up が必要:

```
[1] 旧クラス名を deprecated 扱いとする（CSS は維持）
      ↓
[2] 新クラス名を追加（共存期間を作る）
      ↓
[3] CHANGELOG.md と Component Spec の Change Log に Migration Guide 記載
      ↓
[4] 2 MINOR バージョン分の共存期間（例: v1.0 → v1.2 まで両方サポート）
      ↓
[5] 次の MAJOR で旧クラス名を削除
```

---

## 4. Deprecate Rule（v0.2 暫定版）

### 4-A. 廃止フロー

```
v{N}.x          → 廃止予告: status: deprecated に変更 + Spec に廃止理由・移行先記載
v{N+1}.x        → 共存期間: 旧 + 新 両方サポート
v{N+2}.0        → 削除: 旧クラス・旧 Spec を削除（CHANGELOG に削除記録）
```

### 4-B. Deprecated Spec の記載例

```yaml
---
version: 0.5
status: deprecated
deprecated_in: v0.5
removed_in: v1.0
migration_to: components/new-component.md
deprecation_reason: 命名規則の統一のため `card-old` を `card-legacy` にリネーム
---
```

### 4-C. Legacy 互換枠（tokens.css）

`tokens.css` には `Legacy 互換枠` セクションがあり、廃止予定の Token を一時保持:

```css
/* Legacy 互換枠（v0.5 で廃止予定・新規使用禁止）*/
--z-legacy-sticky-cta: 9990;
```

新規 Component はここを使わない。既存 Component の段階移行のみ。

---

## 5. Branch & Commit 規約

### 5-A. Branch 命名（参考）

```
feature/ds-{component}     新規 Component 追加
fix/ds-{issue}             修正
refactor/ds-{component}    リファクタ
docs/ds-{topic}            ドキュメント更新
```

### 5-B. Commit メッセージ

[Conventional Commits](https://www.conventionalcommits.org/) に準拠:

```
feat(ds): add L4 Modal v0.2 (3 variants × backdrop fixed)
fix(ds): correct hero-section padding in SP layout
refactor(ds): unify button variant naming
docs(ds): update card.md migration guide
```

| Prefix | 用途 |
|---|---|
| `feat(ds):` | 新規 Component / 機能追加 |
| `fix(ds):` | バグ修正・調整 |
| `refactor(ds):` | 構造変更（仕様変更なし）|
| `docs(ds):` | ドキュメント更新のみ |

### 5-C. Commit 粒度

- **1 Component = 1 コミット**を原則
- 関連する複数 Component を 1 セッションで作る場合は別 commit
- 例外: 同じ Worksheet § で複数 Component を統合確定する場合（Bento Tile + Bento Grid 等）は 1 commit

---

## 6. v0.2 の運用上の課題（v0.3 で解決予定）

| 課題 | 内容 | 対応予定 |
|---|---|---|
| **Lint 自動化** | クラス名・Token 使用の Lint 検出が手動。stylelint 等の導入未定 | v0.5 |
| **Figma 同期の自動化** | tokens.css ⇄ Figma Variables を Tokens Studio Plugin 等で半手動同期 | v0.5 |
| **Storybook 等の動作確認環境** | 未整備 | v1.0 |
| **アクセシビリティ自動チェック** | axe-core 等の導入未定 | v0.8 |
| **Contribution Process の Slack / Notion 化** | 現状 git commit のみで運用 | v1.0 |
| **多言語対応** | 命名規則は英語ベースだが、Spec / Worksheet は日本語のまま運用 | v1.0 で英訳 |

---

## 7. 参照

- DS 全体構造: [current.md](../current.md)
- Token SSoT: [tokens/tokens.css](../tokens/tokens.css)
- Figma 構築手順: [operations/figma-master-setup-guide.md](figma-master-setup-guide.md)
- Worksheet（Spec 起源）: [DS_INPUT_WORKSHEET.md](../DS_INPUT_WORKSHEET.md)
- 全変更履歴: [brand/CHANGELOG.md](../../../CHANGELOG.md)

---

## Change Log

- v0.2 (2026-04-28): 初版（Naming Convention + SSoT + Versioning + Contribution + Deprecate を統合）
