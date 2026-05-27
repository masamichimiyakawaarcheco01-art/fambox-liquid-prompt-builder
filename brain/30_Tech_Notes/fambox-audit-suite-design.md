---
title: FAMBOX 全体カバー監査スイート — 設計ドキュメント
date: 2026-05-21
tags: [audit, feedback-layer, harness-layer-5, fambox, ci, lint, lighthouse, llmo]
status: active
priority: high
related:
  - harness-engineering-2026-03.md
  - lpb-human-on-the-loop-roadmap.md
  - design-acceptance-parameters.md
  - fambox-verbal-llmo-extension.md
---

# FAMBOX 全体カバー監査スイート — 設計ドキュメント

## 位置づけ

[ハーネスエンジニアリング Layer 5（フィードバック層）](harness-engineering-2026-03.md) の **本命構築**。LPB の概念（Lighthouse / LLMO Check / Decision Trace）を **FAMBOX 本体 136 セクション + 全ページ** に拡大する。

→ ハーネス完成度: **フィードバック 45% → 80%** への到達ルート。

## 目的

| 目的 | 効果 |
|---|---|
| 全 Liquid セクションの規律遵守を機械検証 | image_url width / z-index 直接指定 / inline style / richtext+p ネスト の **再発防止** |
| 全ページの LLMO スコアを定点測定 | AI 経由の認知獲得を **数値で追跡** |
| 全ページの Lighthouse を定点測定 | パフォーマンス・アクセシビリティ・SEO の **回帰検出** |
| デザイントークン整合性チェック | 仮置きトークン名 / 未定義変数 / 重複定義の **検出** |
| 軸該当性チェック | Brand DNA 軸1-3 + 軸4候補 への適合 **Decision Trace 拡張** |

## 監査項目一覧

### 1. Liquid Static Lint（Phase 1 着手対象）

| 項目 | 検出ルール | 重要度 | 実装 |
|---|---|---|---|
| `image_url width` | 1200未満 / width 指定なし | High | `liquid-section-lint.sh` |
| 直接 z-index | `::before` / `::after` ではない CSS 内の `z-index:` | High | `liquid-section-lint.sh` |
| inline style 過多 | `<tag style="...">` が 5箇所以上 / 単一ファイル | Medium | `liquid-section-lint.sh` |
| richtext + `<p>` ネスト | `{{ block.settings.x }}` を `<p>` で囲み | High | `liquid-section-lint.sh` |
| 未閉じタグ | `liquid-check.sh` 既存（フック稼働中） | High | フック側で OK |
| Schema JSON 不正 | 同上 | High | フック側で OK |

→ T-2 で実装する `liquid-section-lint.sh` で **richtext+p ネスト以外の3項目** を最小実装。残りは Phase 2 拡張。

### 2. Lighthouse 全ページ監査（Phase 2）

| 項目 | 閾値 | 対象ページ |
|---|---|---|
| Performance | ≥ 80 | TOP / カート / 商品 / ブログ各3記事 / 食事診断 |
| Accessibility | ≥ 90 | 同上 |
| SEO | ≥ 90 | 同上 |
| Best Practices | ≥ 90 | 同上 |

実装案: LPB Lighthouse ルートを CLI 化し、URL リストを引数で受ける。

### 3. LLMO Check 全ページ監査（Phase 2）

LPB v4 の `POST /api/llmo-check/audit` を **既存ブログ + 重要ページ** に対して定期実行。

| 対象 | 監査頻度 |
|---|---|
| ブログ記事（既存3記事） | 月次 |
| TOP / 商品ページ | 月次 |
| 食事診断結果ページ | 月次 |
| 守屋選手企画ページ（公開後） | 公開時 + 月次 |

→ スコア < 75 で警告、< 60 で要改善。

### 4. デザイントークン整合性（Phase 3）

| 項目 | 検出ルール |
|---|---|
| 未定義 CSS 変数 | `var(--...)` の参照先が `fambox-tokens.css.liquid` に存在しない |
| 仮置きトークン名 | spec 上の名前と実装上の名前の乖離（過去 Phase A で発生実績） |
| 重複定義 | 同名 CSS 変数の重複 |
| 軸違反カラー | Brand DNA 軸から外れる色値の直接記述 |

実装案: `tools/audit/token-integrity.sh` — `snippets/fambox-tokens.css.liquid` を真ソースとして全 Liquid を grep 検証。

### 5. 軸該当性チェック（Phase 4）

Brand DNA 軸1-3 + 軸4 候補 への適合を Claude API + Decision Trace で評価。

| 入力 | 評価軸 |
|---|---|
| セクション or ページのスクショ | 視覚的に軸1-4 のどれに合致するか |
| セクションの Verbal Identity 準拠度 | NG語 / Verb Bank / 結論先行 |
| デザイントークン使用状況 | カラー / フォント / スペーシング |

→ LPB Decision Trace の拡張版として実装。

## Phase 計画

| Phase | 期間 | 着手 | 成果 |
|---|---|---|---|
| **Phase 1** | 2026-05-21 | T-2 `liquid-section-lint.sh` | image_url / z-index / inline style の3チェック / 初回スキャン report |
| **Phase 2** | 6月 | Lighthouse + LLMO Check の全ページ展開 | 月次 report 自動化 |
| **Phase 3** | 7月 | デザイントークン整合性 | `token-integrity.sh` 実装 + CI 連携検証 |
| **Phase 4** | 8月 | 軸該当性チェック | Decision Trace 拡張 |
| **Phase 5** | 9月 | GitHub Actions / pre-commit 統合（L4 達成） | 違反で merge ブロック化 |

## ディレクトリ構成

```
tools/audit/
├── liquid-section-lint.sh      ← Phase 1 (T-2 で作成)
├── lighthouse-scan.sh          ← Phase 2
├── llmo-scan.sh                ← Phase 2
├── token-integrity.sh          ← Phase 3
├── axis-alignment.sh           ← Phase 4
├── run-all.sh                  ← 全監査をまとめて実行
└── reports/
    ├── 2026-05-21-initial-scan.md
    ├── 2026-06-MM-monthly.md
    └── ...
```

## ハーネス層との対応

| 監査 | ハーネス層 | 検出時アクション |
|---|---|---|
| Liquid Static Lint | Layer 5 | 編集者に警告 → Decision Trace に記録 |
| Lighthouse | Layer 5 | パフォーマンス報告 → 月次レビューでアクション |
| LLMO Check | Layer 5 | コンテンツ責任者に提案 |
| トークン整合性 | Layer 5 | 自動修正 PR（Phase 5 以降） |
| 軸該当性 | Layer 4 + 5 の橋渡し | Brand Intelligence メモリ更新 |

## エスカレーションラダー連動

各監査スクリプトは [harness-engineering Escalation Status](harness-engineering-2026-03.md) の **L3 達成判定** のトリガーとなる:

- Phase 1 完了 → `liquid-coding.md` を **L2 → L3** へ昇格
- Phase 3 完了 → `design-acceptance-parameters.md` を **L2 → L3** へ昇格
- Phase 5 完了 → Verbal Identity v1.0 / LLMO Extension を **L3 → L4** へ昇格（CI merge ブロック）

## 成功条件（フィードバック層 80% 到達）

| 指標 | 現状 | 目標 |
|---|---|---|
| 自動化された監査スクリプト数 | 2（LPB LLMO Check / Lighthouse） | **5以上**（Phase 1-4 完了） |
| 監査対象カバレッジ | LPB 経由のみ | **FAMBOX 136 セクション + 全公開ページ** |
| 月次定期実行 | 未 | **GitHub Actions schedule で稼働** |
| CI merge ブロック | 未 | **L4 達成項目で稼働** |

## リスク・アンチパターン

1. **監査が多すぎて応答遅延**: Phase ごとに段階導入（一気に5本動かさない）
2. **誤検出による信頼喪失**: 各監査は **whitelist / allow comment** をサポートする設計
3. **保守困難化**: 各スクリプトは 200 行以下 / 単一責務 / 入出力は markdown/JSON 標準化
4. **本番 Shopify からデータ取れない**: 全監査はローカル Liquid + curl で完結する設計

## 関連
- [[harness-engineering-2026-03.md]] — ハーネス Layer 5 の母艦
- [[lpb-human-on-the-loop-roadmap.md]] — LPB 側の同思想実装
- [[lpb-decision-trace-design.md]] — メモリ層との接続
- [[design-acceptance-parameters.md]] — 評価基準
- [[fambox-verbal-llmo-extension.md]] — LLMO 8項目
