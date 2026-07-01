# Design Wheel — FAMBOX チラシ対応 設計書

- 日付: 2026-07-01
- ステータス: 設計確定（実装計画へ）
- 関連: ADR-001（`docs/design-wheel/DECISIONS.md`）/ `project_design_wheel_starter_kit` / `fambox-flyer-builder` スキル / `taste-and-tokens.md`

## 1. 目的とゴール

非デザイナー（マレル：松浦/三宅/深澤）が **Design Wheel で FAMBOX ブランドの A4 チラシ叩き台（完成度70%）を出せる**ようにする。出力は **SNS投稿・PDF配布・社内印刷レベル**（入稿grade は対象外）。Design Wheel の思想（HTMLキャプチャ／非デザイナー／FB可）を崩さずに実現する。

### 成功条件
- flyer モードで FAMBOX の A4縦チラシ HTML が生成され、プレビュー・A4 PDF/PNG 書き出しができる。
- 生成物が FAM ブランド（色・フォント・声・確定情報）に沿い、骨格（FOUNDATIONS）＋印刷作法（PRINT-LAYOUT）が効いている。
- アプリと claude.ai Project の両方で使える。
- 既存 `fambox-flyer-builder`（Figma/入稿grade/宮川さん）と役割が明確に分かれている。

## 2. スコープ

### 対象
- 新パターン `fambox`（3サブスタイル：Editorial / Manga / Corporate、既定=Editorial）
- 新出力形態 `flyer`（A4縦固定）
- 印刷レイアウト作法 `PRINT-LAYOUT.md`（flyer 時のみ注入）
- A4 サイズ追加＋ PDF 書き出し
- アプリ＋ Project 両面反映

### 対象外（YAGNI）
- 入稿要素（塗り足し・トリムマーク・CMYK・300dpi）
- A4横・A5・その他判型（後日）
- 実写真の自動差し込み（グレーボックス＋任意 Unsplash。実写真は「仕上げ」工程）

## 3. アーキテクチャ（既存構造への追加）

真ソース = git の `patterns/<p>/SYSTEM.md`（ADR-001 不変条件①）。各UIはそれを読むだけ。出力 = HTMLキャプチャ（不変条件②）。以下は既存の各ユニットへの**追加**のみで、既存パターンの挙動は変えない。

### 3.1 新パターン `fambox`
- **ファイル**: `docs/design-wheel/patterns/fambox/SYSTEM.md`（新規）。真ソースは `.claude/skills/fambox-flyer-builder/references/taste-and-tokens.md`（DNAを共有）。
- **CATALOG 追加**（`lib/patterns.js`）:
  `{ id: 'fambox', label: 'FAM BOX', tagline: 'ブランドの説得', use: 'FAMBOX チラシ・印刷物' }`
- **SYSTEM.md の内容**:
  - カラートークン（1色=1役割）: Drive Orange `#FB4C15` / Deep Blue `#0F2A5C` / コーポレート明青 `#0F43C7` / アンバー `#FFA41A`・イエロー `#FFCC24` / 暖ブラックインク `#252726`（純黒にしない） / サブ `#545655` / グレー枠 `#D9D9D9`・`#E2E2E2` / オフホワイト `#F7F6F4`・`#FAFAFA`
  - タイポ: EN=Poppins / JA=Noto Sans JP（W4〜W8相当は font-weight 400〜800）/ 明朝的箇所=Noto Serif JP。共通スケール（pt→px換算）`32/28/24/20/16/14/12/11/10`。本文行間170%、斜体=エネルギー、数字/実績/価格/栄養価は特大スタッツ化。
  - 3サブスタイル（既定 Editorial）:
    - **A Editorial Catalog**: 雑誌的・データ可視化・落ち着き。実績数字=太字斜体特大。明暗ページ混在・通し番号・三角コーナー・「+」マーク・大図＋2-3カラム。
    - **B Manga Impact**: 掴み最大熱量。極太コミック見出し=**Dela Gothic One**（F910 の web 代替）、英字=Poppins Bold Italic、効果音・斜めコマ割り（黒縁）・吹き出し・切り抜き人物。上で掴み→下で整然3カラム着地。
    - **C Corporate Solution**: B2B・図解・帯・2本柱・信頼。見出し太め、コミック書体は使わない。コネクタチップ・双方向矢印・写真グリッド・ロゴロックアップ。
  - グリッド12カラム（2col=6+6 / 3col=4+4+4、本文幅70-80%）、余白8の倍数 `4/8/12/16/20/24/32/40/56`、内側padding 32基準。
  - 装飾語彙: 背景の帯でゾーニング（濃面=impact / 淡面=reading）、図版は大きく重ねて境界ブリッジ、英字 eyebrow ラベル、淡グラデ奥行き、オレンジ罫。彩度高ベタ2面を隣接させない。
  - **確定マスターデータ**（差し替えマスター）: ブランド名「FAM BOX」（スペース有）/ クーポン `B8483HVWMNEZ`（30%OFF）・初回50%引き定期 / 公式 fam-athletefood-frozen.com・fam-jp.com / 電話 03-6433-5306 / メール fam.athletefood.frozen@gmail.com / 製造所 花かがみ（福岡県北九州市小倉北区熊谷1-29-22）/ 運営 株式会社ARCHECO（〒150-0001 東京都渋谷区神宮前1-15-4 Barbizon76 3F）/ 監修 大前 恵・和田 毅。

### 3.2 flyer モード（`lib/generate.js`）
- `buildSystemPrompt(patternId, { size, mode })` に `mode === 'flyer'` 分岐を追加（banner 分岐と同型）:
  - 出力形態文: 「A4縦 1枚のチラシ。`<body>`と最外要素を A4比率（794×1123px 相当）に固定し、はみ出さない。単一構図。」
  - PRINT-LAYOUT.md（下記 3.3）を FOUNDATIONS の後に注入。
- FOUNDATIONS（Layer①）は全モード共通で既に注入済み。flyer では PRINT-LAYOUT を上乗せ。

### 3.3 印刷レイアウト作法（`docs/design-wheel/foundations/PRINT-LAYOUT.md`・新規）
flyer 時のみ注入する小さな addendum。`build-playbook.md` の HTML 版蒸留：
- **ブロッキング先行**: 色でなく面積で情報優先度を分割（%ブロッキング）→ プレースホルダ配置 → 精緻化。
- **マストヘッド全ブリード**: 最重要帯は紙端までフルブリード（余白ゼロ）。
- **収まらない情報は削る**（A4 1枚に詰め込まない。優先度低は落とす）。
- **背景の帯でゾーニング**（濃面=impact / 淡面=reading）、レイヤー重なりで境界をまたぐ＋影。
- **画像はグレーボックス**（`#D9D9D9`）でプレースホルダ、任意で汎用 Unsplash。実写真は仕上げ工程。
- 本文行間170% / 斜体=エネルギー / 色=役割予約 / 8の倍数余白。

### 3.4 A4 サイズ＋ PDF 書き出し（`lib/export-png.js`）
- SIZES に追加: `'a4': { w: 794, h: 1123, label: 'A4 チラシ（縦）' }`（scale2 で約192dpi 相当 PNG）。
- **PDF 書き出し関数を追加** `exportPdf({ html })`:
  - Chrome ヘッドレス `--print-to-pdf=<out>` ＋ `--no-pdf-header-footer`、HTML 側は `@page{size:A4;margin:0}` 前提。
  - flyer 用。A4 1枚に収める。
- `server.js` の `/api/export` に `format`（`png`|`pdf`）を受け、pdf なら `exportPdf` を呼び `application/pdf` で返す（既存 PNG 経路は不変）。

### 3.5 フロント（`public/index.html` + `app.js`）
- モードトグルに `flyer`（「チラシ A4縦」）を追加。
- flyer 選択時: サイズ選択を A4 に固定（or 自動選択）、書き出しボタンを「PDF書き出し」＋「PNG書き出し」に。
- state.mode に 'flyer' を許容。/api/export 呼び出しに format を付与。

### 3.6 両面反映（claude.ai Project）
- `share/claude-project-v0/knowledge/` に `fambox-SYSTEM.md`（= patterns/fambox/SYSTEM.md）と `PRINT-LAYOUT.md` をコピー。
- `PROJECT-INSTRUCTIONS.md`: パターン早見表に fambox を追加、flyer 依頼時は BRIEF の判型=A4縦を確認＋PRINT-LAYOUT を使う旨を追記。
- `KNOWLEDGE-MANIFEST.md`: fambox / PRINT-LAYOUT を登録一覧に追加。

## 4. データフロー

```
[マレル] flyerモード＋fambox＋サブスタイル＋指示
  → /api/generate
     system = FOUNDATIONS(①) + PRINT-LAYOUT(印刷) + fambox SYSTEM(②) + flyer形態(A4固定)
     user   = 指示（or previousHtml で修正）
  → Opus が A4縦チラシ HTML を生成 → プレビュー
  → /api/export?format=pdf|png → Chrome ヘッドレスで A4 PDF/PNG 書き出し
  → 使用後 #design-wheel / FBスプシに1行
```

## 5. 既存 `fambox-flyer-builder` との関係

| | Design Wheel fambox flyer | fambox-flyer-builder |
|---|---|---|
| エンジン | HTMLキャプチャ | Figma |
| 品質/用途 | SNS・PDF・社内（70%叩き台） | 入稿grade・本番 |
| 使う人 | マレル（非デザイナー） | 宮川さん（作れる人） |
| DNA真ソース | **共通** `taste-and-tokens.md` | 同左 |

同じ DNA を共有し、出力エンジンと品質ティアで棲み分ける。将来 Design Wheel で叩き台 → 宮川さんが Figma で入稿仕上げ、という接続も可能。

## 6. テスト / 検証

- flyer × fambox × Editorial で A4チラシ生成 → PNG＋PDF 書き出し成功を確認（実機）。
- 生成物を目視: FAM 色/フォント/確定情報が入り、マストヘッド全ブリード・帯ゾーニング・8の倍数余白・行間170% が効いているか（PRINT-LAYOUT チェック）。
- 既存 page/banner モードと corporate 等の既存パターンが**回帰しない**ことを確認（1件生成）。
- Manga サブスタイルで Dela Gothic One が Chrome ヘッドレスで実レンダリングされるか確認。

## 7. リスクと対処

- **A4 1枚に情報が収まらない**: PRINT-LAYOUT の「収まらない情報は削る」で対処。プロンプトにも明記。
- **PDF の余白/改ページ**: `@page{size:A4;margin:0}` を SYSTEM/PRINT-LAYOUT の出力ルールに明記し、単一ページ固定。
- **日本語フォント**: Google Fonts（Noto Sans JP / Noto Serif JP / Dela Gothic One）で実レンダリング＝Figma版の課題を回避。
- **実写真なし**: 70%モデルどおりグレーボックス。仕上げで差し替える前提を出力の締め（仕上げ3チェック）に含める。

## 8. 実装順序（概要・詳細は plan で）
1. `patterns/fambox/SYSTEM.md`（3サブスタイル）作成 ＋ CATALOG 追加
2. `foundations/PRINT-LAYOUT.md` 作成
3. `generate.js` に flyer 分岐＋PRINT-LAYOUT 注入
4. `export-png.js` に a4 サイズ＋ exportPdf ／ `server.js` に format 対応
5. フロント（flyerトグル＋PDFボタン）
6. 実機検証（生成→PDF/PNG→目視→回帰）
7. Project 両面反映（knowledge コピー＋指示/マニフェスト更新）
