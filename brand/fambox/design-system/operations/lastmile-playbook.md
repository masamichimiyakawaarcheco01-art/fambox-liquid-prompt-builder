---
title: FAMBOX Last-Mile Playbook（AI生成→人補正のSOP）
type: design-system-operations
layer: L7-Operations
status: active
last_updated: 2026-04-20
owner: 宮川
strategy_source: 須藤さんとの会話「共存のバトンパス」「他社が真似できない領域」
purpose: AI生成物の残5%をFAM品質まで持ち上げる補正パターンを蓄積し、再現可能な型として運用する
---

# FAMBOX Last-Mile Playbook

## 戦略的意図（前提）

> 「FAMデザインシステムを **入口の支配** とし、**ラストワンマイル補正** を **出口の独占** にする」

| 層 | 担当 | 目的 |
|---|---|---|
| **入口** | Design System (MD/Figma) | 誰がClaude Designを叩いても **FAM 95%** が出る |
| **出口（本書）** | Last-Mile Playbook | 残5%のFAMらしさを **再現可能な型** にする |

→ AI生成・人補正のバトンパスをSOP化することで、**他社がコピーできない競争優位** を作る。

---

## 補正パターン4カテゴリ

宮川さんの「感覚的に分かる違和感」を **4つの観点** に分類して言語化する。

### 1. 余白（Spacing）
AIは「無難な余白」を出力する。FAMは **「呼吸する余白」「TNF級の大きな余白」** を必要とする。

### 2. コピー（Copy）
AIは「説明的なコピー」を出す。FAMは **「呼吸のあるコピー」「動詞起点」「背中をそっと押す語感」** を必要とする。

### 3. マイクロインタラクション（Micro-interaction）
AIは「標準のhover/transition」を出す。FAMは **「呼吸アニメ」「Drive方向（前方向1-2px）」「ease-in主体」** が必要。

### 4. ブランド固有のディテール（Brand Detail）
AIは「業界標準の見た目」を出す。FAMは **「Editorial × Lab」「アシックス的本質主義」** に固有のディテールが必要。

---

## 補正パターン記録テンプレート

各補正は以下のフォーマットで記録:

```markdown
## CORRECTION-{ID}: 短い表題

### When（いつ）
- 日付: 2026-04-20
- 案件: TOPページ Hero リファクタ
- AI: Claude Design v0.X

### What — AIが生成したもの
（コードスニペット or スクショ）

### Correction — 補正後
（コードスニペット or スクショ）

### Why — なぜ補正が必要だったか
- DNA / DS のどの原則に違反していたか
- 体感的な違和感の言語化

### Category
- [ ] 余白 / [ ] コピー / [ ] マイクロ / [ ] ブランドディテール

### Prevention — 次回防ぐには
- DS or playbook をどう更新すべきか
```

---

## 補正パターン蓄積（実例）

> **このセクションは案件をこなすたびに追記する**。最初は空でOK。型が溜まると判断速度が上がる。

### CORRECTION-001（雛形例）: ボタン余白が窮屈
- **When**: 2026-04-XX / TOP Hero
- **What**: AI生成 `padding: 8px 16px` → 上下窮屈
- **Correction**: `padding: 16px 32px` に拡大、`btn-lg` Size で `--space-2`/`--space-5` 適用
- **Why**: FAM v0.5 「TNF級の大きな余白」原則。AIは "コンパクトCTA" 寄りに最適化されがち
- **Category**: ☑ 余白
- **Prevention**: button.md に「Hero Primary は必ず `btn-lg`」と明記済（v0.2 で対応）

### CORRECTION-002（雛形例）: コピーが説明的すぎる
- **When**: 2026-04-XX / 問合せセクション
- **What**: AI生成「お問い合わせはこちらから」
- **Correction**: 「話を聞いてみる」
- **Why**: 「〜してみる」試行性で背中押し / Brand DNA Co-driven 原則 / 「お客様」表現排除
- **Category**: ☑ コピー
- **Prevention**: cta-wording-proposal.md に確定（v0.2）

### CORRECTION-003（雛形例）: hover が動かない
- **When**: 2026-04-XX / Card 一覧
- **What**: AI生成 `transition: opacity 0.3s` のみ
- **Correction**: `transform: translateY(-2px)` 追加（前方向ホバー）
- **Why**: FAM視覚軸1 Propulsive（推進）「Drive 方向ホバー」原則。透明度変化だけだと FAM らしさが消える
- **Category**: ☑ マイクロ
- **Prevention**: motion.md に「ホバーは前方向 1-2px」明記済

### CORRECTION-004（雛形例）: グレースケール写真が過剰加工
- **When**: 2026-04-XX / Case Study Hero
- **What**: AI生成: 高彩度モデル写真
- **Correction**: コントラスト高め・彩度抑制・現場風景に差し替え
- **Why**: Brand DNA L4-15「装飾過多の料理写真NG / モデル的ポージングNG / 現場の手OK」
- **Category**: ☑ ブランドディテール
- **Prevention**: L4-15 写真主題を Anti-list 充実

### CORRECTION-005（雛形例）: 価格を煽っている
- **When**: 2026-04-XX / 定期便プラン
- **What**: AI生成: `font-size: 64px` Drive色 価格
- **Correction**: `font-size: 32px` Ink色 + 「税込」併記
- **Why**: Brand DNA Integrity「結果保証ではなく価値で選ばれる」/ Anti「煽り表現」
- **Category**: ☑ ブランドディテール
- **Prevention**: subscription-plan-card.md で価格 h2/Ink 明記済（v0.2）

---

## 案件記録ログ（テンプレ）

各案件で発生した補正を記録:

```markdown
## 案件 {YYYY-MM-DD-案件名}

### 概要
- 案件: 〇〇ページのリファクタ
- AI: Claude Design / Code 等
- 補正対象ファイル: 〇〇.liquid

### 発生した補正
- CORRECTION-XXX: 〇〇
- CORRECTION-XXX: 〇〇

### 学び
（次回への示唆）
```

→ 案件ログを蓄積することで、AI生成プロンプトの改善ヒントが見える。

---

## DS との接続（フィードバックループ）

```
AI生成 → 人補正 → 補正記録（本書）
                ↓
          パターン化・型化
                ↓
       DS or プロンプトに反映
                ↓
       次回 AI生成の品質向上 ↑
```

### Prevention 反映先
| Category | 反映先 |
|---|---|
| 余白 | `tokens/spacing.md` の Do/Don't |
| コピー | `cta-wording-proposal.md` / 言葉遣いガイド |
| マイクロ | `tokens/motion.md` の運用パターン |
| ブランドディテール | `current.md` (DS全体) の Anti-list / 写真主題 |

---

## Claude 向けプロンプトの改善ポイント

蓄積された補正パターンを Claude に投入する際のプロンプトテンプレ:

```
あなたは FAMBOX の Brand DNA / Design System に従ってデザイン/コード生成します。
特に以下の Last-Mile 補正パターンに注意してください:

[CORRECTION-001] Hero CTA は必ず btn-lg / padding 16px 32px 以上
[CORRECTION-002] CTAコピーは「〜してみる」試行形・「お客様」禁止
[CORRECTION-003] hover は transform translateY(-2px)（前方向）
[CORRECTION-004] 写真は現場の手・素直さ重視・スタジオ過剰演出NG
[CORRECTION-005] 価格は h2 サイズ Ink色（Drive煽り禁止）

参照ファイル:
- brand/fambox/design-system/current.md
- brand/fambox/design-system/operations/lastmile-playbook.md
```

---

## 評価基準: ラストマイル補正の質

宮川さんの**感覚的な「ピンとこない」**を**数値化**するための問いかけ:

### 4軸チェック
- 🎯 **余白**: 8の倍数になっているか / TNF級の余白を確保しているか
- 🎯 **コピー**: 「〜してみる」 or 動詞起点 / 「お客様」禁句チェック
- 🎯 **マイクロ**: ease-in 主体 / 前方向ホバー / 呼吸アニメは主要CTAだけ
- 🎯 **ディテール**: Anti-list に該当しないか / FAMらしさが3要素以上含まれるか

### スコアリング
| 軸 | 0-25点 |
|---|---|
| 余白 | 0-25 |
| コピー | 0-25 |
| マイクロ | 0-25 |
| ディテール | 0-25 |
| **合計 100点** | 95点以上で本番採用OK / 80-94点で修正必要 |

---

## 段階運用（v0.X → v1.0）

### v0.2（現在 = 2026-04-20）
- 雛形5件
- 4カテゴリ確立

### v0.3（5月末まで）
- 案件3件以上で発生した補正を記録
- 計15-20件の蓄積目標

### v0.4（6月末まで）
- カテゴリ別の頻出パターンを抽出
- DS への反映タスクを生成

### v1.0（9月末まで）
- 50件以上のパターン
- Claude 向けプロンプトテンプレ完成
- AI生成→補正の Time to Ship 平均30分以内達成

---

## 競争優位の構造（須藤さん談との接続）

```
他社のAI活用            FAMBOXのAI活用
─────────────────       ─────────────────
AI生成 → そのまま納品    AI生成 → DS で 95%
                              ↓
                        Last-Mile 補正で 100%
                              ↓
                        補正パターン蓄積
                              ↓
                        DS / プロンプト更新
                              ↓
                        次回 AI生成の質向上 ↑
                        ↓
                        圧倒的な品質差・速度差
```

→ **「DS as 入口の支配」+「Playbook as 出口の独占」** で他社が真似できない領域を確立。

---

## 関連ファイル
- [current.md](../current.md) — DS全体
- [naming-conventions.md](naming-conventions.md) — 命名規則（次タスク）
- [contribution.md](contribution.md) — 貢献フロー（次タスク）
- [Brand DNA current.md](../../brand-dna/current.md) — ブランド原則
