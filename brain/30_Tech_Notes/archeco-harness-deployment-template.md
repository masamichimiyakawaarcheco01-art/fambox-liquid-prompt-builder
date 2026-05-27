---
title: ARCHECO ハーネス展開テンプレート — 他クライアントへの導入5フェーズ
date: 2026-05-25
tags: [archeco, product, harness-deployment, client-template, business, p4]
status: active
priority: high
related:
  - harness-engineering-2026-03.md
  - archeco-full-harness-vision.md
  - archeco-business-definition-v2.md
  - ../20_Projects/fambox-multi-agent-proposal/proposal-deck-v4.md
---

# ARCHECO ハーネス展開テンプレート

ARCHECO が **他クライアント企業向け** にハーネスエンジニアリングを導入する **5 フェーズ標準フロー**。FAMBOX 適用例（2026-03〜2026-05）を **参照モデル** として含む。

## 商品化の意義

[archeco-full-harness-vision](archeco-full-harness-vision.md) の Phase 4 を実装する。ARCHECO の業態定義を「Web 制作」から **「クライアントブランド固有のハーネスを設計・運用する AI 制御アーキテクト」** へ正式に進化させる。

- **単発外注では再現不能** な長期パートナーシップ商品
- **継続契約の構造的根拠** （ハーネスの運用＝月次サブスク型）
- **再現性の証明** → FAMBOX で 78% → 100% を 3 日で達成した実績

---

## 導入 5 フェーズ

### Phase 1: 診断 (1-2 週間)

クライアントの **現状ハーネス完成度** を 5 層で評価。

| 評価項目 | 確認内容 |
|---|---|
| Layer 1 ルール | Verbal Identity / Brand Guideline / 実装規約の有無と粒度 |
| Layer 2 スキル | 業務手順書 / Playbook / 再利用可能なテンプレ |
| Layer 3 フック | 自動化済プロセス（CI / hooks / 通知） |
| Layer 4 メモリ | 過去意思決定の記録 / Brand Intelligence 素材 |
| Layer 5 フィードバック | lint / 監査 / KPI モニタリング |

**成果物**:
- 診断レポート（完成度 % + ギャップ一覧）
- 重点強化候補 3 つ
- 投資概算

### Phase 2: 設計 (2-4 週間)

クライアント固有のハーネス **5 層の青写真** を作る。

| 設計項目 | 出力 |
|---|---|
| Verbal Identity ガイドライン | NG 語 / Verb Bank / トーン定義 |
| Brand DNA 軸 | 視覚言語の n 軸構造（FAMBOX 例: 3 軸 + 1 候補） |
| 業務 Playbook | 主要 5-10 業務の手順書 |
| 監査スイート要件 | 何を機械検出すべきか |
| Decision Trace 設計 | 修正履歴の構造化スキーマ |

**成果物**:
- ハーネス設計書（5 層詳細）
- 段階導入ロードマップ（3-12 ヶ月）
- KPI 定義

### Phase 3: 構築 (2-4 ヶ月)

実装フェーズ。**フック層・フィードバック層から着手** し、ルール・スキル・メモリは段階的に整備。

| 構築タスク | 担当 |
|---|---|
| Verbal Identity ドキュメント化 | ARCHECO + クライアント |
| 主要監査スクリプト 2-3 本 | ARCHECO（フロント）+ バングラ部隊（バックエンド） |
| Slack/Discord 通知フック | ARCHECO |
| Decision Trace 蓄積基盤 | ARCHECO + バングラ部隊 |
| 既存資産のマイグレーション | ARCHECO |

**成果物**:
- 稼働中のハーネス（最小 3 フック + 2 監査スクリプト）
- 初回監査レポート

### Phase 4: 運用 (3-12 ヶ月 / 継続)

**月次定期チェック + クォータリー鮮度チェック** を運用に組み込む。

| 運用項目 | 頻度 |
|---|---|
| 月次違反件数レポート | 月次 |
| クライアント定例での共有 | 月次 |
| パターン鮮度チェック | 四半期 |
| Decision Trace の集約 → 新ルール候補抽出 | 四半期 |
| 完成度ダッシュボード更新 | 月次 |

**成果物**:
- 月次ハーネスレポート
- ハーネス完成度の継続的向上

### Phase 5: 評価 (継続)

**1 年経過時点で ROI 評価 + 次フェーズ判断**。

| 評価項目 | 計測 |
|---|---|
| 完成度推移 | 5 層各 % の月次変動 |
| 違反検出件数推移 | 監査スイートの累積 |
| 規律違反コスト削減 | 「過去同じミスを N 回繰り返した」がなくなった件数 |
| AI 経由認知獲得 | LLMO スコア・AI 引用率 |
| クライアント業務時間削減 | 自動化されたタスク × 時間単価 |

**判断**:
- ✅ 継続 → Phase 4 を継続 + ハーネスの新機能拡張
- ⏸ 一時停止 → 価値再評価
- ↩ 方向転換 → 別パッケージ提案

---

## FAMBOX 参照モデル（実績）

| Phase | 期間 | 主要成果 |
|---|---|---|
| Phase 1 診断 | 2026-03〜04 | ハーネス未認識段階。Brand DNA / Verbal Identity / Animation Library は既存 |
| Phase 2 設計 | 2026-05-21 | ハーネス v4 提案デッキ完成（20 スライド） |
| Phase 3 構築 | 2026-05-22〜25 | 4 フック → 6 フック / 8 → 20 スキル / 監査スイート Phase 1-2 |
| Phase 4 運用 | 2026-06〜 | 月次レポート開始予定 |
| Phase 5 評価 | 2027-03 | 1 年経過時 ROI 評価予定 |

**現在のハーネス完成度**: **100%**（ 5 層全て 95%+ / 違反 0 件）。

---

## 料金体系設計（参考）

クライアント規模・既存資産で変動。**サブスク型** が基本。

### Phase 1-2: 初期設計フェーズ（一括）
- 小規模クライアント: ¥XXX 万
- 中規模クライアント: ¥XXX 万
- 大規模クライアント: 別途見積もり

### Phase 3: 構築フェーズ（一括 or 月額）
- 監査スイート構築: ¥XXX 万
- スキル / フック整備: ¥XXX 万

### Phase 4-5: 運用フェーズ（月額 / クォータリー）
- 月次レポート + ガードレール調整: ¥XXX 万/月
- クォータリー鮮度チェック: ¥XXX 万/四半期
- 緊急対応: 別途時給

→ 詳細は [archeco-business-definition-v2.md](archeco-business-definition-v2.md) と併用。

---

## 適用候補クライアント特性

ハーネス導入が **特に効く** クライアント像：

1. **すでに 3 年以上 Verbal/Visual 資産が蓄積**（FAMBOX 型）
   → 9 割の素材があり、フック層とフィードバック層だけで一気に立ち上がる

2. **AI 経由の認知獲得を重視**（LLMO ニーズ）
   → Verbal Identity v1.1 系の拡張で即効果

3. **複数チャネル運用**（Shopify + ブログ + SNS + メール 等）
   → 統一規律が労力削減に直結

4. **中長期パートナー前提**
   → 単発契約より、月次運用で価値が累積する関係

逆に **向かない** クライアント：

- ブランド資産が未整備（先に Brand DNA 構築が必要）
- 短期施策のみ求めている（PoC + 即終了）
- 自社内に技術リソースなし（バングラ部隊等の外注前提でも可能）

---

## ARCHECO の役割境界

| ARCHECO が握る | クライアントが握る |
|---|---|
| ハーネス 5 層の設計 | 最終承認（致命的領域） |
| フック層・フィードバック層の実装 | 目的・倫理・文脈の設定 |
| メモリ層の構造化 | Brand Intelligence の中身（コンテンツ自体） |
| バングラ部隊との分担管理 | クライアント業務の運用責任 |
| 月次・四半期レポート | レポートに基づくアクション意思決定 |

---

## 関連

- [ハーネスエンジニアリング](harness-engineering-2026-03.md) — 元思想・5 層構造
- [archeco-full-harness-vision](archeco-full-harness-vision.md) — 10ヶ月ロードマップ
- [archeco-business-definition-v2](archeco-business-definition-v2.md) — 業態定義 / 対外発信用
- [proposal-deck-v4](../20_Projects/fambox-multi-agent-proposal/proposal-deck-v4.md) — FAMBOX 適用例
- [export-brand-intelligence.sh](../../tools/memory/export-brand-intelligence.sh) — メモリ層エクスポート
- [Harness Dashboard](../../tools/dashboard/index.html) — 完成度の可視化
