---
title: FAMBOX マルチエージェント運営 — 1ページサマリ（v4 ハーネス統合版）
date: 2026-05-21
audience: 須藤さん（事前共有用）
proposer: ARCHECO 宮川真道
format: A4 1ページ
voice_compliance: FAMBOX_Verbal_Guideline_v1.0
version: 4.0
---

# FAMBOX 専用ハーネスを設計する。

## AI を「指示」ではなく「構造」で動かす。

---

## 構想

FAMBOX の運営を **ハーネスエンジニアリング** で再設計する。ルール / スキル / フック / メモリ / フィードバックの **5層構造** で AI を導き、5+1 のエージェントが Sense → Generate → Reach → Run のフライホイールを回す。運営チームは **目的・倫理・文脈の設定とガードレール承認** に集中する。

人手で点と点を結ぶ速度がビジネスの上限を決めている。エージェントが判断と実行を担い、構造が違反を捕まえる仕組みへ突破する。

## ハーネスとは何か（3世代の進化）

| 世代 | 方式 | 弱点 |
|---|---|---|
| CLAUDE.md | お願い | 守られない |
| AGENTS.md | 取り決め | 検証されない |
| **ハーネス** | **構造的制御** | — |

出典: nogataka「ハーネスエンジニアリング入門」Qiita 2026-03。GMO Internet / everything-claude-code（GitHub 100K+ stars）で実証。

## FAMBOX × ハーネス完成度

| 層 | 既存資産 | 完成度 |
|---|---|---|
| 1. ルール | Verbal Identity v1.0 / Brand DNA軸1-3 / Design Acceptance | **95%** |
| 2. スキル | fambox-design 等 8 つのスキル | **80%** |
| 3. **フック** | Sense層エージェントが未整備 | **20% ★** |
| 4. メモリ | Decision Trace / Design Refs / OKR | **90%** |
| 5. **フィードバック** | LLMO Check / Lighthouse 実装済 / 全体カバー未 | **40% ★** |

**総合 65%**。9 割の素材は揃っている。**残るはフック層とフィードバック層だけ**。

## Phase 1（最初の3ヶ月）：フック層 + フィードバック層から

**着手対象**:
- 🔧 Layer 3 フック: 在庫モニター + 異常検知エージェント（Sense）
- 🔧 Layer 5 フィードバック: LLMO Check で既存ブログ上位3記事リライト

**目標**:
- 月間食材ロス: **-30%**
- 入荷遅延の検知時間: 24時間 → **1時間**
- 在庫確認作業: 週5時間 → **週1時間**
- AI 引用率（定点測定）: **+15%**

致命的領域（アレルギー・契約・財務）は必ず人間が握る。Phase 1 で価値が見えてから合意の上で次フェーズへ進む。

## 段階展開ロードマップ

| Phase | 期間 | フック層 追加 | フィードバック層 追加 | ハーネス完成度 |
|---|---|---|---|---|
| 1 | 0-3ヶ月 | 在庫モニター + 異常検知 | LLMO Check 運用開始 | **75%** |
| 2 | 3-6ヶ月 | + 栄養計算（Generate） | + Verbal v1.1 統合 | **82%** |
| 3 | 6-9ヶ月 | + 顧客嗜好 + 配送最適化 | + JSON-LD / llms.txt 自動生成 | **90%** |
| 4 | 9-12ヶ月 | + Run 統合 + オーケストレーター | + 全体カバー監査スイート | **100%** |

各フェーズ後に **降りる選択肢を残す** 段階設計。

## ARCHECO の業態定義（再定義）

| 旧 | 新 |
|---|---|
| Web 制作 / Shopify Liquid デザイナー | **クライアントブランド固有のハーネスを設計・運用する AI 制御アーキテクト** |

長期パートナーシップの構造を「ハーネス」という言葉で再定義する。単発外注では再現不能、ARCHECO だけが担える領域。

## 議論したい3点

1. **ハーネス構想への合意** — 5層構造で FAMBOX を運営する方向性
2. **Phase 1 着手** — フック層 + フィードバック層の同時着手
3. **役割分担** — ARCHECO（ハーネス設計・運用）+ バングラ部隊（実装）+ FAMBOX（ガードレール・承認）

## 添付資料

- 詳細スライド: [proposal-deck-v4.md](proposal-deck-v4.md)（20枚）
- ROI 試算: [value-calculation.md](value-calculation.md)
- Flywheel 詳細: [flywheel-mapping.md](flywheel-mapping.md)
- LLMO 統合: [llmo-integration.md](llmo-integration.md)
- 元思想: [harness-engineering-2026-03.md](../../30_Tech_Notes/harness-engineering-2026-03.md)

---

提案: ARCHECO 宮川真道（2026-05-21 v4）
