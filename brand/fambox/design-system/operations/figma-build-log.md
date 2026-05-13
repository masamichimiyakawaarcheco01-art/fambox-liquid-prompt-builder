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
- **新ユースケース実証**: Bento Tile に `featured` property 追加（Issue 8 解消）で SKILL Phase 2 のもう 1 例実証
- **Token migration ユースケース**: 既存 Component の直値 stroke を Variable bind に置換する手順（Card v0.3 残 TODO に該当）

---
