---
title: Liquid z-index 修正パターン集 — Decision Trace素材
date: 2026-05-22
tags: [liquid, z-index, fix-patterns, decision-trace, harness-feedback, fambox]
status: active
priority: high
related:
  - ../../.claude/rules/liquid-coding.md
  - fambox-audit-suite-design.md
  - harness-engineering-2026-03.md
  - ../../tools/audit/liquid-section-lint.sh
---

# Liquid z-index 修正パターン集

## 位置づけ

[liquid-coding.md](../../.claude/rules/liquid-coding.md) の **「z-index が絡む要素は ::before/::after 疑似要素で処理する」** ルールに対する、文脈別の **許容パターン + 真の違反 + 修正テンプレート** を体系化した Decision Trace 素材。

[初回監査スキャン](../../tools/audit/reports/2026-05-22-liquid-lint.md) で 324件の z-index 違反を検出したが、その大半は **意図的なレイヤリング** であり機械的修正は不要と判明。本書は ARCHECO 知見として **どこを直すべきで、どこは触らないか** を明確化する。

## 4分類

z-index の用途を 4 つに分類し、A-C は許容、D のみ修正対象とする。

| 分類 | 例 | ルール | 監査での扱い |
|---|---|---|---|
| **A. 意図的レイヤーマップ** | Hero / 多層構成セクションでの `.bg{z:1} .text{z:4}` 等 | **許容** | lint で **除外**（コメント直後10行内） |
| **B. グローバル要素の z-index** | Modal / Drawer / Sticky CTA | **許容**（要トークン化検討） | lint で **除外**（pragma `z-index-ok` で明示） |
| **C. ヘッダー下調整** | `z-index: 1; /* ヘッダー(z:3-4)より下に配置 */` | **許容**（コメント必須） | lint で **除外**（コメント検出） |
| **D. 真の違反** | 兄弟要素間の積み重ねを意味なく z-index で解決 | **修正**（::before/::after 化） | lint で **検出** |

---

## A. 意図的レイヤーマップ（許容）

### 典型例（`fambox-hero-v17.liquid` より）

```css
/* ── SP z-index レイヤー構造 ──
       .fv17::before  z3  グラデーション（疑似要素）
       ┌ z1  動画 (.fv17-bg)
       ├ z2  皿アニメーション / 皿ロゴ / アクター画像
       ├ z3  .fv17::before グラデーション
       ├ z4  テキスト（h1・サブ）← グラデの上・最前面
       ├ z5  コーナーアイコン / CTAボタン
       └ z6  フッター黒帯
    ── */
.fv17-bg          { z-index: 1; }
.fv17-dish-wrap   { z-index: 2; }
.fv17-dish-logo   { z-index: 2; }
.fv17-actors      { z-index: 2; }
.fv17-text        { z-index: 4; }
.fv17-corner      { z-index: 5; }
.fv17-cta-wrap    { z-index: 5; }
.fv17-footer      { z-index: 6; }
```

### 許容する理由
- **レイヤー構造がドキュメント化されている**（コメントブロックで明示）
- **値が連番で意味を持つ**（1=底, 6=最前面）
- **::before/::after 化すると保守性が下がる**（複雑な多層構成では明示的レイヤー番号の方が読みやすい）

### 該当セクション（既知）
- `fambox-hero-v17.liquid` / `fambox-hero-v17-video.liquid`
- `fam-corp-hero.liquid`
- `fambox-spirit.liquid` / `fam-spirit.liquid`
- `fam-solution.liquid`

### lint 除外条件
コメント（`/* ... */`, `<!-- ... -->`, `// ...`）に `z-index` / `レイヤー` / `layer` のいずれかが含まれていれば、**直後10行内の z-index 行を除外**。実装済（`tools/audit/liquid-section-lint.sh`）。

---

## B. グローバル要素の z-index（許容 / 要トークン化）

### 典型例（`fambox-modal.liquid`）

```css
.fambox-modal {
  position: fixed;
  top: 0; left: 0;
  z-index: 9999;  /* z-index-ok: モーダルは最前面 */
}
```

### 許容する理由
- Modal / Drawer / Sticky CTA / Tooltip は **ページ全体に対する積み重ね順序** が必要
- ::before/::after では実現不可（要素そのものの z-index が必要）

### ルール化提案
- **値は CSS 変数化** する（将来の Phase 3 で `--z-modal: 9999; --z-drawer: 9000; --z-sticky: 100;` 等のトークン化）
- **行末に `/* z-index-ok: 用途 */` pragma を必須** にする（lint で除外、コードレビューで意図確認）

### 該当セクション（既知）
- `fambox-modal.liquid`
- `fambox-drawer.liquid`
- `fam-sticky-cta.liquid`
- `fam-nav.liquid`（header）

### lint 除外条件
行内に `z-index-ok` 文字列があれば除外。実装済。

---

## C. ヘッダー下調整（許容 / コメント必須）

### 典型例（`fambox-faq.liquid`）

```css
.fambox-faq {
  position: relative;
  z-index: 1; /* ヘッダー(z-index:3-4)より下に配置 */
}
```

### 許容する理由
- 既存ヘッダーの z-index 値（3-4）を **意識した相対値** 設定
- 「下に配置」という明確な意図がコメントで伝わる

### ルール化
- **必ずコメントで「なぜその値か」を説明する**
- コメントなしの `z-index: 1` は D（真の違反）として扱う

### lint 除外条件
A の検出ロジック（コメント内 z-index 言及）で除外される。

---

## D. 真の違反（修正対象）

### 典型例

```css
/* ❌ NG: 兄弟要素間の積み重ねを z-index で解決 */
.card-wrap {
  position: relative;
}
.card-bg-image {
  position: absolute;
  z-index: 1;
}
.card-content {
  position: relative;
  z-index: 2;  /* 画像の上に文字を載せたいだけ */
}
```

### 修正テンプレート1: ::before/::after 化

```css
/* ✅ OK: 背景を ::before に */
.card-wrap {
  position: relative;
}
.card-wrap::before {
  content: "";
  position: absolute;
  inset: 0;
  background: url(...);
  /* z-index 不要。::before は自然に下層 */
}
.card-content {
  position: relative;
  /* z-index 不要 */
}
```

### 修正テンプレート2: stacking context で隔離

```css
/* ✅ OK: 親に isolation を付けて子の z-index を局所化 */
.card-wrap {
  position: relative;
  isolation: isolate;  /* これで子要素の z-index が外部に影響しない */
}
```

### 修正テンプレート3: 順序のみで解決

```css
/* ✅ OK: HTML 順序 + position で十分なケース */
/* HTML:
   <div class="card-wrap">
     <img class="card-bg">  ← 先に書く = 下層
     <div class="card-content">  ← 後に書く = 上層
   </div>
*/
.card-bg { position: absolute; inset: 0; }
.card-content { position: relative; }  /* z-index 不要 */
```

### 該当セクション候補（要 grep 確認）
監査レポート [2026-05-22-liquid-lint.md](../../tools/audit/reports/2026-05-22-liquid-lint.md) の z-index 違反 248件のうち、上記 A/B/C 除外後に残るもの。次のセッションでの修正対象。

---

## 修正実行ガイドライン

### 修正してよい条件
1. **WF→承認→Liquid変換→比較検証→修正→書き出し** のサイクルに乗っている
2. 修正前後を **grep + DevTools Computed で検証**
3. 視覚的に **本番と差分がない** ことを確認

### 修正してはいけない条件
1. 本番影響範囲が広い Hero セクション（A 分類）
2. Modal / Drawer のグローバル z-index 値（B 分類・値は不変）
3. 「これは触らないで」と decisions.md に明記されているセクション

---

## エスカレーションラダーへの影響

[liquid-coding.md Escalation Status](../../.claude/rules/liquid-coding.md#escalation-status) と接続：

| 項目 | 現状 | 本書による変化 |
|---|---|---|
| ルール: z-index 直接指定禁止 | L2 (AI レビュー + grep) | **L2 維持** — 機械検出は精緻化済 (324 → 248件) |
| L3 昇格条件 | T 監査スイートで完全機械化 | A/B/C 例外条件を pragma で明示化 → 真の違反 248件のみ追跡 |
| L4 昇格条件 | CI 連動で merge ブロック | Phase 5 で実現 |

→ 本書が **L3 昇格判定の解像度を上げた**。違反 324 → 248件のうち、D に該当する **真の違反は更に絞り込み可能**（次セッションで分類詳細化）。

---

## 次のアクション

1. **Modal/Drawer 系セクション** に `/* z-index-ok: 用途 */` pragma を追加（5-6ファイル / 各 1 箇所程度）
2. 監査レポートを再実行 → 真の D 違反件数を確定
3. D の修正は **小規模セクション 3-5 個から段階着手**（Hero 系は触らない）
4. CSS 変数化（`--z-modal` 等）を Phase 3 で導入

---

## 関連

- [[../../.claude/rules/liquid-coding.md]] — 元ルール
- [[fambox-audit-suite-design.md]] — 監査スイート設計
- [[harness-engineering-2026-03.md]] — Escalation Status 一覧
- [[../../tools/audit/liquid-section-lint.sh]] — 検出ロジック
- [[../../tools/audit/reports/2026-05-22-liquid-lint.md]] — 初回スキャン結果
