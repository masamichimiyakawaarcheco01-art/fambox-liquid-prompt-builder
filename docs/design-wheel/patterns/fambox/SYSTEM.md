# FAM — パターン SYSTEM（FAM ブランド共通：SNS / Web / 印刷）

> 用途: FAM / FAM BOX ブランドの制作物。非デザイナーが70%品質の叩き台を出す。
> 真ソース: `brand/fam/brand-dna/current.md`（v0.5 確定色/タイポ）＋ 印刷は `fambox-flyer-builder/taste-and-tokens.md`。マレルFB(2026-07)反映。
> page / banner(SNS) / flyer の全モードで使える。

## FAM 絶対ルール（全サブスタイル共通・世界観ガイド。これを破ると FAM でなくなる）
- **写真はカラーそのまま**。デュオトーン/モノトーン/カラーオーバーレイ/スクリム暗化を**かけない・提案しない**（FAM世界観違反）。調整は"良い写真を選ぶ／軽い補正"側で。
- **オレンジ `#FB4C15` は CTA・アクション専用**。見出しや広い面に多用しない。
- **暗背景×オレンジ文字を避ける**。CTA は「**オレンジ地＋白文字**」を標準。
- **タイポは抑制**：Poppins（英）＋Hiragino Sans（和）。コンデンス体・ALL CAPS の多用を避ける。メリハリは数値/実績サイズで作る。
- 権威性（プロ選手・監修）を前面に。左端揃えの骨格。装飾過多にしない（装飾過多で中身が見えない＝FAMっぽくない）。

## サブスタイル（配色系統。既定 = A SNS/Poster）
### A. SNS / Poster（既定・banner / リール / 投稿向け）
- ベース: **黄 `#F5C842` × ダーク `#1A1A1A`**。
- 文字色: ダーク面は白 `#FFFFFF`、黄面は `#1A1A1A`。
- CTA: **オレンジ `#FB4C15` 地＋白文字**（画面で1点のみ）。
- 用途: Instagram リール表紙・フィード・ストーリー。権威性の前出し。

### B. Web / DNA（page 向け・ブランドDNA v0.5準拠）
- 色: Drive Orange `#FB4C15`(CTA/達成値) / Sky Blue `#3DB8E8`(データ) / Deep Blue `#0F2A5C`(信頼/ヒーロー深部) / Ink `#1B1D1A`(本文) / Off-White `#FFFFFF`・`#FAFAFA`・`#F3F3F3`。
- Bento Grid＋部分ガラス、Editorial×Lab、余白大。
- 用途: Web LP・ダッシュボード・商品紹介。

### C. Print / Flyer（flyer 向け・印刷DNA）
- 色: Drive Orange `#FB4C15`(CTA/効果音) / Deep Blue `#0F2A5C` / アンバー `#FFA41A`・イエロー `#FFCC24`(データ/実績) / 暖ブラックインク `#252726`(純黒にしない) / オフホワイト `#F7F6F4`。
- 印刷フレーバー（プロンプトで選ぶ・既定 Editorial）: **Editorial**（雑誌的・データ可視化）/ **Manga**（掴み・極太見出し Dela Gothic One・斜めコマ）/ **Corporate**（B2B図解・帯・2本柱）。
- A4固定（PRINT-LAYOUT準拠）。梱包同梱チラシは Editorial 主体。

## タイポグラフィ（Google Fonts で実レンダリング）
- 英数字 = **Poppins**（wght 400/500/600/700）。
- 日本語 = **Hiragino Sans** system stack: `'Hiragino Sans','Hiragino Kaku Gothic ProN','Noto Sans JP','Meiryo',sans-serif`（HTMLキャプチャ環境に Hiragino が無ければ Noto Sans JP に自動フォールバック。Noto Sans JP は Google Fonts で読み込む）。
- 明朝的箇所 = Noto Serif JP。C の極太コミック見出しのみ = Dela Gothic One（Google Fonts）。
- スケール(px): `12/14/16/20/24/32/48/64/96/128`。行間: 見出し1.2 / 本文1.75 / キャプション1.5。字間: 英 -0.02em / 和 0.02em。
- ジャンプ率は高め（display 64-96 ↔ body 14-16）だが **コンデンス/ALL CAPS に頼らない**。数値・実績・価格・栄養価は特大スタッツ化。

## レイアウト / グリッド
- 12カラム / gutter 24px / 8px baseline。余白は8の倍数（8/16/24/32/48/64/96/160）。印刷は 4/8/12/16/20/24/32/40/56 も可、内側 padding 32基準。
- 主構図: 左下→右上の対角線、**左端揃え**。二項対置（Your/Our）。
- 角R: カード8px / 小4px / **CTAピル 50px** / バッジ 9999px。ボタンPrimary = Drive色・白文字・ピル50px。

## 写真・イメージ
- 主題: 決定的瞬間・息遣い・汗・上を向く視線・前方への躍動。動きの途中（静止写真は避ける）。タイポと重ね合わせOK。
- 処理: **カラーそのまま**（オーバーレイ/デュオトーン禁止）。彩度やや抑制・コントラスト高めは"素材選び・軽い補正"で。
- 権威性: プロ選手・監修（大前恵・和田毅）を前面に。
- 素材が無い場合はグレーボックス `#D0D0D0` プレースホルダ＋「実写真差し替え」を仕上げに明記。

## 言葉遣い
- 短く前向き・動詞中心（"次へ""動かす""続ける""積み上げる""挑む""駆動"）。命令形・上から目線・"頑張って"・曖昧応援は禁止。見出しで英字主役＋日本語サポート可。

## 確定マスターデータ（差し替えマスター・そのまま使う）
- ブランド名: **FAM**（親）/ **FAM BOX**（冷凍宅配・スペース有）。文脈で使い分け。
- クーポン: `B8483HVWMNEZ`（30%OFF）／初回50%引き定期
- 公式: fam-athletefood-frozen.com ／ fam-jp.com
- 電話: 03-6433-5306 ／ メール: fam.athletefood.frozen@gmail.com
- 製造所: 花かがみ（福岡県北九州市小倉北区熊谷1-29-22）
- 運営: 株式会社ARCHECO（〒150-0001 東京都渋谷区神宮前1-15-4 Barbizon76 3F）
- 監修: 大前 恵・和田 毅

## 出力ルール
- 上の絶対ルール・色・フォント・確定情報を厳守（創作しない）。写真加工（デュオトーン/オーバーレイ）は提案も適用もしない。
- flyer は PRINT-LAYOUT の A4固定条件（`@page`・794×1123px・overflow:hidden）を満たす。banner はサイズ枠に固定。page はレスポンシブ。
