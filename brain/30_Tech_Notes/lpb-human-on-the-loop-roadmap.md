---
title: Liquid Pipeline (LPB) を Human-on-the-Loop へ進化させる
date: 2026-05-15
tags: [liquid-pipeline, lpb, ai-era, human-on-the-loop, automation, p0-foundation, shopify]
topics: [engineering, ai, design]
status: active
priority: high
target_project: tools/liquid-pipeline
current_state: "Step 1-3完了（Phase 40%/70%）、Step 4（Phase 100%）着手予定"
related:
  - obara-ai-agent-era-ep1.md
  - skill-obsolescence-risk-audit.md
  - design-acceptance-parameters.md
---

# Liquid Pipeline (LPB) を Human-on-the-Loop へ進化させる

## 現状（2026-05-15 時点）

[`tools/liquid-pipeline/CLAUDE.md`](../../tools/liquid-pipeline/CLAUDE.md) より：

| Phase | 進捗 | 内容 |
|---|---|---|
| **40% 生成** | ✅ 完了 | Figma取込 → パラメータ抽出 → Claude生成 |
| **70% 調整** | ✅ 完了（APIなし版） | Gemini 9観点比較（手動チェック版） → Claude修正プロンプト |
| **100% 仕上げ** | ⏳ 未着手 | 25項目チェック → 自動修正ループ（最大3回） |
| **120% 超越** | ⏳ 未着手 | AI Studio提案 → Claude実装 → デプロイ |

→ **Step 4（Phase 100%）が次の着手対象**。これを **Human-on-the-Loop 設計** に組み直す。

---

## なぜ「Human-on-the-Loop」に組み直すか

### 現在の運用ボトルネック
- 各Phaseで **人間が目視チェックして承認** している
- 25項目チェックも人手では実用速度に達しない
- 速度のボトルネックは **「人が手で点と点を結びつけるスピード」**（[尾原Ep1](obara-ai-agent-era-ep1.md)）

### Human-on-the-Loop 後の運用
- AI が **判断 + 実行**、人間はループの **外** で監督
- 自動チェック合格 → ステージング自動デプロイ
- 不合格・境界事例のみ人間が判断
- 売上ページ・チェックアウトは **必ず人間レビュー必須**（ガードレール）

---

## Step 4（Phase 100%）の Human-on-the-Loop 設計

### 設計原則
1. **チェック項目はパラメーター化**（[design-acceptance-parameters.md](design-acceptance-parameters.md) 参照）
2. **自動修正ループは3回まで**（無限ループ防止）
3. **3回失敗で人間に escalate**
4. **判断履歴を保持** → 後の学習・改善に使う

### 25項目チェックの構成（提案）

| カテゴリ | 項目数 | 自動 / 人間 |
|---|---|---|
| Lighthouse Performance | 3 | 自動 |
| Lighthouse Accessibility | 3 | 自動 |
| axe-core | 3 | 自動 |
| FAMBOX ブランド準拠 | 4 | 自動（トークン比較） |
| Liquid 構文・schema | 3 | 自動 |
| 画像処理（image_url width: 1200+） | 2 | 自動 |
| z-index 制御（::before/::after） | 1 | 自動（静的解析） |
| タイポグラフィ準拠 | 2 | 自動 |
| カラーコントラスト | 2 | 自動 |
| **境界事例: ブランドDNA軸該当性** | 2 | 人間 |
| **合計** | **25** | **自動 23 / 人間 2** |

→ **92% を自動化**、人間は最後の2項目（軸該当性判定）のみ。

### 自動修正ループのアルゴリズム
```
generate(prompt, params)
  ↓
run_all_checks() → 結果リスト
  ↓
failed = filter(failed)
if failed.empty: → 承認待ちへ
if loop_count > 3: → 人間 escalate
else:
  fix_prompt = create_fix_prompt(failed)
  generate(fix_prompt, params)  ← ループ
```

---

## P0 アクション（今週）：自動テスト1本だけ追加

### 目的
**Human-on-the-Loop を体験する** ための最小実装。
完璧を目指さず、**1本だけ** 動かして、ループのフィードバックを得る。

### 候補：Lighthouse Performance チェック

**理由**：
- ✅ 既存のpipeline出力（HTML/Liquid）を渡せばすぐ動く
- ✅ 結果が数値で出る → 自動判定しやすい
- ✅ Performanceは見えやすい改善 → モチベーション維持
- ✅ FAMBOXに直結する価値

### 実装ステップ（2-3時間）

1. **依存追加**：`lighthouse` パッケージを `tools/liquid-pipeline/server/` に
   ```bash
   cd tools/liquid-pipeline && npm install -D lighthouse chrome-launcher
   ```

2. **API ルート追加**：`server/routes/lighthouse.ts`
   ```typescript
   import { Hono } from 'hono';
   import lighthouse from 'lighthouse';
   import { launch } from 'chrome-launcher';

   const route = new Hono();

   route.post('/api/lighthouse/audit', async (c) => {
     const { url } = await c.req.json();
     const chrome = await launch({ chromeFlags: ['--headless'] });
     const result = await lighthouse(url, {
       port: chrome.port,
       output: 'json',
       onlyCategories: ['performance', 'accessibility'],
     });
     await chrome.kill();
     return c.json({
       performance: result.lhr.categories.performance.score * 100,
       accessibility: result.lhr.categories.accessibility.score * 100,
       failed: extractFailures(result.lhr),
     });
   });

   export default route;
   ```

3. **Phase 100% UI に組込**：`src/components/phases/Phase100/index.tsx`
   - 「Lighthouse監査を実行」ボタン
   - 結果バッジ（Pass/Fail）
   - 失敗時は Claude API へ修正プロンプト自動投入

4. **合格基準**（[design-acceptance-parameters.md](design-acceptance-parameters.md) より）
   - Performance: モバイル 70+
   - Accessibility: 90+

5. **動作確認**
   - 既存のテストFigma URLで生成 → Lighthouse自動実行 → 結果確認

### 不合格時の自動修正プロンプト（テンプレ）
```
以下のLighthouse監査で失敗した項目を修正してください：

【失敗項目】
{failed_items}

【現在のスコア】
- Performance: {performance_score} (目標: 70+)
- Accessibility: {accessibility_score} (目標: 90+)

【元のLiquidコード】
{current_code}

【修正方針】
- 画像のlazy loading追加
- 不要なJavaScriptの削除
- alt属性の追加（不足分）
- セマンティックHTML構造化

ファイル全体を再生成してください（部分スニペット不可）。
```

---

## Phase 100% 全体の実装ロードマップ

### Week 1（このP0）
- [ ] Lighthouse自動テスト1本追加
- [ ] 動作確認（既存テストFigma URLで）

### Week 2-3
- [ ] axe-core 統合
- [ ] FAMBOX ブランドトークン比較ロジック実装
- [ ] 25項目チェッカーの骨格構築

### Week 4
- [ ] 自動修正ループ実装（最大3回）
- [ ] 境界事例 → 人間 escalate UI

### Week 5+
- [ ] ステージング自動デプロイ
- [ ] 売上ページ・チェックアウト判定 → 人間レビュー必須化

---

## ガードレール（再掲）

[design-acceptance-parameters.md](design-acceptance-parameters.md) のルールが LPB の25項目チェックの仕様書になる。

特に **「自動却下」** マークの項目は **修正なしでmergeさせない**：
- Lighthouse 閾値以下
- 画像 width < 1200
- WCAG AA 違反
- ファイル全体出力でない
- z-index 直接指定（疑似要素以外）

---

## 期待される効果

| 観点 | Before | After |
|---|---|---|
| 1セクション生成時間 | 30〜60分（手動チェック含む） | 5〜10分（自動チェック合格まで） |
| 品質のばらつき | 属人化 | ガードレールで一定 |
| 人間の役割 | 全件チェック | 境界事例のみ判断 |
| クライアント説明 | 「経験で良くしました」 | 「○○項目の自動検証通過」 |

---

## 関連
- [[obara-ai-agent-era-ep1.md]] — Human-on-the-Loop の元思想
- [[skill-obsolescence-risk-audit.md]] — 自分のスキル戦略全体
- [[design-acceptance-parameters.md]] — チェック項目の仕様書
- [`tools/liquid-pipeline/CLAUDE.md`](../../tools/liquid-pipeline/CLAUDE.md) — LPB プロジェクトドキュメント
- [[vibe-coding-six-principles.md]] — 本番投入前の安全弁（特に売上/チェックアウト）
