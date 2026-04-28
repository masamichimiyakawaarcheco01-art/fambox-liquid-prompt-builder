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
  - 2026-04-27: S1 完了（§4 Z-index / §5 Icons / §6 Button）/ S2 完了（§7-§11 Worksheet 同期 + 合成決定 §9.4・§11.3 A 承認）/ S3 完了（§12-§14 Worksheet 同期 + 合成決定 §12.1.a A・§12.1.b B 任意→必須・§12.1.c A・§13.1.a C 不採用・§14.1.a A・§15 A スキップ）/ S3 拡張: §16 Card Pattern 確定（4 Variants + 拡張余地）
  - 2026-04-28: §17 Hero Section L4 Component 確定（4 Variants × 3 Heights × CTA 0-2 / NBA HOOP モード任意 / 動画 parallax 対応 / 4 禁止項目明示）/ §18 Header L4 Component 確定（3 Variants × 3 Heights × 3 Sticky Modes / Logo 左 / Primary CTA 1 / SP 横スクロール DNA 既定 / 4 禁止項目明示）/ §19 Footer L4 Component 確定（3 Variants / Ink 背景固定 / Logo 左 / SNS 必須 40px / Bottom = Copyright + Legal / CTA なし / 4 禁止項目明示）/ §20 Bento Tile L3 Pattern 確定（4 Variants × 5 Sizes / Glass Variant 専用 / Stat-focus fs-display 56px / Glass 5 階調 / 4 禁止項目明示）/ §21 Bento Grid L4 Component 確定（3 Variants / 12-6-1 col / Gap DNA 既定 + modifier / Editorial 主構図強制 / 4 禁止項目明示）
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

# §16. Pattern — Card（2026-04-27 S3 拡張セッションで確定）

**FAMBOX 最頻出 Pattern**。L4 Component（Subscription / Case Study / Article / Stat / Hero）の **基盤**として継承される。詳細仕様: [components/card.md](components/card.md)

### Q1: Variants
- ✅ **4 Variants 採用 + 拡張余地あり** — standard / featured / horizontal / flat。v0.3 以降で `card-{variant-name}` 形式のカスタム追加可能（拡張ルールは card.md の「拡張ルール」節）
- ☐ 3 Variants まで（flat を別 Pattern 化）
- ☐ 2 Variants まで縮小

### Q2: horizontal の SP 折り返し挙動
- ☐ SP では standard レイアウトに自動折り返し
- ✅ **SP でも横並び維持（画像 30% / テキスト 70%）** — Case Study 一覧の視線移動・密度を優先。極小 SP（〜480px）のみ縦折返しを許可

### Q3: Card 内 CTA の必須性
- ✅ **全 Variants で CTA 1 個必須**（Primary / Secondary / Ghost / Link いずれか）— 情報のみ Card は作らず、必要なら `<section>` / `<article>` で素直に組む
- ☐ CTA は任意
- ☐ CTA × 2 まで許可

### Q4: Selected 状態の発現
- ✅ **`.is-selected` で Drive 2px 枠線** — Subscription / Plan / Filter 選択時に共通利用。padding は -1px 補正で外形維持
- ☐ Selected 状態は L3 Card には持たせず、L4 個別実装

### 共通仕様（card.md からの抜粋）
- background: `--bg-primary`（flat のみ `--bg-secondary`）
- border: `1px solid --border-light` 既定 / Featured / Selected: `2px --color-drive`
- border-radius: `--radius-md`（8px）固定 — Pill 禁止
- padding: `--space-3`（24px）
- shadow: `--shadow-1` 既定 / hover で `--shadow-3` + `translateY(-2px)`
- transition: `--duration-base` `--ease-out`

---

# §17. Component — Hero Section（2026-04-28 確定）

**TOPページ DNA 反映（5/29 期限）の主役 Component**。詳細仕様: [components/hero-section.md](components/hero-section.md)

### Q1: Variants
- ✅ **4 Variants 採用 + 拡張余地あり** — video-fullscreen / video-split / image-editorial / minimal-text。v0.3 以降カスタム可
- ☐ 3 Variants（minimal-text 省略）
- ☐ 2 Variants

### Q2: Hero の高さ運用
- ✅ **3 段階用意** — `hero--full`（100vh）/ `hero--tall`（70vh）/ `hero--compact`（40vh）modifier クラスで切替
- ☐ Full のみ
- ☐ Auto + min-height（コンテンツ依存）

### Q3: CTA 数
- ☐ Primary 1 個固定
- ☐ Primary + Secondary 2 個許可
- ✅ **任意（0〜2）**— FAQ Hero / 告知は CTA 0、TOP は Primary 1、Subscription LP は Primary + Secondary（即決派/相談派 両対応）

### Q4: NBA HOOP 型タイポ重ね（Aesthetic 軸）
- ☐ image-editorial Variant の必須仕様として実装
- ✅ **任意機能として ON/OFF 切替可能** — `is-hoop` modifier で発現。`mix-blend-mode: difference` でタイポと写真重ね、撮影／素材選定で干渉回避
- ☐ 後回し（v0.3 で別タスク）

### Q5: パララックス運用
- ☐ ヒーロー背景画像のみ slow parallax 任意
- ✅ **動画でも parallax 適用**（DNA v0.5 既定の拡張）— slow のみ・transform は scrollY の 15% 以下・`prefers-reduced-motion: reduce` で必ず無効
- ☐ パララックスなし

### Q6: Anti-pattern 禁止リスト
- ✅ **全 4 項目を禁止リスト化**:
  1. 動画 + 派手フィルタ重ね（彩度上げ・color burn 等のブレンド多用）禁止
  2. Drive 色背景の全画面ベタ塗り禁止
  3. Hero 内 CTA を Primary 2 個以上 禁止
  4. Pill 形状以外の CTA 禁止
- ☐ 最小限（Primary 2 個禁止 のみ）

### 共通仕様（hero-section.md からの抜粋）
- max-width: `--container-max`（1440px）
- padding (vertical): PC `--space-8` (160px) / SP `--space-7` (96px) ★TNF 級余白
- padding (horizontal): PC `--space-5` (48px) / SP `--space-3` (24px)
- min-height: full=100vh / tall=70vh / compact=40vh
- Title font-size: PC `--fs-mega`（96px）/ SP `--fs-hero`（64px）
- Title font-family: `--font-en`（Poppins）
- Title color: 動画/画像系=`--color-white` + linear-gradient overlay / minimal-text=`--color-ink`

---

# §18. Component — Header（2026-04-28 確定）

**全画面共通の Component**。Brand DNA v0.5 の「ハンバーガー不採用 / 横スクロールメニュー / Drive Pill CTA」を体系化。詳細仕様: [components/header.md](components/header.md)

### Q1: Variants
- ✅ **3 Variants 採用 + 拡張余地あり** — standard / minimal / mega。v0.3 以降カスタム可
- ☐ 2 Variants（mega 省略）
- ☐ 1 Variant

### Q2: SP 挙動
- ✅ **DNA 既定通り** — 横スクロールメニュー + 990px 未満で Shopify drawer 併用（**ハンバーガー不採用**）
- ☐ Drawer + ハンバーガー（Shopify 標準）
- ☐ 横スクロールメニュー単独（drawer 廃止）

### Q3: Sticky 動作
- ☐ Always sticky 固定
- ☐ On scroll up only 固定
- ☐ Never sticky 固定
- ✅ **modifier 切替可能** — `header--sticky`★既定 / `header--scroll-up` / `header--static` の 3 モード

### Q4: Header の高さ
- ☐ Default 80px のみ
- ✅ **3 段階** — `header--compact`（64px）/ `header--default`★既定（80px）/ `header--tall`（96px）modifier 切替
- ☐ Auto

### Q5: ロゴ位置
- ✅ **左固定**（Shopify 標準・実装簡素・SR フレンドリー）
- ☐ 中央
- ☐ 切替可能

### Q6: CTA 配置と数
- ✅ **Header 末尾に Primary 1 個固定**（Drive Pill / btn-primary btn-md / DNA 既定）
- ☐ Primary + Secondary 2 個許可
- ☐ 任意（0 or 1）

### Q7: Anti-pattern 禁止リスト
- ✅ **全 4 項目を禁止リスト化**:
  1. ハンバーガー単独運用 禁止（DNA 違反）
  2. Header に Drive 色ベタ塗り 禁止
  3. Logo を Drive 色背景上に置かない
  4. メニューフォントを Display サイズ（48px+）にしない
- ☐ 最小限（ハンバーガー単独 のみ禁止）

### 共通仕様（header.md からの抜粋）
- background `--bg-primary` / color `--color-ink` / border-bottom 1px `--border-light`
- z-index `--layer-4`（Sticky Header / Drawer 階層）
- menu font: `--font-ja` / `--fs-body`（16px）/ `--fw-medium`（500）★Display サイズ禁止
- menu hover transition: `color var(--duration-fast) var(--ease-out)` ★既存 0.2s 継承
- Logo: 高さは Header 高さの 50% 上限（compact 32px / default 40px / tall 48px）

---

# §19. Component — Footer（2026-04-28 確定）

**全画面共通の Component**。詳細仕様: [components/footer.md](components/footer.md)

### Q1: Variants
- ✅ **3 Variants 採用 + 拡張余地あり** — standard / minimal / sitemap。v0.3 以降カスタム可
- ☐ 2 Variants（sitemap 省略）
- ☐ 1 Variant

### Q2: 背景色
- ✅ **Ink (`--color-ink` `#1B1D1A`) + White テキスト** — 既存 fam-footer-v2 継承・コントラスト 16.6:1（WCAG AAA）
- ☐ White 背景 + Ink テキスト
- ☐ modifier 切替可能

### Q3: ロゴ位置
- ✅ **左固定**（Header と整合）
- ☐ 中央
- ☐ 上部中央 + Brand area 中央寄せ

### Q4: SNS リンク
- ✅ **全 Variants で必須**（Instagram / YouTube / note / X / TikTok 等 / 40×40 サイズ上限）
- ☐ Standard / Sitemap のみ表示
- ☐ 任意

### Q5: Bottom row の要素
- ✅ **Copyright + Legal links のみ**（Privacy / Terms / 特商法）— 最小限・必要十分
- ☐ +Payment methods icons
- ☐ +Payment methods + 言語/通貨スイッチャー

### Q6: CTA 配置
- ✅ **Footer に CTA を置かない**（Header / Hero / Section で CTA は十分・繰り返し回避）
- ☐ Standard のみ末尾に Primary CTA 1 個
- ☐ メール登録フォームを Inline で持つ

### Q7: Anti-pattern 禁止リスト
- ✅ **全 4 項目を禁止リスト化**:
  1. Drive 色背景の全面ベタ塗り 禁止
  2. SNS アイコンを Display サイズ（64px+）にしない
  3. Bottom row に動きアニメ 禁止
  4. Footer 内に Hero 級画像を置かない
- ☐ 最小限（Drive ベタ塗り のみ禁止）

### 共通仕様（footer.md からの抜粋）
- background `--color-ink` (#1B1D1A) / 全 Variants 統一
- text color `--color-white` / Tagline `rgba(255,255,255,0.7)` / Bottom `rgba(255,255,255,0.6)`
- padding (vertical) PC `--space-8` (160px) / SP `--space-7` (96px)
- Bottom row background: `rgba(0,0,0,0.3)` で差別化 / border-top `rgba(255,255,255,0.1)`
- Nav columns: PC 3 列 / Tablet 2 列 / SP 1 列
- SNS icon: 40×40 / `border-radius: --radius-pill` / hover で background Drive 色

---

# §20. Pattern — Bento Tile（2026-04-28 確定）

**TOPページ主役の L3 Pattern**。詳細仕様: [components/bento-tile.md](components/bento-tile.md)

### Q1: Variants
- ✅ **4 Variants 採用 + 拡張余地あり** — standard / glass / image-fill / stat-focus。v0.3 以降カスタム可
- ☐ 3 Variants（stat-focus を別 Pattern 化）
- ☐ 2 Variants

### Q2: Sizes
- ✅ **DNA 5 sizes 厳守** — 1×1 / 2×1 / 1×2 / 2×2 / 3×2（Brand DNA v0.5 C-Bento 既定）
- ☐ DNA 5 + 拡張
- ☐ 3 sizes に縮小

### Q3: Glass 効果の適用範囲
- ✅ **Glass Variant 専用**（他 Variants には適用しない・規律明確）
- ☐ 全 Variants で modifier 切替可能
- ☐ Standard / Image-fill にも Glass 適用可

### Q4: Stat-focus の数字サイズ
- ☐ `--fs-mega`（96px）
- ✅ **`--fs-display`（56px）固定** — Hero との階層成立 / Bento グリッド内の密度保持
- ☐ Tile size に応じて可変

### Q5: ガラス効果の opacity 階調
- ✅ **Glass 1-5（DNA 5 階調）から選択** — `bento-glass--{1-5}` modifier で 0.05/0.1/0.3/0.6/0.8 切替
- ☐ Glass 3（0.3）固定
- ☐ opacity 任意

### Q6: Anti-pattern 禁止リスト
- ✅ **全 4 項目を禁止リスト化**:
  1. 同じサイズタイルの単調並列 禁止（強弱必須）
  2. Drive 色の全タイル背景化 禁止
  3. Glass + Hero 級画像 mix-blend は image-fill 専用
  4. タイル間隔を 16px 未満にしない
- ☐ 最小限（強弱必須 のみ）

### 共通仕様（bento-tile.md からの抜粋）
- 5 Sizes: tile-1x1 / tile-2x1 / tile-1x2 / tile-2x2 / tile-3x2
- border-radius `--radius-md`（8px）固定
- padding `--space-3`（24px）/ Glass / Image-fill は外周 padding なし
- Glass: opacity 0.05/0.1/0.3/0.6/0.8 の 5 階調
- Stat-focus 数字: `--fs-display` 56px / `--font-en` Poppins / `--fw-bold`
- SP（<768px）では全タイル `grid-column: span 1` に強制縮退

---

# §21. Component — Bento Grid（2026-04-28 確定）

**Bento Tile を配置するグリッドシステム**。L4 Component。詳細仕様: [components/bento-grid.md](components/bento-grid.md)

### Q1: Variants
- ✅ **3 Variants 採用 + 拡張余地あり** — standard / editorial / autofit。v0.3 以降カスタム可
- ☐ 2 Variants（autofit 省略）
- ☐ 1 Variant

### Q2: PC グリッド
- ✅ **12 column system**（DNA 既定 / gutter 32px）
- ☐ 6 column system
- ☐ modifier 切替可

### Q3: レスポンシブ挙動
- ✅ **PC 12col / Tablet 6col / SP 1col 縦並び**（DNA 整合・実装簡素・SR フレンドリー）
- ☐ PC 12col / Tablet 6col / SP 横スクロール
- ☐ PC 12col / Tablet 自動 fit / SP 1col

### Q4: Gap サイズ
- ✅ **DNA 既定**: SP 16px / Tablet 24px / PC 32px / `bento-gap--{sm/md/lg}` modifier 上書き可
- ☐ 全画面 24px 固定
- ☐ カスタム可

### Q5: Editorial Variant の主構図ルール
- ✅ **強制**（対角線配置 + 主役 2×2 最低 1 個 / 将来 Lint 検出可能）
- ☐ 推奨（強制せず Do/Don't で記載のみ）
- ☐ 任意（自由配置可）

### Q6: Anti-pattern 禁止リスト
- ✅ **全 4 項目を禁止リスト化**:
  1. 同サイズタイル並列 禁止
  2. 主役タイルなし 禁止（Editorial Variant 必須条件）
  3. Gap 16px 未満 禁止
  4. 1 Bento Grid に 12 タイル以上 禁止（情報過剰）
- ☐ 最小限（同サイズ並列 のみ禁止）

### 共通仕様（bento-grid.md からの抜粋）
- grid-template-columns: PC `repeat(12, 1fr)` / Tablet `repeat(6, 1fr)` / SP `1fr`
- grid-auto-rows: `minmax(160px, auto)`（タイル最小高さ）
- gap: PC `--space-4`(32px) / Tablet `--space-3`(24px) / SP `--space-2`(16px)
- max-width: `--container-max`（1440px）
- 推奨タイル数: 4-9 個（12 個以上禁止）
- Editorial 主構図: 左下→右上 対角線（軸1 / 主役タイル 2×2 以上 必須）
- Auto-fit: `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))` + `grid-auto-flow: dense`

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
