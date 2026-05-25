---
title: FAMBOX Experience Flywheel — 詳細マッピング
date: 2026-05-19
tags: [fambox, ai-agent, experience-flywheel, ep2-applied]
status: active
related:
  - proposal-deck.md
  - ../../30_Tech_Notes/obara-ai-agent-era-ep2.md
---

# FAMBOX Experience Flywheel — 詳細マッピング

提案資料（v2）の補足資料。Adobe Summit 2026 で示された **Experience Flywheel（Sense → Generate → Reach → Run）** をFAMBOX運営に当てはめた詳細設計。

## フライホイール全体像

```
       ┌─→ ① Sense（感知）─────────┐
       │                             │
   ④ Run（学習）              ② Generate（生成）
       ↑                             │
       │                             ↓
       └────── ③ Reach（実行）──────┘
                    ↑
            [Human-in-the-Lead]
            目的・倫理・文脈の設定
```

各段階で **Decision Trace** が記録され、Run でプレーブックが更新される。

---

## ① Sense — 感知層

### 役割
環境を24/7監視し、行動の起点になる **シグナル** を発見する。

### 担当エージェント

| エージェント | 監視対象 | データソース |
|---|---|---|
| **在庫モニターAgent** | 食材在庫・賞味期限・仕入先入荷予定 | 仕入先API・倉庫データ |
| **異常検知Agent** | GA4・売上・問合せ・SNS反応の異常 | GA4・Shopify・Slack |
| **顧客嗜好Agent**（兆候側） | 継続率低下兆候・離脱前シグナル | CRM・注文履歴 |
| **市場Agent**（オプション） | 競合動向・トレンド・バズ | X監視・Google Trends |

### 検知基準（多層）

| Layer | 内容 |
|---|---|
| L1 静的閾値 | 「セッション前日比-30%」等 |
| L2 統計検知 | 移動平均±2σ |
| L3 季節性検知 | 曜日・月パターンから逸脱 |
| L4 仮説生成 | Claude APIで原因仮説3つ |

→ [GA4 Anomaly Detection Enhancement](../../30_Tech_Notes/ga4-anomaly-detection-enhancement.md) で詳細設計済。

### 人間が握る
- 仕入先の追加・変更判断
- 大規模インシデント時のエスカレーション判断
- 監視対象の追加判断

### 期待出力
- **シグナル+仮説のセット** が Generate 層へ流れる
- 例: 「鶏胸肉の入荷停止 / 影響範囲: 顧客XX名 / 仮説: 仕入先A の物流遅延」

---

## ② Generate — 生成層

### 役割
Senseで掴んだシグナルに対し、**ガードレール内で** 解決策を自動生成する。

### 担当エージェント

| エージェント | 生成内容 |
|---|---|
| **栄養計算Agent** | PFCバランス・カロリー・微量栄養素を満たすメニュー候補 |
| **メニュー組み立てAgent**（統合） | 食材組み合わせ × アスリート別最適化 |
| **コンテンツ生成Agent**（オプション） | SNS応答・記事ドラフト |

### ガードレール（事前構造）

| 軸 | 制約 |
|---|---|
| **栄養** | 栄養基準（タンパク質X g以上、ナトリウムY g以下） |
| **アレルギー** | 不可食材リスト → 二重チェック必須 |
| **ブランド** | [FAMBOX軸1/2/3](../../50_Business_Context/fambox-brand-dna-axes.md) に整合 |
| **Verbal** | [Verbal Identity Guideline](../../../docs/okr/FAMBOX_Verbal_Guideline_v1.0.md) 準拠 |
| **コスト** | 1メニューあたり原価上限 |

### 人間が握る
- 栄養基準の決定（栄養士監修）
- アレルギー対応ルールの最終承認
- 季節キャンペーン・新商品の方針

### 期待出力
- **複数の解決策候補** が Reach 層へ流れる
- 例: 「メニューA（鶏胸→豚もも肉） / メニューB（鶏胸→豆腐+卵）」

---

## ③ Reach — 実行層

### 役割
Generate で生成した解決策を **実際の顧客に届ける**。

### 担当エージェント

| エージェント | 実行内容 |
|---|---|
| **配送最適化Agent** | 全配送先の一括ルート計算・冷蔵管理・配達タイミング |
| **顧客通知Agent** | パーソナライズメール・SNS応答 |
| **CRM自動化Agent** | 解約防止施策・クーポン発行・継続促進 |
| **オーケストレーター** | 全エージェント間の整合性確保 |

### Reach の効率化技法

| 技法 | 効果 |
|---|---|
| 巡回セールスマン問題の秒解 | 配送ルート最適化 |
| タイムゾーン計算 | 国境を超える承認フロー（Ulta事例） |
| パーソナライズ配信 | 嗜好別のメッセージ生成 |

### 人間が握る
- 配送パートナーとの関係維持
- 顧客との直接対話（人間関係）
- 重大クレーム時のエスカレーション

### 期待出力
- **実行ログ** が Run 層へ流れる
- 顧客反応（開封・クリック・解約等）も Run 層へ

---

## ④ Run — 学習層

### 役割
顧客反応を **回収・分析** し、プレーブックを更新する。

### 学習対象

| カテゴリ | 学習元データ |
|---|---|
| **継続率パターン** | 顧客嗜好Agent + CRM自動化Agent のログ |
| **離脱要因** | 解約理由 + 直前の体験データ |
| **新ペルソナ発見** | 異常検知が示した「想定外の挙動」 |
| **プレーブック更新** | Decision Trace 履歴からのルール抽出 |
| **新トレンド** | 市場Agent のシグナル分析 |

### プレーブック自動更新の仕組み

```
Decision Trace（修正履歴の蓄積）
   ↓
月次レビュー（自動 + 人間確認）
   ↓
新ルール候補の抽出（Claude API）
   ↓
[人間] 採用 / 棄却の判断
   ↓
ガードレール更新（design-acceptance-parameters.md / fambox-brand-dna-axes.md）
   ↓
次のループから新ルールが適用される
```

→ [LPB Decision Trace Design](../../30_Tech_Notes/lpb-decision-trace-design.md) で実装済。

### 人間が握る
- 新ルール採用 / 棄却の最終判断
- プレーブックの構造的変更（軸追加等）

### 期待出力
- **更新されたプレーブック** が次回 Sense → Generate のガードレールに反映される

---

## エージェント × フライホイール マトリクス

| エージェント | Sense | Generate | Reach | Run |
|---|:---:|:---:|:---:|:---:|
| 在庫モニター | ◎ | ○ | | ○ |
| 異常検知 + 仮説 | ◎ | ○ | | ○ |
| 顧客嗜好 | ◎ | ◎ | ◎ | ◎ |
| 栄養計算 | | ◎ | | ○ |
| 配送最適化 | ○ | | ◎ | ○ |
| 顧客通知 / CRM | | ○ | ◎ | ◎ |
| オーケストレーター | ○ | ◎ | ◎ | ◎ |
| 市場Agent（オプション） | ◎ | | | ○ |

◎ = 主担当 / ○ = 関与

---

## Phase 1 → Phase 4 のフライホイール完成度

| Phase | 完成段階 | 動く範囲 | 人間負荷 |
|---|---|---|---|
| Phase 1 | Sense 25% | 在庫モニター + 異常検知 | 大（手動でGenerate以降） |
| Phase 2 | + Generate = 50% | 栄養計算 統合 | 中（手動でReach以降） |
| Phase 3 | + Reach = 75% | 配送・通知 統合 | 小（Run 手動） |
| Phase 4 | + Run = 100% | 完全フライホイール | 最小（Human-in-the-Lead） |

---

## Ulta型 SNSバズ対応のフライホイール例

守屋選手企画の夏合宿シーズン中、深夜にバズ：

| 時刻 | Flywheel段階 | 動き |
|---|---|---|
| 0:00 | Sense | バズ発生 — Market Agent が検知 |
| 0:05 | Generate | キャンペーン構築（既存素材 + 文脈に整合するコピー） |
| 0:10 | Reach（人間承認） | モバイル通知 → 宮川さん or 須藤さん承認 |
| 0:15 | Reach | 配信開始 → 収益化 |
| 翌日 | Run | 反応データ収集 → 次回のバズ対応プレーブック更新 |

**従来**: 翌朝対応 → 既にバズの波は通過済 → 機会喪失
**新運営**: 15分対応 → 波に乗る → 機会獲得

---

## ブランド・インテリジェンスの素材棚卸し

FAMBOXが既に保有する **ブランド・インテリジェンスの素材** （Run層の学習ベース）：

| 素材 | 場所 | 学習に使える属性 |
|---|---|---|
| Verbal Identity Guideline v1.0 | docs/okr/ | NG語・Verb Bank・キーワード16語 |
| FAMBOX Brand DNA 軸1/2/3 | brain/50_Business_Context/ | 静の信頼・動の発火・努力の結晶 |
| Design References（13件） | brain/45_Design_Refs/ | NG/OK判断 + 軸別配置 |
| 月次レビュー・OKR | docs/okr/ | 戦略意思決定の履歴 |
| Verbal修正履歴 | LPB Decision Trace（着手済） | 修正前後 + 理由タグ |
| 顧客対応ログ | CRM | 個別文脈 |
| MTG議事録 | 各種 | 意思決定の背景 |

→ これらを **構造化して AI に渡せば**、FAMBOX独自の Brand Intelligence が立ち上がる。

---

## 関連
- [proposal-deck.md](proposal-deck.md) — v2 プレゼン本体
- [executive-summary.md](executive-summary.md) — 1ページサマリ
- [value-calculation.md](value-calculation.md) — ROI試算
- [decisions.md](decisions.md) — 意思決定ログ
- [尾原Ep2](../../30_Tech_Notes/obara-ai-agent-era-ep2.md) — Experience Flywheel の元思想
- [LPB Decision Trace Design](../../30_Tech_Notes/lpb-decision-trace-design.md) — Run層の実装
- [GA4 Anomaly Detection](../../30_Tech_Notes/ga4-anomaly-detection-enhancement.md) — Sense層の実装
