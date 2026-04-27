---
title: FAMBOX Design System Input Worksheet
type: worksheet
brand: fambox
status: active
last_updated: 2026-04-27
owner: 宮川
purpose: 4時間集中セッション用の構造化入力シート。各セクションの [ 回答 ] 欄に入力する or 選択肢に ✅ をつける → Claudeが反映して DS を更新
session_log:
  - 2026-04-20: §1-§3 部分回答（color alias / typography）/ §7-§14 確定（Spec 直書き、Worksheet 同期は 4-27 で実施）
  - 2026-04-27: S1 完了（§4 Z-index / §5 Icons / §6 Button）/ S2 完了（§7-§11 Worksheet 同期 + 合成決定 §9.4・§11.3 A 承認）/ S3 完了（§12-§14 Worksheet 同期 + 合成決定 §12.1.a A・§12.1.b B 任意→必須・§12.1.c A・§13.1.a C 不採用・§14.1.a A・§15 A スキップ）
---

# FAMBOX Design System — Input Worksheet（4時間集中用）

**使い方**:
- 各セクションで **[ 回答: ... ]** の欄に入力、または選択肢の前の ☐ を ✅ に変える
- 迷ったら「判断保留」として理由を書く（後で再議論可能）
- 完了したらチャットで「§1-§3 回答完了」のように教えてください。私が反映します

**推奨ペース**:

| Hour | セクション | 想定時間 |
|---|---|---|
| Hour 1 | §1 Foundation / §2 Color Alias / §3 Typography Preset | 60分 |
| Hour 2 | §4 Z-index / §5 Icon / §6 Button / §7 Input | 60分 |
| Hour 3 | §8 FormField / §9 Avatar / §10 Form Controls / §11 Progress | 60分 |
| Hour 4 | §12 Contact Form / §13 Subscription Plan Card / §14 Case Study | 60分 |

---

# §1. L0 Foundation — 視覚軸のFAMBOX優先順

FAM v0.5 の6軸をFAMBOXでどの優先順で使うか。**1位が最も支配的、6位がアクセント程度**。

v0.1 構築プランでの私の提案（検証対象）:

| 順位 | 軸 | 現提案 |
|---|---|---|
| 1位 | Scientific / Personalized | 🔶 |
| 2位 | Continuity | 🔶 |
| 3位 | Co-driven | 🔶 |
| 4位 | Propulsive | 🔶 |
| 5位 | Ascending | 🔶 |
| 6位 | Pulsing | 🔶 |

### 入力
- ☐ 上記提案のままでOK
- ☐ 変更する → 新しい優先順: [ 回答: 1位__Ascending_ / 2位__Propulsive_ / 3位__ Co-driven_ / 4位__Scientific / Personalized_ / 5位__Continuity_ / 6位__Pulsing_ ]

---

# §2. Color — Semantic Alias の運用

意味参照として使える Alias は現在4つ。追加したい別名 or 参照先変更があれば入力。

### 現状（`tokens.css`記載）
```css
--color-cta: var(--color-drive);
--color-focus-ring: var(--color-drive);
--color-link: var(--color-drive);           /* ★要検討 */
--color-link-hover: var(--color-drive-light);
```

### 質問1: リンク基本色は `--color-drive`（オレンジ）? それとも `--color-deep`（Deep Blue）?
- ☐ Drive（オレンジ）— 動的・推進感。ただし本文中の大量リンクでうるさい恐れ
- ☐ Deep Blue — 信頼感・本文リンクで定番の可読性。FAMBOXのB2B文脈にマッチ
- ☐ 場面で使い分け → 使い分けルール: [ 回答: ]背景色がブラック、またはFAFAFAのようなグレーの場合はオレンジでテキストカラーを白、背景がオレンジの場合はボタンテキストをブラック系、テキストを白にする、DeepBlueは使用しない

### 質問2: 追加したい Alias はあるか？（例示）
- ☐ `--color-price` — 価格表示色（Ink or Drive？）→ [ 回答: ]背景色に依存する、背景オレンジの場合は白、ブラックならオレンジか白、明るいグレーの場合はオレンジかInk系の色にする、目立たせる場合はオレンジ、そうでない場合は白かinkブラック系にする
- ☐ `--color-success-text` — 成功テキスト専用
- ☐ `--color-error-text` — エラーテキスト専用 F91A02の色 赤系
- ☐ その他: [ 回答: ]

---

# §3. Typography — Preset運用
文字サイズや余白サイズは基本8の倍数、16以下の余白の場合は4倍数を推奨して使用する

`typography.md` に 9個の Preset を定義済み（display / h1 / h2 / h3 / lead / body / body-sm / caption / stat）。

### 質問1: FAMBOX LPでのフォントサイズ運用（PC基準）

TOPページ Hero の見出しサイズはどれ？
- ☐ `--fs-mega`（96px）— 超迫力
- ☐ `--fs-hero`（64px）— 推奨
- ☐ `--fs-display`（56px）— 落ち着き

B2B 提案書・資料ページの見出しサイズは？
- ☐ `--fs-h1`（48px）
- ☐ `--fs-h2`（32px）

### 質問2: 英字見出し＋日本語サブの組み合わせルール
FAMBOX ヒーローでの典型例を1つ確定したい。
- ☐ **Pattern A**: 英字主役（大）＋ 日本語（小・下段）
  例: `FAMBOX` 96px / `チーム栄養ソリューション` 20px
- ☐ **Pattern B**: 日本語主役（大）＋ 英字（小・上段ラベル）
  例: `POWERED BY SCIENCE` 14px / `スポーツ栄養で勝ち筋を設計する` 48px
- ☐ 両方使う → 使い分けルール: [ 回答: ]

### 質問3: 追加したい Preset はあるか？
- ☐ `.text-eyebrow`（ラベル文字・大文字英字）
- ☐ `.text-quote`（引用・インタビュー）
- ☐ `.text-btn`（ボタン内テキスト）
- ☐ その他: [ 回答: ]

---

# §4. Z-index Scale

現状 `tokens.css` の z-index scale:
```css
--z-base: 0;
--z-raised: 10;
--z-sticky: 100;
--z-drawer: 500;
--z-modal: 1000;
--z-toast: 1500;
--z-tooltip: 2000;
```

### 質問1: 既存Shopifyテーマと衝突する z-index はあるか？
- ☐ 不明（既存確認していない）→確認したい
- ☐ 衝突する → 調整必要: [ 回答: ]
- ✅ 衝突なし — legacy `--z-legacy-sticky-cta: 9990` のみ既存。v0.5 で Layer 3 へ順次刷新（tokens.css 既記載）

### 質問2: 追加が必要な Layer は？
- ✅ 追加なし — `--layer-3` で Sticky CTA / Announcement Bar / Chat Widget を全て吸収（tokens.css 既コメント）。同階層は order/位置で制御
- ☐ `--z-announcement-bar`（お知らせバー・ヘッダーより上）
- ☐ `--z-chat-widget`（Shopify inbox 等）
- ☐ その他: [ 回答: ]

---

# §5. Icon Set 選定（2026-04-27 確定）

### §5.1 路線
- ✅ **自作のみで運用** — `brand/shared/icons/` に既に 9カテゴリ × 3色バリアント（default/drive/white）の自作SVGを整備済。Lucide等への置換やハイブリッドは行わない
- ☐ 自作 + Lucide ハイブリッド
- ☐ Lucide に置換

### §5.2 線幅・グリッド標準
- ✅ **既存自作SVGの実測値に合わせる** — viewBox 24×24 / stroke-width 1.5 / linecap round / linejoin round。`icon-creation-spec.md` を実測値ベースに修正（32×32 マスター記述は v0.2 で訂正）
- ☐ 32×32 grid で再制作

### §5.3 命名規則
- ✅ **並列維持** — ファイル名は `{category}-{name}-{variant}.svg`（現状維持）／Figma 内コンポーネント名は `icon/{category}/{name}-{variant}` でスラッシュ階層化。両者を SSoT 同期で運用

### 判定基準クリア状況（自作運用ベース）
- ✅ 線画1.5px（既存SVG実測）
- ✅ 24px viewBox で整合
- ✅ Scientific軸に合う（FAMBOX独自チューニング可能）
- ✅ ライセンス: 自作のため自由

---

# §6. Primitive — Button（2026-04-27 確定）

### 質問1: 必要なバリアント

**Variant（5種採用）**:
- ✅ **Primary**（`btn-primary`）— Drive色Pill / 白文字
- ✅ **Secondary Outline Ink**（`btn-secondary-ink`）— 2px Ink枠線・透明背景・Ink文字
- ✅ **Secondary Outline Drive**（`btn-secondary-drive`）— 2px Drive枠線・透明背景・Drive文字
- ✅ **Ghost**（`btn-ghost`）— 枠線なし・透明背景・Ink文字（hover時に薄背景）
- ✅ **Link**（`btn-link`）— インラインテキスト型・hover時下線・Pill形状なし
- ☐ Destructive（採用しない・モーダルの Cancel/OK で代替）

**Size（3段階全て採用）**:
- ✅ **SM**（padding 8/16px / fs-body-sm 14px）
- ✅ **MD**（padding 12/32px / fs-body 16px）★既定 — FAM corp-btn 既存値継承
- ✅ **LG**（padding 16/40px / fs-lg 20px）

**State**:
- ✅ default / hover / focus（focus-visible 2px outline）/ active / disabled / loading
- ☐ 追加ステート（v0.2 では追加なし）

### 質問2: Iconボタンの必要性
- ✅ **両方採用** — `btn-icon-only`（正方形・aria-label必須）+ `btn-with-icon`（アイコン+テキスト並列・gap 8px）

### 質問3: CTAボタンの文言候補
- ✅ **別タスクで決定**（CTA Wording Workshop / 大前さん討議要）— Button Spec から文言依存を切り離し、Spec 上は「プライマリCTA」等の汎用例として記載
- 既存採用文言: 「話を聞いてみる」（2026-04-20 暫定確定、`cta-wording-proposal.md` 参照）

---

# §7. Primitive — Input（2026-04-20 確定 / 2026-04-27 Worksheet 同期）

### 質問1: 運用パターン確認（v0.5既定）
- ✅ 下線型（単一入力：検索/ニュースレター/メール等）
- ✅ 枠囲み型（複雑フォーム：診断/問合せ/アカウント）
- 両方併用（ハイブリッド運用）

### 質問2: Textarea（複数行入力）のスタイル
- ✅ 枠囲み型と同じデザインを縦に伸ばす — min-height ≈96px / resize: vertical / line-height body
- ☐ 下線型で伸ばす
- ☐ 独自デザイン: [ 回答: ]

### 質問3: バリデーション表示
- ✅ onBlur即時表示（v0.5既定）+ Submit時に再検証で全エラー一覧
- ☐ Submit時のみ表示
- ✅ 文字数カウンタあり：対象フィールド = **自由記述系のみ**（問合せ内容など長文 textarea）

### 質問4: 必須マーク
- ☐ 赤い「*」をラベル横
- ✅ 「必須」バッジをラベル横（Drive 背景・白文字・`--radius-sm`・`--fs-caption`）
- ☐ 「任意」バッジのほうをつける（必須が多いフォーム想定）
- ☐ その他: [ 回答: ]

---

# §8. Pattern — FormField（2026-04-20 確定 / 2026-04-27 Worksheet 同期）

**FormField = Label + Input + HelperText + ErrorMessage** の構造。

### 質問1: Label の位置
- ✅ **上配置（標準・推奨）** — モバイル含め最も読みやすい / SR 親和性◎
- ☐ 左（インライン）
- ☐ Placeholder（Floating Label）
- ☐ 場面で使い分け: [ 回答: ]

### 質問2: HelperText の位置
- ✅ **Input下・薄色（`--color-sub` `#545655`・`--fs-caption` 12px）**
- ☐ Input上・ラベル下（補足情報）
- ☐ 両方使う: [ 回答: ]

### 質問3: ErrorMessage
- ✅ **Input下・赤（`--color-error-text` `#F91A02`）+ エラー時は HelperText を非表示**
- ☐ Input右側（長い場合切れる懸念）
- ☐ Toast で出す

### 質問4: 入力文字数の目安表示（「例: 〇〇で」）
- ☐ Placeholder に入れる（消えるので不可）
- ✅ **HelperText に書く** — 常時表示で入力中も参照可能・SR 読み上げ可
- ☐ なし

---

# §9. Primitive — Avatar（2026-04-20 確定 / 2026-04-27 Worksheet 同期）

アスリート・栄養士・監督のプロフィール表示に使う。

### 質問1: サイズ
- ✅ **XS 24px / SM 32px / MD 48px / LG 64px / XL 96px**（5段階・全て8の倍数）
- ☐ 別のサイズ: [ 回答: ]

### 質問2: 形状
- ✅ **円形（standard）** — `border-radius: var(--radius-pill)`
- ☐ 角丸正方形（radius-md）
- ☐ 両方: [ 使い分け: ]

### 質問3: フォールバック表示（画像なし時）
- ✅ **イニシャル 1文字**（背景 `--color-deep`・文字 `--color-white`・Poppins semibold・サイズ40%）
- ☐ アイコン（人型シルエット）
- ☐ 無地（Sky色背景）
- ☐ その他: [ 回答: ]

### 質問4: プロフィール枠付き？
- ✅ **装飾なし（default）+ `.is-featured` 時のみ Drive 2px ボーダー**（合成決定・2026-04-27 A 承認）
- ☐ ボーダー2px（Drive色）のフォーカス枠（→ focus は別途 outline 2px で対応）
- ☐ シャドウ（`--shadow-2`）のみ
- ☐ 装飾なし（単独）

---

# §10. Primitive — Form Controls（Checkbox/Radio/Toggle）（2026-04-20 確定 / 2026-04-27 Worksheet 同期）

### 質問1: Checkbox
- ✅ **角4px（`--radius-sm`）・Drive色チェック・24×24px**
- ☐ 角なし（純矩形）
- ☐ カスタム: [ 回答: ]

### 質問2: Radio
- ✅ **円形・Drive色塗り潰し**（外円24px・内点12px）
- ☐ 円形・Drive色アウトライン

### 質問3: Toggle（スイッチ）
- ✅ **Pill型・Drive色ON / `--border-base` グレーOFF**（48×24・ノブ20px白・shadow-1）
- ☐ 角丸・Deep Blue で ON / 白で OFF
- ☐ 独自形状: [ 回答: ]

### 質問4: 使用頻度
- ✅ **Checkbox 多い**（プライバシー同意・食物アレルギー・競技種目等の複数選択）
- ☐ Radio 多い（単一選択）
- ☐ Toggle 多い（設定画面 / 定期便管理）

---

# §11. Primitive — Progress / Spinner（2026-04-20 確定 / 2026-04-27 Worksheet 同期）

### 質問1: Progress bar
- ✅ **両方採用（用途で使い分け）**
  - 線形（`height 4px` / Drive 進行・`--bg-tertiary` 未進行）= フォーム送信・連続的進行
  - 円形（48/64/96/128px・stroke 4-6px）= 食事診断 Step進行・達成率
- ☐ 線形のみ
- ☐ 円形のみ

### 質問2: Spinner
- ✅ **円形回転・Drive色**（24/32/48px・1秒/回 linear infinite・75%欠け円弧）
- ☐ 3点ドット（Typing indicator風）
- ☐ 呼吸アニメ

### 質問3: Loading State の誘導テキスト
- ✅ **基本=文言なし（Spinner のみ）+ 重要処理のみ「処理中です…」**（合成決定・2026-04-27 A 承認）
- ☐ 「読み込み中…」（Get処理と混同）
- ☐ 「準備中です…」（工事中ページ感）
- ☐ 「少々お待ちください」
- ☐ その他: [ 回答: ]
- NG文言: 「もう少しお待ちください！」（煽り）/「がんばって読み込み中…」（擬人化過剰）/「Loading...」（英語直書き）

---

# §12. Component — Contact Form（問合せフォーム）

### 質問1: 必要なフィールド（11項目に確定 / 2026-04-20 確定 + 2026-04-27 拡張承認）

**必須/任意 × 入力タイプ**:
- ✅ 会社名・団体名（**必須** / text）
- ✅ 競技・種目（**必須** / text）
- ✅ お名前（**必須** / text）
- ✅ 役職（**必須** / select 8項目: 監督/コーチ/専属栄養士/マネージャー/学校・クラブ事務局/選手本人/保護者/その他）★ 2026-04-27 拡張承認（Worksheet 4項目→8項目）
- ✅ メールアドレス（**必須** / email）
- ✅ 電話番号（**必須** / tel）★ 2026-04-27 任意→必須 変更（B=必須採択）
- ✅ 選手数・チーム規模（**必須** / select: 〜10/11〜30/31〜50/51〜100/101+）
- ✅ 問合せ種別（**必須** / radio: 資料/相談/試食/その他）
- ✅ 問合せ内容（**必須** / textarea / 10〜500字 + 文字数カウンタ）
- ✅ プライバシーポリシー同意（**必須** / checkbox / オプトイン原則）
- ✅ **利用検討時期**（**任意** / select: すぐ/1か月以内/3か月以内/未定）★ 2026-04-27 追加（リード温度判定）

### 質問2: Confirmation画面の遷移
- ✅ **同画面で inline 確認（送信前）→ 送信後に Success（別ページ /thanks）**
- ☐ 次ページに遷移して確認 → 送信後にSuccess
- ☐ 送信完了画面（購入完了テンプレ共有）

### 質問3: 返信の自動メール要否
- ☐ Shopify 標準の自動返信メール使用
- ✅ **カスタム自動返信（FAMBOX トーン・対等表現・「お客様」回避・件名「【FAMBOX】お問い合わせを承りました」）**
- ☐ 自動返信なし（手動返信のみ）

---

# §13. Component — Subscription Plan Card（定期便プラン）

### 質問1: カードに表示する情報（8項目に確定 / 2026-04-20 確定 + 2026-04-27 縮小）
- ✅ プラン名（h3）
- ✅ 価格（税込 / h2 32px / Ink色）
- ✅ 提供頻度（月1回 / 週2回 等）
- ✅ 1回あたりの食数
- ✅ カスタマイズ可否（○/△/×）
- ✅ 推奨対象（ジュニア / 大学生 / プロ等）
- ✅ 特典・サポート内容（チェックリスト形式）
- ✅ CTA × 2（Primary + Ghost）
- ☐ 最低契約期間 ★ 2026-04-27 不採用（C=両方追加しない）— 別途 FAQ 等で記載
- ☐ 初月特典 ★ 2026-04-27 不採用（C=両方追加しない）— 別途キャンペーン施策側で扱う

### 質問2: 価格訴求の強さ
- ☐ 大きく強調（`--fs-display` 64px / Drive色）
- ✅ **中くらい（`--fs-h2` 32px / Ink色）** — Drive色64pxは煽り回避・Integrity 体現
- ☐ 控えめ（ベネフィット訴求優先）

### 質問3: CTA の位置・文言
- ☐ カード下部・固定CTA
- ✅ **カード下部・複数CTA（Primary「このプランで始めてみる」/ Ghost「話を聞いてみる」）** — 即決派/相談派 両対応
- ☐ その他: [ 回答: ]

### 質問4: バッジ（推奨・人気等）
- ✅ **「おすすめ」バッジ（Drive色）— 1プランのみ表示**
- ☐ 「人気」バッジ（Sky色）
- ☐ 「新規」バッジ
- ☐ 使わない

---

# §14. Component — Case Study / Testimonial（実績・事例）

### 質問1: 事例の表示項目（10項目に確定 / 2026-04-20 確定 + 2026-04-27 拡張承認）
- ✅ チーム名・競技
- ✅ 選手写真（許諾済 / 顔出しNGなら背中・俯瞰）
- ✅ 監督・栄養士名（任意 + Avatar 併用）
- ✅ 導入前の課題（Before）
- ✅ 導入後の変化（After / 数字あれば添える）
- ✅ 具体データ（体重 / 体脂肪 / コンディション等 / Data Viz 併用）
- ✅ 推薦コメント（監督 or 栄養士の引用）
- ✅ 継続期間（「導入から12ヶ月」等）
- ✅ **食事戦略の概要** ★ 2026-04-27 追加（手段の透明性 = Integrity 体現）
- ✅ 関連事例リンク（任意）

### 質問2: 表示レイアウト
- ✅ **複数を組み合わせる**:
  - パターン1: カード一覧（一覧ページ・関連事例エリア）
  - パターン2: ストーリー形式（詳細ページ 1事例 1ページ）
  - パターン3: ロゴリスト（TOP 社会的証明エリア）
- ☐ 単独レイアウトのみ

### 質問3: データ可視化の併用
- ✅ **全 Data Viz 用途別に活用**
  - NutrientRing: 栄養バランス改善 前後比較（ストーリー詳細）
  - TrendLine: 体重・体脂肪率の継続データ（ストーリー詳細）
  - BigStat: 主要数値ハイライト（カード一覧 + ストーリー両方）
- ☐ 使わない

### 質問4: 匿名化の扱い
- ☐ 実名公表（許諾取得済）
- ☐ 「A選手・B大学」等の匿名
- ✅ **混在（公表OKを Hero 優先 / NG は匿名で補足）**

---

# §15. 自由入力欄（Feelings / Ideas / Constraints）

**Status**: 2026-04-27 S3 で **A=リスト化スキップ**を選択。本セクションは別セッション・別タスクで起票・実施する。

## 直感的な懸念・要望
[ 別タスクで実施 ]

## リファレンスにしたい他社UI
[ 別タスクで実施 ]

## 予算・納期・技術制約
[ 別タスクで実施 ]

## 大前さん／須藤さん向けに事前確認したい質問
[ 別タスクで実施 ]

---

# 完了後の流れ

1. 本ファイルのチェックを入れ終えたら、チャットで「Worksheet完了」と送る
2. 私が内容を元に以下を更新:
   - `tokens.css` に §1-§5 の決定値を反映
   - `colors.md` / `typography.md` 等の Docs に反映
   - `components/` 配下に新規MD（button.md を雛形に、input.md / avatar.md 等）を生成
   - DAILY_BACKLOG.md の対応タスクを ✅ に更新
3. 次セッション向けのサマリと未決論点を報告

---

**現在時刻 / 開始**: 2026-04-20 ___:___
**終了**: 2026-04-20 ___:___
**実効作業時間**: ___ 時間

お疲れさまでした。
