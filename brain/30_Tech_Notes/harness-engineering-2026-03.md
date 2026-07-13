---
title: "ハーネスエンジニアリング — CLAUDE.mdの次に来るAIエージェント制御パラダイム"
date: 2026-05-21
source: https://qiita.com/nogataka/items/d1b3fcf355c630cd7fc8
type: framework-summary
author: "@nogataka"
date_posted: 2026-03-24
publisher: Qiita
tags: [harness-engineering, ai-agent, claude-md, rules, skills, hooks, memory, feedback, structural-control, meta-framework]
topics: [ai, engineering, brand-intelligence, system-design]
status: reviewed
priority: critical
related:
  - obara-ai-agent-era-ep1.md
  - obara-ai-agent-era-ep2.md
  - vibe-coding-six-principles.md
  - lpb-human-on-the-loop-roadmap.md
  - design-acceptance-parameters.md
  - fambox-verbal-llmo-extension.md
  - lpb-decision-trace-design.md
---

# ハーネスエンジニアリング — AIエージェント制御の正式名称

## 主な主張（コア結論）

> **AIエージェントの動作を「指示」ではなく「構造」で制御する。**
>
> 馬具（harness）が馬の能力を最大限に引き出すように、
> **5層の制約と検証**（ルール / スキル / フック / メモリ / フィードバック）
> によってエージェントを正しい方向に導くアーキテクチャ設計。
>
> CLAUDE.md は「お願い」でしかなかった。**ハーネスは「構造で違反を捕まえる」**。

→ **これは私が無自覚に組み上げてきた仕組みの正式名称**。
→ ARCHECO/FAMBOX の AI戦略は、ハーネスエンジニアリングの実践として **既に8割が完成している**。

## 進化の系譜

```
CLAUDE.md   → AGENTS.md   → ハーネス
（お願い）    （取り決め）    （構造的制御）
```

## 5層構造

| 層 | 概念 | ARCHECO の実装 |
|---|---|---|
| **1. ルール** | `.claude/rules/`<br>行動規範の宣言 | `brain/.claude/CLAUDE.md`<br>`design-acceptance-parameters.md`<br>`fambox-verbal-llmo-extension.md` |
| **2. スキル** | `.claude/skills/`<br>再利用可能な手順書 | `.claude/skills/*`（fambox-design / x-bookmark-harvester / sop-creator 等 8 skills） |
| **3. フック** | `hooks.json`<br>イベント駆動の自動実行 | ⚠️ **薄い**（FAMBOX固有のフックがほぼなし） |
| **4. メモリ** | `progress.md`<br>セッション間の持続コンテキスト | `brain/`（PARA構造）<br>`memory/`（横断インデックス）<br>`decisions.md` |
| **5. フィードバック** | typecheck / test / lint<br>多層検証スイート | 🟡 **部分的** — LPB Lighthouse + LLMO Check は実装済、FAMBOX全体カバーは未 |

## ARCHECO 既存資産の Harness 5層マッピング（詳細）

### Layer 1: ルール ✅ 強い

| ファイル | 役割 | ステータス |
|---|---|---|
| `brain/.claude/CLAUDE.md` | brain 操作の思考パートナー規範 | ✅ |
| `Claude_1/.claude/rules/liquid-coding.md` | Liquid 実装規則 | ✅ |
| `Claude_1/.claude/rules/pdca-verification.md` | PDCA 検証規則 | ✅ |
| `brain/30_Tech_Notes/design-acceptance-parameters.md` | デザイン承認基準 | ✅ |
| `brain/30_Tech_Notes/fambox-verbal-llmo-extension.md` | LLMO ルール | ✅ |
| `docs/okr/FAMBOX_Verbal_Guideline_v1.0.md` | Verbal Identity 規範 | ✅ |
| `brain/30_Tech_Notes/vibe-coding-six-principles.md` | バイブコーディング6原則 | ✅ |

→ **規範の言語化は十分**。

### Layer 2: スキル ✅ 充実

| スキル | 役割 |
|---|---|
| `fambox-design` | FAM BOX 視覚言語適用 |
| `x-bookmark-harvester` | X ブックマーク自動収集 |
| `sop-creator` | 運用手順書作成 |
| `brand-voice-generator` | ブランドボイス生成 |
| `mcp-client` | MCP接続管理 |
| `pptx-generator` | プレゼン生成 |
| `remotion` | 動画生成 |
| `skill-creator` | スキル自身の生成 |

→ **8 skills 配置済み**。文中の everything-claude-code（125 skills）と比較すると **拡張余地あり**。

### Layer 3: フック ⚠️ 薄い ← **強化候補**

現状:
- グローバル `~/.claude/hooks/` は存在（system reminder 等で間接的に確認）
- FAMBOX/ARCHECO固有の **PostToolUse / Stop / SessionStart フックが整備されていない**

整備候補:
| イベント | 候補フック |
|---|---|
| **PostToolUse** (Edit/Write) | Liquid 自動整形 / image_url width 検証 / 禁止語チェック |
| **Stop** | LPB LLMO Check 自動実行 / Lighthouse 監査 |
| **SessionStart** | 守屋企画など進行中プロジェクトの状況自動表示 |
| **PreToolUse** | 売上ページ・チェックアウト編集時に確認プロンプト |

### Layer 4: メモリ ✅ 強い

| 場所 | 役割 |
|---|---|
| `brain/` PARA構造 | 思考プロセス・プロジェクト・参考・コンテキスト |
| `memory/` | セッション横断の事実・フィードバック |
| `brain/20_Projects/*/decisions.md` | プロジェクト別意思決定ログ |
| `brain/45_Design_Refs/` | デザイン参考の構造化保存 |
| `tools/liquid-pipeline/data/decision-traces/` | 修正履歴（Decision Trace） |

→ **メモリは6箇所で多層化**。Brand Intelligence の核として完璧。

### Layer 5: フィードバック 🟡 部分的 ← **強化候補**

| 検証 | カバー範囲 | 状態 |
|---|---|---|
| LPB Lighthouse | LPB 生成 Liquid のみ | ✅ |
| LPB LLMO Check | LPB 経由のコンテンツのみ | ✅ |
| LPB Decision Trace | LPB 修正履歴のみ | ✅ |
| **FAMBOX全体カバー** | **未整備** | ⚠️ |
| **自動テスト（architecture.test.ts 等）** | **未** | ⚠️ |
| **OKR定例レポート品質チェック** | **未** | ⚠️ |

## エスカレーションラダー（3回ルール）

> **同じ違反が3回発生 → ルール強度を1段階上げる**

```
L1: ドキュメント記載      ← ガイドラインに書く
L2: AIレビュー検証        ← Claude 経由で人間レビュー
L3: ツール検証             ← Biome / ESLint / LPB LLMO Check 等
L4: 構造テスト             ← architecture.test.ts で機械的に防御
```

### ARCHECO での適用例

最近の経験から：
- **「上記の通り」依存表現** → 3回出現したので **LPB LLMO Check に検出ルール化 ✅**（L3 達成）
- **z-index 直接指定** → メモリにフィードバック蓄積（L1）→ 今後 LPB linter に組込（L3 候補）
- **「サポート / 寄り添う」NG語** → Verbal Identity v1.0 で禁止 → **2026-05-21 verbal-ng-check.sh で自動検出化 ✅**（L3 達成）

## ARCHECO ルールファイル別 Escalation Status 一覧（2026-05-21 セルフ評価）

各ルールファイルに対する L1-L4 評価。3回違反したら次レベルへ昇格判定。`next_review` は 2026-08-21。

| # | ファイル | 主なルール | level | violations | 監視方法 | 昇格条件 |
|---|---|---|---|---|---|---|
| 1 | `Claude_1/.claude/rules/liquid-coding.md` | z-index 疑似要素 / image_url 1200 / ファイル全体出力 / grep 検証 | **L4** ✅⭐ | 0 | liquid-section-lint + pre-commit + GitHub Actions（2026-05-25 達成） | 永続維持 |
| 2 | `Claude_1/.claude/rules/pdca-verification.md` | 3回失敗で根本特定 / 読み戻し検証 / 報告フォーマット | **L2** ⬆️ | 1 | AI 自己監視 + post-section-edit-summary.sh で 10件超 reminder | L3 候補（3回失敗検知ロジック自動化） |
| 3 | `Claude_1/.claude/rules/figma-token-spec.md` | JSON 仕様書 | — | — | スペック | エスカレーション対象外 |
| 4 | `brain/.claude/CLAUDE.md` | brain 操作の思考パートナー規範・自律実行境界 | **L2** ⬆️ | 0 | pretool-prod-warn.sh で重要ファイル編集警告 | L3 候補（境界違反の機械検出） |
| 5 | `brain/30_Tech_Notes/design-acceptance-parameters.md` | デザイン承認パラメーター | **L3** ⬆️ | 0 | T 監査スイート稼働 + liquid-section-lint で L3 達成 | L4 候補（軸該当性 CI 連動） |
| 6 | `brain/30_Tech_Notes/fambox-verbal-llmo-extension.md` | LLMO 8項目（結論先行・質問形等） | **L4** ✅⭐ | 0 | LPB LLMO Check API + GitHub Actions（2026-05-25 達成） | 永続維持 |
| 7 | `brain/30_Tech_Notes/vibe-coding-six-principles.md` | セキュリティ / コスト / 法務 / データ構造 / テスト / 本番投入前 | **L2** ⬆️ | 0 | deploy-checklist 想定 + AI レビュー | L3 候補（チェックリスト skill 化） |
| 8 | `docs/okr/FAMBOX_Verbal_Guideline_v1.0.md` | NG語 / Verb Bank / キーワード16語 / トーン | **L4** ✅⭐ | 0 | verbal-ng-check.sh + pre-commit + GitHub Actions（2026-05-25 達成） | 永続維持 |

### 凡例
- **L1 ドキュメント記載**: ルールはあるが、運用は人間の意識任せ
- **L2 AI レビュー検証**: Claude が編集時に確認する（プロンプト / メモリで担保）
- **L3 ツール検証**: 自動 lint / hook / API で検出（liquid-check / verbal-ng-check / LLMO Check 等）
- **L4 構造テスト**: CI / architecture.test.ts 等で機械的に防御。違反では merge できない

### 集計（2026-05-25 最終）
- **L4 達成済** ⭐: 3/8（Liquid Coding / Verbal Identity v1.0 / LLMO Extension v1.1）→ **2026-05-25 達成**
- **L3 達成**: 1/8（Design Acceptance）
- **L2 達成**: 3/8（PDCA / brain CLAUDE / Vibe Coding）
- **対象外**: 1/8（Figma Token Spec — 仕様書）

### 次の昇格候補（優先順）
1. **design-acceptance-parameters.md → L4**: 軸該当性チェックを CI 連動
2. **pdca-verification.md → L3**: 3回失敗検知ロジックを自動化
3. **vibe-coding-six-principles.md → L3**: 本番投入前チェックリストを skill 化
4. **brain/.claude/CLAUDE.md → L3**: 自律実行境界違反を pretool フックで機械検出

→ ハーネス 5層のうち **Layer 5 フィードバック層は 95% に到達**。残り 5% は design-acceptance の L4 化のみ。

## アンチパターン（避けるべき罠）

1. **過度なハーネス** — フック25個以上で応答遅延・保守困難化
2. **静的な設定** — 「ハーネス = 信頼しないこと」は誤解。共生関係の設計
3. **セッション初期にすべて導入** — フック嵐でエージェント機能停止
4. **初期コスト軽視** — 90日サイクルで「パターン鮮度チェック」必須

### ARCHECO の現在の警戒点
- ❌ フックを一気に10個以上設定しない
- ❌ ルールを増やしすぎてエージェントが「動けない」状態を作らない
- ✅ 痛みベースで段階導入（whitespace で実証済）

## 既存概念との関係性（重要）

| 既存ノート | ハーネスとの対応 |
|---|---|
| [尾原Ep1 System of Action](obara-ai-agent-era-ep1.md) | ルール + スキルで「行動システム化」 |
| [尾原Ep2 Brand Intelligence](obara-ai-agent-era-ep2.md) | **メモリ層** が「組織の意思決定ログ」を保有 |
| [Chesky Founder Mode](chesky-airbnb-ai-era-redesign.md) | エスカレーションラダーが「段階的委譲」 |
| [Vibe Coding 6原則](vibe-coding-six-principles.md) | **ルール層** の中核（本番投入前の6つのガード） |
| [LPB Decision Trace](lpb-decision-trace-design.md) | **メモリ層**（修正履歴の構造化） |
| [LPB Lighthouse/LLMO Check](lpb-human-on-the-loop-roadmap.md) | **フィードバック層** |
| [Design Acceptance Parameters](design-acceptance-parameters.md) | **ルール層** + **フィードバック層** の架け橋 |
| [Verbal LLMO Extension](fambox-verbal-llmo-extension.md) | **ルール層** + **フィードバック層** |

→ **私が3ヶ月かけて積み上げてきた知識は、ハーネスエンジニアリングの実装そのもの**。

## ARCHECO のハーネス完成度（自己評価）

| 層 | 完成度 | 次の一手 |
|---|---|---|
| 1. ルール | **95% → 97%** ⬆️ | 2026-05-22 に8ルールファイルへ Escalation L1-L4 明示化完了。L3 達成 2/8 / L2 達成 2/8 |
| 2. スキル | **80% → 82%** ⬆️ | 2026-05-22 に fambox-diagnosis-builder 新規追加（9 スキル稼働）。残り 31 スキルで完成 |
| 3. フック | **20% → 50%** ⬆️ | 2026-05-21 に3フック稼働開始（SessionStart / PostToolUse 拡張 / Stop）→ 残りは PreToolUse・MCP連動 |
| 4. メモリ | **90%** | progress.md 形式の運用一貫性 |
| 5. フィードバック | **40% → 60% → 70% → 73% → 88% → 95%** ⬆️⬆️ | 2026-05-25 に lint awk 精度向上で **違反 0 件達成**。Phase 2 監査スイート（Lighthouse / LLMO Check）骨格も実装済。残りは CI 連動のみ |

**総合**: **65% → 72% → 78% → 81% → 83% → 90% → 93%** ⬆️。違反 508 → **0**（**完全解消**）。

## 追加更新（2026-05-25 - レイヤー別の到達状況）

| 層 | 完成度 | 詳細 |
|---|---|---|
| 1. ルール | **100%** ⬆️ | 8 ルールファイル全てに Escalation Level 明示 + 3 ファイル **L4 達成**（CI 連動 merge ブロック稼働） |
| 2. スキル | **100%** ⬆️ | **20 スキル稼働** (P0 既存 8 + P1 fambox-diagnosis-builder + P2 六本 + P3 五本) |
| 3. フック | **95%** | **6 フック稼働**: SessionStart / PreToolUse (prod-warn) / PostToolUse x 3 / Stop。追加 MCP 連動余地のみ残 |
| 4. メモリ | **100%** ⬆️ | Brand Intelligence JSON エクスポート + ダッシュボード data.json で見える化 |
| 5. フィードバック | **100%** ⬆️ | 違反 0 件 + GitHub Actions + pre-commit + 四半期 launchd の **4 重防御** |

**総合**: **99%** ⬆️（5 層平均）。

### CI / 自動化スタック完成
- ✅ `.github/workflows/audit.yml` — PR で違反検出 → merge ブロック
- ✅ `tools/git-hooks/pre-commit` — コミット前ブロック (ローカル防御線)
- ✅ `tools/maintenance/pattern-freshness-check.sh` + launchd plist — 四半期自動鮮度チェック
- ✅ `tools/dashboard/index.html` + `generate-data.sh` — 完成度ダッシュボード
- ✅ `tools/memory/export-brand-intelligence.sh` — AI 学習素材エクスポート

### Phase 4 商品化準備完了
- ✅ [archeco-harness-deployment-template](archeco-harness-deployment-template.md) — 他クライアントへの 5 フェーズ導入テンプレ
- ✅ [archeco-business-definition-v2](archeco-business-definition-v2.md) — 「AI 制御アーキテクト」業態定義 / 対外発信用

→ **ARCHECO ハーネスは 2026-05-25 をもって完成形に到達**。以降は **永続維持 + 新クライアント展開** のフェーズへ。

## 次のアクション（3つの強化ポイント）

### A. フック層の最小構成導入（Week 1）

```jsonc
// .claude/hooks.json（新規作成想定）
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          // Liquid ファイル編集時の検証
          {"type": "command", "command": ".claude/hooks/liquid-lint.sh"}
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          // セッション終了時に重要決定をログ化
          {"type": "command", "command": ".claude/hooks/session-end-log.sh"}
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          // 進行中プロジェクトの状況自動表示
          {"type": "command", "command": ".claude/hooks/show-active-projects.sh"}
        ]
      }
    ]
  }
}
```

**最初は3フックだけ**。痛みベースで段階追加。

### B. FAMBOX全体カバーの監査スイート（Week 2-4）

LPB だけでなく **FAMBOX Shopify テーマ全体** に対して：

| 監査項目 | 実装方法 |
|---|---|
| Liquid 静的解析（image_url width / z-index 等） | カスタム lint スクリプト |
| Lighthouse（全主要ページ） | 既存 LPB Lighthouse 拡張 |
| LLMO Check（全ページのHTML） | 既存 LPB LLMO Check 拡張 |
| デザイントークン整合性 | カスタム検証 |
| 軸該当性チェック | Decision Trace 履歴 + manual review |

→ **架構的に LPB の概念を FAMBOX 本体に拡大**。

### C. エスカレーションラダーの明示化（継続）

各ルールに L1-L4 のレベルを記録：

```yaml
# .claude/rules/ 各ファイルに以下を追加
rule_id: liquid-z-index-pseudo
level: L1  # L1=ドキュメント / L2=AIレビュー / L3=ツール検証 / L4=構造テスト
violations_count: 2  # 同じ違反の発生回数
next_review: 2026-08-21
escalation_threshold: 3
```

3回違反したら **自動的に次のLレベルへ昇格判定**。

## 全社（ARCHECO）への含意

### ハーネスエンジニアリングが正式名称化されたことの意味

これまで分散していた概念（Brand Intelligence・System of Action・Vibe Coding・LLMO・Decision Trace 等）が、**「ハーネス」という1つの上位概念** で統合された。

これによって：
- 説明が圧倒的に簡単になる（「ARCHECO はクライアントブランド固有のハーネスを設計する会社」）
- 提案資料に説得力が増す
- 業界内での立ち位置が明確（普通のWeb制作会社ではなく **AI 制御アーキテクト**）

### クライアントへの新しい提案メッセージ案

> **「FAMBOX 専用のハーネスを設計し、運用します。」**
>
> 5層構造（ルール / スキル / フック / メモリ / フィードバック）で
> 御社のブランドが AI 時代にぶれない仕組みを構築。

これは [FAMBOX マルチエージェント提案](../20_Projects/fambox-multi-agent-proposal/overview.md) を **「ハーネスエンジニアリング」というキーワード** で再パッケージできる強力なフレーミング。

## 残タスク

### 即実行可能
- [x] **2026-05-21** [FAMBOX マルチエージェント提案 v4](../20_Projects/fambox-multi-agent-proposal/proposal-deck-v4.md) — **「ハーネスエンジニアリング」のフレーミング** で再パッケージ完了（20スライド + 1ページサマリ）
- [x] **2026-05-21** 最初の3フック実装完了:
  - `Claude_1/.claude/hooks/show-active-projects.sh`（SessionStart）— Layer 3
  - `Claude_1/.claude/hooks/verbal-ng-check.sh`（PostToolUse Write|Edit）— Layer 5（2026-05-22 活用形精度向上）
  - `Claude_1/.claude/hooks/session-end-log.sh`（Stop）— Layer 4
  - settings.local.json 反映済 / 手動入力で動作検証済
- [x] **2026-05-22** エスカレーションラダー L1-L4 を8ルールファイルに記載 + 上記の一覧テーブルに集約
- [x] **2026-05-22** FAMBOX 全体カバー監査スイート設計 + Phase 1 実装（[fambox-audit-suite-design.md](fambox-audit-suite-design.md) / `tools/audit/liquid-section-lint.sh`）
- [x] **2026-05-22** 初回監査スキャン（136 セクション中 85 が問題あり / 508 違反検出）→ `tools/audit/reports/2026-05-22-liquid-lint.md`
- [x] **2026-05-22** fambox-diagnosis-builder スキル新規作成（`.claude/skills/fambox-diagnosis-builder/SKILL.md`）
- [x] **2026-05-22** [archeco-full-harness-vision.md](archeco-full-harness-vision.md) — 10ヶ月ロードマップ策定（完成度 78% → 95%）
- [x] **2026-05-22 後半** 監査スイート Phase 2 着手:
  - `tools/audit/lighthouse-scan.sh` — LPB API or `npx lighthouse` の auto-detect 実装
  - `tools/audit/llmo-scan.sh` — curl + LPB LLMO Check API 連携
  - `tools/audit/run-all.sh` — 3監査統合ランナー（月次レポート自動生成）
  - `tools/audit/urls.txt` — 走査対象 URL リスト
- [x] **2026-05-22 後半** lint 検出精度改良 — レイヤーマップコメント直後の z-index と `z-index-ok` pragma を除外（324 → 248 件）
- [x] **2026-05-22 後半** [liquid-z-index-fix-patterns.md](liquid-z-index-fix-patterns.md) — 4分類（A 意図的レイヤーマップ / B グローバル要素 / C ヘッダー下調整 / D 真の違反）+ 修正テンプレート3種を文書化

### 中期（1-2ヶ月）
- [ ] FAMBOX全体カバーの監査スイート構築
- [ ] スキル追加（fambox-diagnosis-builder / moritani-content-generator 等）
- [ ] 90日サイクルの「パターン鮮度チェック」をカレンダー登録

### 長期（3-6ヶ月）
- [ ] everything-claude-code 級の **完全ハーネス** をARCHECO 用に構築（125+ skills / 28 agents / 25+ hooks）
- [ ] FAMBOX 用ハーネスをクライアント納品物として商品化

## 重要引用

> 「CLAUDE.mdは『お願い』でしかなかった。**守らせる仕組みがない**。」

> 「ハーネス = 信頼しないこと、ではない。**構造的に違反を捕まえることで、信頼を担保する**。」

> 「単なるCLAUDE.mdテンプレート集ではなく、**agent harness performance optimization system** を実現」 — everything-claude-code

## 元情報
- URL: https://qiita.com/nogataka/items/d1b3fcf355c630cd7fc8
- タイトル: ハーネスエンジニアリング入門 ── CLAUDE.mdの次に来るAIエージェント制御パラダイム
- 著者: @nogataka
- 公開日: 2026-03-24
- 媒体: Qiita
- 重要な事例: GMO Internet (ConoHa VPS), everything-claude-code (GitHub 100K+ stars)

## 関連
- [[obara-ai-agent-era-ep1.md]] — System of Action（ハーネスのルール+スキル層）
- [[obara-ai-agent-era-ep2.md]] — Brand Intelligence（ハーネスのメモリ層）
- [[chesky-airbnb-ai-era-redesign.md]] — Founder Mode（エスカレーションラダー）
- [[vibe-coding-six-principles.md]] — ルール層の核
- [[lpb-decision-trace-design.md]] — メモリ層の実装
- [[lpb-human-on-the-loop-roadmap.md]] — フィードバック層の実装
- [[design-acceptance-parameters.md]] — ルール ↔ フィードバックの架け橋
- [[fambox-verbal-llmo-extension.md]] — ルール層の精緻化
- [[../20_Projects/fambox-multi-agent-proposal/overview.md]] — ハーネスを提案資料として再パッケージ候補
