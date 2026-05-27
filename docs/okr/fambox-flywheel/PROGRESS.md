# PROGRESS — フェーズ別進捗

> 最新フェーズの状況は **🟢=完了 / 🟡=進行中 / ⚪=未着手** で確認。

最終更新：2026-05-22

---

## 現在のフェーズ

**Phase 0：永続化基盤構築**（このディレクトリ自体の整備）

---

## Phase 0：永続化基盤構築（2026-05-22）

> ゴール：構想・決定・進捗が永続的に追跡でき、セッション断絶からの復帰ができる状態にする。

- 🟢 `docs/okr/fambox-flywheel/` ディレクトリ作成
- 🟢 README.md（プロジェクト全体像）
- 🟢 ARCHITECTURE.md（4層構造正典）
- 🟢 DECISIONS.md（意思決定ログ D-001〜D-009）
- 🟢 PROGRESS.md（このファイル）
- 🟢 OPEN_QUESTIONS.md
- 🟢 phases/phase-1-generate.md（プレースホルダ）
- 🟢 phases/phase-2-sense.md（プレースホルダ）
- 🟢 phases/phase-3-reach.md（プレースホルダ）
- 🟢 phases/phase-4-learn.md（プレースホルダ）
- 🟢 phases/phase-5-multibrand.md（プレースホルダ）
- 🟢 sessions/2026-05-22-kickoff.md（キックオフブレスト議事録）
- 🟢 memory: `project_fambox_flywheel.md` 作成
- 🟢 MEMORY.md に追加（Active Development 最上位）
- 🟢 git commit（後で実施）

**達成条件：** 新セッションで「Flywheel の続き」と言われた時、Claude が文脈を完全復元できる。

---

## Phase 1：Generate 層詳細設計 + プロトタイプ（2026-05-23 〜 2026-06）

> ゴール：マレルチームが Shopify セクション UI を「自分の手で」作れるプロトタイプを作る。

### 1-A：要件詳細化
- ⚪ マレルチームへのインタビュー（または推測ペルソナ確定）
  - どのセクションを最も作りたいか
  - 既存セクションのどれをコピーして派生させたいか
  - フォーム入力のどの粒度なら使えるか
- ⚪ 「マレル向け最小機能セット」の定義

### 1-B：操作 UI（マレル向け）
- ⚪ フォーム入力 UI 設計（既存 LPB v4.1 をベースに簡略化）
- ⚪ フォーム → LPB プロンプトへの変換ロジック
- ⚪ 出力プレビュー UI（生成結果を実機表示）

### 1-C：Brand Brain（生成エンジン側）
- ⚪ Brand DNA + DS + bugs.md を Claude Project に統合
- ⚪ プロンプトテンプレート（用途別）作成
- ⚪ 自動 schema-lint（push 前検証）
- ⚪ 出力 → Shopify Theme push の半自動化

### 1-D：パイロット運用
- ⚪ マレルチーム 1人（候補：松浦さん）にパイロット使用してもらう
- ⚪ フィードバック収集 → 改善
- ⚪ 全員展開判断

**達成条件：** マレルチームが「宮川さんに頼まず」「FAMBOX らしい」Shopify セクションを1つ作れる。

---

## Phase 2：Sense 層強化（2026-07 想定）

> ゴール：データから「次に作るべきもの」を自動提案する。

- ⚪ Design Insight Engine の出力フォーマット標準化（JSON）
- ⚪ Shopify Analytics / GA4 データの統合パイプライン
- ⚪ SNS データ取込（Instagram / X）
- ⚪ 「弱いアセット」自動検知ロジック
- ⚪ Generate 層への指示書フォーマット（→ Generate と接続）

**達成条件：** 月曜にダッシュボードを開くと「今週はこれを作るべき」が3件表示される。

---

## Phase 3：Reach 層自動化（2026-08 想定）

> ゴール：生成 → 配信のパイプラインを自動化する。

- ⚪ Shopify Theme push API 連携
- ⚪ Canva Brand Kit + テンプレ自動更新
- ⚪ メール配信（Klaviyo / Seal）統合
- ⚪ SNS 半自動投稿（Buffer / Hootsuite 検討）

**達成条件：** Generate で作ったものが「ボタン1つで」配信される。

---

## Phase 4：Learn 層構築（2026-09 想定）

> ゴール：配信したアセットの結果を Sense にフィードバックする。

- ⚪ アセット ID 管理（タグ付け）
- ⚪ KPI 自動紐付け（アセット ID → CTR / CVR / 売上）
- ⚪ 反省ログ自動生成（ChatGPT / Claude）
- ⚪ Brand Memory Graph 更新ロジック
- ⚪ Sense へのフィードバックループ完成

**達成条件：** ホイールが1周自動で回る。

---

## Phase 5：マルチブランド化（2026-Q4 〜 想定）

> ゴール：他ブランド（架空 Brand B）で同じ Flywheel を回せるようにする。

- ⚪ Brand Layer 完全分離（FAMBOX 固有のリテラル除去）
- ⚪ DS 4階層の抽象化検証
- ⚪ Brand B の DNA + DS テンプレ作成
- ⚪ 2ブランド並走テスト

**達成条件：** FAMBOX 設定を Brand B 設定に差し替えるだけで動く。

---

## 進捗ルール

- 着手時：⚪ → 🟡 に変更 + 開始日記入
- 完了時：🟡 → 🟢 に変更 + 完了日記入
- ブロック時：🟡 のまま、`OPEN_QUESTIONS.md` に記録
- 新タスク追加時：そのフェーズに ⚪ で追加 + DECISIONS.md にも反映
