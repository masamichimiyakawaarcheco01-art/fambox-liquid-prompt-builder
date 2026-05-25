---
title: "ベイジ枌谷 — LLMO/AIO 入門ガイド（ウェブを作る人のための 2026年5月版）"
date: 2026-05-21
source: https://baigie.me/officialblog/2026/05/20/llmo/
type: article-summary
author: 枌谷力（ベイジ代表取締役）
date_posted: 2026-05-20
publisher: ベイジの図書館
tags: [llmo, aio, seo, content-strategy, ai-citation, e-e-a-t, structured-data, json-ld, llms-txt, fambox-applicable]
topics: [ai, content, seo, marketing, brand-intelligence]
status: reviewed
priority: high
related:
  - obara-ai-agent-era-ep2.md
  - chesky-airbnb-ai-era-redesign.md
  - whitespace-experiments-animations.md
  - design-acceptance-parameters.md
  - ../../docs/okr/FAMBOX_Verbal_Guideline_v1.0.md
---

# ベイジ枌谷 — LLMO/AIO 入門ガイド（2026年5月版）

## 主な主張（コア結論）

> **LLMO は技術施策ではない。実態を伴うビジネス活動があってはじめて成立する戦略的取り組み。**
>
> 生成AIが情報の入口になりつつある今、**自社情報がAIに正しく載り、引用されるよう** に最適化する。
> SEOの土台の上に、**チャンク完結 / 質問形見出し / E-E-A-T明示 / 構造化データ / llms.txt** などの追加層を重ねる。

## 衝撃の数字

| 指標 | 値 |
|---|---|
| AI関連ボットが占めるHTMLリクエスト | **4.2%**（Cloudflareデータ） |
| Google混合で予想される合計 | **7〜10%** |
| 推奨チャンクサイズ | **200-500トークン / 400-800字** |
| 結論先行の文字数 | **200字以内** |
| 「導入企業340社」など固有値の効果 | 抽象表現と比べてAI引用率が格段に上がる |

---

## LLMO とは何か

| 観点 | SEO | **LLMO** |
|---|---|---|
| ゴール | 検索結果表示 → サイト訪問 | **AI回答内への情報引用 → 認知** |
| 位置づけ | 独立した施策 | **SEOの土台 + 追加層** |
| 対象 | Google中心 | ChatGPT / Claude / Perplexity 等 |
| 引用元表示 | 必須 | **不確定**（AIによって異なる） |
| 計測 | クリック・順位 | **AI回答プロンプトでの言及確認** |

**共通点**: E-E-A-T、構造化データ、技術的健全性などの基礎は同じ。

---

## 実装手法 — 3階層 × 10施策

### STEP 1: コンテンツ層

1. **結論先行型** — 見出し配下の最初1-2文に結論。チャンク化されても意味が保持される設計
2. **質問形見出し** — 「私たちの想い」より「採用ブランディングとは何か」。ユーザープロンプトとベクトル距離を縮める
3. **具体性の徹底** — 「多くの企業が」→「**導入企業340社**」など固有値・数値・一次情報

### STEP 2: 技術層

4. **セマンティックHTML** — `article` / `section` / `h1-h6` の正しい階層使用
5. **JSON-LD構造化データ** — Organization / Article / Person schema、特に `sameAs` でエンティティ統合
6. **robots.txt 個別制御** — 学習bot / 検索bot / 直接アクセスbot を役割別に Disallow / Allow

### STEP 3: インデックス層 + 外部信頼層

7. **llms.txt 配置** — サイトルートに Markdown形式でサイト概要・主要セクション・リンク
8. **SSR/SSG実装** — 初期HTMLに本文を含め、JavaScript遅延描画に依存しない
9. **プレスリリース・メディア露出** — 複数ドメインへの転載、具体数値・事実の記載、頻度確保
10. **Wikipedia / Wikidata 登録** — 第三者言及の最高権威ソースとしてのエンティティ定義

---

## AIに引用されやすいコンテンツの3原則

### 原則1: チャンク完結

- 見出し配下1チャンク（**200-500トークン**）が、前後文脈なしで自立的に意味を持つ
- **「上記の通り」「先述したように」などの依存表現を排除**
- 400-800字目安、**結論200字以内**

### 原則2: E-E-A-T明示

- 著者名・肩書き・専門領域を **バイラインと JSON-LD で二重記載**
- 公開日・更新日の両方表示
- **出典リンク明記**（「ある調査によれば」は禁止）

### 原則3: ベクトル明確化

- 単語は **具体的・専門的**（抽象的配置を避ける）
- 固有名詞・数値・一次データで特定領域に位置づけ
- **複数テーマ混在は避ける**

---

## 計測・KPI（4段階の成果指標）

| Level | 指標 | 計測方法 |
|---|---|---|
| 1 | AIに引用される | **週次の定点プロンプト検証**（「FAMBOXについて教えて」を複数AIで実施） |
| 2 | 企業が認知される | AI回答での名前出現頻度 |
| 3 | 好意的印象を持たれる | AI回答の文脈分析 |
| 4 | 問い合わせ/購買等の実ビジネス転換 | GA4 AIチャネル流入 + 問合せフォーム「生成AIで知った」選択数 |

**課題**: AIは引用元URLを必ず表示しない、同じ質問でも回答が毎回変わる → **完全計測不可能**

---

## 重要な caveat — Google 公式発表（2026年5月）

> **llms.txt 不要、作為的言及は逆効果、ユーザーファースト優先**

→ **「LLMOテクニックに走りすぎず、本質的なコンテンツ価値を高めることが最優先」** という方針。
→ チェスキー動画「**素晴らしいものを創ること自体を目的に**」と通底する思想。

---

## ARCHECO/FAMBOXでの応用案

### A. テキスト側の「ブランド・インテリジェンス」

[尾原Ep2](obara-ai-agent-era-ep2.md) の **Brand Intelligence**（AI が学習する暗黙知）の **テキスト側の実装** として LLMO が位置付けられる：

| Adobe Brand Intelligence | LLMO |
|---|---|
| 修正履歴からブランドプレーブック自動構築 | **構造化データ + チャンク設計で AI に正しく載る** |
| 視覚一貫性の維持 | **テキスト一貫性の維持** |
| 内部システム最適化 | **外部AIへの引用最適化** |

→ FAMBOX のブランド・インテリジェンスは **「視覚 + 動き + テキスト + 構造」** の4層になる。

### B. FAMBOX Verbal Identity Guideline v1.0 への追加候補

[Verbal Identity Guideline](../../docs/okr/FAMBOX_Verbal_Guideline_v1.0.md) は **トーン・NG語・キーワード** までは確立済。LLMO 観点で追加すべき項目：

- **結論先行型** の徹底（見出し配下の最初1-2文）
- **質問形見出し** の優先（「FAMBOXとは何か」「アスリートに必要な栄養とは」等）
- **具体性ルール**（「多くの」「いくつかの」を禁止、必ず数値）
- **チャンク完結** — 「上記の通り」「先述」等を禁止用語に追加
- **出典明記** — 「ある研究では」を禁止、必ず一次ソースリンク

### C. FAMBOX サイトの即実装施策（10件・優先度順）

| 優先度 | 施策 | 担当 | 工数 | 効果 |
|---|---|---|---|---|
| **1** | トップページに Organization schema + sameAs | エンジニア | 1h | 中 |
| **2** | 商品ページに Product schema（栄養成分・価格・評価） | Liquid開発者 | 半日 | **高** |
| **3** | ブログ記事を「結論先行型」リライト | ライター + 編集 | 1日/記事 | **高** |
| **4** | 著者バイライン明確化（栄養士の顔写真 + 経歴 + JSON-LD） | デザイン + 編集 | 半日 | 中 |
| **5** | llms.txt 配置（サービス概要 / 購入フロー / ブログリンク） | エンジニア | 1h | 低（Google 不要発表だが ChatGPT 系は読む可能性あり） |
| **6** | robots.txt 確認（AI検索bot は許可、学習は経営判断） | エンジニア | 30min | 中 |
| **7** | 栄養士ブログを外部メディアに寄稿化（月1回） | 広報 + ライター | 継続 | **高** |
| **8** | 問い合わせフォーム「生成AIで知った」選択肢追加 | マーケ計測 | 1h | 中 |
| **9** | 月1回 AI定点検索（「冷凍食定期配送おすすめ」等で FAMBOX 言及確認） | マーケ | 1h/月 | 低 |
| **10** | Google Business Profile + Merchant Center 整備（BtoC有利） | マーケ | 1日 | 中 |

**最短実装ルート（1週間）**: ①③④⑥ を同時並行 → ③のリライト完了時点で効果測定開始

### D. 守屋選手企画への応用

[守屋選手アンバサダー企画](../20_Projects/moritani-ambassador/overview.md) のコンテンツ作りに直接統合：

- **インタビュー記事の構造**:
  - 見出し: 「アスリートの土台は食である理由」（質問形）
  - 冒頭1-2文: 結論先行 — 「守屋選手は20年の競技人生で食事への投資が成績を左右したと語る」
  - チャンク完結 — 各セクションが独立して引用可能
  - E-E-A-T明示: 守屋選手の経歴 + 栄養士監修者の経歴を JSON-LD

- **SNS 切り出しでも LLMO 整合**: 短文でも結論先行・具体性を保つ

### E. LPB v4 への組み込み

[Liquid Pipeline](lpb-human-on-the-loop-roadmap.md) のチェック項目に LLMO 観点を追加：

| Phase | LLMO チェック項目 |
|---|---|
| 40% 生成 | **見出しが質問形か** / 結論が先頭にあるか |
| 70% 調整 | **チャンク完結性**（前後文脈依存表現がないか） |
| 100% 仕上げ | **JSON-LD 出力** / セマンティックHTML / E-E-A-T情報 |
| 120% 超越 | プレスリリース連携 / 外部メディア寄稿候補生成 |

### F. デザイン承認パラメータへの追加候補

[design-acceptance-parameters.md](design-acceptance-parameters.md) に **LLMO項目** を新設：

| 項目 | 合格基準 |
|---|---|
| 見出しが質問形 | 必須（「私たちの想い」型を禁止） |
| 結論先行 | 見出し配下の最初1-2文 |
| チャンク完結 | 「上記の通り」「先述」等の依存表現ゼロ |
| 著者情報の JSON-LD | 主要記事・商品ページ全てで必須 |
| Organization schema | サイトトップで必須・sameAs 設定 |
| 具体性 | 「多くの」「いくつかの」を禁止、必ず数値 |
| SSR/SSG | クライアントサイド遅延描画は最小限 |

---

## 残タスク（更新）

### 即決可能
- [ ] FAMBOX サイトトップに Organization schema 追加（1h、効果中）
- [ ] [Verbal Identity Guideline v1.0](../../docs/okr/FAMBOX_Verbal_Guideline_v1.0.md) に LLMO項目（チャンク完結・質問形見出し・具体性）を追記
- [ ] llms.txt 配置（Google「不要」だが他AIには有効）
- [ ] 既存ブログ記事の上位3件を「結論先行型」にリライト

### FAMBOX定例で議論
- [ ] 商品ページの Product schema 化（栄養成分・価格・評価データの確定）
- [ ] 栄養士ブログの外部メディア寄稿戦略
- [ ] 問い合わせフォームに「生成AIで知った」選択肢追加

### Liquid Pipeline 統合
- [ ] LPB v4 の Phase 100% チェックに LLMO項目追加
- [ ] [design-acceptance-parameters.md](design-acceptance-parameters.md) に LLMO セクション追加

### 効果測定の仕組み
- [ ] 週次AI定点検索のルーチン化（ChatGPT / Claude / Perplexity の3経路）
- [ ] GA4 で AIチャネル流入の比率トラッキング設定

---

## ベイジ枌谷の重要な引用

> 「LLMO は技術施策ではない。**実態を伴うビジネス活動があってはじめて成立する**」

> 「テクニックに走りすぎず、**本質的なコンテンツ価値を高めることが最優先**」（Google公式発表 2026年5月）

→ FAMBOXの場合、これは **「アスリートの土台は食である」という本質的な主張を、AI が正しく載せられる構造で語る**ことを意味する。

---

## 他のAI戦略系ノートとの位置づけ

| ノート | 主軸 | テーマ |
|---|---|---|
| [尾原Ep1](obara-ai-agent-era-ep1.md) | システム | System of Action / Human-on-the-Loop |
| [尾原Ep2](obara-ai-agent-era-ep2.md) | ブランド | Brand Intelligence / Human-in-the-Lead |
| [Chesky](chesky-airbnb-ai-era-redesign.md) | 組織 | プロジェクト・ハワイ / 11つ星体験 |
| [Vibe Coding](vibe-coding-six-principles.md) | 規律 | 本番投入前の6原則 |
| [Whitespace](whitespace-experiments-animations.md) | 視覚 | アニメーション言語 |
| **本ノート（LLMO）** | **テキスト・引用** | **AI が読み・引用する設計** |

→ AI戦略の **6層** が揃った：システム / ブランド / 組織 / 規律 / 視覚 / テキスト

---

## 元情報
- URL: https://baigie.me/officialblog/2026/05/20/llmo/
- タイトル: ウェブを作る人のためのLLMO/AIO入門【2026年5月版】
- 著者: 枌谷力（ベイジ代表取締役）
- 公開日: 2026-05-20
- 媒体: ベイジの図書館（株式会社ベイジ）

## 関連
- [[obara-ai-agent-era-ep2.md]] — Brand Intelligence の元思想
- [[whitespace-experiments-animations.md]] — 視覚側の言語
- [[design-acceptance-parameters.md]] — LLMO項目追加候補
- [[lpb-human-on-the-loop-roadmap.md]] — LPB へのLLMO組み込み
- [[../../docs/okr/FAMBOX_Verbal_Guideline_v1.0.md]] — Verbal Identity 拡張候補
- [[../20_Projects/moritani-ambassador/overview.md]] — 守屋企画への直接応用
- [[../20_Projects/fambox-multi-agent-proposal/overview.md]] — マルチエージェント提案の補強要素
- [[../../brand/fambox/animation-library-v0.1.md]] — 視覚 + 動き + テキスト の統合構造の一部
