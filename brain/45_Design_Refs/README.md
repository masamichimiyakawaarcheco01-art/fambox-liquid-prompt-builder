# 45_Design_Refs — デザイン参考リファレンス

PinterestピンやURLから集めるデザイン参考の知識ベース。視覚優先・スタイル/コンポーネント横串で参照する。

## ディレクトリ構造

```
45_Design_Refs/
├── README.md
├── _index.md              # 全件時系列（追加順 or 投稿順）
├── _by-style/             # スタイル別 wiki
│   ├── minimal.md
│   ├── editorial.md
│   ├── glassmorphism.md
│   └── ...
├── _by-component/         # コンポーネント別 wiki
│   ├── hero.md
│   ├── pricing.md
│   ├── navigation.md
│   └── ...
├── _assets/               # スクリーンショット保存（任意）
└── YYYY/MM/<slug>.md      # 個別ノート
```

## 取り込み方法

**`/design-ref <URL>`** コマンドを使う。対応URL:

| ソース | 例 |
|---|---|
| Pinterestピン | `https://pin.it/xxx` または `https://www.pinterest.com/pin/123456/` |
| デザインサイト | Awwwards / SiteInspire / Lapa.ninja / Cssdesignawards |
| 任意のWebサイト | Linear, Stripe, Vercel 等の参考にしたいサイト |
| ブログ記事 | デザイン関連の記事URL |

実行内容:
1. URL からタイトル・og:image・説明を抽出
2. （可能なら）Chrome MCP でページのスクショを `_assets/` に保存
3. スタイル・コンポーネント分類を推定
4. `YYYY/MM/<slug>.md` に構造化保存
5. `_index.md` と `_by-style/`, `_by-component/` の該当wikiを更新

## 個別ノートのスキーマ

```yaml
---
title: <サイト/ピン名>
url: <元URL>
type: pinterest-pin | site | dribbble | awwwards | article | other
date_added: YYYY-MM-DD
date_posted: YYYY-MM-DD  # 元コンテンツの日付（取れれば）
author: <作者・サイト名>
styles: [minimal, dark]
components: [hero, pricing-table]
colors: [#色1, #色2]   # 任意
mood: editorial        # 任意 (editorial, playful, corporate, ...)
screenshot: _assets/YYYY-MM-DD_<slug>.png  # 任意
status: inbox | reviewed | applied
---

# <タイトル>

## なぜ保存したか
- ...

## 注目ポイント
- **レイアウト**: ...
- **色使い**: ...
- **タイポグラフィ**: ...
- **インタラクション/モーション**: ...

## ARCHECO/FAMBOXでの応用案
- ...

## 元情報
- URL: <元URL>
- 著者/サイト: ...

## Wiki
- [[../_by-style/...]]
- [[../_by-component/...]]
```

## 既存システムとの関係

- **`40_Bookmarks/`**: X専用、自動同期、流量物
- **`45_Design_Refs/`**: マルチソース、手動 or オンデマンド、視覚重視
- **`30_Tech_Notes/`**: 永続的技術知識（記事・原則・SOP）
- **`docs/okr/references/`**: FAMBOX OKR用の参考素材（DNA汚染防止のため引用範囲限定）

`docs/okr/references/` と異なり、`45_Design_Refs/` は **DNA汚染防止ルールなし** の自由な参考エリア。応用するときに「これはFAM/FAMBOXに合うか」を判断する。

## wheel-pattern タグ軸（2026-06-09 追加 / Design Wheel 連携）

FAMBOX軸（意味/隠喩）とは**直交**する表層スタイルの軸。Design Wheel の
パターン在庫（`docs/design-wheel/`）と連動する。

- 値: `geometric / corporate / grid / digital / sporty / lab`
- 記法: 各 ref ファイルの front-matter またはタグ行に `wheel-pattern: <値>` を併記。
- FAMBOX軸タグは従来通り維持（2軸＝意味×スタイルで引ける）。
- `_by-style/` 仕組みとは共存（重複可）。
