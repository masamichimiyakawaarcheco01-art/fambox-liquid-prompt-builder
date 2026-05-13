---
name: figma-component-from-spec
description: Markdown 仕様（components/*.md）から Figma Component Set を生成・更新・統合する手順。Marc-Antoine 流の Audit-first / 小さく作って大きく展開 / Phase 戦略（1=新規 / 2=property 拡張 / 3=参照確立）/ instance swap / 寸法から size 自動推定 / Build Log 蓄積 を体系化したスキル。Use when generating a Figma Component Set from a spec md, expanding variants (state / size / boolean property / featured), replacing placeholders with instances, or swapping existing instances to different variants. Triggers on "Figma に Component を作って", "spec から Figma 化", "L2/L3/L4 を Figma 化", "Component Set 拡張", "variant property 追加", "instance に置換", "featured 追加", "instance を swap", "spec と Figma の整合性確認".
version: 0.4
last_updated: 2026-05-12
owner: 宮川（FAMBOX DS）
origin: Marc-Antoine（Smart City Kit）の 4 層スタック（L1 Transport / L2 Skill / L3 Tokens / L4 CLAUDE.md / L5 Audit-first）を FAMBOX に翻訳。2026-05-12 の 14 セッションで蓄積した 35 項の学び + 11 の実問題（Issue 1-11）+ Phase 1/2/3 戦略 + Phase 3 の 2 パターン（placeholder→instance / instance→instance swap）を体系化
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

### Step 3: Component Set 構築（小さく作って大きく展開 + Phase 戦略）

**Phase 戦略**で進める。Phase 1 で型を作り、Phase 2 で量を増やし、Phase 3 で他 Component との参照を確立する。

#### Phase 1: 新規生成（代表 variant のみ）

代表 variant / 代表 size だけ作る。Phase 2 で残を拡張する戦略。

```js
// Standard pattern: build each variant as a Component, then combineAsVariants
const variant1 = figma.createComponent();
variant1.name = 'variant=primary';
// ... auto-layout / fills / strokes / text setup
const variant2 = figma.createComponent();
variant2.name = 'variant=secondary';
const set = figma.combineAsVariants([variant1, variant2, ...], parentPage);
set.name = 'ComponentName';
```

**combineAsVariants は 1 variant でも有効**（学び 17）— 将来 variant 追加余地のある Component は最初から Component Set でラップする。

#### Phase 2: 既存 Set への variant property 拡張

既存 Set に新 property（state / size 等）を追加する場合は **rename → clone → grid 配置** のフローを使う。

```js
// 1) Rename existing variants to include the new property's default value
for (const v of set.children) {
  if (!v.name.includes('state=')) v.name = v.name + ', state=default';
}

// 2) Clone defaults and set the new property value
const defaults = set.children.filter(c => c.name.includes('state=default'));
for (const def of defaults) {
  const clone = def.clone();
  clone.name = def.name.replace('state=default', 'state=hover');
  set.appendChild(clone);
  // Apply variant-specific changes (color, border, etc.)
}
```

**配置規則（学び 24, 26）**:
- **1D 拡張**（state ごとなど）: 既存 variants の縦並び（または横並び）パターンを inspect で確認し、その規則を踏襲。例: y = 既存最終 y + 既存最終 height + 100px gap
- **2D 拡張**（variant × size のような 2 property 全展開）: **列 = property1 / 行 = property2 の matrix 配置**がレビューしやすい。`x = cIdx * COL_W, y = rIdx * ROW_H`

```js
// 2D matrix layout example
const COL_W = 600;  // max width across variants
const ROW_H = 400;  // max height across sizes
for (const v of set.children) {
  const m = v.name.match(/variant=([^,]+), size=([^,]+)/);
  const cIdx = variantOrder.indexOf(m[1]);
  const rIdx = sizeOrder.indexOf(m[2]);
  v.x = cIdx * COL_W;
  v.y = rIdx * ROW_H;
}
set.resize(variantOrder.length * COL_W, sizeOrder.length * ROW_H);
```

#### Phase 3: Component 間の参照確立（2 パターン）

別 Component の **placeholder を本 Component の instance に置換** または **既存 instance を別 variant に切替** することで、**「Component 単体修正が demo に自動反映」される双方向参照**を確立する。

##### Pattern A: placeholder → instance（新規 instance 作成）

```js
// 1) Get target Set + source Component map
const targetSet = await figma.getNodeByIdAsync(targetSetId);
const sourceVariant = sourceSet.children.find(c => c.name === 'variant=X, size=Y');

// 2) For each placeholder, create instance + position + resize + remove placeholder
const placeholders = targetSet.children.filter(p => p.type === 'FRAME');
for (const ph of placeholders) {
  const instance = sourceVariant.createInstance();
  targetSet.appendChild(instance);
  instance.x = ph.x;
  instance.y = ph.y;
  instance.resize(ph.width, ph.height);
  ph.remove();
}
```

##### Pattern B: instance → instance swap（学び 34）

既存 instance を別 variant に **in-place で切替**。x/y/size を保持したまま、main component だけが入れ替わる。featured property を有効化するなど、property 値の変更に最適。

```js
// 1) Find existing instance and target variant
const existingInstance = await figma.getNodeByIdAsync(instanceId);
const newVariant = await figma.getNodeByIdAsync(newVariantId); // e.g., featured=true 版

// 2) Single-line swap
existingInstance.swapComponent(newVariant);
existingInstance.name = 'new-descriptive-name'; // optional: rename

// position/size/auto-layout 配置はそのまま保持される
```

**Pattern A vs B の使い分け**:
- placeholder（rect / frame）から始める → **Pattern A**
- 既存 instance を property 値だけ変えたい → **Pattern B**（rebuild 不要、効率的）

##### 寸法 → size 自動推定 heuristic（学び 35）

placeholder の text label に依存せず、**width / height の数値から size を逆算** することで堅牢化:

```js
function sizeKey(w, h) {
  // Each col_w / row_h は spec で確定済の値を使う
  const cols = { 200: 1, 424: 2, 648: 3 }[w] || 2;
  const rows = { 200: 1, 424: 2 }[h] || 1;
  const key = `${cols}x${rows}`;
  // Spec で存在する size のみ accept
  const validSizes = ['1x1', '2x1', '1x2', '2x2', '3x2'];
  if (validSizes.includes(key)) return key;
  // Fallback: 不一致 size は近似マッピング（Issue 11 回避）
  if (key === '3x1') return '2x1';  // resize で 3x1 風に伸ばす
  return '1x1';
}
```

これにより size label が欠落している placeholder（自動配置 etc）や spec ↔ Figma の不整合があっても動作する。

**Phase 3 の注意点（学び 27-29, 34-35）**:
- ⚠ **placeholder 固有属性（stroke / overlay）は instance に転写されない** — 主役識別など状態は **source Component 側の property** として持つべき（Issue 8）
- ⚠ **resize は内部 auto-layout を「ある程度」追従させるが、text wrap までは制御できない** — size 別 overflow 規律を spec で別途定める（Issue 9-10）
- ⚠ **spec にない size の placeholder** に遭遇したら、heuristic fallback or spec 改訂で対応（Issue 11）
- ✅ source Component を後で修正すれば、すべての instance に自動反映される（Marc 流の DRY 原則）
- ✅ swapComponent は同 file 内 variant の切替に最適（位置・サイズ保持）

### Step 4: スクリーンショット検証

#### 撮影単位の選択（学び 4.1）

| シチュエーション | 撮影対象 | 理由 |
|---|---|---|
| 新規生成（Phase 1） | **Component Set 全体** | 全 variants を一覧できる、矩形配置が正しいか即確認 |
| 拡張（Phase 2、state / size 追加） | **Component Set 全体** | 既存 vs 新 variants の差分を比較できる |
| 拡張（Phase 2、新 variant 1 個） | **個別 variant** | 新 variant の詳細確認、Set 全体は最後に |
| 参照確立（Phase 3、instance 化） | **対象 variant** + **個別 instance**（必要時） | layout 全体 → 個別の resize 挙動の順 |

```js
// Set 全体
mcp__figma__get_screenshot({ fileKey, nodeId: set.id, maxDimension: 1800 })
// 個別 variant
mcp__figma__get_screenshot({ fileKey, nodeId: variantId, maxDimension: 1600 })
```

#### Phase 3 専用: resize 前後の auto-layout 挙動検証

Component instance の resize で内部 auto-layout がどう振る舞うかを確認する：
- **拡大方向の resize**: 余白が広がるか / text が中央寄せに戻るか
- **縮小方向の resize**: text が切れる位置 / コンテンツが overflow するか

問題があれば spec md の「size 別 content 規律」を確定させる（Issue 9）。

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

### Issue 8: instance 化で placeholder 固有属性（stroke / overlay）が消失
- placeholder の Drive 2px stroke で主役識別していたが、Tile instance には Drive stroke が含まれない
- **対処（v0.4 候補）**:
  - (A) source Component に **`featured` boolean property** を追加（true で stroke 表示）
  - (B) source Component に **`featured` variant** を追加
- **回避**: Phase 3 着手前に、**「主役識別など状態は source Component 側の property として設計済か」を確認**。未設計なら Phase 2 で先に property 追加

### Issue 9: resize した instance のコンテンツ密度オーバー
- instance を縮小 resize すると text が切れる、auto-layout が wrap して縦に伸びる
- **対処**: spec md の「size 別 content 規律」セクションで、各 size の推奨タイトル文字数 / 本文行数を確定させる
- **回避**: Phase 1 で **代表 size の auto-layout 設計時に「縮小耐性」を意識** — text に `layoutSizingHorizontal: 'FILL'` を必ず適用、固定幅 text は避ける

### Issue 10: auto-layout `primaryAxisAlignItems: 'MAX'` の縦伸び挙動
- Glass variant のテキスト下寄せ（MAX）が、3×2 メガサイズで「主役感を出すには下に偏りすぎ」
- **対処**: variant に **`align` boolean property** を追加（top / bottom）or size 別の layout override
- **回避**: 全 size で同じ `primaryAxisAlignItems` を使い回さない。各 size の見せ方を spec で個別確定

### Issue 11: spec にない size の placeholder（Phase 3 で遭遇）
- Spec の Tile sizes は `1x1 / 2x1 / 1x2 / 2x2 / 3x2` のみだが、Grid 側 placeholder に `3x1`（spec 外）が含まれていた
- **症状**: 寸法 → size 推定で `3x1` が出るが、Tile に対応する Component がない
- **対処（暫定）**: heuristic fallback で `2x1` Tile を採用し、resize で 3 col 幅に伸ばす（auto-layout が縦に伸びる可能性）
- **対処（本質的）**: spec の Tile sizes に `3x1` を追加するか、Grid 側 placeholder を spec 通りの size に修正
- **回避**: Phase 3 着手前に **「Grid placeholder size と Tile size の全件照合」** を行い、不整合があれば spec を先に修正

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

### SKILL 設計
21. **SKILL は frontmatter の `description` が trigger 判定の核**: 自然言語の起動キーワード（"Figma 化", "variant 拡張", "instance に置換" 等）を網羅して記述
22. **SKILL は git 管理対象に**: `.claude/skills/<name>/SKILL.md` を **プロジェクトリポジトリ内に置いてコミット** すれば worktree が消えても残り、PR レビュー対象になり、チーム共有できる

### 拡張パターン（Phase 2）
23. **既存 Set への variant 追加は `set.appendChild(newVariant)`**: 新規 Set 作成より少ない手数、property definitions も自動拡張される
24. **既存 Set への variants 追加時の x/y 配置規則**: 既存 variants の縦並び（または横並び）パターンを inspect で確認してから、その規則を踏襲する。例: Hero は y = 0 / 800 / 1600 の 100px gap → 新 variant も y=2200 に配置
25. **`variantOptions` の順序は追加順**: 既存 から clone & rename した場合、Figma 側の `variantOptions` 配列は追加順になり、spec の表記順と一致しない場合がある。UI 表示の視認性のみ問題、機能影響なし
26. **2D Property の grid 配置パターン**: variants × sizes のような 2 property を全展開する場合、**列 = property1 / 行 = property2** の matrix 配置がレビューしやすい。`x = cIdx * COL_W, y = rIdx * ROW_H` で計算

### 参照確立（Phase 3）
27. **`createInstance()` + `resize(W, H)` で双方向参照確立**: 別 Component の placeholder を本 Component の instance に置換することで、「Component 単体修正が demo に自動反映」される DRY 設計
28. **placeholder 固有属性（stroke / overlay）は instance に転写されない**: 主役識別など状態は **source Component 側の property** として持つべき（Phase 3 着手前に必ず確認）
29. **resize と auto-layout の関係**: container 縦間隔は維持されるが、text wrap までは制御できない。size 別 overflow 規律を spec で別途定める必要がある

### Boolean 的 property / stroke 上書き
32. **boolean 的 variant property は `'true'`/`'false'` 文字列で実装**: Figma の variant property 型は VARIANT（文字列）のみで真の Boolean なし。`featured = ['false', 'true']` のような variant option で運用すれば UI でトグル風に表示される
33. **既存 strokes 上書き時は `individualStrokeWeights` もリセット**: 一部 variant に `strokeRightWeight = 2` 等が残っていると新 stroke 適用後も古い individual 値が残る。**4 辺の `Top/Right/Bottom/LeftWeight` を明示**して完全均一化

### Phase 3 拡張パターン（v0.4 追加）
34. **`swapComponent` は Phase 3 の第 2 パターン**: 既存 instance を別 variant に in-place 切替。`createInstance + delete + new` ではなく **swap で 1 行**、x/y/size/auto-layout 配置を全て保持する。featured 切替などの property 値変更に最適
35. **寸法 → size key 自動推定 heuristic**: placeholder の text label に依存せず、width/height から逆算する `sizeKey(w, h)` 関数で堅牢化。spec ↔ Figma の data 整合性が完璧でなくても動作。fallback で不一致 size を近似 mapping することで Issue 11 を回避

---

## チェックリスト（コミット前）

### Phase 1 (新規生成)
- [ ] Step 0 Audit-first を実行した（既存 Component Set 一覧を確認した）
- [ ] spec md を完全読み込み、Variants / Sizes / Props / Do-Don't を把握した
- [ ] 使う Variables / Effect Styles の ID を取得した
- [ ] Variable 健全性（alias 純白固定化なし）を確認した
- [ ] Set 全体スクリーンショットで全 variants を視覚確認した

### Phase 2 (variant property 拡張)
- [ ] 既存 variants の x/y 配置規則を inspect で確認した
- [ ] 1D 拡張なら縦/横並び規則を踏襲、2D 拡張なら matrix 配置を採用した
- [ ] clone 後 `primaryAxisSizingMode = 'FIXED'` を明示した（Issue 5 回避）
- [ ] Set 全体を再 resize して新 variants が収まることを確認した

### Phase 3 (Component 間参照)
- [ ] **Pattern 選択を明確化**: placeholder → instance なら **Pattern A**、既存 instance の property 値変更なら **Pattern B (swapComponent)**
- [ ] source Component 側に「主役識別など状態」property が設計済か確認した（Issue 8）
- [ ] **Pattern A**: placeholder の x/y/size を捕捉 → instance を createInstance → 配置 → resize → placeholder remove の順で操作した
- [ ] **Pattern B**: 既存 instance の id を取得 → 切替先 variant の id を取得 → `existingInstance.swapComponent(newVariant)` で 1 行 swap
- [ ] **寸法 → size key 自動推定** を用意した（text label 欠落でも動作させる、学び 35）
- [ ] **Grid placeholder size と source Component の size 整合性を事前照合**（Issue 11 回避）
- [ ] resize 前後の text wrap / overflow を screenshot で検証した（Issue 9-10）

### 共通（コミット前）
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
