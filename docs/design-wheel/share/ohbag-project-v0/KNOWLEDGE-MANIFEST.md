# 知識ファイル マニフェスト — ohbag Project にアップロードするもの

> claude.ai の「ohbag Design Wheel」Project の**ナレッジ（添付ファイル）**に、以下をドラッグ登録する。
> これが「アプリのコンテンツ」。宮川が改訂したらここを差し替える（＝アップデート）。

## 登録するファイル（5点）
| レイヤー | ファイル | 役割 |
|---|---|---|
| ② ohbag意思 | `knowledge/ohbag-SYSTEM.md` | ohbag の色・フォント・世界観・2テイスト・確定データ。**真ソース** |
| ① 普遍 | `knowledge/FOUNDATIONS.md` | 比率・余白・整列・タイポの土台（全生成） |
| ①印刷 | `knowledge/PRINT-LAYOUT.md` | A4チラシ時の印刷レイアウト作法 |
| ①名刺 | `knowledge/CARD-LAYOUT.md` | 名刺（91×55mm）時のレイアウト・文字階層 |
| ③ 条件 | `knowledge/BRIEF.md` | 依頼ごとの条件ヒアリング → 翻訳 |
| 手順書 | `CHARACTER-RECIPE.md` | 新キャラのセルフ追加手順（指示文から参照される。軽量なので登録推奨） |

## キャラ画像（`knowledge-characters/`・1体1ファイルで登録）
| ファイル | キャラ | 使いどころ |
|---|---|---|
| `logo-ohbag.md` | 正ロゴSVG | 全制作物 |
| `character-business.md` | ビジネス旅行者 | 荷物配送 / 出張 / Wi-Fi |
| `character-senior.md` | シニア夫婦 | 観光 / 行程プラン / 年配ゲスト |
| `character-woman.md` | 若い女性（スマホ） | アプリ操作 / 若年層 / 予約 |
| `character-family.md` | 父と娘（家族旅行） | 家族連れ / ファミリープラン |
| `character-couple.md` | バックパッカーカップル | 欧米ゲスト / 荷物配送 / 個人旅行 |

※ パス基準 = `docs/design-wheel/share/ohbag-project-v0/`。
※ カスタム指示は `PROJECT-INSTRUCTIONS.md` を指示欄に貼る。

## 更新の反映（宮川さん）
- ohbag-SYSTEM を改訂したら、`docs/design-wheel/patterns/ohbag/SYSTEM.md`（真ソース）を直す → このフォルダの `knowledge/ohbag-SYSTEM.md` にコピー → Project のナレッジを差し替え。
- ★項目（正カラー/フォント/ロゴ/3Dキャラ）が実素材で確定したら SYSTEM を更新して再登録。

## 注意
- FOUNDATIONS / BRIEF / PRINT-LAYOUT は FAM 版と共通（普遍レイヤー）。ohbag 固有は ohbag-SYSTEM のみ。
- 古いコピーが Project に残ると分岐する。更新時は必ず差し替え。
