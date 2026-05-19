---
title: Phase B デプロイ計画書 — FAMBOX DS v0.5 + L0 翻訳表の本番反映
type: operations
date: 2026-05-19
session: Phase B (Session #55 末)
status: draft（実行前）/ 宮川さん承認待ち
target_repo: projects/fambox（本番 Shopify テーマ）
source_worktree: docs/okr/.claude/worktrees/jovial-benz-resume（branch claude/jovial-benz-864b2d）
estimated_duration: 2-4 hours（段階デプロイ）/ 30-60 min（フルデプロイ）
blast_radius: 大（本番 Shopify ストアの全 fambox-* セクション表示に影響）
---

# Phase B デプロイ計画書

## 0. 背景と目的

Phase A（Session #55）で **FAMBOX DS v0.5 + L0 翻訳表 v0.1** が worktree `jovial-benz-resume` に完成。22 sections / 133 tokens / Lucide icons / Token 化規律すべて整った。しかし **本番テーマ `projects/fambox/` には未反映**。

本書は本番デプロイの:
1. 差分の完全可視化
2. 段階デプロイ戦略
3. 視覚回帰テスト checklist
4. ロールバック手順

を確定する。実行は本書の承認後、別セッションまたは宮川さん主導で行う。

### 当初 handoff の見積もり誤り

handoff document（`2026-05-18-handoff-to-next-session.md`）には「theme.liquid 統合 / 5 min / 宮川さん手動」と記載されていたが、実際は:
- snippet が本番に未配置 → 配置必要
- 22 sections のうち 13 が本番未配置、9 が Token 化差分あり
- 旧版 sections（hero-v17 / voice）の廃止判断必要

→ 実工数 **2-4 時間（段階デプロイ含む）** が現実的。

---

## 1. 差分の完全可視化

### 1-A. Sections 差分（worktree 22 vs 本番 11）

| カテゴリ | ファイル | デプロイアクション |
|---|---|---|
| **新規 (13 件)** | fambox-active-plans / fambox-active-plans-v2 / fambox-bento-grid / fambox-blog-carousel / fambox-case-study / fambox-contact-form / fambox-footer / fambox-header / fambox-interview / fambox-modal / fambox-nutrition-service / fambox-spirit / fambox-stat-grid | コピー |
| **上書き / Token 化差分 (9 件)** | fambox-easy-cooking / fambox-faq / fambox-hero-v17-video / fambox-menu-showcase / fambox-model-case / fambox-plan-features / fambox-profile / fambox-subscription-plan / fambox-value-proposition | 上書き |
| **廃止候補 (2 件)** | fambox-hero-v17.liquid（→ -video 版に置換）/ fambox-voice.liquid（→ fam-voices or fambox-case-study に統合）| 削除（最終段階）|

### 1-B. var() 参照数の差分（共通 9 sections）

| Section | worktree | 本番 | 差 |
|---|---:|---:|---:|
| fambox-easy-cooking | 10 | 0 | +10 |
| fambox-faq | 40 | 0 | +40 |
| fambox-hero-v17-video | 27 | 3 | +24 |
| fambox-menu-showcase | 21 | 0 | +21 |
| fambox-model-case | 47 | 0 | +47 |
| fambox-plan-features | 32 | 0 | +32 |
| fambox-profile | 35 | 0 | +35 |
| fambox-subscription-plan | 43 | 0 | +43 |
| fambox-value-proposition | 47 | 0 | +47 |
| **合計** | **302** | **3** | **+299** |

新規 13 sections 分（Token 化済）と合わせて **約 1,000+ var() ref** が本番に追加される計算。

### 1-C. Snippets 差分

| Snippet | サイズ | デプロイアクション |
|---|---:|---|
| `fambox-tokens.css.liquid` | 10,258 B / 287 行 / 133 tokens | コピー（**最優先**：他全 sections の前提）|
| `fambox-icon.liquid` | 130 行 / 17 Lucide icons | コピー（header / footer 等で参照済）|
| `fam-scroll-reveal.liquid` | TBD 行 | コピー |

### 1-D. Layout 差分

| ファイル | 編集 |
|---|---|
| `projects/fambox/layout/theme.liquid` | `<head>` 内に `{% render 'fambox-tokens.css' %}` を 1 行追加（既存 `{% render 'meta-tags' %}` の前か後）|

---

## 2. 依存関係と順序

```
[Phase B-Step 1] snippets/ 配置（最優先）
    ├ fambox-tokens.css.liquid  ← 全ての var() 参照の前提
    ├ fambox-icon.liquid        ← header / footer などが参照
    └ fam-scroll-reveal.liquid  ← scroll reveal を使う sections が参照
    ↓
[Phase B-Step 2] layout/theme.liquid 編集
    └ {% render 'fambox-tokens.css' %} を <head> に 1 行追加
    ↓ （ここで :root に CSS 変数が宣言される状態）
    ↓
[Phase B-Step 3] sections/ 上書き（共通 9 件）
    ├ 既存 sections の Token 化版で上書き
    └ fallback 値が残っているので、snippet 未配置でも崩れない設計
    ↓
[Phase B-Step 4] sections/ 新規（13 件）
    ├ Header / Footer / Modal などインフラ系を先行
    └ Bento / Stat / Case Study / Contact Form などコンテンツ系
    ↓
[Phase B-Step 5] 旧 sections 削除（最終）
    ├ fambox-hero-v17.liquid（→ -video 版で置換済を確認後）
    └ fambox-voice.liquid（→ fam-voices で代替確認後）
```

**重要**: snippet を配置せず sections だけ更新するのは Anti（var() 参照失敗 → fallback 直値で動作するが、Token 化の意味が損なわれる）。Step 1 → 2 を **最初に必ず**実行。

---

## 3. デプロイ方式の選択

### 案 A: Shopify CLI による段階デプロイ（推奨）

```bash
# 0. 事前準備
shopify theme list --store fambox-store
# 既存テーマの ID を控える（ロールバック用）

# 1. 開発テーマ（development theme）にプッシュしてプレビュー
shopify theme push --development

# 2. プレビュー URL で視覚確認（§5 checklist）

# 3. 本番テーマに段階反映
shopify theme push --theme=<production-theme-id> --only=snippets/fambox-tokens.css.liquid
shopify theme push --theme=<production-theme-id> --only=snippets/fambox-icon.liquid
shopify theme push --theme=<production-theme-id> --only=layout/theme.liquid

# 視覚確認 → OK なら sections も push
shopify theme push --theme=<production-theme-id> --only=sections/fambox-header.liquid
# ...各 section ごとに
```

**長所**: 各ステップで動作確認、段階的ロールバック可能
**短所**: 工数 2-4 時間

### 案 B: 一括 `shopify theme push`

```bash
shopify theme push --theme=<production-theme-id>
```

**長所**: 5 分で完了
**短所**: ロールバック単位が「テーマ全体」、視覚崩れの原因切り分けが難しい

### 案 C: 手動アップロード（Shopify Admin > テーマ > コードを編集）

snippets / sections / layout を Admin UI で 1 ファイルずつ手動で貼り付け。

**短所**: ヒューマンエラー多発、22+ ファイルで非現実的

**→ 推奨は 案 A**。本書の §4 以降は案 A 前提で記述。

---

## 4. デプロイ手順詳細（案 A）

### 4-A. 事前準備

```bash
# 1. 本番テーマの ID 確認
shopify theme list --store <store-name>

# 2. 現状の本番テーマを backup として複製（Shopify Admin UI 経由）
# → ロールバック用

# 3. worktree から本番 repo に変更ファイルを準備
JBR=/Users/archecoinc./Desktop/Claude_1/docs/okr/.claude/worktrees/jovial-benz-resume
FB=/Users/archecoinc./Desktop/Claude_1/projects/fambox

cp $JBR/snippets/fambox-tokens.css.liquid $FB/snippets/
cp $JBR/snippets/fambox-icon.liquid $FB/snippets/
cp $JBR/snippets/fam-scroll-reveal.liquid $FB/snippets/
```

### 4-B. Step 1: snippets 配置 + theme.liquid 編集

```bash
# snippet コピー
cp $JBR/snippets/fambox-tokens.css.liquid $FB/snippets/
cp $JBR/snippets/fambox-icon.liquid $FB/snippets/
cp $JBR/snippets/fam-scroll-reveal.liquid $FB/snippets/

# theme.liquid 編集（Edit ツール推奨）
# <head> 内、{%- render 'layouthub_header' -%} の直後に追加:
#   {%- render 'fambox-tokens.css' -%}

# Shopify CLI で開発テーマに push
shopify theme push --development --only=snippets/fambox-tokens.css.liquid,snippets/fambox-icon.liquid,snippets/fam-scroll-reveal.liquid,layout/theme.liquid

# プレビュー確認
shopify theme dev
```

**検証**: ブラウザの DevTools で `:root` に `--color-drive: #FB4C15` 等の CSS 変数が宣言されていることを確認。

### 4-C. Step 2: 共通 sections 上書き（9 件 / Token 化差分）

```bash
for f in fambox-easy-cooking fambox-faq fambox-hero-v17-video fambox-menu-showcase fambox-model-case fambox-plan-features fambox-profile fambox-subscription-plan fambox-value-proposition; do
  cp $JBR/sections/$f.liquid $FB/sections/
done

shopify theme push --development --only=sections/fambox-easy-cooking.liquid,sections/fambox-faq.liquid,...
```

各 section の視覚回帰テスト（§5 checklist）を 1 件ずつ確認。

### 4-D. Step 3: 新規 sections（13 件）配置

優先順序:
1. **インフラ系**（最初）: fambox-header / fambox-footer / fambox-modal
2. **コンテンツ系**: fambox-stat-grid / fambox-bento-grid / fambox-case-study / fambox-contact-form
3. **ページ別**: fambox-active-plans / fambox-active-plans-v2 / fambox-blog-carousel / fambox-interview / fambox-nutrition-service / fambox-spirit

```bash
for f in fambox-header fambox-footer fambox-modal fambox-stat-grid fambox-bento-grid fambox-case-study fambox-contact-form fambox-active-plans fambox-active-plans-v2 fambox-blog-carousel fambox-interview fambox-nutrition-service fambox-spirit; do
  cp $JBR/sections/$f.liquid $FB/sections/
done

shopify theme push --development --only=sections/...
```

### 4-E. Step 4: 開発テーマでの完全視覚回帰テスト

§5 checklist を全件実行。視覚崩れがあれば該当 section を修正、再 push。

### 4-F. Step 5: 本番テーマへの反映

```bash
# 本番テーマ ID を確認
shopify theme list

# 一気に反映（リスク覚悟）または段階反映
shopify theme push --theme=<production-theme-id>
```

**重要**: 本番反映前に **Shopify Admin で本番テーマを複製** しておく（ワンクリックロールバック用）。

### 4-G. Step 6: 旧 sections の削除（任意 / 後日）

`fambox-hero-v17.liquid` / `fambox-voice.liquid` を `unpublish` または削除。これは **置換版が完全に動作確認できてから** 実施。本日は実施せず、現状維持 OK。

---

## 5. 視覚回帰テスト checklist

各 section の表示確認項目を 22 件カバー。**開発テーマプレビュー** と **本番反映後** の 2 環境で実行。

### 5-A. Section 別 checklist（22 件 × 主要項目）

#### Header（fambox-header）
- [ ] PC: ロゴ左、ナビ中央、Cart/Account 右の 3 列 layout
- [ ] PC: スクロール時 sticky 動作（Header height 維持）
- [ ] SP: hamburger menu 開閉、Cart icon が右上に表示
- [ ] hover で `--color-drive` のアクセント表示
- [ ] Lucide icons（cart / account / menu）が 1.5px stroke で表示

#### Footer（fambox-footer）
- [ ] PC: 3 列 sitemap layout
- [ ] SP: accordion 開閉
- [ ] SNS icons（X / Instagram / Facebook / YouTube）が表示
- [ ] Copyright と links が `--color-sub` で表示

#### Hero（fambox-hero-v17-video）
- [ ] Video background が再生（loop / muted / autoplay）
- [ ] Display サイズの大型見出し（`--fs-display: 56px`）
- [ ] CTA button（`--color-drive` filled）が hover で `--color-drive-hover` に
- [ ] SP: video が縦長に対応、見出しが折り返し正しく表示

#### Modal（fambox-modal）
- [ ] 開閉時の `--motion-duration-slow: 350ms` 動作
- [ ] backdrop で外側クリックで閉じる
- [ ] `--shadow-5` で modal 影が表示
- [ ] ESC キーで閉じる

#### Subscription Plan（fambox-subscription-plan）
- [ ] PC: 2 列レイアウト（standard / featured）
- [ ] featured の border が `--color-drive` でアクセント
- [ ] 価格表示の階層が `--fs-display` / `--fs-h2` / `--fs-body` で正しい

#### Bento Grid（fambox-bento-grid）
- [ ] standard / editorial / autofit の 3 preset が切替可能
- [ ] tile 間 spacing が `--space-3` / `--space-5` で整列
- [ ] image fill / video fill / glass の variant が表示

#### Stat Grid（fambox-stat-grid）
- [ ] 大数値 (`--fs-display: 56px`) + caption (`--fs-caption: 12px`) のペア
- [ ] 6 stats のグリッド整列（PC 3x2 / SP 2x3）
- [ ] 出典 caption が `--color-sub` で表示

#### Case Study（fambox-case-study）
- [ ] tile / story / logo-list の 3 variant が表示
- [ ] image + テキストの hierarchy が `--color-ink` / `--color-sub` で正しい

#### Contact Form（fambox-contact-form）
- [ ] input fields の border が `--border-base`
- [ ] focus で `--color-focus-ring`（drive 色）
- [ ] error 表示が `--color-error`
- [ ] 送信成功で success message 表示

#### FAQ（fambox-faq）
- [ ] carousel 動作（横スクロール）
- [ ] 質問展開で `--motion-duration-base: 250ms`

#### Profile（fambox-profile）
- [ ] スポーツ栄養士の写真 + 経歴 + 資格表示
- [ ] photo が `--radius-circle` で円形

#### その他 sections（11 件）
- [ ] fambox-active-plans / -v2: タブ切替動作
- [ ] fambox-blog-carousel: カルーセル横スクロール
- [ ] fambox-easy-cooking: 「3 分で完成」訴求が表示
- [ ] fambox-interview: 2 列 layout でテキスト + image
- [ ] fambox-menu-showcase: メニュー横スクロール
- [ ] fambox-model-case: モデルケース 2 列
- [ ] fambox-nutrition-service: サービス 4 タイル
- [ ] fambox-plan-features: プラン特徴のグリッド
- [ ] fambox-spirit: FAM の想いカルーセル + Heartbeat animation
- [ ] fambox-value-proposition: 3 つの価値の横スクロール

### 5-B. 横断確認項目

- [ ] DevTools で `:root` に 133 CSS 変数が宣言されている
- [ ] DevTools で `var(--color-drive)` が `#FB4C15` に resolve される
- [ ] Console にエラー無し（Liquid render エラー / CSS 読込みエラー）
- [ ] Lighthouse Performance が劣化していない（CSS 変数追加で 0-5 ms 増は許容）
- [ ] レスポンシブ（375px / 768px / 1024px / 1440px）の 4 ブレイクポイント全画面確認
- [ ] dark mode（あれば）も確認

### 5-C. 環境別確認

| 環境 | URL | 確認項目 |
|---|---|---|
| Shopify CLI dev | `shopify theme dev` → http://localhost:9292 | snippet 配置 + theme.liquid 編集の動作 |
| 開発テーマプレビュー | Shopify Admin > テーマ > 開発テーマ > プレビュー | 全 sections の視覚確認 |
| 本番反映後 | https://fambox.shop/ | 本番表示の最終確認 |

---

## 6. ロールバック手順

### 6-A. Shopify Admin から（最速 / 1 分以内）

```
Shopify Admin > オンラインストア > テーマ > 旧バックアップテーマ > 公開
```

これで **即座に旧表示に戻る**。

### 6-B. git revert（コードレベル）

```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/fambox  # 本番テーマ repo
git log --oneline -5
git revert <bad-commit-sha>
git push  # GitHub theme integration 経由で反映される場合
```

### 6-C. 段階デプロイ中の部分ロールバック

特定 section だけ崩れた場合:
```bash
git checkout <previous-sha> -- sections/fambox-modal.liquid
shopify theme push --only=sections/fambox-modal.liquid
```

---

## 7. リスクと対策

| # | リスク | 対策 |
|---|---|---|
| 1 | snippet 未配置で sections が崩れる | Step 1 を最優先実行。snippet 内には Token 値が含まれるため、配置漏れは全 var() 失敗を意味する |
| 2 | var() で `:root` 未宣言時の fallback | sections 側に直値 fallback を残してある（学び 95）→ snippet 未配置でも完全崩れではなく軽微差分のみ |
| 3 | 本番テーマでのキャッシュ問題 | Shopify CDN のキャッシュは公開時に自動 purge、ブラウザキャッシュは Cmd+Shift+R |
| 4 | Modal の z-index 衝突 | `--z-modal` token を確認、既存 modal 系コードとの干渉確認 |
| 5 | Lucide icon の inline SVG 置換漏れ | header / footer 等で `{% render 'fambox-icon' %}` 参照、snippet 未配置で 17 icons 表示不能 |
| 6 | PageFly テーマとの相互作用 | PageFly セクション内で fambox-* token を使っていないか事前確認 |
| 7 | Inline style 優先度問題 | feedback_shopify_liquid_specificity.md 参照、CSS変数の値変更が反映されない場合の 5 罠を疑う |

---

## 8. 成功基準

- [ ] 開発テーマプレビューで 22 sections が視覚崩れなく表示
- [ ] DevTools `:root` に 133 CSS 変数が宣言されている
- [ ] Console エラー / Liquid render エラー無し
- [ ] Lighthouse スコア劣化無し
- [ ] 4 ブレイクポイント（375/768/1024/1440px）全 OK
- [ ] 本番反映後の 5-A checklist 全項目 OK
- [ ] ロールバック手順 6-A が即座に実行可能な状態（旧テーマ複製済）

---

## 9. 実行タイミングと体制

### 推奨タイミング

- **平日昼間（11:00-14:00）**: ユーザートラフィック確認しやすい
- **金曜午後は避ける**: 視覚崩れ発見 → 週末対応不可リスク

### 体制

| 役割 | 担当 | 作業 |
|---|---|---|
| デプロイ実行 | 宮川さん | Shopify CLI / Admin 操作 |
| 視覚回帰確認 | 宮川さん | §5 checklist 実行 |
| Liquid 修正（必要時）| Claude | 該当 section の修正 + push |
| 緊急ロールバック判断 | 宮川さん | §6-A 実行 |

### 所要時間（実測想定）

| ステップ | 時間 |
|---|---|
| §4-A 事前準備 | 15 min |
| §4-B Step 1 snippet 配置 | 20 min |
| §4-C Step 2 共通 sections 上書き | 30 min |
| §4-D Step 3 新規 sections 配置 | 45 min |
| §4-E Step 4 視覚回帰テスト | 30-60 min |
| §4-F Step 5 本番反映 | 10 min |
| §4-G Step 6 旧 sections 削除 | 後日（任意）|
| **合計** | **2-3 hours** |

---

## 10. 次のアクション

### 本書 commit 後

1. **宮川さんレビュー** — 本書の手順・リスク・体制を確認
2. **承認 → 実行セッション準備**:
   - Shopify CLI 環境確認（`shopify version` / store auth）
   - 本番テーマ ID 取得
   - バックアップテーマ複製
3. **デプロイ実行** — 別セッションで §4 手順を実行（推奨: Subagent-Driven Development で各 Step を実装）
4. **完了報告** — OKR Excel に Phase B 完遂を記録（Task 1-2-b 進捗反映）

### 本書を実行に移すタイミング

- DNA v1.0 確定（2026-06-30）を待たず実行可（L0 翻訳表は v0.6.3 ベース、本番表示には影響なし）
- ただし FAM brand mode 実装は brand 値確定後

---

## 11. 関連参照

- L0 翻訳表: `brand/fambox/design-system/L0-translation-table.md` v0.1
- DS 現状: `brand/fambox/design-system/current.md` §7 完成度ダッシュボード
- Token snippet: `snippets/fambox-tokens.css.liquid` v0.5 / 133 tokens
- Icon snippet: `snippets/fambox-icon.liquid` / Lucide 17 icons
- Tokens Studio: `operations/scripts/tokens-studio-v05-complete.json`
- OKR: `FAMBOX_OKR_宮川.xlsx` / Task 1-2-b（DSチェック→v1.0完成→成長フェーズ反復）

## 改訂履歴

- v0.1 (2026-05-19 / Session #55 末): 初稿。差分完全可視化 + 段階デプロイ計画 + 視覚回帰 checklist + ロールバック手順。
