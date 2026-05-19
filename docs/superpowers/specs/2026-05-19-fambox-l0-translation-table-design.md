---
title: FAMBOX DS — L0 翻訳表ドラフト 設計 spec
type: spec
date: 2026-05-19
status: draft（承認待ち）
session: Phase A (Session #55)
purpose: DNA → Design Principles → Token 名 の対応表（L0 翻訳表）の構造設計を確定し、本体作成の前提を固める
target_implementation_file: brand/fambox/design-system/L0-translation-table.md
related:
  - brand/fambox/brand-dna/current.md（DNA v0.6.3 / 由来）
  - brand/fambox/design-system/current.md §6（Brand DNA との接続）
  - brand/fambox/design-system/operations/2026-05-12-brand-dna-v0.4-draft.md
  - snippets/fambox-tokens.css.liquid（133 tokens v0.5）
okr_link: OKR Task 1-2-a 「DS 作成」期限 2026-06-30 直結
---

# FAMBOX DS — L0 翻訳表 設計 spec

## 0. 背景と目的

### 背景

FAMBOX DS は L1 Tokens（133 個 / Tokens Studio v0.5）と L2-L4（Primitives / Patterns / Components）の三位一体達成（10/11）に到達。しかし **L0 = Foundation（原則・哲学）** が「DNA 由来の Design Principles」として未言語化のまま。

これは「**新規 Component / Token を追加する時、何を基準に判断するか**」という意思決定の根拠が個別判断に依存している状態を意味する。Phase A（本タスク）で「DNA → Design Principles → Token 名」の対応表を作成し、L0 を初めて構造化する。

### 目的

1. **設計判断の根拠化** — Token / Component 追加時の「なぜこの値か」を Principle で説明できる
2. **DNA 進化（v0.6.3 → v1.0 2026-06-30）への対応** — 原則と構造は固定、値だけ段階更新
3. **FAM brand mode への接続** — 同一原則・異なる Token 値で `[data-brand="fam"]` override を実現する設計基盤
4. **OKR Task 1-2-a 直結** — 期限 2026-06-30 に向けた DS 作成の中核成果物

## 1. スコープ

### 含むもの

- 5 Design Principles の定義（DNA 由来の説明 + 一文定義 + Anti）
- 各原則と Token カテゴリの対応
- 原則間の優先度・矛盾解決ルール
- Token 逆引き表（Token カテゴリ → 関連原則）

### 含まないもの（YAGNI）

- 個別 Component spec の改訂（L2-L4 は既存 spec を保つ）
- Token 値の変更（v0.5 値のまま運用）
- FAM brand mode の具体的 override 値（FAM brand 値確定後の別タスク）
- Anti を超えた「実装禁止リスト」の網羅（L7 Operations 領域）

## 2. ファイル位置と命名

| 項目 | 値 |
|---|---|
| 本体ファイル | `brand/fambox/design-system/L0-translation-table.md` |
| 位置づけ | DS spec 正式ファイル（drafts/ 配下ではない） |
| Status マーカー | frontmatter に `status: draft (DNA v0.6.3 ベース)` を明記 |
| commit worktree | `jovial-benz-resume`（branch `claude/jovial-benz-864b2d`）|
| 参照元 | `current.md §6 Brand DNA との接続` の図に「L0 翻訳表へ」リンク追加 |

## 3. 5 原則（最終確定）

| # | Principle | DNA 由来 | 主要 Token カテゴリ | Anti（避けるミス）|
|---|---|---|---|---|
| 1 | **Evidence-driven** | L1-4 Science / L4-A 視覚軸1位 Scientific-Personalized / L1-6「可能性の確率」 | `--color-data-*` 6色 / `--fs-caption*` 階層 / `--fw-medium` | 数字を装飾扱い／グラフを派手色／"効果保証"風文言 |
| 2 | **Continuity** | L1-4 Continuity / L4-A 視覚軸2位 Continuity / 定期便文脈 | `--space-*` 等比 / `--motion-duration-base: 250ms` / `--border-light` リズム | スペーシング等差／急峻なモーション／段差の大きすぎる視覚リズム |
| 3 | **Equal Partner** | L3-5「共創者 Equal Partner in Challenge」/ L4-A 視覚軸3位 Co-driven / L1-4 Together | `--color-ink: #1b1d1a` / `--fs-body: 16px` / `--bg-*` 3階層 | 過剰演出／Hero CTA の威圧／"お客様"距離感の語彙 |
| 4 | **Quiet Drive** | L3-2 Tone「静かな自信」「引き算」/ L1-3 Brand Concept "Our Drive" / L1-0 Anti「派手・映え」 | `--color-drive: #FB4C15`（抑えた赤橙）/ `--fs-display: 28px`（低ジャンプ率）/ `--shadow-1` 控えめ | ネオン彩度／高ジャンプ率／ドロップシャドウ濫用／glow 過多 |
| 5 | **Disciplined Craft** | L1-4 Integrity / v0.4 draft Section D / Audit-first protocol | Token 命名規則（kebab-case + prefix）/ `--radius-*` 4 値 / `--bp-*` Breakpoint | Magic number 残存／Token を bypass した直値／spec-Figma-Liquid の乖離 |

### 6 視覚言語軸 → 5 原則 への統合根拠

| FAMBOX 視覚言語 6 軸 | 統合先 Principle |
|---|---|
| ①Scientific / Personalized（1位）| 1. Evidence-driven |
| ②Continuity（2位）| 2. Continuity |
| ③Co-driven（3位）| 3. Equal Partner |
| ④Propulsive（4位）| 4. Quiet Drive（"Drive" 本体） |
| ⑤Ascending（5位）| 4. Quiet Drive（演出補助として吸収） |
| ⑥Pulsing（6位）| 4. Quiet Drive（演出補助として吸収） |
| 〔v0.4 draft 提案〕Disciplined | 5. Disciplined Craft |

→ **6 軸 → 5 原則の損失なし統合**。視覚言語 4-6 位は単独で principle になるほど主軸ではないため、Brand Concept "Drive" を中核とする Quiet Drive に統合（"静かな自信 + 引き算" との両立で「派手な推進力」を抑制）。

## 4. 翻訳表本体の heading 構造

```markdown
# FAMBOX DS — L0 翻訳表 v0.1
（frontmatter）
## 0. 翻訳の流れ（DNA → Principles → Tokens → Components の図）
## 1. 5 原則 早見表（1 行サマリ × 5）
## 2. 原則 1: Evidence-driven
   2-A. DNA 由来 / 2-B. Principle 定義 / 2-C. 対応 Token / 2-D. 実装シグナル
## 3. 原則 2: Continuity
## 4. 原則 3: Equal Partner
## 5. 原則 4: Quiet Drive
## 6. 原則 5: Disciplined Craft
## 7. 原則間の優先度・矛盾時の解決ルール
## 8. Token 逆引き表（Token カテゴリ → どの原則を支えるか）
## 9. 改訂履歴
```

各原則セクション（## 2 〜 ## 6）の 4 サブセクション:

- **A. DNA 由来** — L1/L3/L4 のどこから来たか、引用付き
- **B. Principle 定義** — 一文 + 5-10 行の解説 + Do/Anti の 1 行例 3-5 個
- **C. 対応 Token** — 主要 token と「なぜこの値を選ぶか」のロジック
- **D. 実装シグナル** — Component 設計で守るべき判断基準（Hero / CTA / Card 等の具体場面）

## 5. 原則間の優先度ルール

### 5-1. 矛盾時の優先順位

```
Evidence-driven > Continuity > Equal Partner > Quiet Drive > Disciplined Craft
（最上位）                                              （横断・メタ）
```

理由:
- B2B / スポーツ栄養 / 法人購買が主軸 → 論理的、スポーツ栄養学的、実績的に根拠が最上位、信頼が重要である
- Continuity = 定期便文脈の継続性（事業モデル直結）
- Equal Partner = 関係性の核（共創者）
- Quiet Drive = ビジュアル trait
- **Disciplined Craft は横断的メタ原則** — 他 4 原則の適用すべてに Audit-first を上乗せ（順序判定の対象外）

### 5-2. 衝突例と解決

| 衝突 | 解決 |
|---|---|
| Evidence-driven（データ可視化を派手な色で目立たせたい）vs Quiet Drive（ネオン彩度禁止）| Evidence-driven が勝つ。ただし `--color-data-*` 6 色の範囲で（Quiet Drive の Anti「ネオン彩度」は超えない） |
| Continuity（モーションを連続的に）vs Equal Partner（控えめに）| Equal Partner 優先。`--motion-duration-base: 250ms` を超えるアニメ multi-stack 禁止 |
| Disciplined Craft（Token 化）vs Evidence-driven（実験的データ表現）| Disciplined Craft はメタ。実験データは新規 token として追加し命名規則に従う（Token 化を bypass せず） |

## 6. 翻訳表が固定するもの・段階更新するもの

| 要素 | DNA v0.6→v1.0 で変わる | 翻訳表で固定 |
|---|---|---|
| 原則名 | — | ✅ 5 つ固定 |
| 原則の定義文 | DNA v0.7+ で精緻化 | 構造は固定 |
| Token 値 | 値は変動（FAM brand mode の `[data-brand="fam"]` override 想定）| Token カテゴリは固定 |
| 実装シグナル | Component spec の進化で追加 | 既存 5 シグナルは追加のみ |
| Anti 項目 | DNA L1-0 Anti の更新で追加可 | 既存 Anti は削除しない（履歴として残す）|

## 7. 成功基準（受け入れ条件）

- [ ] 5 原則すべてに A-D 4 サブセクションが揃っている
- [ ] 各原則の Token 引用がすべて `snippets/fambox-tokens.css.liquid` 内に存在する（実在検証）
- [ ] 原則間の優先度ルールが衝突例 3 件以上で検証されている
- [ ] Token 逆引き表が 10 カテゴリ（1-A 〜 1-J）すべてカバー
- [ ] current.md §6 から本ファイルへの参照リンクが追加されている
- [ ] frontmatter の Status は `draft (DNA v0.6.3 ベース)` を明記
- [ ] 全体行数: 250-350 行（目標）

## 8. 実装フロー

```
本 spec 承認
    ↓
writing-plans skill 起動 → 実装計画作成
    ↓
L0 翻訳表本体を brand/fambox/design-system/L0-translation-table.md に作成
    ↓
current.md §6 にリンク追加
    ↓
self-verification（成功基準チェックリスト 7 項目）
    ↓
宮川さんレビュー → 承認
    ↓
PR #1 にコミット（Session #55 マーカー）
    ↓
OKR Task 1-2-a の進捗反映（FAMBOX_OKR_宮川.xlsx）
```

## 9. リスクと対策

| リスク | 対策 |
|---|---|
| DNA v1.0 確定時に原則名を変更する必要が生じる | 5 原則は「機能カテゴリ」として抽象化、DNA の細部表現変更には影響されない命名 |
| L4-A 視覚軸 6 軸の優先順位が v0.7 で再シャッフル | 翻訳表は「視覚軸 → 原則への統合根拠」を §3 に明示し、再統合の根拠を残す |
| Quiet Drive の "静かな" が Brand Concept "Drive" と矛盾と読まれる | §3 で「Drive ＝ Brand Concept 中核は維持、ただし "派手な推進" は Anti」と明記 |
| Disciplined Craft が横断的メタ原則として「他 4 原則と同列ではない」感が伝わらない | §5-1 で「Disciplined Craft は横断・メタ」を明示、優先順位の対象外と書く |

## 10. 関連参照

- DNA: `brand/fambox/brand-dna/current.md` v0.6.3
- DS 現状: `brand/fambox/design-system/current.md` §5（残論点 4 件決定済）/ §6（Brand DNA との接続）/ §7（完成度ダッシュボード）
- v0.4 draft 提案: `operations/2026-05-12-brand-dna-v0.4-draft.md`（6 軸目 Disciplined 追加案 — 本 spec で吸収）
- Token: `snippets/fambox-tokens.css.liquid`（133 tokens v0.5）/ Tokens Studio JSON `operations/scripts/tokens-studio-v05-complete.json`

## 改訂履歴

- v0.1 (2026-05-19 / Session #55): 初稿。5 原則 + Approach B セクション型 + 統合根拠 + 優先度ルール。
