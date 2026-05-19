---
title: FAMBOX DS — L0 翻訳表 v0.1
type: design-system
layer: L0-Foundation
brand: fambox
version: 0.1
status: draft (DNA v0.6.3 ベース)
session: Phase A (Session #55)
last_updated: 2026-05-19
source_dna: /Users/archecoinc./Desktop/Claude_1/brand/fambox/brand-dna/current.md (v0.6.3 / main repo)
source_tokens: snippets/fambox-tokens.css.liquid (v0.5 / 133 tokens)
source_spec: docs/superpowers/specs/2026-05-19-fambox-l0-translation-table-design.md
okr_link: OKR Task 1-2-a「DS 作成」期限 2026-06-30
---

# FAMBOX DS — L0 翻訳表 v0.1

> **位置づけ**: DNA v0.6.3 → 5 Design Principles → 133 Tokens への翻訳表。
> DNA v1.0 確定（2026-06-30）まで段階更新。原則名と構造は固定、Token 値は brand mode で切替可能。

## 0. 翻訳の流れ

```
DNA v0.6.3                  → Design Principles (本書 §2-§6)    → Tokens v0.5
─────────────────────────────────────────────────────────────────────────────
L1 Brand Core (Purpose/      → 1. Evidence-driven                → --color-data-*
 Vision/Concept/Values 6)      （L1-4 Science / L4-A 1位）          --fs-caption*
L2 Strategic Core (Market/   → 2. Continuity                     → --space-* (等比)
 Target/JTBD/POD)              （L1-4 Continuity / L4-A 2位）       --motion-duration-*
L3 Brand Personality         → 3. Equal Partner                  → --color-ink
 (Character/Tone/Voice/        （L3-5 共創者 / L4-A 3位）           --fs-body
 関係性)                                                            --bg-*
L4 Sensorial Assets          → 4. Quiet Drive                    → --color-drive
 (視覚言語 6 軸 + ロゴ + 写真) （L3-2 静かな自信 / L1-3 Drive /     --shadow-1〜2
                              L4-A 4-6位 吸収）
                            → 5. Disciplined Craft              → kebab-case 命名
                              （L1-4 Integrity / Audit-first）    --radius-* / --bp-*
```

> 翻訳表は **DNA を原則化（②）→ 原則を Token に落とす（③）** の 2 段で機能する。①DNA は WHY/WHAT、②原則は WHAT を判断軸に変換、③Token は HOW（具体値）。
> Token 値が変わっても原則名は不変、原則が更新されても DNA との対応根拠は §3 統合根拠表に残す。
> FAM brand mode への接続点は ③（`[data-brand="fam"]` で値だけ override / 原則は共通）。

## 1. 5 原則 早見表

| # | Principle | 一文要約 | DNA 由来（主） | 主要 Token カテゴリ |
|---|---|---|---|---|
| 1 | **Evidence-driven** | 設計判断は論理・スポーツ栄養学・実績で裏打ちし、信頼を生む形で表現する | L1-4 Science / L4-A 1位 / L1-6 可能性の確率 / L1-4 Integrity | `--color-data-*` / `--fs-caption*` / `--fw-medium` |
| 2 | **Continuity** | 定期便と習慣化の文脈に、視覚・時間・空間の連続的リズムを与える | L1-4 Continuity / L4-A 2位 / 定期便文脈 | `--space-*` 等比 / `--motion-duration-*` / `--border-light` |
| 3 | **Equal Partner** | 共創者として対等の距離感を保ち、過剰演出と上から目線を排する | L3-5 共創者 / L4-A 3位 / L1-4 Together | `--color-ink` / `--fs-body` / `--bg-*` 3 階層 |
| 4 | **Quiet Drive** | "Our Drive" は静かな自信と引き算で表現し、派手・映えを Anti とする | L3-2 静かな自信 / L1-3 Brand Concept / L1-0 Anti / L4-A 4-6位 | `--color-drive` / `--fs-display`〜`--fs-h1` / `--shadow-1〜2` |
| 5 | **Disciplined Craft** | 既存資産の Audit-first と Token 化規律ですべての実装を支える | L1-4 Integrity / Audit-first / v0.4 draft Section D | 命名規則 / `--radius-*` / `--bp-*` |

## 2. 原則 1: Evidence-driven

### 2-A. DNA 由来

| DNA 要素 | 引用（v0.6.3 原文）|
|---|---|
| L1-4 Core Values #2 **Science** | アスリート個人のコンテクスト（個人の性格、身体の特徴、個人の目標、競技シーンにおける時間軸、今の心理状態、過去1か月の運動量、現在の食習慣）に応じたスポーツ栄養学に基づく根拠ある判断 |
| L1-4 Core Values #6 **Integrity** | 誠実・実直・本物志向。**結果は言い切らず、取り組みの質と継続で「可能性の確率」を上げる**。アシックス的本質主義＝派手さよりも実用と成果で選ばれる立ち位置 |
| L1-6 Messaging Pillar | 「**栄養で、可能性の確率を上げる**」（Integrity 思想直結・大前さん談）／「結果は言い切らない。確率は上げられる。」 |
| L4-A 視覚言語 6 軸 (FAMBOX 1 位) | **Scientific / Personalized** — B2B では科学的根拠が最優先 |
| L2-4 Functional Benefit (実績軸) | スポーツ栄養学に基づいた根拠のある栄養設計（エビデンス同梱）／個別最適化された食事プランの配送／食事診断による選手タイプ別レコメンド／スポーツ栄養士サポート（相談・見直し・栄養の重要性の布教）|
| L2-6 POD (差別化軸) | スポーツ栄養に特化（一般ダイエット系やボディーメイク系と明確に差別化）／**診断 × 個別プラン × 栄養士相談** の三位一体／競技・ポジション・フェーズ別の栄養設計ロジック／**「結果は言い切らず、可能性の確率を上げる」誠実原則（Integrity）** |

### 2-B. Principle 定義

**一文**: FAMBOX のあらゆる設計判断は、**論理的・スポーツ栄養学的・実績的**な根拠に裏打ちされ、**信頼**を生む形で表現される。

**解説**:
- 数字・データ・実績は装飾ではなく **一級市民**として扱う（caption 階層を独立 token 化、出典明示）
- 「効果保証」「必ず勝てる」等の **過大表現は禁止**（L1-4 Integrity / L1-0 Anti）
- 「**可能性の確率を上げる**」という非断定の表現規律を、UI コピー・グラフ表現・data viz すべてに適用
- 4 軸（論理 / 栄養学 / 実績 / 信頼）のうち 2 軸以上を欠いた設計判断は再検討する

**Do**:
- data 可視化に `--color-data-*` 6 色（彩度を抑えた配色）を使う
- 数値に `--fs-caption: 12px` / `--fs-caption-lg: 13px` で出典 / 単位 / 注記を必ず添える
- グラフは凡例必須、軸ラベル省略禁止
- 引用元・出典・取得日を明示する

**Anti**:
- 数字を装飾扱い（巨大 stat + 文脈なし）
- グラフを `--color-drive` の単色で塗りつぶし（Quiet Drive の Anti と二重違反）
- 「効果が保証されます」「必ず勝てます」風の文言
- 単位省略（"+34" のような曖昧表記）

### 2-C. 対応 Token

| Token | 値 | なぜこの原則を支えるか |
|---|---|---|
| `--color-data-1〜6` | drive / success-green / info-blue / warning-orange / purple / teal | 6 色は **データの意味カテゴリ**（重要 / 成功 / 情報 / 警告 / 中立 / 補助）を分節化。意味と色を結び根拠化 |
| `--fs-caption` / `--fs-caption-lg` | 12px / 13px | 出典 / 単位 / 注記の階層を独立確保（body と混同しない）|
| `--fw-medium` | 500 | 数値強調を bold で派手化せず、medium で「読みやすい強調」に留める |
| `--color-sub` | `#5c5f58` | 注記 / 二次情報の階層を主情報から分離（caption と body の中間）|

**運用ルール**: 新規データ表現を作る時は、最低 1 つの `--color-data-*` と `--fs-caption*` を必ず採用する。`--color-drive` を data viz に使う場合は `--color-data-1` 経由で参照（直接参照禁止）。

### 2-D. 実装シグナル

- **Stat Grid / Bento Grid の数値表現**: 大数字 + 出典 caption がペアであること（fambox-stat-grid.liquid / fambox-bento-grid.liquid の preset 設計準拠）
- **Case Study**: 実績データに「取得日・取得元・取得方法」の 3 点セットを caption 化（fambox-case-study.liquid 構造準拠）
- **FAQ / Contact Form**: 法人購買者向けの「信頼根拠」（実績数・契約数・スポーツ栄養士の数）を caption で添える
- **CTA 文言**: 「効果保証」風を排し、「**取り組みの質と継続**」を示す表現を選ぶ
- **新規 Component 設計時の Audit 質問**: 「この Component は 4 軸（論理 / 栄養学 / 実績 / 信頼）のうちいくつを満たすか？」を spec md に明記する

## 3. 原則 2: Continuity

### 3-A. DNA 由来

| DNA 要素 | 引用（v0.6.3 原文）|
|---|---|
| L1-4 Core Values #4 **Continuity** | 日々の積み重ねを尊ぶ |
| L4-A 視覚言語 6 軸 (FAMBOX 2 位) | **Continuity** — 定期便・習慣化の文脈で最重要 |
| L1-5 社会的価値観 | アスリート寿命の延伸（怪我予防・コンディション維持）|
| L1-1 Purpose (継続的支援文脈) | アスリートのパフォーマンスと社会の wellbeing に貢献 |

### 3-B. Principle 定義

**一文**: 定期便・習慣化・継続コミットの体験を、**視覚（spacing 等比）・時間（motion）・空間（hairline rhythm）**の三層で連続的に表現する。

**解説**:
- スペーシングは **等比率（1.5x / 2x）** が DS de facto（学び 95-96）。等差は使わない
- モーション 250ms はリズムの基準。これより速い変化は「急峻」、遅い変化は「もたつき」
- 区切り線は `--border-light` の hairline で「途切れない連続性」を担保
- 1 画面内の視覚リズム断絶（急激な余白・色変化・モーション加速）は **Anti**

**Do**:
- 縦方向のスペーシングは `--space-1`(8px) → `--space-2`(16px) → `--space-3`(24px) → `--space-4`(32px) の等比継承
- すべての state 遷移（hover / focus / open / close）に `--duration-base: 250ms` を採用
- セクション境界は `--border-light: rgba(27, 29, 26, 0.08)` の hairline

**Anti**:
- スペーシング等差（10px / 18px / 25px のような根拠不明な値）
- 0ms 即時切替 / 600ms 超のゆっくり transition
- 強い border-base (1-2px) で section を切断する視覚断絶
- 急峻な scale 変化（hover で `transform: scale(1.2)` のような派手な拡大）

### 3-C. 対応 Token

| Token | 値 | なぜこの原則を支えるか |
|---|---|---|
| `--space-0-5`〜`--space-8` | 4 / 8 / 12 / 16 / 24 / 32 / 40 / 48 / 64 / 96 / 120px | 等比率スケール（1.5x / 2x）で視覚リズムを連続化 |
| `--duration-base` | 250ms | UI 遷移の標準。Continuity 視覚リズムと時間リズムを同期 |
| `--duration-slow` | 350ms | 大型 modal / drawer の open で「もたつかず急がず」|
| `--duration-fast` | 150ms | ボタンの press feedback など瞬時応答 |
| `--border-light` | `rgba(27, 29, 26, 0.08)` | hairline divider で「途切れない連続性」|
| `--ease-out` / `--ease-in` / `--ease-in-out` | ease-out / ease-in / ease-in-out | 自然な減速曲線で視覚リズムを保つ |
| `--duration-breathing` | 2000ms | 呼吸リズムの「ゆっくりとした連続性」の特殊用途 |

**運用ルール**: 新規 Component の縦方向リズムは `--space-*` のみで構成（直値禁止）。アニメは `--duration-*` のいずれかを必ず採用、easing は `--ease-*` から選ぶ。

### 3-D. 実装シグナル

- **Plan Card（subscription-plan-card）**: 月額 / 年額の **継続コミット** を視覚的に強調する（一回購入との差別化）。`--space-*` の整列で「定期感」を作る
- **Bento Grid 縦方向**: section 間 `--space-5: 48px` を基準、子要素は `--space-2`〜`--space-3` を継承
- **Header / Footer**: site 共通の縦リズムを `--space-3: 24px` で固定（fambox-header.liquid / fambox-footer.liquid 準拠）
- **Modal 開閉**: `--duration-slow: 350ms` + `--ease-out` で「もたつかず急がず」
- **新規 Component 設計時の Audit 質問**: 「縦方向のスペーシング 3 段階以上で等比性を保てているか？モーション duration が token から来ているか？」

## 4. 原則 3: Equal Partner

### 4-A. DNA 由来

| DNA 要素 | 引用（v0.6.3 原文）|
|---|---|
| L3-5 関係性の姿勢 | **「共創者（Equal Partner in Challenge）」**：ベンダー⇔顧客ではなく「共同実装者」／対等・対話・相互リスペクト |
| L1-4 Core Values #3 **Together** | 対等な対話、FAMBOX とアスリートは共に尊重し合う |
| L4-A 視覚言語 6 軸 (FAMBOX 3 位) | **Co-driven** — 監督⇔栄養士の対等対話は購買決定要因 |
| L3-3 推奨語彙 | 共創／共創者／伴走／パートナーシップ |
| L3-3 避ける語彙 | **寄り添う**（自己満足化）／**サポーター**（影の従属感）／**お客様**（距離感・上下関係の匂い）|

### 4-B. Principle 定義

**一文**: 共創者として **対等の距離感** を保ち、過剰演出・威圧的 CTA・"お客様"距離感の語彙を Anti とする。

**解説**:
- 視覚的に「上から目線」を排する：Hero CTA の威圧サイズ・glow 過多・派手な背景は **Anti**
- "お客様" 距離感の語彙（"お客様" / "サポーター" / "寄り添う"）を UI コピーから排除
- 主従ではなく **横並び**を意識した視覚レイアウト（左右整列・hierarchy の段差を抑制）
- 落ち着いた ink（#1b1d1a）を主テキストにし、過度に明るい黒（pure #000）を避ける

**Do**:
- 主テキスト `--color-ink: #1b1d1a`（純黒ではなく僅かに緑寄りの落ち着いた黒）
- 標準 body は `--fs-body: 16px` で読みやすさを最優先
- 背景の 3 階層（primary / secondary / tertiary）で「対話の場の落ち着き」を作る
- 「**伴走**」「**共創**」「**パートナーシップ**」を CTA / 見出しに

**Anti**:
- 主テキストに pure black `#000`（コントラスト過剰で威圧感）
- Hero CTA で `--shadow-5`(modal-level) 採用（威圧）
- 「**お客様**」「**サポーター**」「**寄り添う**」を UI コピーで使う
- 一方的な「サービスを提供します」型の見出し

### 4-C. 対応 Token

| Token | 値 | なぜこの原則を支えるか |
|---|---|---|
| `--color-ink` | `#1b1d1a` | 純黒回避で「対話の落ち着き」。コントラスト過剰を避け視線疲労を抑える |
| `--color-sub` | `#5c5f58` | 二次テキストの階層を主から「程よく」分離（過度に薄くしない）|
| `--color-caption` | `#8a8d87` | 三次テキスト。caption / meta 用 |
| `--fs-body` | 16px | 読みやすさ最優先の標準値（小さくしない）|
| `--bg-primary` | `#ffffff` | 対話の場の主背景 |
| `--bg-secondary` / `--bg-tertiary` | `#fafafa` / `#f3f3f3` | 階層差を「微差」で表現（強い色差は威圧感）|

**運用ルール**: 主テキストは `--color-ink` のみ。`#000` 直値は使わない。body は `--fs-body` を基準、本文小型化は `--fs-body-sm: 14px` まで。

### 4-D. 実装シグナル

- **Hero CTA**: `--color-drive` + `--shadow-2` 程度に抑制（`--shadow-5` は modal 専用、Hero では使わない）
- **Contact Form**: 「**お問い合わせ**」より「**共創パートナーとして話す**」の方向（fambox-contact-form.liquid 文言運用準拠）
- **Profile**: スポーツ栄養士を「**伴走者**」「**共創者**」として表現（fambox-profile.liquid 構造準拠）
- **Case Study**: 「クライアントの声」ではなく「**共創パートナーの実績**」（fambox-case-study.liquid 文言運用準拠）
- **Body コピーの主語**: 「**FAMBOX が提供する**」を避け、「**チームと FAMBOX が共に**」型を採用
- **新規 Component 設計時の Audit 質問**: 「主テキストに `--color-ink` を使っているか？避ける語彙（お客様/サポーター/寄り添う）が混入していないか？」

## 5. 原則 4: Quiet Drive

### 5-A. DNA 由来

| DNA 要素 | 引用（v0.6.3 原文）|
|---|---|
| L3-2 Tone of Voice | 硬質×温度／確信と熱量を兼ねた洗練／**静かな自信**（誠実・愚直・実直）／**"引き算"の美学**（アシックス的本質主義）|
| L1-3 Brand Concept | **Your Step. Our Drive.** — あなたの挑戦が、スポーツの未来を動かす |
| L4-A 視覚言語 6 軸 (FAMBOX 4-6 位) | Propulsive (4) / Ascending (5) / Pulsing (6) — Quiet Drive に統合（演出補助）|
| L1-0 Anti | 表面的／派手／"映え"重視／盛り／キラキラ系ブランディング／過度な演出 |
| L1-4 Core Values #1 **Drive** | 推進力で前へ押し出す |

### 5-B. Principle 定義

**一文**: "Our Drive" は **静かな自信と引き算** で表現し、派手・映え・キラキラを徹底的に Anti とする。

**解説**:
- Brand Concept "Drive" は維持。ただし「**派手な推進**」ではなく「**確信に裏打ちされた推進**」
- 色は `--color-drive: #FB4C15`（赤橙）を主軸とするが、glow 過多 / ネオン彩度 / 高彩度多色は禁止
- タイポは Display サイズ (56px) を使うが、**1 画面 1 箇所限定**（視覚的「叫び」を作らない / multi-stack 禁止）
- Shadow は `--shadow-1`〜`--shadow-2` を中心に。`--shadow-3`〜`--shadow-5` は modal/drawer 等の特殊用途のみ
- アニメは Continuity 原則の duration を踏襲。drive 演出のための独自モーションは作らない

**Do**:
- Drive 色は CTA / 重要アクセント / drive 強調の限定使用（**面積比 5% 以下**を目安）
- Display フォントは Hero の 1 箇所のみ、それ以外は H1-H3 で十分
- shadow は `--shadow-1`(hairline) / `--shadow-2`(card hover) を中心

**Anti**:
- 全面 drive 色塗り / 大面積使用
- 高彩度多色（neon green + neon pink 等）
- glow shadow 多用（`--color-drive-glow` の連続適用）
- Display サイズの multi-stack（巨大文字を連続配置）
- `--shadow-5: 0 24px 48px ...` を card に適用（modal の威圧感を card に持ち込む）

### 5-C. 対応 Token

| Token | 値 | なぜこの原則を支えるか |
|---|---|---|
| `--color-drive` | `#FB4C15` | Brand Concept "Drive" の核。彩度を抑えた赤橙で「派手すぎない推進」|
| `--color-drive-hover` | `#e14710` | hover でわずかに暗化し、過度な変化を避ける |
| `--color-drive-light` | `#FC825B` | 控えめなアクセント（背景・微強調）|
| `--color-drive-glow` | `rgba(251, 76, 21, 0.32)` | glow 用、ただし **連続適用禁止**（CTA の 1 箇所のみ）|
| `--fs-display` | `56px` | Hero の **1 箇所のみ**。multi-stack 禁止 |
| `--fs-h1` | `48px` | 通常見出しはここまで。Display は控える |
| `--fs-h2` | `32px` | section 見出し標準 |
| `--fs-h3` | `24px` | sub section 見出し標準 |
| `--shadow-1` | `0 1px 2px rgba(0,0,0,0.04)` | hairline / section 区切り |
| `--shadow-2` | `0 4px 8px rgba(0,0,0,0.08)` | card hover の lift |
| `--shadow-3`〜`--shadow-5` | 8-24px blur / modal | **Card 等の通常用途で使用禁止**（modal/drawer 専用）|

**運用ルール**:
- `--color-drive` の面積比は画面の 5% 以下を目安
- `--fs-display` は Hero 1 箇所のみ（multi-stack 検出は Audit-first で行う）
- shadow level は 1-2 を基本、3 以上は modal/drawer の特殊用途のみ

### 5-D. 実装シグナル

- **Hero (fambox-hero-v17-video)**: Display サイズ (56px) の大型見出し + `--color-drive` の CTA。background は静止画 or 控えめな motion
- **CTA Button**: `--color-drive` の Filled / hover で `--color-drive-hover`。`--color-drive-glow` は focus ring 用途のみ
- **Bento Grid Editorial preset**: drive 色は accent として 1 タイルにのみ採用（全タイル drive 色は Anti）
- **Stat Grid**: `--fs-display: 56px` で stat focus value。隣接 stat は `--fs-h2: 32px` / `--fs-h3: 24px` 程度に抑える
- **Shadow 使用箇所**: card hover = `--shadow-2`、modal = `--shadow-5`、drawer = `--shadow-4`。**card に shadow-5 を使うのは Anti**
- **新規 Component 設計時の Audit 質問**: 「drive 色の面積比は 5% 以下か？Display サイズの multi-stack はないか？shadow level は用途と合致しているか？」

## 6. 原則 5: Disciplined Craft

### 6-A. DNA 由来

| DNA 要素 | 引用 |
|---|---|
| L1-4 Core Values #6 **Integrity** (v0.6.3) | 誠実・実直・本物志向。アシックス的本質主義＝派手さよりも実用と成果で選ばれる立ち位置 |
| operations/2026-05-12-brand-dna-v0.4-draft.md Section D | **Disciplined**：何かを作る前に必ず既存資産を確認する。Audit-first protocol は DNA の実装規律として、視覚言語と同等の重要度を持つ |
| operations/2026-05-12-brand-dna-v0.4-draft.md Section A | Marc 流 4 層スタック（L1 Transport / L2 Skill / L3 Tokens / L4 Definitions / L5 Audit-first）|
| L1-4 Core Values #2 Science (副) | 根拠ある判断 — 直値ではなく Token を介す規律 |

### 6-B. Principle 定義

**一文**: 既存資産の **Audit-first** と **Token 化規律** によって、他 4 原則の適用すべてを支える。

**位置づけ**: 他 4 原則（Evidence-driven / Continuity / Equal Partner / Quiet Drive）と **同列ではなく上乗せ**のメタ規律。優先順位の対象外（§7 で詳述）。

**解説**:
- 新規 Component 作成時、まず **既存資産の全件 audit**（spec md / Figma Set / Liquid section の三位一体）を実行
- 直値（magic number）禁止。色 / spacing / fs / shadow / radius / bp / motion はすべて token 経由
- Token 命名は **kebab-case + カテゴリ prefix**（`--color-*` / `--space-*` / `--fs-*` / `--bp-*`）
- spec md ↔ Figma Component Set ↔ Liquid section の **三位一体達成**を目標（current.md §7 ダッシュボード）

**Do**:
- 既存 Token snippet (`snippets/fambox-tokens.css.liquid`) を grep してから新規追加判断
- L4 Component を作る時、L3 Pattern / L2 Primitive の既存 spec を必ず読む
- Token 化されていない値は **新規 Token として追加**してから使う
- 命名は `--カテゴリ-意味-修飾` の 3 階層（例: `--color-drive-hover`）

**Anti**:
- Magic number / inline hex / inline px の直値使用
- 既存 spec を読まずに新規 spec を書く
- Token 名の独自命名（camelCase / snake_case 等の混在）
- spec md と Liquid section の値が乖離（current.md §7 で N/3 が割れる状態を放置）

### 6-C. 対応 Token

**命名規則**:
- 必須 prefix: `--color-` / `--space-` / `--fs-` / `--fw-` / `--bp-` / `--radius-` / `--shadow-` / `--duration-` / `--ease-` / `--bg-` / `--border-` / `--glass-` / `--white-overlay-` / `--ink-overlay-`
- 修飾サフィックス: `-hover` / `-light` / `-sm` / `-md` / `-lg` / `-base` / `-slow` / `-fast`
- alias 構造: `--color-cta: var(--color-drive)` のような **意味への参照**を使う（§1-A 1-9 Semantic Alias 参照）

**主要 Token（Disciplined Craft が支える基盤）**:

| Token | 値 | 役割 |
|---|---|---|
| `--radius-xs`〜`--radius-pill` | 2/4/8/16px、50%、50px、9999px | 角丸の表現規律。直値禁止 |
| `--bp-sp-sm`〜`--bp-pc` | 480 / 767 / 768 / 1024px | レスポンシブ規律 |
| `--space-0-5`〜`--space-8` | 4/8/12/16/24/32/40/48/64/96/120px | spacing の規律 |
| `--color-cta` | `var(--color-drive)` | 意味への参照（semantic alias）|

**運用ルール**:
- 新規 Token 追加時は `current.md §1` と `snippets/fambox-tokens.css.liquid` を同時更新（学び 111）
- Tokens Studio との同期は `operations/scripts/tokens-studio-v05-complete.json` 経由

### 6-D. 実装シグナル

- **新規 Component 作成時の手順**（Audit-first protocol）:
  1. `current.md §7` 完成度ダッシュボードで既存 spec / Figma / Liquid の存在を確認
  2. `snippets/fambox-tokens.css.liquid` を grep して既存 token を確認
  3. SKILL `figma-component-from-spec` v0.7 の Step 0.5 Audit を実行
  4. 既存資産で代替できない場合のみ新規作成
- **Liquid 書式**: 全 fambox-* section は `{% render 'fambox-tokens.css' %}` を <head> 経由で参照（学び 95-96 / 22 sections 全 Token 化済）
- **三位一体の更新**: Component spec を変更したら、Figma Set と Liquid section も同タイミングで更新（current.md §7 N/3 ラベルで track）
- **新規 Component 設計時の Audit 質問**: 「既存 spec / Figma Set / Liquid section を全て読んだか？magic number は残っていないか？token 命名規則に従っているか？」

## 7. 原則間の優先度・矛盾時の解決ルール

### 7-1. 矛盾時の優先順位

```
Evidence-driven > Continuity > Equal Partner > Quiet Drive
（最上位）                                              

[横断・メタ] Disciplined Craft
```

**理由**:
- **Evidence-driven が最上位**: B2B / スポーツ栄養 / 法人購買が主軸 → 論理的・スポーツ栄養学的・実績的に根拠が最上位、信頼が重要である
- **Continuity**: 定期便文脈の継続性（事業モデル直結）
- **Equal Partner**: 関係性の核（共創者 / L3-5）
- **Quiet Drive**: ビジュアル trait（Tone of Voice の視覚化）
- **Disciplined Craft は横断的メタ原則** — 他 4 原則の適用すべてに Audit-first を上乗せ（順序判定の対象外）

### 7-2. 衝突例と解決

| # | 衝突 | 解決 |
|---|---|---|
| 1 | **Evidence-driven**（データ可視化で意味カテゴリを派手な色で目立たせたい）vs **Quiet Drive**（ネオン彩度禁止）| Evidence-driven が勝つ。ただし `--color-data-*` 6 色の範囲内で（Quiet Drive の Anti「ネオン彩度」「neon green+neon pink」は超えない）|
| 2 | **Continuity**（モーションを連続的に重ねたい）vs **Equal Partner**（控えめに）| Equal Partner 優先。`--duration-base: 250ms` を超えるアニメ multi-stack 禁止。1 画面で同時 active な motion は 2 個まで |
| 3 | **Disciplined Craft**（Token 化を強制）vs **Evidence-driven**（実験的データ表現で新値が欲しい）| Disciplined Craft はメタ。実験データは **新規 token として追加**し命名規則に従う（Token 化を bypass せず、`--color-data-7` のように拡張）|

### 7-3. 適用範囲の注意

- 優先順位は **設計判断が複数原則に分岐する場合**のみ参照（通常は複数原則を同時に満たす設計を目指す）
- **両立可能な場合は必ず両立させる**。優先順位は「妥協が必要な時の最後の判断材料」
- 順位が低い原則を「無視」してよい意味ではない（Quiet Drive 4 位でも `--color-drive` の派手使いは依然 Anti）
- **Disciplined Craft はすべての設計判断で並列適用**（順位の対象外）

## 8. Token 逆引き表

## 9. 改訂履歴

- v0.1 (2026-05-19 / Session #55): 初稿。DNA v0.6.3 ベース、5 原則確定（Evidence-driven / Continuity / Equal Partner / Quiet Drive / Disciplined Craft）、Token 逆引き表 10 カテゴリ × 5 原則。spec: `docs/superpowers/specs/2026-05-19-fambox-l0-translation-table-design.md`
