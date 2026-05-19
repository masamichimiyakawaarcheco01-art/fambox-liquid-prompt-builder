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

## 3. 原則 2: Continuity

## 4. 原則 3: Equal Partner

## 5. 原則 4: Quiet Drive

## 6. 原則 5: Disciplined Craft

## 7. 原則間の優先度・矛盾時の解決ルール

## 8. Token 逆引き表

## 9. 改訂履歴

- v0.1 (2026-05-19 / Session #55): 初稿。DNA v0.6.3 ベース、5 原則確定（Evidence-driven / Continuity / Equal Partner / Quiet Drive / Disciplined Craft）、Token 逆引き表 10 カテゴリ × 5 原則。spec: `docs/superpowers/specs/2026-05-19-fambox-l0-translation-table-design.md`
