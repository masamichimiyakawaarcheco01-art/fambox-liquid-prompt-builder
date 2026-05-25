---
title: LPB Decision Trace 機構 — ブランド・インテリジェンスの素材蓄積
date: 2026-05-19
tags: [lpb, decision-trace, brand-intelligence, ai-era, ep2-applied, p3]
topics: [engineering, ai, brand]
status: active
priority: high
target_project: tools/liquid-pipeline
related:
  - obara-ai-agent-era-ep2.md
  - design-acceptance-parameters.md
  - ../50_Business_Context/fambox-brand-dna-axes.md
---

# LPB Decision Trace 機構 — ブランド・インテリジェンスの素材蓄積

## なぜ作るか

[尾原Ep2](obara-ai-agent-era-ep2.md) のデシジョントレース機構を LPB v4 に実装する。

> AIガードレールは「人間の事後チェック」ではなく「システム内部の構造」に組み込む。
> 修正履歴からAIが自動的にブランドプレーブックを構築する。

宮川さんが日々 LPB v4 で行う「ここはNG / OK / 修正」の判断履歴を **構造化して保存** することで、後に AI に「FAMBOXらしさ」を学習させる素材になる。

## 実装内容（2026-05-19 着手）

### サーバールート: `/api/decision-trace/*`

| エンドポイント | 役割 |
|---|---|
| `POST /log` | 単一トレースを記録 |
| `GET /list` | 履歴一覧（from/to/axis/reason でフィルタ） |
| `GET /summary` | 集計サマリ（reason・axis・phase別カウント） |
| `POST /suggest-rules` | ルール候補抽出用の Claude プロンプトを生成 |
| `GET /health` | データディレクトリの状態確認 |

実装ファイル: [tools/liquid-pipeline/server/routes/decision-trace.ts](../../tools/liquid-pipeline/server/routes/decision-trace.ts)

### データ構造

```typescript
interface DecisionTraceEntry {
  id: string                     // UUID
  timestamp: string              // ISO 8601
  phase: '40' | '70' | '100' | '120'  // LPB のどのフェーズか
  decision: 'accepted' | 'modified' | 'rejected'
  sectionId?: string             // 対象セクション識別子
  beforeContent: string          // AI が生成したもの
  afterContent?: string          // 人間が修正した結果
  reasonTag: string              // 例: 'color-out-of-range', 'voice-ng-word'
  reasonNote?: string            // 自由記述
  axisInvolved?: 'axis-1' | 'axis-2' | 'axis-3' | 'verbal-guideline' | 'unspecified'
  metadata?: Record<string, unknown>
}
```

### 保存先

- ローカルファイル: `tools/liquid-pipeline/data/decision-traces/YYYY-MM-DD.jsonl`
- 1日1ファイル、JSONL形式（追記しやすい）
- バックアップは git 管理外（プライバシー）

### reasonTag の標準カタログ

ガードレール（[design-acceptance-parameters](design-acceptance-parameters.md)）と整合：

| reasonTag | 説明 | 対応軸 |
|---|---|---|
| `color-out-of-range` | ブランドカラーパレット外 | axis-1 / axis-2 |
| `color-contrast-low` | WCAG AA 未達 | （全軸） |
| `font-not-allowed` | Poppins/Hiragino以外 | verbal-guideline |
| `voice-ng-word` | NG語使用 | verbal-guideline |
| `voice-verb-missing` | Verb Bank未使用 | verbal-guideline |
| `axis-mismatch` | 軸の判定が違う | axis-1 / 2 / 3 |
| `lighthouse-perf-low` | パフォーマンス不足 | （全軸） |
| `image-width-low` | image_url width: 1200未満 | （全軸） |
| `z-index-direct` | ::before/::after を使っていない | （全軸） |
| `tone-mismatch` | トーンが冷静で情熱的でない | verbal-guideline |
| `metaphor-missing` | 軸2の発火/火花/結晶等の視覚隠喩なし | axis-2 |

カタログは運用しながら拡張していく。

## 利用フロー

### 1. Phase 70/100 で UI から呼ぶ（要 UI 改修）

```typescript
// Phase70 で「修正プロンプト生成」ボタンを押した時に、同時にトレース記録
const res = await fetch('/api/decision-trace/log', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    phase: '70',
    decision: 'modified',
    sectionId: currentSection.id,
    beforeContent: aiGenerated,
    afterContent: humanModified,
    reasonTag: 'color-out-of-range',
    reasonNote: 'Primary が #ff5500 → #06c352 へ修正',
    axisInvolved: 'axis-1',
  }),
})
```

### 2. 月次でルール候補を抽出

```bash
# サマリ確認
curl 'http://localhost:3001/api/decision-trace/summary?from=2026-05-01&to=2026-05-31' | jq

# ルール候補抽出プロンプトを生成
curl -X POST 'http://localhost:3001/api/decision-trace/suggest-rules?from=2026-05-01&to=2026-05-31' | jq -r '.claudePrompt'
```

得られたプロンプトを Claude に投入 → 新ルール候補を取得 → [fambox-brand-dna-axes.md](../50_Business_Context/fambox-brand-dna-axes.md) に追加検討。

### 3. 動作確認（インストール直後）

```bash
# サーバー起動
cd tools/liquid-pipeline
npm run dev:server

# 健康チェック
curl -s http://localhost:3001/api/decision-trace/health | jq

# テスト記録
curl -X POST http://localhost:3001/api/decision-trace/log \
  -H 'Content-Type: application/json' \
  -d '{
    "phase": "70",
    "decision": "modified",
    "beforeContent": "AI生成のテスト内容",
    "afterContent": "人間が修正したテスト内容",
    "reasonTag": "axis-mismatch",
    "reasonNote": "軸2のつもりが軸1寄りに生成された",
    "axisInvolved": "axis-2"
  }' | jq

# 一覧確認
curl -s 'http://localhost:3001/api/decision-trace/list?limit=5' | jq

# サマリ確認
curl -s http://localhost:3001/api/decision-trace/summary | jq
```

## 次のステップ（UI統合）

実装済みのバックエンドだけでは「ログAPIが存在する」だけ。実運用には UI 統合が必要：

### Phase 70 UI への統合
- [ ] 既存の差分プロンプト生成ボタンに **「修正履歴として記録」** チェックボックスを追加
- [ ] reasonTag を選択する セレクタ（標準カタログから選ぶ）
- [ ] reasonNote を自由記述する textarea

### Phase 100 UI への統合（Lighthouse連動）
- [ ] Lighthouse監査で失敗した時、自動で `reasonTag: 'lighthouse-perf-low'` 等を記録
- [ ] 人間が「これはOKとして承認」と判断した境界事例も記録

### 月次レビュー UI（任意）
- [ ] `/api/decision-trace/summary` を呼んで、ブラウザでサマリを可視化
- [ ] 「ルール候補を抽出」ボタンで `/api/decision-trace/suggest-rules` 起動
- [ ] 結果を編集 → fambox-brand-dna-axes.md に反映

## ガードレール（このシステム自体の）

- **個人情報**: クライアント名・顧客データを `beforeContent` / `afterContent` に含めない
- **Git管理外**: `data/decision-traces/` は `.gitignore` 推奨（FAMBOXの内部情報を含む可能性）
- **保持期間**: 当面は無期限。年次でアーカイブ判断
- **アクセス権**: ローカルファイルのみ。クラウド同期しない

## 期待される効果

### 短期（1-3ヶ月）
- 修正履歴が **構造化されて蓄積** する
- 同じ修正を繰り返す箇所が **可視化** される
- reasonTag の頻度から **ガードレール強化候補** が見える

### 中期（3-6ヶ月）
- 月次でルール候補抽出 → ガードレールに反映する **ループ** が回る
- LPB v4 の自動生成精度が **段階的に向上**

### 長期（6-12ヶ月）
- AI が学習した「FAMBOXらしさ」が定着 → **事後チェックの工数が大幅減少**
- ARCHECO の競争優位 = **FAMBOXの文脈の濃度** が定量化される

## Ep2 の理論的根拠

> 「組織内の文脈（メール、カレンダー、ドキュメント更新ログ）をAIに学習させることが最強の防壁」
> — 尾原Ep2

LPB v4 の修正履歴は、この **「組織内の文脈」の一部** に相当する。
ARCHECOがFAMBOXに対する深い理解を、システムが代替不能な形で蓄積していく仕組み。

## 関連
- [[obara-ai-agent-era-ep2.md]] — 元思想
- [[design-acceptance-parameters.md]] — reasonTag の元になるガードレール
- [[../50_Business_Context/fambox-brand-dna-axes.md]] — ルール候補の追加先
- [[lpb-human-on-the-loop-roadmap.md]] — LPB全体ロードマップ
- [`tools/liquid-pipeline/server/routes/decision-trace.ts`](../../tools/liquid-pipeline/server/routes/decision-trace.ts) — 実装
