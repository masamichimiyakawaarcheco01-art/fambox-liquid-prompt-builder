---
name: Seal Subscriptions 通知メール統一デザイン
description: Seal Subscriptions から配信される 12 種類の定期便通知メールを FAM ブランド DNA（Drive Orange / Ink / ライト基調 / Editorial×Lab）で統一刷新するための設計書。
type: design-spec
status: draft
created: 2026-04-22
author: 宮川真道（ARCHECO）/ Claude
target_app: Seal Subscriptions（Shopify）
target_store: FAMBOX・FAMアスリート食トレ
related:
  - brand/FAM_brand_DNA_v0.5.md
  - .claude/skills/fambox-design/references/01-tokens.md
  - .claude/skills/fambox-design/references/03-components.md
---

# Seal Subscriptions 通知メール統一デザイン設計書

## 1. 目的 / ゴール

### 1.1 体験ゴール
**定期便の顧客が、どのメールを受け取っても "FAM からの便り" と一瞬で分かり、継続・スキップ・解約・決済の判断を安心して行えること。**

### 1.2 具体的な改善項目（現状課題）
現行 Seal デフォルトメールの問題：
- ① **ブランドが無い**：ロゴ無し、色無し、書体は端末依存
- ② **英語混在**：`This e-mail was sent to you to remind you about the upcoming charge...` がそのまま残る
- ③ **金額表記が冷たい**：`950.00 JPY` のような小数点2桁＋スペース＋通貨コードは日本の EC で違和感
- ④ **文言が事務的**：「定期購買の決済が正常に実行されましたのでご通知いたします」が無機質
- ⑤ **背景色が端末依存**：ダークモード時に文字が潰れる／明度が不安定
- ⑥ **CTAボタンが非ブランド**：Seal 既定のスカイブルーは FAM ではない

### 1.3 非目標（やらないこと）
- Shopify 標準通知（注文確認・配送通知）の刷新 → 別案件
- Shopify Email を使ったマーケティング配信（ニュースレター）→ 別案件
- Apple Wallet / LINE 等のチャネル連携 → 別案件

---

## 2. 対象メール一覧（12 種類）

| # | 種別（日本語） | Seal 管理画面の名称 | トリガー | 優先度 |
|---|---|---|---|---|
| 1 | 定期便開始のお礼 | Subscription created | 初回決済＋定期便登録 | ★★★ |
| 2 | 次回発送予告リマインド | Upcoming billing reminder | 決済 N 日前（Seal 設定に従う） | ★★★ |
| 3 | 決済完了／注文確定 | Billing attempt succeeded | 自動決済成功 | ★★★ |
| 4 | 決済失敗のお知らせ | Billing attempt failed | カード決済失敗 | ★★★ |
| 5 | 一時停止を受け付けました | Subscription paused | お客様 or 管理者が Pause | ★★ |
| 6 | 定期便を再開しました | Subscription resumed | Resume 操作 | ★★ |
| 7 | 解約を受け付けました | Subscription cancelled | Cancel 操作 | ★★★ |
| 8 | スキップを受け付けました | Subscription skipped | Skip 操作 | ★★ |
| 9 | 期間満了のお知らせ | Subscription expired | 契約期間終了 | ★ |
| 10 | まもなく発送します | 24h before fulfillment | 発送 24h 前 | ★★ |
| 11 | お届け先を変更しました | Shipping address updated | 住所更新 | ★ |
| 12 | お支払い方法を変更しました | Payment method updated | 決済情報更新 | ★ |

**★★★ = コア体験 4 種（開始・予告・成功・失敗・解約）**。この 5 通はコピー・画像・CTA まで作り込む。
★★ = 確認系。コピーは定型、デザインは共通パーツ流用。
★ = 追加系。同上。

---

## 3. 全メール共通デザイン仕様

### 3.1 カラー（FAM DNA から抽出）

メール内では **8 色のみ使用**（fambox-design の tokens からメール用サブセット）。

| 用途 | 色 | HEX |
|---|---|---|
| 本文テキスト | Ink | `#1B1D1A` |
| サブテキスト | Sub | `#545655` |
| キャプション・注釈 | Caption | `#888888` |
| プライマリ CTA／アクセント線 | Drive Orange | `#FB4C15` |
| 成功ステータス | Success | `#10B981` |
| 警告ステータス（決済失敗） | Error | `#DC2626` |
| 背景・面 | White / Off-White | `#FFFFFF` / `#FAFAFA` |
| 区切り線 | Border | `#ECECEC` |

**ダークモード対策**：背景は `#FFFFFF` 固定＋インラインCSSで `color-scheme: light;` 指定。Gmail/Apple Mail のダーク反転で潰れないよう、ロゴは背景と十分なコントラストを持つ単色 PNG を使用。

### 3.2 タイポグラフィ

Web フォントは使えないため、システムフォント＋フォールバック。

```css
/* 日本語 */
font-family: 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', 'Yu Gothic UI', 'Meiryo', 'Noto Sans JP', sans-serif;

/* 英数字（金額、日付、注文番号） */
font-family: 'Helvetica Neue', 'Arial', 'Hiragino Kaku Gothic ProN', sans-serif;
```

サイズスケール（メール専用に縮小）：

| 用途 | PC/SP | weight | line-height |
|---|---|---|---|
| 大見出し（H1） | 24px | 600 | 1.45 |
| 見出し（H2） | 18px | 600 | 1.5 |
| 本文 | 15px | 400 | 1.7 |
| サブ・注釈 | 13px | 400 | 1.7 |
| キャプション | 12px | 400 | 1.6 |
| ボタン文言 | 15px | 600 | 1 |
| 金額（強調） | 20px | 600 | 1.2 |
| 英字ラベル（SUBSCRIPTION / ORDER など） | 11px | 600 | 1 / letter-spacing 0.15em |

ロゴ部分だけは Poppins の視覚印象を**画像 PNG**で再現する。

### 3.3 レイアウト寸法

```
[viewport 全体 = #FAFAFA 背景]
│
│ padding-top: 32px
│
│ ┌──────────────── email container (max-width: 600px, margin: 0 auto) ─┐
│ │  bg: #FFFFFF
│ │  border-radius: 0（メールクライアント互換重視）
│ │
│ │  ┌─ Header (padding: 32px 32px 24px) ─────────────────────────────┐
│ │  │  [ FAMBOX ロゴ  高さ 28px 中央配置 ]                             │
│ │  └────────────────────────────────────────────────────────────────┘
│ │
│ │  ┌─ Drive Orange 4px アクセント帯 (width:100%, height:4px) ────────┐
│ │  │  bg: #FB4C15                                                    │
│ │  └────────────────────────────────────────────────────────────────┘
│ │
│ │  ┌─ Hero Block (padding: 40px 32px 24px) ─────────────────────────┐
│ │  │  [ 英字 eyebrow: SUBSCRIPTION / ORDER / REMINDER など ]          │
│ │  │  [ H1: 「定期便の決済が完了しました」（24px bold） ]              │
│ │  │  [ lead: 「マサミチ ミヤカワ様 いつもありがとうございます…」]      │
│ │  └────────────────────────────────────────────────────────────────┘
│ │
│ │  ┌─ CTA Primary (padding: 0 32px 32px) ───────────────────────────┐
│ │  │  [ Drive Orange ボタン：定期便の管理はこちら → ]                 │
│ │  └────────────────────────────────────────────────────────────────┘
│ │
│ │  ┌─ Info Card （注文内容／次回配送／ステータス詳細） ────────────────┐
│ │  │  bg: #FAFAFA, padding: 24px, border-radius: 8px                 │
│ │  │  [ ラベル ][ 値 ]  のテーブル                                    │
│ │  │  [ 商品行 ]                                                     │
│ │  │  [ 小計・送料・合計 ]                                            │
│ │  └────────────────────────────────────────────────────────────────┘
│ │
│ │  ┌─ 補助リンク群 ─────────────────────────────────────────────────┐
│ │  │ [ スキップ・一時停止はマイページから ] (subtle link)              │
│ │  └────────────────────────────────────────────────────────────────┘
│ │
│ │  ┌─ Divider (1px #ECECEC, margin: 32px) ──────────────────────────┘
│ │
│ │  ┌─ Footer (padding: 24px 32px 40px) ─────────────────────────────┐
│ │  │  [ 会社名・住所・問い合わせ先 ]                                  │
│ │  │  [ プライバシーポリシー ｜ 特商法 ｜ お問い合わせ ]                │
│ │  │  [ © 2026 ARCHECO Inc. ]                                        │
│ │  └────────────────────────────────────────────────────────────────┘
│ └────────────────────────────────────────────────────────────────────┘
│
│ padding-bottom: 40px
```

**SP**：`max-width: 600px` のコンテナがそのまま縮小。横 padding を 32px → 20px、H1 を 24px → 22px、本文 15px → 14px に切り替え（メディアクエリ対応クライアントのみ）。対応外のクライアントでも破綻しないよう、600px 基準で設計。

### 3.4 共通 UI コンポーネント仕様

#### 3.4.1 ヘッダー（ロゴブロック）
- ロゴ画像：`LMLT_FAMBOX_Black.png` を Shopify Files にアップして CDN URL 参照
- 高さ **28px**、中央配置
- 周囲 padding `32px 32px 24px`
- ロゴ下 **4px の Drive Orange 帯**で FAM の存在証明

#### 3.4.2 CTA プライマリボタン
```
bg: #FB4C15（Drive Orange）
color: #FFFFFF
padding: 16px 32px
font: 15px / 600 / letter-spacing 0.02em
border-radius: 4px   ← メール互換のため pill ではなく sm
display: inline-block
text-decoration: none
```
- Outlook 対応の bulletproof button（VML＋テーブルラッパ）で実装
- ホバーエフェクトはメールでは使えないので固定デザイン

#### 3.4.3 情報カード
```
bg: #FAFAFA
padding: 24px
border-radius: 8px
内部は <table>（Outlook 対応）で構成
行間に 1px #ECECEC の区切り線
```

#### 3.4.4 商品行
```
[商品画像 64x64 border-radius:8px] | [商品名 15px/600, バリエーション 13px/regular #888] | [数量 13px] | [金額 15px/600]
```
※ 商品画像は Liquid 変数 `{{ line_item.image }}` を `width:128px&height:128px&crop=center` で取得

#### 3.4.5 金額表記
**統一ルール**：
- `950.00 JPY` → `¥950`
- `1,088.00 JPY` → `¥1,088`
- 3 桁カンマ区切り、`¥` は半角、小数点は常に削除
- Liquid フィルタで `{{ total_price | money_without_trailing_zeros }}` を使い、必要なら `| replace: '¥', '¥'` で半角統一

#### 3.4.6 ステータス Pill（採用メール：決済完了／失敗／解約／再開など）
```
小さなピル型ラベル：
- Success:  bg: rgba(16,185,129,0.12)  color: #0B7D59  text: "決済完了"
- Warning:  bg: rgba(245,158,11,0.12)  color: #92661C  text: "要対応"
- Error:    bg: rgba(220,38,38,0.12)   color: #B4261F  text: "決済失敗"
- Info:     bg: rgba(61,184,232,0.12)  color: #1A6F93  text: "受付完了"

padding: 4px 12px, border-radius: 9999px, font: 11px/600, letter-spacing:0.08em
```

#### 3.4.7 補助リンク群
定期便管理 CTA の下に、二次導線をテキストリンクで3本並べる：
- マイページで**スキップ**する
- マイページで**一時停止**する
- **解約**する

色は `#545655`、下線あり、font-size 13px。

#### 3.4.8 フッター
- 会社名（株式会社ARCHECO／ブランド名：FAMBOX・FAMアスリート食トレ）
- 住所
- 問い合わせメールアドレス（現行 `fam.athletefood.frozen@gmail.com` → 独自ドメイン化は別途課題）
- リンク 3 つ：プライバシーポリシー／特定商取引法／お問い合わせ
- コピーライト `© 2026 ARCHECO Inc.`
- unsubscribe リンク（Seal 自動生成の `{{ unsubscribe_link }}`）

---

## 4. メール種別ごとの差分仕様

### 4.1 共通構造
すべてのメールは **同じ共通パーツ**を使う。差分は以下 6 項目のみ：

1. **件名（Subject）**
2. **プリヘッダー**（受信箱プレビュー用、非表示テキスト）
3. **Eyebrow（英字ラベル）**
4. **H1（大見出し）**
5. **Lead（導入文）**
6. **CTA ラベル＋遷移先**
7. **情報カードの中身**（注文内容 or 次回日時 or ステータス）
8. **ステータス Pill の色・文言**

### 4.2 各メールのコピー雛形

#### ① 定期便開始のお礼（Subscription created）
- **件名**：`【FAMBOX】ようこそ。あなたの食習慣、はじまります。`
- **プリヘッダー**：`{{ customer.first_name }} 様、定期便のご登録ありがとうございます。`
- **Eyebrow**：`SUBSCRIPTION STARTED`
- **H1**：`ようこそ、FAM のコミュニティへ。`
- **Lead**：
  > {{ customer.first_name }} 様
  > このたびは FAMBOX の定期便をお選びいただきありがとうございます。
  > 管理栄養士監修の食事を、あなたの日常に無理なく届けます。
  > 初回のお届け予定日と、定期便の管理方法をご案内いたします。
- **CTA**：`定期便の管理はこちら →`
- **情報カード**：初回配送日／次回決済日／プラン内容／小計・送料・合計
- **ステータス Pill**：`Info・ご登録完了`

#### ② 次回発送予告リマインド（Upcoming billing reminder）
- **件名**：`【FAMBOX】{{ next_order_date }} にお届けします（スキップ・変更は本日中に）`
- **プリヘッダー**：`次回のお届けまであと N 日。内容の変更・スキップは本日が目安です。`
- **Eyebrow**：`UPCOMING ORDER`
- **H1**：`次回のお届け、準備を始めています。`
- **Lead**：
  > {{ customer.first_name }} 様
  > 次回の定期便を {{ next_order_date }} にお届け予定です。
  > 配送内容の変更・スキップ・お休みは、**{{ cutoff_date }} まで**にマイページからお手続きください。
- **CTA**：`配送内容を確認する →`
- **補助リンク強調**：スキップ／一時停止／数量変更
- **情報カード**：次回お届け日／次回決済予定額／内容物
- **ステータス Pill**：`Warning・要確認`

#### ③ 決済完了／注文確定（Billing attempt succeeded）← 今回のリファレンス
- **件名**：`【FAMBOX】今回のご注文が確定しました（注文 #{{ order.number }}）`
- **プリヘッダー**：`定期便の決済が完了し、まもなく発送準備に入ります。`
- **Eyebrow**：`ORDER CONFIRMED`
- **H1**：`今回のご注文が確定しました。`
- **Lead**：
  > {{ customer.first_name }} 様
  > いつも FAMBOX をご利用いただきありがとうございます。
  > 定期便の決済が完了しましたので、ご案内いたします。
  > 発送準備が整い次第、追跡番号つきの配送通知をお送りします。
- **CTA**：`定期便の管理はこちら →`
- **情報カード**：注文番号／商品／小計／送料／合計
- **ステータス Pill**：`Success・決済完了`

#### ④ 決済失敗（Billing attempt failed）
- **件名**：`【FAMBOX・重要】お支払いができませんでした。お届けのため情報更新をお願いします`
- **プリヘッダー**：`カード情報をご確認のうえ、{{ retry_date }} までに更新をお願いします。`
- **Eyebrow**：`ACTION REQUIRED`
- **H1**：`お支払いの確認ができませんでした。`
- **Lead**：
  > {{ customer.first_name }} 様
  > 申し訳ございません。本日の定期便のお支払いが完了できませんでした。
  > カードの有効期限・限度額・残高をご確認のうえ、情報を更新いただけますと幸いです。
  > {{ retry_date }} までに更新がない場合、今回のお届けを見送らせていただきます。
- **CTA**：`お支払い方法を更新する →`（遷移先：Seal customer portal / payment method）
- **ステータス Pill**：`Error・お支払い未完了`
- **装飾**：ヘッダー下のアクセント帯を Drive Orange ではなく **#DC2626 に差し替え**て注意喚起

#### ⑤ 解約を受け付けました（Subscription cancelled）
- **件名**：`【FAMBOX】解約のお手続きを承りました`
- **Eyebrow**：`SUBSCRIPTION CANCELLED`
- **H1**：`解約のお手続きを承りました。`
- **Lead**：
  > {{ customer.first_name }} 様
  > FAMBOX をご利用いただき、誠にありがとうございました。
  > 定期便の解約を承りました。今後のお届けは停止いたします。
  > もしまた食習慣を整えたくなったら、いつでも戻ってきてください。
- **CTA**：`もう一度 FAMBOX を試す →`（遷移先：商品ページ）
- **ステータス Pill**：`Info・解約完了`
- **装飾**：アクセント帯は Drive Orange のまま（縁を切らない思想）

#### ⑥ 一時停止／再開／スキップ／住所更新／支払方法更新
定型の受付完了メール。**共通パーツをそのまま使い、H1 と Lead、ステータス Pill だけ差し替え**。

| 種別 | H1 | Pill |
|---|---|---|
| Paused | 一時停止を承りました。 | Info・停止中 |
| Resumed | 定期便を再開しました。 | Success・再開完了 |
| Skipped | 次回のお届けをスキップしました。 | Info・スキップ完了 |
| Shipping updated | お届け先を変更しました。 | Info・変更完了 |
| Payment updated | お支払い方法を変更しました。 | Success・更新完了 |
| Expired | 契約期間が満了しました。 | Info・満了 |
| 24h before fulfillment | まもなく発送します。 | Info・発送準備中 |

---

## 5. 技術仕様

### 5.1 レンダリング方針
- **テーブルレイアウト**ベース（`<table role="presentation" cellpadding="0" cellspacing="0" border="0">`）
- すべてのスタイルは **インライン** `style=""`
- 先頭に MSO コメント条件分岐で Outlook 専用 CSS を入れる
- `<img>` には必ず `alt`・`width`・`height`・`style="display:block; border:0; outline:none;"`
- ボタンは bulletproof button パターン（VML＋インナーテーブル）

### 5.2 Liquid 変数（Seal が提供するもの）
主要な変数（Seal のプレビュー機能で確認可）：
- `{{ customer.first_name }}` / `{{ customer.last_name }}` / `{{ customer.email }}`
- `{{ subscription.id }}` / `{{ subscription.status }}`
- `{{ subscription.manage_url }}` — マイページリンク
- `{{ next_order_date }}` / `{{ next_charge_date }}`
- `{{ line_items }}` — 商品配列、`{ title, quantity, price, image, variant_title }`
- `{{ order.number }}` / `{{ order.total_price }}`
- `{{ shop.name }}` / `{{ shop.address }}` / `{{ shop.email }}`
- `{{ unsubscribe_link }}`

**実装時に Seal プレビューで全変数の実値を確認し、存在しないものはハードコードする方針**。

### 5.3 金額の Liquid フォーマッタ
```liquid
{%- assign yen = amount | money_without_currency | replace: '.00', '' -%}
¥{{ yen }}
```
または Shopify 標準の `{{ amount | money_without_trailing_zeros }}` が使えれば優先。

### 5.4 画像ホスティング
- ロゴ：`LMLT_FAMBOX_Black.png`（黒・横組）を Shopify Admin > Settings > Files にアップし、取得した CDN URL（例：`https://cdn.shopify.com/s/files/1/XXXX/files/LMLT_FAMBOX_Black.png`）をテンプレートにハードコード
- 同ロゴ Retina 用に **@2x（56px 高さ相当）画像**をアップし、`srcset` ではなくただ大きめをダウンスケール表示（`width="120" height="28"`）
- 商品画像は Liquid 変数から自動（`{{ line_item.image | img_url: '128x128', crop: 'center' }}`）

### 5.5 ダークモード対策
- 最外コンテナに `style="color-scheme: light; supported-color-schemes: light;"`
- ロゴは**単色黒のみ**（透過 PNG）— Apple Mail / iOS Mail のダーク反転で自動的に白抜きされる
- 本文コンテナを `background:#FFFFFF !important` で明示固定
- `<meta name="color-scheme" content="light">`

### 5.6 アクセシビリティ
- セマンティックな見出し（H1 は 1 回のみ）
- リンクは下線＋色コントラスト AA 以上
- 画像には意味のある `alt`（装飾のみなら `alt=""`）
- ボタンは `role="button"` ＋十分なタップ領域 44x44 以上
- メール全体に `lang="ja"`

---

## 6. 実装ファイル構成

```
projects/fambox/emails/seal/
├── README.md                          ← Sealへの貼り付け手順、検証手順、Liquid変数対応表
├── _partials/                         ← 貼り付け前の共通パーツ（人間用の管理、Sealにはコピペで埋め込む）
│   ├── header.html
│   ├── hero-block.html
│   ├── cta-button.html
│   ├── info-card.html
│   ├── line-item-row.html
│   ├── status-pill.html
│   ├── divider.html
│   └── footer.html
├── 01-subscription-created.html
├── 02-upcoming-reminder.html
├── 03-billing-succeeded.html          ← 最優先。既存リファレンス
├── 04-billing-failed.html
├── 05-subscription-paused.html
├── 06-subscription-resumed.html
├── 07-subscription-cancelled.html
├── 08-subscription-skipped.html
├── 09-subscription-expired.html
├── 10-fulfillment-24h.html
├── 11-shipping-updated.html
└── 12-payment-method-updated.html
```

**理由**：Seal の管理画面にはパーシャル共有機能がない。なのでローカルでは「部品単位」で管理しつつ、実際に Seal にコピペする最終 HTML は各メール独立ファイル。共通パーツを修正したら、全 12 ファイルにも反映して再貼付する運用。

---

## 7. 検証（テスト観点）

### 7.1 レンダリング検証（最低限）
- Gmail（Web、iOS、Android）
- Apple Mail（macOS、iOS）
- Outlook（Web、Windows、Mac）
- Yahoo Mail
- Thunderbird

**ツール**：[Email on Acid](https://www.emailonacid.com/) or [Litmus](https://litmus.com/) または Seal のプレビュー機能＋実送信で自社内テスト。

### 7.2 機能検証
- Liquid 変数が全て正しく描画される（名前、日付、金額、商品、URL）
- CTA クリックで正しいマイページに遷移する
- unsubscribe リンクが動作する
- ダークモード／ライトモード両方で可読
- 画像ブロック環境（Outlook デフォルト）でも意味が伝わる
- 日本語長文で折返しが不自然にならない
- 迷惑メール判定されない（SPF/DKIM は Shopify 側依存、本設計の範囲外だが件名の絵文字乱用・大文字多用を避ける）

### 7.3 コピー品質検証
- 宮川さん／運用者の目視確認
- 最優先 5 通（①②③④⑦）は社内で誰かに実受信→読み聞かせでトーン確認
- 薬機法・景表法の問題となる表現がないか（医療系は特に注意）

---

## 8. オープン項目（実装プラン段階で確定する）

1. **問い合わせメールアドレス**：現行 `fam.athletefood.frozen@gmail.com` のままでいいか、独自ドメインに置き換えるか
2. **会社住所・特商法 URL・プラポリ URL** の正式文字列
3. **unsubscribe リンクの Liquid 変数名**（Seal プレビューで確認）
4. **定期便管理ページ（マイページ）の URL 構造**（Seal customer portal のドメイン）
5. **ロゴの CDN URL**（Shopify Files にアップ後に確定）
6. **配送カットオフ日（{{ cutoff_date }}）** の Seal 変数での取り方、または店舗ルールで固定値にするか
7. **ブランドボイス**：今回の文案はドラフト。宮川さん／社内で 1 回トーン調整を入れる前提
8. **FAMBOX と FAMアスリート食トレ の出し分け**：商品に応じて件名のブランド名・ロゴを分岐させるか、ストア単位で別テンプレを持つか

---

## 9. 参考資料

- `brand/FAM_brand_DNA_v0.5.md` — FAM ブランド DNA v0.5（Drive Orange / Editorial×Lab / ライト基調）
- `.claude/skills/fambox-design/references/01-tokens.md` — FAM BOX デザイントークン
- `.claude/skills/fambox-design/references/03-components.md` — コンポーネント仕様
- [Seal Subscriptions – Where can I edit the email notification template?](https://www.sealsubscriptions.com/articles/frequently-asked-questions/where-can-i-edit-the-email-notification-template-1x)
- [Shopify Help Center – Customizing email notification templates](https://help.shopify.com/en/manual/fulfillment/setup/notifications/customizing-notification-template)
- [Shopify Help Center – Notifications variables reference](https://help.shopify.com/en/manual/fulfillment/setup/notifications/email-variables)

---

## 10. 承認チェック

- [ ] 対象メール 12 種類の洗い出しが十分か
- [ ] カラー・タイポ・レイアウトが FAM DNA に準拠しているか
- [ ] 文言ドラフトのトーンが宮川さんの意図と合致するか
- [ ] 金額表記・英語日本語化・ロゴ挿入・背景色の 4 大課題がすべてカバーされているか
- [ ] 実装ファイル構成と運用フロー（共通パーツ→各メール貼り付け）に無理がないか
- [ ] 検証観点（メールクライアント互換）が現実的か

**承認 → `writing-plans` スキルで実装プランを作成 → 実装 → 検証 → Seal 管理画面に投入**
