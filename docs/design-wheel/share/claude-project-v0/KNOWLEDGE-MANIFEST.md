# 知識ファイル マニフェスト — Project にアップロードするもの

> claude.ai の Design Wheel Project の「ナレッジ（添付ファイル）」に、以下を**ドラッグして登録**する。
> これが「アプリのコンテンツ」。宮川が改訂したらここを差し替える（= アップデート。手順は PUBLISH.md）。

## まず登録する土台（全パターン共通・最優先）

| レイヤー | アップロードするファイル | 役割 |
|---|---|---|
| ① 普遍 | `foundations/FOUNDATIONS.md` | 比率・余白・キャラクターライン・タイポ・状態の作法。**全生成の土台** |
| ③ 条件 | `foundations/BRIEF.md` | 依頼ごとの6因子ヒアリング → パラメータ翻訳 |
| ①印刷 | `foundations/PRINT-LAYOUT.md` | チラシ（flyer）時の印刷レイアウト作法（A4固定・ブロッキング先行等） |

> これらは Layer ②（各 SYSTEM）より先に効く。教材「UIデザインの基本」全121pを蒸留したもの。

## v0 で登録するファイル（在庫4パターン＝Layer ②）

リポジトリの真ソースから、以下をアップロード：

| パターン | アップロードするファイル |
|---|---|
| corporate | `patterns/corporate/SYSTEM.md` |
| digital | `patterns/digital/SYSTEM.md` ＋ `ds-bundle/_upload/digital-SYSTEM-spec.md` |
| gradient | `patterns/gradient/SYSTEM.md` |
| sporty | `patterns/sporty/SYSTEM.md`（2 sub-style）＋ `ds-bundle/sporty-product-ui/product-ui-SYSTEM-spec.md` |
| fambox | `patterns/fambox/SYSTEM.md`（FAM ブランド・3配色サブスタイル：SNS/Web/Print） |

※ パス基準 = `docs/design-wheel/`。
※ 余裕があれば各 `ds-bundle/<p>/` の HTMLカード（色・フォントの実例）も足すと精度が上がる。

## MVP の絞り込み（推奨）
最初の1周は **digital と sporty(product-UI) の2つだけ**で始めてもよい
（在庫が最も強く・写真不要で非デザイナーが完結しやすい）。痛点が見えたら他も足す。

## 注意
- 画像参照（`../../brain/...`）はリンク切れになるが、SYSTEM の**値（色/フォント/余白/規律）が本体**なので問題ない。
- ファイルを更新したら必ず Project 側も差し替える（古いコピーが残ると分岐する）。
