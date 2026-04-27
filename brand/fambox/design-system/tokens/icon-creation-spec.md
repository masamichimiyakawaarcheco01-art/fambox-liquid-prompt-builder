---
title: FAMBOX Icon — 作成・エクスポート・格納 仕様
type: design-system-reference
layer: L1-Tokens-Icon
status: active
last_updated: 2026-04-27
owner: 宮川
purpose: Figma でのアイコン作成サイズ・形式・格納場所を標準化し、宮川さん制作 → Claude/Shopify で即使える状態にする
---

# FAMBOX Icon — 作成・エクスポート・格納 仕様

[icon-inventory.md](icon-inventory.md) のアイコンを**実際に作る**ための実務仕様。

> **v0.3 訂正履歴（2026-04-27）**: Worksheet §5.2 確定により、本仕様の master 描画サイズを **既存 `brand/shared/icons/` 実測値（24×24）に整合**。32×32 推奨記述は撤回。色運用も `currentColor` 単一案 → **3バリアント別ファイル（default/drive/white）の現行運用** に再確定。

---

## 1. Figma マスターサイズ（1択で確定）

### 採用: **24×24px マスター** ＋ **2px セーフティ余白**

既存 `brand/shared/icons/` 配下の自作SVGが全て `viewBox="0 0 24 24"` で運用中（実測）。これを SSoT として固定。

```
┌─────────────────┐ ← 24×24px フレーム（外枠）
│ ┌─────────────┐ │
│ │             │ │ ← 20×20px Safe Area（描画可能域）
│ │   [ ICON ]  │ │
│ │             │ │
│ └─────────────┘ │
└─────────────────┘
  ↑ 上下左右に 2px の余白
```

### なぜ 24×24px マスターか？

| サイズ | Figma標準 | 既存資産整合 | 1.5px stroke 表示 |
|---|---|---|---|
| 16×16 | ✓ | × | 過大 |
| **24×24** ★採用 | ✓ (定番) | ✅ 既存自作SVG全件と一致 | 1.5px 適正 |
| 32×32 | ✓ | × 既存資産と不整合 | 1.5px 正確だが過剰品質 |
| 48×48 | △ | × | 複雑になりすぎる |

**結論**: 24×24px で作成 → SVG は無限スケール、CSSで 16/24/32/48 表示OK

### 描画ルール

| 項目 | 仕様 |
|---|---|
| フレーム | **24 × 24 px** |
| Safe Area | 20 × 20 px（上下左右 2px 余白） |
| 最小ストローク | **1.5 px**（既存実測） |
| ベースラインGrid | **1 px** |
| コーナー | round or square（アイコンの性格で使い分け・Brand DNAと整合） |
| 色 | **3バリアント別ファイル方式**（下記§2参照／`currentColor` 単一案は不採用） |
| 塗り | **線画 Stroke のみ**（fill 原則使用禁止）|
| 線端 | **round**（柔らかさ・Brand DNAに沿う）|
| 線結合 | **round** |

---

## 2. エクスポート形式（SVG 一択）

### 採用: **SVG（Scalable Vector Graphics）+ 3色バリアント運用**

**理由**:
- 無限スケール（16px〜256px 画質劣化なし）
- 3色バリアント（Ink/White/Drive）を別ファイルで持つ → 背景色に応じて即切替・CSS依存なし
- Shopify Liquid で inline 埋め込み可能
- ファイルサイズ小（1-3KB/個）
- アクセシビリティ（`<title>`・`aria-label` 組込可能）

### 3色バリアント運用（2026-04-20 確定 / 2026-04-27 再確認）

各色は SVG ファイル内に直接 hex 値で記述（`currentColor` を使わず3ファイル分割）。背景色に応じて読み込むファイルを切り替える運用。

| バリアント | ファイル名サフィックス | 色 | 用途 |
|---|---|---|---|
| Ink（デフォルト）| なし（`{cat}-{name}.svg`）| `#1B1D1A` | 明るい背景上 |
| White | `-white.svg`（`{cat}-{name}-white.svg`）| `#FFFFFF` | 暗い背景・Drive背景上 |
| Drive | `-drive.svg`（`{cat}-{name}-drive.svg`）| `#FB4C15` | アクセント・CTA連動 |

**理由**:
- メーラー・古いブラウザでも色が確実に出る（`currentColor` 非対応環境への保険）
- Liquid 側が単純（`render 'icon', name: 'nav-close-drive'` で完結、CSS 干渉不要）
- ファイル数は増えるが SVG 1-3KB のため転送量影響軽微

詳細は [shared/icons/README.md](../../../shared/icons/README.md) を参照。

### エクスポート設定（Figma）

Figma の Export パネルで以下を設定:
| 項目 | 値 |
|---|---|
| Format | **SVG** |
| Suffix | なし |
| Include "id" attribute | ✕ OFF |
| Outline text | ✓ ON |
| Include bounding box | ✕ OFF |
| Simplify stroke | ✓ ON |

### SVG クリーンアップ（Figma出力後に必須）

Figma 出力の SVG には冗長な属性が入るので、**SVGO で最適化**して使う。推奨設定:

```bash
# コマンド例（SVGO インストール済み前提）
svgo --multipass \
     --enable=removeDimensions \
     --disable=removeViewBox \
     input.svg -o output.svg
```

**手作業時のチェックリスト**:
- [ ] `<svg width="24" height="24" viewBox="0 0 24 24">` 形式（既存資産と統一）
- [ ] `stroke="#1B1D1A"`（Ink）/ `#FFFFFF`（White）/ `#FB4C15`（Drive）— 3バリアントで別ファイル
- [ ] `stroke-width="1.5"` 明示
- [ ] `stroke-linecap="round"`
- [ ] `stroke-linejoin="round"`（曲がりがある場合）
- [ ] 不要な `<g>` や `id` 属性を削除
- [ ] インデントは 2 spaces

### SVG テンプレート（基準雛形・既存実測準拠）

`brand/shared/icons/nav/nav-close.svg` の実形式:

```xml
<!-- nav-close.svg（Ink default）-->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M6 6L18 18" stroke="#1B1D1A" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M18 6L6 18" stroke="#1B1D1A" stroke-width="1.5" stroke-linecap="round"/>
</svg>
```

```xml
<!-- nav-close-drive.svg（Drive variant）-->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M6 6L18 18" stroke="#FB4C15" stroke-width="1.5" stroke-linecap="round"/>
  <path d="M18 6L6 18" stroke="#FB4C15" stroke-width="1.5" stroke-linecap="round"/>
</svg>
```

### PNG を出力する場合（例外用途）

基本不要だが、以下の用途でのみ PNG 書き出し:
- OGP / SNSカード（1200×630 内の装飾）
- メール HTML（SVG が一部メーラーで非対応）
- 印刷物

→ 必要時のみ「@2x / @3x の PNG」を別途エクスポート。

---

## 3. 格納フォルダ構造

### 二層構造（マスター ＋ デプロイ）

```
brand/
└── shared/
    └── icons/                     ← 🎯 マスター（Single Source of Truth）
        ├── _master.fig.md         ← Figma マスターファイル参照メモ
        ├── nav/                   ← Navigation / Structure
        │   ├── nav-close.svg
        │   ├── nav-menu.svg
        │   ├── nav-search.svg
        │   └── ...
        ├── action/                ← Action
        │   ├── action-download.svg
        │   ├── action-edit.svg
        │   └── ...
        ├── content/               ← Content / Media
        │   ├── content-play.svg
        │   ├── content-document.svg
        │   └── ...
        ├── status/                ← Status / Feedback
        ├── comm/                  ← Communication / Contact
        ├── social/                ← Social
        ├── domain/                ← ★ FAMBOX独自（athlete/team/meal/etc）
        │   ├── domain-athlete.svg
        │   ├── domain-team.svg
        │   ├── domain-meal.svg
        │   └── ...
        ├── commerce/              ← Commerce
        └── misc/                  ← Misc

projects/fambox/assets/           ← 🚀 デプロイ先（Shopifyテーマ用コピー）
└── icons/
    └── （マスターから必要なものをコピー）
```

### なぜ二層構造？
- **マスター**: バージョン管理・編集・全体把握用
- **デプロイ**: Shopify テーマ配下・本番稼働用
- マスター → デプロイは手動コピー or スクリプト同期（詳細は§5）

---

## 4. 命名規則

### ファイル名

**形式**: `{category}-{name}.svg`

- 全小文字
- ハイフン区切り
- 拡張子は `.svg`

**例**:
- ✅ `nav-close.svg`
- ✅ `domain-athlete.svg`
- ✅ `action-download.svg`
- ❌ `navClose.svg`（camelCase禁止）
- ❌ `nav_close.svg`（underscore禁止）
- ❌ `NavClose.svg`（PascalCase禁止）

### カテゴリ（全9種・icon-inventory.md と完全一致）

| コード | 意味 |
|---|---|
| `nav` | Navigation / Structure |
| `action` | Action |
| `content` | Content / Media |
| `status` | Status / Feedback |
| `comm` | Communication / Contact |
| `social` | Social |
| `domain` | Sports / Nutrition（FAMBOX独自）|
| `commerce` | Commerce |
| `misc` | Misc |

---

## 5. Shopify 統合（Liquid 側の読み込み）

### パターンA: Liquid snippet 経由（推奨）

`snippets/icon.liquid` を作って、全アイコンを1箇所で管理:

```liquid
{% raw %}{% comment %}
  Usage: {% render 'icon', name: 'nav-close', size: 24 %}
{% endcomment %}

{%- assign size = size | default: 24 -%}

{% case name %}
  {% when 'nav-close' %}
    <svg width="{{ size }}" height="{{ size }}" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <line x1="8" y1="8" x2="24" y2="24"/>
      <line x1="24" y1="8" x2="8" y2="24"/>
    </svg>
  {% when 'nav-menu' %}
    <!-- ... -->
{% endcase %}{% endraw %}
```

**使い方**:
```liquid
{% raw %}{% render 'icon', name: 'nav-close', size: 24 %}{% endraw %}
```

**メリット**:
- SVGインライン → CSS で色制御可能
- サイズ可変
- アクセシビリティ属性組込
- 軽量（外部ファイル取得不要）

### パターンB: `assets/` に置いて `asset_url` 参照

```liquid
{% raw %}<img src="{{ 'nav-close.svg' | asset_url }}" alt="閉じる" width="24" height="24">{% endraw %}
```

**欠点**: 色変更できない（CSS で操作不可）→ 単色アイコンには不向き

### 結論

**パターンA（snippet経由）を採用**。マスターSVG → snippets/icon.liquid の `case 文` に手動転記。将来的に自動生成スクリプトで運用。

---

## 6. 運用ワークフロー（作成 → デプロイ）

```
[1] Figma マスターファイルで作成・編集
      ↓ Export SVG (32×32 / currentColor)
[2] SVGO で最適化（または手動クリーンアップ）
      ↓
[3] brand/shared/icons/{category}/{name}.svg に保存
      ↓
[4] snippets/icon.liquid の case 文に追記
      ↓
[5] Shopifyテーマ反映（コードエディタで更新）
      ↓
[6] ブラウザ確認（render 正常・色変更OK）
```

### 追加したい時のチェックリスト

- [ ] Figma マスターで 32×32 フレームに描画
- [ ] ストローク 1.5px / currentColor / round
- [ ] Export SVG（cleanUp 済）
- [ ] `brand/shared/icons/{category}/{name}.svg` に保存
- [ ] ファイル名が `{category}-{name}.svg` 形式
- [ ] [icon-inventory.md](icon-inventory.md) の該当行で Status を ✅ 更新
- [ ] snippets/icon.liquid に `{% raw %}{% when '{name}' %}{% endraw %}` 追記
- [ ] Shopify テーマにデプロイ・動作確認

---

## 7. Figma マスターファイル構成（推奨）

```
FAMBOX_Icons.fig（マスター）
├── Cover Page
├── Icon Components
│   ├── Navigation (8 icons)
│   ├── Action (10 icons)
│   ├── Content (7 icons)
│   ├── Status (7 icons)
│   ├── Communication (6 icons)
│   ├── Social (6 icons)
│   ├── Domain ★FAMBOX (16 icons)
│   ├── Commerce (7 icons)
│   └── Misc (7 icons)
├── Usage Guide（サイズ例・色例）
└── Change Log
```

### Figma Tips
- **Component 化必須**: 各アイコンを Component にする（Variant不要）
- **Main Component は 32×32**
- **Library 公開**: FAMBOX Design System として Team Library に公開
- **命名**: Figma 内名称も `nav/close`, `domain/athlete` のように スラッシュ区切り（フォルダ化される）

---

## 8. まとめ：宮川さんの作業順

1. Figma に **FAMBOX_Icons** ファイルを新規作成（要 M3 マスターファイル前提）
2. カテゴリごとに 32×32 フレームを Component として配置
3. ★★★ アイコン約20個を優先的に描画
4. SVG エクスポート → SVGO → `brand/shared/icons/{category}/` に保存
5. `snippets/icon.liquid` に順次追記
6. [icon-inventory.md](icon-inventory.md) の Status を ✅ に更新

### 目安工数
- 描画: 1 icon あたり **5-15分**（Lucide参考）
- 全50個（★3+★2）: **8-12時間** = 2-3日
- ★3 の20個だけなら **3-4時間**

---

## 9. 質問への直接回答（まとめ・v0.3 更新）

| 質問 | 回答 |
|---|---|
| どれくらいのサイズで作る？ | **Figma 24×24px** マスター（Safe Area 20×20px・既存資産と整合）|
| どの形式で書き出す？ | **SVG**（3色バリアント別ファイル: default / -drive / -white）|
| どこに格納する？ | マスター: `brand/shared/icons/{category}/`<br>デプロイ: `snippets/icon.liquid` の case 文 or `assets/icons/` |
| 命名規則は？ | `{category}-{name}{-variant}.svg`（小文字＋ハイフン、variant省略時=Ink）|
| ストローク幅は？ | **1.5px**（24×24 マスター基準・実測値） |
| 塗り or 線画？ | **線画のみ**（fill なし）|
| Figma 内の命名は？ | `icon/{category}/{name}-{variant}` でスラッシュ階層化（ファイル名と並列維持） |

必要なら次セッションで `snippets/icon.liquid` の雛形＋最初のアイコン5個（例: nav-close, nav-menu, action-download, content-play, status-check）の SVG テンプレートを生成します。
