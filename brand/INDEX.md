---
title: FAM / FAM BOX Brand Repository Index
type: index
last_updated: 2026-05-22
purpose: Claude最優先読み込みファイル。構造・現在地・依存関係・意思決定履歴を一括把握。
---

# FAM / FAMBOX Brand Repository — Claude Index

新セッションでは **このファイルを最初に読む**。全体像・現在地・依存関係を把握できる。

---

## 1. Quick Links（最新版への直行リンク）

| Deliverable | Path | Version | Status |
|---|---|---|---|
| FAM Brand DNA | [fam/brand-dna/current.md](fam/brand-dna/current.md) | v0.5 | ✅ Decode完了 |
| FAM BOX Brand DNA | [fambox/brand-dna/current.md](fambox/brand-dna/current.md) | **v0.7+ADR-011〜026** | ✅ **30/36 項目確定（83%）= v1.0 相当の構造定着**（2026-05-22 / 6/30 期限を 5 週前倒し）/ 公式 v1.0 昇格は宮川さん最終承認待ち |
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
| **★ Audit-first Protocol** | [fambox/design-system/operations/audit-first-protocol.md](fambox/design-system/operations/audit-first-protocol.md) | v0.2 | 新規追加前の既存資産棚卸し必須プロトコル（Marc-Antoine Archeco kit v7.0 知見統合） |
| **★ Promotion Rule** | [fambox/design-system/operations/promotion-rule.md](fambox/design-system/operations/promotion-rule.md) | v0.2 | ad-hoc 指摘 → 正式ルール昇格の判定基準（3 回反復トリガー） |
| **★ bugs.md（罠・strict rule 候補・運用ルール 28 エントリ）** | [fambox/design-system/bugs.md](fambox/design-system/bugs.md) | v0.2 | 13 feedback memory 統合 + セッション内事故事例 — BUG 13 / DOCTRINE 5 / PROC 10 + PROC-005-A。LPB v4.1 と fambox-new-section script の規律源 |
| **★ fambox-new-section script** | [scripts/fambox-new-section](../scripts/fambox-new-section) | v0.1 | audit-first 強制 + Token 実在検証 + WF ゲート内蔵の新規セクション生成 CLI |
| **★ MCP Adoption Plan** | [docs/mcp/adoption-plan.md](../docs/mcp/adoption-plan.md) | v0.3 | 採用 4 / 不採用 5。Iconify ✓ Lottie ✓ Connected / Simple Icons CDN 直接 / ローカル画像 MCP 自作予定 |
| **★ Liquid Prompt Builder v4.1** | [index.html](../index.html) | v4.1 | bugs.md 規律自動注入版。STANDARD FOOTER に DOCTRINE/BUG/PROC + MCP アセット参照ルール内蔵 |
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
| 2026-05-22 | KR1-1 | **DNA v0.7（5論点確定）** | ✅ **100%**（ADR-011〜015 / 5/15 期限 7 日遅延も到達）|
| ~~2026-06-06~~ | ~~KR1-1~~ | ~~DNA v0.8（第三者テスト5名初回）~~ | ❌ **スキップ（2026-05-22 宮川さん判断）** |
| **2026-06-30** | **KR1-1** | **DNA v1.0 確定** | ✅ **v0.7+ADR-011〜026 で v1.0 相当到達**（2026-05-22 / 5 週前倒し）/ 公式 v1.0 昇格は宮川さん最終承認待ち |
| 2026-07-31 | KR1-2 | DS v0.5（DNA→原則→Tokens） | — |
| 2026-08-21 | KR1-2 | DS v0.8（Patterns/Components） | — |
| 2026-08-31 | KR1-2 | 主要セクション適用率50% | — |
| **2026-09-30** | **KR1-2** | **DS v1.0 + 適用率100%** | — |

---

## 3. 意思決定ログ（ADR・新着順）

v0.7 までの主要意思決定。詳細は `fambox/brand-dna/decisions/` 配下。

| ADR | 決定内容 | 日付 | 状態 |
|---|---|---|---|
| **ADR-026** | **L5-1〜6 体験レイヤー全項目確定 — L5-5 問合せ返信は「営業日翌日中（現状）+ 将来 24h」/ POP #2 整備領域と連動** | **2026-05-22** | ✅ |
| **ADR-025** | **L4-15 写真の主題最終承認 — 実在トップアスリート起用 + FAMスポーツ栄養アドバイザー登場 + Lab×Editorial撮影トーン** | **2026-05-22** | ✅ |
| **ADR-024** | **L4-14 ロックアップ詳細 10項目確定 — クリアスペース0.5倍 / 最小24px×80px / 3色 / 配置左上主右下副 / 5納品形式** | **2026-05-22** | ✅ |
| **ADR-023** | **L4-1〜6 視覚言語6軸 FAM BOX優先順位確定 — 1位Scientific→2位Continuity→3位Co-driven→...** | **2026-05-22** | ✅ |
| **ADR-022** | **L3-7 ユーモア比率（真面目70/ユーモア10/親しみ20）+ L3-8 一人称・二人称確定** | **2026-05-22** | ✅ |
| **ADR-021** | **L3-2 Tone of Voice + L3-3 推奨語彙最終確定（Tone 2項目追加 / 「FAM スポーツ栄養アドバイザー」推奨 / 「効率」「ボディメイク」を避ける語彙へ）** | **2026-05-22** | ✅ |
| **ADR-020** | **L2-7 POP 最終確定 — 配送品質×開封体験×アフターケア を整備優先領域として明示（5項目）** | **2026-05-22** | ✅ |
| **ADR-019** | **L2-4 機能便益（8項目 / 「FAMスポーツ栄養アドバイザー」改称）+ L2-5 情緒便益 + 水分補給戦略をスコープ外に確定** | **2026-05-22** | ✅ |
| **ADR-018** | **L2-3 JTBD を Top 5 に絞り込み（a 層対応・POD Tier 1/2 と直結）** | **2026-05-22** | ✅ |
| **ADR-017** | **L2-6 POD 最終確定 — 3 階層構造（Tier 1 コア / Tier 2 強化 / Tier 3 文化）+ 競合比較表 + サプリメント提供範囲外を確定** | **2026-05-22** | ✅ |
| **ADR-015** | **L4-14 ロゴ運用 — FAM = 母体組織 / FAM BOX = 独立ブランド・事業（表記使い分けルール新設）** | **2026-05-22** | ✅ |
| **ADR-014** | **L3-1 ブランドキャラクターを 1 人格固定（大前さん型・温度調整なし）に確定** | **2026-05-22** | ✅ |
| **ADR-013** | **L2-2 ターゲット第一優先を「法人プロ起点（Buyer+EB+End User）」に確定** | **2026-05-22** | ✅ |
| **ADR-012** | **L2-1 サブセグメントを 3 層階層に再定義（a 法人プロ / b 部活クラブ / c 保護者栄養士）** | **2026-05-22** | ✅ |
| **ADR-011** | **L1-6 Messaging Pillar 2 案確定 — 「栄養で、可能性の確度を上げる」+「支えるではなく、共に創る」** | **2026-05-22** | ✅ |
| ADR-010 | ブランドリポジトリ構造を4層（README/INDEX/current/drafts+archive）に再構築 | 2026-04-20 | ✅ |
| ADR-009 | 色・タイポ・UI等をデザインシステム側に移管（DNAから除外） | 2026-04-20 | ✅ |
| ADR-008 | 関係性を「共創者（Equal Partner in Challenge）」として正式命名 | 2026-04-20 | ✅ |
| ADR-007 | ブランドキャラクターを二層構造で定義（Primary=大前さん型）→ **v0.7 で ADR-014 により1人格固定に変更** | 2026-04-20 | ⚠️ 上書き |
| ADR-006 | ターゲット選定基準を「態度（本気度）」に据える | 2026-04-20 | ✅ |
| ADR-005 | 戦う市場を「栄養ソリューション市場」として独自定義 | 2026-04-20 | ✅ |
| ADR-004 | Core Values に Integrity（6番目）追加 — 確率を上げる誠実原則 | 2026-04-20 | ✅ |
| ADR-003 | Anti（反対概念）をブランド核 L1-0 に格上げ | 2026-04-20 | ✅ |
| ADR-002 | Brand Concept「Your Step. Our Drive.」をFAM×FAM BOX 同一コンセプト運用 | 2026-04-20 | ✅ |
| ADR-001 | Vision「すべてのアスリートに、スポーツ栄養アドバイザーを」をFAMから継承 | 2026-04-20 | ✅ |

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

## 6. 現在の残論点（v0.7 → v1.0 で決める）

**v0.6.3 で残っていた 5 論点はすべて v0.7（2026-05-22）で確定済**（ADR-011〜015 参照）。

**v0.7+ADR-011〜026 で 30/36 項目確定 → DNA v1.0 相当の構造定着（2026-05-22）**

残 6 項目はすべて漸進的整理 or v1.0 公式昇格後の後続フェーズ:

| # | 論点 | 関連要素 | 区分 |
|---|---|---|---|
| 1 | 視覚軸 v2 軸3 候補（努力の結晶）昇格判定 | 視覚軸 | 🔶 refs 蓄積で確定 |
| 2 | 視覚軸 v2 軸4 候補（蓄積する負荷）昇格判定 | 視覚軸 | 🔶 refs 蓄積で確定 |
| 3 | Animation Library v0.1 と FAM 継承 6 軸の整合性検証 | 視覚軸 | 🔶 実装で確定 |
| 4 | L5-7 KEEP/REFINE/CREATE/IGNORE 4 象限実施 | 体験 | ⏳ v1.0 公式昇格後 |
| 5 | L5-8 第三者ブランド認知テスト設計 | 体験 | ⏳ スキップ判断（2026-05-22）|
| 6 | L5-9 ブランド運用ガイド作成 | 体験 | ⏳ v1.0 公式昇格後 |

### v0.7 → v1.0 公式昇格の判断条件

宮川さん最終承認 → `brand/fambox/brand-dna/v1.0.md` を正式版として作成 + current.md エイリアス更新 + decisions-log.md に正式版昇格 ADR 追加

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
