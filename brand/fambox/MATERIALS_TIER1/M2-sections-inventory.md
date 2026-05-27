---
title: Shopify Sections Inventory — M2 Tier 1
date: 2026-05-27
owner: 宮川（ARCHECO）
status: tier-1-partial
material_id: M2
scope:
  - projects/fambox/sections/ (115 files)
  - projects/fam/sections/ (21 files)
total_count: 136
---

# M2: 現存 Shopify セクション一覧

MATERIALS_CHECKLIST.md M2 に対応する**全 136 セクション**の棚卸し。Brand DNA / DS Phase B 着手のため、各セクションの「役割 / 刷新優先度 / DS v0.2 対応状況」を一覧化します。

## サマリ（命名 prefix 別カテゴリ）

| カテゴリ | 件数（fambox） | 件数（fam） | 合計 | 役割 |
|---|---:|---:|---:|---|
| **`fambox-*`** | 25 | — | 25 | FAMBOX 専用カスタム（最新ブランド整合済 or v0.2 反映候補） |
| **`fam-*`** | 33 | 20 | 53 | FAM 親ブランド系（過渡期 / 一部 FAMBOX 流用） |
| **`main-*`** | 20 | — | 20 | Dawn デフォルト（テンプレ駆動） |
| **`cart-*`** | 5 | — | 5 | カート関連 Dawn snippets/sections |
| **`image-*`** | 3 | — | 3 | Dawn 標準 |
| **`featured-*`** | 3 | — | 3 | Dawn 標準（商品 / コレクション / ブログ） |
| **`custom-*`** | 3 | — | 3 | アスリート voices / blog-carousel / 汎用 |
| **その他汎用** | 23 | 1 | 24 | header / footer / page / contact-form 等 |
| **総計** | **115** | **21** | **136** | |

## 役割別 ×刷新優先度（DS Phase B 観点）

### 🔴 High: DS v0.2 適用済 or 適用候補

| Section | 状況 | 備考 |
|---|---|---|
| `fambox-header.liquid` / `header.liquid` | Phase 2b 適用済 + v0.2.1 patch | 本日 GO 判定済（PR #2） |
| `fambox-modal.liquid` | v0.2 達成（Phase B-5 Token 化済） | Stat Card と同時達成 |
| `fambox-stat-grid.liquid` | v0.2 Stat Card 適用済 | OKR KR1-2 完成基準到達 |
| `fambox-footer.liquid` / `footer.liquid` | L4 Footer v0.2 適用済 | 3 variants + Ink background |
| `fambox-bento-grid.liquid` | L4 Bento Grid v0.2 適用済 | DNA 5 sizes + 12 col system |
| `fambox-faq.liquid` | bulk maintenance 適用済 | image_url width 1200 化済 |
| `fambox-contact-form.liquid` | OKR KR2-1 完成基準対応 | B2B 問合せ動線 |

### 🟡 Mid: FAMBOX 流用候補 / 部分修正

| Section | 状況 | DS Phase B 対応案 |
|---|---|---|
| `fambox-hero-v17.liquid` / `fambox-hero-v17-video.liquid` | v17 系（複数バージョン履歴あり） | v18 リファクタで Token 統一 |
| `fambox-active-plans.liquid` / `fambox-active-plans-v2.liquid` | v1 と v2 並存 | v2 へ統一 + v1 退役 |
| `fambox-case-study.liquid` / `fam-case-study.liquid` | FAMBOX 版を maintain / FAM 版は legacy | FAM 版を fambox-* へ吸収 |
| `fambox-blog-carousel.liquid` / `custom-blog-carousel.liquid` | 重複 | fambox-* へ統一 |
| `fambox-easy-cooking.liquid` | 単独使用 | DNA v0.5 対応の見直し |
| `fambox-interview.liquid` | 守屋選手企画で使用 | スティッキー CTA との連動確認 |
| `fambox-menu-showcase.liquid` | 食事診断後の提案 | 食事診断ウィザードとの連携 |
| `fambox-model-case.liquid` | 導入実績ページで使用 | tokusetsu-jisseki と連動 |
| `fambox-nutrition-service.liquid` | 大前さんアドバイザー紹介 | 写真 master 待ち |
| `fambox-plan-features.liquid` | プラン特徴 | コレクションタブと連動 |
| `fambox-profile.liquid` | スタッフ紹介 | DNA キャラクター単一/複数決定後に調整 |
| `fambox-spirit.liquid` / `fam-spirit.liquid` | FAMBOX / FAM 並存 | FAM 版退役方針 |
| `fambox-subscription-plan.liquid` | 定期便プラン | Seal Subscriptions と連動 |
| `fambox-value-proposition.liquid` | 価値訴求 | Messaging Pillar 確定後（A1-4）に文言更新 |
| `fambox-voice.liquid` | 利用者の声 | アスリート voices と統合検討 |
| `fambox-drawer.liquid` | SP drawer | header v0.2.1 と連動 |

### 🟢 Low: FAM 系 legacy（廃止 or 段階退役）

| Section | 状況 | 退役判断 |
|---|---|---|
| `fam-active-plans.liquid` / `fam-active-plans-v2.liquid` | FAM 専用 | fambox-* に移行後、廃止 |
| `fam-blog-hero.liquid` / `fam-blog-posts.liquid` | FAM ブログ | fam-jp.com 移行で再利用判断 |
| `fam-collection-plan.liquid` / `fam-collection-tabs.liquid` | コレクション系 | fambox-* との重複確認 |
| `fam-corp-*`（10 件: contact-channels / faq / features / hero / interview / issues / mission / nutrition-service / solution / steps / supervisor / text-block） | FAM 法人ページ用 | fam-jp.com 移行ターゲット |
| `fam-footer-test.liquid` / `fam-footer-v2.liquid` | テスト用 | 削除候補 |
| `fam-header-menu.liquid` | 親ブランドヘッダー | header v0.2 への統合 or 退役 |
| `fam-item.liquid` / `fam-item-plans.liquid` | FAM 専用商品 | fambox-* への置換 |
| `fam-nav.liquid` / `fam-nav-panels.liquid` | FAM ナビ | header v0.2 で置換 |
| `fam-plan-features.liquid` / `fam-solution.liquid` | FAM 専用 | fambox-* への置換 |
| `fam-sticky-cta.liquid` | スティッキー CTA | DS v0.2 button.md と整合 |
| `fam-subscription-plan.liquid` | FAM 定期便 | Seal と連動 / fambox-* へ統合 |
| `fam-voices.liquid` / `fam-voices-message.liquid` | FAM 利用者の声 | アスリート voices と統合 |
| `fam-achievement.liquid` | 実績表示 | 守屋企画と整合 |

### ⚪ Untouched: Dawn 標準（テンプレ駆動）

`main-*` 20 件 / `cart-*` 5 件 / `image-*` 3 件 / `featured-*` 3 件 / `announcement-bar` / `apps` / `bulk-quick-order-list` / `collage` / `collapsible-content` / `collection-list` / `contact-form` / `email-signup-banner` / `multicolumn` / `multirow` / `newsletter` / `page` / `pagefly-section` / `pickup-availability` / `predictive-search` / `quick-order-list` / `related-products` / `rich-text` / `slideshow` / `video` / `home-footer` / `main-password-header` / `main-password-footer`

→ 基本的に Dawn 標準のまま維持。DS 適用は Tokens CSS Liquid 化（Phase B）で全 sections に間接適用される。

## 役割別 重複・統合候補

| カテゴリ | 重複セット | 統合方向 |
|---|---|---|
| Hero | `fambox-hero-v17` / `fambox-hero-v17-video` / Dawn `image-banner` | `fambox-hero-v18`（DS Token 統一） |
| Active Plans | `fambox-active-plans` v1/v2 + `fam-active-plans` v1/v2 | `fambox-active-plans-v2` 単独 |
| Footer | `footer.liquid` / `fambox-footer.liquid` / `home-footer.liquid` / `fam-footer-test.liquid` / `fam-footer-v2.liquid` | `fambox-footer.liquid` 単独 |
| Spirit | `fambox-spirit` / `fam-spirit` | `fambox-spirit` 単独 |
| Case Study | `fambox-case-study` / `fam-case-study` | `fambox-case-study` 単独 |
| Blog Carousel | `fambox-blog-carousel` / `custom-blog-carousel` | `fambox-blog-carousel` 単独 |
| Voices | `fam-voices` / `fam-voices-message` / `fambox-voice` / `custom-athlete-voices` | DS pattern として整理 |

→ **統合により 136 sections → 推定 95〜100 sections に削減可能**（fam-jp.com 移行と連動）

## 不足項目

| 項目 | 必要性 | 取得方法 |
|---|---|---|
| 各 section のスクショ | High | Shopify Theme Customizer プレビューで個別取得（136 件 / 半日仕事） |
| 各 section の使用ページマップ | High | Shopify 管理画面 templates フォルダ確認 |
| 各 section の最終更新日 / 修正履歴 | Mid | git log で生成可能 |
| 「使われていない」死蔵 section 検出 | Mid | templates JSON 内の section 参照を grep |

## 次アクション

1. **本ファイル**を `fam-jp.com 移行` プロジェクトの `L0 翻訳表 v0.2` の基盤として参照
2. 重複統合の最優先（Footer / Active Plans / Hero v18）を OKR KR1-2 の Phase B 工程に組み込む
3. Dawn 標準は Phase B「Tokens」適用で間接対応

## 関連

- [MATERIALS_CHECKLIST.md M2](../MATERIALS_CHECKLIST.md#m2-現存-shopify-テーマ-セクション一覧--スクリーンショット)
- [L0 翻訳表 v0.1](../design-system/operations/L0-translation-table.md)（Phase A 完成済 412 行）
- [Section Refactor Helper skill](../../../.claude/skills/...) — 規律に沿ったリファクタを支援

## 変更履歴

- 2026-05-27: Initial inventory — 全 136 sections のカテゴリ分類 + 刷新優先度 + 統合候補（宮川 / Claude）
