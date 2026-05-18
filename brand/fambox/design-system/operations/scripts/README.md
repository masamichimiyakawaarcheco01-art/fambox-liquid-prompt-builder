# DS Dashboard Generator

`current.md §7 完成度ダッシュボード` を Audit 結果（fixture）+ 実 file scan から自動生成する Python script。

## ファイル構成

```
operations/scripts/
├── README.md                 ← このファイル
├── generate-dashboard.py     ← メインスクリプト
└── figma-sets.json           ← Figma Audit fixture（手動更新）
```

## 使い方

### 1. ダッシュボード出力（stdout）

worktree root から実行:

```bash
python3 brand/fambox/design-system/operations/scripts/generate-dashboard.py
```

stdout に `current.md §7` 全体（§7-A 〜 §7-F、§7-D / §7-E は手動管理）が Markdown 形式で出力される。

### 2. current.md への反映

**自動上書きはしない**（人間レビュー必須）。出力を確認 → 差分を手動で current.md §7-A / §7-B / §7-C / §7-F に反映する:

```bash
python3 brand/fambox/design-system/operations/scripts/generate-dashboard.py > /tmp/dashboard.md
# /tmp/dashboard.md を current.md と diff して反映箇所を判断
diff /tmp/dashboard.md brand/fambox/design-system/current.md
```

### 3. fixture 更新フロー

Figma Component Set に変更があった場合は `figma-sets.json` を更新:

#### Step A: SKILL v0.7 Step 0.5 詳細 Audit を実行

`.claude/skills/figma-component-from-spec/SKILL.md` line 54-144 のテンプレを `use_figma` で実行し、対象 Set の最新情報を取得:

```js
const targets = [
  { id: '<set-id>', label: '<component name>' },
  // ...
];
// → variant 数 / property variantOptions / overlapping / overflow を取得
```

#### Step B: figma-sets.json の該当 entry を更新

```json
{
  "name": "Header",
  "spec_md": "header.md",
  "figma_id": "59:33",
  "variants": "3v / standard / minimal / mega",  ← properties[].variantOptions を反映
  "liquid": "fambox-header.liquid",
  "note": ""
}
```

#### Step C: `_meta.last_audit` と `last_audit_session` を更新

```json
{
  "_meta": {
    "last_audit": "2026-05-15",      ← Audit 実行日
    "last_audit_session": "#42",     ← 該当 Session 番号
    ...
  }
}
```

#### Step D: スクリプト再実行で出力検証

```bash
python3 brand/fambox/design-system/operations/scripts/generate-dashboard.py
```

## 設計意図

### 3 つの数え方を併記（学び 97）

L2 Primitives は **3 つの数え方** で同時カウント:

| 軸 | 数 | 用途 |
|---|---|---|
| Figma Component Set 数 | 6 | デザイナーの認知（Figma 上の管理単位）|
| 個別 Primitive 数 | 8 | ユーザーの認知（独立した UI 要素）|
| spec md 数 | 5 | エンジニアの認知（触る md ファイル数）|

`primitive_count` field で各 entry の **個別 Primitive 数**を明示（Form Controls は 3、他は 1）。

### N/3 / N/2 ラベル化（学び 77）

各 layer の評価基準が異なる:

- **L4 Components**: spec ↔ Figma ↔ Liquid section の **N/3**
- **L3 Patterns**: 一部 N/3、他は **Pattern level OK**（L4 内包で評価対象外）
- **L2 Primitives**: spec ↔ Figma の **N/2**（Liquid は Snippet レベル運用）

### 自動 scan vs 手動 fixture

| 情報源 | 取得方法 | 鮮度 |
|---|---|---|
| spec md 存在 | 実 file scan（自動）| リアルタイム |
| Liquid section 存在 & 行数 | 実 file scan（自動）| リアルタイム |
| Figma Set ID / variants 内訳 | fixture（手動）| Audit 実行時点 |

→ **spec / Liquid は実態追従、Figma は手動 fixture 更新**。Figma 自動同期は Phase 2 候補（MCP `use_figma` 連携の自動化）。

## ロードマップ

### Phase 1（現在 / v0.3-dashboard）✅
- ✅ fixture + 実 file scan のハイブリッド
- ✅ stdout 出力（人間レビュー必須）
- ✅ N/3 + 3 つの数え方併記
- ✅ Figma variants 内訳明示

### Phase 2（候補 / v0.4-dashboard）
- Figma audit の自動連携（`use_figma` 経由で `figma-sets.json` を自動更新）
- current.md §7 への **差分自動反映**（git diff -p で適用可能な patch 出力）
- Stale 検出（fixture last_audit が 30 日以上前なら警告）
- TOP / LP 専用 sections（§7-D / §7-E）の自動 scan

### Phase 3（候補 / v0.5-dashboard）
- 複数 brand（FAM / FAMBOX）横展開
- CI 統合（PR 時に diff コメント自動投稿）
- ダッシュボード履歴の version 管理

## 制約

- **`figma.notify` / `figma.closePlugin` は使わない**（SKILL `figma-use` 規則）
- `figma-sets.json` の更新は **手動**（Phase 2 で自動化候補）
- スクリプトは **stdout のみ**。current.md への直接上書きは安全のためしない
- spec md / Liquid section の存在は file scan のみで判断（内容の充実度までは見ない → 学び 96 の false-negative は **fixture 側で明示**して防ぐ）

## 関連

- `current.md §7` — 出力の反映先
- `.claude/skills/figma-component-from-spec/SKILL.md` v0.7 — Step 0.5 詳細 Audit テンプレ
- `operations/figma-build-log.md` — Audit 履歴（Session 単位）
