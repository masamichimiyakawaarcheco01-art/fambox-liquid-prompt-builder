# corporate — critique log

> [CRITIQUE-RUBRIC.md](../../CRITIQUE-RUBRIC.md) の記録フォーマットで各版を記録。

## v1 採点 2026-06-10

**対象**: FlowOps LP（Hero + 特徴3カード）/ Figma frame `137:77` / figma-bridge 構築
**比較参照**: refs 3枚（fintech シード / pharmacy 明るい系 / RIDEQUEST ダーク系）

| 観点 | 点 | コメント |
|---|---|---|
| 1 色ゾーニング | 2/2 | bg #F4F5F6 / カード #FFF / ink near-black / accent は番号ラベルのみ — トークン通り。CTA は黒ピル（pharmacy 型）で accent 乱用なし |
| 2 タイポ階層 | 2/2 | Display 64 × eyebrow 11 uppercase × Body 14 — ジャンプ率 4.6x が明快に出ている |
| 3 グリッド | 2/2 | 外マージン 80 / カード3等分+ガター24 / 円形画像は右端揃え。ズレなし |
| 4 コンポーネント | 2/2 | 3カード完全同型（角丸16・hairline stroke・padding 32）、ピルCTA・円形マスクも仕様通り |
| 5 余白 | 1/2 | セクション間 64 / カード内 16 は等比リズム通り。**減点**: カード高さ固定 220px のため本文下に不均等な空きが出る（HUG にすべきだった） |
| 6 らしさ | 2/2 | pharmacy 系「明るい・ほぼモノクロ・番号ラベル・円形マスク」の corporate DNA がそのまま出ている |

**合計: 11/12 ／ 構造系0点: 無 ／ 判定: 昇格条件達成（宮川さん最終確認待ち — D-021 Human validates）**

**人間仕上げメモ（採点対象外の3割）:**
- フォント: 全テキスト Inter 固定（bridge 制約）→ 日本語展開時は Noto Sans JP へ差替
- 円形グレーボックス → 実画像（プロダクトUI / 抽象3D）差込
- eyebrow "PLATFORM" に letter-spacing .08em 付与（bridge では指定不可）

**次の改訂指示（v2 で反映）:**
- カードは `layoutSizingVertical: HUG` で作る（固定高さによる余白ムラ解消）→ figma-recipe.md 手順4に反映済み
- Hero 左テキストブロックの幅は本文の自然な折返し幅（~560px）に絞ると参照にさらに近づく

**純構築時間: 4分15秒**（10:40:27→10:44:42 / join_channel 後の最初の create_frame から export 確認まで）
→ 横展開時の基準値。人力比でのスピード検証は次パターンで実測比較。
