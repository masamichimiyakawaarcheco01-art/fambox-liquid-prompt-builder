---
title: FAMBOX マルチエージェント運営提案（v4 ハーネス統合）
date: 2026-05-15
last_updated: 2026-05-21
tags: [project, fambox, ai-agent, proposal, p2, system-of-action, harness-engineering]
status: active
proposer: ARCHECO 宮川真道
proposal_target: 須藤さん（FAMBOX）+ FAMBOX運営チーム
target_meeting: 次回FAMBOX定例
version: 4.0
related:
  - ../../30_Tech_Notes/harness-engineering-2026-03.md
  - ../../30_Tech_Notes/obara-ai-agent-era-ep1.md
  - ../../30_Tech_Notes/chesky-airbnb-ai-era-redesign.md
  - ../../50_Business_Context/fambox-brand-dna-axes.md
verbal_guideline: docs/okr/FAMBOX_Verbal_Guideline_v1.0.md
---

# ゴール

FAMBOX の運営を **ハーネスエンジニアリング 5層構造（ルール / スキル / フック / メモリ / フィードバック）** で再設計し、5+1 のエージェントが Sense → Generate → Reach → Run のフライホイールを回す体制への進化を、次回 FAMBOX 定例で正式提案する。

ARCHECO の業態定義を **「クライアントブランド固有のハーネスを設計・運用する AI 制御アーキテクト」** に進化させる長期パートナーシップ構造を確立する。

# Why

[尾原Ep1](../../30_Tech_Notes/obara-ai-agent-era-ep1.md) の核心：

> **「ビジネスのスピードが、人間が手作業で点と点を結びつけるスピードによって上限設定されてしまっている」**

FAMBOXも同じ構造を抱えている：
- 食材供給の変動 → 手動でメニュー再構成（数時間〜数日）
- 顧客個別最適化 → 個別対応で属人化
- 異常検知 → 人間が気づいた時点で機会損失

**「全任せ」ではなく「Human-on-the-Loop」** で、運営チームは **ガードレール設計・最終承認** に集中、実行はエージェントが担う。

# 成功条件（Definition of Done）

- [ ] 提案資料一式（プレゼン用 + サマリ + ROI）が完成
- [ ] FAMBOX定例で提案 → **「次のステップを踏み出す合意」** を得る
- [ ] Phase 1（在庫モニターエージェント）の **試作着手の合意** を得る
- [ ] バングラ部隊（トモアキ経由）・須藤さんとの **役割分担合意**

# 成果物一覧

| ファイル | 用途 | 状態 |
|---|---|---|
| [overview.md](overview.md) | プロジェクト概要（このファイル） | ✅ |
| **[proposal-deck-v4.md](proposal-deck-v4.md)** | **★最新版 プレゼン用スライド20枚（ハーネス統合）** | ✅ |
| **[executive-summary-v4.md](executive-summary-v4.md)** | **★最新版 1ページサマリ（ハーネス統合）** | ✅ |
| [proposal-deck.md](proposal-deck.md) | v2 プレゼン20枚（Experience Flywheel構造・参照用） | ✅ |
| [executive-summary.md](executive-summary.md) | v1 1ページサマリ（参照用） | ✅ |
| [llmo-integration.md](llmo-integration.md) | LLMO 統合層（v3 拡張・v4 に統合済） | ✅ |
| [flywheel-mapping.md](flywheel-mapping.md) | Experience Flywheel 詳細マッピング | ✅ |
| [value-calculation.md](value-calculation.md) | ROI 試算（時間削減・売上影響） | ✅ |
| [decisions.md](decisions.md) | 意思決定ログ | ✅ |

# トーン・声の方針

[FAMBOX Verbal Identity Guideline v1.0](../../../docs/okr/FAMBOX_Verbal_Guideline_v1.0.md) に厳密準拠：

- **冷静で情熱的** — 科学的・事実ベース × 挑戦への深いリスペクト
- **NG語** を使わない（サポート / 寄り添う / 応援 / 〜かもしれません 等）
- **Verb Bank** を使う（壁を超える / 突破する / 動かす / 踏み出す / 燃やす 等）
- **キーワード16語**（内燃 / 推進 / 上昇 / 循環）を最低1系統含める
- **断定する**（曖昧な語尾で逃げない）

提案先は須藤さん。**「FAMBOXの言葉でFAMBOXの未来を語る」** スタンス。ARCHECOが提案者でも、FAMBOX側のトーンで書く。

# マイルストーン

- [ ] **MS1: 5/15** — 提案資料一式 ドラフト完成（本日）
- [ ] **MS2: 5/16-19** — 宮川さん内部レビュー・修正
- [ ] **MS3: 次回定例** — 正式提案
- [ ] **MS4: 定例後1週間** — Phase 1 試作着手の合意取得
- [ ] **MS5: Phase 1 着手** — 在庫モニターエージェントの試作開始（2026-06-?）

# 提案の構造（3層）

```
[戦略層] AI時代の構造変化 → System of Intelligence から System of Action へ
   ↓
[ビジョン層] FAMBOXを 5エージェント + 人間監督 のマルチエージェント運営へ
   ↓
[実行層] Phase 1: 在庫モニターから始める Quick Win
       Phase 2-3: 段階的に5エージェント体制へ拡張
```

# 関連プロジェクト

- **[ハーネスエンジニアリング 元思想](../../30_Tech_Notes/harness-engineering-2026-03.md)** — v4 の核となる統合概念
- [守屋選手アンバサダー企画](../moritani-ambassador/overview.md) — エージェント化候補（撮影→文字起こし→記事ドラフト）と接続
- [LPB Human-on-the-Loop](../../30_Tech_Notes/lpb-human-on-the-loop-roadmap.md) — 同じ思想の自社ツール実装
- [FAMBOXブランドDNA軸](../../50_Business_Context/fambox-brand-dna-axes.md) — 軸1 デジタル/システム型と整合

# リスク・要判断

- **クライアント側の温度感**: 須藤さんの「全任せ」への抵抗感を測る必要
- **予算規模**: 5エージェント全実装は数百万円規模 → Phase 1 単独で価値を見せる
- **バングラ部隊との分担**: バックエンド実装は外部委託前提、設計は宮川さん
- **既存業務との並走**: OKR・守屋企画と並行。提案後の本実装はリソース調整必要
