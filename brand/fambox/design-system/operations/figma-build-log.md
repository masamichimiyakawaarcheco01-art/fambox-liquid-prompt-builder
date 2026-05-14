---
title: FAMBOX Design System — Figma Build Log
type: operations
last_updated: 2026-05-12
purpose: Markdown仕様→Figma Component の自動生成履歴。スキル「figma-component-from-spec」で実施した各セッションの記録。
---

# Figma Build Log

`figma-component-from-spec` スキル経由で行った Markdown → Figma 自動生成の履歴。
発生した問題・修復内容も記録（再発防止のナレッジ蓄積）。

---

## Session 2026-05-12 — L2 Primitives 一括構築

**契機**: Marc-Antoine（外部デザイナー）の Smart City Kit 制作プロセスを学習。
Marc流4層スタック（L1 Transport / L2 Skill / L3 Tokens / L4 CLAUDE.md / L5 Audit-first）を
FAMBOX に翻訳・適用した最初のセッション。

### 成果

| Component | Variants | Component Set ID | Page | Notes |
|---|---|---|---|---|
| Button | 15 (5 variant × 3 size) | `46:32` | 3. Primitives | default state only。hover/disabled/loading/icon は v0.3 で追加 |
| Input | 12 (3 variant × 4 state) | `50:26` | 3. Primitives | underline / bordered / textarea × default/focus/disabled/error |
| Avatar | 20 (2 type × 2 state × 5 size) | `53:32` | 3. Primitives | fallback("F") / photo(gray placeholder) × default/featured × xs..xl |
| Form Controls | 9 (3 kind × 3 state) | `54:16` | 3. Primitives | checkbox / radio / toggle × default/checked-or-on/disabled |
| Progress Bar | 5 (5 value) | `55:11` | 3. Primitives | value=0/25/50/75/100 |
| Spinner | 3 (3 size) | `55:21` | 3. Primitives | sm/md/lg。arcData による 75% 円弧 |

**合計**: 64 variants、推定 280+ Variable バインド、約 60 分。

### 発生問題と修復

#### 🐛 Issue 1: alias Variables 12 個が純白に固まっていた（最大発見）
- **症状**: Button Link variant のテキスト色が drive オレンジにならず白に
- **原因**: Tokens Studio から `{color.brand.drive}` 等の alias 参照が import 時に解決失敗、
  全 alias 系 Variables が静的 `{r:1, g:1, b:1, a:1}` に固定化
- **影響範囲**: `cta` / `focus-ring` / `link-on-light` / `link-on-dark` / `link-on-drive` /
  `link-hover` / `data/primary` / `data/secondary` / `data/tertiary` /
  `data/zone-good` / `data/zone-caution` / `data/zone-danger`
- **修復**: `setValueForMode` で正しい VARIABLE_ALIAS に再接続（12 件）
- **再発防止**: `figma-component-from-spec` SKILL の Step 1 に alias 健全化スクリプトを必須化

#### 🐛 Issue 2: Textarea の placeholder テキストが縦書きで wrap
- **症状**: 1 文字ずつ縦に並んで描画
- **原因**: `figma.createText()` の初期 width が極小、`textAutoResize='HEIGHT'` で固定された
- **修復**: `appendChild` 後に `resize(innerWidth, height) → textAutoResize='HEIGHT' →
  layoutSizingHorizontal='FILL'` の順で再設定
- **再発防止**: 多行テキストは作成順序が重要、SKILL ドキュメントに明記

### Known TODOs

- **Button v0.3**: hover / disabled / loading state + Icon variants（with-icon / icon-only）
- **Input v0.3**: hover / active state、必須バッジ表示
- **Avatar v0.3**: focus ring（WCAG 2.1 AA）、写真フィル実装
- **Form Controls v0.3**: focus / hover state、Toggle 影の量感調整
- **Progress Circular**: arc 描画（vectorPath による SVG path）— Circular Progress 全体が未着手
- **Spinner v0.3**: 円弧の見た目を CSS 仕様に近づける（pie ではなく純粋な arc curve）

### 使用した Variables（主要）

```
FAMBOX/color/brand/drive          (Primary CTA)
FAMBOX/color/brand/deep           (Avatar fallback bg)
FAMBOX/color/ink/ink              (本文)
FAMBOX/color/ink/white            (反転テキスト)
FAMBOX/color/ink/placeholder      (Disabled / Empty)
FAMBOX/color/bg/primary           (Input bg)
FAMBOX/color/bg/tertiary          (Disabled bg / Photo placeholder)
FAMBOX/color/border/base          (Input default border)
FAMBOX/color/border/light         (Disabled border)
FAMBOX/color/semantic/error       (Input error border)
FAMBOX/color/alias/link-on-light  (Link text — 修復後)
FAMBOX/radius/sm                  (Checkbox 4px)
FAMBOX/radius/md                  (Input bordered 8px)
FAMBOX/radius/pill                (Avatar / Toggle / Spinner)
FAMBOX/radius/pill-cta            (Button)
FAMBOX/border-width/thin          (Input 1px)
FAMBOX/border-width/thick         (Button outline / Featured Avatar 2px)
FAMBOX/typography/font-size/body-sm   (Button sm 14px)
FAMBOX/typography/font-size/body      (Button md / Input 16px)
FAMBOX/typography/font-size/lg        (Button lg 20px)
```

### 学んだこと

1. **Audit-first protocol は実効性が高い**: Step 0 で既存資産を確認することで重複生成と
   隠れバグ（alias 破損）を早期発見。Marc流ノウハウの即時実証。

2. **テキスト描画は順序依存が大きい**: `loadFontAsync → createText → characters →
   appendChild → layoutSizing` の順序を守らないと描画ミスする。

3. **MVP→拡張 が正解**: 状態×サイズ×バリアントを 30 超で一気に作るより、
   default state のみで先に variant 構造を確立してから state を追加するほうが
   失敗コストが低い。

4. **Hiragino Sans は Figma に無い**: `Noto Sans JP` で代替。CSS と完全一致は
   できないが、visual fidelity は実用範囲。

---

## 次回セッション着手候補

優先順:
1. ✅ **Button v0.3 第1弾（state property 追加）**: 2026-05-12 完了 — 下記 Session 参照
2. **Button v0.3 第2弾（icon variants）**: `with-icon` property（leading / trailing / icon-only）追加
3. **Spinner v0.3**: dashed ring を vectorPath ベースの arc curve に置換
4. **L3/L4 Components の Figma 化**: Card / Hero / Header / Footer / FAQ / Profile / Bento の順
5. **L2 Primitives の所在ページ整合**: 現在 `0. Cover` にあるが Build Log 表記は `3. Primitives` — 全 L2 を 3. Primitives へ移動

---

## Session 2026-05-12 (#2) — Button v0.3 state property 拡張

**契機**: Build Log v0.1 で次回着手候補 #1 として明示されていた「Button v0.3 — hover/disabled/loading state」を実行。Marc 流 incremental（小さく作って大きく展開）に従い、icon variants は v0.4 へ送り state のみに集中。

### 成果

| Component | Property 追加 | Variants 追加 | 合計 | Component Set ID |
|---|---|---|---|---|
| Button | `state` (default / hover / disabled / loading) | +45（hover 15 / disabled 15 / loading 15）| **60**（旧 15 → 60）| `46:32`（変わらず）|

**配置**: state ごとに横方向ブロック（`x` offset: default=0 / hover=700 / disabled=1400 / loading=2100、各ブロック 626 幅）
**Component Set 全体**: width 626 → **2726**、height 430 のまま

### 各 state の Variable バインド

| state | bg | text | stroke | 特記 |
|---|---|---|---|---|
| default | 既存維持 | 既存維持 | 既存維持 | rename のみ（`state=default` を name に追加） |
| hover | primary → `drive-light` / secondary-ink → `ink` 反転 / secondary-drive → `drive` 反転 / ghost → `rgba(27,29,26,0.06)` 直値 | secondary 反転時は `white` / link は `link-hover`（→ alias drive-light） | 既存維持 | link は `textDecoration: 'UNDERLINE'` |
| disabled | 全 variant → `border/base` | 全 variant → `ink/caption` | **除去** | spec 整合（背景強制） |
| loading | 既存維持（default の見た目を維持）| **opacity 0** で透明化 | 既存維持 | 中央に variant 色の dashed ring（sm14 / md16 / lg20）を絶対配置 |

### 発生問題と修復

#### 🐛 Issue 3: link variant の `textDecoration` 設定で「Poppins Medium 未ロード」エラー
- **症状**: hover variants ループ中、link variants の `tn.textDecoration = 'UNDERLINE'` で
  `Cannot write to node with unloaded font "Poppins Medium"`
- **原因**: 事前ロードしたのは `Inter Semi Bold` / `Inter Medium` のみ。link variants は実際には Poppins Medium で組まれていた
- **影響範囲**: link hover 3 variants（sm/md/lg）— underline 未適用で clone 自体は作成済
- **修復**: `figma.listAvailableFontsAsync()` で Poppins の正式 style 名（`Medium` / `SemiBold`）を確認後、対象 text node の `fontName` を読み取り `loadFontAsync(tn.fontName)` で動的ロード、その後 underline と link-hover binding を後追い適用
- **再発防止**: state cloning では「テキスト node の実フォントを node ごとに動的ロード」をパターン化（事前に全フォント列挙してロードするより堅実）

#### 🐛 Issue 4: clone 直後の variants が default と同位置に重なる
- **症状**: hover variants 生成直後、screenshot に 15 個分しか映らない（実際は重なって 30 個ある）
- **原因**: Component Set が `layoutMode: 'NONE'`（auto-layout なし）。clone は親と同座標で生成され、手動で再配置が必要
- **修復**: state ごとに x オフセット（default=0 / hover=700 / disabled=1400 / loading=2100）を割り振り、`set.resize(blockEnd, height)` で Set 自体を拡幅
- **再発防止**: Component Set 構築時は **layoutMode を `'HORIZONTAL'` または `'VERTICAL'` で auto-layout 化することを v0.4 で検討**（手動 x 計算は state 数が増えると壊れやすい）

### Known TODOs（v0.3 残）

- **Button with-icon**: leading / trailing / icon-only variants（INSTANCE_SWAP property で実装、variants 増やさない方針も検討）
- **Spinner v0.3**: 現状の dashed ring を vectorPath で正確な arc curve に置換し、Button loading も同 Spinner Component の instance に差し替え
- **Secondary-ink disabled のコントラスト改善**: 現状 `caption (#888) on border-base (#d0d0d0)` は約 2:1 で WCAG NG。Spec 改訂で disabled text を `--color-sub` (#545655) へ昇格する案を検討

### 学んだこと（追加）

5. **`layoutMode: 'NONE'` の Component Set は state 拡張に向かない**: 新 variants が同座標で重なる。
   今後は **Component Set を auto-layout 化**してから state を追加するのが安全。

6. **Variable bind には `setBoundVariableForPaint` の戻り値の paint で配列を再構築する**: 既存 paint をin-place 改変ではなく
   新 paint オブジェクトを作って `[newPaint]` を fills に代入する方が安定（既存 fills が空配列のときの NPE を回避）。

7. **「Spec の `:disabled` 一律適用」は Figma で stroke 除去が必要**: CSS の `.btn:disabled` は背景上書きするので
   border は視覚的に隠れるが、Figma variant では明示的に `strokes = []` しないと border が残る。

---

## Session 2026-05-12 (#3) — Card Pattern v0.2 Audit-first 補完

**契機**: 「L3 Card Pattern Figma 化」を新規生成で着手しようとしたところ、Audit ステップで Component Set `57:35` が `4. Patterns` ページに**既存**していることを発見。Marc 流 Audit-first protocol が再び有効に作用し、重複生成を回避。

### 成果

| Component | 状態 | Variants | Component Set ID | 操作内容 |
|---|---|---|---|---|
| Card | 既存資産の audit + 唯一の gap を補完 | 4（standard / featured / horizontal / flat） | `57:35`（既存）| **shadow `FAMBOX/shadow/1` を 3 variants に適用**（flat 除く） |

### Audit-first で確認した既存実装

| Variant | bg | stroke | shadow（適用前） | 寸法 |
|---|---|---|---|---|
| standard | `bg/primary` ✅ | `border/light` 1px ✅ | **なし → shadow/1 適用** | 320 × 383 |
| featured | `bg/primary` ✅ | `color/brand/drive` 2px ✅ | **なし → shadow/1 適用** | 320 × 312 |
| horizontal | `bg/primary` ✅ | `border/light` 1px ✅ | **なし → shadow/1 適用** | 480 × 174 |
| flat | `bg/secondary` ✅ | なし（spec 通り）✅ | なし（spec 通り）✅ | 280 × 176 |

各 variant は Button (`46:32`) Component instance を埋め込み済。Featured は「おすすめ」バッジ用の Frame を内包。

### 学んだこと（追加）

8. **Audit-first protocol は L3 でも有効**: 既存 Card Component Set を発見できたことで「重複生成 → 後で 2 つの Card を統合」という最悪フローを回避。**Figma で何かを作る前に必ず `findAll(name match)` で既存確認** することをルール化。

9. **Effect Style の適用は `setEffectStyleIdAsync` が必須**: 同期 setter (`v.effectStyleId = id`) ではなく async 版を使う（モダン Figma API の規約）。

### Known TODOs（Card v0.3 残）

- **state property 追加**: hover / focus-visible / active / disabled / selected（5 states × 4 variants = +20 variants）
- **stroke weight Variable バインド**: 現状直値 1 / 2 → `border-width/thin` / `border-width/thick` に置換
- **Flat の Button instance を `variant=link` に切り替え**: Spec では Flat は Link CTA だが、現状 Primary Button instance が入っている

---

## Session 2026-05-12 (#4) — L2–L4 全 Component Set 一括 Audit

**契機**: L4 Hero Figma 化に着手しようとしたところ、Card で発見した「既存資産の見落とし」が他にもある可能性を懸念。Marc 流 Audit-first を **15 Component Set 全件に拡張**して spec ↔ Figma の整合マトリクスを作成。

### 成果: Figma 上に存在する 15 Component Sets

| Layer | Component | Set ID | Page | Variants | Property | 状態 |
|---|---|---|---|---|---|---|
| L2 | Avatar | `53:32` | 3. Primitives | 20 | type × state × size | ✅ |
| L2 | Button | `46:32` | 3. Primitives | 60 | variant × size × state | ✅ v0.3 |
| L2 | Form Controls | `54:16` | 3. Primitives | 9 | kind × state | ✅ |
| L2 | Input | `50:26` | 3. Primitives | 12 | variant × state | ✅ |
| L2 | Progress Bar | `55:11` | 3. Primitives | 5 | value | ✅ |
| L2 | Spinner | `55:21` | 3. Primitives | 3 | size | △ arc curve 化 v0.4 |
| L3 | Card | `57:35` | 4. Patterns | 4 | variant | ✅ shadow 補完済 |
| L3 | FormField | `56:34` | 4. Patterns | 4 | state | ⚠ spec md 未整合確認 |
| L3 | Stat Card | `64:49` | 4. Patterns | 6 | size × layout | ⚠ spec md 整合確認要 |
| L4 | Case Study | `66:91` | 5. Components | 2 | variant: tile/story | ✅ |
| L4 | Footer | `60:95` | 5. Components | 3 | variant: standard/minimal/sitemap | ✅ |
| L4 | Header | `59:33` | 5. Components | 3 | variant: standard/minimal/mega | ✅ |
| L4 | Hero Section | `67:73` | 5. Components | **3** | variant: video-fullscreen/image-editorial/minimal-text | ⚠ spec 4 variant × 3 heights = 12 を期待、現状 3 のみ |
| L4 | Modal | `62:33` | 5. Components | 3 | variant: confirmation/detail/sheet | ✅ |
| L4 | Subscription Plan Card | `65:110` | 5. Components | 2 | variant: standard/featured | ✅ |

### Figma 未実装の Spec md

| Component | spec md | 期限 / 優先度 | 用途 |
|---|---|---|---|
| Bento Tile (L3) | bento-tile.md | TOP 実装 5/29 主役 | Bento Grid の構成要素・5 size |
| Bento Grid (L4) | bento-grid.md | TOP 実装 5/29 主役 | TOP 主要セクション・12 col |
| FAQ (L4) | faq.md ← NEW | 既 Spec 化 | TOP 末尾 / 横スクロール Carousel |
| Profile (L4) | profile.md ← NEW | 既 Spec 化 | TOP 監修者紹介 / Drive 全面塗り Section |
| Contact Form (L4) | contact-form.md | OKR Task 2-1 中核 | 問合せフォーム |

### 検出されたギャップ

#### 🐛 Gap A: Button 所在ページの誤認
- 直前 Session (#2) で Button の Page を `0. Cover` と表記したが、**実際は `3. Primitives`**
- 原因: `getNodeByIdAsync` は document-wide 検索で、`setCurrentPageAsync` でループしていても**最初のページで一致判定**されてしまった
- 修復: button.md の Page 表記を `3. Primitives ...` に訂正
- 再発防止: 親ページ判定は **`node.parent`（場合により `parent.parent`）を辿って `type === 'PAGE'` まで遡る** のが正解

#### 🐛 Gap B: Hero Section variants 数の spec 不一致
- spec: 4 variant × 3 heights = 12 variants 想定
- Figma 実態: 3 variants（heights プロパティなし、各 variant 単一 height）
- 判断: 即修正せず、Hero 個別の audit で「heights を別 property として追加するか」を検討（v0.3 候補）

#### 🐛 Gap C: spec md 側の Figma 参照欠落（8 件）
- 以下の md に **Figma 参照セクション未記載**:
  case-study / contact-form / faq / footer / form-field / header / hero-section / modal / profile / stat-card / subscription-plan-card
- 影響: 「spec → Figma → 実装」の双方向追跡が切れている
- 修復: 本セッション末尾で 8 件（Figma 実装ある分）に最小 Figma 参照を追加。Figma 未実装の 5 件（bento-tile/bento-grid/faq/profile/contact-form）は別途実装と併せて追加

### 学んだこと（追加）

10. **「Audit-first は新規生成前に必ず実行」を体制化**: L3 で 1 件発見 → L2-L4 全件 audit で 15 件マッピングが完成 + 3 つのギャップ検出。30 分の investigation で重複生成と所在誤認を一掃。

11. **Page 判定は node.parent を辿る**: `getNodeByIdAsync` は document-wide で、ループ内で `setCurrentPageAsync` してから取得すると最初の page で「見つけた」ことになり判定が壊れる。**`while (node.parent && node.parent.type !== 'PAGE') node = node.parent` で親ページに到達** する形式が安全。

### 次セッション着手候補（更新版）

優先度高い順:
1. ✅ **Bento Tile + Bento Grid Figma 新規生成**: 2026-05-12 完了（下記 Session #5 参照）
2. **Hero Section variants 拡充**: 4 variant × 3 heights = 12 への拡張（または heights を別 property 化）
3. **FAQ Carousel Figma 新規生成**: spec 化済、preview-faq.html を参照に
4. **Profile Section Figma 新規生成**: spec 化済、Drive 全面塗り Section
5. **L3 FormField / Stat Card の spec ↔ Figma 整合確認**: spec md と Figma 実態の差分洗い出し
6. **Contact Form Figma 生成 + spec md 補強**
7. **Spinner v0.3** / **Button v0.4 with-icon**
8. **Bento Tile 残 4 sizes 追加**: 1×1 / 2×1 / 1×2 / 3×2（計 20 variants 完備）
9. **Bento Grid 内の placeholder を Bento Tile instance に置換**

---

## Session 2026-05-12 (#5) — L3 Bento Tile + L4 Bento Grid Figma 新規生成

**契機**: Audit #4 で「Figma 未実装の Spec md 5 件」のうち最優先（TOP 実装 5/29 期限の主役エリア）として、Bento Tile + Bento Grid を一体生成。Marc 流 incremental に従い、**まず代表 size のみで型を作り、残 sizes は次セッション** とした。

### 成果

| Component | Set ID | Page | Variants | Phase 1 範囲 |
|---|---|---|---|---|
| Bento Tile (L3) | `87:26` | 4. Patterns | 4 | 各 variant × default size 2×2（360×360）|
| Bento Grid (L4) | `91:107` | 5. Components | 3 | placeholder rect で grid layout demo |

### Bento Tile 詳細

各 variant の Variable bind と構造:
- **standard**: `bg/primary` + `border/light` 1px + `shadow/1` + Eyebrow（Drive `CASE`）+ Title（Bold 24）+ Body（Regular 16）
- **glass**: dark base 直値 + 半透明 overlay rect（opacity 0.3 黒、Spec の Glass 3 既定）+ 下寄せ白文字
- **image-fill**: 画像 placeholder（dark blue-gray）+ bottom gradient overlay（透明→黒 0.7、Liner Gradient）+ 下寄せ白文字
- **stat-focus**: `bg/primary` + `border/light` + `shadow/1` + 大型数字 `-3.2 kg`（56px Drive Bold / `kg` 部分 22px sub）+ ラベル 16px sub

### Bento Grid 詳細（placeholder demo）

各 variant 内に **rect placeholder** を grid 風に配置（後で Bento Tile instance に差替予定）:
- **Standard** 936×520: 自由配置 5 tiles（2×1 / 1×1×2 / 1×1 / 3×1）
- **Editorial** 1160×968: **対角線パターン A** 9 tiles（2×2 主役 右上 + 3×2 主役 左下 + 1×1×4 + 2×1×2）— 主役タイルは Drive 2px stroke で識別
- **Autofit** 936×520: KPI ギャラリー 8 tiles（1×1 均等）

### 発生問題と修復

#### 🐛 Issue 5: Component の resize 後に子要素追加で AUTO sizing が再計算される
- **症状**: `resize(360, 360)` 直後は 360×360 だが、子テキスト要素を appendChild すると `primaryAxisSizingMode: 'AUTO'` で高さが HUG（コンテンツ依存）に縮む
- **影響**: Bento Tile 4 variants が当初 86-186px 高さ（期待 360px から大幅縮退）
- **修復**: 各 variant の `primaryAxisSizingMode = 'FIXED'` を明示設定後、再度 `resize(360, 360)` を実行
- **再発防止**: Auto-layout component を固定サイズで作るときは、子要素 append 前に `resize` → 子追加 → **`primaryAxisSizingMode = 'FIXED'` 確認 → 必要なら再 resize** の順序を守る。Gotcha 12（layoutSizing は parent.appendChild 後）と関連する罠

### 学んだこと（追加）

12. **Component Set 高さは variants の最終 height に追従しない場合がある**: 内部 variants の高さを変えても Set の bounding box が更新されないことがある。**`set.resize(setW, expectedH)` で明示的に拡張** が確実。

13. **Figma Plugin API でグラデーション overlay**: Linear Gradient は `gradientTransform`（2D アフィン行列）+ `gradientStops` で指定。`[[0,1,0],[-1,0,1]]` で「上 → 下」方向のグラデを実現。

14. **`setRangeFontSize` / `setRangeFills` で複合スタイル**: `-3.2 kg` のように単語内で size / color を変えるときに有効。Spec の「kg 部分 22px sub」など細部要件に対応可能。

### Known TODOs（Bento v0.3 残）

- **Bento Tile 残 4 sizes**: 1×1 / 2×1 / 1×2 / 3×2 → 計 20 variants 完備
- **Bento Tile state property**: hover（shadow-3 + translateY -2px）/ focus-visible / disabled
- **Bento Tile Glass の 5 階調 modifier**: glass--1 ～ --5（opacity 0.05 / 0.1 / 0.3 / 0.6 / 0.8）
- **Bento Grid 内の placeholder を Bento Tile instance に置換**
- **Tablet / SP responsive variants**: 6 col / 1 col 縦並び

---

## Session 2026-05-12 (#6) — L4 FAQ Carousel + L4 Profile Section Figma 新規生成

**契機**: 直前に Spec 化した 2 件（faq.md / profile.md）を Figma 化することで「spec → Figma」の往復サイクルを締める。Audit #4 で残っていた Figma 未実装 3 件のうち 2 件を本セッションで消化。

### 成果

| Component | Set ID | Page | Variants | サイズ |
|---|---|---|---|---|
| FAQ (L4) | `93:90` | 5. Components | 1（`variant`: carousel）| 1440 × 560 |
| Profile (L4) | `96:79` | 5. Components | 1（`variant`: section）| 1440 × 760 |

### FAQ Carousel 詳細

- Section bg: `bg/secondary` (#FAFAFA)、padding 64×4辺
- Title: 「よくあるご質問」Noto Sans JP Bold 32 Ink + margin-bottom 56
- Scroll track: HORIZONTAL / gap 32 / 4 cards
- 各 card 320 wide / auto height / itemSpacing 24:
  - Avatar 40×40 円（`bg/tertiary`）
  - Question N（Poppins SemiBold 24 Ink）
  - 質問文（Bold 18 Ink、170%）
  - 黒線 32×2（`ink/ink`）← FAMBOX Editorial キャラクターライン
  - 回答文（Regular 18 **Drive**、170%）
  - FAMBOX logo placeholder（80×32）

### Profile Section 詳細

- Section bg: `color/brand/drive` (#FB4C15) 全面、padding 64×4辺
- Title box: 1312 × 72 / 2px `drive-light` 枠
  - Icon box 72×72: **右側のみ 2px drive-light 罫線**（`individualStrokeWeights.right = 2`）
  - Icon glyph: 40×40 drive-light 半透明 placeholder
  - "Profile" Poppins Regular 32 white
- Profile list: HORIZONTAL / gap 64 / 2 boxes
- 各 Profile box 624 × 517 / `layoutMode: 'NONE'` / `clipsContent: true`:
  - dark bg placeholder
  - content w284: Name 40 / 肩書 14 / spacer 24 / line 284×2 drive-light / spacer 24 / Bio 14（全 white）

### 発生問題と修復

#### 🐛 Issue 6: `layoutPositioning = 'ABSOLUTE'` は親が auto-layout の時のみ可
- **症状**: Profile box の `layoutMode: 'NONE'` 内で `content.layoutPositioning = 'ABSOLUTE'` が
  `Can only set layoutPositioning = ABSOLUTE if the parent node has layoutMode !== NONE` で失敗
- **原因**: layoutPositioning は auto-layout の **子要素の例外配置**指定 API。NONE の場合は元から x/y で自由配置できるため不要・かつ不正
- **修復**: `layoutPositioning` 行を削除し、`content.x = 0; content.y = 0` で直接配置
- **再発防止**: parent の `layoutMode` を判定して、NONE の場合は `layoutPositioning` を**設定しない**。素直に `x/y` だけ使う

### 学んだこと（追加）

15. **`individualStrokeWeights` で部分ボーダー**: Figma の単一 frame で「右だけ 2px 線」を引くには `strokeTopWeight = 0` / `strokeBottomWeight = 0` / `strokeLeftWeight = 0` / `strokeRightWeight = 2` を組み合わせる。CSS の `border-right` 相当を Plugin API で再現する正式手段。

16. **auto-layout の itemSpacing は均一前提**: 「avatar→Q番号 16 / Q番号→質問文 24 / 質問文→線 24 / 線→回答文 24 / 回答文→logo 32」のように要素間で異なる margin を持たせる場合、**spacer frame を挟む** か **個別 padding** で表現する必要がある。今回 Profile は spacer 24px frame で line 上下 32px margin を実現。

17. **`combineAsVariants` は単一 variant でも有効**: 将来 variant 追加余地のある Component は最初から Component Set でラップする方が、後で property 追加しやすい（FAQ / Profile はそれぞれ Carousel / Section の 1 variant だけだが Set 化）。

### Known TODOs（FAQ / Profile v0.3 残）

- **FAQ Accordion variant**: `/pages/faq` 長文 FAQ 専用
- **FAQ SP layout**: card 幅 `calc(100vw - 80px)` + scroll-snap
- **Profile Card variant**: About ページ・メンバー一覧用
- **Profile 背景画像 Image Fill バインド**: 現状 dark placeholder
- **Profile SP layout**: テキスト下に画像 180px 配置の縦積み
- **Profile WCAG 改善**: bio 14px white on drive を 16px へ昇格 spec 改訂

---

## Session 2026-05-12 (#7) — L4 Contact Form Figma 新規生成（最後の Figma 未実装 spec を消化）

**契機**: Audit #4 で残っていた Figma 未実装 1 件（Contact Form）を消化することで「**Spec md ↔ Figma の完全カバー**」を達成し、Marc 流 4 層スタックの 1 サイクルが完結する。

### 成果

| Component | Set ID | Page | Variants | サイズ |
|---|---|---|---|---|
| Contact Form (L4) | `98:121` | 5. Components | 1（`variant`: input）| 768 × 1200 |

**🏆 マイルストーン**: Figma 未実装 Spec md **1 件 → 0 件** に減少。Marc 流 4 層スタック（Spec → Figma → Build Log → Audit）の **完全カバー** 達成。

### Contact Form 詳細（Phase 1 = 入力フェーズ）

- Section bg: `bg/secondary` (#FAFAFA)、padding 64×4辺
- Title 「お問い合わせ」Bold 32 Ink + サブタイトル 16 sub
- Fields container (gap 24) — 代表 7 フィールド（spec 11 のうち主要型を網羅）:
  - **text** × 2（会社名・お名前）
  - **select** × 1（役職、`▾` 右寄せ）
  - **email** × 1（メール）
  - **radio** × 1（問合せ種別 4 options）
  - **textarea** × 1（500 字カウンタ付き）
  - **checkbox** × 1（プライバシーポリシー同意）
- 各 Label に **必須 badge**（Drive bg + white「必須」10px）
- Submit Button: Button (`46:32`) instance `variant=primary, size=lg, state=default`、テキスト「内容を確認する」

### 発生問題と修復

#### 🐛 Issue 7: `parent.removeChild(child)` は Figma Plugin API に存在しない
- **症状**: `wrapper.removeChild(labelRow)` で `TypeError: no such property 'removeChild' on FRAME node`
- **原因**: Figma Plugin API のノード削除は **`child.remove()`** が正解。DOM API の `removeChild` 慣性で書いてしまった
- **修復**: checkbox 分岐では最初から label row を作らないように分岐前置（より良いアプローチ）
- **再発防止**: ノード削除のときは常に `child.remove()`、parent からの除去 API は存在しない

### 学んだこと（追加）

18. **既存 Component の instance 化は `child.createInstance()`**: Button (46:32) の特定 variant を埋め込むには、Component Set の children から target variant Component を見つけて `.createInstance()` を呼ぶ。これで親 Form に instance を append すれば、Button の変更が Contact Form の Submit にも反映される（双方向）。

19. **必須 badge は label row 内の補助 frame で**: HORIZONTAL auto-layout の label row に「ラベル + badge」を gap 8 で配置することで、CSS の inline-flex 相当を実現。

20. **Phase 1 で型を作り Phase 2 で拡張する Marc 流の真価**: Contact Form 11 フィールド全部を一発で作らず、各フィールド型（text/select/email/radio/textarea/checkbox）の代表だけ作ったことで、`buildFormField` 関数が再利用可能なパターンライブラリとして残った。残 4 フィールドの追加は **既存関数に定義だけ追加** で済む。

### Known TODOs（Contact Form v0.3 残）

- **残 4 フィールド追加**: 競技・種目 / 電話番号 / 選手数・チーム規模 / 利用検討時期（任意）
- **`variant=review`**: 確認フェーズ inline 表示（readonly + 修正/送信 2 ボタン）
- **`variant=success`**: Success 画面（TOPに戻る + 事例を見る）
- **error state variants**: 各フィールドの error 表示（FormField `56:34` の state=error を継承）
- **SP layout**: Form 全幅 + button 全幅

---

## 🎯 マイルストーン到達: Marc 流 4 層スタック完全カバー

2026-05-12 の 7 セッションで、FAMBOX Design System の **Spec md ↔ Figma Component Set ↔ Build Log** の完全な往復サイクルを確立した。

### 最終マトリクス（2026-05-12 時点）

| Layer | Spec md | Figma Set | 状態 |
|---|---|---|---|
| L1 Tokens | colors / typography / spacing / motion 等 | Variables / Effect Styles | ✅ |
| L2 Primitives | 6 件 | 6 件（Button 60v / Input 12v / Avatar 20v / Form Controls 9v / Progress 5v / Spinner 3v）| ✅ |
| L3 Patterns | 3 件 | 3 件（Card 4v / FormField 4v / Stat Card 6v / Bento Tile 4v Phase1）| ✅ |
| L4 Components | 9 件 | 9 件（Header 3v / Footer 3v / Modal 3v / Hero 3v / Case Study 2v / Plan Card 2v / Bento Grid 3v / FAQ 1v / Profile 1v / Contact Form 1v）| ✅ |

### Marc 流 7 セッションで蓄積した学び（計 20 項）

| Session | 内容 | 学び |
|---|---|---|
| #1 (前期) | L2 Primitives 64 variants 構築 | 1-4: alias 健全化 / テキスト順序 / MVP→拡張 / Hiragino 代替 |
| #2 | Button v0.3 state property 拡張 | 5-7: auto-layout / paint 再構築 / stroke 明示除去 |
| #3 | Card audit + shadow 補完 | 8-9: Audit-first L3 適用 / setEffectStyleIdAsync 必須 |
| #4 | 全 Component Set 一括 Audit | 10-11: 重複生成回避 / node.parent で安全な page 判定 |
| #5 | Bento Tile + Grid 新規生成 | 12-14: resize 後 sizing 罠 / Gradient 行列 / Range スタイル |
| #6 | FAQ + Profile 新規生成 | 15-17: individualStrokeWeights / spacer frame / 1variant でも Set 化 |
| #7 | Contact Form 新規生成 | 18-20: `createInstance()` / 必須 badge label row / Phase 1 で型作り→Phase 2 で拡張 |

これらを **figma-component-from-spec SKILL v0.2** として整備するのが次の本質的な打点。

---

## Session 2026-05-12 (#8) — figma-component-from-spec SKILL v0.2 整備

**契機**: 7 セッションで蓄積した 20 項の学び + 7 つの実 Issue を、**再利用可能なナレッジ資産** として SKILL に体系化。次プロジェクト・別 brand での Figma 化作業で即活用可能にする。

### 成果

| 成果物 | 場所 | 内容 |
|---|---|---|
| `figma-component-from-spec/SKILL.md` | `.claude/skills/figma-component-from-spec/` | 287 行 / Marc 流 7 ステップ + 既知 Issue 1-7 + ベストプラクティス 1-20 + チェックリスト |

### SKILL 構造

1. **frontmatter**: name / description（trigger キーワード網羅）/ version / origin
2. **いつ使うか**: 4 シナリオ（新規生成 / 拡張 / audit / Build Log 記録）
3. **前提**: brand DS 構造 / Variables / figma-use Skill load
4. **ワークフロー（Marc 流 7 ステップ）**:
   - Step 0: **Audit-first**（最重要・絶対省略禁止）
   - Step 1: Spec md 完全読み込み
   - Step 2: Variables / Effect Styles 現状取得 + 健全性確認
   - Step 3: Component Set 構築（Phase 1 = 代表で型作り）
   - Step 4: スクリーンショット検証
   - Step 5: spec md に Figma 参照追記
   - Step 6: figma-build-log.md に Session 追加
   - Step 7: current.md milestone 更新
5. **既知の罠（Issue 1-7）**: 症状 / 原因 / 対処 / 回避をパターン化
6. **ベストプラクティス（学び 1-20）**: 4 カテゴリ（構造設計 / Variable bind / Layout / Text 等）に整理
7. **チェックリスト**: コミット前の確認 8 項目

### 学んだこと（追加）

21. **SKILL は frontmatter の `description` が trigger 判定の核**: 自然言語の起動キーワードを description に網羅することで、Skill 自動起動の精度が上がる。今回は「Figma に Component を作って」「spec から Figma 化」「L2/L3/L4 を Figma 化」「Component Set 拡張」「spec と Figma の整合性確認」を網羅。

22. **SKILL を git 管理対象に**: `.claude/skills/<name>/SKILL.md` を **プロジェクトリポジトリ内に置いてコミット** することで、worktree が消えても SKILL が消えない・チームで共有できる・PR レビュー対象になる。

### Known TODOs（SKILL v0.3 候補）

- **brand 横展開**: 「`brand/<brand>/...`」のように brand 名をパラメータ化（現状 FAMBOX 前提のパス）
- **他 brand での実証**: FAM ではない別 brand のプロジェクトで SKILL を起動して有効性検証
- **figma-use との依存関係明示**: SKILL load 順序を frontmatter で宣言できる仕組み（プラットフォーム側に要望）

---

## Session 2026-05-12 (#9) — Hero Section variants 拡充（SKILL v0.2 実証実験）

**契機**: 直前に整備した `figma-component-from-spec` SKILL v0.2 を実 Component で実証。Audit #4 で検出した Hero Section の spec gap（spec 4 variants / Figma 3 variants）を SKILL の 7 ステップを愚直に踏んで解消する。

### SKILL の各ステップ実証ログ

| Step | 実行内容 | 結果 |
|---|---|---|
| 0. Audit-first | 既に Audit #4 で実施済（67:73 存在、3 variants）| ✅ 重複生成回避 |
| 1. Spec md 完全読み込み | `## Variants（4 種 / 拡張可）` 表 + `## Heights（3 段階）` を確認、4 つ目の variant が **video-split** と判明 | ✅ spec の真意把握 |
| 2. Variables / Effect Styles | drive / ink / white / 既存 ID 再利用 | ✅ 既存 token 活用 |
| 3. Component Set 構築 | 不足 1 variant（video-split）を Phase 1 で追加。heights property は v0.4 へ送付 | ✅ Phase 戦略適用 |
| 4. スクリーンショット検証 | `get_screenshot` で spec の「左右分割 + 4 Corner + 中央テキスト」表現を視覚確認 | ✅ 一発で OK |
| 5. spec md に Figma 参照追記 | hero-section.md に v0.3-figma エントリ + video-split 仕様 + v0.4 残 TODO | ✅ |
| 6. figma-build-log 更新 | 本 Session #9 を記録 | ✅ |
| 7. current.md milestone | 4 → 4 variants 完備マイルストーン追加 | ✅ |

### 成果

| Component | 操作 | 状態 | Set ID | Variants |
|---|---|---|---|---|
| Hero Section | variant=video-split 追加 | 3 → 4 variants | `67:73`（変わらず） | video-fullscreen / image-editorial / minimal-text / **video-split** |

### video-split 詳細

- 1440 × 700, `layoutMode: 'NONE'`（4 corner + overlay の絶対配置のため）
- 左 video placeholder 720×700 dark teal / 右 720×700 dark slate
- 4 Corner Icons 40×40 Drive、32px offset
- 中央 overlay 600×auto: Eyebrow "FAMBOX × CAMPAIGN" Poppins SemiBold 14 + Title 48 Bold White + Sub 16 + CTA Button (46:32) instance「話を聞いてみる」

### SKILL v0.2 の検証結果

| 検証項目 | 評価 | コメント |
|---|---|---|
| Step 0 Audit-first の有効性 | ◎ | 既存 Set を再利用、新規生成回避 |
| Step 1 Spec md 一次資料化 | ◎ | spec 表を読むだけで「4 つ目は video-split」と即特定 |
| Phase 1 戦略 | ◎ | 12 variants 全展開でなく 4 variants 完備を優先、heights は v0.4 へ |
| Issue 6 回避（layoutMode NONE での layoutPositioning 不使用）| ◎ | 直接 `x/y` で配置、エラーなし |
| 学び 19 適用（既存 Button の `createInstance`）| ◎ | CTA を Button (46:32) primary lg から instance 化 |
| 学び 22 適用（SKILL の git 管理）| ◎ | SKILL ファイルが既に commit 済、利用フローが透明 |
| **総合** | **A+** | SKILL は実用レベル、抜け漏れなし |

### 検出した SKILL 改善点（v0.3 候補）

- **Step 3 に「拡張時の変位置決定パターン」を明記**: 既存 Set に新 variant を `appendChild` する際、x/y は既存 variants の縦並び規則に合わせる（今回は y = 既存最終 y + 既存最終 height + 100 gap）。
- **Step 4 の検証フローに「Component Set 全体 vs 個別 variant の screenshot を選ぶ判断」を追加**: 新 variant 単体を撮るか、Set 全体で他 variants との比較を撮るかをガイド化。

### 学んだこと（追加）

23. **既存 Component Set への variant 追加は `set.appendChild(newVariant)`**: 新規 Set 作成より少ない手数、property definitions も自動拡張される。

24. **既存 Set への variants 追加時の x/y 配置規則**: 既存 variants の縦並び（または横並び）パターンを inspect で確認してから、その規則を踏襲する。今回 Hero は y = 0 / 800 / 1600 の 100px gap だったので、新 variant も y=2200 に配置。

### Known TODOs（Hero v0.4 残）

- **`height` property 追加**: compact / default / tall → 4 × 3 = 12 variants 完備
- **NBA HOOP モード** boolean property（Editorial variant のタイポ重ね ON/OFF）
- **left video / right video の image fill バインド**（現状 dark gray placeholder）
- 4 Corner Icons を実 icon instance に置換（現状 Drive rectangle placeholder）

---

## Session 2026-05-12 (#10) — Bento Tile 20 variants 完備（size property 拡張）

**契機**: Session #9 で SKILL v0.2 の実用性を A+ で検証済。続いて Bento Tile の Phase 2 = 残 4 sizes 追加を SKILL の手順通りに実行し、TOP 実装 5/29 主役エリアの完全体化を目指す。

### SKILL の各ステップ実証ログ

| Step | 実行内容 | 結果 |
|---|---|---|
| 0. Audit-first | 既存 `87:26` 確認、4 variants × default size のみ | ✅ 重複生成回避 |
| 1. Spec md 再読み込み | Sizes 表（5 sizes）と各サイズの寸法・用途を確認 | ✅ spec の真意把握 |
| 2. Variables | 既存 token 再利用、新規取得不要 | ✅ |
| 3. Component Set 拡張 | 既存 4 variants を rename（`size=2x2` 追加）→ 16 variants clone（4 variants × 4 残 sizes）→ grid 配置 | ✅ Phase 2 完了 |
| 4. スクリーンショット検証 | 20 variants が grid に配置されることを確認、1×1 でコンテンツ切れ検出 | ✅ + 次 Phase 課題発見 |
| 5. spec md 更新 | bento-tile.md に v0.3-figma エントリ + 20 variants の完全マッピング | ✅ |
| 6. figma-build-log 更新 | 本 Session #10 を記録 | ✅ |
| 7. current.md milestone | 20 variants 完備マイルストーン追加 | ✅ |

### 成果

| Component | 操作 | 状態 | Set ID | Variants |
|---|---|---|---|---|
| Bento Tile | size property 拡張 | 4 → 20 variants | `87:26`（変わらず）| 4 variant × 5 size = **20 variants 完備** |

### 配置レイアウト（grid 2400 × 2000）

| 列（variant） \ 行（size） | 1×1 (160×160) | 2×1 (360×160) | 1×2 (160×360) | 2×2 (360×360) | 3×2 (560×360) |
|---|---|---|---|---|---|
| standard | ✅ | ✅ | ✅ | ✅（元）| ✅ |
| glass | ✅ | ✅ | ✅ | ✅（元）| ✅ |
| image-fill | ✅ | ✅ | ✅ | ✅（元）| ✅ |
| stat-focus | ✅ | ✅ | ✅ | ✅（元）| ✅ |

### 検出した次 Phase 課題

- **1×1 (160×160) でコンテンツ切れ**: spec のデフォルトテキスト「タイルタイトル」「本文テキストの説明…」が 160px 幅で見切れる
- **判断**: spec で「1×1 は小タイル / Icon / Quote 用」と既定。production では size に応じたコンテンツが入る前提。**コンテンツ最適化は v0.4 で各 size 別の見せ方を Spec 化** する

### SKILL v0.2 の検証結果（実証 2 回目）

| 検証項目 | 評価 | コメント |
|---|---|---|
| Step 0 Audit-first | ◎ | 既存 Set 即発見 |
| Step 1 Spec md | ◎ | Sizes 表が即読み込め、判断材料に直結 |
| Step 3 拡張パターン | ◎ | rename → clone → grid 配置のフローが安定 |
| Issue 5 回避（resize 後の FIXED 設定）| ◎ | clone 後に `primaryAxisSizingMode = 'FIXED'` 明示で size 反映 |
| 学び 23 適用（既存 Set への `appendChild`）| ◎ | clone を Set に直接 append、property definitions 自動拡張 |
| **総合** | **A+** | SKILL v0.2 は L3 multi-property 拡張でも有効 |

### 学んだこと（追加）

25. **size property の variantOptions 順序は追加順**: 既存 `2x2` から clone & rename した場合、Figma 側の `variantOptions` 配列は `['2x2', '1x1', '2x1', '1x2', '3x2']` の追加順になる。**spec の表記順（1x1 / 2x1 / 1x2 / 2x2 / 3x2）と一致しない**ため、UI で表示する時の並び順は別途整列が必要（プロパティ panel での視認性のみ問題、機能的影響なし）。

26. **2D Property の grid 配置パターン**: variants × sizes のような 2 property を全展開する場合、`列 = property1 / 行 = property2` の matrix 配置がレビュー時に最も読みやすい。Set の x/y を `cIdx * COL_W + rIdx * ROW_H` で計算。

### Known TODOs（Bento v0.4 残）

- **size 別のコンテンツ最適化**: 1×1 / 2×1 / 1×2 / 3×2 ごとの推奨コンテンツ密度を spec 化（タイトル文字数 / 本文行数 等）
- **state property 追加**: hover（shadow-3 + translateY -2px）/ focus-visible / disabled
- **Glass の 5 階調 modifier**: glass--1 ～ --5（opacity 0.05 / 0.1 / 0.3 / 0.6 / 0.8）を別 property 化
- ✅ **Bento Grid (`91:107`) の placeholder rect を Bento Tile instance に置換**（Phase 3）— Session #11 で editorial variant 完了

---

## Session 2026-05-12 (#11) — Bento Grid editorial × Bento Tile 双方向参照確立（Phase 3）

**契機**: Bento Tile 20 variants 完備（#10）で Tile 側準備が整ったため、Bento Grid editorial variant の placeholder 9 個を Bento Tile instance に置換し、**Tile 単体修正が Grid demo に自動反映** される双方向参照を確立する。

### SKILL の各ステップ実証ログ

| Step | 実行内容 | 結果 |
|---|---|---|
| 0. Audit-first | Grid (`91:107`) と Tile (`87:26`) の現状確認 | ✅ |
| 1. Spec md | editorial パターン A の 9 tiles 構成を再確認（主役 2×2 + 主役 3×2 + 1×1×4 + 2×1×2）| ✅ |
| 2. Variables | 既存 token 再利用 | ✅ |
| 3. Component 操作 | placeholder の x/y/size/stroke 識別 → Tile instance 化 → resize → placeholder 削除 | ✅ 9/9 成功 |
| 4. スクリーンショット検証 | 全 9 tiles が instance として表示確認、課題 3 件検出 | ✅ + 課題発見 |
| 5. spec md 更新 | bento-grid.md に v0.3 進捗とv0.4 残 TODO 追加 | ✅ |
| 6. figma-build-log 更新 | 本 Session #11 を記録 | ✅ |
| 7. current.md milestone | 双方向参照確立マイルストーン追加 | ✅ |

### 成果

| Component | 操作 | 結果 | Set ID |
|---|---|---|---|
| Bento Grid editorial | placeholder 9 個 → Bento Tile instance 9 個に置換 | 双方向参照確立 | `91:107` / editorial variant `91:67` |

### Tile instance マッピング規則

| placeholder 属性 | 適用 Tile variant |
|---|---|
| stroke = 2px Drive（主役）| **glass** variant |
| stroke = 1px border-light（非主役）| **standard** variant |
| size label "1×1" | tile size `1x1` |
| size label "2×1" | tile size `2x1` |
| size label "2×2" | tile size `2x2` |
| size label "3×2" | tile size `3x2` |

placeholder の x/y/width/height を読み取り、instance を **同位置・同サイズ** で配置（`instance.resize(phW, phH)` で Grid 内の placeholder サイズに合わせる）。

### 検出した次 Phase 課題

#### 🐛 Issue 8: Tile instance 化で主役識別の Drive 2px 枠が消失
- **症状**: placeholder では Drive 2px stroke で主役識別していたが、Tile instance には Drive stroke が含まれない
- **原因**: Bento Tile Component 自体に `featured` 概念がなく、主役識別が Grid 側 placeholder の責務だった
- **対処（v0.4）**: 以下のいずれか:
  - (A) Bento Tile に **`featured` boolean property** を追加し、true で Drive 2px stroke を表示
  - (B) Bento Tile に **`featured` variant** を追加（Card の `card-featured` と同パターン）
  - (C) Grid 側で instance の上に Drive stroke の rect overlay を別途配置
- **暫定**: 主役識別が失われたまま v0.3 完了とし、v0.4 で (A) または (B) を実装

#### 🐛 Issue 9: resize した Tile instance のコンテンツ密度オーバー
- **症状**: 1×1 (200×200) / 2×1 (424×200) では本文「タイルタイトル / 本文テキストの説明…」が切れる
- **原因**: Tile の auto-layout がコンテンツ固定で、container resize しても text は wrap せず溢れる
- **対処（v0.4）**: size 別の text overflow 規律を spec で確定（例: 1×1 は title のみ、2×1 は title + 1 行本文）

#### 🐛 Issue 10: Glass variant 3×2 のテキスト下寄せが過剰
- **症状**: 3×2 メガサイズで Glass の text が左下に集中、main hero として上中央に配置したい
- **原因**: Glass variant の `primaryAxisAlignItems: 'MAX'` がデフォルト、size 共通で適用されてしまう
- **対処（v0.4）**: Glass variant に `align` boolean property（top / bottom）を追加 or size 別の auto-layout overrideroad

### 学んだこと（追加）

27. **既存 Component の instance 化と resize で双方向参照を確立**: `createInstance()` → `resize(W, H)` で別サイズ Set の demo として利用可能。Tile 単体修正が Grid に反映される設計が機能。

28. **instance 化で「stroke / overlay 等の placeholder 固有属性は失われる」**: placeholder の strokes は Tile に転写されない。**主役識別など Component 横断の状態は Tile 側 property として持つべき**（Phase 3 で発覚した設計ミス）。

29. **resize は内部 auto-layout を**ある程度**追従させる**: Tile の auto-layout は container 拡張時に縦間隔が維持される。ただしテキストの wrap までは制御できないので、size 別の text overflow 規律を spec で別途定める必要がある（学び 29.5）。

### SKILL v0.2 の検証結果（実証 3 回目）

| 検証項目 | 評価 | コメント |
|---|---|---|
| Step 0 Audit + 既存 Component の inspect | ◎ | placeholder 9 個と Tile 20 variants の mapping を一発取得 |
| Step 3 instance 化フロー | ◎ | createInstance + resize + 削除の 3 ステップが clean |
| Step 4 検証で課題発見 | ◎ | screenshot で Issue 8-10 を即特定 |
| Step 5-7 ドキュメント反映 | ◎ | v0.4 課題化が体系的 |
| **総合** | **A** | SKILL は有効、ただし「Phase 3 = 双方向参照確立」のような新ユースケースで Issue を新規発見 → SKILL v0.3 にも反映余地あり |

### SKILL v0.3 改善候補（追加）

- **Phase 3「Component 間の参照確立」**を Step 3 のサブパターンとして明記:
  - instance 化と resize の手順
  - placeholder 固有属性（stroke / overlay 等）が転写されないことを警告
  - 主役識別など状態は Component 側 property として設計推奨
- **Tile 間サイズ乖離の検証手順**を Step 4 に追加（resize 前後の auto-layout 挙動を screenshot で比較）

---

## Session 2026-05-12 (#12) — figma-component-from-spec SKILL v0.3 整備

**契機**: Session #9-11 の 3 回の SKILL 実証実験で発見した改善候補 5 件 + 学び 21-29 + Issue 8-10 を SKILL に還元し、次サイクル以降の作業を安定化させる。

### 成果

| 成果物 | 変更内容 |
|---|---|
| `SKILL.md` v0.2 → **v0.3** | 287 行 → 拡張後 計 ~390 行 |

### v0.3 で追加した内容

#### 1. frontmatter 拡充
- `description`: 「Phase 戦略」「Component 間参照確立」「variant property 追加」「instance に置換」を triggers に追加
- `origin`: 7 → 11 セッション / 20 → 29 項の学び / 7 → 10 Issue
- `version`: 0.2 → 0.3

#### 2. Step 3 を「Phase 戦略」セクションに大幅拡張
- **Phase 1 (新規生成)**: 既存内容 + combineAsVariants 1 variant 化
- **Phase 2 (variant property 拡張)**: rename → clone → grid 配置のフロー、1D / 2D 配置規則、コードサンプル
- **Phase 3 (Component 間参照確立)**: instance 化 + resize + remove、placeholder 固有属性転写なしの warning、source Component 側 property 設計推奨

#### 3. Step 4 を「撮影単位の選択ガイド」に拡張
- 新規生成 / 拡張 / 参照確立 の 3 シナリオごとの screenshot 撮影単位を表化
- Phase 3 専用「resize 前後の auto-layout 挙動検証」セクション追加

#### 4. 既知の罠を Issue 1-7 → Issue 1-10 に拡張
- Issue 8: instance 化で placeholder 固有属性消失（Phase 3 で発覚）
- Issue 9: resize 後の content 密度オーバー
- Issue 10: auto-layout `primaryAxisAlignItems: 'MAX'` の縦伸び挙動

#### 5. ベストプラクティスを 20 → 29 項に拡張
- **新カテゴリ「SKILL 設計」（21-22）**: description が trigger 核 / SKILL の git 管理
- **新カテゴリ「拡張パターン (Phase 2)」（23-26）**: appendChild / x/y 配置 / variantOptions 順序 / 2D matrix
- **新カテゴリ「参照確立 (Phase 3)」（27-29）**: createInstance + resize / 属性転写なし / resize と auto-layout

#### 6. チェックリストを Phase 別に分割
- Phase 1 / Phase 2 / Phase 3 / 共通 の 4 セクション化
- 計 18 項目（v0.2 は 8 項目）に細分化

### 学んだこと（追加）

30. **SKILL は実証→改善→再実証のサイクルで進化させる**: v0.2 を作って即実 Component で実証することで、SKILL 自体の抜け漏れが判明する。**3 回の実証で 5 改善 + 9 新学び + 3 新 Issue を還元** できた。これは SKILL 単独設計より圧倒的に有効。

31. **Phase 戦略は Marc 流の本質**: 「Phase 1 で型作り → Phase 2 で量増 → Phase 3 で参照確立」という段階構造は、Component の拡張規律として再利用可能。Skill に明示することで、次プロジェクトでも一貫した進め方ができる。

### Known TODOs（SKILL v0.4 候補）

- **brand 横展開のパラメータ化**: `brand/<brand>/` パスを変数化、別 brand プロジェクト即適用
- **figma-use との依存関係宣言**: SKILL load 順序を frontmatter で宣言できる仕組み（プラットフォーム側に要望）
- ✅ **新ユースケース実証**: Bento Tile に `featured` property 追加 — Session #13 完了
- **Token migration ユースケース**: 既存 Component の直値 stroke を Variable bind に置換する手順（Card v0.3 残 TODO に該当）

---

## Session 2026-05-12 (#13) — Bento Tile featured property 追加（SKILL v0.3 実証 + Issue 8 解消）

**契機**: SKILL v0.3 で明示した「Phase 2 = variant property 拡張」と Session #11 で発見した Issue 8（instance 化で主役識別 stroke 消失）を同時に解消。SKILL v0.3 の Phase 2 を新しい variant property（boolean 的）でも実証する。

### SKILL v0.3 Phase 2 実証ログ

| Phase 2 ステップ | 実行内容 | 結果 |
|---|---|---|
| 0. Audit-first | 既存 `87:26` (20 variants) 確認 | ✅ |
| 1. Spec md | featured 仕様（spec の `card-featured` パターン継承）を Issue 8 から逆算 | ✅ |
| 2. Variables | `color/brand/drive` 既存利用 | ✅ |
| 3. rename → clone → 配置 | featured=false 追加 → 全 variants を clone して featured=true 化 → Drive 2px stroke 適用 → 2 ブロック配置 | ✅ |
| 4. スクリーンショット検証 | 左 (false) / 右 (true) ブロックで対比、stroke が全 20 variants に均一適用されたことを確認 | ✅ |
| 5-7. ドキュメント反映 | bento-tile.md / build-log / current.md 同時更新 | ✅ |

### 成果

| Component | 操作 | 結果 | Set ID |
|---|---|---|---|
| Bento Tile | featured boolean variant property 追加 | 20 → 40 variants | `87:26`（変わらず） |

**最終 property 構成**: `variant` (4) × `size` (5) × `featured` (2) = 40 variants

### featured 仕様

| featured 値 | stroke 仕様 | 用途 |
|---|---|---|
| `false` (既定) | 既存維持（standard/stat-focus: border-light 1px / glass/image-fill: なし） | 通常 Tile |
| `true` | **全 variant 一律 Drive 2px stroke**（individualStrokeWeights を 2/2/2/2 で均一化） | Bento Grid editorial の主役識別 / Subscription Plan 推奨プラン |

### 配置レイアウト（4900 × 2000）

```
左ブロック (featured=false)              右ブロック (featured=true)
x: 0 - 2400                              x: 2500 - 4900
4 cols × 5 rows                          4 cols × 5 rows
既存通り                                 全 variants に Drive 2px stroke
```

### SKILL v0.3 の検証結果

| 検証項目 | 評価 | コメント |
|---|---|---|
| Step 3 (Phase 2) の rename → clone → grid 配置 フロー | ◎ | v0.3 で明文化されたコードサンプルがそのまま機能 |
| Issue 8 への対処（Tile 側 property として featured を追加） | ◎ | v0.3 で「placeholder 固有属性は source 側 property として持つべき」と明記、それに従って実装 |
| 学び 24 適用（配置規則の踏襲）| ◎ | 既存 2400 × 2000 の grid 配置を踏襲、featured=true ブロックを +2500 offset で並置 |
| 学び 25 適用（variantOptions 順序は追加順）| △ | `featured=['false', 'true']` 自体は順序問題なし。`size` は前 Session 順を継承（'2x2' が先頭）— UI 表示時の整列は別途対応 |
| **総合** | **A+** | SKILL v0.3 は Phase 2 の boolean 的 property 追加でも有効 |

### 学んだこと（追加）

32. **boolean 的な variant property は文字列 'true'/'false' で**: Figma の variant property 型は `VARIANT`（文字列）のみで、真の Boolean 型は存在しない。`featured` を `true`/`false` の variant option として実装すれば、UI 側で boolean トグル風に表示される。

33. **既存 strokes を上書きする場合は individual stroke weights もリセット**: 一部の既存 variant に `strokeRightWeight = 2`（Profile の Title icon 等）が残っていると、新 stroke 適用後も古い individual 値が残る。**4 辺の `strokeTopWeight / RightWeight / BottomWeight / LeftWeight = 2` を明示** することで完全均一化。

### Known TODOs（Bento featured v0.4 残）

- ✅ **Bento Grid editorial の主役 instances を `featured=true` に切替**: Session #14 で完了
- featured=true で `--shadow-2` の hover 拡張（Card Pattern の selected 状態と同期）

---

## Session 2026-05-12 (#14) — Bento エコシステム完成 + Issue 8 完全解消

**契機**: Session #13 で Tile 側に featured property を用意できたので、Bento Grid の Phase 3 を完成させる:
- editorial の 2 主役 instance を featured=true 版に **swap** で切替
- standard / autofit variant の placeholder を **Tile instance に置換**（editorial と同手順）

### 成果

| Variant | 操作 | 結果 |
|---|---|---|
| editorial | 2 主役 instance を featured=true に **`swapComponent`** | Drive 2px stroke 復活、Issue 8 完全解消 |
| standard | placeholder 5 個 → **standard Tile instance** 置換 | 双方向参照確立 |
| autofit | placeholder 8 個 → **stat-focus Tile instance** 置換 | spec 整合（KPI ダッシュボード = "-3.2 kg" × 8）|

**置換総計**: 13 placeholder → 13 instance + 2 swap = 15 操作。エラー 0。

### `swapComponent` の活用（学び 34）

既存 instance の main component を **swap** することで、placeholder を delete + 新 instance を作成 のフローを 1 行に短縮できる。x/y/size はそのまま保持される。

```js
const hero2x2 = await figma.getNodeByIdAsync('104:57'); // existing instance
const featuredTrueVariant = await figma.getNodeByIdAsync('105:14'); // glass/2x2/featured=true
hero2x2.swapComponent(featuredTrueVariant);
// position/size unchanged, but stroke and all featured=true property reflect through
```

**Phase 3 の 2 種類のパターン**:
- **placeholder → instance**: 新規 instance 作成（remove old, create new）
- **instance → instance**: `swapComponent` で main component を切替（同一 instance 維持）

### 寸法 → size key の自動推定（学び 35）

Bento Grid の placeholder は size label を text として持っていたが、これに依存せず **寸法から size を直接推定** する関数を採用:

```js
function sizeKey(w, h) {
  const cols = { 200: 1, 424: 2, 648: 3 }[w] || 2;
  const rows = { 200: 1, 424: 2 }[h] || 1;
  // ...
}
```

これにより size label が欠落している placeholder（自動配置 etc）でも置換可能。

### 検出した次 Phase 課題

#### 🐛 Issue 11: spec にない size の placeholder（3×1）
- **症状**: standard variant の最後の placeholder が 648 × 200 = 3×1 だが、Tile sizes は 1x1 / 2x1 / 1x2 / 2x2 / 3x2 のみ
- **対処**: 2×1 Tile を resize で対応（横長表現は維持できるが、Tile auto-layout が崩れる可能性）
- **本質的解消**: spec で Tile sizes に **3x1 を追加するか**を v0.4 で判断（DNA 5 sizes 厳守ルールとの整合）

### SKILL v0.3 の検証結果（実証 2 回目）

| 検証項目 | 評価 | コメント |
|---|---|---|
| Step 3 Phase 3 「instance → instance swap」パターン | ◎ | v0.3 で明示した「createInstance + resize + remove」に加え、`swapComponent` パターンを発見 → v0.4 SKILL へ追加候補 |
| 寸法 → size 推定 heuristic | ◎ | spec ↔ Figma の不整合（3x1）に対しても fallback で動作 |
| placeholder 全件置換の安定性 | ◎ | 13 placeholder + 2 swap = 15 操作でエラー 0 |
| **総合** | **A+** | SKILL v0.3 Phase 3 は安定運用フェーズ |

### 学んだこと（追加）

34. **`swapComponent` は Phase 3 の第 2 パターン**: 既存 instance を別 variant に切り替える時、delete + new ではなく **swap で in-place 変更**できる。x/y/size を再設定不要、上位の auto-layout 配置も保持される。

35. **寸法 → size key 自動推定**: placeholder の text label に依存せず、width/height の数値から size を逆算する関数で堅牢化。spec ↔ Figma の data 整合性が完璧でなくても動作する。

### Known TODOs（Bento エコシステム v0.4 残）

- Issue 11: Tile に 3x1 size 追加 or Grid placeholder を 2x1 + 1x1 に分割
- Tablet / SP responsive variants
- `bento-gap--sm/md/lg` modifier の Figma 表現
- editorial 以外の variant にも主役識別が必要か仕様レビュー（現状 standard / autofit は主役なし）

---

## Session 2026-05-12 (#15) — figma-component-from-spec SKILL v0.4 整備

**契機**: Session #13-14 で得た新パターン（boolean 的 variant、swapComponent、寸法 → size 自動推定）と Issue 11 を SKILL v0.3 に還元し、Phase 3 を堅牢化。

### v0.4 で追加した内容

#### 1. frontmatter 拡充
- `description`: 「instance を swap」「featured 追加」を triggers に追加 / Phase 3 の 2 パターンを明記
- `origin`: 11 → 14 セッション / 29 → 35 学び / 10 → 11 Issue / Phase 3 の 2 パターン明示
- `version`: 0.3 → 0.4

#### 2. Step 3 Phase 3 に「2 パターン」明示
- **Pattern A**: placeholder → instance（既存内容、`createInstance + resize + remove`）
- **Pattern B (新規)**: instance → instance **swap**（`existingInstance.swapComponent(newVariant)`、x/y/size 保持）
- **使い分け**: rect/frame から始める → A、property 値変更だけ → B

#### 3. Step 3 に「寸法 → size 自動推定 heuristic」追加
- `sizeKey(w, h)` 関数のコードサンプル
- text label に依存せず、width/height から逆算する堅牢化パターン
- fallback で不一致 size（Issue 11）に対応

#### 4. Issue 1-10 → Issue 1-11 に拡張
- Issue 11: spec にない size の placeholder（Phase 3 で遭遇する spec ↔ Figma 不整合）

#### 5. ベストプラクティスを 29 → 35 項に拡張
- **既存「SKILL 設計」「拡張パターン」「参照確立」カテゴリに新項目追加**
- **新カテゴリ「Boolean 的 property / stroke 上書き」（32-33）**: featured 等の boolean 風 property の実装 + stroke 上書き時の individualStrokeWeights リセット
- **新カテゴリ「Phase 3 拡張パターン」（34-35）**: swapComponent / 寸法→size 自動推定

#### 6. チェックリスト Phase 3 セクションを Pattern 別に再構成
- Pattern A / Pattern B の選択を明確化
- 寸法 → size 自動推定の用意を必須項目化
- Grid placeholder と source Component の size 事前照合を追加（Issue 11 回避）

### 学んだこと（追加）

36. **SKILL v0.3 で「拡張時に新パターンが現れる」を予測できなかった**: v0.3 は Phase 3 を 1 パターン（placeholder→instance）のみで明示していたが、Session #14 で swapComponent パターンが実用上の第 2 パターンとして出現。**新ユースケースは実証してから明示する**しかなく、SKILL は永続的に進化する性質を持つ。

37. **「Phase 3 の事前 audit」を SKILL に追加すべき**: Issue 11（spec にない size の placeholder）は事前 audit で防げた。Phase 3 着手前に「Grid placeholder size × Source Component size の cross-check」をルーチン化 → v0.5 SKILL で。

### SKILL v0.4 検証計画（次セッション以降）

- 新ユースケース: Hero `height` property 追加（4 × 3 = 12 variants）で Phase 2 の 1D 拡張をもう 1 回実証
- Phase 3 Pattern B の追加実証: Card Pattern の Featured variant を card-featured 用 instance に swap
- Token migration ユースケース: 直値 stroke → Variable bind の置換（Card v0.3 残）

### Known TODOs（SKILL v0.5 候補）

- **Phase 3 事前 audit ステップ追加**: Grid placeholder size × Source Component size の cross-check ルーチン化
- **brand 横展開のパラメータ化**: `brand/<brand>/` パスを変数化、別 brand プロジェクト即適用
- **Token migration セクション**: 既存 Component の直値 → Variable bind 置換手順
- **新 Issue が出るたびに v0.X+1 で還元**するサイクルを継続

---

## Session 2026-05-12 (#16) — Hero Section height property 追加（SKILL v0.4 Phase 2 1D 拡張実証）

**契機**: SKILL v0.4 を実証するため、Audit #4 で残っていた Hero Section の spec gap（spec 12 variants 想定 / Figma 4 variants）を解消。SKILL v0.4 の Phase 2 = 1D 拡張パターンで `height` property を追加。

### SKILL v0.4 Phase 2 (1D 拡張) 実証ログ

| Step | 実行内容 | 結果 |
|---|---|---|
| 0. Audit-first | `67:73` の現状 4 variants 確認 | ✅ |
| 1. Spec md | Heights セクションの `hero--full` (100vh) / `hero--tall` (70vh) / `hero--compact` (40vh) を取得 | ✅ |
| 2. Variables | 既存利用 | ✅ |
| 3. Phase 2 拡張 | rename → clone × 2 → 2D matrix 配置 + minimal-text 既存高さ統一 | ✅ |
| 4. スクリーンショット | 12 variants が 4×3 matrix に配置されることを確認、compact で内部要素見切れ検出 | ✅ + 課題発見 |
| 5-7. ドキュメント | hero-section.md / figma-build-log / current.md 同時更新 | ✅ |

### 成果

| Component | 操作 | 結果 |
|---|---|---|
| Hero Section | height property 追加 + minimal-text 高さ統一 | **4 → 12 variants 完備** |

**Property 構成**: `variant` (4) × `height` (3) = 12 variants
**配置**: 4 列 × 3 行 matrix (`x = cIdx * 1500, y = rIdx * 750`)、Set 全体 6000 × 2250
**Figma px → Spec vh 対応**:
- `default` 1440×700 = `hero--full` (100vh)
- `tall` 1440×550 = `hero--tall` (70vh)
- `compact` 1440×400 = `hero--compact` (40vh)

### SKILL v0.4 の検証結果（Phase 2 1D 拡張、3 回目）

| 検証項目 | 評価 | コメント |
|---|---|---|
| Step 3 Phase 2 「rename → clone → 2D matrix」フロー | ◎ | v0.3 で明文化されたパターンがそのまま機能 |
| 学び 24 (配置規則踏襲) と 26 (2D matrix) の組合せ | ◎ | 1D 拡張だが既存配置と直交する 2D matrix で表示すると視認性高い |
| 学び 33 (既存 strokes 上書き) | – | 今回は stroke 操作なし、適用機会なし |
| **総合** | **A+** | SKILL v0.4 は Phase 2 1D 拡張でも安定運用フェーズ |

### 検出した次 Phase 課題

#### 🐛 Issue 12: compact で内部要素が見切れる
- **症状**: minimal-text variant の default (700) を compact (400) に縮めると、内部の text / CTA が一部見切れる
- **原因**: 既存 variants は default (700) を前提に auto-layout 設計されていて、内部要素間の余白が固定
- **対処（v0.5）**:
  - (A) compact 専用に内部 padding / itemSpacing を縮小 override
  - (B) `primaryAxisAlignItems: 'CENTER'` で中央寄せに変更
  - (C) compact では一部要素を非表示（boolean property で）
- **回避**: 今回は Phase 2 = サイズ拡張に集中、内部最適化は別 Phase へ送付

### 学んだこと（追加）

38. **1D 拡張でも 2D matrix 配置がレビューしやすい**: variant × height のような 2 property を持つ場合、新規 property が 1D だけ拡張する場合でも、視覚的には matrix で配置することで「どの組合せが完備しているか」が一目瞭然。

39. **既存 variants のサイズ差異は拡張前に統一する**: minimal-text の既存 height 500（他は 700）を、default 揃えで 700 に統一した。**Phase 2 拡張時に既存の不揃いを正す**ことで、後続の variants が綺麗に配置される。

### SKILL v0.5 への新たな改善候補（追加）

- **Phase 2 着手前の「既存 variants サイズ統一」チェック**: 不揃いがあれば Phase 2 着手前に修正
- **Phase 2 の auto-layout 制約**: 既存 variants の auto-layout 設計が default size 前提なら、拡張時に内部要素が見切れる（Issue 12）。**Phase 2 では「サイズ変動でも内部要素が崩れない auto-layout 設計」を確認** すべきと SKILL に明記

### Known TODOs（Hero v0.5 残）

- Issue 12 解消: compact で内部要素が見切れる auto-layout 調整
- NBA HOOP モードの boolean property 化
- video-fullscreen / video-split の `image-fill` Image fill バインド

---

## Session 2026-05-12 (#17) — figma-component-from-spec SKILL v0.5 整備

**契機**: Session #15-16 で得た **Phase 2 / Phase 3 の事前 audit 必要性** + 学び 38-39 + Issue 12 を SKILL v0.4 に還元し、各 Phase 着手前のリスク検知をルーチン化する。

### v0.5 で追加した内容

#### 1. frontmatter 拡充
- `description`: 「Phase 2/3 事前 audit」「height property 追加」を triggers / 説明に追加
- `origin`: 14 → 16 セッション / 35 → 39 学び / 11 → 12 Issue / Phase 2/3 事前 audit 追記
- `version`: 0.4 → 0.5

#### 2. Phase 2 に「事前 audit」サブセクションを正式追加（必須）
- 既存 variants のサイズ差異検出（学び 39）
- 既存 auto-layout のサイズ変動耐性確認（Issue 12 回避）
- audit 結果に応じた対応分岐（統一 / 補修計画 / そのまま進行）

#### 3. Phase 3 に「事前 audit」サブセクションを正式追加（必須）
- target placeholder size × source Component variant size の cross-check
- unmatched があれば「spec 改訂」or「fallback heuristic」を判断
- Issue 11 を Phase 3 事前 audit で検知可能に

#### 4. Issue 1-11 → Issue 1-12 に拡張
- Issue 12: Phase 2 サイズ拡張で既存 auto-layout が縮小耐性なし（Hero compact で発覚）

#### 5. ベストプラクティスを 35 → 39 項に拡張
- **新カテゴリ「Phase 2 補強」（38-39）**: 1D でも 2D matrix 配置 / 既存サイズ統一を事前に

#### 6. チェックリストに事前 audit を必須化
- Phase 2: 「サイズ差異検出」「auto-layout 変動耐性」の 2 項目を必須化
- Phase 3: 「placeholder × source size 全件照合」を必須化

### 学んだこと（追加）

40. **「事前 audit」は Phase 戦略のメタパターン**: Step 0 Audit-first（既存 Component 全件確認）と並んで、各 Phase 着手前にも事前 audit を入れることで、後で「Issue として表面化する問題」を **着手前に検知** できる。

41. **SKILL は「Issue 検知のチェックポイント」を増やすほど堅牢化する**: 各 Phase の事前 audit で「想定外を早期発見」する設計。Issue 12 のように Phase 2 拡張後に発覚した問題も、事前 audit があれば「補修計画を組み込んでから進む」判断ができた。

### Phase 1/2/3 + 事前 audit のフロー（v0.5 完成形）

```
[Step 0] 既存全件 Audit (図全体)
   ↓
[Step 1] Spec md 読み込み
   ↓
[Step 2] Variables / Effect Styles 取得
   ↓
[Step 3] Phase 戦略選択
   ├─ Phase 1 (新規生成)
   ├─ Phase 2 (property 拡張)
   │  └─ ★Phase 2 事前 audit (v0.5)
   │     ├─ 既存サイズ差異検出
   │     └─ auto-layout 変動耐性確認
   └─ Phase 3 (参照確立)
      └─ ★Phase 3 事前 audit (v0.5)
         └─ placeholder × source size cross-check
   ↓
[Step 4] スクリーンショット検証
   ↓
[Step 5-7] spec md / build-log / current.md 更新 → commit
```

### SKILL v0.6 候補

- **Phase 2/3 事前 audit の自動化 helper script**: チェックを Plugin API でワンライナー化（手動 mental simulation を機械化）
- **brand 横展開のパラメータ化**: `brand/<brand>/` パスを変数化
- **Token migration セクション**: 既存 Component の直値 → Variable bind 置換手順
- **Phase 4 提案: コンテンツ最適化**: Phase 2/3 後の auto-layout 補修・size 別 padding override を体系化

---

## Session 2026-05-12 (#18) — Issue 12 解消（SKILL v0.5 事前 audit 実証）

**契機**: SKILL v0.5 で正式手順化した「Phase 2 事前 audit」を実 Issue で実証。Hero Section の compact/tall variants の内部 auto-layout が default size 前提で設計されていた問題（Issue 12）を、audit → 補修パターンで完全解消する。

### SKILL v0.5 事前 audit 実証ログ

| ステップ | 実行内容 | 結果 |
|---|---|---|
| 事前 audit | compact 4 + tall 2 = 6 variants の内部構造（layoutMode / padding / 子要素 size）を inspect | ✅ 問題箇所 4 件特定 |
| 補修計画 | (A) padding 縮小 / (B) 内部 Rectangle resize / (C) layoutMode=NONE の絶対座標再計算 の 3 パターンを選定 | ✅ |
| 補修実行 | 6 variants を 1 script で一括補修 | ✅ エラー 0 |
| 検証 | screenshot で全 12 variants の表示確認、見切れ要素ゼロ | ✅ Issue 12 完全解消 |

### 事前 audit で検出した問題詳細

| Variant | height | 問題 | 補修内容 |
|---|---|---|---|
| video-fullscreen | compact | padding 96×2 + 内部要素 260h > 利用可 208h | padding 96→40、itemSpacing 24→12 |
| image-editorial | compact | 内部 Rectangle が 500h で 400h frame 内に収まらない | padding 96→32、Rectangle 500h→336h |
| minimal-text | compact | 元々問題なし（内部 149h < 利用可 208h）だが余裕で padding 縮小 | padding 96→64、itemSpacing 16→12 |
| video-split | compact | layoutMode=NONE、video 720×700 が 400h frame 外にはみ出す | video left/right 700h→400h、corners 再配置、overlay 中央 |
| image-editorial | tall | Rectangle 500h が 550h - padding 192 = 358h より大 | padding 96→72、Rectangle 500h→486h |
| video-split | tall | video 700h が 550h frame 外 | video 700h→550h、corners 再配置 |

### 補修パターン（学び 42）

3 つの再利用可能なヘルパー関数として整理:
- **`fixVerticalVariant(v, padding, itemSpacing)`**: VERTICAL auto-layout の padding / itemSpacing を縮小
- **`fixImageEditorial(v, padding, rectH)`**: HORIZONTAL auto-layout で内部 Rectangle のサイズを補修
- **`fixVideoSplit(v, targetH)`**: layoutMode=NONE で video/corners/overlay を targetH に合わせて手動再配置

これらは **Phase 2 後の auto-layout 補修パターン** として SKILL v0.6 に「Phase 4: コンテンツ最適化」として組み込み候補。

### SKILL v0.5 の検証結果（実証 1 回目）

| 検証項目 | 評価 | コメント |
|---|---|---|
| Phase 2 事前 audit による問題検知 | ◎ | 6 variants で問題箇所 4 件、全件事前検出可能 |
| Issue 12 の対処パターン化 | ◎ | 3 つのヘルパー関数で補修フローを再利用可能化 |
| **総合** | **A+** | 事前 audit ルーチンが実 Issue で機能することを実証 |

### 学んだこと（追加）

42. **補修パターンも SKILL に組み込む**: Phase 2 後の auto-layout 補修は 3 パターンに分類可能（VERTICAL padding 縮小 / HORIZONTAL 内部 Rectangle / NONE 絶対座標）。**Phase 4 = コンテンツ最適化フェーズ** として SKILL v0.6 に正式追加候補。

43. **事前 audit は実 Issue で初めて価値が顕在化する**: v0.5 で事前 audit ルーチンを SKILL に追加した時点では「予防的な手順」でしかなかったが、Session #18 で実際に Issue 12 を audit → 検知 → 補修まで通したことで、**ルーチンの有効性が実証** された。SKILL 整備は実証ループとセットで進化する（学び 30 の延長）。

### Known TODOs（Hero v0.6 残）

- NBA HOOP モードの boolean property 化
- video-fullscreen / video-split の `image-fill` Image fill バインド
- minimal-text の sub text が compact で 0 行になる場合の挙動確認

---

## Session 2026-05-12 (#19) — figma-component-from-spec SKILL v0.6 整備

**契機**: Session #18 の Issue 12 補修で得た 3 つのヘルパー関数（fixVerticalVariant / fixImageEditorial / fixVideoSplit）と Phase 4 = コンテンツ最適化フェーズの概念を SKILL に正式組み込み。学び 42-43 を還元。

### v0.6 で追加した内容

#### 1. frontmatter 拡充
- `description`: 「auto-layout 補修」「見切れ修正」「padding override」を triggers に追加
- 「Phase 戦略（1=新規 / 2=property 拡張 / 3=参照確立 / **4=コンテンツ最適化**）」と 4 フェーズ明示
- `origin`: 16 → 18 セッション / 39 → 43 学び / **Phase 4 補修ヘルパー 3 種** を体系化
- `version`: 0.5 → 0.6

#### 2. Phase 4 = コンテンツ最適化セクションを正式追加（v0.6 主成果）
- 「いつ Phase 4 が必要か」判定表
- **補修ヘルパー関数 3 種**を一般化:
  - `fixVerticalVariant(v, newPadding, newItemSpacing)`
  - `fixHorizontalVariantRect(v, newPadding, internalRectName, newRectH)`
  - `fixAbsoluteLayoutVariant(v, targetH, anchorNames)`
- Phase 4 の典型フロー（audit → 補修パターン選択 → 検証）コードサンプル付き
- 代替案: Override Property の制約と将来検討（v0.7 候補）

#### 3. ベストプラクティスを 39 → 43 項に拡張
- **新カテゴリ「Phase 4 コンテンツ最適化」（42-43）**
- 既存「事前 audit メタパターン」カテゴリ（40-41）を独立化

#### 4. チェックリストに「Phase 4」セクション追加（5 項目）
- 必要性の判定 / audit / 補修パターン選択 / 補修実行 / 検証

### Phase 1-4 完成形フロー（v0.6 確定）

```
[Step 0] 既存全件 Audit (図全体)
   ↓
[Step 1] Spec md 読み込み
   ↓
[Step 2] Variables / Effect Styles 取得
   ↓
[Step 3] Phase 戦略選択
   ├─ Phase 1 (新規生成)
   ├─ Phase 2 (property 拡張)
   │  ├─ 事前 audit (v0.5)
   │  └─ rename → clone → 配置
   ├─ Phase 3 (参照確立)
   │  ├─ 事前 audit (v0.5)
   │  ├─ Pattern A (placeholder → instance)
   │  └─ Pattern B (instance → instance swap)
   └─ Phase 4 (コンテンツ最適化) ← v0.6 追加
      ├─ audit: innerH vs availableH
      ├─ 補修パターン選択 (VERTICAL / HORIZONTAL / NONE)
      └─ ヘルパー関数で 1 script 補修
   ↓
[Step 4] スクリーンショット検証
   ↓
[Step 5-7] spec md / build-log / current.md 更新 → commit
```

### 学んだこと（追加）

44. **Phase 戦略は線形でなく入れ子**: Phase 1 → 2 → 3 → 4 と進む必要はなく、各 Component の状態に応じて **「Phase 2 を実施したから Phase 4 も必要」のような連動条件** がある。SKILL は **「条件 → Phase 選択」** を明示する設計に進化中。

### SKILL v0.7 候補

- **Phase 2/3/4 事前 audit の自動化 helper script**: 手動 mental simulation を Plugin API 化
- **brand 横展開のパラメータ化**: `brand/<brand>/` パスを変数化
- **Token migration セクション**: 既存 Component の直値 → Variable bind 置換手順
- **Phase 5 提案: テスト**: Component Set を import → 利用シーンで検証する自動テスト

---

## Session 2026-05-12 (#20) — Brand DNA v0.4 反映 draft + Header Liquid 雛形

**契機**: ユーザー指示「A (TOPページ Liquid 実装) と B (Brand DNA v0.4 整備) を同時に進める」。Brand DNA は main repo 別ブランチ管理のため worktree 内に「v0.4 反映 draft」を operations/ に書き出し、Header 実装は worktree 内の `projects/fambox/sections/fambox-header.liquid` として新規生成。

### 成果

| 成果物 | 場所 | 内容 |
|---|---|---|
| Brand DNA v0.4 反映 draft | `operations/2026-05-12-brand-dna-v0.4-draft.md` | 4 Section（Marc 流 4 層スタック / Phase 戦略 / 三位一体 / 6 軸目「Disciplined」）|
| FAMBOX Header section | `projects/fambox/sections/fambox-header.liquid` | 343 行、spec v0.2 準拠の Phase 1 雛形 |

### Brand DNA v0.4 への提案内容（4 Section）

- **A**: 実装規律の Marc 流 4 層スタック（L1 Transport / L2 Skill / L3 Tokens / L4 Definitions / L5 Audit-first）
- **B**: Phase 戦略（1=新規 / 2=拡張 / 3=参照確立 / 4=コンテンツ最適化）の 4 Phase 体系
- **C**: Spec md ↔ Figma Component Set ↔ Build Log の三位一体（DNA 永続化の必須要件）
- **D**: Brand Principle 6 軸目「**Disciplined**」追加（Audit-first を視覚言語と同等の重要度に格上げ）

main repo `brand/fambox/brand-dna/current.md` への正式反映は宮川さん承認後に手動転記。

### FAMBOX Header section の実装範囲（Phase 1）

| 機能 | 実装状況 |
|---|---|
| Variants: standard | ✅ |
| Variants: minimal / mega | v0.3（別 section に分離検討）|
| Heights: compact (64) / default (80) / tall (96) | ✅ schema で選択可 |
| Sticky modes: sticky | ✅（CSS のみで動作）|
| Sticky modes: scroll-up / static | v0.3（JS 追加必要）|
| Logo 左固定 / Menu 中央 / Utilities 右 | ✅ |
| Account / Cart icon（切替可）| ✅ |
| Primary CTA 1 個 | ✅（DNA 規律準拠）|
| SP 横スクロールメニュー（ハンバーガー不採用）| ✅ |
| `data-gtag-*` 属性（GA4 計測継続）| ✅ |
| accessibility (aria-label / focus-visible / reduced-motion) | ✅ |
| Variable bind（`--bg-primary` / `--border-light` / `--color-drive` 等）| ✅ fallback 値付き |
| Schema settings（height / sticky_mode / logo / menu / cta_*）| ✅ |

### 学んだこと（追加）

45. **worktree 内 Liquid 実装は本番テーマへ移植する前提**: `projects/fambox/sections/fambox-header.liquid` は雛形として worktree 内で完成させ、宮川さんが本番 Shopify テーマリポジトリ（OKR 5/29 期限の対象）へ手動移植する。Marc 流 4 層スタックの L1 Transport（git worktree + PR）は **雛形 → 本番** のフローも保持する。

46. **Brand DNA への学習成果反映は main repo 別ブランチ**: design-system は jovial-benz-864b2d ブランチで進めたが、Brand DNA は別ブランチで管理。「**worktree 内の operations/ に draft を残す → 後で本体に手動転記**」は OKR Excel / memory と同じ「**non-disruptive reflection pattern**」（直接書き込まず、PR で永続化された draft を経由）。

### Known TODOs

- Header v0.3: minimal / mega variant の別 section 分離 + scroll-up JS 実装
- Header SP: section.settings から SP 表示制御（Account icon 省略等）
- Brand DNA v0.4 の main repo 反映（手動転記）
- TOPページ実装 Week 2: 主役 Section（Hero / Bento / Plan Card）の Liquid 化

---

## Session 2026-05-12 (#21) — TOPページ Week 2: Hero section Liquid 雛形

**契機**: ユーザー指示「A (Hero Section の Liquid 雛形)」。実装計画書 Week 2 タスク「Hero / 主役 Section の Liquid 化」を着手。Figma Component Set 67:73 の 12 variants（4 variant × 3 height）に対応する **汎用 section** として 1 ファイルで実装。

### 成果

| 成果物 | 場所 | サイズ | 内容 |
|---|---|---|---|
| FAMBOX Hero section | `projects/fambox/sections/fambox-hero.liquid` | 441 行 | 4 variants 汎用 + 3 heights + NBA HOOP モード |

### 実装範囲（Phase 1）

| 機能 | 実装状況 |
|---|---|
| 4 variants 統一 section: video-fullscreen / video-split / image-editorial / minimal-text | ✅ schema dropdown で切替 |
| 3 heights: compact (40vh) / tall (70vh) / full (100vh) | ✅ modifier クラスで CSS 切替 |
| 背景動画: `<video>` autoplay/muted/loop/playsinline | ✅ |
| 背景画像: `image_url`（最大 1920w）+ alt | ✅ |
| video-split: 左右 50% 分割動画 + 4 Corner Icons | ✅ |
| NBA HOOP モード: image-editorial で boolean toggle、タイポ大型重ね | ✅ |
| content alignment: left / center / right | ✅ schema 選択可 |
| Eyebrow / Title (h1) / Sub / Primary CTA / Secondary CTA | ✅ |
| Variable bind（`--bg-primary` / `--color-drive` / `--font-en` 等 fallback 付き）| ✅ |
| `data-gtag-cta` で GA4 連携 | ✅ |
| SP responsive（content padding / btn full-width / corners 縮小）| ✅ |
| `prefers-reduced-motion` で video 非表示 | ✅ |
| Schema settings: variant / height / content_align / is_hoop / images / videos / texts / 2 CTA | ✅ |

### Phase 2 / v0.3 候補

- パララックス JS（動画 / 画像のスクロール連動）
- scroll-cue（任意の下スクロール促進）
- NBA HOOP の詳細レイアウト（eyebrow を画像端に重ね、大型タイポ overflow）
- video の autoplay 抑制（モバイル / 帯域考慮）
- 既存 `fambox-hero-v17-video.liquid`（578 行 / video-split 特化）との統合 or deprecate 判断

### 学んだこと（追加）

47. **「複数 variants を 1 section で扱うか / variant 別に分離するか」の判断軸**: Figma Component Set は variants を 1 Set にまとめるが、Liquid section は **1 ファイル 1 variant** が Shopify エディタとの相性が良い場合もある。Hero では「**4 variants の共通要素が多く、schema 切替で十分機能する**」と判断し 1 section に統合。Header は「3 variants の構造差が大きい」ため v0.3 で別 section 分離検討（Session #20 参照）。判断軸は **「共通要素率 ≥ 60% → 統合、未満 → 分離」**。

### Known TODOs

- Hero v0.3: パララックス / scroll-cue / 既存 v17 統合判断
- TOPページ実装 Week 2 続き: Plan Card 改修、Bento Grid Liquid 化
- TOPページ実装 Week 3-5: Tier 2-4 sections の改修

---

## Session 2026-05-12 (#22) — TOPページ Week 1 残: Subscription Plan Card Liquid 改修

**契機**: 実装計画書 Week 1 残タスク「Subscription Plan Card 改修」を着手。既存 `fambox-subscription-plan.liquid` (506 行 / v0.1 系) は破壊せず、spec v0.2 準拠版を **別ファイル新規** として生成（Marc 流「既存を破壊しない」原則）。

### 成果

| 成果物 | 場所 | サイズ | 内容 |
|---|---|---|---|
| FAMBOX Subscription Plan Card v0.2 | `projects/fambox/sections/fambox-subscription-plan-v0.2.liquid` | 約 450 行 | Card Pattern 継承 + 8 項目 + 2 CTA |

### 実装範囲（Phase 1）

| 機能 | 実装状況 |
|---|---|
| Card Pattern 継承 (`card-standard` / `card-featured`) | ✅ block.settings.is_featured で切替 |
| 8 項目構成（spec §13 v0.3） | ✅ plan_name / price / frequency / meals / customizable / target / features / 2 CTA |
| 価格訴求 (h2 32px Ink、Drive 不使用)| ✅ Anti「煽り 64px」回避 |
| 「おすすめ」バッジ（Drive 背景 + 白テキスト、Section 内で 1 個まで）| ✅ section 内 Lint は未実装（人間運用） |
| CTA × 2（Primary + Ghost）| ✅ Spec §13 Q3 確定 |
| section blocks で複数プラン並列 (limit 6) | ✅ |
| Responsive: PC 3 列 / Tablet 2 列 / SP 1 列 | ✅ |
| Variable bind（fallback 値付き）| ✅ |
| `data-gtag-cta` で GA4 連携 | ✅ |
| Disclaimer（税表記 + 「最低契約期間は FAQ」誘導）| ✅ spec の Anti「カード内に最低契約期間 / 初月特典」を回避 |
| Schema preset: 3 plan（中央を Featured）| ✅ |

### Phase 1 で適用した spec 規律（Anti 回避）

| Anti | 回避方法 |
|---|---|
| 価格 Drive 64px（煽り）| 価格は `--fs-h2` 32px + `--color-ink`、Drive 色は CTA のみ |
| カード内に「最低契約期間」表示 | カード外 disclaimer に「FAQ 参照」誘導のみ |
| カード内に「初月特典」表示 | カード非表示。キャンペーンは別建て |
| 全プランに「おすすめ」バッジ | block.settings.is_featured で 1 個のみ |

### 学んだこと（追加）

48. **「既存実装を破壊しない」Marc 流原則の Liquid 適用**: 既存 `fambox-subscription-plan.liquid` (506 行 v0.1) を上書きせず `-v0.2.liquid` として並行配置。Shopify section の場合、片方を `archive` 移動 / もう片方を `enabled_on` で本番ページ限定 することで衝突回避可能。**v0.3 で v0.1 を deprecate**するタイミングを決めて統合。

### Known TODOs

- v0.3: 既存 v0.1 (506 行) との統合判断 / Featured 1 個以上の Lint 警告 / 推奨対象別の条件分岐
- TOPページ Week 1 完了 → Week 2 へ: Bento Grid Liquid 化 / Hero v17 統合判断

---

## Session 2026-05-12 (#23) — TOPページ Week 2 主役: Bento Grid + Tile Liquid 化

**契機**: 実装計画書 Week 2 主役エリア（fam-voices / fam-item の Bento 化）の前提として、Bento Grid + Tile の汎用 Liquid section を生成。Figma Component Set 91:107 (Grid) + 87:26 (Tile) の双方向参照を Liquid に持ち込む。

### 成果

| 成果物 | 場所 | サイズ | 内容 |
|---|---|---|---|
| FAMBOX Bento section | `projects/fambox/sections/fambox-bento.liquid` | 563 行 | Grid (3 variants) + Tile (4 variants × 5 sizes × featured) 統合 |

### 実装範囲（Phase 1）

| 機能 | 実装状況 |
|---|---|
| **Grid 3 variants** (standard / editorial / autofit) | ✅ section.settings.grid_variant |
| **Tile 4 variants** (standard / glass / image-fill / stat-focus) | ✅ block.settings.tile_variant |
| **Tile 5 sizes** (1×1 / 2×1 / 1×2 / 2×2 / 3×2) | ✅ block.settings.tile_size |
| **Featured** (Drive 2px 枠で主役識別) | ✅ block.settings.is_featured |
| **Gap modifiers** (sm 16 / md 24 / lg 32) | ✅ section.settings.gap_size |
| **Responsive**: PC 12 col / Tablet 6 col / SP 1 col | ✅ |
| Tile クリック化（`<a>` ラップ）| ✅ block.tile_url で切替 |
| Stat-focus の数字 + 単位（22px sub）| ✅ |
| Glass の半透明 overlay (`::before` + opacity 0.3) | ✅ |
| Image-fill の bottom gradient overlay | ✅ |
| Variable bind + GA4 連携 + reduced-motion | ✅ |
| **Schema preset**: Editorial (5 tiles) + Autofit KPI (4 tiles) | ✅ 即配置可能 |

### Phase 1 で適用した spec 規律（Anti 回避）

| Anti | 回避方法 |
|---|---|
| Gap < 16px（密度過剰）| `bento-gap--sm` の最小値を 16px に clamp |
| 全 tile 同 size 並列（強弱なし）| Schema コメントで「主役 2×2 推奨」明記、Lint は v0.3 |
| 全 tile に Featured | block 個別制御 |
| 12 tile 以上 | block `limit: 12` で厳守 |

### Phase 2 候補

- Editorial variant の主構図 Lint（主役 2×2 最低 1 個チェック）
- Glass の 5 階調 modifier（glass--1 〜 5）
- Image fill バインドの強化（responsive sizes）
- Parallax（Glass tile の背景画像）

### 学んだこと（追加）

49. **Grid + Tile の Liquid 統合は 1 section が正解**: Figma では Grid (`91:107`) と Tile (`87:26`) が別 Component Set として双方向参照していたが、**Liquid ではユーザー編集の単位が「Section」で、Grid と Tile が同じ section.blocks に属する方が編集体験が良い**。Figma の参照構造を機械的に Liquid に持ち込まず、**「ユーザー編集単位」に合わせて統合 / 分離を判断する**。

50. **Schema preset で「最初の配置」を spec 準拠にする**: Editorial preset を「2×2 主役 + 1×1 stat + 1×1 + 2×1 + 3×2 主役」の 5 tile で構成し、spec の「対角線パターン A」を **デフォルトで再現**。これにより Shopify エディタの「Section 追加」時点で DNA 準拠の配置が出来上がる。

### Known TODOs

- Bento v0.3: 主構図 Lint / Glass 5 階調 modifier / Parallax / Image fill responsive
- Week 2 続き: fam-voices / fam-item を `fambox-bento.liquid` の preset / block 化で実装
- Week 3-4: 残 Tier 2-3 sections (FAQ / Profile / value-proposition 等)

---

## Session 2026-05-12 (#24) — TOPページ Week 4 前倒し: FAQ + Profile Liquid 化

**契機**: Week 1-2 が高品質に早期完了したため、Week 4 Tier 3 改修の前提（FAQ / Profile Liquid 化）を先行実装。両方とも spec / Figma 完成済（Session #6 で Spec 化、Session #16 で Figma 化）で、**spec → Figma → Liquid の三位一体**を Liquid 側で締結。

### 成果

| 成果物 | 場所 | サイズ | 内容 |
|---|---|---|---|
| FAMBOX FAQ section | `projects/fambox/sections/fambox-faq.liquid` | 292 行 | Carousel variant + 4-8 card scroll |
| FAMBOX Profile section | `projects/fambox/sections/fambox-profile.liquid` | 321 行 | Section variant + Drive 全面塗り |

### FAQ Carousel 実装範囲

| 機能 | 実装状況 |
|---|---|
| Carousel variant (横スクロール 4-8 card) | ✅ |
| Card 構造: Avatar 40 + Q番号 + 質問 + **黒線 32×2** + 回答 + ロゴ | ✅ |
| Q 番号 Poppins SemiBold 24 / 質問 Bold 18 / 回答 Regular 18 Drive | ✅ |
| SP: scroll-snap で 1 枚送り、カード幅 `calc(100vw - 80px)` | ✅ |
| FAMBOX ロゴ：画像 or text fallback | ✅ |
| `tabindex="0"` + `aria-label`（横スクロール領域）| ✅ |
| 4 card の preset | ✅ |

### Profile Section 実装範囲

| 機能 | 実装状況 |
|---|---|
| Section variant (Drive `#FB4C15` 全面塗り) | ✅ |
| Title box: 2px drive-light 罫線 + 72×72 icon 枠 + Poppins 32 white "Profile" | ✅ `border-right` で部分罫線 |
| Profile box 624×517: 背景画像 PC absolute / SP 下配置 | ✅ |
| Name 40px Bold / 肩書 14px Medium / **284×2 drive-light 線** / Bio 14px Regular（全 white）| ✅ |
| Block limit: 3（DNA 規律 "1-3 名"）| ✅ |
| 2 名 preset（大前 恵 + 和田 毅、spec 例文）| ✅ |
| SP: 縦並び + テキスト下に画像 180h | ✅ |

### Spec → Figma → Liquid の三位一体達成

| Component | Spec md | Figma Set | Liquid section |
|---|---|---|---|
| FAQ | ✅ faq.md | ✅ 93:90 | ✅ fambox-faq.liquid |
| Profile | ✅ profile.md | ✅ 96:79 | ✅ fambox-profile.liquid |

これにより、**spec → Figma → Liquid の全 3 媒体に同じ情報が再現可能**（学び 51）。

### 学んだこと（追加）

51. **spec → Figma → Liquid の三位一体は L4 Component で完成形**: Marc 流 4 層スタックは「Spec を一次資料」として、Figma が「視覚的実装」、Liquid が「production 実装」となる三層を**同じ情報量で再現**できる。Session #24 で FAQ / Profile を Liquid 化したことで、**Audit-first の対象が「Spec ↔ Figma ↔ Liquid」の 3 ペア全部**になり、整合性チェックが体系化。

52. **既存 preview-*.html は L4 Component の「DNA 確認の rapid prototype」**: preview-faq.html / preview-profile.html は Spec 化前の DNA 確認用 HTML だった。Spec → Figma → Liquid の三位一体が完成すると、**preview-*.html の役割は「rapid prototype」へ縮小**（spec が一次資料の地位を取る）。preview-*.html は今後「L4 候補の新規 DNA 確認」用途に専念。

### Known TODOs

- FAQ v0.3: Accordion variant (`/pages/faq` 専用、details/summary)
- Profile v0.3: Card variant (About ページ・メンバー一覧用)
- Week 3 着手: fam-spirit / value-proposition / plan-features 改修案策定

---

## Session 2026-05-12 (#25) — TOPページ Week 3: Bento preset で 3 Section を一括解決

**契機**: 実装計画書 Week 3 タスク（fam-spirit / value-proposition / plan-features）を `fambox-bento.liquid` の **preset 追加**で解決。Marc 流 学び 50「Schema preset で『最初の配置』を DNA 準拠に」を実証する。**3 sections の新規ファイル不要、Bento の preset 3 個追加で対応**。

### 成果

| Week 3 タスク | 実装計画書の方針 | 本セッションでの実装 |
|---|---|---|
| fam-spirit | Bento Grid editorial + glass tile | ✅ "FAMBOX Spirit (Editorial)" preset（5 tile / 主役 2x2 + 3x2 + 標準 3） |
| value-proposition | Bento Grid standard + standard tile | ✅ "FAMBOX Value Proposition" preset（6 tile / 主役 2x2 + stat 2 + 横長 + 1x1×2） |
| plan-features | Card Pattern standard Grid | ✅ "FAMBOX Plan Features" preset（6 tile / 1x1 × 6 autofit） |

### 各 preset の DNA 準拠

#### FAMBOX Spirit (Editorial)
- Grid: editorial / gap: lg
- 5 tile: 2x2 主役 (INTEGRITY) + 1x1×2 (CO-DRIVEN / DRIVE) + 2x1 (EDITORIAL) + 3x2 主役 (LAB)
- 対角線パターン A（左上 2x2 → 右下 3x2）
- Glass variant で写真背景 + 半透明 overlay 想定

#### FAMBOX Value Proposition
- Grid: standard / gap: lg
- 6 tile: 2x2 主役 (EXPERTISE 15 年) + 1x1×2 stat-focus (120 名+ / 98%) + 2x1 (全国配送) + 1x1×2 (カスタマイズ / 月次相談)
- 主役 + Stat + Standard の mix で「実績で語る」DNA

#### FAMBOX Plan Features
- Grid: autofit / gap: md
- 6 tile: 1x1 × 6 standard (eyebrow 番号 01-06 で順序明示)
- 「サポート内容を一覧で」フラットなリスト型
- 8 項目超過時は spec の Anti「12 tile 以上禁止」前に分割推奨

### Marc 流 学び 50 の実証

「**Schema preset で『最初の配置』を DNA 準拠に**」が **3 sections 一括解決** で機能。
- Shopify エディタで「FAMBOX Bento」を追加 → preset 5 種から選択 → 即 DNA 準拠の配置が出来上がる
- 各 preset は spec の DNA Anti（gap < 16 / 12 tile 超 / 全 Featured）を踏まない
- block の編集（text / image 差替）で容易にカスタマイズ可能

### 既存 section との関係

| 既存 section | 行数 | 今後の扱い |
|---|---|---|
| `fambox-value-proposition.liquid` | 513 行 | v0.3 で deprecate 判断、`fambox-bento.liquid` の preset で代替 |
| `fambox-plan-features.liquid` | 396 行 | 同上 |
| (fam-spirit は新規 section なし) | — | `fambox-bento.liquid` の preset として新規運用 |

### 学んだこと（追加）

53. **「3 sections 1 file で解決」は Marc 流の効率の極み**: 学び 50（Schema preset で DNA 準拠の初期配置）と学び 49（Liquid のユーザー編集単位）の組合せで、**新規 3 ファイル不要、既存 1 ファイルへの preset 5 行追加 × 3 = 15 行で Week 3 タスク完了**。Phase 1 戦略の「最小コストで最大カバー」を実証。

54. **既存 section の deprecate 判断は preset カバー範囲で決まる**: 既存 `fambox-value-proposition.liquid` (513 行) / `fambox-plan-features.liquid` (396 行) は v0.3 で deprecate 判断するが、判断軸は **「Bento の preset で同等以上の表現ができるか」**。preset がカバーできていれば deprecate、できていなければ統合改修。今回の 3 preset はカバー OK と判断。

### Known TODOs

- Week 3 進捗: 3 sections を Bento preset で解決完了 → 残り Week 5 QA / 本番反映
- Modal / Footer の Liquid 化（残 L4 の Liquid 化で完全カバー）
- Stat Card / Case Study Liquid 化（Tier 1-2 補完）

---

## Session 2026-05-12 (#26) — TOPページ Week 4 残: easy-cooking preset + menu-showcase tokens ガイド

**契機**: 実装計画書 Week 4 Day 22-24 の残タスク 2 件を対応。
- **easy-cooking**: spec で「Hero Section image-editorial tall」と確定 → `fambox-hero.liquid` の preset 追加
- **menu-showcase**: spec で「専用 Pattern 保持、tokens.css 適用のみ」と確定 → operations/ に tokens 適用ガイドを書き出し（本番テーマ転記対象）

### 成果

| 成果物 | 場所 | 内容 |
|---|---|---|
| Hero preset 拡充（4 個追加）| `fambox-hero.liquid` の schema.presets | Video Fullscreen / Video Split / **Easy Cooking** / Minimal Text の即配置 preset |
| menu-showcase tokens 移行ガイド | `operations/2026-05-12-menu-showcase-tokens-migration.md` | 直値 → Variable 置換マッピング表 + 改修フロー |

### Hero preset 4 個の内訳

1. **Video Fullscreen** — TOP 用、FAMBOX × ATHLETES
2. **Video Split (Campaign)** — キャンペーン LP 用、4 Corner Icons
3. **Easy Cooking (image-editorial tall)** — Week 4 Day 23-24 タスク対応、「解凍するだけ、3 分で完成。」+ 2 CTA
4. **Minimal Text (FAQ)** — `compact` height、装飾なし

### menu-showcase の戦略的判断

spec の「構造変更なし、tokens.css 適用のみ」確定方針を踏襲し、**新規 Liquid section 不要**と判断:
- 既存 sections/fambox-menu-showcase.liquid (264 行) は本番テーマリポジトリ管理
- 横スクロール track という独自レイアウトは Bento / Card に収まらない
- 「tokens 適用のみで DNA 準拠化」が最小コストで最大効果

### Tokens 移行ガイドの内容

| カテゴリ | マッピング数 |
|---|---|
| 色（Drive / Ink / Sub / Caption / Placeholder / White / bg-secondary / border-light）| 8 |
| 余白（space-1 〜 7）| 7 |
| Radius（sm / md / pill）| 3 |
| フォント（Hiragino / Poppins + 4 weight）| 6 |
| フォントサイズ（caption / body-sm / body / lg / h3 / h2 / h1）| 7 |
| Shadow（effect style 参照）| 2 |
| **合計** | **33 placement-rule** |

加えて改修フロー（バックアップ / 置換 / fallback 付与 / grep 検証）と注意点（GA4 属性保持等）を明示。

### 学んだこと（追加）

55. **Liquid preset 拡充は L4 単一 section の表現力を桁違いに上げる**: `fambox-hero.liquid` 1 ファイルが 5 preset を持つことで、**Shopify エディタ上では 5 つの異なる Section type に見える**（実装計画書の "Hero / Easy Cooking / FAQ" などが全部 Hero section に集約）。**spec → Figma → Liquid の三位一体の "Liquid 側" は preset 化で最大化**。

56. **Tokens 移行は「構造変更なし」の中で最大の DNA 準拠化手段**: 直値（hex / px）→ Variable 置換だけで、**ライト / ダーク / カスタムテーマ切替に強くなる**、**brand DNA の token 変更が即反映する**、**spec ↔ 実装の整合性が grep で検証可能になる**。menu-showcase のような独自 Pattern でも、tokens 適用だけで DS 整合できる。

### Known TODOs

- Week 4 完了 → Week 5 (QA / 本番反映) 着手
- menu-showcase: 本番テーマでの tokens 適用作業（宮川さん手動転記）
- Modal / Footer / Stat Card / Case Study の Liquid 化（v0.3 候補）

---

## Session 2026-05-14 (#27) — L4 Modal Liquid 化（三位一体達成）

**契機**: 前回 Session #26 の Known TODOs「Modal / Footer / Stat Card / Case Study の Liquid 化」のうち、最も小さく独立性が高い **Modal** から着手。spec md（v0.2）+ Figma Component Set `62:33`（実装済 3 variants）が揃っているため、Liquid 1 ファイル追加で三位一体が完成する状態だった。

### 成果

| 成果物 | 場所 | 内容 |
|---|---|---|
| Modal Liquid section | `sections/fambox-modal.liquid` (672 行) | 3 variants 内包 + JS（ESC/Backdrop/Focus trap）+ 3 presets |
| spec md 更新 | `components/modal.md` | `## Liquid 実装` セクション追加、Change Log に v0.2-liquid 追記 |

### Modal Liquid の設計判断（学び 57 への布石）

**1 section / 3 variants / 3 presets という凝縮**:
- spec の Liquid 実装例（Confirmation / Detail / Sheet）を **1 ファイル**に統合
- `variant` setting + `{% case variant %}` のような分岐ではなく **CSS class `modal-{variant}` で表示制御**
- preset 3 個 = Plan 変更確認 / Case Study 詳細 / SP フィルタの即配置パターン
- → `fambox-hero.liquid` 5 preset 戦略（学び 55）を Modal にも適用

**JS の汎用 API 設計**:
- `window.FAMBoxModal[modalId] = { open, close }` で外部からも呼び出し可能
- `data-modal-trigger="<modalId>"` で宣言的に trigger 設定
- 確定ボタンはカスタムイベント `fambox-modal:confirm` を bubble 発火 → 呼び出し側で `addEventListener` してフォーム送信等に接続
- URL 指定時は `<a>` タグに切替（リンクのまま遷移）

**Accessibility の網羅**:
- `role="dialog"` + `aria-modal="true"` + `aria-labelledby` + `aria-describedby`
- Focus trap（Tab を Modal 内に閉じ込め、Shift+Tab も対応）
- `body.fambox-modal-open` で背景 scroll lock
- 初期 focus を最初の focusable へ、close 後は trigger 要素に復元
- `prefers-reduced-motion: reduce` で transition 無効化

**spec 準拠の Anti 回避**:
- Backdrop opacity 0.6 固定（Glass 4）
- Sheet variant は PC（768px 以上）で Confirmation 風挙動に CSS 切替（spec の Don't「Sheet を PC で使わない」を実装側でガード）
- SP の `.modal__actions` は `flex-direction: column-reverse` で Primary が上
- Modal Detail の max-height: 90vh 厳守（90% 超を防ぐ）

### 検証

- `wc -l`: 672 行
- Schema JSON: valid（settings 14 / presets 3）
- Liquid tag balance: `{% %}` 26 pairs / `{{ }}` 64 pairs / section/style/script 各 1 開閉
- modal-confirmation / modal-detail / modal-sheet クラス: 計 8 箇所登場

### 学んだこと（追加）

57. **Modal は「単一 section に 3 variants + JS API + custom event」で完結する**: spec の Liquid 実装例が 3 つあっても、CSS class 切替 + Liquid 内 if 分岐で**1 ファイル**にまとまる。JS は `window.FAMBoxModal[modalId]` という公開 API + `data-modal-trigger` 宣言で**他の section / カスタム HTML から呼び出し可能**にする。確定アクションは `CustomEvent` で bubble 発火させれば、呼び出し側に **コンテキスト依存の挙動（フォーム送信 / Plan 変更 API / GA4 イベント）** を委ねられる → section は「**Modal の見た目と開閉**」だけに責任を持つ純粋な L4 になる。

58. **三位一体（spec / Figma / Liquid）の Liquid 側完成は spec の "Liquid 実装例" の品質に比例する**: modal.md は Confirmation / Detail / Sheet の Liquid 例を 3 つとも書いてあった → Liquid 化は **コピー & 統合 + JS 肉付け** で済んだ。逆に spec に Liquid 例がない component（Stat Card 等）は、Liquid 化前に spec を補強する必要がある。**spec に Liquid 例を書く投資 = 後の Liquid 化セッションの所要時間を短縮する投資**。

### Known TODOs

- **Footer Liquid 化**: 既存 `fam-footer-v2.liquid` を spec v0.2 の 3 variants（Standard / Minimal / Sitemap）に refactor → `fambox-footer.liquid` 化。ボリューム大のため次セッション。
- Stat Card / Case Study の Liquid 化（spec に Liquid 例追記 → Liquid 化の 2 段階）
- 本番テーマへの移植リハーサル（Week 5 QA 準備）

---

## Session 2026-05-14 (#28) — L4 Footer Liquid 化（三位一体達成）

**契機**: Session #27（Modal）と連続して、Known TODOs の **Footer Liquid 化** に着手。前回判断「既存 `fam-footer-v2.liquid` を refactor」は**並存方式に変更**: fam-footer-v2 は LP 用として保持し、spec v0.2 準拠の新ファイル `fambox-footer.liquid` を**新規追加**するルートで進めた。理由 = 旧ファイルを上書きすると LP の世界観（コーナー SVG 4 枚 + 独自レイアウト）が破壊される / 本番反映前の段階で既存実装を消す必要はない / DS 標準は新ファイルが担う。

### 成果

| 成果物 | 場所 | 内容 |
|---|---|---|
| Footer Liquid section | `sections/fambox-footer.liquid` (665 行) | 3 variants 内包 + `nav_column` block + 3 presets |
| spec md 更新 | `components/footer.md` | `## Liquid 実装` + `## 既存 fam-footer-v2.liquid との関係` 追加、Change Log に v0.2-liquid 追記 |

### 設計判断（学び 59 への布石）

**「refactor」ではなく「並存」を選んだ理由**:
1. fam-footer-v2.liquid は LP / プロモ専用の世界観（コーナー SVG 4 枚）を表現している → 構造刷新で失われる
2. DS 標準（spec v0.2）と LP 用世界観は**役割が違う** → 1 ファイルにまとめるべきでない
3. Week 5 QA / 本番反映の段階で、ページ単位に「どちらの footer を使うか」を判断する自由度を残す
4. 旧ファイルを撤去するコスト > 並存させるコスト（footer は section テンプレート単位で選択可能）

**`nav_column` block の二段構え**:
- 主: Shopify ナビ (`link_list` setting) を選択 → エディタ上で管理しやすい
- 副: `manual_links` textarea（"ラベル|URL" 改行区切り）の fallback → preset で即配置可能
- preset で manual_links を仕込むと、エディタで Shopify ナビを後から設定するだけで切替できる

**SNS の inline SVG 化**:
- 旧実装は `{%- render 'icon', name: 'social-instagram-white' -%}` snippet 依存
- 新実装は 5 種（Instagram / YouTube / note / X / TikTok）を inline SVG で同梱 → **snippet 未配置の本番テーマでも即動作**
- 40×40 円形ボタン + hover で Drive 色 (#FC5214) に切替（spec Q4 準拠）

**Legal URL の settings 化**:
- 旧実装は hard-coded `/policies/privacy-policy` 等
- 新実装は URL settings 3 個（空なら非表示）→ **ストア差替え対応・本番/staging で URL 違っても対応可**

### 検証

- `wc -l`: 665 行
- Schema JSON: valid（settings 18 / blocks 1 type / presets 3）
- preset blocks: Standard 3 / Minimal 0 / Sitemap 4
- Liquid tag balance: `{% %}` 62 pairs / `{{ }}` 66 pairs / footer/section/style 各 1 開閉

### 学んだこと（追加）

59. **既存実装と DS 標準は「並存」が原則。refactor は本番反映の段階で判断する**: 既存の独自世界観 Liquid（fam-footer-v2 のコーナー SVG 4 枚等）を spec 準拠で**置き換える**判断は、ページ単位の用途を理解してから行うべき。**「DS 標準は新規ファイルとして増設」が安全**で、ページ単位の `section` 選択で切替できる Shopify の仕組みを活かせば、旧ファイルを残しても害がない。**spec → Liquid の三位一体は "旧実装の廃止" を必須としない**。

60. **SNS / Legal は snippet 依存 / hard-coded URL を避け、section 内自己完結 + settings 化する**: `{% render 'icon' %}` snippet 依存は**そのテーマに snippet が無いと動かない**。本番テーマや staging で「Footer が壊れる」原因の典型。**inline SVG で自己完結**させ、URL は settings で受ける形にすれば、**section ファイルをコピーするだけで他テーマでも動く**。DS 標準 section の**移植性**が桁違いに上がる。

### Known TODOs

- TOP ページの footer を `fambox-footer.liquid` に切替（Week 5 QA で判断）
- fam-footer-v2.liquid は LP 専用ラベルに整理（コメント追記 or rename 検討）
- Stat Card / Case Study の Liquid 化（spec に Liquid 例追記 → 化の 2 段階）
- 本番テーマへの移植リハーサル（Week 5 QA 準備、※今期スコープ外）

---

## Session 2026-05-14 (#29) — L3 Pattern Stat Card → Stat Grid Liquid 化（三位一体達成）

**契機**: Footer の次は Tier 1-2 補完。stat-card.md は spec §Liquid 実装例が既に 5 パターン書かれていたため、**spec 追記の前段は不要**。直接 Liquid 化に着手。L3 Pattern は単体配置よりも「複数並列で見せる」用途が多いため、Stat Card そのものではなく **Stat Grid** という上位 L4 セクションとして実装した。

### 成果

| 成果物 | 場所 | 内容 |
|---|---|---|
| Stat Grid Liquid section | `sections/fambox-stat-grid.liquid` (454 行) | size 3 × layout 2 + cols range + 3 presets |
| spec md 更新 | `components/stat-card.md` | `## Liquid 実装` 追加、Change Log に v0.2-liquid 追記 |

### 設計判断（学び 61 への布石）

**L3 Pattern を「複数並列で見せる」L4 化**:
- stat-card.md は L3 Pattern なので、本来は単体配置可能（Hero 内 / Card 内 / Bento 内）
- ただし**単独で 1 Stat だけ section に置く実用性は低い** → 複数並列 (KPI Grid) が本命
- Stat Card 1 個 = 1 block、複数 block を grid 配置する section にした
- `cols_pc` (1-6 range) × `cols_sp` (1-3 range) でレイアウト柔軟性を確保

**Anti 厳守の実装**:
- カウントアップ JS なし（静的提示 / spec §Don't 準拠）
- Unit は CSS `font-size: 0.4em` 固定 → schema からは触れない（情報階層を守る）
- Value 色は Drive (#FC5214) 固定（Sky/Deep/Ink 切替不可 / v0.3 課題）
- 1 block = 1 数字（spec §Don't「1 Stat に複数数字を並べない」を block 構造で物理的にガード）

**SP 縮退の自動化**:
- Large (96px) → SP 64px、Default (56px) → SP 48px に CSS で縮退
- horizontal layout は ≤480px で vertical に自動切替（情報密度を保つ）

**Accessibility 強化**:
- `role="list"` / `role="listitem"` で Stat 群を意味的にリスト化
- `sr_prefix` setting で「マイナス」「およそ」等の SR 補助テキストを `<span class="visually-hidden">` で挿入可能（spec §Accessibility 準拠）

### 検証

- `wc -l`: 454 行
- Schema JSON: valid（settings 10 / block_types 1 / presets 3）
- preset blocks: KPI 4 / Big Numbers 3 / Single Stat 1
- Liquid tag balance: `{% %}` 34 pairs / `{{ }}` 47 pairs

### 学んだこと（追加）

61. **L3 Pattern の Liquid 化は「複数並列の L4 化」が現実的な選択肢**: Stat Card は L3 Pattern として「単体で使える」が、**単独で section に置く実用性は低い**。section という単位は「ページに 1 ブロック並ぶもの」が前提なので、L3 Pattern を section 化するなら「複数並べる」前提で **L4 グリッドにラップ**する設計が自然。**1 block = 1 Pattern instance** にすれば、spec §Don't「1 Stat に複数数字」もブロック構造で物理的にガードできる。spec のレベル（L3）と Liquid のレベル（L4 section）はずれていい。

---

## Session 2026-05-14 (#30) — L4 Case Study 3 patterns 統合 Liquid 化（三位一体達成）

**契機**: stat-card と連続して、最後の Tier 1-2 補完 Case Study に着手。spec §レイアウトパターン は 3 patterns (tile-grid / story / logo-list) 想定だが、Figma は 2 variants (tile / story) のみで **logo-list が Figma 未整備**だった。本セッションで Liquid 側だけ先に 3 patterns 全部実装し、Figma 側の logo-list 追加は v0.3 残課題とした。

### 成果

| 成果物 | 場所 | 内容 |
|---|---|---|
| Case Study Liquid section | `sections/fambox-case-study.liquid` (1102 行) | 3 patterns 内包 + 3 block types + 3 presets |
| spec md 更新 | `components/case-study.md` | `## Liquid 実装` + `## 既存との関係` 追加、Change Log に v0.2-liquid 追記 |

### 設計判断（学び 62 への布石）

**3 patterns を 1 file に統合する spec gap 解消**:
- Figma は tile/story の 2 variants（logo-list 不在）
- spec §レイアウトパターン は 3 patterns 想定
- **Liquid 側で 3 patterns 全部実装** → spec ↔ Liquid は 100% 整合、Figma は v0.3 で logo-list 追加して三位一体達成へ
- Liquid 側が**spec ベースの最新仕様を先行実装**する形に（Figma 追従待ち）

**3 block types の使い分け**:
- `case_card` (tile-grid 用): image / meta / team_name / summary / stat_value-unit-label / link_url
- `strategy_point` (story 用): text のみ（食事戦略の各ポイント、Story の中で list 表示）
- `logo_item` (logo-list 用): logo image / team_name（alt + placeholder）
- pattern 切替時に他 block type は自動的に**無視される**（`{% if block.type == ... %}` ガード）

**煽り表現排除の placeholder 整備**:
- spec §トーン規律で「劇的」「絶対」「保証」「優勝」が NG
- **preset / settings の default 値を全て事実ベース表現に統一**
  - ✅「12 ヶ月の継続でコンディションが安定」
  - ✅「シーズン後半でも練習強度を維持」
  - ✅「目に見える変化が出るまでに 3 ヶ月」
- エディタで宮川さんが書き換える時の「お手本」として機能

**カード全体リンク化の動的タグ切替**:
- `link_url` が指定されているカードだけ `<a>` タグに、空なら `<div>` に動的切替
- `{%- assign card_tag = 'div' -%}` → `{%- if block.settings.link_url != blank -%}{%- assign card_tag = 'a' -%}{%- endif -%}`
- 開閉タグを `<{{ card_tag }}>...</{{ card_tag }}>` で出力（Liquid 動的タグ生成パターン）

**Logo List の grayscale + opacity 演出**:
- spec §3 ロゴリストは「社会的証明」用途で**控えめさが正解**
- `filter: grayscale(100%)` + `opacity: 0.7` → hover で復元
- DNA Anti「ブランド借り（有名選手起用のみ）」を避ける = 派手に見せない演出と整合

### 検証

- `wc -l`: 1102 行
- Schema JSON: valid（settings 35 / block_types 3 / presets 3）
- preset blocks: Tile Grid 3 / Story 3 (strategy_point) / Logo List 10
- Liquid tag balance: `{% %}` 120 pairs / `{{ }}` 117 pairs / section 3 開閉（中の `<section>` 含む）/ article 1 開閉

### 学んだこと（追加）

62. **spec ↔ Figma の variants 数がずれている時、Liquid は spec 側を先行実装する**: spec §レイアウトパターン は 3 patterns、Figma は 2 variants という gap があった場合、**Liquid は spec ベースで 3 patterns 全部書く**のが正解。理由 = (1) spec が最新の意思決定を反映している、(2) Liquid は本番反映の唯一の手段で「Figma に無い variant も実装する必要がある」、(3) Figma の追従は別タスクとして残せる。**spec ↔ Liquid の整合性 > spec ↔ Figma ↔ Liquid の三者整合性**。先行実装の判断を Change Log に残せば後で Figma に反映する根拠になる。

63. **DS 標準 section の `placeholder` / `preset` default 値は「お手本」として機能する**: ユーザー（宮川さん）はエディタで書き換えるが、最初に表示される default 文言が**そのままトーンの基準**になる。case-study.md の spec §トーン規律「煽り表現禁止」を実装に落とすには、**preset / settings の default を全て事実ベースに統一**するだけで十分。「劇的」を default に書かなければ、書き換え時にも「劇的」を打たないバイアスがかかる。**DS 標準の規律は preset の文言設計で担保される**。

### Known TODOs

- Figma に Case Study `logo-list` variant 追加（v0.3 / spec gap 解消）
- TOP ページに `fambox-case-study.liquid` 配置（Week 5 QA で判断）
- fam-case-study.liquid を「ブログ記事用」ラベルに整理（コメント追記 or rename 検討）
- Tier 3 以下の component（FormField / Input / Progress / Spinner 等）の Liquid 化判断（必要性が低ければ skip）

---

## Session 2026-05-14 (#31) — Case Study Component Set 66:91 へ logo-list variant 追加（Phase 2 拡張 / spec gap 解消）

**契機**: 前 Session #30 で記録した Known TODOs「Figma に Case Study `logo-list` variant 追加」に着手。spec §14 の 3 patterns（カード一覧 / ストーリー / ロゴリスト）と Figma の 2 variants（tile / story）の **gap を Figma 側で解消**。Liquid 側は Session #30 で先行実装済みのため、本セッションで Figma を spec ↔ Liquid に追従させた。

### 成果

| 成果物 | 内容 |
|---|---|
| `variant=logo-list`（node `118:123`）追加 | Case Study Component Set `66:91` に 3 つ目の variant を追加 |
| Set bounding 拡張 | `66:91` を 1220×1032 → **1220×1372** に明示 resize（layoutMode=NONE は子の overflow を自動補正しないため） |
| 10 logo placeholder | 5 列 × 2 行で配置（200×80 / corner radius 4 / "Team 1〜10" ラベル / Inter Medium 12px） |
| spec md 更新 | `components/case-study.md` の Figma 参照を variants 3 に更新、Change Log に v0.2-figma-logo-list 追記 |

### Phase 2 適用フロー

1. **Audit-first**（SKILL Step 0 / 必須）: `66:91` の現状確認
   - 既存 variants: `variant=tile`（66:50 / 360×458 / x=0, y=0）/ `variant=story`（66:70 / 720×1032 / x=500, y=0）
   - Set: layoutMode=NONE / 1220×1032
   - Property: `variant` = ["tile", "story"]
2. **新規 Component 作成**: `figma.createComponent()` で `variant=logo-list` を生成し `set.appendChild()`
3. **配置**: layoutMode=NONE のため明示位置 `x=0, y=1092`（story 末端 + 60 gap）
4. **Auto Layout 構築**: variant 内部を VERTICAL（2 rows）+ 各 row を HORIZONTAL（5 logo slots）
5. **Set bounding 明示 resize**: 子の `y + h = 1332` + padding 40 = **1372** に Set.resize() で拡張
6. **logo slot サイズ修正**: auto-layout HORIZONTAL を後付けすると resize 値が HUG にリセットされる現象に遭遇 → `primaryAxisSizingMode='FIXED'` + `counterAxisSizingMode='FIXED'` + `layoutSizingHorizontal='FIXED'` の三点セットで明示

### 発生問題と修復

#### 🐛 Issue 13: COMPONENT_SET (layoutMode=NONE) は子の overflow を自動補正しない
- **症状**: Set 66:91 に y=1092 の variant を append しても Set 自体は 1220×1032 のまま → logo-list が Set boundary 外に位置
- **原因**: COMPONENT_SET の layoutMode=NONE は **自由配置モード**。子の bounding box を自動で fold しない
- **修復**: 子の `y + h` を計算して `set.resize(1220, 1372)` で明示拡張
- **再発防止**: SKILL Phase 2 拡張時、layoutMode=NONE の Set に variant を追加する場合は **resize 必須** をチェックリスト化

#### 🐛 Issue 14: auto-layout を後付けすると resize 値が HUG に化ける
- **症状**: 初回スクリプトで `slot.resize(200, 80)` → `slot.layoutMode = 'HORIZONTAL'` の順で実行 → screenshot で slot が縦長に表示
- **原因**: `layoutMode = 'HORIZONTAL'` を呼ぶと、`primary/counterAxisSizingMode` がデフォルト AUTO（HUG）になり、内容（12px text）にフィットして縦長に縮む
- **修復**: 2 段階目スクリプトで `primaryAxisSizingMode='FIXED'` + `counterAxisSizingMode='FIXED'` + `layoutSizingHorizontal/Vertical='FIXED'` を明示してから `resize(200, 80)`
- **再発防止**: auto-layout 設定後の resize は **sizing mode を明示**。`resize → layoutMode → resize` の 2 段階を最初から書く

#### 🐛 Issue 15: Math.max(...arr.map(v => v.y + v.height)) で NaN 発生
- **症状**: spreadした max が NaN を返し、set.resize() で `Property "width" failed validation: Expected number, received nan`
- **推定原因**: スクリプト atomic context で何かの中間値が NaN になった（再現性は低い）
- **修復**: debug script で各 child の x/y/width/height/type を return → 全て正常な number であることを確認 → 明示値 `set.resize(1220, 1372)` で回避
- **再発防止**: Phase 2 で Set サイズ計算する時は、計算式より **観測値ベースの明示値** が安全

### 学んだこと（追加）

64. **COMPONENT_SET の bounding は layoutMode によって挙動が違う**: `layoutMode=VERTICAL/HORIZONTAL` の Set は子の追加で自動拡張するが、**`layoutMode=NONE` の Set は子が overflow しても拡張しない**。Phase 2 で variant を append する時、layoutMode を必ず audit して、NONE なら明示 resize を計画する。学び 9-12 の Layout カテゴリに追加。

65. **auto-layout を後付けする時は sizing mode を明示する三点セット**: `layoutMode='HORIZONTAL'/'VERTICAL'` を後から設定すると、`primaryAxisSizingMode` / `counterAxisSizingMode` が AUTO（HUG）になり、それ以前の resize 値が無効化される。回避策は **(1) `primaryAxisSizingMode='FIXED'`、(2) `counterAxisSizingMode='FIXED'`、(3) `layoutSizingHorizontal/Vertical='FIXED'`** の三点セットを resize の前後で必ず明示。Issue 5 の延長系として SKILL に明記。

66. **spec ↔ Figma の gap 解消は Liquid 先行 → Figma 追従が現実的**: Session #30 で Liquid を spec 準拠の 3 patterns で先行実装し、本セッションで Figma を追従させた。**Liquid → Figma の順は逆方向に見えるが、(1) Liquid の方が「いま動く本番反映物」、(2) Figma 操作は SKILL でスクリプト化されているため後追いが早い、(3) spec ↔ Liquid 整合さえ取れていれば三位一体は時間差で達成可能** → **gap が見つかったら "Liquid を spec に追従させる" → "Figma を spec に追従させる" の 2 段階で OK**。学び 62 の補強。

### Known TODOs

- TOP ページに `fambox-case-study.liquid` 配置（Week 5 QA で判断）
- fam-case-study.liquid を「ブログ記事用」ラベルに整理
- Tier 3 以下の component の Liquid 化要否判断
- Modal / Footer の Figma Component Set Audit 再確認（spec ↔ Figma 整合性 cross-check）

---

## Session 2026-05-14 (#32) — Modal / Footer Component Set Audit 再確認（spec ↔ Figma cross-check）

**契機**: 前 Session #31 で Case Study の spec gap を解消した流れで、Modal / Footer も spec ↔ Figma の整合性を再 audit。Tier 1-2 補完が三位一体達成しているはずだが、**配置や boundary の隠れた問題**がないか cross-check した。

### 成果

| Set | Audit 結果 | アクション |
|---|---|---|
| **Modal `62:33`** | ✅ 全項目 OK（3 variants × 3 sizes × property `variant` × Set boundary 全て整合）| **修正不要**。spec md に `v0.2-audit-ok` を Change Log 追記 |
| **Footer `60:95`** | ⚠️ 3 variants が x=0, y=0 で**重なり**配置 / sitemap が standard と中身同等 | **配置修正 + spec gap 記録**。Set boundary を 1440×329 → 1440×1044 に拡張 |

### Modal Audit 詳細（✅ 修正不要）

```
Set: 62:33 "Modal" / 2200×345 / layoutMode=NONE
Variants:
  - variant=confirmation (62:5)  400×219, x=0,    y=0
  - variant=detail       (62:13) 800×236, x=500,  y=0
  - variant=sheet        (62:21) 800×345, x=1400, y=0
Property: variant = ["confirmation", "detail", "sheet"]
```

3 variants が水平方向に並んで配置済み、各サイズは spec の **max-width 規律**（confirmation 400 / detail 800 / sheet 100%）と整合。Set boundary 2200×345 も全 variants 内包済み。

### Footer Audit 詳細（⚠️ 修正実施）

**Before**:
```
Set: 60:95 "Footer" / 1440×329 / layoutMode=NONE
Variants（全て x=0, y=0 で重なり）:
  - variant=standard (60:5)  1440×329, x=0, y=0
  - variant=minimal  (60:44) 1440×226, x=0, y=0  ← 重なり
  - variant=sitemap  (60:56) 1440×329, x=0, y=0  ← 重なり
```

**After**:
```
Set: 60:95 "Footer" / 1440×1044 / layoutMode=NONE
Variants:
  - variant=standard (60:5)  1440×329, x=0, y=0
  - variant=minimal  (60:44) 1440×226, x=0, y=389  (329+60 gap)
  - variant=sitemap  (60:56) 1440×329, x=0, y=675  (389+226+60 gap)
```

### Footer の spec gap 発見（v0.3 残課題）

screenshot で確認した結果、**Figma 上の sitemap variant の中身が standard と実質同等**。spec § Variants では Sitemap = 「Standard + 詳細 Sitemap（多列カテゴリ・4 列）」。

| Layer | Standard | Sitemap | spec 想定 |
|---|---|---|---|
| Liquid | `.footer__nav` 3 列 | `.footer-sitemap .footer__nav` **4 列**（CSS で差別化済）| 4 列 |
| Figma | Nav 3 列 | Nav 3 列（standard と同じ）| 4 列にすべき |

→ **spec ↔ Liquid は整合、spec ↔ Figma に gap**。Liquid 先行実装と同じ構図（学び 66）。**v0.3 で sitemap variant を 4 列に再構築**する Known TODO として記録。

### 学んだこと（追加）

67. **三位一体達成済の component でも、再 Audit すると配置 / boundary / 細部整合性の隠れた問題が見つかる**: Modal / Footer は前々回（#28 / #27）に spec ↔ Liquid を整合させていたが、**Figma 側の配置（variants 重なり）と内容差別化（sitemap 4 列化）の 2 つの問題**が再 audit で発覚。**「三位一体達成」は spec / Figma / Liquid の 3 層の "存在" が揃った状態であり、"完璧性" は別**。**周期的な cross-check audit** を組み込むことで、後から見つかる小さな整合性問題を早期に拾える。再 audit の所要時間は 1 component あたり数分程度。

68. **spec ↔ Figma の gap は「片方が正解、もう一方が追従するべき」と判断する**: Footer sitemap の 4 列化問題は、**spec が正、Figma が追従するべき**（Liquid は既に追従済み）。逆に Case Study の logo-list は **Liquid が先行、Figma が追従**（Session #31）。**3 層のうちどこに最新の意思決定が反映されているかを毎回判断し、他 2 層を追従させる**のが gap 解消の基本ルール。仕様 = spec / 動作 = Liquid / 視覚 = Figma の役割を意識する。

69. **layoutMode=NONE の Component Set で variants を append すると同位置に重なる典型ケースが Issue 4 系の再発**: 学び 24, 26 で記載済の「1D 拡張 = 既存 variants の縦/横並びパターンを inspect で確認、その規則を踏襲」。Footer は Figma 初期生成時の append 時点で variant 配置を怠っていたと推定される（過去の SKILL 適用前の手作業生成？）。新規 variant 追加だけでなく **既存 Set の Audit でも variant 配置の重なりチェック**を含めるべき。Issue 4 の延長として「Phase 0 Audit-first チェックリスト」に追加候補。

### Known TODOs

- **Footer sitemap variant の 4 列化**（v0.3 / spec ↔ Figma gap 解消）
- TOP ページに新 sections 配置判断（Week 5 QA）
- fam-footer-v2 / fam-case-study を「LP/ブログ専用」ラベルに整理
- Tier 3 以下（FormField / Input / Progress / Spinner）の Liquid 化要否判断
- 他 component の周期 Audit（Header / Hero / Plan Card / Bento / FAQ / Profile）

---

## Session 2026-05-14 (#33) — Footer sitemap variant 4 列化（spec ↔ Figma ↔ Liquid 完全整合）

**契機**: Session #32 で発見した Footer sitemap の spec gap（Liquid は 4 列 / Figma は 3 列）を解消。Phase 2 拡張ではなく **Component 内部構造の追加**（既存 column の clone + 文言入れ替え）で対応。

### 成果

| 操作 | 内容 |
|---|---|
| BUSINESS column 追加 | sitemap variant 60:56 の Nav container 60:62 に 4 列目を追加（`129:123`）|
| 文言入れ替え | BUSINESS / 法人向けプラン / 導入事例 / パートナー |
| spec md 更新 | `components/footer.md` に v0.3-figma-sitemap + 4 列構造表追加、Known TODOs から解消 |

### 実装フロー（既存 column clone パターン）

1. **Audit**: sitemap 60:56 の構造を walk → Nav container 60:62 内に 3 columns（PRODUCTS 60:63 / COMPANY 60:68 / SUPPORT 60:73）を確認
2. **Font 検出**: 既存 PRODUCTS column の各 text の fontName を Set で収集して `loadFontAsync`
3. **Clone**: `productsColumn.clone()` でテンプレ複製
4. **append**: Nav container は HORIZONTAL auto-layout なので `appendChild` で自動末尾配置（x=398, gap 48）
5. **文言入れ替え**: clone 内の TEXT node 4 つ（見出し + 3 リンク）を順に書き換え

結果: BUSINESS column が x=398, w=98, h=111 で配置、Nav container 928×111 内に収まる。

### 設計判断: BUSINESS 文言の決定理由

spec の Liquid Sitemap preset は `ABOUT / PRODUCTS / SUPPORT / BUSINESS` だが、**Figma 既存の見出しは PRODUCTS / COMPANY / SUPPORT** という日本語ストア構成。既存 3 列の見出しを書き換えず、4 列目だけ追加する非侵襲アプローチを採用:

- 既存変更なし: PRODUCTS / COMPANY / SUPPORT
- 4 列目追加: **BUSINESS**（法人向けプラン / 導入事例 / パートナー）

Liquid 側の preset は default 値であり、エディタで自由に書き換え可能なため、**Figma の見出しと Liquid の preset が 100% 一致する必要はない**（学び 63 と整合）。

### TEXT node 防御コード（Issue 16 再発防止）

audit script で `node.layoutMode` / `node.children` を TEXT node に直接 access して TypeError が連続発生（2 回）。最終的に `'layoutMode' in node` / `'children' in node` の **in 演算子 check** で解決。Issue として記録:

#### 🐛 Issue 16: walk スクリプトで TEXT node の属性アクセスで TypeError
- **症状**: `node.layoutMode: no such property 'layoutMode' on TEXT node`、続いて `node.children: no such property 'children'`
- **原因**: `null` への OR フォールバック (`node.layoutMode || null`) は **property 自体が存在しない**場合は getter のエラーが先に発生する。TEXT node は LayoutMixin / ChildrenMixin を実装していない
- **修復**: `'<key>' in node` で属性存在を check してから access
- **再発防止**: 汎用 walk スクリプトの defensive helper を SKILL に追加候補。Issue 16 として「Component / Frame と TEXT / VECTOR の MixIn 差異」を記載

```js
// ❌ Bad: getter throws on TEXT
out.layoutMode = node.layoutMode || null;

// ✅ Good: check existence first
if ('layoutMode' in node) out.layoutMode = node.layoutMode;
```

### 学んだこと（追加）

70. **Component 内部構造の追加は「既存 child の clone + 文言入れ替え」が最速**: 新規 Component / variant 生成ではなく、**既存と同じ構造を持つ child を clone して中身だけ書き換える**。フォント / spacing / 色 / auto-layout 全てが自動継承され、文言だけ 4 行入れ替えれば終わる。10 分タスク。新規ゼロベース実装と比較して **5-10 倍速い**。既存 design system に追加するときの黄金パターン。学び 19-20 の Instance/再利用 カテゴリに追加。

71. **「spec の preset 文言」と「Figma の見出し」は完全一致を求めない**: Liquid preset は **default 値** に過ぎず、エディタで書き換えられる。Figma 側は**既存ストアの実際の見出し**に合わせるのが自然（ユーザーの認知負荷を増やさない）。**spec / Figma / Liquid の三位一体は "構造" の整合性であって "文言" の完全一致ではない**。3 層で文言が違っても、構造（カラム数 / 階層 / property 名）が揃っていれば三位一体達成。学び 63 の補強。

72. **TEXT / VECTOR / ELLIPSE 等の non-container node は LayoutMixin / ChildrenMixin を持たない**: 汎用 walk スクリプトで属性 access する時、container node（FRAME / COMPONENT / COMPONENT_SET / GROUP / SECTION / INSTANCE）と非 container node の区別を意識する。**`'<key>' in node` で属性存在を確認**してから access するか、container 系の type を allowlist で filter する。

### Known TODOs

- TOP ページに新 sections 配置判断（Week 5 QA）
- fam-footer-v2 / fam-case-study を「LP/ブログ専用」ラベルに整理
- Tier 3 以下（FormField / Input / Progress / Spinner）の Liquid 化要否判断
- 他 component の周期 Audit（Header / Hero / Plan Card / Bento / FAQ / Profile）

---

## Session 2026-05-14 (#34) — 7 Component Sets 一括 Audit（全件 OK 確認）

**契機**: Session #32-33 で Footer に隠れた問題（variants 重なり / sitemap 3 列）が見つかった経験から、**Tier 1 component の周期 Audit** を実施。1 スクリプトで 7 set 一括 audit する効率的フローを確立。

### Audit 結果サマリ（7/7 OK）

| # | Set | ID | Variants | 配置 / 配置規則 | 状態 |
|---|---|---|---|---|---|
| 1 | Header | 59:33 | 3 (standard / minimal / mega) | 全 1440×80, y=0/120/240（gap 40 縦並び）| ✅ OK |
| 2 | Hero Section | 67:73 | **12** (variant 4 × height 3) | 4×3 matrix（COL 1500 × ROW 750）| ✅ OK |
| 3 | Subscription Plan Card | 65:110 | 2 (standard / featured) | 320×587, x=0/400（横並び）| ✅ OK |
| 4 | Bento Grid | 91:107 | 3 (standard / editorial / autofit) | 横並び（standard 936 → editorial 1160 → autofit 936）| ✅ OK |
| 5 | Bento Tile | 87:26 | **40** (variant 4 × size 5 × featured 2) | 完全 3D matrix（最大 4900×2000）| ✅ OK |
| 6 | FAQ | 93:90 | 1 (carousel) | 1440×560 単独 | ✅ OK（spec 想定通り）|
| 7 | Profile | 96:79 | 1 (section) | 1440×760 単独 | ✅ OK（spec 想定通り）|

**累計 variants**: 3 + 12 + 2 + 3 + 40 + 1 + 1 = **62 variants** すべて整然配置。重なり 0 件 / overflow 0 件 / property 名 spec 完全整合。

### 一括 Audit スクリプトの設計

7 set を 1 スクリプトで for-loop して以下 3 軸を観測:

```js
// Axis 1: variant 配置の重なり検出
const posCount = {};
variants.forEach(v => { posCount[`${v.x},${v.y}`] = (posCount[`${v.x},${v.y}`] || 0) + 1; });
const overlapping = Object.entries(posCount).filter(([k, n]) => n > 1);

// Axis 2: Set boundary overflow 検出
const maxRight = Math.max(...variants.map(v => v.x + v.w));
const maxBottom = Math.max(...variants.map(v => v.y + v.h));
const overflow = { right: Math.max(0, maxRight - setW), bottom: Math.max(0, maxBottom - setH) };

// Axis 3: property definitions の取得
const propDefs = reloaded.componentPropertyDefinitions;
```

返り値は `overlapping: null` / `overflow: null` であれば OK。**異常検出が `!= null` 条件で書ける**ので、後続 audit を自動化しやすい構造。

### Hero と Bento Tile の matrix 整然配置を確認

Hero（12 variants）と Bento Tile（40 variants）は **2D / 3D matrix 配置**で複雑だが、x/y 計算が完全に整然:

**Hero（4 variant × 3 height）**:
- variant 軸: video-fullscreen (x=0) / video-split (x=1500) / image-editorial (x=3000) / minimal-text (x=4500)
- height 軸: compact (y=0) / default (y=750) / tall (y=1500)
- 全 12 variants が 1440×{400|550|700} で配置済

**Bento Tile（4 variant × 5 size × 2 featured）**:
- featured=false: x 0/600/1200/1800 (variant 4 軸)
- featured=true:  x 2500/3100/3700/4300 (featured 軸で 700 offset)
- size 軸: 1x1 y=0 / 2x1 y=400 / 1x2 y=800 / 2x2 y=1200 / 3x2 y=1600

学び 24, 26 の「2D matrix layout は COL×ROW で機械的に配置」を完璧に実装している。**過去セッション（#9-19）で SKILL 適用済**の Set はその後も整然性が維持されている → SKILL の効果が観測できる。

### 学んだこと（追加）

73. **三位一体達成済の Set は SKILL の effect が継続して観測できる**: Hero（12v）/ Bento Tile（40v）/ Plan Card（2v）等、**過去に SKILL Phase 1-3 で生成された Set は数 ヶ月後の Audit でも 100% 整然**。逆に Footer のような **SKILL 適用前に手作業で作られた Set は重なり / 差別化不足 / property 不整合が残る**。「**Audit で問題が出るのは SKILL 適用前の遺産**」が経験則として成り立つ。次世代の Audit は「SKILL 適用日」を tag として記録すると、優先 audit 対象を絞り込める。

74. **一括 Audit スクリプトは "異常を null で表現" すると後続自動化が容易**: `overlapping: null` / `overflow: null` のように **OK 状態を null** で表現すると、`results.filter(r => r.overlapping || r.overflow)` で異常 set だけ抽出できる。さらに **threshold（例: overflow > 10px は警告）** を加えれば段階的 audit が可能。次回以降の Audit セッションでは、本スクリプトを `figma-component-from-spec` SKILL の Step 0 audit テンプレに昇格させる候補。

### Known TODOs

- 一括 Audit スクリプトを SKILL Step 0 の audit テンプレに昇格（既存ロジックの再利用化）
- TOP ページに新 sections 配置判断（Week 5 QA）
- fam-footer-v2 / fam-case-study を「LP/ブログ専用」ラベルに整理
- Tier 3 以下（FormField / Input / Progress / Spinner）の Liquid 化要否判断
- Drawer (Header 派生?) / Contact Form Set の Audit（残 Tier 1-2 完了）

---

## Session 2026-05-14 (#35) — SKILL.md を v0.7 に昇格（一括 Audit を Step 0.5 として正式化）

**契機**: Session #34 の Known TODOs「一括 Audit スクリプトを SKILL Step 0 audit テンプレに昇格」に着手。Session #32-34 で 3 連続で価値を発揮した一括 Audit スクリプトを、**SKILL.md 内部に Step 0.5 として正式化** + **チェックリスト統合** + **frontmatter / Issue / 学びカウンタ更新**を実施。

### 成果

| 編集箇所 | 内容 |
|---|---|
| frontmatter `version` | 0.6 → **0.7** |
| frontmatter `last_updated` | 2026-05-12 → 2026-05-14 |
| frontmatter `description` | 「周期 cross-check Audit」trigger を追加 |
| frontmatter `origin` | v0.7 で蓄積した 18 学び（57-74）+ 4 Issue（13-16）を反映 |
| **Step 0.5 新設**（line 54-144）| 詳細 Audit テンプレ（**88 行**）を新規追加 |
| `## 既知の罠` タイトル | (Issue 1-7) → **(Issue 1-16)** + v0.7 注追記 |
| `## ベストプラクティス` タイトル | (学び 1-20) → **(学び 1-74)** + 主要 v0.7 追加学び 7 個を bullet で記載 |
| チェックリスト 新設 | Step 0.5 詳細 Audit 用の 6 項目 |
| チェックリスト Phase 1 拡張 | Step 0.5 を実施した行を追加 |
| チェックリスト Phase 2 拡張 | auto-layout 後付け時の sizing mode 三点セット項目を追加（Issue 14 回避） |
| 行数 | 610 → **727 行**（+117 行） |

### Step 0.5 の内容

```
- 一括 Audit スクリプト（30 行程度）
- 3 軸観測（重なり / overflow / property defs）
- 異常を null で表現する設計（学び 74）
- 結果の解釈ガイド（OK / Issue 4 系再発 / Issue 13 系再発）
- spec ↔ Figma の cross-check ルール（学び 68）
- defensive コード（Issue 16: 'key' in node check）
```

「使うタイミング」を明示:
1. 新規実装の前に既存 Set との整合確認
2. 三位一体達成済の Set に対する周期 audit
3. 複数 Set を一括で audit

### チェックリスト「Step 0.5」項目（v0.7 新設）

```
- [ ] variantCount と spec md の Variants 数が一致
- [ ] properties[].variantOptions と spec の variant 名が完全一致
- [ ] overlapping: null（Issue 4 / 69 系再発なし）
- [ ] overflow: null（Issue 13 系の resize 忘れなし）
- [ ] layoutMode=NONE の Set は子の y+h が Set.height 以内（学び 64）
- [ ] cross-check で gap が見つかった場合、spec/Liquid/Figma の最新を判断して追従（学び 68）
```

### 設計判断: 学び・Issue の本文は build log 側に温存

学び 21-74 と Issue 13-16 の**本文（症状 / 原因 / 修復 / 再発防止）は figma-build-log.md 側にのみ記載**し、SKILL.md には**タイトルとカウンタ更新のみ**反映。理由:

1. SKILL.md を**短く保つ**（既に 727 行 / これ以上膨らむと運用負担）
2. 学び本文は**セッション履歴と紐づいて意味を持つ**（build log の方が文脈豊か）
3. SKILL.md は**手順書**としての性質を維持（参照リンクで build log に飛ばす）

代わりに SKILL.md には **「主要な v0.7 追加学び 7 個」**を bullet で並べる早見表を `## ベストプラクティス` 直下に配置。次に SKILL を読む人が **どの学びが新しいか** を一目で把握できる。

### 学んだこと（追加）

75. **SKILL は「手順書 + カウンタ + 早見表」の 3 層で運用すると膨張せず継続可能**: 学び 21+ / Issue 13+ は build log 側に温存し、SKILL は **タイトル更新 + 早見表 + 参照リンク**で十分。SKILL の役割は「次の人がすぐ実行できる手順書」であり、学びの**ストック**は build log。SKILL に学びの**フロー（最新ハイライト）**を入れることで、両者が補完関係になる。継続セッションでも SKILL は線形に膨張しない設計。

76. **チェックリスト追加は v0.X ラベルで version 履歴を埋め込む**: 「Step 0.5 詳細 Audit — v0.7 追加」のように **追加 version を section タイトルに書く**ことで、SKILL を読む人が **新規 vs 既存 手順**を即区別できる。Phase 1-4 のチェックリストも `v0.5 必須` / `v0.6 追加` 等の tag を付け継続。同様に **コード snippet の冒頭コメント**にも「v0.7 追加」を入れる規律を継続。

### Known TODOs

- TOP ページに新 sections 配置判断（Week 5 QA）
- fam-footer-v2 / fam-case-study を「LP/ブログ専用」ラベルに整理
- Tier 3 以下の Liquid 化要否判断
- Drawer / Contact Form Set の Audit（Step 0.5 を実戦投入）
- SKILL v0.8 候補: テストフェーズ（Phase 5）/ brand 横展開のパラメータ化

---
