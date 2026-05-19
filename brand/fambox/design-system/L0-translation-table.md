---
title: FAMBOX DS — L0 翻訳表 v0.1
type: design-system
layer: L0-Foundation
brand: fambox
version: 0.1
status: draft (DNA v0.6.3 ベース)
session: Phase A (Session #55)
last_updated: 2026-05-19
source_dna: brand/fambox/brand-dna/current.md (v0.6.3)
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

### 3-B. Principle 定義

### 3-C. 対応 Token

### 3-D. 実装シグナル

## 4. 原則 3: Equal Partner

### 4-A. DNA 由来

### 4-B. Principle 定義

### 4-C. 対応 Token

### 4-D. 実装シグナル

## 5. 原則 4: Quiet Drive

### 5-A. DNA 由来

### 5-B. Principle 定義

### 5-C. 対応 Token

### 5-D. 実装シグナル

## 6. 原則 5: Disciplined Craft

### 6-A. DNA 由来

### 6-B. Principle 定義

### 6-C. 対応 Token

### 6-D. 実装シグナル

## 7. 原則間の優先度・矛盾時の解決ルール

## 8. Token 逆引き表

## 9. 改訂履歴

- v0.1 (2026-05-19 / Session #55): 初稿。DNA v0.6.3 ベース、5 原則確定（Evidence-driven / Continuity / Equal Partner / Quiet Drive / Disciplined Craft）、Token 逆引き表 10 カテゴリ × 5 原則。spec: `docs/superpowers/specs/2026-05-19-fambox-l0-translation-table-design.md`
