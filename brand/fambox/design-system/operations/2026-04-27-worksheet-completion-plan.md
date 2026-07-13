---
title: DS_INPUT_WORKSHEET 完了計画 v0.2 (S1-S3)
type: design-system-operations
layer: L7-Operations
status: active
created: 2026-04-27
owner: 宮川
purpose: Worksheet §4-§14 の意思決定を3セッションで完了し、Tokens/Components/Worksheet/CHANGELOG を同期反映。Figma Step 6-7 と Primitive 設計の着手可能状態を作る。
---

# Worksheet 完了計画（2026-04-27）

## Goal
Worksheet §4-§14 の意思決定をチャット上で完了し、関連 Spec ファイルに同期反映。Figma Step 6-7 と Primitive 設計を着手可能な状態にする。

## 前提状態（2026-04-27 時点）
- Figma master file: `QsiBrc2v20BYw76YHI9x3e`、Step 1-5（ファイル/ページ/Variables/Text Styles/Effect Styles）完了
- Worksheet §1-§3: 部分回答済（color alias / typography 微調整 → tokens.css 反映済）
- v0.2 期限: 5月上旬（DS マイルストーン）

## Sessions

| # | カバー範囲 | 出力ファイル |
|---|---|---|
| **S1** ✅ 完了 (2026-04-27) | §4 Z-index / §5 Icons / §6 Button | Worksheet §4-§6 同期 + button.md v0.3 stable（5 Variant）+ icon-creation-spec.md 訂正（24×24 化）+ CHANGELOG |
| **S2** ✅ 完了 (2026-04-27) | §7 Input / §8 FormField / §9 Avatar / §10 Form Controls / §11 Progress | Worksheet 同期のみ（Spec は 2026-04-20 で confirmed 済）/ CHANGELOG.md。合成決定 §9.4・§11.3 を A 承認 |
| **S3** ✅ 完了 (2026-04-27) | §12 Contact Form / §13 Subscription Card / §14 Case Study / §15 自由入力 | Worksheet 同期 + Spec 改訂 2 件（contact-form v0.3 / subscription-plan-card v0.3）+ current.md v0.2 タグアップ + CHANGELOG。合成決定: §12.1.a A / §12.1.b B（任意→必須）/ §12.1.c A / §13.1.a C（両方不採用）/ §14.1.a A / §15 A（スキップ） |

## 決定フォーマット（毎項目共通）

```
§X.Y 〔項目名〕
現状/既定: ...
選択肢: A=... / B=... / C=...
推奨: ◯（理由 1 行）
```

ユーザー応答: ✅A / ✅B / ✅C / 代替案。多くは 2-5 秒で決まる前提。

## SSoT 反映ルール

1. `tokens.css` を先に更新（影響ある場合のみ）
2. `components/*.md` Spec を更新
3. Worksheet `[ 回答 ]` / `☐` を ✅ に
4. CHANGELOG に「v0.2 §X-§Y 決定」を追記

各セッション末に Claude が `git diff --stat` 相当の要約を提示。

## コミット粒度
- 1 セッション = 1 コミット
- メッセージ例: `feat(ds): worksheet §4-§6 決定をv0.2に反映`
- ユーザー明示の指示があった時のみ commit を実行

## 非ゴール
- Figma 側の Variables / Components 修正反映（S3 完了後に別タスクで一括）
- アイコン SVG の収集・命名・取り込み（§5 でセット決定後の別作業）
- L0 Foundation / Brand DNA v1.0 連動（Phase A 範囲外）
- §15「大前さん／須藤さん向け事前確認」のヒアリング実施（リスト化のみ）

## 順序の根拠
1. §5 Icons → §6 Button より先（Button にアイコンを使う依存）
2. §4 Z-index は tokens.css 既定義のため確認のみ
3. S2 はフォーム系 Primitive 一塊（依存密）
4. S3 は Components 層（S1-S2 の Primitive を組み立てる側）

## 完了条件
- Worksheet §4-§14 全セクションに ✅ または明示的「保留＋理由」
- 該当 components/*.md 全て v0.2 ヘッダで status: stable に
- `current.md` を v0.2 にタグアップ
- CHANGELOG に S1-S3 のエントリ
