---
title: FAMBOX Component — Contact Form
type: design-system
layer: L4-Components
component: ContactForm
version: 0.3
status: confirmed
last_updated: 2026-04-27
owner: 宮川
deadline: 2026-08-28〜2026-08-31（OKR Task 2-1-c）
source: Worksheet §12（2026-04-20 確定 + 2026-04-27 S3 拡張：電話番号 任意→必須 / 利用検討時期 追加）
brand_alignment:
  - Integrity（誠実）: 過度な必須化を避け、ユーザー負担を最小化
  - Co-driven（対等）: 「お客様」表現を排除し対等トーン
  - 共創者: 自動返信メールの語尾で対等性を担保
related:
  - input.md
  - form-field.md
  - tokens/colors.md
  - cta-wording-proposal.md
---

# Contact Form — Component

## 概要
FAMBOX の主要リード獲得 Component。**OKR Task 2-1-c で 8月末期限**。Brand DNA を体験で伝える最重要接点のひとつ。

## ブランド整合性
- **Integrity**: 必須項目を厳選（11項目・うち1任意）し、Submit完了率を確保
- **Co-driven**: 「お客様」用法を排除、自動返信メールも対等トーン
- **Anti**: 「無料相談」「今すぐ」等の煽り文言を回避

---

## フィールド構成（Worksheet §12 Q1 確定 / 2026-04-27 拡張）

### 必須/任意の振分（11項目）

| # | フィールド | 入力タイプ | 必須/任意 | 用途・理由 |
|---|---|---|---|---|
| 1 | 会社名・団体名 | text | **必須** | B2B基本情報 |
| 2 | 競技・種目 | text | **必須** | リード品質判定の核 |
| 3 | お名前 | text | **必須** | 連絡時の呼びかけ |
| 4 | 役職 | select | **必須** | ターゲット階層判定（8選択肢） |
| 5 | メール | email | **必須** | 連絡手段・基本 |
| 6 | 電話番号 | tel | **必須** ★2026-04-27 任意→必須 | 緊急時の連絡手段確保 |
| 7 | 選手数・チーム規模 | select | **必須** | プラン提案精度 |
| 8 | 問合せ種別 | radio | **必須** | 営業フロー振分 |
| 9 | 問合せ内容（自由記述） | textarea | **必須** | 文脈把握（500字目安）|
| 10 | **利用検討時期** ★2026-04-27 追加 | select | 任意 | リード温度判定（営業優先度） |
| 11 | プライバシーポリシー同意 | checkbox | **必須** | 法的必須 |

### 各フィールドの選択肢

#### #4 役職（select）
```
- 監督
- コーチ
- 専属栄養士
- マネージャー
- 学校・クラブ事務局
- 選手本人
- 保護者
- その他
```

#### #7 選手数・チーム規模（select）
```
- 〜10名
- 11〜30名
- 31〜50名
- 51〜100名
- 101名以上
```

#### #8 問合せ種別（radio）
```
- 資料を見たい（資料DL希望）
- 一度話を聞いてみたい（相談希望）
- 試食してみたい（サンプル希望）
- その他（自由記述）
```

#### #10 利用検討時期（select / 任意）★2026-04-27 正式採用
```
- すぐ
- 1か月以内
- 3か月以内
- 未定
```

### 不採用（要判断済）
- ✕ 「予算感」（select）— 圧迫感あり・Anti違反（2026-04-20 不採用）

---

## 画面遷移（Worksheet §12 Q2 確定）

**🎯 確定: 同画面 inline 確認 → 送信後に Success 画面**

### フロー
```
[1] 入力画面（同画面）
      ↓ 「内容を確認する」ボタン
[2] 確認画面（同画面に展開・readonly表示）
      ↓ 「送信する」or「修正する」
[3] Success 画面（別ページ /thanks）
```

### 理由
- ページ遷移コストを下げる（離脱防止）
- 確認後の戻りも同画面なら摩擦少ない
- Success 画面のみ別ページで完了感・GTM測定容易

### 画面構造（HTML疑似コード）
```html
<form class="contact-form" id="contactForm">
  <!-- 入力フェーズ -->
  <div class="contact-form__step contact-form__step--input is-active">
    <h2 class="text-h2">お問い合わせ</h2>
    <p class="text-body">通常24時間以内にご返信いたします。</p>
    <!-- 各 form-field -->
    <button type="button" class="btn btn-primary btn-lg" id="reviewBtn">
      内容を確認する
    </button>
  </div>

  <!-- 確認フェーズ -->
  <div class="contact-form__step contact-form__step--review" hidden>
    <h2 class="text-h2">内容のご確認</h2>
    <!-- readonly 表示 -->
    <div class="action-row">
      <button type="button" class="btn btn-ghost" id="editBtn">修正する</button>
      <button type="submit" class="btn btn-primary btn-lg">送信する</button>
    </div>
  </div>
</form>
```

---

## 自動返信メール（Worksheet §12 Q3 確定）

**🎯 確定: カスタム自動返信（FAMBOXトーンで作成）**

### 件名
```
【FAMBOX】お問い合わせを承りました
```

### 本文（テンプレート）
```
{{ name }}様

このたびはFAMBOXへお問い合わせいただきありがとうございます。
内容を確認のうえ、24時間以内（営業日）に担当者よりご連絡いたします。

【お問い合わせ内容】
- 会社名・団体名: {{ company }}
- 競技・種目: {{ sport }}
- 役職: {{ role }}
- 選手数・チーム規模: {{ team_size }}
- 問合せ種別: {{ inquiry_type }}
- ご相談内容:
{{ message }}

急ぎのご相談がございましたら、下記までお気軽にご連絡ください。
[メールアドレス] / [電話番号]

---
アスリートと共に走る、栄養戦略のチーム。
FAMBOX
[サイトURL]
```

### トーン設計のポイント
- 冒頭「ありがとうございます」は1行で簡潔に（Brand DNA L5-6 準拠）
- 「いたします」を過度に重ねない
- 結びの一言「アスリートと共に走る〜」で **共創者** を体現
- 「お客様」表現は使わない（「{{ name }}様」のみ）

### Shopify実装
- Shopify標準の自動返信は Settings > Notifications で編集
- Liquid テンプレートで `{{ form.author }}` `{{ form.body }}` 等を活用
- 件名のテンプレ化必須

---

## バリデーションルール

| フィールド | ルール | エラーメッセージ |
|---|---|---|
| 会社名・団体名 | 必須・1〜100字 | 会社名・団体名をご入力ください |
| 競技・種目 | 必須・1〜50字 | 競技・種目をご入力ください |
| お名前 | 必須・1〜50字 | お名前をご入力ください |
| 役職 | 必須・select選択 | 役職をご選択ください |
| メール | 必須・正規メール形式 | 正しいメールアドレスをご入力ください |
| 電話番号 | **必須**・数字とハイフンのみ・10〜13文字 | 半角数字とハイフンでご入力ください（例: 03-1234-5678） |
| 選手数 | 必須・select選択 | 選手数をご選択ください |
| 問合せ種別 | 必須・radio選択 | 問合せ種別をお選びください |
| 問合せ内容 | 必須・10〜500字 | 10字以上500字以内でご入力ください |
| 利用検討時期 | 任意・select | （省略可） |
| 同意 | 必須・チェック | プライバシーポリシーにご同意ください |

実装は [form-field.md](form-field.md) の onBlur 即時バリデーション準拠。

---

## CTA 文言（cta-wording-proposal.md 連動）

| 状態 | 文言 |
|---|---|
| 入力フェーズ Primary | **内容を確認する** |
| 確認フェーズ Primary | **送信する** |
| 確認フェーズ Secondary | **修正する**（Ghost） |
| Success画面 Primary | **TOPに戻る** |
| Success画面 Secondary | **事例を見る** |

※ Hero CTA「話を聞いてみる」は Contact Form への動線文言、フォーム内では「送信する」等の機能語に切り替え。

---

## レイアウト仕様

| 項目 | 値 |
|---|---|
| Container | `--container-narrow`（1200px） |
| Form 最大幅 | 640px（中央寄せ） |
| FormField 間隔 | `--space-3`（24px） |
| Section 間隔 | `--space-5`（48px） |
| Submit ボタン | `--space-4`（32px）上余白 |

### モバイル
- Form 全幅（左右 16px padding）
- ボタン全幅
- Select は OS ネイティブ UI 利用

---

## Accessibility

- ✅ 全フィールドに `<label>` 紐付け
- ✅ Required は `required` 属性 + バッジ両方
- ✅ Submit 後の確認・成功は `role="status"` で SR 通知
- ✅ Tab 順序が論理順（上→下）
- ✅ Submit 失敗時、最初のエラー Field にフォーカス自動移動
- ✅ プライバシーポリシーリンクは別ウィンドウ警告（`target="_blank" rel="noopener"`）

---

## Privacy & Tracking

- GA4 イベント発火: `funnel_step` (4) `contact_form_submit` + `generate_lead`（既存実装あり・KR5-1）
- Privacy: `<a href="/policies/privacy-policy">プライバシーポリシー</a>` で Shopify 標準ページへ
- 同意必須は WCF 等の規約準拠

---

## Do / Don't

### ✅ Do
- 必須項目は最小限（11項目・うち1任意）に厳選
- 「お客様」を使わず「{{ name }}様」
- 自動返信メールも Brand DNA 準拠で書く
- 確認画面で readonly 表示・修正可能に

### ✕ Don't
- 「無料相談」「今すぐお問い合わせ」等の煽り文言を使わない
- 任意項目を必須にしない（特に電話番号）
- Submit 後にエラーで全消去しない（入力値保持）
- Privacy 同意を Default Checked にしない（オプトイン原則）

---

## 関連ファイル
- [input.md](input.md) — Input Primitive
- [form-field.md](form-field.md) — FormField Pattern
- [cta-wording-proposal.md](cta-wording-proposal.md) — CTA 文言体系
- [colors.md](../tokens/colors.md) — エラー色 `--color-error-text`

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `5. Components Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study`
- **Component Set ID**: `98:121` ✅ 新規生成（2026-05-12 Session #7）
- 生成スキル: `figma-component-from-spec` + `figma-use`
- **実装済 variants**: 1（`variant`: input）/ 確認フェーズ・Success 画面は v0.3 拡張枠で保留
- **構造**（Phase 1 = 入力フェーズの代表 7 フィールド）:
  - Section bg: `bg/secondary` (#FAFAFA)、padding 64×4辺、Form width 768（内寸 640）
  - Title 「お問い合わせ」Noto Sans JP Bold 32 Ink + サブタイトル 16 sub
  - **Fields container** (gap 24):
    1. 会社名・団体名 (text): Label Bold 14 + 必須 badge (Drive bg, 10px white) + Input border-base 1px / radius 8 / placeholder
    2. お名前 (text): 同上
    3. 役職 (select): placeholder + `▾` 右寄せ
    4. メール (email): 同 text
    5. 問合せ種別 (radio): 4 options（円形 20×20 + label）
    6. 問合せ内容 (textarea): 144px 高 + helper text 「0 / 500 字」caption
    7. プライバシーポリシー (checkbox): 20×20 box + inline label
  - **Submit Button**: Button (`46:32`) instance variant=primary, size=lg, state=default、テキスト「内容を確認する」
- **未実装（v0.3 で追加予定）**:
  - 残 4 フィールド: 競技・種目 / 電話番号 / 選手数・チーム規模 / 利用検討時期（任意）
  - **`variant=review` (確認フェーズ)**: 同画面 inline 確認、readonly 表示 + 修正/送信 ボタン 2 つ
  - **`variant=success` (Success 画面)**: TOPに戻る + 事例を見る の 2 CTA
  - エラーステート variants: 各フィールドの error state（FormField `56:34` の `state=error` を参照）
  - SP layout: Form 全幅 / button 全幅 / select OS ネイティブ UI

## Change Log
- v0.3-figma (2026-05-12): Figma Component Set `98:121` 新規生成（input variant 1個 / 代表 7 フィールド + Submit Button instance）。FormField パターン化が機能、必須 badge も spec 通り Drive bg + white。残 4 フィールド・確認/Success フェーズは v0.3 拡張枠
- v0.3 (2026-04-27): Worksheet §12 拡張承認（11フィールド化）— **電話番号 任意→必須**（緊急連絡確保）/ **利用検討時期 select 任意 を正式採用**（リード温度判定）/ 役職 8選択肢確認
- v0.2 (2026-04-20): Worksheet §12 確定（10フィールド・inline確認・カスタム自動返信）
