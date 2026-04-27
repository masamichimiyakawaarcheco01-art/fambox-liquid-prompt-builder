# FAM / FAMBOX ブランド資産リポジトリ

FAMマスターブランドとFAMBOX（B2Bチャネル）のブランドDNA・デザインシステム・意思決定記録の一元管理リポジトリ。

## 現在地（Quick Access）

| 種類 | 最新版 | Status |
|---|---|---|
| **FAM Brand DNA** | [fam/brand-dna/current.md](fam/brand-dna/current.md) | v0.5（Decodeフェーズ完了）|
| **FAMBOX Brand DNA** | [fambox/brand-dna/current.md](fambox/brand-dna/current.md) | v0.6.3（言語化中）|
| **FAMBOX Design System** | [fambox/design-system/current.md](fambox/design-system/current.md) | v0.1（構築プラン）|
| **デイリー実行バックログ** | [fambox/DAILY_BACKLOG.md](fambox/DAILY_BACKLOG.md) | 毎朝確認 |
| **Claude用インデックス** | [INDEX.md](INDEX.md) | 構造化メタデータ |
| **変更履歴（全体）** | [CHANGELOG.md](CHANGELOG.md) | 昇格・確定イベント |

## フォルダ構造

```
brand/
├── README.md            ← このファイル（人間向け）
├── INDEX.md             ← Claude用構造化インデックス
├── CHANGELOG.md         ← 全体変更履歴
│
├── fam/                 ★ マスターブランド
│   └── brand-dna/
│       ├── current.md       ← 常に最新版への複製
│       ├── v0.5.md          ← 確定版
│       └── archive/         ← 過去版
│
├── fambox/              ★ B2Bチャネル
│   ├── brand-dna/
│   │   ├── current.md       ← v0.6.3の内容
│   │   ├── drafts/          ← 作業中バージョン
│   │   ├── decisions/       ← ADR（意思決定記録）
│   │   └── references/      ← インタビュー・参考記事
│   ├── design-system/
│   │   ├── current.md       ← v0.1の内容
│   │   ├── drafts/
│   │   ├── principles/      ← L0 デザイン原則
│   │   ├── tokens/          ← L1 CSS変数（実装の正）
│   │   ├── components/      ← L2-L4 コンポ仕様
│   │   ├── templates/       ← L5 画面仕様
│   │   ├── guidelines/      ← L6 使い方
│   │   └── operations/      ← L7 運用ルール
│   ├── prototypes/          ← HTML試作
│   ├── DAILY_BACKLOG.md     ← 毎日の実行タスク
│   └── CHANGELOG.md         ← FAMBOX内変更履歴
│
└── shared/              ← FAM+FAMBOX共通（将来用）
```

## 運用ルール（要点）

### 1. Single Source of Truth
- 「最新版どれ？」→ 常に `current.md`
- `drafts/` の最新版を `current.md` にコピーで反映
- 確定時は `v{MAJOR}.{MINOR}.md`（例: `v1.0.md`）にも昇格

### 2. バージョン番号
| 形式 | 意味 | 例 |
|---|---|---|
| `v{M}.{m}.md` | 確定版（draft は `drafts/` へ） | `v1.0.md` |
| `v{M}.{m}.{p}.md` | ドラフト | `v0.6.3.md` |
| `current.md` | 最新版の複製（動的） | — |

### 3. 意思決定はADRで残す
- `fambox/brand-dna/decisions/ADR-{3桁}-{kebab}.md`
- 例: `ADR-004-nutrition-solution-market.md`
- 後から「なぜその選択？」を追える

### 4. 更新サイクル
- DNA: 毎週木曜17時前に見直し → 金曜定例MTGで共有
- DS: 月次レビュー / 四半期メジャー改版

## CLAUDEへの指示

新セッションで作業する場合は、以下の順で読むのを推奨:
1. [INDEX.md](INDEX.md) — 構造・現在地・依存関係を把握
2. [fambox/DAILY_BACKLOG.md](fambox/DAILY_BACKLOG.md) — 今日やるべきタスク
3. `current.md`（作業対象のもの）— 現状の全体像

## 連携メンバー

| 役割 | 担当 |
|---|---|
| 設計主 | 宮川 |
| ブランド整合判断 | 大前さん |
| ビジネス整合 | 須藤さん |
| レビュー | 井上さん／三宅さん／深澤さん |
| コンテンツ | 安原さん／大竹さん |
