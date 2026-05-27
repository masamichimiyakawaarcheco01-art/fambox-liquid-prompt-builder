---
title: FAMBOX 出荷 SLA / 自動送信メール定型文
date: 2026-05-25
tags: [fambox, sla, shipping, customer-communication, transactional-email, voice-and-tone]
status: active
priority: high
source:
  - projects/fambox/emails/shopify/01-order-confirmation.html (commit 996707e)
  - 注文確認メール SHIPPING SCHEDULE ブロック
related:
  - ../../brand/fambox/STRATEGY.md
  - ../../projects/fambox/emails/shopify/
  - ../30_Tech_Notes/fambox-audit-suite-design.md
---

# FAMBOX 出荷 SLA / 自動送信メール定型文

顧客対応・CS・新規トランザクショナルメール作成時に **必ず参照する固定情報**。文言の揺れを防ぐため、ここに集約しておく。

## 1. 出荷リードタイム（公式 SLA）

| 区間 | 期間 | 起算ルール |
|---|---|---|
| 注文 → 発送 | **3 営業日**（土日祝を除く） | **翌営業日**から起算 |
| 発送 → お届け | **1〜2 日**（目安） | 配送業者依存（地域差あり）|

### 顧客向け定型文（注文確認メール本文）

> 商品は、ご注文の翌営業日から起算して、3営業日（土日祝を除く）で発送いたします。発送後は、通常1〜2日でのお届けが目安です。

### Preheader / プッシュ通知向け短縮形

> ご注文 {{ name }} を承りました。翌営業日から起算して3営業日（土日祝を除く）で発送いたします。

## 2. メール内ラベル / マークアップ規約

注文確認メールの「発送について」ブロックは以下の固定スタイルで実装する（DS Token 未対応の HTML メール用 inline スタイル）:

```
ラベル: "SHIPPING SCHEDULE"
  font: 'Helvetica Neue', Arial, sans-serif
  size: 11px
  weight: 600
  letter-spacing: 0.15em
  color: #FB4C15 (Drive orange)

見出し: "発送について"
  font: 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', sans-serif
  size: 14px
  weight: 600
  color: #1B1D1A (Ink)

本文:
  size: 14px
  weight: 400
  line-height: 1.8
  color: #545655

枠線: 左 3px solid #FB4C15
背景: #FAFAFA on white card
border-radius: 4px
```

## 3. 問合せ先 / 自動送信メール明示

すべての自動送信メールのフッターには以下を含める:

```
ご不明な点がございましたら、fam.athletefood.frozen@gmail.com までお問い合わせください。

このメールは自動送信されています。
ご返信いただいてもお答えできない場合がございます。
```

問合せ先メールアドレス: **fam.athletefood.frozen@gmail.com**

## 4. ブランド文言ルール（このトピックでの注意）

- ❌ 「発送準備が整い次第、改めてご連絡いたします。」 — **使わない**（リードタイムが曖昧で顧客の不安を招く）
- ✅ 翌営業日起算 3 営業日（土日祝を除く） — **常に明記**
- ✅ 「目安です」と書くことで配送業者依存の遅延に対する期待値調整を行う

## 5. 適用範囲

このSLAは以下のメール・チャネルで一貫運用する:

- 注文確認メール（01-order-confirmation.html）
- 出荷確認メール（02-shipping-confirmation.html）— 発送日確定後に自動送信
- 商品詳細ページの「お届けについて」セクション
- FAQ「いつ届きますか?」項目
- CS 個別返信のテンプレート

## 6. SLA 変更時のチェックリスト

リードタイムを変更する場合は以下を **同時更新**:

- [ ] `projects/fambox/emails/shopify/01-order-confirmation.html`（SHIPPING SCHEDULE ブロック）
- [ ] `projects/fambox/emails/shopify/02-shipping-confirmation.html`
- [ ] 商品詳細ページ ([fam-item.liquid](../../sections/fam-item.liquid)) 「お届けについて」
- [ ] FAQ section ([fambox-faq.liquid](../../sections/fambox-faq.liquid))
- [ ] 当ファイル（fambox-shipping-sla.md）
- [ ] CS テンプレ（Seal Subscriptions メール群）

---

## 出典

- **commit 996707e** — feat(email): add SHIPPING SCHEDULE block to order confirmation (2026-05-25)
- 旧文言「発送準備が整い次第、改めてご連絡いたします。」を廃止し、リードタイム明示型に統一
