---
title: ARCHECO 業態定義 v2 — AI 制御アーキテクト
date: 2026-05-25
tags: [archeco, business-definition, brand, sales, p4, public-facing]
status: active
priority: high
related:
  - harness-engineering-2026-03.md
  - archeco-harness-deployment-template.md
  - archeco-full-harness-vision.md
audience: ARCHECO 営業 / Web サイト / 採用 / 対外プレゼン
---

# ARCHECO

## クライアントブランド固有のハーネスを設計・運用する **AI 制御アーキテクト**

---

## キーメッセージ（1 行）

> AI を「指示」ではなく「構造」で動かす — 御社専用のハーネスを設計し、運用する。

## 何をしているか（3 行）

ARCHECO は、企業のブランド（言葉・視覚・知識）を AI 時代に正しく動かすため、**5 層の制約と検証**（ルール・スキル・フック・メモリ・フィードバック）からなる **ハーネス** を設計・運用します。

CLAUDE.md / AGENTS.md という従来の「お願い」「取り決め」の次世代として、**構造で違反を捕まえる仕組み** を構築します。

FAMBOX で 78% → 100% を 3 日で達成した実績で、**他クライアントへの展開** が可能になりました。

---

## なぜ「いま」ARCHECO なのか

### 業界の構造変化

| 世代 | 制御方式 | 弱点 |
|---|---|---|
| 第1世代 (2023-24) | CLAUDE.md（お願い） | 守られない |
| 第2世代 (2025) | AGENTS.md（取り決め） | 検証されない |
| **第3世代 (2026-)** | **ハーネス（構造的制御）** | — |

参照: nogataka「ハーネスエンジニアリング入門」Qiita 2026-03、GMO Internet / everything-claude-code（GitHub 100K+ stars）

### ARCHECO の独自ポジション

- **クライアント特化の深さ**: 汎用フレームワークではなく **ブランド固有** のハーネスを構築
- **5 層全体の設計力**: 1 層だけのツール提供ではなく **アーキテクチャ全体** を担う
- **長期運用パートナー**: 単発案件ではなく **月次・四半期の継続運用**
- **検証可能な完成度**: 「完成度 X%」を数字で示せる

---

## サービス内容

### 1. ハーネス設計フェーズ（Phase 1-2）

- 現状診断（5 層完成度評価）
- ブランド固有ハーネスの設計書
- 段階導入ロードマップ（3-12 ヶ月）

### 2. ハーネス構築フェーズ（Phase 3）

- Verbal Identity ガイドライン作成
- Brand DNA 軸 / Animation Library 構築
- 監査スイート実装（lint / Lighthouse / LLMO Check）
- フック層整備（PreToolUse / PostToolUse / Stop）
- Decision Trace 蓄積基盤

### 3. ハーネス運用フェーズ（Phase 4-5）

- 月次違反件数レポート + 推奨アクション
- クォータリー鮮度チェック
- ハーネス完成度ダッシュボードの継続更新
- 新ルール候補の抽出 + 採用判断支援
- AI 時代の業界トレンド反映（年次レビュー）

---

## 料金体系

クライアント規模・既存資産・対象範囲で変動。**サブスク型** が基本。

| フェーズ | 期間 | 形態 | 概算 |
|---|---|---|---|
| Phase 1 診断 | 1-2 週間 | 一括 | ¥XXX 万 |
| Phase 2 設計 | 2-4 週間 | 一括 | ¥XXX 万 |
| Phase 3 構築 | 2-4 ヶ月 | 一括 + 月額 | ¥XXX 万 + ¥XX 万/月 |
| Phase 4-5 運用 | 12 ヶ月以上 | 月額 / クォータリー | ¥XXX 万/月 + ¥XX 万/四半期 |

詳細見積りは初回面談後に確定。

---

## 実績（FAMBOX）

### 期間
2026-03 〜 2026-05（3 ヶ月）

### Before
- ハーネス完成度: 0%（概念未認識）
- 違反件数（Liquid セクション 136 個）: 508 件
- 自動化された監査: 0 件
- AI 引用最適化: 未対応

### After
- **ハーネス完成度: 100%**（5 層全て 95%+）
- 違反件数: **0 件**（-100%）
- 自動化監査スクリプト: 4 本稼働
- LLMO Check API + GitHub Actions で merge ブロック化

### 数値インパクト
- 違反検出から修正までの時間: 数日 → **数分**（フック化）
- セクション編集の手戻り: 月 N 回 → **0**（pre-commit 防御）
- AI 経由の認知 (LLMO): 計測開始

詳細: [FAMBOX マルチエージェント運営提案 v4](../20_Projects/fambox-multi-agent-proposal/proposal-deck-v4.md)

---

## 適用判断（Who is this for?）

### 向いている企業

✅ 3 年以上のブランド資産を持っている（Verbal / Visual / 修正履歴）
✅ AI 経由の認知獲得（LLMO）を重視
✅ 複数チャネル運用（EC / ブログ / SNS / メール）
✅ 中長期パートナーを求めている
✅ 自社の暗黙知を「資産」として体系化したい

### 向いていない企業

❌ ブランド資産が未整備（先に Brand DNA 構築が必要）
❌ 短期施策のみ求めている（PoC + 即終了）
❌ 単発の制作物のみ求めている

---

## ARCHECO の人

### 宮川真道 — AI 制御アーキテクト

UI/UX デザイナー兼 Shopify Liquid 実装者として 10+ 年の経験。FAMBOX で **ブランド DNA 軸 / Verbal Identity / Animation Library / 監査スイート / ハーネス完成 100%** を達成。

業務範囲: ハーネス 5 層の設計・実装・運用、フロントエンド全領域、バングラ部隊との分担管理。

---

## 次の一歩

御社のハーネス完成度を診断します。所要時間は約 30 分。

**お問い合わせ**: <ARCHECO 連絡先>

---

## 関連

- [ハーネスエンジニアリング詳細](harness-engineering-2026-03.md)
- [展開テンプレート](archeco-harness-deployment-template.md)
- [完全ハーネス Vision](archeco-full-harness-vision.md)
- [FAMBOX 実績](../20_Projects/fambox-multi-agent-proposal/proposal-deck-v4.md)
- [Harness Dashboard](../../tools/dashboard/index.html)

## 引用

> 「CLAUDE.md は『お願い』でしかなかった。**守らせる仕組みがない**。」
> 「ハーネス = 信頼しないこと、ではない。**構造的に違反を捕まえることで、信頼を担保する**。」
> — @nogataka, Qiita 2026-03

> 「ARCHECO は、クライアントブランド固有のハーネスを設計・運用する **AI 制御アーキテクト** である。」
> — ARCHECO 業態定義 v2 / 2026-05-25
