# gradient — 参照索引

> `wheel-pattern:gradient` の根拠画像。10〜20枚を目標に収集。
> ★ 6パターン構想（geometric/corporate/grid/digital/sporty/lab）に無かった**追加パターン**。
> corporate 収集時に弾いた紫ブロブ（2026-06-10_p3-ticket-font.jpg）が前兆だった。

## 確定 refs

| # | タイトル | 45_Design_Refs リンク | 一言メモ | 抽出注目点 |
|---|---|---|---|---|
| 1 | Graints 素材ライブラリLP（Web UI 型） | [graints-gradient-library](../../../../brain/45_Design_Refs/2026/06/2026-06-10_graints-gradient-library.md) | アウトライン特大文字を奥に、グラデカード9枚を扇状散布。UIは白黒のみ | 粒子質感 ／ アウトライン文字=奥の層 ／ ±回転散布 ／ 手書き注釈 |
| 2 | HELMO MODE ポスター（印刷物型） | [helmo-showroom-gradient](../../../../brain/45_Design_Refs/2026/06/2026-06-10_helmo-showroom-gradient.md) | 有機ブロブ2つ＋テキスト2ロックのみ。文字とブロブの境界を溶かす | ブロブ3点セット（有機形状/grain/ソフトシャドウ） ／ 溶け込み型深度 ／ 要素最小主義 |
| 3 | Aura Dome ロゴ（アイデンティティ型） | [aura-dome-gradient-logo](../../../../brain/45_Design_Refs/2026/06/2026-06-11_aura-dome-gradient-logo.md) | 半円に閉じ込めたオーロラグラデ×4色バリエーション | グラデの器3型（規格形状/ブロブ/文字） ／ 同一形状×グラデ差替のシステム化 |

## 遡及候補

- 紫グラデブロブ壁紙（`_assets/2026-06-10_p3-ticket-font.jpg` — 未 ref 化。テクスチャ参考として弱いが系統の証拠）

## 隣接技法: glass（パターン候補・シード1）
- [Glass Effect タイルグリッド](../../../../brain/45_Design_Refs/2026/06/2026-06-11_glass-effect-tiles.md) — `wheel-pattern: glass`。glass は「gradient の上に乗る表面材質」の性格が強く、シード3件たまったら独立パック化を判断。LPB v4 残存課題「ぼかし・ガラス加工」と直結。

## 収集メモ
- **確定3件＋遡及候補1件 = Systematize 水準に到達**（Web UI / 印刷物 / アイデンティティの3型）。
- 補完すると強い: ①grain グラデを使った実ブランドサイト ②文字溶け込みの別例 ③ダーク背景×グラデの例。
- 技法メモ: 深度の語彙が2型ある — **アウトライン型**（文字の塗りを抜いて奥へ）と**溶け込み型**（境界を blur で曖昧に）。HTML チャネルなら `-webkit-text-stroke` / `filter: blur` + `mix-blend-mode` で両方再現可能（gradient も HTML 優位パターンの見込み）。
