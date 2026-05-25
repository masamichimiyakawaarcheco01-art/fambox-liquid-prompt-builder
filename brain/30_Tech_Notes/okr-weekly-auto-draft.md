---
title: OKR週次レポート 自動ドラフト生成 — 既存スクリプトのブリッジ設計
date: 2026-05-15
tags: [ai-era, automation, okr, weekly-report, p1, analytics, human-on-the-loop]
topics: [ai, business-strategy, automation]
status: active
priority: high
target_project: projects/analytics
related:
  - skill-obsolescence-risk-audit.md
  - obara-ai-agent-era-ep1.md
  - design-acceptance-parameters.md
---

# OKR週次レポート 自動ドラフト生成 — 既存スクリプトのブリッジ設計

## 現状把握（重要）

**既に充実したインフラがあった**：

| 既存スクリプト | 役割 | 状態 |
|---|---|---|
| `projects/analytics/daily_collect.py` | GA4/Shopify日次データ収集 | ✅ launchd で日次実行中 |
| `projects/analytics/weekly_report.py` | 月-日の週次集計 → スプレッドシート | ✅ launchd で週次実行中 |
| `projects/analytics/weekly_insight_report.py` | 事業開発向けインサイトレポート | ✅ 運用中 |
| `projects/analytics/monthly_report.py` | 月次レビュー（前月比較含む） | ✅ 運用中 |
| `projects/analytics/alert_check.py` | 異常値検知 + Slack通知 | ✅ 運用中 |
| `projects/analytics/design_insight.py` | Phase 1 Design Insight Engine | ✅ 月曜08:03 自動実行 |

**FAMBOXの月次レビュー例**（[docs/okr/FAMBOX_4月レビュー_20260508.md](../../docs/okr/FAMBOX_4月レビュー_20260508.md)）の構造：
- 30秒サマリ（須藤さん向け）
- 主要指標テーブル（前月比較・評価記号）
- KR別の主要成果（O1ブランドDNA、O2集客、O3顧客接点など）
- 次月のフォーカス

→ **「ゼロから作る」ではなく「既存集計 → OKR形式ドラフトに翻訳」** が最短経路。

## 設計：OKR Auto-Draft Bridge スクリプト

新規スクリプト `projects/analytics/okr_weekly_draft.py` を追加。
既存 `weekly_report.py` と `weekly_insight_report.py` の **出力を統合し、Claude API でOKR形式の Markdown ドラフトを生成** する。

### データフロー

```
daily_collect.py（日次）
   ↓
weekly_report.py（週次・月曜 09:00）
   ↓ → スプレッドシート: 週次サマリーシート
weekly_insight_report.py（週次・月曜 10:00）
   ↓ → スプレッドシート: インサイトシート
okr_weekly_draft.py（週次・木曜 16:00） ★NEW
   ↓ 既存シートを読む
   ↓ Claude API で OKR形式に翻訳
   ↓ 前週との差分・KR紐付け・次週アクション提案
   ↓ → docs/okr/weekly-drafts/YYYY-WW.md
   ↓ → Slackに通知（要レビュー）
宮川さん（木曜17時の定期報告前）が **物語化部分のみ追記** → 須藤さん共有
```

### スクリプト構成（実装案）

```python
# projects/analytics/okr_weekly_draft.py
"""
FAM Analytics - OKR週次ドラフト生成
weekly_report.py + weekly_insight_report.py の結果を読み、
Claude API で須藤さん共有用のOKR形式ドラフトを生成する。

使い方:
  python okr_weekly_draft.py              # 直近完了週
  python okr_weekly_draft.py 2026-05-12   # 指定日を含む週
"""

# 1. config + spreadsheet 接続（既存スクリプトと同じパターン）
# 2. 週次サマリーシートから当週・前週のデータ取得
# 3. インサイトシートから施策結果を取得
# 4. OKR 構造（O1〜O5、KR1〜KRn）を別ファイル（okr_structure.yml）から読み込み
# 5. Claude API に以下を渡してドラフト生成:
#    - 当週 vs 前週の数値
#    - 異常検知のアラート（alert_check.py の結果）
#    - 直近のインサイトレポート要点
#    - OKR定義（O/KRと現状）
# 6. Markdown を docs/okr/weekly-drafts/YYYY-WW.md に保存
# 7. Slack に「レビューしてください」通知
```

### Claude API への投入プロンプト（テンプレ）

```
あなたは FAMBOX のOKR管理者です。以下の週次データから、須藤さん共有用のレポート
ドラフトを Markdown で作成してください。

【期間】
2026-MM-DD 〜 2026-MM-DD（W##）

【主要指標（前週比較）】
| 指標 | 前週 | 今週 | 変化 | 評価 |
|---|---|---|---|---|
{metrics_table}

【今週の異常検知】
{anomalies}

【直近のインサイトレポート要点】
{insights}

【FAMBOX OKR構造】
{okr_structure}

【出力形式】
docs/okr/FAMBOX_4月レビュー_20260508.md と同じ構造で：
1. 30秒サマリ（3行以内）
2. 主要指標テーブル
3. KR別の主要成果（O1〜O5）
4. 次週のフォーカス（最大3点）
5. リスク・要判断（あれば）

【制約】
- 物語化部分は「事実のみ」記載、感情的表現は使わない
- 数値の解釈・原因推測は「（仮説）」を明記
- 宮川さんが追記する余地を残す
```

## 実装ステップ

### Day 1（今週末）— 設計確定
- [x] 本設計ドキュメント作成
- [ ] 既存 `weekly_report.py` の出力フォーマット確認
- [ ] OKR構造を YAML 化（`projects/analytics/okr_structure.yml`）
- [ ] Slack Webhook URL の準備状況確認

### Day 2-3 — 実装
- [ ] `okr_weekly_draft.py` 雛形作成
- [ ] スプレッドシート読み込み部分（既存スクリプトから流用）
- [ ] Claude API 呼び出し部分
- [ ] Markdown 出力 + ファイル保存
- [ ] Slack 通知

### Day 4 — 試験運用
- [ ] 過去1週分のデータで手動実行
- [ ] 宮川さんが手で書いたレポートと比較・調整
- [ ] プロンプト微調整

### Day 5 — 自動化
- [ ] launchd plist 作成（`com.fam.analytics.okr-weekly-draft.plist`）
- [ ] 毎週木曜 16:00 自動実行に設定
- [ ] 1週間運用 → 改善判断

## OKR構造の YAML 化（事前準備）

`projects/analytics/okr_structure.yml`：

```yaml
quarter: 2026-Q2
objectives:
  - id: O1
    title: "FAMBOXブランドDNA & DS 確立"
    key_results:
      - id: KR1
        title: "Verbal Identity GL v1.0 確定"
        target: 100
        current: 100
        unit: "%"
      - id: KR2
        title: "Design System コアコンポーネント実装"
        target: 20
        current: 8
        unit: "components"
  - id: O2
    title: "集客拡大"
    key_results:
      - id: KR3
        title: "月間セッション数"
        target: 1500
        current: 862
        unit: "sessions"
  # 以下続く...
```

このYAMLを更新するだけで、自動ドラフトが最新のKR数値を反映する。

## ガードレール（[design-acceptance-parameters.md](design-acceptance-parameters.md) 準拠）

- **自動却下条件**:
  - 指標データが取れていない週 → ドラフト生成せず、エラー通知のみ
  - Claude API がレート制限 → リトライ後失敗ならエラー通知
- **警告条件**:
  - 主要指標で **2σ 以上の異常変動** → アラートを目立つ位置に挿入
  - 前週と完全同一の結果 → データ取得失敗の可能性をフラグ
- **人間が必ず確認する項目**:
  - 「次週のフォーカス」
  - 「リスク・要判断」セクション
  - 数値解釈の妥当性

## 期待される効果

| 観点 | Before | After |
|---|---|---|
| 週次レポート作成時間 | 60〜90分（手動集計含む） | **15分以下**（ドラフト確認 + 物語化追記のみ） |
| 抜け漏れ | 多い（指標見落とし） | ほぼゼロ（自動集計） |
| 異常検知の反映 | 手動で記憶頼り | 自動でアラート挿入 |
| 前週比較 | 手動計算 | 自動 |

## 関連
- [[skill-obsolescence-risk-audit.md]] — 高リスク業務B「FAMBOX OKR週次レポート」の移行先
- [[obara-ai-agent-era-ep1.md]] — Human-on-the-Loop の元思想
- [[design-acceptance-parameters.md]] — ガードレール仕様
- `projects/analytics/weekly_report.py` — 既存集計
- `projects/analytics/weekly_insight_report.py` — 既存インサイト
- `projects/analytics/alert_check.py` — 既存異常検知
- `docs/okr/FAMBOX_4月レビュー_20260508.md` — レポート形式の参照
