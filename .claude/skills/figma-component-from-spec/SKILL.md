---
name: figma-component-from-spec
description: Markdown 仕様（components/*.md）から Figma Component Set を生成・更新する手順。Marc-Antoine 流の Audit-first / 小さく作って大きく展開 / Build Log 蓄積 を体系化したスキル。Use when generating a Figma Component Set from a spec md, expanding variants, or auditing the spec ↔ Figma gap. Triggers on "Figma に Component を作って", "spec から Figma 化", "L2/L3/L4 を Figma 化", "Component Set 拡張", "spec と Figma の整合性確認".
version: 0.2
last_updated: 2026-05-12
owner: 宮川（FAMBOX DS）
origin: Marc-Antoine（Smart City Kit）の 4 層スタック（L1 Transport / L2 Skill / L3 Tokens / L4 CLAUDE.md / L5 Audit-first）を FAMBOX に翻訳。2026-05-12 の 7 セッションで得た 20 項の学び + 7 つの実問題（Issue 1-7）を体系化
---

# figma-component-from-spec

Markdown 仕様 (`brand/<brand>/design-system/components/*.md`) を一次資料に、**Figma Component Set を生成・更新・監査**するための作業手順。**figma-use Skill が前提**（Plugin API の作法は figma-use を参照）。

## いつ使うか

- 新しい L2/L3/L4 spec を Figma 化する
- 既存 Component Set に state / variants を追加拡張する（Phase 2）
- spec md と Figma 実態の整合性を audit する
- Build Log（`operations/figma-build-log.md`）にセッション記録を残す

## 前提

- 対象 brand の `brand/<brand>/design-system/` 構造が整備済（spec md + tokens + operations）
- Figma File に Variables（`color/*`, `bg/*`, `border/*`, `radius/*` 等）と Effect Styles（`shadow/1` 〜 `shadow/5`）が定義済
- `figma-use` Skill を事前に load 済

---

## ワークフロー（Marc 流 7 ステップ）

### Step 0: Audit-first（**最重要・絶対省略禁止**）

**何かを Figma で作る前に、必ず既存 Component Set を全件確認** する。これを怠ると重複生成・統合作業の二重コストが発生する。

```js
// findAll で全 COMPONENT_SET を列挙
const results = [];
for (const page of figma.root.children) {
  await figma.setCurrentPageAsync(page);
  page.findAll(n => {
    if (n.type === 'COMPONENT_SET') {
      results.push({ id: n.id, name: n.name, page: page.name, variants: n.children.length });
    }
    return false;
  });
}
return results;
```

**該当 spec と一致する Component Set が存在する場合**:
- それを起点にして「spec ↔ Figma の差分」だけを補完する（新規生成ではなく audit + 補完）
- 例: Card は既に存在していて shadow だけ未適用だった → shadow 1 つ追加で完了

### Step 1: Spec md を一次資料として読み込む

- `components/<component>.md` を完全読み込み
- 重要セクション: 概要 / Variants / Sizes / 共通 Props / CSS（v0.2 実装）/ Do-Don't
- spec の **数値（padding / radius / font-size / line-height）** は厳守
- spec の **DNA Anti リスト** に違反する実装は絶対避ける

### Step 2: Variables / Effect Styles の現状取得

```js
const allVars = await figma.variables.getLocalVariablesAsync();
const wanted = ['bg/primary', 'border/light', 'color/drive', 'radius/md', ...];
const found = allVars.filter(v => wanted.some(w => v.name.toLowerCase().includes(w)))
  .map(v => ({ id: v.id, name: v.name, type: v.resolvedType }));

const effectStyles = await figma.getLocalEffectStylesAsync();
const shadows = effectStyles.filter(s => /shadow/i.test(s.name)).map(s => ({ id: s.id, name: s.name }));
```

**alias variables の健全性確認**（Issue 1 再発防止）:
- Tokens Studio から import した alias が純白 `{r:1,g:1,b:1,a:1}` に固定化されていないか
- 確認方法: `valuesByMode` の値が `VARIABLE_ALIAS` 型になっているか、SOLID color になっていないか
- 異常時は `setValueForMode` で正しい alias に再接続

### Step 3: Component Set 構築（小さく作って大きく展開）

**Phase 1 = 代表 variant / 代表 size のみ作る**。Phase 2 で残を拡張する戦略を取る。

例: Button v0.3 → state property 追加（4 states × 5 variants × 3 sizes = 60 variants だが、 まず default の rename だけで state property を認識させ、その後 hover / disabled / loading を個別 step で追加）。

```js
// Standard pattern: build each variant as a Component, then combineAsVariants
const variant1 = figma.createComponent();
variant1.name = 'variant=primary';
// ... auto-layout / fills / strokes / text setup
const variant2 = figma.createComponent();
variant2.name = 'variant=secondary';
// ...
const set = figma.combineAsVariants([variant1, variant2, ...], parentPage);
set.name = 'ComponentName';
```

**combineAsVariants は 1 variant でも有効**（学び 17）— 将来 variant 追加余地のある Component は最初から Component Set でラップする。

### Step 4: スクリーンショット検証

```js
// 各 Set 完成後、必ず get_screenshot で視覚確認
mcp__figma__get_screenshot({ fileKey, nodeId: set.id, maxDimension: 1800 })
```

確認項目:
- spec の数値（padding / radius / font-size）と一致しているか
- variant 名がプロパティパターン（`prop1=val1, prop2=val2`）に従っているか
- 期待のサイズで Set 全体が表示されているか（Set の height が縮退していないか — Issue 5）

### Step 5: spec md に Figma 参照を追記

`components/<component>.md` の末尾「Change Log」の前に **`## Figma 参照` セクション** を必ず追加:

```markdown
## Figma 参照

- File: `<Project Name>`（`<fileKey>`）
- Page: `<ページ名>`
- **Component Set ID**: `XX:YY` ✅（生成日）
- 生成スキル: `figma-component-from-spec` vX.X
- **実装済 variants**: N（`prop1` × `prop2`）
- **Variable バインド**: fills / strokes / effects の Variable 名
- **未実装（次バージョンで追加予定）**: ...

## Change Log
- v0.X-figma (YYYY-MM-DD): セッション概要
```

### Step 6: figma-build-log.md にセッション記録を追加

`operations/figma-build-log.md` の末尾に **新 Session セクション** を追加:

```markdown
## Session YYYY-MM-DD (#N) — <Component> v0.X <意図>

**契機**: ...

### 成果

| Component | 状態 | Variants | Set ID | 操作内容 |
|---|---|---|---|---|

### 発生問題と修復
#### 🐛 Issue X: <症状>
- 症状 / 原因 / 影響範囲 / 修復 / 再発防止

### 学んだこと（追加）
N. ...

### Known TODOs（vX.X 残）
- ...
```

### Step 7: 整合性 milestone を current.md に記録

`current.md` の `milestone:` ブロックに 1 行追加し、Component 追加 / variants 数 / 残課題を明記する。

---

## 既知の罠（Issue 1-7）

セッションで実際に踏んだ罠と対処。これらを **回避する書き方を最初から採用** する。

### Issue 1: alias Variables が純白固定化（import 由来）
- Tokens Studio import で alias 参照が解決失敗、純白 `{r:1, g:1, b:1, a:1}` になる
- **対処**: 起動時に alias variable の `valuesByMode` を全件チェックし、`VARIABLE_ALIAS` 型に再接続
- **回避**: Step 0 で必ず Variable 健全性を確認

### Issue 2: Textarea placeholder が縦書きで wrap
- `figma.createText()` の初期 width が極小、`textAutoResize='HEIGHT'` で固定された
- **対処**: `appendChild` 後に `resize(innerWidth, height) → textAutoResize='HEIGHT' → layoutSizingHorizontal='FILL'` の順
- **回避**: 多行テキストは作成順序を守る

### Issue 3: link variant の `textDecoration` で「フォント未ロード」エラー
- 事前 loadFont が漏れていた変種フォントで text 操作したらエラー
- **対処**: text node の `fontName` を読み取って `loadFontAsync(tn.fontName)` で動的ロード
- **回避**: clone した text node には常に動的フォントロードを噛ます

### Issue 4: clone 直後の variants が同位置に重なる
- Component Set が `layoutMode: 'NONE'` だと clone が親と同座標
- **対処**: state / variant ごとに x オフセットを手動付与
- **回避**: 拡張前提の Component Set は **`layoutMode: 'HORIZONTAL'` か `'VERTICAL'` で auto-layout 化** を検討

### Issue 5: `resize(W, H)` 後の子追加で AUTO sizing が再計算
- `primaryAxisSizingMode: 'AUTO'` だと子追加で HUG（コンテンツ依存）に縮む
- **対処**: 子追加後に `primaryAxisSizingMode = 'FIXED'` を明示し、再 `resize`
- **回避**: 固定サイズの auto-layout は **resize → 子追加 → FIXED 設定 → 必要なら再 resize** の順

### Issue 6: `layoutPositioning = 'ABSOLUTE'` は親が auto-layout の時のみ
- `layoutMode: 'NONE'` の親内で ABSOLUTE 設定するとエラー
- **対処**: NONE 親では `layoutPositioning` 不要、直接 `x/y` で配置
- **回避**: 親の `layoutMode` を判定してから ABSOLUTE 設定

### Issue 7: `parent.removeChild(child)` は存在しない
- DOM API 慣性で書くと `TypeError: no such property 'removeChild'`
- **対処**: `child.remove()` を使う（Plugin API のノード削除はこれ）
- **回避**: そもそも条件分岐で「削除する場面」を作らず、最初から分岐前置で必要な要素だけ作る

---

## ベストプラクティス（学び 1-20）

セッションで蓄積した実用知。コード書く前に再確認すべき。

### 構造設計
1. **Audit-first 体制化**: 30 分の investigation が数時間の重複生成を防ぐ。L2/L3/L4 全層で有効
2. **小さく作って大きく展開**: state × variant × size の組合せ爆発（60+ variants）は段階生成
3. **Phase 1 で型作り → Phase 2 で拡張**: 代表型を作ると、その後の追加は同関数の引数増だけで済む
4. **1 variant でも Component Set 化**: 将来 variant 追加余地に備える

### Variable / Style bind
5. **Variable 健全性確認は起動時必須**: 純白固定 alias を発見・修復
6. **paint 再構築パターン**: `setBoundVariableForPaint` の戻り値で配列を再構築（既存 fills の in-place 改変は不安定）
7. **Effect Style は `setEffectStyleIdAsync` が必須**（同期 setter は使えない）
8. **shadow / radius / border-width は Variable bind**（直値は避ける）

### Layout
9. **layoutMode: 'NONE'` は state 拡張に向かない**: auto-layout 化（HORIZONTAL/VERTICAL）が安全
10. **`primaryAxisSizingMode = 'FIXED'` を明示**: 固定サイズの auto-layout に必須
11. **`individualStrokeWeights` で部分ボーダー**: CSS `border-right` 相当を `strokeRightWeight = N` で実現
12. **`spacer frame` で個別 margin**: itemSpacing は均一前提、異なる margin が必要なら空 frame 挟む

### 配置 / 整列
13. **Page 判定は `node.parent` を辿る**: `getNodeByIdAsync` は document-wide 検索のため誤判定しやすい
14. **Set 全体の resize は明示**: variants の高さに自動追従しないことがある（`set.resize(W, H)` で強制拡張）
15. **`combineAsVariants` の戻り値 set を使う**: 個別 Component への参照は無効化される場合あり

### Text
16. **Font は node ごとに動的ロード**: text の `fontName` を読んで都度 `loadFontAsync`
17. **`setRangeFontSize` / `setRangeFills`**: 単語内で size / color を変えるとき有効（例: `-3.2 kg` の kg だけ 22px sub）

### Gradient / Effect
18. **Linear Gradient は行列指定**: `gradientTransform: [[0,1,0],[-1,0,1]]` が上→下方向

### Instance / 再利用
19. **`child.createInstance()` で既存 Component 埋込**: Submit Button などを既存 Set から instance 化、双方向反映が機能
20. **必須 badge は label row 内の HORIZONTAL frame**: CSS inline-flex 相当を実現

---

## チェックリスト（コミット前）

- [ ] Step 0 Audit-first を実行した（既存 Component Set 一覧を確認した）
- [ ] spec md を完全読み込み、Variants / Sizes / Props / Do-Don't を把握した
- [ ] 使う Variables / Effect Styles の ID を取得した
- [ ] 各 variant のスクリーンショットを get_screenshot で視覚確認した
- [ ] spec md に「## Figma 参照」セクションを追加した（ID / variants / Variable bind / TODO）
- [ ] figma-build-log.md に Session #N を追加した（成果 / 発生 Issue / 学び / TODO）
- [ ] current.md の milestone 行を追加した
- [ ] git commit + push までを完了した

---

## 関連

- `figma-use` — Plugin API の作法（必須前提）
- `brand/<brand>/design-system/operations/figma-build-log.md` — 過去セッションの完全記録
- `brand/<brand>/design-system/current.md` — milestone と全 Component マッピング
- `brand/<brand>/design-system/components/*.md` — 各 Component の一次資料
