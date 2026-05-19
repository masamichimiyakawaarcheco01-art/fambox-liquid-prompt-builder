# FAMBOX DS L0 翻訳表 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** FAMBOX Brand DNA v0.6.3 から 5 Design Principles（Evidence-driven / Continuity / Equal Partner / Quiet Drive / Disciplined Craft）への翻訳表本体を `brand/fambox/design-system/L0-translation-table.md` に作成し、L0 Foundation を初めて構造化する。OKR Task 1-2-a「DS 作成」期限 2026-06-30 直結。

**Architecture:** 単一 markdown ファイル（250-350 行）に 9 セクション構成。各原則は 4 サブセクション（A. DNA 由来 / B. Principle 定義 / C. 対応 Token / D. 実装シグナル）で展開。Token 引用は `snippets/fambox-tokens.css.liquid` に対して grep で実在検証する（spec §3 の `--fs-display: 28px` のような誤記を防ぐ）。DNA 引用は `brand/fambox/brand-dna/current.md` v0.6.3 から原文を載せる。完了後 `current.md §6 Brand DNA との接続` から本ファイルへのリンクを追加する。

**Tech Stack:** Markdown (CommonMark) + YAML frontmatter / git (jovial-benz-resume worktree, branch `claude/jovial-benz-864b2d`) / Bash grep for token verification.

**Spec source:** `docs/superpowers/specs/2026-05-19-fambox-l0-translation-table-design.md` (commits 7a82e54 + cad0ef3, branch `claude/jovial-benz-864b2d`)

---

## File Structure

| 種別 | パス | 役割 | 想定行数 |
|---|---|---|---|
| 新規 | `brand/fambox/design-system/L0-translation-table.md` | L0 翻訳表本体（5 原則 × 4 サブセクション + 早見表 + 優先度 + 逆引き）| 250-350 |
| 修正 | `brand/fambox/design-system/current.md` | §6 内に L0 翻訳表へのリンクを 1 行追加 | +2 行 |
| Read-only 参照 | `brand/fambox/brand-dna/current.md` | DNA v0.6.3 引用元（L1-0/L1-1〜L1-6/L3-2/L3-5/L4-A）| — |
| Read-only 参照 | `snippets/fambox-tokens.css.liquid` | Token 引用の実在検証対象（133 tokens v0.5）| — |
| Read-only 参照 | `docs/superpowers/specs/2026-05-19-fambox-l0-translation-table-design.md` | 承認済 spec（commits 7a82e54 + cad0ef3）| — |

**全タスクの作業 worktree**: `/Users/archecoinc./Desktop/Claude_1/docs/okr/.claude/worktrees/jovial-benz-resume`
**全コマンドは `git -C $JBR ...` 形式で実行**（JBR は jovial-benz-resume の絶対パス）

**実行前 setup**:
```bash
JBR=/Users/archecoinc./Desktop/Claude_1/docs/okr/.claude/worktrees/jovial-benz-resume
cd $JBR  # または git -C $JBR を使う
git -C $JBR status  # clean であることを確認
git -C $JBR log --oneline -3  # 最新 commit が cad0ef3 (spec 修正) であることを確認
```

---

## Task 1: Skeleton + frontmatter + §0 + §1 + §9 骨格作成

**Files:**
- Create: `brand/fambox/design-system/L0-translation-table.md`

- [ ] **Step 1: 新規ファイル作成 (frontmatter + heading 骨格)**

ファイルに以下を書く（heading のみ、本文は後続 task で埋める）:

```markdown
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

## 1. 5 原則 早見表

## 2. 原則 1: Evidence-driven

## 3. 原則 2: Continuity

## 4. 原則 3: Equal Partner

## 5. 原則 4: Quiet Drive

## 6. 原則 5: Disciplined Craft

## 7. 原則間の優先度・矛盾時の解決ルール

## 8. Token 逆引き表

## 9. 改訂履歴
```

- [ ] **Step 2: §0 翻訳の流れ図を書く**

§0 配下に以下の図を追加:

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

文（5-7 行）:
> 翻訳表は **DNA を原則化（②）→ 原則を Token に落とす（③）** の 2 段で機能する。①DNA は WHY/WHAT、②原則は WHAT を判断軸に変換、③Token は HOW（具体値）。
> Token 値が変わっても原則名は不変、原則が更新されても DNA との対応根拠は §3 統合根拠表に残す。
> FAM brand mode への接続点は ③（`[data-brand="fam"]` で値だけ override / 原則は共通）。

- [ ] **Step 3: §1 5 原則 早見表 を書く**

```markdown
| # | Principle | 一文要約 | DNA 由来（主） | 主要 Token カテゴリ |
|---|---|---|---|---|
| 1 | **Evidence-driven** | 設計判断は論理・スポーツ栄養学・実績で裏打ちし、信頼を生む形で表現する | L1-4 Science / L4-A 1位 / L1-6 可能性の確率 / L1-4 Integrity | `--color-data-*` / `--fs-caption*` / `--fw-medium` |
| 2 | **Continuity** | 定期便と習慣化の文脈に、視覚・時間・空間の連続的リズムを与える | L1-4 Continuity / L4-A 2位 / 定期便文脈 | `--space-*` 等比 / `--motion-duration-*` / `--border-light` |
| 3 | **Equal Partner** | 共創者として対等の距離感を保ち、過剰演出と上から目線を排する | L3-5 共創者 / L4-A 3位 / L1-4 Together | `--color-ink` / `--fs-body` / `--bg-*` 3 階層 |
| 4 | **Quiet Drive** | "Our Drive" は静かな自信と引き算で表現し、派手・映えを Anti とする | L3-2 静かな自信 / L1-3 Brand Concept / L1-0 Anti / L4-A 4-6位 | `--color-drive` / `--fs-display`〜`--fs-h1` / `--shadow-1〜2` |
| 5 | **Disciplined Craft** | 既存資産の Audit-first と Token 化規律ですべての実装を支える | L1-4 Integrity / Audit-first / v0.4 draft Section D | 命名規則 / `--radius-*` / `--bp-*` |
```

- [ ] **Step 4: §9 改訂履歴 雛形を書く**

```markdown
- v0.1 (2026-05-19 / Session #55): 初稿。DNA v0.6.3 ベース、5 原則確定（Evidence-driven / Continuity / Equal Partner / Quiet Drive / Disciplined Craft）、Token 逆引き表 10 カテゴリ × 5 原則。spec: `docs/superpowers/specs/2026-05-19-fambox-l0-translation-table-design.md`
```

- [ ] **Step 5: ファイル構造検証**

Run:
```bash
grep -E "^## [0-9]\." $JBR/brand/fambox/design-system/L0-translation-table.md
```

Expected (10 行):
```
## 0. 翻訳の流れ
## 1. 5 原則 早見表
## 2. 原則 1: Evidence-driven
## 3. 原則 2: Continuity
## 4. 原則 3: Equal Partner
## 5. 原則 4: Quiet Drive
## 6. 原則 5: Disciplined Craft
## 7. 原則間の優先度・矛盾時の解決ルール
## 8. Token 逆引き表
## 9. 改訂履歴
```

- [ ] **Step 6: Commit**

```bash
git -C $JBR add brand/fambox/design-system/L0-translation-table.md
git -C $JBR commit -m "feat(L0): 翻訳表 skeleton + §0 翻訳の流れ + §1 早見表 (Session #55)"
```

---

## Task 2: §2 原則 1 Evidence-driven 執筆

**Files:**
- Modify: `brand/fambox/design-system/L0-translation-table.md` (§2 配下)
- Read-only verify: `snippets/fambox-tokens.css.liquid`
- Read-only reference: `brand/fambox/brand-dna/current.md` (L1-4 / L1-6 / L4-A)

- [ ] **Step 1: 2-A DNA 由来 サブセクションを書く**

§2 配下に以下を追加:

```markdown
### 2-A. DNA 由来

| DNA 要素 | 引用（v0.6.3 原文）|
|---|---|
| L1-4 Core Values #2 **Science** | アスリート個人のコンテクスト（個人の性格、身体の特徴、個人の目標、競技シーンにおける時間軸、今の心理状態、過去1か月の運動量、現在の食習慣）に応じたスポーツ栄養学に基づく根拠ある判断 |
| L1-4 Core Values #6 **Integrity** | 誠実・実直・本物志向。**結果は言い切らず、取り組みの質と継続で「可能性の確率」を上げる**。アシックス的本質主義＝派手さよりも実用と成果で選ばれる立ち位置 |
| L1-6 Messaging Pillar | 「**栄養で、可能性の確率を上げる**」（Integrity 思想直結・大前さん談）／「結果は言い切らない。確率は上げられる。」 |
| L4-A 視覚言語 6 軸 (FAMBOX 1 位) | **Scientific / Personalized** — B2B では科学的根拠が最優先 |
| L2-4 Functional Benefit (実績軸) | （DNA §L2-4 を実装時に該当行追記） |
| L2-6 POD (差別化軸) | （DNA §L2-6 を実装時に該当行追記） |
```

- [ ] **Step 2: 2-B Principle 定義を書く**

```markdown
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
```

- [ ] **Step 3: 2-C 対応 Token を書く**

```markdown
### 2-C. 対応 Token

| Token | 値 | なぜこの原則を支えるか |
|---|---|---|
| `--color-data-1〜6` | drive / success-green / info-blue / warning-orange / purple / teal | 6 色は **データの意味カテゴリ**（重要 / 成功 / 情報 / 警告 / 中立 / 補助）を分節化。意味と色を結び根拠化 |
| `--fs-caption` / `--fs-caption-lg` | 12px / 13px | 出典 / 単位 / 注記の階層を独立確保（body と混同しない） |
| `--fw-medium` | 500 | 数値強調を bold で派手化せず、medium で「読みやすい強調」に留める |
| `--color-sub: #5c5f58` | — | 注記 / 二次情報の階層を主情報から分離（caption と body の中間） |

**運用ルール**: 新規データ表現を作る時は、最低 1 つの `--color-data-*` と `--fs-caption*` を必ず採用する。`--color-drive` を data viz に使う場合は `--color-data-1` 経由で参照（直接参照禁止）。
```

- [ ] **Step 4: 2-D 実装シグナルを書く**

```markdown
### 2-D. 実装シグナル

- **Stat Grid / Bento Grid の数値表現**: 大数字 + 出典 caption がペアであること（fambox-stat-grid.liquid / fambox-bento-grid.liquid の preset 設計準拠）
- **Case Study**: 実績データに「取得日・取得元・取得方法」の 3 点セットを caption 化（fambox-case-study.liquid 構造準拠）
- **FAQ / Contact Form**: 法人購買者向けの「信頼根拠」（実績数・契約数・スポーツ栄養士の数）を caption で添える
- **CTA 文言**: 「効果保証」風を排し、「**取り組みの質と継続**」を示す表現を選ぶ
- **新規 Component 設計時の Audit 質問**: 「この Component は 4 軸（論理 / 栄養学 / 実績 / 信頼）のうちいくつを満たすか？」を spec md に明記する
```

- [ ] **Step 5: Token 引用の実在検証**

Run:
```bash
grep -E "^\s*--(color-data-[1-6]:|fs-caption:|fs-caption-lg:|fw-medium:|color-sub:)" $JBR/snippets/fambox-tokens.css.liquid
```

Expected: 9 行以上 hit（`--color-data-1`〜`--color-data-6` の 6 行 + `--fs-caption` + `--fs-caption-lg` + `--fw-medium` + `--color-sub`）

もし hit しない token があれば、`snippets/fambox-tokens.css.liquid` を再 grep して正しい token 名に書き換える。

- [ ] **Step 6: Commit**

```bash
git -C $JBR add brand/fambox/design-system/L0-translation-table.md
git -C $JBR commit -m "feat(L0): §2 Evidence-driven 原則を執筆 (Session #55)"
```

---

## Task 3: §3 原則 2 Continuity 執筆

**Files:**
- Modify: `brand/fambox/design-system/L0-translation-table.md` (§3 配下)

- [ ] **Step 1: 3-A DNA 由来 サブセクションを書く**

```markdown
### 3-A. DNA 由来

| DNA 要素 | 引用（v0.6.3 原文）|
|---|---|
| L1-4 Core Values #4 **Continuity** | 日々の積み重ねを尊ぶ |
| L4-A 視覚言語 6 軸 (FAMBOX 2 位) | **Continuity** — 定期便・習慣化の文脈で最重要 |
| L1-5 社会的価値観 | アスリート寿命の延伸（怪我予防・コンディション維持） |
| L1-1 Purpose (継続的支援文脈) | アスリートのパフォーマンスと社会の wellbeing に貢献 |
```

- [ ] **Step 2: 3-B Principle 定義を書く**

```markdown
### 3-B. Principle 定義

**一文**: 定期便・習慣化・継続コミットの体験を、**視覚（spacing 等比）・時間（motion）・空間（hairline rhythm）**の三層で連続的に表現する。

**解説**:
- スペーシングは **等比率（1.5x / 2x）** が DS de facto（学び 95-96）。等差は使わない
- モーション 250ms はリズムの基準。これより速い変化は「急峻」、遅い変化は「もたつき」
- 区切り線は `--border-light` の hairline で「途切れない連続性」を担保
- 1 画面内の視覚リズム断絶（急激な余白・色変化・モーション加速）は **Anti**

**Do**:
- 縦方向のスペーシングは `--space-1`(8px) → `--space-2`(16px) → `--space-3`(24px) → `--space-4`(32px) の等比継承
- すべての state 遷移（hover / focus / open / close）に `--motion-duration-base: 250ms` を採用
- セクション境界は `--border-light: rgba(27, 29, 26, 0.08)` の hairline

**Anti**:
- スペーシング等差（10px / 18px / 25px のような根拠不明な値）
- 0ms 即時切替 / 600ms 超のゆっくり transition
- 強い border-base (1-2px) で section を切断する視覚断絶
- 急峻な scale 変化（hover で `transform: scale(1.2)` のような派手な拡大）
```

- [ ] **Step 3: 3-C 対応 Token を書く**

```markdown
### 3-C. 対応 Token

| Token | 値 | なぜこの原則を支えるか |
|---|---|---|
| `--space-0-5`〜`--space-8` | 4 / 8 / 12 / 16 / 24 / 32 / 40 / 48 / 64 / 80 / 96 / 120px | 等比率スケール（1.5x / 2x）で視覚リズムを連続化 |
| `--motion-duration-base` | 250ms | UI 遷移の標準。Continuity 視覚リズムと時間リズムを同期 |
| `--motion-duration-slow` | 350ms | 大型 modal / drawer の open で「もたつかず急がず」 |
| `--motion-duration-fast` | 150ms | ボタンの press feedback など瞬時応答 |
| `--border-light: rgba(27, 29, 26, 0.08)` | — | hairline divider で「途切れない連続性」 |
| `--motion-ease-base` | cubic-bezier (実装値で確認) | 自然な減速曲線で視覚リズムを保つ |

**運用ルール**: 新規 Component の縦方向リズムは `--space-*` のみで構成（直値禁止）。アニメは duration token のいずれかを必ず採用。
```

- [ ] **Step 4: 3-D 実装シグナルを書く**

```markdown
### 3-D. 実装シグナル

- **Plan Card（subscription-plan-card）**: 月額 / 年額の **継続コミット** を視覚的に強調する（一回購入との差別化）。`--space-*` の整列で「定期感」を作る
- **Bento Grid 縦方向**: section 間 `--space-5: 48px` を基準、子要素は `--space-2`〜`--space-3` を継承
- **Header / Footer**: site 共通の縦リズムを `--space-3: 24px` で固定（fambox-header.liquid / fambox-footer.liquid 準拠）
- **Modal 開閉**: `--motion-duration-slow: 350ms` + ease-out で「もたつかず急がず」
- **新規 Component 設計時の Audit 質問**: 「縦方向のスペーシング 3 段階以上で等比性を保てているか？モーション duration が token から来ているか？」
```

- [ ] **Step 5: Token 引用の実在検証**

Run:
```bash
grep -E "^\s*--(space-[0-9]|motion-duration|border-light|motion-ease)" $JBR/snippets/fambox-tokens.css.liquid
```

Expected: 15 行以上 hit。もし `--motion-ease-base` / `--motion-duration-fast` 等が無ければ、Step 3 の表で「(該当 token 未確認)」とマーク、Token 名は実在値に修正。

- [ ] **Step 6: Commit**

```bash
git -C $JBR add brand/fambox/design-system/L0-translation-table.md
git -C $JBR commit -m "feat(L0): §3 Continuity 原則を執筆 (Session #55)"
```

---

## Task 4: §4 原則 3 Equal Partner 執筆

**Files:**
- Modify: `brand/fambox/design-system/L0-translation-table.md` (§4 配下)

- [ ] **Step 1: 4-A DNA 由来 サブセクションを書く**

```markdown
### 4-A. DNA 由来

| DNA 要素 | 引用（v0.6.3 原文）|
|---|---|
| L3-5 関係性の姿勢 | **「共創者（Equal Partner in Challenge）」**：ベンダー⇔顧客ではなく「共同実装者」／対等・対話・相互リスペクト |
| L1-4 Core Values #3 **Together** | 対等な対話、FAMBOX とアスリートは共に尊重し合う |
| L4-A 視覚言語 6 軸 (FAMBOX 3 位) | **Co-driven** — 監督⇔栄養士の対等対話は購買決定要因 |
| L3-3 推奨語彙 | 共創／共創者／伴走／パートナーシップ |
| L3-3 避ける語彙 | **寄り添う**（自己満足化）／**サポーター**（影の従属感）／**お客様**（距離感・上下関係の匂い） |
```

- [ ] **Step 2: 4-B Principle 定義を書く**

```markdown
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
```

- [ ] **Step 3: 4-C 対応 Token を書く**

```markdown
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
```

- [ ] **Step 4: 4-D 実装シグナルを書く**

```markdown
### 4-D. 実装シグナル

- **Hero CTA**: `--color-drive` + `--shadow-2` 程度に抑制（`--shadow-5` は modal 専用、Hero では使わない）
- **Contact Form**: 「**お問い合わせ**」より「**共創パートナーとして話す**」の方向（fambox-contact-form.liquid 文言運用準拠）
- **Profile**: スポーツ栄養士を「**伴走者**」「**共創者**」として表現（fambox-profile.liquid 構造準拠）
- **Case Study**: 「クライアントの声」ではなく「**共創パートナーの実績**」（fambox-case-study.liquid 文言運用準拠）
- **Body コピーの主語**: 「**FAMBOX が提供する**」を避け、「**チームと FAMBOX が共に**」型を採用
- **新規 Component 設計時の Audit 質問**: 「主テキストに `--color-ink` を使っているか？避ける語彙（お客様/サポーター/寄り添う）が混入していないか？」
```

- [ ] **Step 5: Token 引用の実在検証**

Run:
```bash
grep -E "^\s*--(color-ink|color-sub|color-caption|fs-body|bg-primary|bg-secondary|bg-tertiary)" $JBR/snippets/fambox-tokens.css.liquid
```

Expected: 7 行以上 hit

- [ ] **Step 6: Commit**

```bash
git -C $JBR add brand/fambox/design-system/L0-translation-table.md
git -C $JBR commit -m "feat(L0): §4 Equal Partner 原則を執筆 (Session #55)"
```

---

## Task 5: §5 原則 4 Quiet Drive 執筆 (※ Token 値の事前検証必須)

**Files:**
- Modify: `brand/fambox/design-system/L0-translation-table.md` (§5 配下)

⚠️ **事前検証必須**: spec §3 で `--fs-display: 28px` と書いていたが、実際は `56px`（stat-focus value）。Quiet Drive の「低ジャンプ率」根拠は font-size scale 全体で議論する必要がある。

- [ ] **Step 1: Token 値の事前確認**

Run:
```bash
grep -E "^\s*--fs-(display|h[0-6]|body|caption)" $JBR/snippets/fambox-tokens.css.liquid
```

確認事項:
- `--fs-display` の実値（56px）
- 最大 size と body size の比（=ジャンプ率）
- 「低ジャンプ率」の主張根拠を、`--fs-display`(56) vs `--fs-body`(16) = 3.5x なのか、`--fs-h1`(?) vs body なのか整理

→ Step 3 の Token 表で **実値ベースで「低ジャンプ率」の根拠を再構成**

- [ ] **Step 2: 5-A DNA 由来 サブセクションを書く**

```markdown
### 5-A. DNA 由来

| DNA 要素 | 引用（v0.6.3 原文）|
|---|---|
| L3-2 Tone of Voice | 硬質×温度／確信と熱量を兼ねた洗練／**静かな自信**（誠実・愚直・実直）／**"引き算"の美学**（アシックス的本質主義）|
| L1-3 Brand Concept | **Your Step. Our Drive.** — あなたの挑戦が、スポーツの未来を動かす |
| L4-A 視覚言語 6 軸 (FAMBOX 4-6 位) | Propulsive (4) / Ascending (5) / Pulsing (6) — Quiet Drive に統合（演出補助） |
| L1-0 Anti | 表面的／派手／"映え"重視／盛り／キラキラ系ブランディング／過度な演出 |
| L1-4 Core Values #1 **Drive** | 推進力で前へ押し出す |
```

- [ ] **Step 3: 5-B Principle 定義を書く**

```markdown
### 5-B. Principle 定義

**一文**: "Our Drive" は **静かな自信と引き算** で表現し、派手・映え・キラキラを徹底的に Anti とする。

**解説**:
- Brand Concept "Drive" は維持。ただし「**派手な推進**」ではなく「**確信に裏打ちされた推進**」
- 色は `--color-drive: #FB4C15`（赤橙）を主軸とするが、glow 過多 / ネオン彩度 / 高彩度多色は禁止
- タイポは Display サイズを使うが、**多用しない**（1 画面 1 箇所程度。視覚的「叫び」を作らない）
- Shadow は `--shadow-1`〜`--shadow-2` を中心に。`--shadow-3`〜`--shadow-5` は modal/drawer 等の特殊用途のみ
- アニメは Continuity 原則の duration を踏襲。drive 演出のための独自モーションは作らない

**Do**:
- Drive 色は CTA / 重要アクセント / drive 強調の限定使用（面積比 5% 以下を目安）
- Display フォントは Hero の 1 箇所のみ、それ以外は H1-H3 で十分
- shadow は `--shadow-1`(hairline) / `--shadow-2`(card hover) を中心

**Anti**:
- 全面 drive 色塗り / 大面積使用
- 高彩度多色（neon green + neon pink 等）
- glow shadow 多用（`--color-drive-glow` の連続適用）
- Display サイズの multi-stack（巨大文字を連続配置）
- `--shadow-5: 0 24px 48px ...` を card に適用（modal の威圧感を card に持ち込む）
```

- [ ] **Step 4: 5-C 対応 Token を書く（Step 1 の実値で構成）**

```markdown
### 5-C. 対応 Token

| Token | 値 | なぜこの原則を支えるか |
|---|---|---|
| `--color-drive` | `#FB4C15` | Brand Concept "Drive" の核。彩度を抑えた赤橙で「派手すぎない推進」|
| `--color-drive-hover` | `#e14710` | hover でわずかに暗化し、過度な変化を避ける |
| `--color-drive-glow` | `rgba(251, 76, 21, 0.32)` | glow 用、ただし **連続適用禁止**（CTA の 1 箇所のみ） |
| `--fs-display` | 56px | Hero の **1 箇所のみ**。multi-stack 禁止 |
| `--fs-h1` 〜 `--fs-h3` | (実値は Step 1 で確認) | 通常見出しはここまで。Display は控える |
| `--shadow-1` | hairline | section 区切り |
| `--shadow-2` | card hover | card の lift 表現 |
| `--shadow-3` 〜 `--shadow-5` | (modal / drawer 用) | **Card 等の通常用途で使用禁止** |

**運用ルール**:
- `--color-drive` の面積比は画面の 5% 以下を目安
- `--fs-display` は Hero 1 箇所のみ（multi-stack 検出は Audit-first で行う）
- shadow level は 1-2 を基本、3 以上は modal/drawer の特殊用途のみ
```

- [ ] **Step 5: 5-D 実装シグナルを書く**

```markdown
### 5-D. 実装シグナル

- **Hero (fambox-hero-v17-video)**: Display サイズの大型見出し + `--color-drive` の CTA。background は静止画 or 控えめな motion
- **CTA Button**: `--color-drive` の Filled / hover で `--color-drive-hover`。`--color-drive-glow` は focus ring 用途のみ
- **Bento Grid Editorial preset**: drive 色は accent として 1 タイルにのみ採用（全タイル drive 色は Anti）
- **Stat Grid**: `--fs-display: 56px` で stat focus value。隣接 stat は `--fs-h2`/`--fs-h3` 程度に抑える
- **Shadow 使用箇所**: card hover = `--shadow-2`、modal = `--shadow-5`、drawer = `--shadow-4`。**card に shadow-5 を使うのは Anti**
- **新規 Component 設計時の Audit 質問**: 「drive 色の面積比は 5% 以下か？Display サイズの multi-stack はないか？shadow level は用途と合致しているか？」
```

- [ ] **Step 6: Token 引用の実在検証**

Run:
```bash
grep -E "^\s*--(color-drive|fs-display|fs-h[1-3]|shadow-[1-5])" $JBR/snippets/fambox-tokens.css.liquid
```

Expected: 全 Token が hit。hit しない場合は実装時に正しい token 名へ修正。

- [ ] **Step 7: Commit**

```bash
git -C $JBR add brand/fambox/design-system/L0-translation-table.md
git -C $JBR commit -m "feat(L0): §5 Quiet Drive 原則を執筆 (Session #55)"
```

---

## Task 6: §6 原則 5 Disciplined Craft 執筆

**Files:**
- Modify: `brand/fambox/design-system/L0-translation-table.md` (§6 配下)

- [ ] **Step 1: 6-A DNA 由来 サブセクションを書く**

```markdown
### 6-A. DNA 由来

| DNA 要素 | 引用 |
|---|---|
| L1-4 Core Values #6 **Integrity** (v0.6.3) | 誠実・実直・本物志向。アシックス的本質主義＝派手さよりも実用と成果で選ばれる立ち位置 |
| operations/2026-05-12-brand-dna-v0.4-draft.md Section D | **Disciplined**：何かを作る前に必ず既存資産を確認する。Audit-first protocol は DNA の実装規律として、視覚言語と同等の重要度を持つ |
| operations/2026-05-12-brand-dna-v0.4-draft.md Section A | Marc 流 4 層スタック（L1 Transport / L2 Skill / L3 Tokens / L4 Definitions / L5 Audit-first）|
| L1-4 Core Values #2 Science (副) | 根拠ある判断 — 直値ではなく Token を介す規律 |
```

- [ ] **Step 2: 6-B Principle 定義を書く**

```markdown
### 6-B. Principle 定義（横断的メタ原則）

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
```

- [ ] **Step 3: 6-C 対応 Token を書く**

```markdown
### 6-C. 対応 Token（命名規則と構造）

**命名規則**:
- 必須 prefix: `--color-` / `--space-` / `--fs-` / `--fw-` / `--bp-` / `--radius-` / `--shadow-` / `--motion-` / `--bg-` / `--border-` / `--glass-` / `--white-overlay-` / `--ink-overlay-`
- 修飾サフィックス: `-hover` / `-light` / `-sm` / `-md` / `-lg` / `-base` / `-slow` / `-fast`
- alias 構造: `--color-cta: var(--color-drive)` のような **意味への参照**を使う（§1-A 1-9 Semantic Alias 参照）

**主要 Token（Disciplined Craft が支える基盤）**:

| Token | 値 | 役割 |
|---|---|---|
| `--radius-xs`〜`--radius-pill` | 2/4/8/16/50%/50px/9999px | 角丸の表現規律。直値禁止 |
| `--bp-sp-sm`〜`--bp-pc-lg` | 480/767/768/...px | レスポンシブ規律 |
| `--space-0-5`〜`--space-8` | 4/8/12/...px | spacing の規律 |
| `--color-*` (semantic alias) | `--color-cta: var(--color-drive)` 等 | 意味と値の分離 |

**運用ルール**:
- 新規 Token 追加時は `current.md §1` と `snippets/fambox-tokens.css.liquid` を同時更新（学び 111）
- Tokens Studio との同期は `operations/scripts/tokens-studio-v05-complete.json` 経由
```

- [ ] **Step 4: 6-D 実装シグナルを書く**

```markdown
### 6-D. 実装シグナル

- **新規 Component 作成時の手順**（Audit-first protocol）:
  1. `current.md §7` 完成度ダッシュボードで既存 spec / Figma / Liquid の存在を確認
  2. `snippets/fambox-tokens.css.liquid` を grep して既存 token を確認
  3. SKILL `figma-component-from-spec` v0.7 の Step 0.5 Audit を実行
  4. 既存資産で代替できない場合のみ新規作成
- **Liquid 書式**: 全 fambox-* section は `{% render 'fambox-tokens.css' %}` を <head> 経由で参照（学び 95-96 / 22 sections 全 Token 化済）
- **三位一体の更新**: Component spec を変更したら、Figma Set と Liquid section も同タイミングで更新（current.md §7 N/3 ラベルで track）
- **新規 Component 設計時の Audit 質問**: 「既存 spec / Figma Set / Liquid section を全て読んだか？magic number は残っていないか？token 命名規則に従っているか？」
```

- [ ] **Step 5: Token 引用の実在検証**

Run:
```bash
grep -E "^\s*--(radius-|bp-|space-|color-cta)" $JBR/snippets/fambox-tokens.css.liquid
```

Expected: 各カテゴリで複数 hit

- [ ] **Step 6: Commit**

```bash
git -C $JBR add brand/fambox/design-system/L0-translation-table.md
git -C $JBR commit -m "feat(L0): §6 Disciplined Craft 原則を執筆 (Session #55)"
```

---

## Task 7: §7 原則間の優先度ルール + 衝突例 3 件

**Files:**
- Modify: `brand/fambox/design-system/L0-translation-table.md` (§7 配下)
- Source: spec §5（既に確定）の内容を本体に反映

- [ ] **Step 1: 7-1 矛盾時の優先順位**

```markdown
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
```

- [ ] **Step 2: 7-2 衝突例 3 件**

```markdown
### 7-2. 衝突例と解決

| # | 衝突 | 解決 |
|---|---|---|
| 1 | **Evidence-driven**（データ可視化で意味カテゴリを派手な色で目立たせたい）vs **Quiet Drive**（ネオン彩度禁止）| Evidence-driven が勝つ。ただし `--color-data-*` 6 色の範囲内で（Quiet Drive の Anti「ネオン彩度」「neon green+neon pink」は超えない） |
| 2 | **Continuity**（モーションを連続的に重ねたい）vs **Equal Partner**（控えめに）| Equal Partner 優先。`--motion-duration-base: 250ms` を超えるアニメ multi-stack 禁止。1 画面で同時 active な motion は 2 個まで |
| 3 | **Disciplined Craft**（Token 化を強制）vs **Evidence-driven**（実験的データ表現で新値が欲しい）| Disciplined Craft はメタ。実験データは **新規 token として追加**し命名規則に従う（Token 化を bypass せず、`--color-data-7` のように拡張）|
```

- [ ] **Step 3: 7-3 適用範囲の注意**

```markdown
### 7-3. 適用範囲の注意

- 優先順位は **設計判断が複数原則に分岐する場合**のみ参照（通常は複数原則を同時に満たす設計を目指す）
- **両立可能な場合は必ず両立させる**。優先順位は「妥協が必要な時の最後の判断材料」
- 順位が低い原則を「無視」してよい意味ではない（Quiet Drive 4 位でも `--color-drive` の派手使いは依然 Anti）
- **Disciplined Craft はすべての設計判断で並列適用**（順位の対象外）
```

- [ ] **Step 4: Commit**

```bash
git -C $JBR add brand/fambox/design-system/L0-translation-table.md
git -C $JBR commit -m "feat(L0): §7 原則間優先度ルール + 衝突例 3 件 (Session #55)"
```

---

## Task 8: §8 Token 逆引き表（10 カテゴリ × 5 原則）

**Files:**
- Modify: `brand/fambox/design-system/L0-translation-table.md` (§8 配下)

- [ ] **Step 1: 10 カテゴリの抽出**

current.md §1 のカテゴリ:
- 1-A. Color Tokens
- 1-B. Typography Tokens
- 1-C. Spacing Tokens
- 1-D. Motion Tokens
- 1-E. Elevation / Shadow Tokens
- 1-F. Radius Tokens
- 1-G. Breakpoint Tokens
- 1-H. Z-index Tokens
- 1-I. Icon Tokens
- 1-J. Variable Mode（端末別・テーマ別切替）

- [ ] **Step 2: 逆引き表を書く**

```markdown
### 8. Token 逆引き表（Token カテゴリ → 関連原則）

凡例: ● = 主導原則 / ○ = 副次的に関与 / — = 無関係

| Token カテゴリ | Evidence-driven | Continuity | Equal Partner | Quiet Drive | Disciplined Craft |
|---|---|---|---|---|---|
| **1-A. Color** | ●（`--color-data-*`）| — | ●（`--color-ink/sub/caption/bg-*`）| ●（`--color-drive*`）| ○（命名規則）|
| **1-B. Typography** | ●（`--fs-caption*`, `--fw-medium`）| ○（`--lh-base` リズム）| ●（`--fs-body`）| ●（`--fs-display`, jump rate 制御）| ○（命名規則 `--fs-*` / `--fw-*`）|
| **1-C. Spacing** | — | ●（等比スケール）| ○（hierarchy）| — | ●（規律 / 直値禁止）|
| **1-D. Motion** | — | ●（`--motion-duration-*`）| ○（控えめさ）| ○（drive 演出抑制）| ●（命名規則 `--motion-*`）|
| **1-E. Shadow** | — | — | ○（威圧抑制）| ●（`--shadow-1〜2` / `--shadow-5` の用途制限）| ○（命名規則）|
| **1-F. Radius** | — | — | — | ○（過度な角丸の抑制）| ●（`--radius-*` 7 値）|
| **1-G. Breakpoint** | — | ○（連続的レスポンシブ）| — | — | ●（`--bp-*` 規律）|
| **1-H. Z-index** | — | — | ○（modal 階層）| — | ●（直値禁止）|
| **1-I. Icon** | — | — | ○（Lucide 1.5px / 控えめさ）| ●（誠実・控えめ）| ●（Lucide 採用規律）|
| **1-J. Variable Mode** | — | ○（dark mode で continuity 維持）| ○（brand mode で対等の距離感を保つ）| ●（FAM brand mode で drive 色切替）| ●（mode 規律 `[data-brand]`）|
```

- [ ] **Step 3: Token カテゴリ 10 件カバー検証**

Run:
```bash
grep -c "^| \*\*1-" $JBR/brand/fambox/design-system/L0-translation-table.md
```

Expected: `10`（10 カテゴリ全て表に登場）

- [ ] **Step 4: 主導原則の偏り検証**

各原則の ● カウントが 2-4 件あることを目視確認:
- Evidence-driven: ● Color / Typography → 2 個
- Continuity: ● Spacing / Motion → 2 個
- Equal Partner: ● Color / Typography → 2 個
- Quiet Drive: ● Color / Typography / Shadow / Icon → 4 個
- Disciplined Craft: ● Spacing / Motion / Radius / BP / Z-index / Icon / VarMode → 7 個（横断のため多くて OK）

→ 偏りが極端な場合（0 個など）は割り当てを再検討

- [ ] **Step 5: Commit**

```bash
git -C $JBR add brand/fambox/design-system/L0-translation-table.md
git -C $JBR commit -m "feat(L0): §8 Token 逆引き表 10 カテゴリ × 5 原則 (Session #55)"
```

---

## Task 9: current.md §6 リンク追加 + Final self-verification + commit

**Files:**
- Modify: `brand/fambox/design-system/current.md` (§6 内に L0-translation-table.md へのリンク追加)

- [ ] **Step 1: current.md §6 にリンク追加**

`current.md` を読み、§6 の 3 階層翻訳表の骨格図の **直後**に以下を追加:

```markdown
### L0 翻訳表本体

> 上記の翻訳①②③の **本体実装**: [L0-translation-table.md](L0-translation-table.md) v0.1 (2026-05-19 / Session #55)
> - DNA v0.6.3 → 5 Design Principles → 133 Tokens の対応表
> - 原則間の優先度ルール + Token 逆引き表 10 カテゴリ × 5 原則
> - DNA v1.0（2026-06-30）確定まで段階更新
```

挿入位置: `## 6. Brand DNA との接続` の図ブロック直後（行 ~588 付近 / `└────────────────────┘` の直後）。

実際の挿入は Edit ツールで `└────────────────────┘\n```` の直後に追加する。

- [ ] **Step 2: Final self-verification（成功基準 7 項目チェック）**

spec §7 の受け入れ条件に対して 1 つずつ verify:

```bash
# 1. 5 原則すべてに A-D 4 サブセクションが揃っている
grep -cE "^### [2-6]-[A-D]\." $JBR/brand/fambox/design-system/L0-translation-table.md
# Expected: 20 (5 原則 × 4 サブセクション)

# 2. 各原則の Token 引用が snippets に実在
# 既に各 Task の Step 5/6 で検証済

# 3. 原則間の優先度ルールが衝突例 3 件以上
grep -cE "^\| [0-9] \|" $JBR/brand/fambox/design-system/L0-translation-table.md
# §7-2 表で 3 件あること（Expected: 3 以上）

# 4. Token 逆引き表が 10 カテゴリすべてカバー
grep -c "^| \*\*1-" $JBR/brand/fambox/design-system/L0-translation-table.md
# Expected: 10

# 5. current.md §6 から本ファイルへの参照リンクが追加されている
grep -c "L0-translation-table.md" $JBR/brand/fambox/design-system/current.md
# Expected: 1 以上

# 6. frontmatter の Status は `draft (DNA v0.6.3 ベース)`
grep "^status:" $JBR/brand/fambox/design-system/L0-translation-table.md
# Expected: status: draft (DNA v0.6.3 ベース)

# 7. 全体行数: 250-350 行（目標）
wc -l $JBR/brand/fambox/design-system/L0-translation-table.md
# Expected: 250-350 行
```

すべて Expected に合致しなければ、該当タスクに戻って修正。

- [ ] **Step 3: 最終 Commit + 全タスク完了マーク**

```bash
git -C $JBR add brand/fambox/design-system/current.md brand/fambox/design-system/L0-translation-table.md
git -C $JBR commit -m "$(cat <<'EOF'
feat(L0): 翻訳表 v0.1 完成 + current.md §6 リンク追加 (Session #55)

== Phase A 完遂 ==
brand/fambox/design-system/L0-translation-table.md (~XXX 行) を新規作成。
DNA v0.6.3 → 5 Design Principles → 133 Tokens の対応表を確立。
OKR Task 1-2-a 「DS 作成」期限 2026-06-30 直結。

== 内容 ==
- §0 翻訳の流れ + §1 5 原則早見表
- §2-§6 5 原則 (Evidence-driven / Continuity / Equal Partner /
  Quiet Drive / Disciplined Craft) × 4 サブセクション
  (DNA 由来 / Principle 定義 / 対応 Token / 実装シグナル)
- §7 原則間優先度ルール + 衝突例 3 件
- §8 Token 逆引き表 (10 カテゴリ × 5 原則)
- §9 改訂履歴 v0.1

== 統合根拠 ==
視覚言語 6 軸 (FAMBOX 優先順) を 5 原則に統合:
1位 Scientific/Personalized → Evidence-driven
2位 Continuity              → Continuity
3位 Co-driven               → Equal Partner
4-6位 Propulsive/Ascending/Pulsing → Quiet Drive (吸収)
v0.4 draft Disciplined      → Disciplined Craft (横断メタ)

== 検証 ==
- 5 原則 × 4 サブセクション = 20 セクション全揃え
- Token 引用は snippets/fambox-tokens.css.liquid に実在検証済
- 衝突例 3 件、Token カテゴリ 10 件カバー

next: 宮川さんレビュー → OKR Task 1-2-a 進捗反映 (FAMBOX_OKR_宮川.xlsx)

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

- [ ] **Step 4: 完了報告**

最終 commit hash を確認し、ユーザーに以下を報告:
1. 完成 commit hash
2. 全体行数（spec §7 受け入れ条件: 250-350 行）
3. 7 項目チェックリストの結果
4. 次のアクション提案:
   - 宮川さんレビュー
   - OKR Excel の進捗反映（FAMBOX_OKR_宮川.xlsx）
   - PR #1 への push（リモート同期）

---

## Self-Review（writing-plans skill の checklist）

### 1. Spec coverage

| spec §X | 該当 Task | 状態 |
|---|---|---|
| §0 背景と目的 | (本体実装には反映不要、spec 側で完結) | ✅ |
| §1 スコープ | Task 1 frontmatter / 全 Task の本文構成 | ✅ |
| §2 ファイル位置と命名 | Task 1 frontmatter / Task 9 | ✅ |
| §3 5 原則最終確定 | Task 2-6 | ✅ |
| §3 後半 6 軸統合根拠 | Task 1 §0 翻訳の流れ図 / §9 final commit message | ✅ |
| §4 heading 構造 | Task 1 skeleton | ✅ |
| §5 原則間の優先度ルール | Task 7 | ✅ |
| §6 翻訳表が固定するもの・段階更新 | Task 1 frontmatter `status: draft` / 改訂履歴 | ✅ |
| §7 成功基準 7 項目 | Task 9 Step 2 final self-verification | ✅ |
| §8 実装フロー | 本 plan 自体が実装フロー | ✅ |
| §9 リスクと対策 | Quiet Drive ネーミング → Task 5 §5-B 解説 / fs-display 値 → Task 5 Step 1 事前検証 | ✅ |

→ spec のすべての要件が plan のいずれかの task でカバーされている。

### 2. Placeholder scan

- "TBD" / "TODO" / "implement later" → なし
- "Add appropriate error handling" → なし（markdown 文書のため該当せず）
- "Write tests for the above" → なし（成功基準 7 項目で代替）
- "Similar to Task N" → なし（各 Task で本体内容を独立記載）

→ Placeholder なし。

### 3. Type consistency

- Token 名: 全 Task で `snippets/fambox-tokens.css.liquid` を真実の源として grep 検証
- セクション heading: Task 1 で skeleton 確定後、Task 2-9 で内容を追記（heading 名の不整合なし）
- DNA 引用元: 「L1-4 Core Values #N」「L4-A 視覚言語 6 軸」等の表記を全 Task で統一
- 5 原則名: Evidence-driven / Continuity / Equal Partner / Quiet Drive / Disciplined Craft を全 Task で同一表記

→ 不整合なし。

---

## 想定実装時間

| Task | 内容 | 所要 |
|---|---|---|
| 1 | Skeleton + §0 + §1 + §9 骨格 | 15 min |
| 2 | §2 Evidence-driven | 12 min |
| 3 | §3 Continuity | 12 min |
| 4 | §4 Equal Partner | 12 min |
| 5 | §5 Quiet Drive（Token 値事前検証あり）| 15 min |
| 6 | §6 Disciplined Craft | 12 min |
| 7 | §7 優先度ルール + 衝突例 | 8 min |
| 8 | §8 Token 逆引き表 | 12 min |
| 9 | current.md §6 リンク + final verification + commit | 10 min |
| **合計** | | **~108 min** |

spec の想定 60-90 min をやや超過するが、Token 検証ステップで品質ゲートを通すため許容範囲。

---

## 関連参照

- 設計 spec: `docs/superpowers/specs/2026-05-19-fambox-l0-translation-table-design.md` (commits 7a82e54 + cad0ef3)
- DNA 由来: `brand/fambox/brand-dna/current.md` v0.6.3
- Token 検証対象: `snippets/fambox-tokens.css.liquid` v0.5（133 tokens）
- 既存 DS 構造: `brand/fambox/design-system/current.md` §5-§7
- v0.4 draft: `operations/2026-05-12-brand-dna-v0.4-draft.md`
- OKR: `FAMBOX_OKR_宮川.xlsx`（Task 1-2-a / 期限 2026-06-30）
