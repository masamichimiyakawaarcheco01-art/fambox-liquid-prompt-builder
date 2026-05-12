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
