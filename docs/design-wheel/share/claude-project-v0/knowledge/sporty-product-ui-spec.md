# sporty / product-UI — DS Bundle spec（Claude Design 登録用）

> sporty パターンの sub-style **A: product-UI**。真ソース= `patterns/sporty/SYSTEM.md v1`。
> ユーザー refs（Nike Run+ / PLAYPAD / NestEgg）から確定。Nike Run Club 級の洗練が目標。

## カード構成
| ファイル | group | name |
|---|---|---|
| 00-color.html | Foundations · sporty-product-UI | Color |
| 01-type.html | Foundations · sporty-product-UI | Type scale |
| 02-spacing.html | Foundations · sporty-product-UI | Spacing & grid |
| 10-components.html | Components · sporty-product-UI | Buttons, chips, tiles |
| 11-dataviz.html | Components · sporty-product-UI | Data viz (signature) |
| _sample-pulse-LP.html | — | サンプルLP（PULSE / v3 実証） |

## 一言定義
ダークテーマ × 電光アクセント × データ可視化で「精度・先端」を説得する sporty。
写真主役の poster 型とは別系統。**写真不要で完結**＝非デザイナー運用に最適。

## 凍結トークン（変更禁止）
- bg #0A0C0B / surface #14171A / surface-2 #1C2024 / line #272C30
- accent = **volt #C6FF3A**（product-UI の signature 色）
- 見出し = Space Grotesk 700（-.03em）／本文 = Inter
- 余白 = セクション L80 / グループ内 tight 8–16

## 必ず守る
1. **データ可視化を主役 UI に**（リング・ミニバー・チップ・スタッツタイル）
2. accent は1色を画面内3〜4回まで
3. カードは整然・角丸18–20・hover で border を accent 化
4. 質感は radial グロー（**grain・斜め・回転・グランジは禁止** ＝ poster 側の語彙）

## 生成時のプロンプト例
```
sporty の product-UI で、架空の○○のLPを作って。
ダークテーマ + volt アクセント、Space Grotesk 見出し。
プログレスリングやミニチャートのデータカードを hero に入れて。
```

## 昇格ステータス
v3（pulse-v3.html）で 6観点 12/12。写真不要・再現性あり。
