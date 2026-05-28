# Environment Audit v0.1 — 宮川さんの現在の AI / Design 環境棚卸し

> **目的：** Marc に見せて差分（gap）を引き出すための「現状スナップショット」。
> **使い方：** Marc に共有 → 「足りない」「冗長」「左側用に変えるべき」を引き出す。

最終更新：2026-05-26

---

## 1. AI ツール

| ツール | 用途 | 利用頻度 | 備考 |
|---|---|---|---|
| **Claude Code (CLI)** | デザイン構想・Liquid 生成・コードレビュー・ドキュメント生成 | 毎日 | プライマリ |
| **Claude (Web)** | 単発相談・テキスト生成 | 週数回 | サブ |
| **ChatGPT** | 単発質問・他視点 | 週数回 | 補助 |

### Claude Code の使い方
- 主にデザイン構想・Shopify Liquid 生成・既存セクション修正
- カスタム skills（後述）でブランド適用を自動化
- Custom hooks で post-tool 検証（liquid-check.sh / schema-lint）

---

## 2. MCP サーバー（接続中）

| サーバー | 用途 |
|---|---|
| **Slack** | チームコミュニケーション、メッセージ送受信、検索 |
| **Figma Bridge** | Figma ファイル操作（ノード作成、レイアウト等） |
| **Figma 公式 (use_figma)** | デザイン情報取得、コード変換 |
| **Notion** | ドキュメント管理、タスク、ナレッジベース |
| **Google Drive** | ファイル管理、共有ドキュメント |
| **Gmail** | メール検索、ラベル管理 |
| **Google Calendar** | スケジュール |
| **Claude in Chrome** | ブラウザ自動化、Web スクレイピング |
| **Claude Preview** | フロントエンド確認、コンソールログ |
| **Iconify** | アイコン検索・取得 |
| **Lottie** | アニメーション素材検索 |
| **Context7** | ライブラリドキュメント取得 |
| **Scheduled Tasks** | 定期実行スクリプト管理（FAMレモン君環境）|
| **MCP Registry** | MCP 検索・追加 |

---

## 3. デザインツール

| ツール | 用途 |
|---|---|
| **Figma** | 主力デザインツール、Marc 流 Figma kit 検討中 |
| **Canva** | チーム共有テンプレ（マレル向け）|
| **Adobe Photoshop / Illustrator** | 紙印刷物、最終仕上げ |
| **Shopify Theme Editor** | Liquid セクションの実機編集・確認 |

---

## 4. 既存資産（教師データ候補）

> ★ Marc に「これを AI にどう食わせるか」を相談したいコア資産。

### 4-1. ブランド資産

| 資産 | 場所 | 内容 | 完成度 |
|---|---|---|---|
| **FAMBOX Brand DNA v1.0** | `brand/fambox/brand-dna/current.md` | 視覚言語、Editorial × Lab メタファー（2026-05-27 v1.0 promoted） | v1.0 |
| **FAMBOX Verbal Identity v1.0** | `docs/okr/FAMBOX_Verbal_Guideline_v1.0.md` | コピートーン、語彙、avoid 表現 | v1.0 |
| **FAMBOX Design System v0.5** | `brand/fambox/design-system/` | tokens / components / patterns | v0.5 |
| **bugs.md 28規律** | `brand/fambox/design-system/bugs.md` | BUG/DOCTRINE/PROC 28エントリ。Anti-pattern 回避規範 | 28 entries |
| **L0 翻訳表 v0.1** | `brand/fambox/design-system/` | 抽象指示 → トークン値の翻訳 | v0.1 / 412 行 |
| **animation-library v0.1** | `brand/fambox/animation-library-v0.1.md` | モーション規範 | v0.1 |
| **STRATEGY.md** | `brand/fambox/STRATEGY.md` | ブランド戦略 | 最新 |

### 4-2. 制作資産

| 資産 | 場所 | 内容 | 件数 |
|---|---|---|---|
| **Shopify Liquid セクション** | `projects/fambox/sections/` | 過去制作セクション（FAMBOX 専用 + Dawn 派生）| 100+ ファイル |
| **Liquid sections (FAM)** | `projects/fam/sections/` | FAM 親ブランド | 20+ |
| **Snippets** | `projects/fambox/snippets/` | 再利用部品 | 多数 |
| **Email templates (Seal)** | `projects/fambox/emails/seal/` | 12種ワイヤフレーム | 12 |

### 4-3. ツール・自動化資産

| ツール | 場所 | 内容 |
|---|---|---|
| **LPB v4.1（Liquid Prompt Builder）** | `liquid-pipeline/` | Figma → Liquid 構造化プロンプト生成。37% → 84% 精度向上の実績 |
| **schema-lint.py** | `tools/audit/` | Shopify Schema 事前検証 |
| **liquid-section-lint.sh** | `tools/audit/` | 全 136 セクションの構文監査 |
| **liquid-check.sh** | `.claude/hooks/` | PostToolUse フック、単一ファイル構文検証 |
| **pre-commit hook** | git | コミット前ブロック |
| **GitHub Actions audit.yml** | `.github/workflows/` | PR merge ブロック |
| **lighthouse-scan.sh** | `tools/audit/` | パフォーマンス監査 |
| **llmo-scan.sh** | `tools/audit/` | LLM 関連監査 |

### 4-4. Claude Custom Skills（既に存在）

`/Users/archecoinc./Desktop/Claude_1/.claude/skills/` 配下：

| Skill | 用途 |
|---|---|
| `fambox-design` | FAMBOX ブランド DNA 適用 UI 構築 |
| `fambox-diagnosis-builder` | 食事診断ウィザード Liquid 実装 |
| `fambox-blog-publisher` | ブログ記事公開支援 |
| `fam-collection-builder` | コレクションプラン構築 |
| `seal-email-builder` | Seal メール HTML |
| `section-refactor-helper` | セクションリファクタ |
| `shopify-theme-migrator` | テーマ移行 |
| `token-integrity-fixer` | トークン整合性修正 |
| `audit-report-summarizer` | 監査レポート要約 |
| `brand-voice-generator` | トーン・ブランドシステム生成 |
| `ga4-anomaly-investigator` | GA4 異常検知 |
| `pptx-generator` / `pptx-presenter-prep` | プレゼン資料 |
| `sop-creator` | 運用手順書 |
| `x-bookmark-harvester` | X ブックマーク取込 |
| `moritani-content-generator` | コンテンツ生成 |
| `client-meeting-recap` | クライアントMTG議事録 |
| `mcp-client` | 汎用 MCP クライアント |
| `remotion` | Remotion 動画作成 |
| `skill-creator` | スキル作成 |

---

## 5. ワークフロー（現在の典型パターン）

### 5-1. Shopify セクション制作（最も頻度高）

```
1. Figma デザイン受領 / 要件聴取
2. get_design_context() → FigmaDesignToken JSON 取得
3. LPB v4.1 で構造化プロンプト生成
4. Claude Code でLiquid 生成
5. ローカル grep 検証（feedback_shopify_liquid_specificity.md 5罠チェック）
6. schema-lint.py で事前検証
7. Shopify CLI push（dev theme）
8. curl で本番 HTML 検証
9. DevTools Computed で 3段階目視確認
10. live push（必要に応じて）
```

### 5-2. 検証スタック（L4 達成済）

| 層 | ツール |
|---|---|
| Claude post-tool | `liquid-check.sh`（単一ファイル構文） |
| 全体スキャン | `liquid-section-lint.sh`（136 セクション） |
| Git pre-commit | フック自動実行 |
| CI/CD | GitHub Actions audit.yml（PR merge ブロック）|

### 5-3. デザイン記憶システム

`~/.claude/projects/.../memory/` 配下に：
- 29ファイルの feedback / project / reference / user メモリ
- セッション開始時に MEMORY.md → 該当ファイルを Claude が自動 Read
- 失敗パターン・成功パターン・好みを永続学習

---

## 6. 自動化が進んでいる領域

| 領域 | 状態 |
|---|---|
| **Sense 部分**（Design Insight Engine）| 🟢 月曜08:03 自動実行（FAMレモン君環境 Phase 1） |
| **GA4 / Shopify Analytics 自動レポート** | 🟢 稼働中 |
| **明細データ拡張**（安原さん依頼）| 🟢 5/6 自動化済 |
| **Schema lint**（事前検証）| 🟢 commit/push 前自動 |
| **Liquid 構文監査**（136 セクション）| 🟢 PR/コミット時自動 |
| **セッション学習**（feedback 自動蓄積）| 🟢 session-end フック |

---

## 7. ギャップ（推測：Marc 流と比較した不足点）

> ここを Marc にレビューしてもらいたい。

### 7-1. 教師データの統合

- **現状**：DS v0.5、bugs.md、Brand DNA、Verbal Identity が **別ファイルで散在**
- **理想**：単一の AI が一括参照できる **統合教師データレイヤー**
- **Marc に聞きたい**：あなたはどのフォーマットで教師データを AI に食わせている？

### 7-2. プロンプト技術の体系化

- **現状**：LPB v4.1 で Figma → 構造化プロンプトはあるが、用途別の使い分けが暗黙的
- **理想**：用途別（LP / セクション / バナー / メール）のプロンプトテンプレートが標準化
- **Marc に聞きたい**：プロンプトの「型」をどう管理している？再利用は？

### 7-3. 「持ってこい資料」フォーマット

- **現状**：依頼者から要件を引き出す型がない（暗黙的に宮川さんが質問しながら）
- **理想**：D-018 の Standard 形式が Slack ワークフロー化されている
- **Marc に聞きたい**：須藤さんとのキャッチボールで使った「要件 + ジャーニー」はどうフォーマット化した？

### 7-4. レビュー文化

- **現状**：宮川さん 1人運用、外部レビューなし
- **理想**：金曜事業開発で発表 → 緊張感あるフィードバック
- **Marc に聞きたい**：あなた達のチーム会（マーク・アフタブ・角田）の運用ルールは？

### 7-5. 出力の即時 push 化

- **現状**：Shopify CLI で手動 push
- **理想**：Claude → Shopify Theme への半自動 push
- **Marc に聞きたい**：あなたの環境では生成 → 確認 → 配信はどう繋がっている？

### 7-6. 多出力対応

- **現状**：Liquid 専用、他フォーマット（PPT / 紙 / 画像 / 動画）は別ツール
- **理想**：中間表現（JSON）→ 任意フォーマット出力
- **Marc に聞きたい**：右側で多サービスをカバーする時、どう抽象化している？

---

## 8. 仮の次のステップ（Marc のフィードバック後に確定）

1. **教師データ統合レイヤー設計**（DS + bugs.md + Brand DNA + Verbal を統合形式に）
2. **用途別プロンプトテンプレ作成**（LP / セクション / バナー / メール）
3. **Slack ワークフロー化**（指示書フォーマット）
4. **金曜発表会の運用ルール確立**
5. **半自動 push パイプライン**（Shopify CLI 周辺）

---

## 9. 用語の整理

| 用語 | 意味 |
|---|---|
| **Step 1 / Step 2 / Step 3** | 須藤さん3段階モデル（D-010）|
| **7割 / 3割** | AI と人間の境界（D-020） |
| **Middle & Fast** | 宮川さんの目指すポジショニング（D-017）|
| **指示書（持ってこい資料）** | Step 2 で依頼者が書くフォーマット（D-018）|
| **左側 / 右側** | 宮川さんの領域 / Marc 達の領域（須藤さん用語）|

---

## バージョン履歴

| バージョン | 日付 | 内容 |
|---|---|---|
| v0.1 | 2026-05-26 | 初稿。Marc レビュー前のスナップショット |
