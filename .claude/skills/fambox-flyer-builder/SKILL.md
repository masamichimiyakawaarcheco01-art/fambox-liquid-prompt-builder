---
name: fambox-flyer-builder
description: "FAM BOX の印刷物（チラシ・パンフレット・ポスター・カタログ・梱包同梱物・B2B提案資料）を Figma 上で設計・構築する。3テイストモード（Editorial Catalog / Manga Impact / Corporate Solution）を宣言し、背景バンドゾーニング・箱(auto-layout)・タイポ階層・グレーボックス画像・写真の upload_assets 配置・生成後の自己検証まで一貫して行う。Use when creating or revising any FAM BOX / FAM 印刷物（チラシ/flyer/パンフレット/pamphlet/ポスター/poster/カタログ/catalog/梱包同梱/B2B 提案・solution 資料）, building A4/大判 print layouts in Figma, applying FAM print design DNA, or iterating on flyer feedback. Triggers 「チラシ」「パンフレット」「印刷物」「梱包同梱」「ポスター」「カタログ」「flyer」「poster」「提案資料」+ FAM/FAMBOX 文脈。"
---

# FAM BOX Flyer / Print Builder

FAM BOX の印刷物を「誰でも7割を早く」出すための器。過去制作物のリバースエンジニアリング（PRINT-DESIGN-DNA）と miyaFB ブラッシュアップ学びを体系化済み。**抽象ルールより、ここに挙げる living docs と実機検証を優先**する。

## 0. 起動時に必ず読む（真実源）

新規/修正の前に以下を Read する。**仮置きでなく実値を使う**こと。

| ファイル | 役割 |
|---|---|
| `docs/okr/fambox-flywheel/projects/flyer-packaging/PRINT-DESIGN-DNA-research-2026-06-04.md` | 3テイストモード・モード別 type/color/装飾語彙（過去制作物実測） |
| `docs/okr/fambox-flywheel/projects/flyer-packaging/TEMPLATE-fambox-flyer-v1.md` | 梱包チラシの型（グリッド/モジュール/確定データ/スタイル宣言） |
| `brand/fambox/design-system/bugs.md` | DOCTRINE-006(印刷4書体)/007(色ゾーニング)/008(3テイストモード)・PROC-011(Figma分担) |
| [references/build-playbook.md](references/build-playbook.md) | Figma 構築の手続き知見（figma-bridge/use_figma/upload_assets/箱/自己検証/既知の罠） |
| [references/taste-and-tokens.md](references/taste-and-tokens.md) | 3モード早見＋type/color/tracking/line-height トークン（DNA 蒸留版） |
| [references/asset-index.md](references/asset-index.md) | 画像アセット索引（スロット→実写真の自動選択＋ upload_assets 配置） |
| [references/quality-rubric.md](references/quality-rubric.md) | 品質ルーブリック（9軸/合格80%）＋ゴールド見本。生成後の自己採点基準。ループ運用は `docs/okr/fambox-flywheel/quality-loop/CRITIQUE-AGENT.md` |

関連 feedback memory（罠回避）：`feedback_figma_bridge_text_limitations` / `feedback_fam_typography`（印刷物例外）/ `feedback_visual_design_video_first`。

## 1. ワークフロー（毎回この順・DOCTRINE-008/009）

**色やバンドから入らない。比率ブロッキング先行 → 主役から精緻化。**

1. **モード宣言**（必須・DOCTRINE-008）：A. Editorial Catalog ／ B. Manga Impact ／ C. Corporate Solution。複数なら primary 1＋secondary 1-2（スコープ明記、3つ以上禁止）。チラシ＝A主体＋Hero に B 少量＋CTA に C。
2. **参照画像を同梱**：人力サンプルがあれば画像で渡し「この画像に合わせ差分を自己批評して直せ」。記述でなく画像が最強の入力。
3. **情報設計**：載せる情報を棚卸し→優先度（大=大きく見せる／中=じっくり読ませる／小=必要な人だけ）。表に載せない情報は裏へ。
4. **内側パディング決定**：アートボードに 32（情報多め）〜48（ゆとり）を設定。
5. **比率ブロッキング**：パディング内を**優先度で % にグレー面分割**（色・装飾はまだ）。各ブロックにリード文/本文/画像の入る場所をプレースホルダ配置。
6. **俯瞰調整**：全体を見て狭い/はみ出すブロックは比率調整、収まらない情報は裏面へ。**32パディングからはみ出さない**。
7. **優先度が高いブロックから精緻化**（色・タイポ・装飾はここで）：
   - **マストヘッド（Hero）は artboard 際までフルブリード**（x0 y0 w595、角丸なし）。文字は左32尊重。箱に閉じ込めない（弱く見える）。
   - **レイヤー3層**：前景（切り抜き人物・浮くカード/バッジ）＞中景（文字）＞背景（カラー帯）。**図/バッジをゾーン境界にまたがせ＋ドロップシャドウで浮かせる**＝奥行き・複雑さ・美しさ。事故の重なり（文字を潰す）は厳禁、z-order とクリアランスを意図設計。
   - 色ゾーニング：濃面=impact／淡面=reading。橙=CTA/Hero、Deep Blue=信頼/連絡、Ink濃=特集/監修。彩度高ベタを2面隣接させない。
8. **タイポ**：日本語 Hiragino を W4〜W8（構築時は Noto Sans JP 代替→Mac で差し替え）、英字 Poppins、行間 本文170%/見出し125-150%/Display150%、トラッキング Display-3〜4%/見出し-2%/本文+1%。数字・実績は**斜体スタッツ**で特大。
9. **画像**：まず構造はグレーボックスで確定 → **asset-index.md でスロットに合う実写真を選び `upload_assets` で配置**（build-playbook §3）。索引に無い/質不足はグレーのまま＋必要素材をユーザーに依頼（無理な合成はしない）。人物の肖像/契約/チーム許諾は確定前に確認。
10. **生成後スクショで自己検証＋ルーブリック採点**：右端/下端のはみ出し・要素衝突・濃背景上のコントラストを確認した上で、`references/quality-rubric.md` の9軸で**同じ面のゴールド見本と並べて採点（加重・合格80%）**。80%未満は未完成として優先ギャップ Top3 を直す。再発ギャップは §3 で恒久ルール化（書き戻し）してから報告。

## 2. モード別の要点（詳細は taste-and-tokens.md）

- **A. Editorial Catalog**：明暗ページ混在・英字セクションラベル＋通し番号・大図＋2-3カラム・斜体スタッツ・三角コーナー。
- **B. Manga Impact**：F910 効果音特大・斜めコマ割り・吹き出し・切り抜き人物・縦組極太→下半分は整然3カラムで着地（緩急）。※効果音手描き感・切り抜き合成・斜めコマは人間仕上げ領域。
- **C. Corporate Solution**：白/明青#0F43C7/橙のバンド・2本柱ダイアグラム＋コネクタチップ＋双方向矢印・写真グリッド・スマホモック。

## 3. 成長ループ（このスキルを育てる仕組み）★重要

チラシ作業で新しい学び・罠・好フィードバックが出たら、**その場で次のいずれかに必ず追記**する（散逸させない）：

1. **再利用可能な規律** → `brand/fambox/design-system/bugs.md` の DOCTRINE/PROC に追加（件数サマリも更新）。strict 候補は promotion-rule に従う。
2. **モード/トークン/装飾語彙の更新** → `PRINT-DESIGN-DNA-research-*.md` と本スキルの `references/taste-and-tokens.md`。
3. **Figma 手続きの罠/回避** → `references/build-playbook.md` と feedback memory。
4. **型の改訂** → `TEMPLATE-fambox-flyer-v1.md`（モジュール・確定データ）。
5. セッション終了時は `session-end` で memory に反映。

> 原則：**毎回のフィードバックを「次回の自動適用」に変換する**。docs に書くだけで終えず、bugs.md DOCTRINE と本スキル references を真実源として同期し続ける。これが Flywheel の Learn→Generate。

## 4. やらないこと（Anti）

- モード宣言なしで作り始める（テイスト混在の失敗）。
- 押し売り・空語（「今だけ」「最高の」「プレミアム」「revolutionary」「業界No.1」）。配置前に Words-first 監査。
- グリッド/フォント/色ゾーニングを案件ごとに自己流で変える（型・DNA に従う）。
- 写真を無理に合成（未熟領域）。グレーボックスで構造を出し、人間/素材待ちにする。
- 生成しっぱなしで報告（必ずスクショ自己検証）。
