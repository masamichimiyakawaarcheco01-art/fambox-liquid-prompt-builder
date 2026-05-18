---
title: FAMBOX Design System (current alias)
type: design-system
brand: fambox
version: 0.2
status: current
alias_of: fambox/design-system/drafts/v0.1.md
last_updated: 2026-04-27
owner: 宮川
milestone:
  - 2026-04-20: v0.1 構造定義（10層フレームワーク・111要素マップ）
  - 2026-04-27: v0.2 到達（Worksheet §1-§14 全クローズ・L1 Tokens / L2 Primitives 5件 / L3 Patterns 1件 / L4 Components 3件 Spec 確定）
  - 2026-04-27: v0.2 拡張（§16 Card Pattern 確定 / L3 Patterns 1件 → 2件・最頻出 Pattern として L4 Component の継承基盤化）
  - 2026-04-28: v0.2 拡張（§17 Hero Section L4 Component 確定 / L4 Components 3件 → 4件・5/29 TOPページ DNA 反映の主役）
  - 2026-04-28: v0.2 拡張（§18 Header L4 Component 確定 / L4 Components 4件 → 5件・全画面共通 Component / DNA「ハンバーガー不採用 + 横スクロール」体系化）
  - 2026-04-28: v0.2 拡張（§19 Footer L4 Component 確定 / L4 Components 5件 → 6件・全画面共通 Component / Ink 背景固定 + Legal 必須 + CTA なしの誠実設計）
  - 2026-04-28: v0.2 拡張（§20-§21 Bento Tile L3 + Bento Grid L4 確定 / L3 Patterns 2件→3件・L4 Components 6件→7件 / DNA Bento 仕様体系化・5/29 TOPページ主役エリアの Spec 完成）
  - 2026-04-28: v0.2 完成基準到達（§22 Modal L4 + §23 Stat Card L3 確定 / TOPページ実装計画策定 / L7 Naming Convention & Governance v0.2 整備 / L3 Patterns 4件・L4 Components 8件・L7 運用ルール 1件 = v0.2 全要素確定）
  - 2026-05-12: v0.2 拡張（L4 FAQ Component 確定 / L4 Components 8件 → 9件 / preview-faq.html を一次資料に Carousel Variant Spec 化 / Accordion variant は v0.3 拡張枠として保留 / 実装計画書 §7「5/20 期限 L4 FAQ Accordion」をクローズ）
  - 2026-05-12: v0.2 拡張（L4 Profile Component 確定 / L4 Components 9件 → 10件 / preview-profile.html を一次資料に Section Variant Spec 化 / Drive 全面塗りを Profile/Hero 専用表現として位置付け / Card variant は v0.3 拡張枠として保留 / 実装計画書 §7「5/22 期限 L4 Profile Card」をクローズ）
  - 2026-05-12: v0.3 着手（L2 Button Figma state property 拡張完了 / 15 → 60 variants / hover/disabled/loading 3 state を Variable bind 込みで実装 / focus/active と with-icon は v0.4 へ送付 / figma-build-log に Issue 3-4 と再発防止策蓄積）
  - 2026-05-12: v0.2 Figma 整合補完（L3 Card Pattern Figma を Audit-first で発見 — Component Set 57:35 既存。唯一の gap だった shadow を `FAMBOX/shadow/1` で 3 variants 適用 / flat は spec 通り shadow なし維持 / Audit-first protocol が L2/L3 両方で重複生成を回避することを実証）
  - 2026-05-12: 全 Component Set 一括 Audit (#4) — Figma 上 15 Component Sets を発見。L2 全 6 + L3 全 3 + L4 全 6 のマッピング表完成 / spec md 8 件に Figma 参照を追加 / Button 所在ページ誤認を訂正（`0. Cover` → `3. Primitives`）/ Hero Section の variants gap（spec 12 ↔ Figma 3）を検出、v0.3 課題化 / Figma 未実装の Spec md 5 件（Bento Tile/Bento Grid/FAQ/Profile/Contact Form）を特定
  - 2026-05-12: L3 Bento Tile + L4 Bento Grid Figma 新規生成 (Session #5) — Audit #4 で未実装と判明した TOP 実装 5/29 期限の主役エリアを最優先で生成 / Bento Tile (`87:26`) 4 variants × default size 2×2 / Bento Grid (`91:107`) 3 variants × placeholder grid demo（Editorial 対角線パターン視覚化）/ 残 sizes と instance 置換は v0.3 へ / Figma 未実装 5 件 → 3 件（FAQ / Profile / Contact Form）へ減少
  - 2026-05-12: L4 FAQ Carousel + L4 Profile Section Figma 新規生成 (Session #6) — 直前 Spec 化 2 件を即 Figma 化し spec ↔ Figma 往復サイクルを締結 / FAQ (`93:90`) Carousel 1 variant × 4 cards / Profile (`96:79`) Section 1 variant × Drive 全面塗り + 2 名並列 / individualStrokeWeights で部分ボーダー実装 / Figma 未実装 3 件 → 1 件（Contact Form のみ）に減少
  - 2026-05-12: 🏆 **Marc 流 4 層スタック完全カバー達成** (Session #7) — Contact Form (`98:121`) input variant 1 個 / 代表 7 フィールド + Submit Button instance / **Figma 未実装 Spec md 1 件 → 0 件**、Spec md ↔ Figma Component Set ↔ Build Log の完全な往復サイクル確立 / 7 セッションで蓄積した学び 20 項を figma-component-from-spec SKILL v0.2 整備へ展開予定
  - 2026-05-12: 📚 **`figma-component-from-spec` SKILL v0.2 整備** (Session #8) — 8 セッションで蓄積した 20 項の学び + 7 つの実 Issue を 287 行の SKILL に体系化 / `.claude/skills/figma-component-from-spec/SKILL.md` として git 管理対象化 / Marc 流 7 ステップ workflow + Issue 1-7 + 学び 1-20 + チェックリスト構成 / 次プロジェクト・別 brand での即活用可能なナレッジ資産化完了
  - 2026-05-12: ✅ **Hero Section variants 完備 + SKILL v0.2 実証実験** (Session #9) — 直前整備の SKILL v0.2 を実 Component で愚直に 7 ステップ実行し有効性を検証 / Hero `67:73` に video-split 追加（3 → 4 variants）/ spec の 4 variants gap 解消 / heights property は v0.4 / SKILL 検証結果 A+ / 学び 23-24 追加（既存 Set への variant 追加と x/y 配置規則）
  - 2026-05-12: 🎨 **Bento Tile 20 variants 完備** (Session #10) — SKILL v0.2 実証 2 回目（L3 2D property 拡張）/ Bento Tile `87:26` に size property 拡張で残 4 sizes（1×1/2×1/1×2/3×2）を 16 variants 追加 / 4 variant × 5 size = **20 variants 完備**、4 列 × 5 行 grid 配置 / 1×1 でコンテンツ切れ検出 → v0.4 で size 別最適化を spec 化 / SKILL 検証 A+ / 学び 25-26 追加（variantOptions 追加順 / 2D property の grid 配置）/ Bento Grid placeholder 置換は Phase 3 で実施
  - 2026-05-12: 🔗 **Bento Grid editorial × Tile 双方向参照確立** (Session #11, Phase 3) — placeholder 9 個 → Bento Tile instance 9 個に置換完了 / 主役 = Glass / 非主役 = Standard で variant 自動選択 / Tile 単体修正が Grid editorial demo に自動反映 / Issue 8-10 検出（主役 Drive 枠消失 / size 別 content 密度 / Glass 3×2 下寄せ）→ v0.4 課題化 / SKILL v0.2 実証 3 回目 A / 学び 27-29 追加（instance + resize で双方向参照 / placeholder 固有属性は転写されない / resize と auto-layout の関係）
  - 2026-05-12: 📚 **`figma-component-from-spec` SKILL v0.3 整備** (Session #12) — 3 回の実証 (#9-11) で発見した改善候補 5 件 + 学び 21-29 + Issue 8-10 を SKILL に還元 / Step 3 を Phase 1/2/3 戦略に大幅拡張 / Step 4 に撮影単位選択ガイド + Phase 3 専用検証 / Issue を 7 → 10、学び を 20 → 29、checklist を 8 項 → 18 項 (Phase 別) に拡張 / 学び 30-31 追加 (実証→改善→再実証サイクル / Phase 戦略は Marc 流の本質)
  - 2026-05-12: 🛡 **Bento Tile featured property 追加 + Issue 8 解消** (Session #13) — SKILL v0.3 Phase 2 の boolean 的 property 拡張実証 / Bento Tile `87:26` に featured property 追加 (20 → 40 variants) / featured=true で全 variants に Drive 2px stroke 適用、主役識別を Tile 側 property として保持可能に / Bento Grid editorial の主役 instances 差し替えは v0.4 / 学び 32-33 追加 (boolean 的 variant は 'true'/'false' 文字列 / individual stroke weights リセット)
  - 2026-05-12: 🎉 **Bento エコシステム完成 + Issue 8 完全解消** (Session #14) — editorial 主役 2 個を `swapComponent` で featured=true 版に切替 / standard 5 placeholder + autofit 8 placeholder を Tile instance に置換 / 全 3 variants × 22 tiles が双方向参照に / Issue 11 検出 (Tile に 3x1 size がない) → v0.4 課題化 / SKILL v0.3 実証 2 回目 A+ / 学び 34-35 追加 (swapComponent は Phase 3 第 2 パターン / 寸法 → size 自動推定)
  - 2026-05-12: 📚 **`figma-component-from-spec` SKILL v0.4 整備** (Session #15) — Session #13-14 の新パターン (boolean variant / swapComponent / 寸法→size 自動推定) + Issue 11 を SKILL に還元 / Phase 3 を「Pattern A: placeholder→instance」「Pattern B: instance→instance swap」の 2 パターンに明文化 / Issue を 10 → 11、学び を 29 → 35、チェックリストを Pattern 別に再構成 / 学び 36-37 追加 (新ユースケースは実証してから明示 / Phase 3 事前 audit を v0.5 で)
  - 2026-05-12: 🚀 **Hero Section 12 variants 完備** (Session #16) — SKILL v0.4 Phase 2 1D 拡張実証 / Hero `67:73` に height property 追加 (4 → 12 variants) / spec の hero--full/tall/compact を Figma 完全再現 (1440×700/550/400) / 4 列 × 3 行 matrix 配置 / minimal-text 既存 500h を 700h 統一 / Issue 12 検出 (compact で内部見切れ) → v0.5 課題化 / SKILL 検証 A+ / 学び 38-39 追加 (1D でも 2D matrix 配置 / 既存サイズ統一を Phase 2 前に)
  - 2026-05-12: 📚 **`figma-component-from-spec` SKILL v0.5 整備** (Session #17) — Phase 2/3 事前 audit を正式手順化 / Phase 2 事前 audit: 既存サイズ差異検出 + auto-layout 変動耐性確認 (Issue 12 回避) / Phase 3 事前 audit: placeholder × source size cross-check (Issue 11 回避) / Issue を 11→12、学び を 35→39、チェックリスト 18→20 項に拡張 / 学び 40-41 追加 (事前 audit は Phase 戦略のメタパターン / Issue 検知のチェックポイント増)
  - 2026-05-12: 🔧 **Issue 12 完全解消 + SKILL v0.5 事前 audit 実証** (Session #18) — Hero compact 4 + tall 2 = 6 variants の内部 auto-layout を補修 / video-fullscreen padding 縮小、image-editorial 内部 Rectangle resize、video-split 絶対座標再配置 / 3 つのヘルパー関数 (fixVerticalVariant / fixImageEditorial / fixVideoSplit) で補修パターン化 / SKILL v0.5 事前 audit が実 Issue で機能することを実証 / 学び 42-43 追加 (補修パターンも SKILL に / 事前 audit は実証ループで価値顕在化)
  - 2026-05-12: 📚 **`figma-component-from-spec` SKILL v0.6 整備** (Session #19) — Phase 4 = コンテンツ最適化フェーズを正式追加 / 補修ヘルパー関数 3 種を一般化 (fixVerticalVariant / fixHorizontalVariantRect / fixAbsoluteLayoutVariant) / 「いつ Phase 4 が必要か」判定表 + 典型フロー code sample / ベストプラクティス を 39→43 項に拡張、チェックリストに Phase 4 セクション 5 項追加 / 学び 44 追加 (Phase 戦略は線形でなく条件連動) / Phase 1-4 完成形フローを確定
  - 2026-05-12: 🚀 **TOPページ実装着手 + Brand DNA v0.4 draft** (Session #20) — Phase 1 として FAMBOX Header section (`projects/fambox/sections/fambox-header.liquid` 343 行) を spec v0.2 準拠で雛形化 / Brand DNA v0.4 反映 draft (`operations/2026-05-12-brand-dna-v0.4-draft.md`) で Marc 流 4 層スタック / Phase 戦略 / 三位一体 / 6 軸目「Disciplined」を提案 / 学び 45-46 追加 (worktree 内 Liquid は本番テーマへ移植前提 / non-disruptive reflection pattern)
  - 2026-05-12: 🦸 **TOPページ Week 2: Hero section Liquid 雛形** (Session #21) — `projects/fambox/sections/fambox-hero.liquid` 441 行を新規生成 / 4 variants (video-fullscreen / video-split / image-editorial / minimal-text) × 3 heights (compact/tall/full) を 1 section 統合実装 / NBA HOOP モード boolean property / 4 Corner Icons (video-split) / Variable bind + GA4 連携 + SP responsive + reduced-motion 完備 / 学び 47 追加 (複数 variants 統合 vs 分離の判断軸 = 共通要素率 60%)
  - 2026-05-12: 💰 **TOPページ Week 1 完了: Subscription Plan Card v0.2 Liquid** (Session #22) — `fambox-subscription-plan-v0.2.liquid` 約 450 行を新規生成（既存 v0.1 系 506 行と並行配置、Marc 流「既存破壊しない」）/ Card Pattern 継承 (card-standard / card-featured) / 8 項目構成 / 2 CTA (Primary + Ghost) / バッジ 1 プラン限定 / 価格 32px Ink (煽り Anti 回避) / 最低契約期間・初月特典は disclaimer から FAQ 誘導 / PC 3 列 / Tablet 2 列 / SP 1 列 / 学び 48 追加 (既存 Liquid 破壊しない原則)
  - 2026-05-12: 🍱 **TOPページ Week 2 主役: Bento Grid + Tile Liquid 化** (Session #23) — `fambox-bento.liquid` 563 行を新規生成 / Grid 3 variants (standard / editorial / autofit) + Tile 4 variants × 5 sizes × featured を 1 section に統合 / DNA Anti 予防 (gap < 16 clamp / 12 tile 上限) / Schema preset 2 種 (Editorial 5 tiles + Autofit KPI 4 tiles) / 学び 49-50 追加 (Grid + Tile は Liquid で 1 section 統合が正解 / Schema preset で「最初の配置」を DNA 準拠に)
  - 2026-05-12: 🎬 **TOPページ Week 4 前倒し: FAQ + Profile Liquid 化** (Session #24) — `fambox-faq.liquid` 292 行 + `fambox-profile.liquid` 321 行を新規生成 / FAQ Carousel (黒線 32×2 + Drive answer + SP scroll-snap) / Profile Section (Drive 全面塗り + Title box 部分罫線 + 624×517 box) / **spec → Figma → Liquid の三位一体達成** (FAQ / Profile の 3 媒体すべて同期) / 学び 51-52 追加 (三位一体は L4 Component で完成形 / preview-html の役割縮小)
  - 2026-05-12: ⚡ **TOPページ Week 3: Bento preset で 3 sections 一括解決** (Session #25) — `fambox-bento.liquid` に preset 3 個追加 (Spirit Editorial / Value Proposition / Plan Features) / **新規 3 ファイル不要、+55 行で Week 3 完了** / 学び 50 の実証 (Schema preset = DNA 準拠の初期配置 = 効率の極み) / 既存 fambox-value-proposition (513行) と fambox-plan-features (396行) は v0.3 で deprecate 判断 / 学び 53-54 追加 (3 sections 1 file 解決の極み / 既存 deprecate 判断軸 = preset カバー範囲)
  - 2026-05-12: 🍳 **TOPページ Week 4 残: Hero preset 4 個 + menu-showcase tokens ガイド** (Session #26) — `fambox-hero.liquid` に preset 4 個追加 (Video Fullscreen / Video Split / **Easy Cooking** / Minimal Text) で Easy Cooking (Day 23-24) を即配置可能化 / `operations/2026-05-12-menu-showcase-tokens-migration.md` 作成 (33 placement-rule で本番テーマ tokens 適用ガイド) / 学び 55-56 追加 (Liquid preset 拡充は L4 単一 section の表現力を桁違いに上げる / Tokens 移行は構造変更なしで最大の DNA 準拠化手段)
---

# FAMBOX デザインシステム v0.1 — 構築に必要な要素の洗い出し

**目的**: OKR Task 1-2「DNA→原則→CSS変数の3階層翻訳表＋DS適用率100%（9月末）」の設計基盤。6記事＋FAM v0.5資産の統合から、FAMBOX専用デザインシステムに必要な要素を構造化。
**作成**: 2026-04-20
**Status**: Phase A（Brand DNA v1.0完成後に翻訳表着手）の準備段階

---

## 0. 設計方針

### 参照記事の統合サマリ
| 出典 | 主要概念 | FAMBOX DSへの活かし方 |
|---|---|---|
| zenn/jinjer | 3層（スタイルガイド/コンポ/運用ルール）／6つの壁 | **運用ルールを第1級要素として扱う** |
| Goodpatch（★中核） | **デザイン言語／ツールボックス／組織体制** の3つの柱 | **本DSの最上位フレームに採用** |
| usagimaruma | 思想×道具×人間関係の統合／4実装段階（文書化→理解普及→体制→運用） | 運用段階の設計に利用 |
| tego1050（★実装軸） | **トークン層／Component層／Variant管理／連携層** の4層実装 | **実装レイヤの具体骨格に採用** |
| anna_morozova | 命名規則／プロパティ定義／Iteration的拡張 | 命名規則・段階的拡張のガイドに利用 |

### FAM と FAMBOX の関係
- **FAM（マスター）**: 既に v0.5 で色・タイポ・モーション・UI・データ可視化 F 章（8コア）まで決定済み → **99%継承**
- **FAMBOX（B2Bチャネル）**: FAMトークンを基盤に、B2B特化の接点（法人LP／提案書／問合せ／定期便）向けの **Primitives・Patterns・Templates** を追加

---

## 1. 10層フレームワーク（統合提案）

```
╔═══════════════════════════════════════════════════╗
║  思想レイヤ                                        ║
║  ┌─────────────────────────────────────────────┐  ║
║  │ L0  Foundation（原則・哲学）                │  ║
║  └─────────────────────────────────────────────┘  ║
║  道具レイヤ                                        ║
║  ┌─────────────────────────────────────────────┐  ║
║  │ L1  Design Tokens（基礎変数）               │  ║
║  │ L2  Primitives（原子コンポーネント）         │  ║
║  │ L3  Patterns（分子・小規模複合）             │  ║
║  │ L4  Components（生体：構造・複合）           │  ║
║  │ L5  Templates（画面テンプレート）            │  ║
║  └─────────────────────────────────────────────┘  ║
║  ドキュメント・人間関係レイヤ                       ║
║  ┌─────────────────────────────────────────────┐  ║
║  │ L6  Documentation（使い方／Do&Don't）        │  ║
║  │ L7  Operations（運用ルール・更新フロー）      │  ║
║  │ L8  Tools & Infrastructure                  │  ║
║  │ L9  Metrics（効果測定）                     │  ║
║  └─────────────────────────────────────────────┘  ║
╚═══════════════════════════════════════════════════╝
```

---

# L0 — Foundation（原則・哲学）

Brand DNA v1.0 からの翻訳で成り立つ。**3階層翻訳表の1段目**。

| # | 要素 | 内容 | DNA源泉 |
|---|---|---|---|
| 0-1 | **デザイン原則** | 3-5項目に集約（例: Science first / Continuity / Co-driven ／ Integrity／ Substance over Style） | L1-4 Core Values 6項目から導出 |
| 0-2 | **視覚言語6軸の優先順位** | Scientific 1位 → Continuity 2位 → Co-driven 3位 → Propulsive → Ascending → Pulsing | L4-1〜L4-6 |
| 0-3 | **Anti（視覚的に避けるもの）** | 表面的／派手／映え／エセ高級／キラキラ系／モデル手／スタジオ過剰演出 | L1-0 |
| 0-4 | **アクセシビリティ基準** | WCAG 2.1 AA／タッチターゲット44px／フォーカス2px／prefers-reduced-motion対応 | FAM v0.5 B章 |
| 0-5 | **メタファー運用** | Editorial × Lab の使い分けルール | FAM v0.5 A章 |
| 0-6 | **引き算の美学（Aシックス的本質主義）** | 装飾過多・盛り・インフルエンサー臭の禁止 | v0.6.3 追加 |

**Status**: ⏳ DNA v1.0 確定後（6月末）に着手

---

# L1 — Design Tokens（基礎変数）

FAM v0.5 CSS変数をベースに構造化。**3階層翻訳表の2段目**。

## 1-A. Color Tokens
| # | カテゴリ | 項目数 | v0.5継承 |
|---|---|---|---|
| 1-1 | Primary（Drive） | **4値**（base #FC5214 / hover #E14710 / light #FF7A51 / glow） | ✅ + **hover 追加 Session #48** |
| 1-2 | Secondary（Sky/Deep） | 2値 | ✅ |
| 1-3 | Ink / Text 5段階 | 5値（ink #1B1D1A / sub #5C5F58 / caption #8A8D87 / placeholder #DDD / white #fff）| ✅ + **placeholder 追加 Session #48** |
| 1-4 | Background 3階層 | 3値（primary #fff / secondary #FAFAFA / tertiary #F3F3F3）| ✅ |
| 1-5 | Border（Light/Base/Soft/Subtle） | **4値**（追加: soft #D0D1DB）| ✅ + **soft 追加 Session #48** |
| 1-6 | Semantic（Success/Warning/Error/Info） | 4値（error #D32F2F / success #2E7D32）| ✅ |
| 1-7 | Data Color Palette | 6値 | ✅ |
| 1-8 | Glass Opacity（5階調） | 5値（0.05/0.1/0.3/0.6/0.8）| ✅ |
| 1-9 | **Semantic Alias**（意味参照） | 例: `--color-cta = --color-drive`、`--color-focus-ring = --color-drive`、**`--color-disabled = #B3B5B0`** | **FAMBOX新設** + Session #48 で disabled 追加 |

### v0.5 実装からの逆抽出（Session #47-48 / de facto 確定）

**Drive 表記揺れ解消**: `#FB4C15`（24件）を `#FC5214` に統一（Session #48）。**`#FC5214` を Drive base color の正式値**として確定。

**マジックナンバー統合判断**:
- `#92939c`（4件 / カード sub text）→ **`--color-caption #8A8D87`** に集約推奨（微小差 / 視覚的に区別なし）
- `#545655`（4件 / カード本文）→ **`--color-sub #5C5F58`** に集約推奨（微小差 / 視覚的に区別なし）
- `#d0d1db`（5件 / 区切り線）→ **`--border-soft` として新規追加**（既存 Token と用途が異なる）

## 1-B. Typography Tokens
| # | 項目 | v0.5継承 |
|---|---|---|
| 1-10 | font-family EN（Poppins） | ✅ |
| 1-11 | font-family JA（Hiragino Sans） | ✅ |
| 1-12 | font-size scale（12/14/16/20/24/32/48/64/96/128） | ✅ |
| 1-13 | font-weight（400/500/600/700） | ✅ |
| 1-14 | line-height（heading 1.2 / body 1.75 / caption 1.5） | ✅ |
| 1-15 | letter-spacing（EN -0.02em / JA 0.02em） | ✅ |
| 1-16 | **Text Style Preset**（h1/h2/h3/body/caption等のまとめ） | **FAMBOX新設** |

## 1-C. Spacing Tokens
| # | 項目 | v0.5継承 |
|---|---|---|
| 1-17 | Base unit 8px | ✅ |
| 1-18 | Scale **拡張**（4/8/12/16/24/32/40/48/64/96/120）| ✅ + **0.5/1.5/4.5/8 追加 Session #48**（実装で頻出）|
| 1-19 | Section spacing（SP 96 / PC 120）| ✅ + **160→120 修正 Session #48**（実装は 120 が中心）|
| 1-20 | Component spacing（16/24/32） | ✅ |

### Spacing scale v0.5 命名（実装に揃えて確定）

| Token | px |
|---|---|
| `--space-0.5` | 4 |
| `--space-1` | 8 |
| `--space-1.5` | 12 |
| `--space-2` | 16 |
| `--space-3` | 24 |
| `--space-4` | 32 |
| `--space-4.5` | 40 |
| `--space-5` | 48 |
| `--space-6` | 64 |
| `--space-7` | 96 |
| `--space-8` | 120 |

## 1-D. Motion Tokens
| # | 項目 | v0.5継承 |
|---|---|---|
| 1-21 | duration **更新**（150/250/350ms）| 🔶 + **Session #48 で 150/300/600 → 150/250/350 に修正**（実装と整合）|
| 1-22 | easing（ease-out 中心）| ✅ + **`--ease-out` を default に集約**（実装は ease-out が 80%）|
| 1-23 | 呼吸アニメ（2秒サイクル）| ✅ |
| 1-24 | line-height **拡張**（1.2/1.4/1.5/1.75/1.8）| ✅ + **3 → 5 段階拡張 Session #48** |

### Motion / Typography line-height v0.5 命名

| Token | 値 | 用途 |
|---|---|---|
| `--duration-fast` | 150ms | hover / focus transition |
| `--duration-base` | 250ms | modal open/close / nav slide |
| `--duration-slow` | 350ms | sheet variant slide-up |
| `--lh-tight` | 1.2 | heading H1/H2 |
| `--lh-heading` | 1.4 | heading H3/H4 |
| `--lh-base` | 1.5 | caption / form field |
| `--lh-body` | 1.75 | body 標準 |
| `--lh-relaxed` | 1.8 | quote / 強調本文 |

## 1-E. Elevation / Shadow Tokens
| # | 項目 | v0.5継承 |
|---|---|---|
| 1-24 | shadow-1〜5（5段階） | ✅ |

## 1-F. Radius Tokens
| # | 項目 | v0.5継承 |
|---|---|---|
| 1-25 | radius-sm/md/pill-cta(50px)/pill(9999px) | ✅ |

## 1-G. Breakpoint Tokens
| # | 項目 | v0.5継承 |
|---|---|---|
| 1-26 | SP-sm/SP/Tablet/PC **拡張**（〜480/481-767/768-1023/1024+）| ✅ + **480 (SP-sm) 追加 Session #48**（実装で Header / Modal SP layout に頻出）|

| Token | 範囲 | 用途 |
|---|---|---|
| `--bp-sp-sm` | 480px | Header / Modal の SP small（actions 縦並びへ切替）|
| `--bp-sp-max` | 767px | SP 上限 |
| `--bp-tablet` | 768px | Tablet 下限 |
| `--bp-pc` | 1024px | PC 下限 |
| `--container-max` | 1440px | コンテナ最大幅 |

## 1-H. Z-index Tokens
| # | 項目 | 状態 |
|---|---|---|
| 1-27 | z-index scale（base/raised/sticky/modal/toast） | **FAMBOX新設** |

## 1-I. Icon Tokens
| # | 項目 | 状態 |
|---|---|---|
| 1-28 | アイコンサイズ（16/24/32/48） | ✅ FAM v0.5 |
| 1-29 | 線幅 1.5px | ✅ |
| 1-30 | アイコンセット選定（Lucide/Phosphor/Heroicons/自作） | ❌ 未定 |

## 1-J. Variable Mode（端末別・テーマ別切替）
| # | 項目 | 状態 |
|---|---|---|
| 1-31 | Light/Dark モード（v0.5 darkはsemantic tokenで対応可能） | 🔶 |
| 1-32 | Mobile/Desktop モード | 🔶 |

**Status**: 🔶 v0.5 ほぼ継承、FAMBOX新設4項目（Semantic Alias／Text Style Preset／Z-index／Icon set選定）

---

# L2 — Primitives（原子コンポーネント）

最小単位のUI部品。FAM既存Liquidから抽出＋B2B向け追加。

| # | コンポ | v0.5状態 | FAMBOXで追加検討 |
|---|---|---|---|
| 2-1 | Icon | ✅ | セット確定後 |
| 2-2 | Input（下線型／枠囲み型） | ✅ | テキストエリア追加 |
| 2-3 | Button（Primary Pill / Secondary / Ghost） | ✅ | アイコンボタン、サイズ3段階（sm/md/lg） |
| 2-4 | Label | 🔶 | — |
| 2-5 | Link | 🔶 | 外部リンク・ファイルDLリンク |
| 2-6 | Badge | ✅ | — |
| 2-7 | Tag / Chip | 🔶 | フィルタ用、色付きバリアント |
| 2-8 | Avatar | ❌ | 栄養士・選手プロフィール用 |
| 2-9 | Checkbox / Radio / Toggle | ❌ | フォーム必須 |
| 2-10 | Progress / Spinner | ❌ | 診断進捗・送信中表示 |
| 2-11 | Divider | 🔶 | — |
| 2-12 | Pill型Tab（v0.5タブ踏襲） | ✅ | — |

**Status**: v0.5踏襲6件＋FAMBOX新設6件（Avatar/Form controls/Progress等）

---

# L3 — Patterns（分子・小規模複合）

Primitivesを2-3個組み合わせた単位。

| # | パターン | 用途 | 状態 |
|---|---|---|---|
| 3-1 | FormField | Label+Input+HelperText+ErrorMessage | ❌ 要設計 |
| 3-2 | Card | Image+Title+Body+CTA | ✅ v0.5踏襲 |
| 3-3 | ListItem | Icon+Text+Meta+Action | ❌ |
| 3-4 | Tooltip | 付箋的ヒント | ❌ |
| 3-5 | Alert / Toast | Success/Warning/Error通知 | 🔶 v0.5 motion指定のみ |
| 3-6 | Breadcrumb | 階層ナビ | ❌ |
| 3-7 | Pagination | 一覧ページ送り | ❌ |
| 3-8 | Dropdown / Select | フォーム | ❌ |
| 3-9 | Accordion | FAQ・詳細展開 | 🔶 |
| 3-10 | Stat Card | 数値ハイライト（BigStat） | ✅ F-6参考 |

**Status**: ❌要設計が多い。B2B文脈のフォーム系が最優先

---

# L4 — Components（構造・複合）

複数Patternsで構成する大きな機能ブロック。

| # | コンポ | 用途 | 状態 |
|---|---|---|---|
| 4-1 | Header（固定ヘッダー） | 共通ナビ | ✅ v0.5 |
| 4-2 | Drawer（SP990px未満） | モバイルメニュー | ✅ v0.5 |
| 4-3 | Footer | 共通フッター | 🔶 |
| 4-4 | Modal / Dialog | 確認・詳細 | ✅ v0.5 motion |
| 4-5 | Table | データ表示 | ❌ |
| 4-6 | Filter Panel | 一覧絞り込み | ❌ |
| 4-7 | Hero Section（NBA HOOP型） | ページ冒頭 | 🔶 |
| 4-8 | Bento Tile（5サイズ） | グリッド主役 | ✅ v0.5 |
| 4-9 | **Data Viz 8コア** | NutrientRing/MacroBar/StreakDots/ZoneGauge/RadarCompare/BigStat/PersonaCard/TrendLine | ✅ v0.5 設計済 |
| 4-10 | Contact Form | 問合せフォーム | ❌ Task 2-1の中核 |
| 4-11 | Diagnosis Flow | 食事診断UI | 🔶 Task 2-2と連動 |
| 4-12 | Subscription Plan Card | 定期便プラン | 🔶 |
| 4-13 | Testimonial / Case Study | 実績コンテンツ | 🔶 既存fam-case-study参考 |
| 4-14 | FAQ（Carousel）| 質問カード横スクロール | ✅ v0.2（[faq.md](components/faq.md)）/ Accordion variant は v0.3 |
| 4-15 | Profile（Section）| 監修者・推薦者の Drive 全面塗り紹介 | ✅ v0.2（[profile.md](components/profile.md)）/ Card variant は v0.3 |

**Status**: v0.5継承6件＋FAMBOX新設9件（Table/Filter/Contact/Diagnosis/Subscription/FAQ/Profile 等）

---

# L5 — Templates（画面テンプレート）

OKR Task 2-1「4画面DNA反映」と連動する優先順。

| # | 画面 | 期限 | 主要Components |
|---|---|---|---|
| 5-1 | **TOP** | 5/29 | Header / Hero / Bento Grid / Case Study / Footer |
| 5-2 | **定期便ページ** | 6/12 | Subscription Plan Card / Data Viz / FAQ |
| 5-3 | **問合せフォーム** | 6/22 | Contact Form / FAQ |
| 5-4 | **購入完了** | 6/30 | Success Alert / Next Step CTA |
| 5-5 | 食事診断 | 7月 | Diagnosis Flow |
| 5-6 | Blog 一覧 / 記事 | 8月 | Article Card / TOC |
| 5-7 | 商品詳細 | 8月 | Product Info / Data Viz |
| 5-8 | カート / 確認 | 9月 | Order Summary |

**Status**: ❌ 期限順に設計着手

---

# L6 — Documentation（ドキュメント）

各要素の「使い方」を文書化。

| # | 項目 | 内容 |
|---|---|---|
| 6-1 | **Usage Guideline**（Do/Don't） | 各Primitive/Component/Templateごと |
| 6-2 | Code snippets | Liquid / CSS variables 例 |
| 6-3 | Accessibility notes | WCAG AA対応、キーボード操作、スクリーンリーダー |
| 6-4 | Props / Attributes 仕様書 | バリアント・状態・パラメータ |
| 6-5 | Responsive behavior | SP/Tablet/PCでの振る舞い |
| 6-6 | 8状態仕様 | default/hover/focus/active/disabled/loading/empty/error/success |
| 6-7 | Change log | バージョンごとの変更履歴 |
| 6-8 | Migration guide | v0.x→v1.x等の移行ガイド |

**Status**: ❌ Components確定と並行で記述

---

# L7 — Operations（運用ルール）

★ zenn記事の「6つの壁」の対処。**ここが最も失敗しやすい**。

| # | ルール | 内容 |
|---|---|---|
| 7-1 | **SSoT（Single Source of Truth）** | Figma = 設計の正／Liquid = 実装の正。差分はFigmaをマスタにする |
| 7-2 | **Naming Convention** | 小文字＋ハイフン：`button-primary-pill`／`color-drive-light`／`space-4`／`fambox-header`（anna_morozova記事準拠） |
| 7-3 | Versioning | Semantic Versioning（1.0.0 / 1.1.0 / 2.0.0）。破壊的変更は Major |
| 7-4 | **Update Cycle** | 月次レビュー（使用状況・提案収集）／四半期Major |
| 7-5 | Contribution process | 新コンポ提案 → 審査 → Figma追加 → Liquid実装 → ドキュメント更新 → 告知 |
| 7-6 | 浸透策 | オンボーディング資料／クイックリファレンス1枚／運用ガイド |
| 7-7 | 判断の責務分担 | 宮川（設計主）／井上・三宅・深澤さん（レビュー）／大前さん（ブランド整合判断） |
| 7-8 | Deprecate ルール | 廃止予告→2バージョン並存→削除 |

**Status**: ❌ v1.0の骨格を6月末までに策定

---

# L8 — Tools & Infrastructure

| # | 項目 | 用途 | 状態 |
|---|---|---|---|
| 8-1 | Figma Master File | 設計の正 | ❌ 新規構築 |
| 8-2 | Figma Variables / Tokens | トークン管理 | ❌ |
| 8-3 | CSS Variables File（Liquid snippet） | 実装の正 | ✅ v0.5テンプレートあり |
| 8-4 | Liquid Section Library | 再利用セクション | 🔶 fam-*, fambox-* 既存 |
| 8-5 | **Liquid Preview / Playground** | 実装確認環境 | 🔶 liquid-pipeline連動 |
| 8-6 | Tokens Studio / Supernova（検討） | Figma→Code同期 | ❌ |
| 8-7 | GitHub Repo | コード管理 | ✅ 既存 |
| 8-8 | CI lint / a11y チェック | 品質担保 | ❌ |

**Status**: 🔶 Figma構築が最重要タスク

---

# L9 — Metrics（効果測定）

OKRと連動させて「DSの効果」を可視化。

| # | 指標 | 目標値 | 測定方法 |
|---|---|---|---|
| 9-1 | **DS適用率** | 9月末 **100%**（OKR KR1-2） | 全Liquidファイルに占める変数適用率 |
| 9-2 | Component再利用率 | — | 同一コンポの参照回数 |
| 9-3 | Designer Velocity | 画面設計所要時間の削減 | 前期比較 |
| 9-4 | Developer Velocity | Liquid実装所要時間の削減 | 前期比較 |
| 9-5 | a11y Score | Lighthouse 90以上 | 月次測定 |
| 9-6 | デザインの一貫性 | 第三者ブランド認知テストのFAMBOXらしさ評価 | v0.8/v1.0で測定 |

**Status**: ⏳ v1.0後に定点観測開始

---

## 2. FAM v0.5 からの継承カバレッジ

| 層 | v0.5 継承 | FAMBOX 新設 | 合計 |
|---|---|---|---|
| L0 Foundation | 5 | 1 | 6 |
| L1 Tokens | 28 | 4 | 32 |
| L2 Primitives | 6 | 6 | 12 |
| L3 Patterns | 2 | 8 | 10 |
| L4 Components | 6 | 7 | 13 |
| L5 Templates | 0 | 8 | 8 |
| L6 Docs | 0 | 8 | 8 |
| L7 Operations | 0 | 8 | 8 |
| L8 Tools | 1 | 7 | 8 |
| L9 Metrics | 0 | 6 | 6 |
| **合計** | **48** | **63** | **111** |

---

## 3. 段階的ロードマップ（OKR KR1-2 連動）

| フェーズ | 期限 | 成果物 | 対応レイヤ |
|---|---|---|---|
| **Phase A** | 2026-06-30 | DNA v1.0 → 翻訳表ドラフト（DNA→原則→Token対応表） | L0 + L1 |
| **Phase B** | 2026-07-31 | DS v0.5（Tokens完成＋Primitives定義） | L1 + L2 |
| **Phase C** | 2026-08-21 | DS v0.8（Patterns/Components設計） | L3 + L4 |
| **Phase D** | 2026-08-31 | 主要セクション適用率50% | L5 TOP/定期便反映 |
| **Phase E** | 2026-09-30 | 適用率100% + DS v1.0運用版 + 運用ルール確定 | 全層 |

---

## 4. 最優先でやるべきこと（v0.2→v0.5まで）

### v0.1（今）
- 本ドキュメント作成 ✅

### v0.2（5月上旬・OKR Task 1-1-b と並行）
- **L7 Operations 骨格確定**: 命名規則／SSoT宣言／Versioning／Contribution process
- **L8 Figma構築着手**: マスタファイル枠＋変数ページ

### v0.3（5月末）
- **L1 Tokens 全項目を Figma Variables として入力**
- **CSS変数ファイル v0.1 を Liquid snippet として実装**

### v0.4（6月中旬・Brand DNA v1.0 と並行）
- **L0 Foundation 翻訳表** を DNA v1.0 から導出
- **L2 Primitives 12件の設計着手**

### v0.5（6月末・Task 1-2-a「DS作成」期限）
- **Tokens + Primitives を Liquid に実装**
- TOPページ（5/29期限）に適用テスト

---

## 5. 残論点（先に決めるべき）

1. **Figmaマスターファイルの構造**: 1ファイル集約 or 機能別分割？
2. **アイコンセット選定**: Lucide / Phosphor / Heroicons / 自作（Brand DNA L4-18 と連動）
3. **Tokens Studio 等のFigma→Code同期ツールを入れるか**（工数と ROI の判断）
4. **命名規則の最終形**: BEM / アトミック / 単純ハイフン区切り のいずれを採用するか
5. **FAM と FAMBOX の DS を分離するか統合するか**（単一DS or マルチブランドDS）

---

## 6. Brand DNA との接続（3階層翻訳表の骨格）

```
┌────────────────────┐
│ Brand DNA v1.0     │ ← L1 Brand Core / L2 Strategic / L3 Personality
│ （WHY / WHAT 中心） │
└──────────┬─────────┘
           │ 翻訳①：DNA → Design Principles
           ▼
┌────────────────────┐
│ Design Principles  │ ← L0 Foundation（本DS）
│ （3-5個の原則）     │
└──────────┬─────────┘
           │ 翻訳②：Principles → Token Names
           ▼
┌────────────────────┐
│ Design Tokens      │ ← L1 Tokens（本DS）
│ （CSS変数）         │
└──────────┬─────────┘
           │ 翻訳③：Tokens → Components
           ▼
┌────────────────────┐
│ Implementation     │ ← L2-L5 Primitives〜Templates
│ （Liquid実装）      │
└────────────────────┘
```

---

## 7. 完成度ダッシュボード（spec ↔ Figma ↔ Liquid 三位一体）

> 学び 77（N/3 ラベル化）の実装。各 Component の **3 層存在** を即可視化。
> 凡例: ✅ = 存在、❌ = 未作成、⚪ = 評価対象外（Pattern として L4 に内包 / Primitive は Snippet レベル運用）
> 最終更新: 2026-05-14 / Session #38

### 7-A. L4 Components（10 件 / Section 化対象）

> **表記ルール（v0.3-dashboard 標準化 / Session #43）**: Figma Set 列は `<ID> (<Nv> / <内訳>)` 形式で variant 構成を明示

| Component | spec md | Figma Set | Liquid section | N/3 | Status | 残課題 |
|---|---|---|---|---|---|---|
| Header | ✅ header.md | ✅ `59:33` (3v / standard / minimal / mega) | ✅ fambox-header (719行) | **3/3** | ✅ 三位一体 | Figma height/sticky-mode property 追加（v0.4）|
| Hero | ✅ hero-section.md | ✅ `67:73` (12v / 4 variant × 3 height) | ✅ fambox-hero-v17-video (578行) | **3/3** | ✅ 三位一体 | preset 拡充（v0.4）|
| Plan Card | ✅ subscription-plan-card.md | ✅ `65:110` (2v / standard / featured) | ✅ fambox-subscription-plan (506行) | **3/3** | ✅ 三位一体 | — |
| Bento Grid | ✅ bento-grid.md | ✅ `91:107` (3v / standard / editorial / autofit) | ✅ fambox-bento-grid (740行) | **3/3** | ✅ 三位一体 | — |
| Modal | ✅ modal.md | ✅ `62:33` (3v / confirmation / detail / sheet) | ✅ fambox-modal (672行) | **3/3** | ✅ 三位一体 | — |
| Footer | ✅ footer.md | ✅ `60:95` (3v / standard / minimal / sitemap-4列) | ✅ fambox-footer (665行) | **3/3** | ✅ 三位一体 | — |
| FAQ | ✅ faq.md | ✅ `93:90` (1v / carousel) | ✅ fambox-faq (419行) | **3/3** | ✅ 三位一体 | Accordion variant（v0.3 拡張枠）|
| Profile | ✅ profile.md | ✅ `96:79` (1v / section) | ✅ fambox-profile (321行) | **3/3** | ✅ 三位一体 | Card variant（v0.3 拡張枠）|
| Case Study | ✅ case-study.md | ✅ `66:91` (3v / tile / story / logo-list) | ✅ fambox-case-study (1102行) | **3/3** | ✅ 三位一体 | — |
| Contact Form | ✅ contact-form.md | ✅ `98:121` (1v / input) | ✅ fambox-contact-form (942行) | **3/3** | ✅ 三位一体 | review/success variant 追加（v0.4）/ Notifications テンプレ手動設定 |
| Drawer | ❌ | ❌ | ❌ | **0/3** | ⚫ 未着手 | spec から開始（顕在化時）|

**L4 サマリ**: 11 中 **10 件 三位一体達成（3/3）** / 0 件 2/3 / 1 件 0/3（Drawer）— **L4 完全制覇 10/10 達成 🏆**（Drawer 除く）

### 7-B. L3 Patterns（4 件 / 一部のみ Section 評価）

| Pattern | spec md | Figma Set | Liquid section | N/3 | Status |
|---|---|---|---|---|---|
| Card | ✅ card.md | ✅ `57:35` (4v / standard / flat / image / horizontal) | ⚪ L4 内包（fambox-bento 等）| Pattern OK | Pattern level ✅ |
| Form Field | ✅ form-field.md | ✅ `56:34` (4v / state: default/focus/error/disabled) | ⚪ Contact Form 内包 | Pattern OK | Pattern level ✅ |
| Stat Card | ✅ stat-card.md | ✅ `64:49` (6v / 3 size × 2 layout) | ✅ fambox-stat-grid (454行) | **3/3** | ✅ 三位一体 |
| Bento Tile | ✅ bento-tile.md | ✅ `87:26` (40v / 4 variant × 5 size × 2 featured) | ✅ fambox-bento-grid 内 `bento_tile` block | Pattern OK | Pattern level ✅（v0.3-liquid で実体化）|

**L3 サマリ**: 4 中 **1 件 独立 Section（3/3）** / 3 件 Pattern として L4 に内包（評価対象外で正常）

### 7-C. L2 Primitives（6 単位 / 8 Primitive 内訳 / Snippet レベル運用）

L2 は通常 **Liquid Section ではなく Snippet (`{%- render '...' -%}`) または Inline コードで運用**。三位一体は **spec ↔ Figma の 2/2 で完了**と定義。

**表記ルール（v0.3-dashboard 標準化 / Session #43）**:
- 1 行 = 1 **DS 要素単位**（spec md ファイル数ではなく Figma Component Set 数で数える）
- spec が **統合記載**の場合は spec 列に「`<md ファイル> §<section>（統合: <他要素>）`」と明示
- Figma Set が **内訳を持つ**場合は「(<variant数>v / 内訳: <kind>)」を Figma 列に明示

| Primitive | spec md | Figma Set | N/2 | Status |
|---|---|---|---|---|
| Button | ✅ button.md | ✅ `46:32` (60v) | **2/2** | ✅ Primitive 完成 |
| Input | ✅ input.md | ✅ `50:26` (12v) | **2/2** | ✅ Primitive 完成 |
| Avatar | ✅ avatar.md | ✅ `53:32` (20v) | **2/2** | ✅ Primitive 完成 |
| **Form Controls** | ✅ form-controls.md **（統合: Checkbox / Radio / Toggle の 3 kind）** | ✅ `54:16` (9v / 3 kind × 3 state) | **2/2** | ✅ Primitive 完成（**3 Primitive 内包**）|
| **Progress Bar** | ✅ progress.md §Progress Bar **（統合: Progress Bar / Spinner）** | ✅ `55:11` (5v / value 0-100) | **2/2** | ✅ Primitive 完成 |
| **Spinner** | ✅ progress.md §Spinner **（統合: Progress Bar / Spinner）** | ✅ `55:21` (3v / size sm/md/lg) | **2/2** | ✅ Primitive 完成（Session #42 で false-negative 修正）|

**L2 サマリ**:
- **Figma Component Set 数で 6/6 完全制覇 🏆**（Button / Input / Avatar / Form Controls / Progress Bar / Spinner）
- **個別 Primitive 数では 8/8**（Form Controls 内訳 3 kind を分解した場合）
- **spec md 数では 5/5**（progress.md / form-controls.md は統合記載で複数 Primitive を含む）
- 統合 spec md は **「機能カテゴリ単位で md を統合」**が正しい設計（学び 95）。3 つの数え方が一致する構造になっている

### 7-D. その他 TOP ページ用 Liquid sections（DS spec 厳密対応外）

> 以下は **TOP ページ専用の合成 section**。DS の L4 Component を**内包・組み合わせ**して使う。三位一体 Section の preset / 内包で代替可能なものもあるが、独自レイアウト保持のため共存。

| Liquid section | 役割 | 移行戦略 |
|---|---|---|
| fambox-active-plans / -v2 | プラン表示の TOP 専用 | Plan Card section 内包に統合候補 |
| fambox-blog-carousel | ブログ記事カルーセル | Bento Grid 内包に統合候補 |
| fambox-easy-cooking | 「3 分で完成」訴求 | Hero preset で代替済（Session #26）|
| fambox-interview | インタビュー風 case | Case Study section に統合候補 |
| fambox-menu-showcase | メニュー横スクロール | 独自 Pattern 保持（tokens.css 移行ガイドあり、Session #26）|
| fambox-model-case | モデル case 表示 | Case Study tile-grid preset に統合候補 |
| fambox-nutrition-service | 栄養サービス紹介 | Bento Grid preset で代替候補 |
| fambox-plan-features | プラン特徴一覧 | Bento Grid preset で代替済（Session #25）|
| fambox-spirit | 「fam-spirit」TOP コア | Bento Grid preset で代替済（Session #25）|
| fambox-value-proposition | 価値提案 | Bento Grid preset で代替済（Session #25）|

### 7-E. 旧 / LP 専用 Liquid（並存保持）

> Session #41（2026-05-15）で各ファイル冒頭に **ラベルコメント**を追加（3 カテゴリ分類）。エディタで開いた瞬間に役割が判別できる。

#### 🎨 LP-ONLY（legacy-but-active / 撤去不要）

| Liquid section | 用途 | 並存理由 / 移行戦略 |
|---|---|---|
| fam-footer-v2 (546行) | LP / プロモ用フッター（コーナー SVG 4 枚の独自世界観）| LP のアートディレクションを破壊しない。通常ページは fambox-footer、LP は fam-footer-v2 を継続使用 |

#### 📝 BLOG-ARTICLE（legacy-but-active / 撤去不要）

| Liquid section | 用途 | 並存理由 / 移行戦略 |
|---|---|---|
| fam-case-study (928行) | ブログ記事用 1-story テンプレ | 個別ブログ記事は fam-case-study を継続使用、TOP / 一覧 / 関連事例 は fambox-case-study |

#### ⚠ LEGACY / pending-migration（v0.4-0.5 で撤去予定）

| Liquid section | 用途 | DS 代替先 |
|---|---|---|
| fam-achievement (306行) | 旧 TOP「導入実績」（ticker 形式）| fambox-bento-grid Auto-fit preset で代替可 |
| fam-issues (276行) | 旧 TOP「課題（ISSUES）訴求」| fambox-bento-grid Editorial Glass/Image-fill で代替候補（spec 未確定）|
| fam-item (300行) | 旧 TOP「商品タイトル（勝負メシ）」| fambox-bento-grid Editorial / Standard preset で代替可 |
| fam-voices (529行) | 旧 TOP「アスリートの声」| fambox-case-study tile-grid preset / fambox-bento-grid Editorial で代替候補 |

移行手順（Week 5 QA で実行）:
1. TOP に fambox-* preset を配置
2. プレビューで視覚比較（旧 vs 新）
3. 承認後に fam-* を撤去 → 最終的に L4 三位一体達成 sections のみで TOP 構成完了

### 7-F. 全体ステータス（2026-05-14 時点）

```
L4 Components:    10/11 三位一体達成 (91%) ✅✅✅✅✅✅✅✅✅✅⚫  🏆 完全制覇
L3 Patterns:      4/4 Pattern level OK   (100%) ✅✅✅✅
L2 Primitives:    6/6 Primitive 完成     (100%) ✅✅✅✅✅✅  🏆 完全制覇
Section 累計新規行: 6,999行 (modal 672 + footer 665 + stat-grid 454 +
                              case-study 1102 + contact-form 942 + hero 578 + plan 506 +
                              faq 419 + profile 321 + header 719 + bento-grid 740)
```

**🏆 L4 + L2 + L3 すべての層で「ほぼ完全」状態へ**

| Layer | 状態 | 残課題 |
|---|---|---|
| L4 Components | 10/11（91%）🏆 | Drawer 1 件のみ（spec から着手・顕在化時）|
| L3 Patterns | 4/4（100%）🏆 | 完成 |
| L2 Primitives | 6/6（100%）🏆 | 完成（Session #42 で Spinner を 2/2 と再評価）|

**次のフォーカス**: Drawer は顕在化時。**TOP ページへの新 sections 配置（Week 5 QA）** が次の主要工程。

---

## 改訂履歴
- v0.2-dashboard (2026-05-14): 完成度ダッシュボード（§7）追加。L4 10/11 中 8 件三位一体達成・L3 4/4 Pattern OK・L2 5/6 Primitive 完成の現状を可視化。Session #38。
- v0.1（2026-04-20）: 初稿。6記事フレームワーク統合＋FAM v0.5 48要素継承マップ＋FAMBOX独自63要素＋段階ロードマップ完成。
