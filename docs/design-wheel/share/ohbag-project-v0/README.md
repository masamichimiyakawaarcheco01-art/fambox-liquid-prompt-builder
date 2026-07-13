# ohbag Design Wheel — Project キット（須藤さんチーム用）

> 目的 = ホテル現地で、前日の気づきをもとに **ohbag のA4チラシ・名刺・SNS投稿を70%品質でその場生成**し、日次PDCAを回す。
> Design Wheel（FAM で実証済みの「デザインシステム→非デザイナー高速生成」の仕組み）の **ohbag 版**。

## 中身
| ファイル | 役割 |
|---|---|
| `PROJECT-INSTRUCTIONS.md` | Project のカスタム指示（ツールの頭脳） |
| `KNOWLEDGE-MANIFEST.md` | Project に登録する知識ファイル一覧（4点） |
| `knowledge/` | ohbag-SYSTEM＋FOUNDATIONS＋PRINT-LAYOUT＋BRIEF |
| `SCENARIO-INTAKE.md` | 現場でコピペして送る入力テンプレ |
| `FEEDBACK.md` | 現地1行FBの型（日次PDCA） |
| `CHARACTER-DATAURIS.md` | 3Dキャラ写真の data URI（Project でキャラを出す用・コピペ素材） |
| `CHARACTER-RECIPE.md` | **新キャラを自分で追加する手順書**（Gemini生成→remove.bg→変換ツール。5分） |
| `image-to-snippet.html` | **画像→貼り付けスニペット変換ツール**（ダブルクリックで起動・オフライン動作） |

## 3Dキャラ写真を Project で使う（重要）
- ロゴ等の **SVG は自動で使える**（ohbag-SYSTEM に索引済み）。
- **キャラ写真（PNG/WebP）は claude.ai Artifact が外部URLを読めない** → `CHARACTER-DATAURIS.md` を開き、使いたいキャラの `<img ...>`（data URI）をコピー → チャットに貼って「この img を右に配置して」と指示。
- ⚠️ `CHARACTER-DATAURIS.md` は容量が大きいので **Project のナレッジには登録しない**（都度コピペ用の参照ファイル）。須藤さんには Slack/Drive で共有すると良い。
- ローカル app では data URI 不要（`/pa/ohbag/assets/characters/…` で参照）。

## セットアップ手順（宮川さん・15分）
1. claude.ai で**新規 Project**「ohbag Design Wheel」を作る（須藤さんチームに共有・**使用可**権限）
2. `PROJECT-INSTRUCTIONS.md` の中身を Project の**カスタム指示**に貼る
3. `KNOWLEDGE-MANIFEST.md` に沿って **knowledge の4ファイルをナレッジに登録**
4. Google スプレッドシート「ohbag Design Wheel FB」を作る（FEEDBACK の列）
5. `SCENARIO-INTAKE.md` を須藤さんに渡す（現場の入力型）
6. 自分で1回テスト → 須藤さんチームに現地で使ってもらう

## 現地での使い方（須藤さんチーム）
1. `SCENARIO-INTAKE.md` を埋めて Project に送る（誰に・シナリオ・媒体）
2. 出た叩き台を会話で微修正（「見出し短く」「QR大きく」等）
3. 印刷 = 画面スクショ or ブラウザ **Cmd+P → A4 PDF**
4. 使ったら FBシートに1行

## 回し方（PDCA）
```
現場で使う → FBシートに1行 → 宮川が週1集計
  → 弱いシナリオ/媒体を特定 → ohbag-SYSTEM 改訂 → Project 更新 → 翌日から良くなる
```

## いまの状態（v0）
- ohbag-SYSTEM は **App Store スクショ＋サイトから decode した v0**。英字フォントは実サイトCSSで確定（見出しPoppins/本文Manrope）。
- ★要確認（実素材で確定）: 正カラーHEX / ロゴデータ＋HIS・富士通併記ルール / 3Dキャラ素材 / ダウンロードQR実物。
- これらが揃うと本番品質に上がる。無い間は近似＋プレースホルダ（「差し替え」表示）で運用可能。

## 関連
- 雛形: `../claude-project-v0/`（FAM 版）
- 真ソース: `docs/design-wheel/patterns/ohbag/SYSTEM.md`
