# Brand Repository CHANGELOG

FAM / FAMBOX ブランドDNA・デザインシステムの全体変更履歴。昇格・確定・構造変更のイベントを記録。

---

## 2026-04-27（DS v0.2 — Worksheet S3 完了 / Worksheet §1-§14 全クローズ）

### S3: §12 Contact Form / §13 Subscription Card / §14 Case Study / §15 自由入力 確定

#### 状況
- §12-§14 の Spec ファイル群（contact-form.md / subscription-plan-card.md / case-study.md）は 2026-04-20 に v0.2 confirmed 状態
- S3 では Worksheet 同期 + 合成決定の正式承認 + 一部 Spec 改訂を実施

#### 既存決定の確認
- **§12 Contact Form**: 同画面 inline 確認 → Success 別ページ / カスタム自動返信「処理中です…」トーン
- **§13 Subscription Card**: 価格 h2 Ink 色 / 2 CTA / 「おすすめ」バッジ Drive 1 プランのみ
- **§14 Case Study**: 3 レイアウト併用（カード/ストーリー/ロゴ）/ 全 Data Viz 活用 / 公表 OK + 匿名 混在

#### 合成決定の判定（5件）
- ✅ **§12.1.a 役職拡張 4→8 項目** A 承認 — 監督/コーチ/専属栄養士/マネージャー/学校・クラブ事務局/選手本人/保護者/その他
- 🔄 **§12.1.b 電話番号** Spec の「任意」を **B 採択で必須に変更** — 緊急連絡確保のため
- ✅ **§12.1.c 利用検討時期 select 追加** A 承認 — リード温度判定（任意フィールド・select: すぐ/1か月/3か月/未定）
- 🔄 **§13.1.a 最低契約期間・初月特典** Spec の「両方追加推奨」を **C 採択で両方不採用** — カード内に詰め込まず FAQ / キャンペーン側で扱う
- ✅ **§14.1.a 食事戦略の概要** A 承認 — Integrity 体現として正式採用

#### §15 自由入力欄
- A=リスト化スキップ採択 — 別タスクで実施（懸念/リファレンス/予算制約/事前確認の 4 項目を後日起票）

#### Spec 改訂
- `components/contact-form.md` v0.2 → **v0.3**: 11 フィールド化（電話番号 必須化 + 利用検討時期 追加）/ バリデーション table 更新
- `components/subscription-plan-card.md` v0.2 → **v0.3**: 10 → 8 項目化（最低契約期間・初月特典をカードから外す）/ レイアウト構造・Liquid 例・Do/Don't 整合
- `components/case-study.md` v0.2 維持: 「食事戦略の概要」は既に ✅推奨 で記載済 → A 承認で確定

### 更新ファイル
- `brand/fambox/design-system/DS_INPUT_WORKSHEET.md`（§12-§15 ✅ 同期、session_log 追記、3 セッション完了マーク）
- `brand/fambox/design-system/components/contact-form.md` v0.3
- `brand/fambox/design-system/components/subscription-plan-card.md` v0.3
- `brand/fambox/design-system/operations/2026-04-27-worksheet-completion-plan.md` S3 完了マーク
- `brand/fambox/design-system/current.md` v0.1 → v0.2 タグアップ

### v0.2 マイルストーン到達
- Worksheet §1-§14 全クローズ
- L1 Tokens / L2 Primitives 5 件（Button/Input/Avatar/FormControls/Progress）/ L3 Patterns 1 件（FormField）/ L4 Components 3 件（Contact Form/Subscription Card/Case Study）すべて Spec 確定
- 5/29 期限 TOPページ DNA 反映の前提が整備完了

### 次フェーズ（v0.3 以降）
- Figma master file Step 6（Icons）→ Step 7（Library 公開）
- Primitive デザイン Figma 化（Button v0.3 仕様準拠で開始可能）
- §15 自由入力（懸念・リファレンス・予算・事前確認）別タスク起票
- L0 Foundation: DNA v1.0 確定後（6月末予定）

---

## 2026-04-27（DS v0.2 — Worksheet S2 完了）

### S2: §7 Input / §8 FormField / §9 Avatar / §10 Form Controls / §11 Progress 確定

#### 状況
- §7-§11 の Spec ファイル群（input.md / form-field.md / avatar.md / form-controls.md / progress.md）は 2026-04-20 に既に v0.2 confirmed 状態で作成済
- Worksheet 側に ✅ マークが未反映だった SSoT 不整合を解消するセッション

#### 確認・承認した既存決定
- **§7 Input**: 下線型 + 枠囲み型ハイブリッド / Textarea = 枠囲み縦伸 / onBlur 検証 + 自由記述に文字数カウンタ / 「必須」バッジ
- **§8 FormField**: Label 上配置 / HelperText Input下薄色 / ErrorMessage Input下赤（HelperText 非表示）/ 入力例は HelperText
- **§9 Avatar**: XS24/SM32/MD48/LG64/XL96 / 円形 / フォールバック=イニシャル1文字（Deep Blue 背景・White 文字）
- **§10 Form Controls**: Checkbox 角4px Drive / Radio 円形 Drive 塗り潰し / Toggle Pill Drive ON / 主用途 Checkbox
- **§11 Progress**: 線形 + 円形 両方 / Spinner 円形回転 Drive

#### 合成決定の正式承認（A 採択）
- **§9.4 Avatar 枠**: default 装飾なし + `.is-featured` 時のみ Drive 2px ボーダー（focus は別途 outline）
- **§11.3 Loading text**: 基本=文言なし（Spinner のみ）+ 重要処理（送信・決済等）のみ「処理中です…」 — Worksheet 元選択肢には不在の独自文言を採用

#### NG文言ガイドライン明示
「もう少しお待ちください！」（煽り）/「がんばって読み込み中…」（擬人化過剰）/「Loading...」（英語直書き）/「ロード中」（略語）

### 更新ファイル
- `brand/fambox/design-system/DS_INPUT_WORKSHEET.md`（§7-§11 ✅ 同期、session_log 追記）

### 次セッション
- **S3**: §12 Contact Form / §13 Subscription Card / §14 Case Study / §15 自由入力

---

## 2026-04-27（DS v0.2 — Worksheet S1 完了）

### 実行設計
- `brand/fambox/design-system/operations/2026-04-27-worksheet-completion-plan.md` を作成（S1-S3 の3セッション計画）

### S1: §4 Z-index / §5 Icons / §6 Button 確定

#### §4 Z-index（既存仕様の確認）
- 既存 Shopify テーマとの z-index 衝突なしと確定（`--z-legacy-sticky-cta: 9990` のみ legacy、v0.5 で `--layer-3` へ順次刷新）
- 追加 Layer 不要 — Sticky CTA / Announcement Bar / Chat Widget は `--layer-3` で全て吸収

#### §5 Icons（自作運用に確定）
- 路線: **自作のみ運用**。Lucide / Phosphor / Heroicons への置換やハイブリッドは不採用
- グリッド: **24×24 viewBox** に確定（既存 `brand/shared/icons/` 実測値準拠）
- 色運用: **3色バリアント別ファイル方式**（default Ink / `-drive` / `-white`）— `currentColor` 単一案は撤回
- 命名: ファイル名 `{cat}-{name}{-variant}.svg` 維持／Figma 内は `icon/{cat}/{name}-{variant}` 階層化（並列維持）
- `tokens/icon-creation-spec.md` を訂正（master サイズ 32×32 → 24×24、currentColor → 3バリアント実測形式へ）

#### §6 Button（5 Variant × 3 Size × 6 State 確定）
- Variant 5種採用: `btn-primary` / `btn-secondary-ink` / `btn-secondary-drive` / `btn-ghost` / `btn-link`（Destructive 不採用）
- Size 3段階全採用: `btn-sm`（8/16）/ `btn-md`（12/32）★既定 / `btn-lg`（16/40）— FAM corp-btn 既存値継承
- State 6種: default / hover / focus（focus-visible）/ active / disabled / loading
- Icon Button 両形態採用: `btn-icon-only`（aria-label 必須）+ `btn-with-icon`（leading/trailing）
- CTA 文言は別タスク（CTA Wording Workshop / 大前さん討議要）として分離
- `components/button.md` を v0.2 seed → v0.3 stable に更新（フル実装可能なCSS含む）

### 更新ファイル
- `brand/fambox/design-system/DS_INPUT_WORKSHEET.md`（§4-§6 ✅ 反映、session_log 追記）
- `brand/fambox/design-system/components/button.md`（v0.3 stable）
- `brand/fambox/design-system/tokens/icon-creation-spec.md`（24×24 訂正・3バリアント運用明記）
- `brand/fambox/design-system/operations/2026-04-27-worksheet-completion-plan.md`（新規）

### 次セッション
- **S2**: §7 Input / §8 FormField / §9 Avatar / §10 Form Controls / §11 Progress
- **S3**: §12 Contact Form / §13 Subscription Card / §14 Case Study / §15 自由入力

---

## 2026-04-24（GA4 Phase 1 完全稼働化）

### GA4 Shopify デプロイ完了
- **4 Liquid ファイルを Shopify 本番反映**:
  - `fam-corp-hero.liquid`（data-gtag-cta 1箇所追加）
  - `fam-case-study.liquid`（data-gtag-cta/nav 4箇所追加）
  - `fam-collection-plan.liquid`（data-gtag-cta 1箇所追加）
  - `fam-ga4-events.liquid`（285行・funnel_step + generate_lead 追加）
- theme.liquid GTM noscript クリーン確認（既に削除済）
- 旧測定ID `G-T41J15LDX1` 不在確認（Google & YouTube チャネル設定）

### GA4 カスタムディメンション登録（MVP冷凍プロパティ）
- ステップ名（`step_name`）/ Event scope
- ステップ番号（`step_number`）/ Event scope
- ステップラベル（`step_label`）/ Event scope

### Realtime 動作確認（全イベント正常発火）
- `page_view`: 10-12回 ✅
- `cta_click`: 7回 ✅（新規追加CTAを含む全対象）
- `funnel_step`: 5回 ✅（step_name パラメータ値 `corp_lp_view` 記録確認）
- `form_funnel`: 1回 ✅（フォーム関与計測・ボーナス機能）
- `user_engagement` / `session_start`: 標準イベント発火

### OKR 進捗
- **Task 5-1-a（GA4計測設計仕上げ）: 90% → 100%** ✅
- **KR5-1（GA4計測＆週次自動レポート）: 95% 達成**
- OKR Excel（`FAMBOX_OKR_宮川_backup_pre_v6.4.xlsx`）更新済

### ドキュメント
- `docs/ga4/deploy-guide-20260424.md`（デプロイ手順書）
- `DAILY_BACKLOG.md` の B3-1 / B3-2 / B3-3 を完了マーク

### 次フェーズへの布石
- ファネル離脱分析（form_funnel）により Contact Form 改修（8月・Task 2-1-c）の前提データ蓄積開始
- KR5-2 因果仮説サイクル（6月以降）のデータ基盤完成

---

## 2026-04-20（集中セッション・DS v0.2 → v0.3 Seed完成）

### Figma Library 構築
- Figma マスターファイル「FAMBOX Design System」作成（7ページ構成）
- Tokens Studio 経由で 117 Variables 投入
- 213 Icon Components 取り込み・命名整理（icon/{category}/{name}-{color} 形式）
- 11 Text Styles 登録（mega/hero/display/h1/h2/h3 英字 + lead/body/body-sm/caption 日本語 + stat）
- 5 Effect Styles 登録（shadow/1〜5）
- Library 公開（v0.3）
- URL: https://www.figma.com/design/QsiBrc2v20BYw76YHI9x3e/FAMBOX-Design-System

### DS構築関連ドキュメント
- 9つの Component MD（Button/Input/FormField/Contact Form/Avatar/FormControls/Progress/Plan Card/Case Study）完成
- tokens/ 以下 5MD + tokens.css + tokens-figma.json
- z-index-audit.md（ZOZO Layer Stack 方式）
- icon-inventory.md + icon-creation-spec.md
- cta-wording-proposal.md（Primary CTA「話を聞いてみる」確定）

### 戦略・運用
- STRATEGY.md（入口の支配 × 出口の独占）
- lastmile-playbook.md（AI生成→人補正 SOP・4カテゴリ）
- figma-master-setup-guide.md（7ステップ手順書）

### Repository 構造変更
- ブランドリポジトリを4層構造に再構築（README / INDEX / current / drafts+archive）
- FAM v0.2〜v0.5 を `fam/brand-dna/` 配下に整理
- FAMBOX v0.6.3 を `fambox/brand-dna/drafts/` 配下に移動
- FAMBOX DS v0.1 を `fambox/design-system/drafts/` 配下に移動
- HTML試作を `fambox/prototypes/` に移動

### FAMBOX Brand DNA v0.6.3（作業版）
- インタビュー反映版として主要要素を確定
- 新規: L1-0 Anti（反対概念）をブランド核に格上げ
- 新規: Core Values 6番目に Integrity 追加
- 新規: L3-1 キャラクターを二層構造で定義
- 新規: L3-5 関係性を「共創者（Equal Partner in Challenge）」として正式命名
- 確定: L2-1 戦う市場を「栄養ソリューション市場」として独自定義
- 確定: L1-2 Vision / L1-3 Brand Concept を FAM継承で確定
- ADR-001〜010 を記録

### FAMBOX Design System v0.1
- 初版構築プラン作成（10層フレームワーク・111要素）
- FAM v0.5 から 48要素継承 + FAMBOX 63要素新設の整理

---

## 2026-04-20 以前

### FAM Brand DNA v0.5（2026-04-15）
- Decodeフェーズ完了
- Semantic色確定 / L-1入力UI確定 / L-3ナビ既存踏襲確定
- B-6多言語方針確定 / H パララックス・ページ遷移方針確定
- Motion変数をCSS変数に追加

### FAM Brand DNA v0.4（2026-04-15）
- 5色パレット確定（Drive/Sky/Deep/Ink/BG）
- タイポ確定（Poppins + Hiragino）
- CSS変数テンプレート

### FAM Brand DNA v0.3（2026-04-15）
- メタファー確定（Editorial × Lab）
- ライト基調確定 / Bento Grid確定
- データ表現F 8コンポ詳細設計

### FAM Brand DNA v0.2（2026-04-15）
- 視覚言語5軸を6軸に拡張
- 87項目に要素拡張

---

## バージョン昇格ルール

- **draft（`drafts/v*.md`）**: 作業中・頻繁に更新
- **current（`current.md`）**: 最新版の動的エイリアス（drafts最新をcp）
- **release（ルート直下 `v*.md`）**: 確定版として昇格（第三者テスト＋主要関係者レビュー通過）

### 昇格イベント
- 2026-04-15: FAM DNA v0.5 release
- （予定）2026-06-30: FAMBOX DNA v1.0 release
- （予定）2026-09-30: FAMBOX DNA v1.1 release / FAMBOX DS v1.0 release
