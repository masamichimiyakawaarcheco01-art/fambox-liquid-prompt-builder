# FAMBOX Design Flywheel — プロジェクト Hub

> FAMBOX の自律型デザインホイール（Experience Flywheel）構築プロジェクト。
> 長期目標：非デザイナーチームが自律的に「FAMBOX らしい」アウトプットを作り続けられる仕組み。最終的にマルチブランド展開。

---

## このディレクトリの読み方

| ファイル | 内容 | いつ読む |
|---|---|---|
| **README.md**（このファイル）| プロジェクト全体像 | 最初の1回 + 迷った時 |
| **ARCHITECTURE.md** | 4層アーキテクチャの正典 | 設計判断時 |
| **DECISIONS.md** | 「なぜそう決めたか」の意思決定ログ | 過去判断を振り返る時 |
| **PROGRESS.md** | フェーズ別進捗（チェックボックス） | 状況確認 |
| **OPEN_QUESTIONS.md** | 未決定事項リスト | 次の議論ポイント確認 |
| **phases/phase-N-*.md** | 各フェーズの詳細計画 | フェーズ着手時 |
| **sessions/YYYY-MM-DD-*.md** | ブレスト・議論の議事録 | 過去の文脈復元時 |

---

## プロジェクト概要

### 解こうとしている問題

マレルチーム（松浦・三宅・深澤）など、非デザイナーが「FAMBOX らしい」UI・広告・画像を作ろうとすると、以下のいずれかになる：

1. **宮川さん（ブランド責任者）に依頼** → ボトルネック
2. **自己流で Canva 等で作成** → ブランド逸脱
3. **外注** → コスト・リードタイム

**いずれも解決策にならない。**

### 目指す状態（Vision）

> 非デザイナーが、ブランド逸脱せずに、自律的にアウトプットを作り続けられ、
> その結果が次のアウトプットに学習として還元され続ける仕組み。

これを **Experience Flywheel**（Sense → Generate → Reach → Learn のサイクル）として構築する。

### スコープ

#### 含むもの
- FAMBOX 自律型デザインホイールの構築
- マレルチーム（非デザイナー）が使えるレベルへの仕上げ
- Shopify Liquid セクション UI の生成（短期最優先）
- 長期：Shopify 非依存の汎用 Web UI 生成
- 長期：マルチブランド展開アーキテクチャ

#### 含まないもの
- 1回限りのアウトプット制作（既存ワークフローで対応）
- 完全自動化（最初は人間 + AI ハイブリッド）
- マルチブランド展開の即時実装（FAMBOX 完成後）

---

## 4層アーキテクチャ概要

詳細は [ARCHITECTURE.md](./ARCHITECTURE.md) 参照。

```
┌─ Brand Layer（ブランド設定 — 入れ替え可能）──────────────┐
│   FAMBOX  |  Brand B  |  Brand C  ...                  │
│   • Brand DNA  • DS v0.x  • Templates                  │
└────────────────────────────────────────────────────────┘
            ↓
┌─ Engine Layer（ブランド非依存 — 共通コア）───────────────┐
│   Sense → Generate → Reach → Learn ──┐                 │
│      ↑                                │                 │
│      └────────────────────────────────┘                 │
└────────────────────────────────────────────────────────┘
            ↓
┌─ Data Layer（長期記憶 — Second Brain）───────────────────┐
│   Performance History | Asset Library | Brand Memory   │
└────────────────────────────────────────────────────────┘
```

### 4つの輪（Wheel）の現状

| 層 | 既存資産 | 状態 |
|---|---|---|
| **Sense** | Design Insight Engine（月曜08:03自動）、GA4自動レポート、Shopify Analytics | 🟢 部分稼働 |
| **Generate** | LPB v4.1 + FAMBOX DS v0.5 + bugs.md 28規律 + Brand DNA v0.3 | 🟢 高完成度（個人運用のみ） |
| **Reach** | Shopify / Seal メール / SNS（手動） | 🟡 手動運用 |
| **Learn** | brain/40_Bookmarks / sessions index | 🟡 取込のみ、学習未統合 |

**現状の課題：4つの輪はあるが、繋がっていない。**

---

## ロードマップ概要

詳細は [PROGRESS.md](./PROGRESS.md) と [phases/](./phases/) 参照。

| フェーズ | 内容 | 完了目標 |
|---|---|---|
| **Phase 0** | 永続化基盤構築（このディレクトリ） | 2026-05-22 |
| **Phase 1** | Generate 層詳細設計 + マレルチーム向けプロトタイプ | 2026-06 |
| **Phase 2** | Sense 層強化（Insight Engine → 自動指示化） | 2026-07 |
| **Phase 3** | Reach 層自動化（配信パイプライン） | 2026-08 |
| **Phase 4** | Learn 層構築（フィードバックループ閉じる） | 2026-09 |
| **Phase 5** | マルチブランド化（FAMBOX 1.0 後） | 2026-Q4 〜 |

---

## 関連プロジェクト

このプロジェクトは既存の以下と連動する：

- [project_okr_fambox.md](../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_okr_fambox.md) — OKR管理（KR連動）
- [project_fam_lemon_env.md](../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_fam_lemon_env.md) — FAMレモン君（Design Insight Engine）
- [project_brand_output_expansion.md](../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_brand_output_expansion.md) — ブランド多出力アーキテクチャ（ストリーム A〜E）
- [project_fambox_ds_v05_tokens_studio_2026-05-18.md](../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_fambox_ds_v05_tokens_studio_2026-05-18.md) — DS v0.5
- [project_fam_brand_dna.md](../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_fam_brand_dna.md) — Brand DNA v0.3
- [project_analytics_reporter.md](../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_analytics_reporter.md) — 自動レポートシステム（Sense層の一部）

---

## セッション再開のお作法（Claude 向け）

新セッションでこのプロジェクトを継続する時の手順：

1. `~/.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_fambox_flywheel.md` を読む
2. `docs/okr/fambox-flywheel/PROGRESS.md` を読む（現在のフェーズ確認）
3. `docs/okr/fambox-flywheel/OPEN_QUESTIONS.md` を読む（未決事項確認）
4. `docs/okr/fambox-flywheel/sessions/` の直近セッションを読む（前回の文脈）
5. ユーザーに「○○まで決まっていて、次は△△を決める段階です」と報告

---

## ユーザー向け運用フロー

### 確認したい時
- `docs/okr/fambox-flywheel/README.md`（このファイル）を読む
- または `PROGRESS.md` で進捗を見る

### 議論を再開したい時
- 「Flywheel の続き」「FAMBOX デザインホイールの続き」と Claude に言うだけ
- Claude が文脈を復元して提案します

### 更新する時
- 基本は Claude が DECISIONS.md / PROGRESS.md を更新します
- 自分で書き加えるのも自由

---

## 開始日

2026-05-22（キックオフブレスト）
