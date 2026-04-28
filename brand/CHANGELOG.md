# Brand Repository CHANGELOG

FAM / FAMBOX ブランドDNA・デザインシステムの全体変更履歴。昇格・確定・構造変更のイベントを記録。

---

## 2026-04-28（DS v0.2 完成基準到達 — Modal + Stat Card + 実装計画 + Operations 運用ルール）

### 4 タスクを 1 セッションで完了

ユーザー指定の「1〜4 を実行」フローを順次完了:

#### タスク 1: TOPページ DNA 反映 実装計画 v0.1 策定
- **新規ファイル**: `operations/2026-04-28-top-implementation-plan.md`（542 行）
- TOPページ既存 25 sections を 4 Tier に分類:
  - Tier 1（5/29 期限直撃）: 7 sections / 21h
  - Tier 2（優先度中）: 5 sections / 13h
  - Tier 3（優先度低）: 2 sections / 3h
  - Tier 4（既存維持・トークン適用のみ）: 11 sections / 5.5h
- **総工数 42.5h**（5/29 まで 30 日 / 1.5h/日 で完了可能）
- 5 週間スケジュール（週次タスクブロック）と依存関係マップ
- 8 項目の section 改修共通検証チェックリスト

#### タスク 2: L4 Modal を v0.2 confirmed として追加
- **新規ファイル**: `components/modal.md`（約 460 行）
- **Variants 3 種**: confirmation / detail / sheet
- **Backdrop**: Glass 4（opacity 0.6）固定
- **Close 3 方法**: × ボタン + ESC + Backdrop クリック すべて許容（a11y 最大）
- **サイズ**: Confirmation 400 / Detail 800（max-height 90vh）/ Sheet 100%（SP）→ 400（PC で confirmation 風）
- **Anti-pattern 禁止 4 項目**: ネスト / 英語ボタン / 90% 超 / PC で Sheet
- Focus trap・初期 focus・スクロールロック・focus 復元 等 a11y 仕様明記

#### タスク 3: L3 Stat Card 独立 Pattern 化（v0.2 confirmed）
- **新規ファイル**: `components/stat-card.md`（約 380 行）
- Card Pattern Flat と Bento Tile Stat-focus を統合し**汎用 L3 Pattern として独立**
- **Sizes 3 段階**: compact（fs-h2 32px）/ default（fs-display 56px）★既定 / large（fs-mega 96px / SP fs-hero 64px）
- **Layouts 2 種**: vertical（既定）/ horizontal
- **4 要素**: Value（必須）/ Unit（0.4em）/ Label（必須）/ Period（任意）
- **Color**: Value は Drive 色固定（FAMBOX らしさ）
- **Anti-pattern 禁止 4 項目**: アニメ / 単位ラベル同サイズ / large 背景画像 / 複数数字並列
- v0.3 で `bento-stat-focus` を Stat Card 薄 wrapper 化予定

#### タスク 4: L7 Naming Convention & Governance v0.2 整備
- **新規ファイル**: `operations/naming-convention.md`（約 400 行）
- v0.2 完成基準で抜けていた運用ルール 4 項目を統合:
  1. **SSoT 宣言**: 各レイヤーの Single Source of Truth 明示・競合時のルール
  2. **命名規則**: CSS クラス / Token / Liquid Snippet / Section / Figma の全領域
     - `{component-name}` `{component}-{variant}` `.is-{state}` `.has-{property}` パターン定義
     - Token category prefix 表（color- / bg- / space- / fs- 等）
     - 禁止事項（camelCase / snake_case / 番号サフィックス 等）
  3. **Versioning Policy**: Semantic Versioning 準拠 / Component 個別 status（seed/confirmed/stable/deprecated）
  4. **Contribution / Deprecate Process**: 新規追加 10 ステップ / 廃止 3 段階フロー
- Branch / Commit メッセージ規約（Conventional Commits）も明記

### 全更新ファイル
- `brand/fambox/design-system/operations/2026-04-28-top-implementation-plan.md`（新規）
- `brand/fambox/design-system/components/modal.md`（新規）
- `brand/fambox/design-system/components/stat-card.md`（新規）
- `brand/fambox/design-system/operations/naming-convention.md`（新規）
- `brand/fambox/design-system/DS_INPUT_WORKSHEET.md`（§22-§23 追記、session_log 拡張）
- `brand/fambox/design-system/current.md`（milestone 完成基準到達行追記）

### v0.2 完成基準到達

```
L0 Foundation:  🔶 50%（DNA v1.0 待ち / 6月末）
L1 Tokens:      ✅ 完成
L2 Primitives:  ✅ 5件
L3 Patterns:    ✅ 4件（FormField / Card / Bento Tile / Stat Card）
L4 Components:  ✅ 8件（Contact Form / Subscription Card / Case Study / Hero / Header / Footer / Bento Grid / Modal）
L5 Templates:   📋 TOPページ実装計画策定済み（実装は別フェーズ）
L7 Operations:  ✅ Naming Convention & Governance v0.2 + figma-master-setup-guide + lastmile-playbook + 各種 plan
L8 Tools:       🔄 60%（Figma Step 5/7）
```

### 次フェーズ（v0.3 以降）
- TOPページ実装着手（Tier 1 から開始 / Header 先行）
- L4 FAQ Accordion / Profile Card / Tabs Spec 化
- L7 Operations の Lint 自動化・Figma 同期自動化（v0.5）
- L0 Foundation 翻訳表（DNA v1.0 連動・6月末）
- v0.5 マイルストーン（DS Tokens + Primitives 完成版・6/30）

---

## 2026-04-28（DS v0.2 拡張 — §20-§21 Bento Tile + Bento Grid 確定）

### L3 Bento Tile + L4 Bento Grid を v0.2 confirmed として追加

#### 背景
- 5/29 TOPページ DNA 反映の **主役エリア**（Hero と並ぶ重要要素）
- 既存 Liquid に Bento 実装なし → Brand DNA v0.5 C-Bento タイル仕様（5 sizes / 12 col / 主構図対角線）をゼロから体系化
- L3 Pattern（Tile 単体）と L4 Component（Grid 配置システム）を分離設計

#### Bento Tile（L3 Pattern）— Variants 4 種 + 拡張余地
- **Standard**: Card Standard 継承（タイトル + 本文 + 任意 CTA）
- **Glass**: 部分ガラス効果（Glass 1-5 opacity 5 階調）
- **Image-fill**: 画像が全面 + テキスト下部オーバーレイ
- **Stat-focus**: 大型数字（`--fs-display` 56px）+ ラベル

#### Bento Tile — 5 Sizes（DNA 既定）
- `tile-1x1` / `tile-2x1` / `tile-1x2` / `tile-2x2`（主役）/ `tile-3x2`（メガ）
- SP では全タイル `grid-column: span 1` に強制縮退

#### Bento Grid（L4 Component）— Variants 3 種 + 拡張余地
- **Standard**: PC 12 col / Tablet 6 col / SP 1 col + 自由配置
- **Editorial**: Standard + **主構図ルール強制**（対角線 + 主役 2×2 最低 1 個必須）
- **Auto-fit**: `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))` + `grid-auto-flow: dense`

#### Bento Grid — Gap（DNA 既定 + modifier 上書き）
- 既定: SP 16 / Tablet 24 / PC 32px
- modifier: `bento-gap--sm`(16) / `bento-gap--md`(24) / `bento-gap--lg`(32)

#### 確定事項
- **DNA 5 sizes 厳守**（拡張は規律内のみ）
- **Glass Variant 専用** — 他 Variant には Glass 適用しない
- **Stat-focus は `--fs-display` 56px 固定** — Hero `--fs-mega` 96px との階層成立
- **Editorial 主構図強制** — 主役 2×2 以上 最低 1 個・対角線配置・将来 Lint 検出可能
- **Tile 数 4-9 個推奨** — 12 個以上禁止（情報過剰）

#### Anti-pattern 禁止リスト（Tile / Grid 各 4 項目）
- Tile: 同サイズ並列 / Drive 全タイル背景 / Glass + Hero級 mix-blend を image-fill 以外 / 間隔 16px 未満 禁止
- Grid: 同サイズ並列 / 主役タイルなし / Gap 16px 未満 / 12 タイル以上 禁止

#### L4 派生（bento-grid.md / bento-tile.md §派生関係 に明記）
- Hero 内 Bento ブロック ← editorial（compact）+ Glass tile-3x2
- KPI Dashboard ← autofit + Stat-focus tile 群
- Product Showcase Grid ← standard + Image-fill 主体

### 更新ファイル
- `brand/fambox/design-system/components/bento-tile.md`（新規・v0.2 confirmed・約 480 行）
- `brand/fambox/design-system/components/bento-grid.md`（新規・v0.2 confirmed・約 470 行）
- `brand/fambox/design-system/DS_INPUT_WORKSHEET.md`（§20-§21 追記、session_log 拡張）
- `brand/fambox/design-system/current.md`（milestone 拡張行追記）

### 効果（5/29 TOPページ前提整備の完成）
- L3 Patterns 2件 → 3件（FormField / Card / **Bento Tile**）
- L4 Components 6件 → 7件（Contact Form / Subscription / Case Study / Hero / Header / Footer / **Bento Grid**）
- **5/29 TOPページ DNA 反映の Spec 全前提が完全に揃った状態**:
  - Header / Hero / Bento Grid（中央主役）/ Case Study / Footer すべて Spec 確定
  - 中継ぎセクションは Hero `hero--tall` または Bento Grid Standard で実装可能
- TOPページ実装着手可能

---

## 2026-04-28（DS v0.2 拡張 — §19 Footer L4 Component 確定）

### L4 Footer を v0.2 confirmed として追加

#### 背景
- 全画面共通 Component / 5/29 TOPページ DNA 反映で Header と並ぶ必須要素
- 既存 Liquid（fam-footer-v2 / fambox/sections/footer）の実測抽出
- Brand DNA Integrity 体現（Legal 提示 / 煽り CTA 排除 / 控えめな Social）

#### Variants 3 種採用 + 拡張余地あり
- **Standard**: Brand + Nav columns + Social + Bottom row（fam-footer-v2 継承）
- **Minimal**: Brand + Bottom row のみ（LP / チェックアウト）
- **Sitemap**: Standard + 詳細 Sitemap 多列カテゴリ（将来用）

#### 確定事項
- **背景**: Ink (`#1B1D1A`) 単色固定（Drive ベタ塗り禁止 / White on Ink = 16.6:1 WCAG AAA）
- **Logo 配置**: 左固定（Header と整合）
- **SNS リンク**: 全 Variants で必須（Instagram / YouTube / note 等 / 40×40 上限）
- **Bottom row**: Copyright + Legal links（Privacy / Terms / 特商法）の最小構成
- **CTA**: Footer に CTA を置かない（Header / Hero / Section で十分・繰り返し回避）
- **背景差別化**: Bottom row に `rgba(0,0,0,0.3)` + `border-top rgba(255,255,255,0.1)`

#### Anti-pattern 禁止リスト（Q7 A 全採択）
1. Drive 色背景の全面ベタ塗り 禁止
2. SNS アイコンを Display サイズ（64px+）にしない
3. Bottom row に動きアニメ 禁止
4. Footer 内に Hero 級画像を置かない

#### L4 派生関係（footer.md §L4 派生関係 に明記）
- Checkout Footer ← Minimal + Trust badge / セキュリティロゴ
- Email Footer（メール埋め込み）← Minimal + inline CSS
- Mobile App Footer（PWA）← Standard（compact）+ App-specific links

### 更新ファイル
- `brand/fambox/design-system/components/footer.md`（新規・v0.2 confirmed・約 600 行）
- `brand/fambox/design-system/DS_INPUT_WORKSHEET.md`（§19 追記、session_log 拡張）
- `brand/fambox/design-system/current.md`（milestone 拡張行追記）

### 効果（TOPページ前提整備の完成）
- L4 Components 5件 → 6件（Hero + Header + Footer の TOP 三役確定）
- 5/29 TOPページ DNA 反映の **Header / Hero / Footer 全 Spec 完成**
- 残り Bento Grid（Card 派生）/ Case Study 配置（既存 Spec）/ 中継ぎセクションのみ
- TOPページ実装着手可能な状態

---

## 2026-04-28（DS v0.2 拡張 — §18 Header L4 Component 確定）

### L4 Header を v0.2 confirmed として追加

#### 背景
- 全画面共通の Component / 5/29 TOPページ DNA 反映に必須
- 既存 Liquid（fam/sections/header / fam-header-menu / fambox/sections/header）の実測抽出
- Brand DNA v0.5 の「ハンバーガー不採用 / 横スクロールメニュー / Drive Pill CTA」を体系化

#### Variants 3 種採用 + 拡張余地あり
- **Standard**: Logo + Menu + CTA + Cart/Account（通常ページ全般）
- **Minimal**: Logo + CTA のみ（LP / チェックアウト）
- **Mega**: Standard + Mega Menu（カテゴリ展開・将来用）

#### Heights 3 段階
- `header--compact`（64px）/ `header--default`（80px）★既定 / `header--tall`（96px）

#### Sticky Modes 3 種（modifier 切替・Q3 D 採択）
- `header--sticky` ★既定（DNA 既定の常時固定）
- `header--scroll-up`（下方向スクロールで隠れ・上方向で再表示）
- `header--static`（sticky なし・Hero 一体化演出用）

#### 確定事項
- **Logo 配置**: 左固定（高さは Header の 50% 上限）
- **CTA**: Header 末尾に Primary 1 個固定（btn-primary btn-md / DNA 既定）
- **SP 挙動**: 990px 未満で横スクロールメニュー + Shopify drawer 併用（**ハンバーガー不採用**）
- **メニューフォント**: `--fs-body`（16px）/ `--fw-medium` / Display サイズ禁止
- **z-index**: `--layer-4`（tokens.css の Sticky Header / Drawer 階層）

#### Anti-pattern 禁止リスト（Q7 A 全採択）
1. ハンバーガー単独運用 禁止（DNA 違反）
2. Header に Drive 色ベタ塗り 禁止
3. Logo を Drive 色背景上に置かない
4. メニューフォントを Display サイズ（48px+）にしない

#### L4 派生関係（header.md §L4 派生関係 に明記）
- Article Header（Blog 記事冒頭）← Standard（compact）+ Breadcrumb / カテゴリラベル
- Checkout Header ← Minimal（compact）+ ステップ表示
- Sticky CTA Bar（Header 連動）← Minimal（compact）/ 別 Component / `--layer-3`

### 更新ファイル
- `brand/fambox/design-system/components/header.md`（新規・v0.2 confirmed・約 460 行）
- `brand/fambox/design-system/DS_INPUT_WORKSHEET.md`（§18 追記、session_log 拡張）
- `brand/fambox/design-system/current.md`（milestone 拡張行追記）

### 効果
- L4 Components 4件 → 5件（Hero Section + Header 連動で TOP 上半分の Spec 確定）
- 5/29 TOPページ DNA 反映に必要な共通 Component が揃う
- Footer Spec で TOP の上下が完成（次セッションタスク）

---

## 2026-04-28（DS v0.2 拡張 — §17 Hero Section L4 Component 確定）

### L4 Hero Section を v0.2 confirmed として追加

#### 背景
- 5/29 TOPページ DNA 反映（OKR Task 2-1-a）の主役 Component
- 既存 Liquid（fam-corp-hero / fambox-hero-v17-video / fam-blog-hero）の実測抽出をベース
- Brand DNA v0.5 の「NBA HOOP 型タイポ重ね」「TNF 級余白」を体系化

#### Variants 4 種採用 + 拡張余地あり
- **Video Fullscreen**: 全画面動画 + Logo + Title + Text + CTA（fam-corp-hero / fam-blog-hero 継承）
- **Video Split**: 左右分割動画 + 4 Corner Icons + 中央テキスト（fambox-hero-v17 継承）
- **Image Editorial**: 静止画 + タイポ Editorial 配置（NBA HOOP モード ON/OFF 可）
- **Minimal Text**: 装飾なし大型タイポ（FAQ / 告知 / 社内ページ）

#### Heights 3 段階
- `hero--full`（100vh）★既定 / `hero--tall`（70vh）/ `hero--compact`（40vh）

#### 確定事項
- **CTA 数**: 任意（0〜2）— FAQ Hero=0 / TOP=Primary 1 / Subscription LP=Primary+Secondary
- **NBA HOOP モード**: `is-hoop` modifier で任意 ON/OFF（mix-blend-mode: difference）
- **パララックス**: 動画にも適用可能（DNA v0.5 拡張）/ slow + 15% 以下 / prefers-reduced-motion で必ず無効

#### 共通仕様
- max-width `--container-max`（1440px）/ padding PC `--space-8`(160px) SP `--space-7`(96px) ★TNF 級
- Title PC `--fs-mega`(96px) / SP `--fs-hero`(64px) / `--font-en` Poppins / `--fw-bold`
- Loader / Scroll cue（`SCROLL` bouncing animation）/ overlay gradient（動画系）

#### Anti-pattern 禁止リスト（Q6 A 全採択）
1. 動画 + 派手フィルタ重ね禁止
2. Drive 色背景の全画面ベタ塗り禁止
3. Hero 内 Primary CTA 2 個以上禁止
4. Pill 形状以外の CTA 禁止

#### L4 派生関係（hero-section.md §L4 継承関係 に明記）
- Bento Tile ← Image Editorial / Standard Card 派生
- Section Hero（中継ぎ）← Image Editorial（hero--tall）
- Page Header（記事冒頭）← Minimal Text（hero--compact）

### 更新ファイル
- `brand/fambox/design-system/components/hero-section.md`（新規・v0.2 confirmed・530+ 行）
- `brand/fambox/design-system/DS_INPUT_WORKSHEET.md`（§17 追記、session_log 拡張記録）
- `brand/fambox/design-system/current.md`（milestone 拡張行追記）

### 効果と次フェーズ
- 5/29 TOPページ DNA 反映の主役 Spec 確定 → 実装着手可能
- Bento Tile / Section Hero / Page Header を Hero 派生として高速に書ける土台
- L4 Components 3件 → 4件（Contact Form / Subscription Card / Case Study + Hero Section）

---

## 2026-04-27（DS v0.2 拡張 — §16 Card Pattern 確定）

### L3 Card Pattern を v0.2 confirmed として追加

#### 背景
- v0.2 マイルストーン到達直後、L3 Patterns に唯一未着手の最頻出要素「Card」を 30 分セッションで Spec 化
- 既存 Liquid（fam-achievement / card-product / subscription-plan-card / case-study）の実測抽出をベースに L3 Pattern として一般化

#### 確定事項
- **Variants 4 種採用 + 拡張余地あり**: standard / featured / horizontal / flat。v0.3 以降で `card-{variant-name}` 形式のカスタム追加可能（拡張ルールは card.md §拡張ルールに明記）
- **horizontal の SP 折り返し**: SP でも横並び維持（画像 30% / テキスト 70%）/ 極小 SP（〜480px）のみ縦折返し許可
- **CTA 必須ルール**: 全 Variants で CTA 1 個以上必須（情報のみ Card は作らない）
- **`.is-selected` 状態**: Drive 2px 枠線で表現、padding -1px 補正で外形維持

#### 共通 Props
- background `--bg-primary`（flat のみ `--bg-secondary`）/ border `1px --border-light`（Featured・Selected は 2px Drive）/ radius `--radius-md` 固定 / padding `--space-3` / shadow-1 default → shadow-3 hover

#### L4 Component への継承マップ（card.md §L4 継承関係 に明記）
- Subscription Plan Card ← Featured / Standard
- Case Study Card ← Horizontal
- Article Card ← Standard
- Stat Card ← Flat
- Hero Card（Bento Tile）← Standard / Horizontal

### 更新ファイル
- `brand/fambox/design-system/components/card.md`（新規・v0.2 confirmed・479 行）
- `brand/fambox/design-system/DS_INPUT_WORKSHEET.md`（§16 追記、session_log 拡張記録）
- `brand/fambox/design-system/current.md`（milestone 拡張行追記）

### 次フェーズへの効果
- Subscription Plan Card v0.3 / Case Study v0.2 が Card Pattern を継承する関係を明示化
- Hero Section / Header / Article Card 等の未 Spec 化 L4 Component を Card 派生として高速に書ける土台が完成
- 5/29 TOPページ DNA 反映の前提整備が一段進捗

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
