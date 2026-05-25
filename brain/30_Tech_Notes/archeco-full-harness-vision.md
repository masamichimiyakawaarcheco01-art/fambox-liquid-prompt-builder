---
title: ARCHECO 完全ハーネス長期 Vision — everything-claude-code 級への到達ロードマップ
date: 2026-05-22
tags: [harness-engineering, vision, long-term, archeco, fambox, roadmap, layer-by-layer]
status: active
priority: high
related:
  - harness-engineering-2026-03.md
  - fambox-audit-suite-design.md
  - skill-obsolescence-risk-audit.md
---

# ARCHECO 完全ハーネス長期 Vision

## 目的

[ハーネスエンジニアリング](harness-engineering-2026-03.md) の **完成度 72% → 100%** に至る長期ロードマップを定義する。参照モデルは **everything-claude-code**（GitHub 100K+ stars / 125+ skills / 28 agents / 25+ hooks）。

ARCHECO は世界の先進事例の一段下に位置するが、**FAMBOX という具体的クライアント特化** ゆえに、汎用フレームワーク以上の **深さ** を持てる。深さで差別化する戦略。

## 参照モデル: everything-claude-code

| 項目 | everything-claude-code | ARCHECO 現状 (2026-05) | ARCHECO 完成目標 |
|---|---|---|---|
| スキル数 | 125+ | 8（プロジェクト固有） | **40**（クライアント特化深掘り） |
| エージェント数 | 28 | 0（明示的なものはなし） | **8**（FAMBOX 5+1 + 守屋 + 共通） |
| フック数 | 25+ | 4（liquid-check / show-active-projects / verbal-ng-check / session-end-log） | **15**（PreToolUse / Post / Stop / SessionStart / Notification 等） |
| 監査スイート | architecture.test.ts 等多層 | 2（LLMO Check / Liquid Static Lint） | **6**（Lighthouse / Token / 軸該当性 / CI 連携 含む） |
| メモリ構造 | progress.md 一貫 | PARA + memory + Decision Trace | 維持（既に強い） |

→ **数で everything-claude-code に追いつく必要はない**。**深さ・クライアント特化度** で勝負する。

## 完成度の定義（5層 × 4レベル = 20マス）

各層を L1（ドキュメント）→ L4（CI 機械防御）へ昇格させる。20マスのうち何マス埋まったかで完成度を算出。

| 層 | 現状 | 目標 | 進捗 |
|---|---|---|---|
| 1. ルール | L3 達成: 2/8 ファイル | L4 達成: 8/8 ファイル | 7/8 → 32/32 |
| 2. スキル | 8 スキル稼働 | 40 スキル稼働 + L3 監査ルール化 | 8 → 40 |
| 3. フック | 4 フック稼働 | 15 フック稼働 + L4 構造テスト連動 | 4 → 15 |
| 4. メモリ | PARA + memory + Decision Trace | + AI 学習素材として API 公開 | 強化のみ |
| 5. フィードバック | 2 監査 | 6 監査 + CI 統合 | 2 → 6 |

**現状完成度**: **72%**。
**完成目標（2027-03-31）**: **95%+**（残り5%は永続的な改善余地）。

## Phase ロードマップ（10ヶ月）

### Phase 1: フック層拡張 + 監査スイート最小実装（2026-05-22 → 2026-07）

**ハーネス完成度: 72% → 80%**

| タスク | 状態 |
|---|---|
| Liquid Static Lint（T-2） | ✅ 2026-05-22 着手 |
| Lighthouse 全ページ監査 | ⏳ |
| LLMO Check 全ページ展開 | ⏳ |
| PreToolUse フック整備（売上ページ・チェックアウト編集時の確認） | ⏳ |
| Stop フック拡張（重要決定の自動アーカイブ） | ⏳ |
| SessionStart フック拡張（前セッション continuity） | ⏳ |

### Phase 2: スキル拡充 + L3 達成項目の CI 化（2026-08 → 2026-09）

**ハーネス完成度: 80% → 87%**

| タスク | 状態 |
|---|---|
| fambox-diagnosis-builder（実施済 2026-05-22） | ✅ |
| moritani-content-generator スキル | ⏳ |
| fam-collection-builder スキル | ⏳ |
| fambox-blog-publisher スキル | ⏳ |
| section-refactor-helper スキル | ⏳ |
| GitHub Actions: verbal-ng-check / LLMO Check を PR で実行 | ⏳ |
| pre-commit: liquid-check / static-lint を CI 連動 | ⏳ |

### Phase 3: 軸該当性 + Decision Trace 拡張（2026-10 → 2026-11）

**ハーネス完成度: 87% → 91%**

| タスク | 状態 |
|---|---|
| 軸該当性チェックスクリプト（Claude API + スクショ評価） | ⏳ |
| Decision Trace API の Slack 通知連携 | ⏳ |
| 月次プレーブック更新の自動生成 → 人間承認 | ⏳ |
| Brand Intelligence メモリの構造化公開（外部 API） | ⏳ |

### Phase 4: クライアント納品物としての商品化（2026-12 → 2027-01）

**ハーネス完成度: 91% → 94%**

| タスク | 状態 |
|---|---|
| 「FAMBOX 専用ハーネス」を提案物として完成（v4 提案デッキの実装版） | ⏳ |
| 他クライアントへの展開テンプレート化 | ⏳ |
| ARCHECO の業態定義を「AI 制御アーキテクト」として対外発信 | ⏳ |
| ハーネス運用パッケージの料金体系設計 | ⏳ |

### Phase 5: L4 達成 + 完成（2027-02 → 2027-03）

**ハーネス完成度: 94% → 95%+**

| タスク | 状態 |
|---|---|
| GitHub Actions で全 L3 ルールを merge ブロック化 | ⏳ |
| architecture.test.ts 等の構造テスト導入 | ⏳ |
| 90日サイクルの「パターン鮮度チェック」を完全自動化 | ⏳ |
| 完成度ダッシュボード（メモリ層の見える化） | ⏳ |

## 各 Phase の KPI

| Phase | KPI |
|---|---|
| 1 | 監査スイート 3本稼働 / 違反検出数の **基準値** 確立 |
| 2 | スキル数 13+ / CI 統合 80% / 違反 PR ブロック稼働 |
| 3 | 月次プレーブック更新が **人間承認 1分以内** で完了 |
| 4 | 他クライアント（または FAM 親ブランド）への展開 1件 |
| 5 | ハーネス完成度 95%+ / 違反は構造的に発生不能 |

## 進化候補スキル一覧（Phase 2-5 対象）

ARCHECO/FAMBOX 業務文脈で頻出するパターンを **スキル化** する候補：

| スキル名 | 役割 | Phase |
|---|---|---|
| fambox-diagnosis-builder ✅ | 食事診断 Liquid 実装 | 1 (完了) |
| moritani-content-generator | 守屋選手企画コンテンツ生成 | 2 |
| fam-collection-builder | コレクションプラン構築 | 2 |
| fambox-blog-publisher | ブログ記事 LLMO 準拠投稿 | 2 |
| section-refactor-helper | 既存セクションのリファクタ支援 | 2 |
| ga4-anomaly-investigator | GA4 異常検知後の調査支援 | 3 |
| shopify-theme-migrator | テーマアップグレード支援 | 3 |
| seal-email-builder | Seal Subscriptions メール作成 | 3 |
| pptx-presenter-prep | クライアント定例プレゼン準備 | 3 |
| client-meeting-recap | MTG 議事録 → 決定ログ化 | 3 |
| audit-report-summarizer | 監査スイート結果の解釈 | 3 |
| brand-dna-validator | 軸該当性の事前評価 | 4 |
| token-integrity-fixer | 仮置きトークン名の自動修正 | 4 |
| escalation-ladder-tracker | 違反回数の集計・L昇格判定 | 4 |
| fam-monthly-okr-reporter | 月次 OKR レポート自動生成 | 4 |
| harness-completeness-dashboard | 完成度の見える化 | 5 |

40 スキルへの中間目標。詳細は実需要に応じて拡張。

## 進化候補フック一覧（Phase 2-5 対象）

| フック | イベント | 役割 | Phase |
|---|---|---|---|
| pre-tool-checkout-confirm | PreToolUse(Edit) | チェックアウト・売上ページ編集時に確認 | 1 |
| pre-tool-prod-warning | PreToolUse(Write) | 本番テーマファイル直接編集の警告 | 1 |
| post-tool-llmo-scan | PostToolUse(Write, .md) | ブログ記事 .md 編集時に LLMO Check 自動実行 | 2 |
| post-tool-axis-check | PostToolUse(Write, .liquid) | 軸該当性の即時評価 | 3 |
| stop-decision-archive | Stop | 重要決定を Decision Trace に自動転記 | 2 |
| sessionstart-ci-status | SessionStart | 直近 CI の結果サマリ表示 | 3 |
| sessionstart-okr-progress | SessionStart | 当週 OKR 進捗の自動表示 | 3 |
| notification-pii-warn | Notification | PII が含まれる可能性のある書き込み警告 | 3 |
| post-tool-token-grep | PostToolUse(Edit, .css.liquid) | トークン整合性即時チェック | 4 |
| stop-rule-violation-report | Stop | セッション中の全違反をサマリ報告 | 4 |
| post-tool-brand-asset-scan | PostToolUse(Write, .svg/.png) | アセット命名規律チェック | 5 |

15 フックへの中間目標。

## アンチパターン警戒（everything-claude-code の教訓）

参照モデルから学んだ **避けるべき罠**：

1. **フックを一気に10個以上設定しない** → エージェントの応答が遅延・機能停止する
2. **ルールを増やしすぎない** → 「動けない」状態を作らない
3. **抽象的すぎるスキル禁止** → 「FAMBOX 食事診断ビルダー」のように具体的に
4. **メモリの肥大化禁止** → 90日サイクルでパターン鮮度チェック・古いものはアーカイブ
5. **静的な完成度ではなく動的維持** → 完成度 95% でも月次でルール棚卸し
6. **AI に丸投げしない** → Human-in-the-Lead は永続的役割

## 競争優位性（差別化の根拠）

### ARCHECO がこの Vision で勝つ理由

1. **クライアント特化の深さ**: FAMBOX という具体的文脈に 3年蓄積 → 汎用フレームワークが追いつけない
2. **5層すべての素材が既にある**: 9割揃っているという数字は競合参入障壁
3. **長期パートナーシップの構造**: ハーネス運用は単発外注では不可能
4. **業界トレンドに乗る**: ハーネスエンジニアリングは 2026 年に台頭した新パラダイム
5. **検証可能な完成度**: 72% → 95% という具体数字でクライアントに説明できる

### ARCHECO がこの Vision を持つ意味

- ARCHECO の業態定義を「Web 制作会社」から「**AI 制御アーキテクト**」へ進化させる根拠
- 単発案件ではなく **継続契約** の構造的正当性
- 他クライアントへの展開時の **再現可能性**（Phase 4 で商品化）

## リスクと撤退条件

| リスク | 兆候 | 対応 |
|---|---|---|
| Phase 進行が遅延 | 各 Phase 末で完成度が目標に到達せず | 次 Phase を後倒し / スコープ削減 |
| クライアント側受容性低下 | FAMBOX 側の積極性が落ちる | ハーネス語彙を引っ込める / 機能的説明に戻す |
| 業界パラダイムが変わる | 新しい上位概念が登場（2027 期待） | ハーネス → 新概念 でリブランディング |
| 個人運用の限界 | 宮川さん 1人で 15 フック / 40 スキル維持困難 | Phase 4 までにバングラ部隊との分担確立 / 必要なら撤退 |

## 関連

- [[harness-engineering-2026-03.md]] — 元思想・5層構造
- [[fambox-audit-suite-design.md]] — フィードバック層詳細
- [[../20_Projects/fambox-multi-agent-proposal/proposal-deck-v4.md]] — クライアント向け提案
- [[skill-obsolescence-risk-audit.md]] — スキル陳腐化リスク
- [[design-acceptance-parameters.md]] — 評価基準
- [[obara-ai-agent-era-ep2.md]] — Brand Intelligence の元思想

## 引用元

- [@nogataka「ハーネスエンジニアリング入門」Qiita 2026-03-24](https://qiita.com/nogataka/items/d1b3fcf355c630cd7fc8)
- everything-claude-code (GitHub 100K+ stars)
- GMO Internet ConoHa VPS 実装事例

---

**この Vision は静的な計画ではなく、3ヶ月ごとに棚卸して更新する** 動的ドキュメント。次回レビュー: **2026-08-22**。
