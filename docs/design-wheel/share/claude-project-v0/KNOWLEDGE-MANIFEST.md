# 知識ファイル マニフェスト — Project にアップロードするもの

> claude.ai の Design Wheel Project の「ナレッジ（添付ファイル）」に、以下を**ドラッグして登録**する。
> これが「アプリのコンテンツ」。宮川が改訂したらここを差し替える（= アップデート。手順は PUBLISH.md）。

## v0 で登録するファイル（在庫4パターン）

リポジトリの真ソースから、以下をアップロード：

| パターン | アップロードするファイル |
|---|---|
| corporate | `patterns/corporate/SYSTEM.md` |
| digital | `patterns/digital/SYSTEM.md` ＋ `ds-bundle/_upload/digital-SYSTEM-spec.md` |
| gradient | `patterns/gradient/SYSTEM.md` |
| sporty | `patterns/sporty/SYSTEM.md`（2 sub-style）＋ `ds-bundle/sporty-product-ui/product-ui-SYSTEM-spec.md` |

※ パス基準 = `docs/design-wheel/`。
※ 余裕があれば各 `ds-bundle/<p>/` の HTMLカード（色・フォントの実例）も足すと精度が上がる。

## MVP の絞り込み（推奨）
最初の1周は **digital と sporty(product-UI) の2つだけ**で始めてもよい
（在庫が最も強く・写真不要で非デザイナーが完結しやすい）。痛点が見えたら他も足す。

## 注意
- 画像参照（`../../brain/...`）はリンク切れになるが、SYSTEM の**値（色/フォント/余白/規律）が本体**なので問題ない。
- ファイルを更新したら必ず Project 側も差し替える（古いコピーが残ると分岐する）。
