# FAMBOX — Project CLAUDE.md

> **目的**：FAMBOX に関する **すべての判断基準** を1ファイルに集約。
> 非デザイナーが Step 2 で参加する時、最初に読む単一ファイル。
> Marc-Antoine Lecat（Archeco kit v7.34 / `projects/_TEMPLATE/CLAUDE.md`）のパターンを採用、FAMBOX 用に進化。

**ファイル位置：** `brand/fambox/CLAUDE.md`
**バージョン：** v0.2（2026-05-28）
**完成目標：** v1.0（Step 2 開始前 / 2026-09 想定）
**参照：** [DECISIONS.md D-024](../../docs/okr/fambox-flywheel/DECISIONS.md)

---

## 🚀 5分で全体像を掴む（Quick Orientation）

> 時間がない人はここだけ読めば「次に何を読むか」が分かる。

### このファイルが答える3つの問い

| 問い | どこを読む |
|---|---|
| **何を作るのか？** | §1 Identity → §2 Surfaces |
| **どこまでやるのか？守るルールは？** | §3 Hard Rules → §6 Exclusions |
| **誰が何を担当するのか？** | §4 AI/Human Boundary |

### 30秒サマリ

- **FAMBOX** はアスリート / 健康経営に取り組む法人向けの食事サブスク
- 視覚言語は **Editorial × Lab**（信頼感 × 検証性）
- AI が 70% を提案、人間が承認・微調整・決定する
- **bugs.md** が品質の中核（過去に踏んだ罠 28規律）
- 違反コミットは pre-commit で自動ブロック

### 「今すぐ作業に入る」5ステップ

```
1. このファイル §1〜§4 をざっと読む（5分）
2. §2 Surfaces で「今回作るもの」を見つける
3. §3 Hard Rules を必ず通す
4. §4 AI/Human Boundary で自分の役割を確認
5. 作業開始。詰まったら §11 テンプレ集を参照
```

---

## このファイルの読み方

```
1. Identity（何のブランドか）
   ↓
2. Surface（今回作るものはどれか）
   ↓
3. Hard Rules（絶対守るルール）
   ↓
4. AI/Human Boundary（誰が何を担当するか）
   ↓
5〜11. 必要時に参照
```

詰まったら：
- 細かいルール → [bugs.md](design-system/bugs.md)
- ブランドの感性 → [brand-dna/current.md](brand-dna/current.md)
- 過去の決定 → [DECISIONS.md](../../docs/okr/fambox-flywheel/DECISIONS.md)

---

## 1. Identity（このブランドは何か）

**FAMBOX** は、アスリート・スポーツチーム・健康経営に取り組む法人向けの食事サブスクリプションサービス。

**Brand DNA**（[詳細](brand-dna/current.md)）：
- **Editorial × Lab**：丁寧に編集された情報の信頼感（Editorial）× 科学的な検証・実験性（Lab）
- **人格**：プロフェッショナルで穏やか、押し付けず、結果で語る
- **戦略**：B2B 中心、健康経営トレンドに対する確かな選択肢

**Verbal Identity v1.0**（[詳細](../../docs/okr/FAMBOX_Verbal_Guideline_v1.0.md)）：
- トーン：誠実、根拠ベース、押し売りしない
- NG ワード：「最強」「No.1」など根拠不明な superlative
- 推奨：データ・実例・第三者の声で語る

### Identity の「らしさ」見分け方

| FAMBOX らしい | FAMBOX らしくない |
|---|---|
| 「TOYOTA RED CRUISERS の選手7名が継続利用」 | 「アスリート絶賛！」 |
| 「アドバイザー大前恵氏（管理栄養士）監修」 | 「業界最高峰の栄養士が監修！」 |
| 落ち着いた白背景 + Drive Orange アクセント | ネオン色 + グラデーション全開 |
| 「食事改善で組織パフォーマンス向上を支援」 | 「最強の栄養で勝つ！」 |

---

## 2. Surfaces（このブランドが展開する出力面）

> 各 surface には固有の制約と AI/Human boundary がある。

| Surface | 出力フォーマット | 主な担当 | 詳細 |
|---|---|---|---|
| **Shopify Liquid セクション** | .liquid（LP / 商品ページ）| 宮川（Step 1）→ 松浦・宮川共作（Step 2）| §2.1 |
| **法人ページ（LP）** | Shopify セクション組合せ | 松浦・宮川 共作 | §2.2 |
| **メール HTML（Seal）** | Klaviyo / Seal templates | 宮川 | §2.3 |
| **Instagram フィード画像** | 1:1 PNG（Canva） | マレル（Step 3 から AI 統合）| §2.4 |
| **Instagram リール / TikTok** | 9:16 動画 | マレル（Step 3 から AI 統合）| - |
| **YouTube サムネ** | 16:9 PNG | マレル | - |
| **法人向けバナー / CTA** | 配信先別サイズ | 松浦・宮川 共作 | §2.5 |
| **印刷物（チラシ・パンフ）** | PDF | 宮川（外注の場合あり）| - |
| **提案書 / 社内資料** | PPTX | 須齋・松浦 | §2.6 |

**長期：** Marc の v7.34 の Surface 概念（6 surfaces formalized as production modes）を採用予定（[DECISIONS.md D-024](../../docs/okr/fambox-flywheel/DECISIONS.md) Tier 2）

### 2.1 Shopify Liquid セクション — 典型ワークフロー

```
1. 要件聴取（or 既存セクションのコピー指示）
   ↓
2. Figma デザインがあれば get_design_context() で取り込み
   ↓
3. LPB v4.1 で構造化プロンプト生成
   ↓
4. Claude Code で Liquid 生成
   ↓
5. ローカル grep で 5罠チェック
   (inline style / richtext <p> / CDN cache / theme 違い / browser cache)
   ↓
6. schema-lint.py で事前検証
   ↓
7. Shopify CLI で dev theme へ push
   ↓
8. curl で本番 HTML 検証
   ↓
9. DevTools Computed で 3段階目視確認
   ↓
10. live push（必要に応じて）
```

**典型時間：** Step 1 個人インフラ確立後 = 1 セクション 2〜4時間（Before：1〜2日）

### 2.2 法人ページ（LP）— 典型ワークフロー

```
1. 松浦さんと要件すり合わせ（目的・ターゲット・ジャーニー）
   ↓
2. 既存の /pages/tokusetsu-jisseki 等を参考に構造設計
   ↓
3. セクション単位で 2.1 のフローを N回繰り返す
   ↓
4. 全体での流れ・トーンの一貫性チェック
   ↓
5. 松浦さんに最終レビュー依頼
   ↓
6. 公開判断（松浦 × 宮川）
```

### 2.3 メール HTML（Seal / Klaviyo）— 典型ワークフロー

```
1. メールタイプ確定（注文確認 / キャンペーン / ニュースレター 等）
   ↓
2. 既存 12種ワイヤフレーム（Seal）から最近いものを選定
   ↓
3. 件名 3案 + プレヘッダ 1案を準備
   ↓
4. HTML 生成（Yahoo Mail / Gmail / iOS Mail 対応）
   ↓
5. 主要クライアントでレンダリングテスト
   ↓
6. A/B テスト設計（件名 or CTA バリエーション）
   ↓
7. Klaviyo / Seal へ配信設定
```

### 2.4 Instagram フィード画像 — 典型ワークフロー（マレル運用 / Step 3 対象）

```
1. 投稿テーマ確定（マレル企画）
   ↓
2. Canva FAMBOX ブランドキットから派生
   ↓
3. 1:1（フィード）or 4:5（縦長）テンプレ選定
   ↓
4. テキスト・画像差替
   ↓
5. ブランドチェック（色 / フォント / トーン）
   ↓
6. 投稿スケジュール
```

**Step 3 で目指す姿：** AI が初稿 → マレルが3割を手詰め → 即投稿

### 2.5 法人向けバナー / CTA — 典型ワークフロー

```
1. 配信先・サイズ確認（バナー広告 / LP 内 CTA / メール内 ボタン 等）
   ↓
2. 主訴求 1行 + サブ訴求（必要なら）+ アクション動詞 CTA
   ↓
3. デザイン生成（テンプレ or 新規）
   ↓
4. A/B 案を 2〜3 用意（コピー違い / 色違い / 配置違い）
   ↓
5. 効果測定設計（CTR / CVR）
   ↓
6. 配信 → 結果を bugs.md / feedback に反映（Learn 層）
```

### 2.6 提案書 / 社内資料 — 典型ワークフロー

```
1. 用途確定（社外向け提案書 / 社内共有 / 投資家向け 等）
   ↓
2. pptx-generator skill で FAMBOX ブランドの PPTX 生成
   ↓
3. Yu Gothic UI 固定（feedback_document_font 規律）
   ↓
4. 白背景 + Drive Orange アクセント基調
   ↓
5. 内容微調整 → 配布
```

---

## 3. Hard Rules（絶対に守るルール）

> このセクションは **bugs.md の DOCTRINE カテゴリから抽出**。違反すると出荷不能。
> 各ルールは **「ルール + 反例」のペアリング**（Marc 流）で記述。

### 3.1 ブランド系

| ルール | 反例（NG） |
|---|---|
| **タイポ：Poppins（英）+ Hiragino Kaku Gothic Pro（和）固定** | Archivo / Space Grotesk / Manrope 等の重いスポーツ系 Display |
| **DS v0.5 のトークン値を使う** | 「ブランドカラーに似てるから」とカスタム HEX を直書き |
| **派手な FX 禁止**（[feedback_fambox_visual_effects](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_fambox_visual_effects.md)）| 輪郭歪み / noise-bloom / グリッチ / 過剰グラデ |

### 3.2 コピー系

| ルール | 反例（NG） |
|---|---|
| **根拠ベース表現** | 「最強」「No.1」「業界 No.1」等の superlative |
| **誠実な勧誘** | 「今すぐ」「お見逃しなく」「限定」等の煽り |
| **B2B 法人向けの落ち着いたトーン** | スポ根・体育会系の押しの強さ |
| **数値で語る**（13チーム / アドバイザー大前恵氏 等） | 「すごい結果」「驚異的な改善」等の形容詞ベース |

### 3.3 Liquid / 実装系

| ルール | 反例（NG） |
|---|---|
| **schema-lint 違反コミット禁止**（pre-commit / GitHub Actions でブロック） | color/url default に var() を入れる、text default が空文字 |
| **inline style より外部 CSS**（[詳細](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_liquid_specificity.md)）| Liquid 内で `style="..."` を多用、後で外部 CSS で上書きしようとしても効かない |
| **画像 `image_url width: 1200` 以上**（Retina 対応）| `image_url width: 600` で iPhone Retina でボケる |
| **z-index は ::before / ::after で**（疑似要素処理） | 通常要素に直接 z-index を当てて stacking context が壊れる |
| **ファイル全体を出力**（部分スニペット禁止）| 「ここだけ修正」とスニペット渡し → 整合性破綻 |

### 3.4 プロセス系

| ルール | 反例（NG） |
|---|---|
| **同じ修正が3回失敗 → 対処療法停止、根本原因特定**（[詳細](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_implementation_discipline.md)）| 同じバグを4回・5回 patch でつぶそうとして時間浪費 |
| **3段階検証**（ローカル grep / curl 本番 / DevTools Computed） | 「保存しました」だけで完了報告 → 本番反映漏れ |
| **証拠付き報告** | 「修正済」「動作確認済」だけで具体的な検証ログなし |

---

## 4. AI/Human Boundary（D-021 のカテゴリ別）

> パーセンテージ（70/30）ではなく、**作業カテゴリ** で定義（D-021）。
> 「declining = re-declaring」原則（Marc v7.33）：明示的に宣言する。曖昧なまま進めない。

### 4.1 Surface 共通の基本

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

### 4.3 「declining = re-declaring」原則の実例

**原則：** Boundary を変更したい時、必ず別の Boundary を「再宣言」する。「曖昧なまま進める」は禁止。

#### 実例 A：Instagram 画像で「コピー初稿も人間が書きたい」場合

❌ **NG（曖昧な変更）：**
> 「今回は自分でコピー書きたいから AI proposes は飛ばす」 → そのまま進行

✅ **OK（再宣言）：**
> 「今回の Instagram 画像は **AI proposes をスキップ**。代わりに：
> - Human proposes：コピー（マレル本人が書く）
> - AI adjusts：FAMBOX らしさのトーン微調整
> - Human decides：投稿可否」

#### 実例 B：法人ページで「Marc にレビュー入れたい」場合

❌ **NG（曖昧な追加）：**
> 「念のため Marc に見せます」 → どの段階で何を見せるか不明

✅ **OK（再宣言）：**
> 「法人ページ HTML 制作で、**Human validates の後に Peer validates（Marc）を追加**。
> - Marc は構造・アーキテクチャに対するレビュー
> - ブランド整合性は Human validates で完結
> - 出荷可否は依然として Human decides（宮川）」

#### 実例 C：マレルが Step 3 前に AI で投稿画像作りたい場合

❌ **NG（boundary 無視）：**
> 「Canva と AI 使えば自分で作れる」 → ブランド逸脱リスク

✅ **OK（再宣言）：**
> 「マレルが Instagram 画像を AI で作る。Step 3 前だが、暫定 boundary：
> - AI proposes：レイアウト・コピー初稿
> - Human validates：マレル自身が bugs.md 確認 + 山本さん（マレル内のデザイン担当）が二重確認
> - Human adjusts：マレル
> - Human decides：マレル + 山本さん」

**重要：** declining だけして re-declaring しないと、Step 3 未満で品質崩壊のリスク。

---

## 5. Vocabulary（重要用語）

| 用語 | 意味 |
|---|---|
| **Editorial × Lab** | FAMBOX の二軸メタファー（信頼感 × 検証性）|
| **Middle & Fast** | 宮川さんの目指すポジショニング（[DECISIONS.md D-017](../../docs/okr/fambox-flywheel/DECISIONS.md)）|
| **AI proposes / Human validates / adjusts / decides** | AI と人間の境界カテゴリ（D-021）|
| **Step 1 / 2 / 3** | 須藤さん 3段階モデル（[DECISIONS.md D-010](../../docs/okr/fambox-flywheel/DECISIONS.md)）|
| **指示書 / 持ってこい資料** | Step 2 で依頼者が書く Standard 形式の brief（[D-018](../../docs/okr/fambox-flywheel/DECISIONS.md)）|
| **bugs.md / バグログ** | 失敗の記録 + ルールへの変換ログ（FAMBOX 品質の中核、Marc 検証済）|
| **Learn 層** | bugs.md 更新 + feedback 蓄積による学習機構（D-022）|
| **Surface** | 出力面の分類（Shopify / Email / Instagram 等、Marc v7.34 ベース）|
| **Hard Rules / Doctrine** | 違反不可の規律（bugs.md DOCTRINE カテゴリ）|
| **Evolution Triggers** | DNA / Doc を次バージョンへ進める条件（D-023）|
| **declining = re-declaring** | Boundary 変更時に必ず別の Boundary を宣言する原則（Marc v7.33）|

---

## 6. Exclusions（絶対にやらないこと）

> bugs.md の BUG カテゴリから抽出。「過去に踏んだ罠」。それぞれ実例付き。

### 6.1 実装系の罠（具体例）

#### Exclusion A：richtext の `<p>` ネスト問題
- **失敗例：** Shopify schema の `richtext` setting で本文を入力。出力 HTML は `<p>本文</p>` で自動ラップされる。さらに `<p>` で包んだ CSS を書いて二重ネスト → スタイルが効かない。
- **解決：** richtext 出力を `<div class="rich">` で包んで、CSS は `.rich p` で書く。
- **参照：** [feedback_shopify_liquid_specificity](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_liquid_specificity.md)

#### Exclusion B：schema validator の 5パターン違反
- **失敗例：** `color` setting の default に `var(--color-drive)` を入れる → validator が「invalid color value」で push 拒否。
- **解決：** default は実 HEX `#FB4C15` を入れる。`var()` は section CSS 内で参照。
- **参照：** [feedback_shopify_schema_validator](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_schema_validator.md)

#### Exclusion C：Liquid `for i in (1..N)` の CSS クラス名 ゼロパディング不整合
- **失敗例：** Liquid で `.pos-{{ i | prepend: '0' }}` と書いて CSS は `.pos-1, .pos-2...` → 不一致でスタイル当たらない。
- **解決：** Liquid 出力と CSS セレクタを必ず grep で一致確認。
- **参照：** [feedback_shopify_liquid_loop_class_mismatch](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_liquid_loop_class_mismatch.md)

#### Exclusion D：テンプレート命名衝突
- **失敗例：** 新規 `page.tokusetsu-jisseki.json` を作る前に管理画面で確認せず、既存と被って上書き。
- **解決：** 新規作成前に管理画面 Templates フォルダで現状把握。日本語ローマ字（被りにくい）。
- **参照：** [feedback_shopify_template_naming_conflict](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_shopify_template_naming_conflict.md)

### 6.2 検証系の罠

#### Exclusion E：プレビューだけで「公開済」と判断
- **失敗例：** Theme Editor のプレビューで OK → 「公開しました」報告 → 実は live theme に push されておらず本番未反映。
- **解決：** 必ず `curl https://...` で本番 HTML を取得して grep 検証。

#### Exclusion F：視覚デザインを文字情報だけで進める
- **失敗例：** Hero アニメ v1〜v12 を「もっと滑らかに」「もう少しゆっくり」等の言葉だけで12回試行錯誤。
- **解決：** mp4 受領 + ffmpeg フレーム抽出で一発解決。視覚要素は最初に画面録画 or スクショ依頼。
- **参照：** [feedback_visual_design_video_first](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_visual_design_video_first.md)

### 6.3 操作系の罠

#### Exclusion G：Figma で listAvailableFontsAsync 未確認
- **失敗例：** Figma で `Hiragino Sans` を指定 → 環境によっては未インストールでフォント代替発生 → デザイン崩れ。
- **解決：** text 操作前に必ず `listAvailableFontsAsync()` で family + style 確認。
- **参照：** [feedback_figma_font_availability](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_figma_font_availability.md)

#### Exclusion H：git add のディレクトリ指定で untracked 混入
- **失敗例：** `git add projects/fambox/sections/` で untracked 118ファイル混入 → コミット肥大。
- **解決：** 修正対象が限定的なら明示パス指定。コミット前に `git diff --cached --stat` 検算。
- **参照：** [feedback_git_add_directory_caution](../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_git_add_directory_caution.md)

詳細は [bugs.md](design-system/bugs.md) を参照。

---

## 7. Learn Loop（学習機構）

> Step 1 から必須の最小機構（D-022）。

### 7.1 トリガーとアクション

| トリガー | アクション | 頻度 |
|---|---|---|
| Generate で失敗発生 | bugs.md に候補エントリ追加 | 都度 |
| 2回目の同じ修正 | bugs.md に即ルール化（Marc M2 原則） | 都度 |
| 月1回 | bugs.md 追加件数を可視化 | 月次 |
| 金曜事業開発 | 「今週の Learn 進捗」発表 | 週次 |

### 7.2 Learn が停滞しているサイン

- bugs.md の追加が 2週間以上ない → 失敗を見逃している、または記録忘れ
- 同じ feedback*.md ファイルが何度も参照される → ルール化漏れ
- 月次振り返りで「特になし」が続く → 学習が止まっている

### 7.3 Learn 層を保護する仕組み

- 金曜発表に「Learn 進捗」を **恒久発表項目** として組み込む（自然に可視化）
- 月1回、bugs.md の追加件数を須齋さんに共有
- 半年に1回、bugs.md 全体の見直し（不要規律の削除も含む）

---

## 8. Onboarding Flow（新メンバーの最初の30分）

> Step 2 以降、新規メンバー（須齋・松浦・三宅・マレル・安原さん等）が入ってきた時のオリエンテーション手順。

### 8.1 0〜5分：このファイルを読む

- [§Quick Orientation](#-5分で全体像を掴むquick-orientation)
- 重要：「今すぐ作業に入る5ステップ」を覚える

### 8.2 5〜15分：作る予定の Surface を理解

- §2 Surfaces から、自分が触る Surface を特定
- そのSurface の典型ワークフロー（§2.X）を読む
- §4.2 で自分の role を確認

### 8.3 15〜25分：禁止事項とサンプルを見る

- §6 Exclusions で「過去にあった失敗」を理解（特に Exclusion A〜H）
- bugs.md（[実物](design-system/bugs.md)）の DOCTRINE カテゴリだけ確認

### 8.4 25〜30分：依頼フォーマットを見る

- §11 テンプレ集の「持ってこい資料」例を見る
- 実際に1件依頼を書いてみる（Slack 下書きまで）

### 8.5 オンボーディング完了の判定

以下を全部 yes と言えれば OK：

- [ ] FAMBOX が何を提供しているか説明できる
- [ ] Editorial × Lab メタファーを 1分で説明できる
- [ ] 自分が担当する Surface を特定できる
- [ ] AI/Human boundary の 4カテゴリを言える
- [ ] 「declining = re-declaring」原則を実例で説明できる
- [ ] bugs.md がどこにあるか、どんな構造か知っている
- [ ] 「持ってこい資料」を書ける（5項目以上埋められる）

---

## 9. Decision Log Pointer

すべての構造的決定は `docs/okr/fambox-flywheel/DECISIONS.md` を参照。
D-001 〜 D-025 に番号付きで管理。新しい決定は連番追加で。

直近の重要決定（Marc 2nd reply 反映）：
- **D-021**：AI/Human のカテゴリベース定義（D-020 上書き）
- **D-022**：Learn 層を Step 1 から保護
- **D-023**：DNA Evolution Triggers
- **D-024**：この CLAUDE.md パターン採用
- **D-025**：Marc コラボ受諾

---

## 10. このファイルの維持

- **Owner**：宮川
- **Reviewer**：Marc-Antoine（peer review）、須齋（事業視点）、松浦（実運用視点）
- **更新頻度**：DECISIONS.md に新規 D-NNN 追加時、影響あれば更新
- **バージョニング**：v0.1（初稿）→ v0.X（運用しながら拡張）→ v1.0（Step 2 開始前）

### Evolution Triggers（このファイル）

| トリガー | 想定バージョン |
|---|---|
| 新規 Surface 追加（例：YouTube long video） | v0.X 微更新 |
| AI/Human Boundary の大幅変更 | v1.0 にバンプ検討 |
| 新規 Step（Step 4 等）導入 | v1.0 → v2.0 |
| マルチブランド化（D-008）| v2.0 + brand split |

---

## 11. テンプレート集（実践用）

### 11.1 「持ってこい資料」テンプレート（Standard 形式 / D-018）

```markdown
# 依頼書：[案件名] / [日付]

## 1. 目的（Purpose）
- ビジネスゴール：（例：法人問い合わせ件数 +30%）
- 何が成功か：（例：CTR 2%以上）

## 2. ターゲット（Target）
- ペルソナ：（例：中小企業の総務担当 / 部活顧問）
- 心理状態：（例：「健康経営してるか問われている」）

## 3. ジャーニー（Journey）
- 前：（例：Google 検索「社員食堂 健康」で流入）
- このページで：（例：「FAM が課題解決すると体感」）
- 次：（例：「資料請求 / 相談予約」）

## 4. メッセージ（Message）
- 主訴求：
- サブ：
- 避けたい：（例：押し売り感）

## 5. 制約（Constraints）
- 期限：
- 形式：（例：Shopify セクション）
- 文字数：

## 6. 参照（References）
- 自社過去：
- 外部：
- NG例：
```

### 11.2 Good / Bad コピー例

| シーン | ❌ Bad | ✅ Good |
|---|---|---|
| Hero 見出し | 「アスリート最強の食事」 | 「アスリート飯を社員食堂に」 |
| サブコピー | 「圧倒的な栄養価で勝利を掴め！」 | 「PFC バランス設計で、組織の食事を底上げ」 |
| CTA | 「今すぐ申し込み」 | 「資料を請求する」 |
| 信頼訴求 | 「業界 No.1 の実績」 | 「TOYOTA RED CRUISERS 監督2名 + 選手7名が利用」 |
| アドバイザー紹介 | 「最高峰の栄養士監修」 | 「アドバイザー：大前恵（管理栄養士）」 |

### 11.3 declining = re-declaring 宣言テンプレート

```markdown
## Boundary 変更宣言

**変更前（標準）：**
- AI proposes：[標準内容]
- Human validates：[標準内容]
- Human adjusts：[標準内容]
- Human decides：[標準内容]

**変更後（今回案件）：**
- AI proposes：[変更後内容]
- Human validates：[変更後内容]
- Human adjusts：[変更後内容]
- Human decides：[変更後内容]

**変更理由：**
[なぜこの案件で標準と異なる boundary が必要か]

**リスクと対策：**
[品質崩壊リスクと、それに対する追加チェック]
```

### 11.4 Friday Learn 進捗報告テンプレート

```markdown
## 今週の Learn 進捗（YYYY-MM-DD）

### 今週 bugs.md / feedback に追加された規律
- [新規エントリ N件、内訳]

### 「2回説明したらルール化」発火例
- [具体例 / 何が共通化されたか]

### 月次サマリ（金曜が月末週の場合のみ）
- 今月の bugs.md 追加件数：N件
- 停滞傾向：あり / なし
- 改善案：[あれば]
```

---

## バージョン履歴

| 版 | 日付 | 内容 |
|---|---|---|
| v0.1 | 2026-05-28 | 初稿。Marc の v7.34 `_TEMPLATE/CLAUDE.md` パターンを採用し FAMBOX 用に整備。D-024 に基づく |
| v0.2 | 2026-05-28 | **強化版**。Quick Orientation 追加 / Surface 別ワークフロー実例 / Hard Rules の Rule+反例ペアリング / declining=re-declaring 実例3件 / Exclusions の具体的失敗実例 / Onboarding 30分フロー / 4種のテンプレート集（持ってこい資料 / Good Bad コピー / boundary 宣言 / Friday Learn 進捗）|
