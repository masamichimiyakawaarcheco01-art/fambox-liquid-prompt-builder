# FAMBOX — Project CLAUDE.md

> **目的**：FAMBOX に関する **すべての判断基準** を1ファイルに集約する。
> 非デザイナーが Step 2 で参加する時、最初に読む単一ファイル。
> Marc-Antoine Lecat（Archeco kit v7.34 / `projects/_TEMPLATE/CLAUDE.md`）のパターンを採用。

**ファイル位置：** `brand/fambox/CLAUDE.md`
**初稿：** v0.1（2026-05-28）
**完成目標：** v1.0（Step 2 開始前 / 2026-09 想定）
**参照：** [DECISIONS.md D-024](../../docs/okr/fambox-flywheel/DECISIONS.md)

---

## このファイルの読み方

このファイルを **最初に読んでから** 作業に入る：

```
1. Identity を読む（このブランドは何か）
   ↓
2. Surface を読む（今回作るものはどの surface か）
   ↓
3. Hard Rules を読む（絶対に守るルール）
   ↓
4. AI/Human Boundary を読む（誰がどこまで担当するか）
   ↓
5. 作業開始
```

詰まったら：
- 細かいルール → [bugs.md](design-system/bugs.md)
- ブランドの感性 → [brand-dna/current.md](brand-dna/current.md)
- 過去の決定 → [DECISIONS.md](../../docs/okr/fambox-flywheel/DECISIONS.md)

---

## 1. Identity（このブランドは何か）

**FAMBOX** は、アスリート・スポーツチーム・健康経営に取り組む法人向けの食事サブスクリプションサービス。

**Brand DNA**（[詳細](brand-dna/current.md)）：
- **Editorial × Lab**：丁寧に編集された情報の信頼感（Editorial） × 科学的な検証・実験性（Lab）
- **人格**：プロフェッショナルで穏やか、押し付けず、結果で語る
- **戦略**：B2B 中心、健康経営トレンドに対する確かな選択肢

**Verbal Identity v1.0**（[詳細](../../docs/okr/FAMBOX_Verbal_Guideline_v1.0.md)）：
- トーン：誠実、根拠ベース、押し売りしない
- NG ワード：「最強」「No.1」など根拠不明な superlative
- 推奨：データ・実例・第三者の声で語る

---

## 2. Surfaces（このブランドが展開する出力面）

> 各 surface には固有の制約と AI/Human boundary がある。

| Surface | 出力フォーマット | 主な担当 |
|---|---|---|
| **Shopify Liquid セクション** | .liquid（LP / 商品ページ）| 宮川（Step 1）→ 松浦・宮川共作（Step 2）|
| **法人ページ（LP）** | Shopify セクション組合せ | 松浦・宮川 共作 |
| **メール HTML（Seal）** | Klaviyo / Seal templates | 宮川 |
| **Instagram フィード画像** | 1:1 PNG（Canva） | マレル（Step 3 から AI 統合）|
| **Instagram リール / TikTok** | 9:16 動画 | マレル（Step 3 から AI 統合）|
| **YouTube サムネ** | 16:9 PNG | マレル |
| **法人向けバナー / CTA** | 配信先別サイズ | 松浦・宮川 共作 |
| **印刷物（チラシ・パンフ）** | PDF | 宮川（外注の場合あり）|
| **提案書 / 社内資料** | PPTX | 須齋・松浦 |

**長期：** Marc の v7.34 の Surface 概念（6 surfaces formalized as production modes）を採用予定（[DECISIONS.md D-024](../../docs/okr/fambox-flywheel/DECISIONS.md) Tier 2）

---

## 3. Hard Rules（絶対に守るルール）

> このセクションの内容は **bugs.md の DOCTRINE カテゴリから抽出**したもの。
> 違反すると出荷不能。

### ブランド系

- **タイポグラフィ**：Poppins（英字）+ Hiragino Kaku Gothic Pro（和字）固定。Archivo・Space Grotesk・Manrope 等の重いスポーツ系 Display NG（[feedback_fam_typography](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_fam_typography.md)）
- **ビジュアル技法**：輪郭歪み・noise-bloom・グリッチ等の派手な FX 禁止（[feedback_fambox_visual_effects](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_fambox_visual_effects.md)）
- **DS v0.5 のトークンを使う**：未定義のカスタム値を勝手に追加しない

### コピー系

- **「最強」「No.1」「業界 No.1」等の superlative 禁止**（根拠ベース原則）
- **押し売り表現 NG**：「今すぐ」「お見逃しなく」等の煽り NG
- **B2B 法人向けの落ち着いたトーン**を維持

### Liquid / 実装系

- **schema-lint 違反コミット禁止**（pre-commit / GitHub Actions でブロック済）
- **inline style より外部 CSS**（[feedback_shopify_liquid_specificity](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_liquid_specificity.md)）
- **画像は `image_url width: 1200` 以上**（Retina 対応）
- **z-index は `::before` / `::after` 疑似要素で処理**
- **ファイル全体を出力**（部分スニペット禁止、[feedback_file_verification](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_file_verification.md)）

### プロセス系

- **同じ修正が3回失敗 → 対処療法停止、根本原因特定**（[feedback_implementation_discipline](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_implementation_discipline.md)）
- **ファイル生成後は grep / curl / DevTools の3段階検証**
- **「保存しました」だけの報告禁止、証拠付きで報告**

---

## 4. AI/Human Boundary（D-021 のカテゴリ別）

> パーセンテージ（70/30）ではなく、**作業カテゴリ** で定義（D-021）。

### 4.1 Surface 共通

| カテゴリ | 主体 | 具体例 |
|---|---|---|
| **AI proposes（提案）** | AI | 構造、レイアウト、ブランド準拠、初稿コピー、CTA バリエーション、コード |
| **Human validates（承認）** | 人間 | bugs.md 規律通過、ブランド整合性、出荷判定 |
| **Human adjusts（微調整）** | 人間 | コピーの魂、画像最終選定、案件固有事情の反映 |
| **Human decides（決定）** | 人間 | 複数案からの選択、戦略判断、出荷可否 |

### 4.2 Surface 別の boundary

| Surface | AI proposes | Human validates | Human adjusts | Human decides |
|---|---|---|---|---|
| Shopify セクション | レイアウト・構造・ベース Liquid・コピー初稿 | bugs.md 通過 / DS v0.5 準拠 / lint 通過 | コピー仕上げ / 画像差替 | 公開判断 |
| メール HTML | レイアウト・コピー初稿・件名候補 | bugs.md 通過 / レンダリング検証 | コピー仕上げ / プレヘッダ | 配信判断 |
| Instagram 画像 | レイアウト・コピー初稿 | ブランド整合性 / 色使い | コピー仕上げ / 画像選定 | 投稿判断 |
| 法人 CTA | バリエーション3案 | ブランド整合性 | 主訴求の最終調整 | 採用案決定 |

### 4.3 「declining = re-declaring」（Marc の v7.33 原則）

非デザイナーがこの boundary を **明示的に宣言する** ことが運用の根幹。
宣言を拒否する場合は、別の boundary を宣言し直す必要がある。「曖昧なまま進める」は禁止。

---

## 5. Vocabulary（重要用語）

| 用語 | 意味 |
|---|---|
| **Editorial × Lab** | FAMBOX の二軸メタファー（信頼感 × 検証性）|
| **Middle & Fast** | 宮川さんの目指すポジショニング（[DECISIONS.md D-017](../../docs/okr/fambox-flywheel/DECISIONS.md)）|
| **7 割 / 3 割** → **AI proposes / Human validates / adjusts / decides** | D-021 で再定義 |
| **Step 1 / 2 / 3** | 須藤さん 3段階モデル（[DECISIONS.md D-010](../../docs/okr/fambox-flywheel/DECISIONS.md)）|
| **指示書 / 持ってこい資料** | Step 2 で依頼者が書く Standard 形式の brief（[D-018](../../docs/okr/fambox-flywheel/DECISIONS.md)）|
| **bugs.md / バグログ** | 失敗の記録 + ルールへの変換ログ（FAMBOX 品質の中核、Marc 検証済）|
| **Learn 層** | bugs.md 更新 + feedback 蓄積による学習機構（D-022）|
| **Surface** | 出力面の分類（Shopify / Email / Instagram 等、Marc v7.34 ベース）|
| **Hard Rules / Doctrine** | 違反不可の規律（bugs.md DOCTRINE カテゴリ）|

---

## 6. Exclusions（絶対にやらないこと）

> bugs.md の BUG カテゴリから抽出。「過去に踏んだ罠」。

- **richtext の `<p>` ネスト前提のスタイル**（[feedback_shopify_liquid_specificity](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_liquid_specificity.md)）
- **schema validator が弾く5パターン**（[feedback_shopify_schema_validator](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_schema_validator.md)）
- **Liquid `for i in (1..N)` のCSSクラス名 ゼロパディング不整合**（[feedback_shopify_liquid_loop_class_mismatch](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_liquid_loop_class_mismatch.md)）
- **テンプレート命名衝突**（[feedback_shopify_template_naming_conflict](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_template_naming_conflict.md)）
- **プレビューだけで「公開済」と判断**（必ず curl で本番 URL 検証）
- **視覚デザインを文字情報だけで進める**（動画・スクショ先行）
- **Figma で listAvailableFontsAsync を確認せず text 操作**
- **git add でディレクトリ指定（untracked 混入リスク）**
- **Tokens 名を grep 実在検証せずに spec 化**

詳細は [bugs.md](design-system/bugs.md) を参照。

---

## 7. Learn Loop（学習機構）

> Step 1 から必須の最小機構（D-022）。

- **失敗発生時**：bugs.md に候補エントリ追加
- **2回目の同じ修正**：bugs.md に即ルール化（Marc の M2 原則）
- **月1回**：bugs.md 追加件数を可視化（停滞検知）
- **金曜事業開発**：「今週の Learn 進捗」を恒久発表項目

---

## 8. Decision Log Pointer

すべての構造的決定は `docs/okr/fambox-flywheel/DECISIONS.md` を参照。
D-001 〜 D-025 に番号付きで管理。新しい決定は連番追加で。

直近の重要決定：
- D-021: AI/Human のカテゴリベース定義
- D-022: Learn 層を Step 1 から保護
- D-023: DNA Evolution Triggers
- D-024: この CLAUDE.md パターン採用
- D-025: Marc コラボ受諾

---

## 9. このファイルの維持

- **Owner**：宮川
- **Reviewer**：Marc-Antoine（peer review）、須齋（事業視点）、松浦（実運用視点）
- **更新頻度**：DECISIONS.md に新規 D-NNN 追加時、影響あれば更新
- **バージョニング**：v0.1（初稿）→ v0.X（運用しながら拡張）→ v1.0（Step 2 開始前）

---

## バージョン履歴

| 版 | 日付 | 内容 |
|---|---|---|
| v0.1 | 2026-05-28 | 初稿。Marc の v7.34 `_TEMPLATE/CLAUDE.md` パターンを採用し FAMBOX 用に整備。D-024 に基づく |
