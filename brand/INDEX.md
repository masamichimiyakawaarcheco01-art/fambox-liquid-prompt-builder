---
title: FAM/FAMBOX Brand Repository Index
type: index
last_updated: 2026-04-20
purpose: Claude最優先読み込みファイル。構造・現在地・依存関係・意思決定履歴を一括把握。
---

# FAM / FAMBOX Brand Repository — Claude Index

新セッションでは **このファイルを最初に読む**。全体像・現在地・依存関係を把握できる。

---

## 1. Quick Links（最新版への直行リンク）

| Deliverable | Path | Version | Status |
|---|---|---|---|
| FAM Brand DNA | [fam/brand-dna/current.md](fam/brand-dna/current.md) | v0.5 | ✅ Decode完了 |
| FAMBOX Brand DNA | [fambox/brand-dna/current.md](fambox/brand-dna/current.md) | v0.6.3 | 🔶 言語化中 |
| FAMBOX Design System | [fambox/design-system/current.md](fambox/design-system/current.md) | v0.1 | 🔶 構築プラン段階 |
| **DS v0.2 Seed (tokens.css)** | [fambox/design-system/tokens/tokens.css](fambox/design-system/tokens/tokens.css) | v0.2 | 🔶 実装用CSS変数 |
| **DS Input Worksheet** | [fambox/design-system/DS_INPUT_WORKSHEET.md](fambox/design-system/DS_INPUT_WORKSHEET.md) | active | 🔶 4時間集中入力用 |
| DS Tokens Docs | [fambox/design-system/tokens/](fambox/design-system/tokens/) | v0.2 | colors / typography / spacing / motion |
| DS Components（雛形） | [fambox/design-system/components/button.md](fambox/design-system/components/button.md) | v0.2 | Primitive Button（他コンポの型見本）|
| **DS Component Input** | [fambox/design-system/components/input.md](fambox/design-system/components/input.md) | v0.2 | Primitive — 下線型+枠囲み型ハイブリッド |
| **DS Pattern FormField** | [fambox/design-system/components/form-field.md](fambox/design-system/components/form-field.md) | v0.2 | Pattern — Label/Input/Helper/Error |
| **DS Component Contact Form** | [fambox/design-system/components/contact-form.md](fambox/design-system/components/contact-form.md) | v0.2 | 10フィールド・inline確認・カスタム自動返信 |
| **DS Primitive Avatar** | [fambox/design-system/components/avatar.md](fambox/design-system/components/avatar.md) | v0.2 | 5サイズ・円形・Deep Blue fallback |
| **DS Primitive Form Controls** | [fambox/design-system/components/form-controls.md](fambox/design-system/components/form-controls.md) | v0.2 | Checkbox/Radio/Toggle |
| **DS Primitive Progress** | [fambox/design-system/components/progress.md](fambox/design-system/components/progress.md) | v0.2 | 線形+円形+Spinner |
| **DS Component Subscription Plan Card** | [fambox/design-system/components/subscription-plan-card.md](fambox/design-system/components/subscription-plan-card.md) | v0.2 | 10項目・h2/Ink価格・2CTA |
| **DS Component Case Study** | [fambox/design-system/components/case-study.md](fambox/design-system/components/case-study.md) | v0.2 | 3レイアウト併用・全Data Viz活用 |
| **★ STRATEGY** | [fambox/STRATEGY.md](fambox/STRATEGY.md) | active | 入口の支配 × 出口の独占（戦略フレーム）|
| **★ Last-Mile Playbook** | [fambox/design-system/operations/lastmile-playbook.md](fambox/design-system/operations/lastmile-playbook.md) | v0.2 | AI生成→人補正のSOP・4カテゴリ蓄積 |
| Figma Master Setup Guide | [fambox/design-system/operations/figma-master-setup-guide.md](fambox/design-system/operations/figma-master-setup-guide.md) | active | Figma立ち上げ7ステップ手順書 |
| **Figma File (立ち上げ済)** | [FAMBOX Design System](https://www.figma.com/design/QsiBrc2v20BYw76YHI9x3e/FAMBOX-Design-System) | active | Figma Master File（2026-04-20立ち上げ）|
| **Tokens Studio JSON** | [fambox/design-system/tokens/tokens-figma.json](fambox/design-system/tokens/tokens-figma.json) | v0.2 | Figma Variables一括投入用 |
| Daily Backlog | [fambox/DAILY_BACKLOG.md](fambox/DAILY_BACKLOG.md) | active | 毎朝更新 |
| **Materials Checklist** | [fambox/MATERIALS_CHECKLIST.md](fambox/MATERIALS_CHECKLIST.md) | active | 宮川作成が必要な実資産17件 |

---

## 2. OKR マイルストーン（現在位置）

**今日 = 2026-04-20（月）**

| 期限 | KR | Deliverable | 現在進捗 |
|---|---|---|---|
| 2026-04-30 | KR1-1 | DNA構成要素の洗い出し完了 | ✅ 100%（v0.6.3完成） |
| 2026-05-15 | KR1-1 | DNA v0.7（言語化中間） | 🔶 25% |
| 2026-06-06 | KR1-1 | DNA v0.8（第三者テスト5名初回） | — |
| **2026-06-30** | **KR1-1** | **DNA v1.0 確定** | — |
| 2026-07-31 | KR1-2 | DS v0.5（DNA→原則→Tokens） | — |
| 2026-08-21 | KR1-2 | DS v0.8（Patterns/Components） | — |
| 2026-08-31 | KR1-2 | 主要セクション適用率50% | — |
| **2026-09-30** | **KR1-2** | **DS v1.0 + 適用率100%** | — |

---

## 3. 意思決定ログ（ADR・新着順）

v0.6.3 までの主要意思決定。詳細は `fambox/brand-dna/decisions/` 配下。

| ADR | 決定内容 | 日付 | 状態 |
|---|---|---|---|
| ADR-001 | Vision「すべてのアスリートに、スポーツ栄養アドバイザーを」をFAMから継承 | 2026-04-20 | ✅ |
| ADR-002 | Brand Concept「Your Step. Our Drive.」をFAM×FAMBOX同一コンセプト運用 | 2026-04-20 | ✅ |
| ADR-003 | Anti（反対概念）をブランド核 L1-0 に格上げ | 2026-04-20 | ✅ |
| ADR-004 | Core Values に Integrity（6番目）追加 — 確率を上げる誠実原則 | 2026-04-20 | ✅ |
| ADR-005 | 戦う市場を「栄養ソリューション市場」として独自定義 | 2026-04-20 | ✅ |
| ADR-006 | ターゲット選定基準を「態度（本気度）」に据える | 2026-04-20 | ✅ |
| ADR-007 | ブランドキャラクターを二層構造で定義（Primary=大前さん型） | 2026-04-20 | ✅ |
| ADR-008 | 関係性を「共創者（Equal Partner in Challenge）」として正式命名 | 2026-04-20 | ✅ |
| ADR-009 | 色・タイポ・UI等をデザインシステム側に移管（DNAから除外） | 2026-04-20 | ✅ |
| ADR-010 | ブランドリポジトリ構造を4層（README/INDEX/current/drafts+archive）に再構築 | 2026-04-20 | ✅ |

---

## 4. 依存関係グラフ

```
FAM Brand DNA v0.5
  ├── [継承] → FAMBOX Brand DNA
  │            ├── L1 Core: Purpose/Vision/Concept/Values/Society/Messaging
  │            ├── L2 Strategic: 市場/ターゲット/JTBD/POD/POP
  │            ├── L3 Personality: キャラクター/Tone/語彙/関係性
  │            ├── L4 Sensorial: 視覚軸/ロゴ/写真（色タイポ等はDS移管）
  │            ├── L5 Experience: ジャーニー/接点/ガイド
  │            └── L1-0 Anti
  │
  └── [参考] → FAMBOX Design System
               ├── L0 Foundation     ← DNA v1.0翻訳
               ├── L1 Tokens         ← FAM v0.5踏襲28 + FAMBOX 4
               ├── L2-L4 Components  ← FAM 6継承 + FAMBOX 20新設
               ├── L5 Templates      ← B2B 8画面（TOP/定期便/問合せ/購入完了/診断/Blog/商品詳細/カート）
               ├── L6 Documentation
               ├── L7 Operations     ← 命名規則/SSoT/Contribution
               ├── L8 Tools          ← Figma/CSS変数/Liquid Library
               └── L9 Metrics        ← DS適用率等

並行: Brand DNA v1.0 確定（6/30）→ DS Phase A 翻訳表作成（同日起点）
```

---

## 5. 参照記事・インタビュー

| カテゴリ | ファイル | 内容 |
|---|---|---|
| Brand DNA 参考記事 | fambox/brand-dna/references/articles-brand-dna-summary.md | kigyosm/enhanced/141ishii/maelop の4記事要約 |
| Design System 参考記事 | fambox/design-system/drafts/v0.1.md §0 | zenn/Goodpatch/usagimaruma/tsubotax/tego1050/anna_morozova の6記事 |
| インタビュー（大前さん） | fambox/brand-dna/references/interview-oomae-2026-04.md | トップアスリート対応・"共創者"概念・寄り添い懸念 |
| インタビュー（深澤さん） | fambox/brand-dna/references/interview-fukasawa-2026-04.md | 栄養ソリューション市場定義・総合サポートチーム |
| インタビュー（三宅さん） | fambox/brand-dna/references/interview-miyake-2026-04.md | 日本代表組織としての位置づけ |

---

## 6. 現在の残論点（v0.7 で決める）

| # | 論点 | 関連要素 | 決定期限 |
|---|---|---|---|
| 1 | FAMBOXは FAM サブブランド or 独立定期便ブランド？ | L4-14 ロゴ | v0.7（5/15） |
| 2 | 第一ターゲット起点は Buyer / Champion / Influencer のどこ？ | L2-2 | v0.7（5/15） |
| 3 | キャラクターは1人格（大前さん型）or 複数ペルソナ（大前/村野差分）？ | L3-1 | v0.7（5/15） |
| 4 | L2-1 サブセグメント a/b/c のいずれを選ぶ？ | 戦う市場 | v0.7（5/15） |
| 5 | Messaging Pillar を何案に絞るか？ | L1-6 | v0.7（5/15） |

---

## 7. ファイル命名規約

| 種類 | 形式 | 例 |
|---|---|---|
| 確定版 | `v{MAJOR}.{MINOR}.md` | `v1.0.md` |
| ドラフト | `v{MAJOR}.{MINOR}.{PATCH}.md` | `v0.6.3.md` |
| 最新エイリアス | `current.md` | 常に最新版のcp |
| ADR | `ADR-{3桁}-{kebab-case}.md` | `ADR-005-nutrition-solution-market.md` |
| インタビュー | `interview-{name}-{YYYY-MM}.md` | `interview-oomae-2026-04.md` |
| 記事要約 | `articles-{topic}-summary.md` | `articles-brand-dna-summary.md` |

---

## 8. フロントマター標準（全MDファイル）

```yaml
---
title: 文書タイトル
type: brand-dna | design-system | adr | reference | interview | index | changelog | backlog
version: 0.6.3
status: draft | current | archived
supersedes: v0.6.2        # 直前版
superseded_by: null       # 次版が出たら更新
last_updated: 2026-04-20
owner: 宮川
related:
  - path/to/related1.md
  - path/to/related2.md
---
```
