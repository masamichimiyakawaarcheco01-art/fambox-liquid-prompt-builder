# FAMレモン君環境 設計スペック

**作成日**: 2026-04-15
**目的**: 南場会長の3段階モデル（プロンプト→コンテキスト→エンバイロメント）の第3段階を、FAMBOX OKR運用に適用する
**背景**: 現在のOKR運用はコンテキストエンジニアリング段階（AIに資料を読ませて出力）。これを「AIエージェントがSlack/GA4/Sheetsを自律的に巡回し、データ駆動の改善提案までループを回す環境」に進化させる

## 全体アーキテクチャ

3つのコンポーネントが、Googleスプレッドシート + okr_weekly_log.md を共有メモリとして連携する。

```
GA4 → Insight Engine → Sheets(UI改善提案) ─┐
                                         │
Slack 3ch → OKR Reporter ←───────────────┤─→ okr_weekly_log.md
                                         │                ↓
Figma + Liquid → Comparison Verifier ────┘         須藤さん共有レポート
```

## Component 1: GA4 Design Insight Engine

**役割**: 数値データからデザイン改善の「具体的アクション」を自動生成する

### 入力
- Googleスプレッドシート（既存）
  - `デイリーログv2`: 訪問回数・直帰率・CTA
  - `流入元別`: チャネル別セッション
  - `ページ別ビュー`: パス別PV
  - `検索ページ別`: GSC クリック/表示/順位
- Liquidセクションファイル一覧（`sections/*.liquid`）

### 処理
1. 直近7日のデータ集計
2. Claude API にコンテキスト渡し（データ + セクション一覧 + デザイン原則）
3. 以下を出力させる:
   - 問題箇所（ページパス × 指標）
   - 対応するLiquidセクション（推測ベース）
   - 改善仮説（CTA配置、コピー変更、レイアウト等）
   - 優先度（高/中/低 × 実装工数小/中/大）

### 出力
- 新規シート: `UI改善提案_W{週番号}`

| 優先度 | ページ | セクション | 現状指標 | 問題仮説 | 改善案 | 実装工数 |
|---|---|---|---|---|---|---|
| 高 | /pages/company | fam-corp-hero.liquid | 直帰率78%(平均65%↑) | ファーストビューでCTAが見えない | CTAボタンを画面上部に移動+資料DL強調 | 小 |

- Slack DM（ユーザー宛）: 「UI改善提案_W{週番号} を生成しました。{提案数}件」＋シートURL

### 実装
- 新規ファイル: `projects/analytics/design_insight.py`（データ集計 + Claude API呼び出し + シート書き込み）
- 依存: 既存の `config.json`, `ga4_service_account.json`, gspread
- Claude API: `anthropic` パッケージ（要インストール）
- **実行方式**: Claude scheduled task として毎週月曜 08:00 起動
  - scheduled-tasks MCP で登録（既存の okr-weekly-report と同じ方式）
  - タスク内容: 「design_insight.py を実行 → 結果を Slack MCP で宮川にDM」
  - Python単体のlaunchdではなくClaude経由にする理由: Slack DM送信にSlack MCPを使えるため、別途Bot設定不要

## Component 2: OKR Slack-Aware Reporter

**役割**: Slack会話から進捗を自動検出し、Component 1の改善提案と統合した週次レポートを生成

### 入力
- Slack MCP: `#famコンテンツwg` `#pmo` `#事業開発` 直近7日の発言
- `okr_weekly_log.md` 前週分
- `project_okr_fambox.md` OKR構造
- 最新の `UI改善提案_W{週番号}` シート

### 処理
1. Slack MCPで3チャンネルから直近7日のメッセージ取得
2. Claude API が KR別に分類:
   - 完了タスク（動詞: 実装した/完成/公開した 等）
   - 意思決定（動詞: 決めた/方針 等）
   - ブロッカー（動詞: 詰まっている/待ち 等）
3. Component 1 の改善提案を「来週の山場」候補として統合
4. OKR v5.1 構造（KR1-5）に沿ってレポート生成

### 出力
- `okr_weekly_log.md` に追記（既存フォーマット踏襲）
- `FAMBOX_OKR_宮川.xlsx` の「週次タスク」シート更新
- ユーザーに Slack DM: 「W{週番号} レポート生成完了。確認依頼」

### 実装
- 既存の木曜17時 scheduled task のプロンプトを拡張（新規skillファイル作成）
- Slack MCP は既に接続済みのため新規依存なし

## Component 3: Liquid Comparison Verifier

**役割**: Figmaデザインと実装Liquidの視覚差分を自動検出し、修正プロンプトを生成

### 入力
- Figma画像URL（または画像パス）
- Liquidファイルパス（または対応するpreview-*.html）

### 処理
1. Figma画像取得（Figma MCP経由）
2. Liquidプレビューのスクリーンショット生成（Playwright or Chrome MCP）
3. Gemini API（`gemini-2.0-flash-exp`）に両画像を渡し、差分を抽出:
   - 色の差
   - レイアウトのずれ
   - タイポグラフィの不一致
   - エフェクト（blur/gradient）の再現度
4. 差分を構造化JSON + Markdown レポートで出力
5. 修正プロンプト自動生成（プロンプトビルダーv4の形式に合わせる）

### 出力
- `projects/liquid_verifier/reports/YYYY-MM-DD-{section}.md`
- `projects/liquid_verifier/reports/YYYY-MM-DD-{section}.json`
- 修正プロンプト（標準出力 + クリップボード）

### 実装
- 新規ディレクトリ: `projects/liquid_verifier/`
- 新規ファイル: `verify.py`, `config.json`
- 依存: `google-generativeai`, `playwright`
- CLI: `python verify.py --figma <url> --liquid <path>`
- 手動起動（自動化は将来のv6で検討）

## 連携仕様

### データの流れ
1. 月曜 08:00: Component 1 が `UI改善提案_W{N}` を生成 → ユーザーDM
2. 月〜水: ユーザーが提案を確認、実装着手
3. 実装時: Component 3 を手動起動して視覚検証
4. 木曜 17:00: Component 2 が Slack + Component 1 提案 + 実装結果を統合 → レポート生成

### KR連鎖への対応
- Component 1 の出力は KR-5（計測基盤）の成果
- Component 2 のレポート内「来週の山場」は KR-1（ブランド）+ KR-3（直帰率改善）に紐づく
- Component 3 の検証は KR-1 の実装品質保証

## 優先順位と段階実装

**Phase 1（最優先・今週実装）**: Component 1（GA4 → 改善提案シート + Slack DM）
- 理由: 既存の analytics インフラ上に構築可能。最短で価値を出せる
- 完了条件: 月曜朝に実行→シート生成→DM到達

**Phase 2（次週）**: Component 2 の Slack統合拡張
- 理由: Slack MCP経由で既存の木曜タスクを拡張するだけ
- 完了条件: 次の木曜17時に Slack発言が反映された報告生成

**Phase 3（余裕あれば）**: Component 3（Liquid Verifier）
- 理由: 独立性が高く、手動起動で足りる
- 完了条件: 1セクションで差分レポート生成成功

## 制約と注意事項

### プライバシー
- Slackメッセージは分析後に保存しない（メモリ内のみ）
- GA4データは既存プロジェクト範囲内のみ

### API費用
- Claude API: 週1回 × 2コンポーネント（月8回、数百円想定）
- Gemini API: Component 3 は手動起動のため利用時のみ

### 失敗時の挙動
- Slack MCP エラー時: Slack情報なしで既存ロジックのみでレポート生成（degraded）
- Claude API エラー時: エラーログ + Slack DM で通知、手動フォールバック
- シート書き込み失敗時: ローカルJSONに保存 + リトライ

### 冪等性
- 同じ週の2回目実行時はシート上書きではなく `_v2` 等でサフィックス付与
- okr_weekly_log.md は追記のみ（重複チェック付き）

## 成功条件

- Component 1: 毎週月曜に改善提案シートが生成され、宮川が「この提案を元に今週の実装タスクを決められる」状態
- Component 2: 木曜の須藤さん共有レポートに「Slackで議論されたこと」が自動で反映される
- Component 3: プロンプトビルダーv4の出力→Liquid実装→視覚検証のループが手動3コマンドで完結

## 次のステップ

このspecを元に、writing-plansスキルで Phase 1 (Component 1) の詳細実装プランを作成する。
