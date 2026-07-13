# sporty — Reference Extraction v1（測れる仕様への蒸留）

> 「単調・テンプレ感」を脱するための、リファレンス＋リサーチ由来の **measurable な入力**。
> 出典: Awwwards Sport/Editorial ギャラリー、condensed grotesque の系譜リサーチ（2026-06-18）。
> これを SYSTEM.md v1 に反映する前段の抽出メモ。

## 0. 現状 refs の弱点（refs.md より）

確定3件＋遡及6件は **ポスター/写真型に偏り**、Web UI 型・組版 craft が薄い。
→ 深度・デュオトーン・色帯は抽出済みだが、**フォント体系・余白の緩急比・クロップ規律・装飾の語彙化**が未抽出。
これが v1→v2 で改善しきれなかった「もう一段」の正体。

## 1. フォント（最大の伸びしろ）

### 抽出した事実
スポーツ/アスレチックの組版伝統 = **コンデンスド・グロテスク**。
- 高級職業フォント: **Druk**（超圧縮・Bloomberg Businessweek 由来）/ **Tungsten**（競技ユニフォーム由来）/ **Knockout**（ボクシングポスター由来・32スタイル）
- これらの共通点 = **狭い字幅 × 複数ウェイト/幅で"体系"を組む**

### measurable 入力（無料で再現）
| 役割 | v2（頭打ち） | v1 推奨（体系が組める） |
|---|---|---|
| Display | Anton（**1ウェイトのみ**） | **Oswald**（ExtraLight〜Bold 6+ウェイト）or **Barlow Condensed**（9ウェイト）|
| 数字/特大 | Anton | Bebas Neue（uppercase 特化）or Oswald 700 |
| 本文 | Inter | Inter（維持）|
- **トラッキング**: 特大 Display は `letter-spacing: -0.02〜-0.04em`（締める）。Small ラベルは `+0.1〜0.26em`（開く）。**この振れ幅が craft**。
- **ルール**: Display=ALL CAPS、本文=小文字。混ぜない。
- ウェイト混在（例: 同じ語の中で 300 と 800 を併置）で速度のリズムを作る。

## 2. レイアウト

### 抽出した事実（Awwwards Editorial/Sport トレンド）
- 「ポスター様式のレイアウト」「big-personality typography でリズムとコントラスト」「typeface の混在が基本作法」。

### measurable 入力
- **タイトクロップ**: 写真は全身でなく **動作の一部（手/筋肉/踏み込み/汗）を寄りで断つ**。`object-position` で被写体の動的部分をフレーム端に寄せる。
- **グリッド破り**: 要素をセクション境界をまたいで重ねる（margin-top 負値で次セクションに食い込む）。
- **1ビューポート1焦点**: 各画面に主役を1つ。詰めない。
- **誌面型の非対称**: 1大＋2小（v2 で実証済み）を基本グリッドに昇格。

## 3. 余白

### measurable 入力（緩急比が鍵）
- **セクション間**: v2 の 64–72px → **120–160px** に拡大。
- **グループ内**: 4–8px に圧縮。
- **= tight:loose 比を 1:20 前後まで極端化**（v2 は 16:64=1:4 で差が小さく単調の一因）。
- **光学整列**: 特大 Display は左端を負マージンで視覚的に揃える（メトリック揃えは左がズレて見える）。

## 4. 装飾（語彙化 = system 化）

### measurable 入力
- **テレメトリ層**（計測の気配を一貫システムで）: 番号 `#01`・座標 `35.6°N`・タイムスタンプ・計測目盛・`REC●`・スプリットタイム。バラバラの飾りでなく「同じ語彙の反復」。
- **モーション言語**: マーキーティッカー / 方向矢印 `→` / 写真端のキネティックブラー / スピードライン。
- **質感**: SVG グレイン（v2 実装済み・opacity .04〜.06）/ デュオトーンの一貫適用。
- **抑制ルール**: accent は **1色を画面内3〜4回まで**。盛るほど安く見える。

## 5. 次アクション

1. **ユーザーの好み refs を 3〜4 件追加**（URL/画像）→ 上記の measurable 軸で抽出表に追記。**ユーザーの taste = 目標水準**。
2. refs 充足後、SYSTEM.md を v1 に改訂（Type に Oswald/Barlow、Layout に誌面型・タイトクロップ、Spacing に緩急比、Components にテレメトリ層を明記）。
3. v3 プロトタイプで到達点を実機確認 → Claude Design 上げ直し。

## ⭐ 最大の学び（2026-06-18・ユーザー refs で方向転換）

ユーザー提供の3 refs（[Nike Run+ App](https://www.behance.net/gallery/116349159/), [PLAYPAD store](https://www.behance.net/gallery/246581921/), [NestEgg Dashboard](https://www.behance.net/gallery/246825297/)）は
**全て「スポーツ・プロダクトUI」**（アプリ/EC/ダッシュボード）。ポスター/エディトリアルは0件。

→ **sporty には2つの sub-style が存在する**ことが判明:
| sub-style | 語彙 | refs |
|---|---|---|
| **sporty-poster**（既存 SYSTEM v0 が捉えていた方）| 写真主役・深度・デュオトーン・色帯・グランジ質感・コンデンス grunge | TENISTA / NIKE GUANGZHOU / Nike First Step |
| **sporty-product-UI**（ユーザーの本命・未捕捉だった）| ダークテーマ・volt/電光アクセント・データ可視化（リング/チャート/チップ）・整然カード・幾何サンセリフ・キネティック曲線・**装飾でなくコントラストと余白で premium** | Nike Run+ / PLAYPAD / NestEgg |

**v1/v2 の失敗原因**: SYSTEM v0 が sporty-poster しか想定せず、ユーザーの本命（product-UI）と不一致だった。
グレイン・斜め・回転・グランジは product-UI には**逆効果**（雑に見える）。

### sporty-product-UI の measurable 入力（v3 で実証 = `prototypes/pulse-v3.html`）
- **Color**: bg=#0A0C0B 近黒 / surface=#14171A / line=#272C30 / accent=**volt #C6FF3A**（電光色が product-UI の signature。orange/blue より「アプリらしさ」が出る）
- **Type**: 見出し=**Space Grotesk 700**（幾何 grotesk・tight -.03em）/ 本文=Inter。コンデンス grunge は使わない
- **データ可視化を主役 UI に**: SVG プログレスリング・ミニバーチャート・ステータスチップ・スタッツタイル＝「精度・計測」の信頼演出（digital パターンと隣接）
- **質感**: グレイン廃止。代わりに **radial-gradient のグロー**（accent 22% → 透明）で先端感
- **カード**: 角丸20px・1px line・hover で border を accent 化（回転・グランジ無し）
- **余白**: セクション L80px・グループ内 tight。整然・余白で premium

## 出典
- ユーザー提供 Behance refs 3件（product-UI 方向の確定根拠）
- Awwwards: Sport / Editorial / Typography ギャラリー
- condensed grotesque 系譜（Druk / Tungsten / Knockout と Oswald / Barlow Condensed / Bebas Neue / League Gothic）= sporty-poster 側で活用
