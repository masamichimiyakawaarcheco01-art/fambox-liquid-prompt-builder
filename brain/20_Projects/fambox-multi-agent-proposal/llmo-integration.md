---
title: "FAMBOX マルチエージェント運営 — LLMO統合層（v2 拡張）"
date: 2026-05-21
tags: [fambox, multi-agent, llmo, brand-intelligence, ai-citation, text-side]
status: active
priority: high
extends: proposal-deck.md (v2)
related:
  - ../../30_Tech_Notes/baigie-llmo-aio-guide-2026-05.md
  - ../../30_Tech_Notes/fambox-verbal-llmo-extension.md
  - overview.md
---

# FAMBOX マルチエージェント運営 — LLMO統合層

## 位置づけ

[proposal-deck v2](proposal-deck.md) の **Experience Flywheel + 5エージェント** 構造に、**LLMO（テキスト側 Brand Intelligence）** を統合する補強層。

## 核心メッセージ

> **AIに「動かされる」ブランドではなく、「載せられる」ブランドへ。**
>
> FAMBOX の存在自体を、**ChatGPT / Claude / Perplexity が正しく引用する** ように設計する。
> Adobe の **Brand Intelligence** が「視覚側」なら、**LLMO は「テキスト側」** の Brand Intelligence。

## なぜ統合するか

[尾原Ep2](../../30_Tech_Notes/obara-ai-agent-era-ep2.md) が示した Brand Intelligence は **「企業の文脈をAIが学習する」** という概念。これには：

| 側面 | 既存統合状況 |
|---|---|
| **視覚** | [Animation Library v0.1](../../../brand/fambox/animation-library-v0.1.md) ✅ |
| **動き** | 同上 ✅ |
| **トーン** | [Verbal Identity v1.0](../../../docs/okr/FAMBOX_Verbal_Guideline_v1.0.md) ✅ |
| **構造（テキスト）** | **LLMO ★今回追加** |
| **修正履歴** | [LPB Decision Trace](../../30_Tech_Notes/lpb-decision-trace-design.md) ✅ |

→ 5層すべてが揃って **真の Brand Intelligence** が成立する。

## 提案デッキへの追加スライド（v3 候補）

[proposal-deck.md (v2)](proposal-deck.md) の 20枚に、以下2枚を Slide 14 と 15 の間に挿入する v3 拡張案：

---

### NEW Slide 14.5 — LLMO: テキスト側の Brand Intelligence

# AIに「載せられる」FAMBOXへ

**LLMO（Large Language Model Optimization）** = AI が正しく引用するためのコンテンツ最適化。

| 既存ガードレール | + LLMO 追加層 |
|---|---|
| Verbal Identity v1.0（トーン・NG語・Verb Bank） | **質問形見出し / 結論先行 / 具体性ルール / チャンク完結** |
| Design DNA軸（視覚） | **JSON-LD / セマンティックHTML / E-E-A-T明示** |
| Animation Library v0.1（動き） | **llms.txt / 外部メディア寄稿戦略** |

数字（Cloudflare 2026）：
- AI関連ボットがHTMLリクエストの **4.2%** を占有
- Google混合で合計 **7-10%** 予想

→ **AI 経由の認知が「無視できない流量」になっている**。

> **話すこと**: ブランドDNAを「人が見るとき」だけでなく、「AIが読み・引用するとき」にも美しく動かす。
> これが LLMO 統合層の目的です。

---

### NEW Slide 14.6 — LLMO 監査エージェント（6番目のエージェント）

# Agent 6: LLMO 監査（Run 層）

**役割**: 全ての公開コンテンツを LLMO 観点で自動監査し、引用可能性を最大化。

| 段階 | 動き |
|---|---|
| Sense | 新規記事・更新・SNS投稿を検知 |
| **Generate** | **LLMO違反を検出 → 修正案を Claude API で生成** |
| Reach | 編集者に提案 → 承認後に反映 |
| Run | 月次で「AI引用率」をAI定点検索で計測 → ルール更新 |

**自動チェック項目**:
- ✅ 見出しが質問形 / 定義形か
- ✅ 結論先行（最初1-2文 ≤ 200字）
- ✅ 依存表現（上記の通り 等）ゼロ
- ✅ 抽象表現（多くの 等）ゼロ
- ✅ JSON-LD（Organization + Article）
- ✅ セマンティック HTML 構造
- ✅ 著者バイライン
- ✅ 出典リンク

**実装状態（2026-05-21）**:
- LPB v4 に LLMO Check API 実装済（`POST /api/llmo-check/audit`）
- 8項目を自動判定、スコア化（0-100）
- 不合格時は Claude API への修正プロンプトを自動生成

→ **Phase 1 と並行して即着手可能**（既に実装基盤あり）。

> **話すこと**: 6番目のエージェントは既に動き始めています。
> Phase 1 が在庫モニター（外向き）なら、LLMO監査は「コンテンツ品質を守る監視人」として全体を底支えします。

---

## Phase ロードマップへの統合

[proposal-deck.md](proposal-deck.md) の Phase 1-4 ロードマップに **LLMO レーン** を並走させる：

| Phase | 既存 | + LLMO レーン |
|---|---|---|
| Phase 1 (0-3ヶ月) | 在庫モニター + 異常検知（Sense） | **LLMO Check API 運用開始**（既存ブログ上位3記事をリライト） |
| Phase 2 (3-6ヶ月) | + 栄養計算（Generate） | **Verbal Identity v1.1 + LLMO Check を新規記事の標準フローに統合** |
| Phase 3 (6-9ヶ月) | + 配送・通知（Reach） | **JSON-LD自動付与 / llms.txt生成 / 外部メディア寄稿パイプライン** |
| Phase 4 (9-12ヶ月) | + Run統合（オーケストレーター） | **AI引用率を経営KPIに昇格 / Brand Intelligence 統合監視** |

## ROI への寄与

[value-calculation.md](value-calculation.md) の効果領域に LLMO効果を追加：

| 追加効果領域 | 試算値 | 根拠 |
|---|---|---|
| **AI経由の認知獲得** | ¥XXX万/年 | AI流量 7-10% × CV率 × LTV |
| **検索流入の質向上** | ¥XXX万/年 | Search Console AI Overviews 流入の上昇 |
| **コンテンツ制作時間削減** | ¥XXX万/年 | LLMO Check で品質保証 → リライト戻し削減 |

※ 実数値はLLMO Check API運用開始後、定点検索 + GA4 で実測。

## Verbal Identity v1.1 への統合

[fambox-verbal-llmo-extension.md](../../30_Tech_Notes/fambox-verbal-llmo-extension.md) を **v1.0 と併用** する運用：

```
[書く]
  ↓ v1.0 ルール（トーン・NG語・Verb Bank・キーワード16語）
[ドラフト]
  ↓ v1.1 ルール（結論先行・質問形・具体性・チャンク完結）
[LPB v4 LLMO Check]
  ↓ 8項目自動監査 → スコア ≥ 75 で合格
[公開]
  ↓ AI定点検索で計測（月次）
[Run 学習]
  ↓ プレーブック更新（v1.2 候補ルール抽出）
```

## 「AIに載せられる」FAMBOXのキーメッセージ案

LLMO観点でブランドメッセージを再起草する候補：

| 場面 | 旧（v1.0） | 新（v1.1 LLMO準拠） |
|---|---|---|
| トップH1 | 「次の一歩に、燃料を」 | 「**スポーツ栄養を、3食×7日で完結させる**」 |
| サービス紹介 | 「私たちの想い」 | 「**FAMBOXとは何か**」 |
| アスリート向け | 「あなたを、次のステージへ」 | 「**アスリートに必要な栄養設計とは**」 |

→ 元のメッセージピラー（Fuel your next step / Carry You Further）は **キャッチコピー** として保持し、**SEO/LLMO見出しは別途に質問・定義型** で書く運用に。

## 守屋選手企画への直接応用

[moritani-ambassador](../moritani-ambassador/overview.md) の **インタビュー記事** が最初の LLMO 完全準拠コンテンツになる候補：

| 記事構成 | LLMO 仕様 |
|---|---|
| タイトル | 「**ラグビー選手・守屋圭佑が語る、アスリートの食事戦略**」（具体性 + 定義型） |
| H2 #1 | 「**なぜ食事への投資が競技成績を左右するのか**」（質問形） |
| H2 #2 | 「**ラグビー選手のPFCバランスは何が違うのか**」（質問形） |
| H2 #3 | 「**FAMBOX を半年継続して何が変わったか**」（質問形） |
| 各H2 冒頭 | 1-2文の結論先行（200字以内） |
| 著者 | 守屋選手 + 監修者を JSON-LD で記載 |
| 出典 | ラグビー栄養ガイドライン等を一次ソースリンク |

→ Phase 1 着手と同時に、**Phase 1 の Sense層（在庫）+ LLMO レーン（コンテンツ）+ 守屋企画（実コンテンツ）** が並走する設計。

## 議論したい点（提案当日）

1. **6番目エージェント（LLMO監査）の追加**に合意できるか
2. **既存ブログ3記事のリライト** を Phase 1 と並行して着手することの合意
3. **AI引用率の経営KPI化** を Phase 4 までに目指すかの方針

## 関連
- [proposal-deck.md (v2)](proposal-deck.md) — 本提案のメインデッキ
- [executive-summary.md](executive-summary.md) — 1ページサマリ（LLMO追記候補）
- [flywheel-mapping.md](flywheel-mapping.md) — Experience Flywheel詳細
- [baigie-llmo-aio-guide](../../30_Tech_Notes/baigie-llmo-aio-guide-2026-05.md) — 元思想
- [fambox-verbal-llmo-extension](../../30_Tech_Notes/fambox-verbal-llmo-extension.md) — v1.1 ルール
- [llmo-article-rewrite-checklist](../../30_Tech_Notes/llmo-article-rewrite-checklist.md) — リライト手順
- [LPB LLMO Check 実装](../../../tools/liquid-pipeline/server/routes/llmo-check.ts) — 8項目自動監査
