# Design Wheel Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 非デザイナーが70%品質の成果物を作れるよう、デザインパターンを"在庫"として体系化・蓄積するホイールの基盤を作り、パイロット1パターン（corporate）を Sense→Systematize→Generate→Learn で端から端まで貫通させる。

**Architecture:** リポジトリの「パターンパック」(`docs/design-wheel/patterns/<p>/SYSTEM.md`) を唯一の真ソースとする。Claude Design は画像→体系の抽出ワークベンチ（使い捨て・組織1公開制約に非依存）、figma-bridge は SYSTEM.md を読む出力エンジン、critique-log は学習蓄積。既存の `brain/45_Design_Refs/` と `/design-ref` スキルを Sense 層として流用する。

**Tech Stack:** Markdown（ドキュメント真ソース）/ Claude Design（抽出）/ figma-bridge MCP（Figma構築）/ `/design-ref` スキル / git。

**検証の考え方（このプロジェクト特有）:** コードではなくドキュメント＋Figma成果物のため、TDDの「テスト」は (a) 必須セクションの grep 検証、(b) 生成物の read-back 検証、(c) CRITIQUE-RUBRIC 採点に置き換える。「保存しました」だけの報告は禁止（[[feedback_file_verification]]）。

**人間ゲート:** Pinterest収集（Task 6）・Claude Design操作（Task 7）・Figma目視（Task 9）はユーザー操作を含む。該当ステップに 🧑 を付す。AIは指示書・テンプレ・採点・索引化を担当。

---

## File Structure

| ファイル | 責務 | Task |
|---|---|---|
| `docs/design-wheel/README.md` | ハブのインデックス・目的・運用ルール・パターン一覧 | 1 |
| `docs/design-wheel/PATTERN-SCHEMA.md` | SYSTEM.md の標準スキーマ（全パック共通の型） | 2 |
| `docs/design-wheel/CRITIQUE-RUBRIC.md` | 6観点採点・70%到達判定基準 | 3 |
| `docs/design-wheel/LOOP.md` | 4フェーズ手順書（具体コマンド・MCP・チェックリスト） | 4 |
| `brain/45_Design_Refs/_index.md` | `wheel-pattern` 列を追加 | 5 |
| `brain/45_Design_Refs/README.md` | `wheel-pattern:` タグ軸の説明を追記 | 5 |
| `docs/design-wheel/patterns/corporate/refs.md` | corporate refs 索引 | 6 |
| `docs/design-wheel/patterns/corporate/SYSTEM.md` | corporate の真ソース（抽出蒸留） | 7 |
| `docs/design-wheel/patterns/corporate/figma-recipe.md` | figma-bridge ビルド手順 | 8 |
| `docs/design-wheel/patterns/corporate/critique-log.md` | レビュー履歴・学び | 9 |

---

## Task 1: ハブ README.md

**Files:**
- Create: `docs/design-wheel/README.md`

- [ ] **Step 1: 受け入れ基準を確認**

このファイルは grep で次を含むこと: `## 目的`, `## パターン一覧`, `## 運用ルール`, `corporate`。

- [ ] **Step 2: ファイル作成**

```markdown
# Design Wheel

> 非デザイナーが **70%以上の品質のデザイン成果物**を素早く作れるようにするための、
> デザインパターン在庫を体系化・蓄積する仕組み。FAMBOX Flywheel の Purpose（D-015）を
> 多パターン対応へ一般化したもの。FAM BOX とは独立。

## 目的

`幾何学 / コーポレート / グリッド / デジタル / スポーティ / Lab` 等のパターンを、
Pinterest収集 → Claude Design体系化 → Figma別UI生成 → レビュー学習 のループで
"在庫"として積み上げ、誰でもパターンを選べば7割の土台が出る状態を作る。

## アーキテクチャ（案A）

\`\`\`
Pinterest画像 → Claude Design（抽出＋Web即プレビュー）→蒸留→ patterns/<p>/SYSTEM.md（真ソース）
                                                                  → figma-bridge → Figma 7割構築 → レビュー → SYSTEM.md改訂
\`\`\`

- **真ソース** = `patterns/<p>/SYSTEM.md`（git版管理）。Claude Design は使い捨て抽出、Figma は出力。
- Claude Design の `Publish`（組織1公開制約）は在庫管理に使わない。

## パターン一覧

| パターン | ステータス | パック |
|---|---|---|
| corporate | 🟡 パイロット進行中 | [patterns/corporate/](patterns/corporate/) |
| geometric | ⬜ 未着手 | — |
| grid | ⬜ 未着手 | — |
| digital | ⬜ 未着手 | — |
| sporty | ⬜ 未着手 | — |
| lab | ⬜ 未着手 | — |

## ファイル構成

- `LOOP.md` — 4フェーズ手順書
- `PATTERN-SCHEMA.md` — SYSTEM.md の型
- `CRITIQUE-RUBRIC.md` — レビュー・70%判定
- `patterns/<p>/` — 各パターンのパック（SYSTEM.md / refs.md / figma-recipe.md / critique-log.md）

## 運用ルール

1. 1パターンずつループを貫通させてから次へ（YAGNI）。
2. `SYSTEM.md` が唯一の真ソース。Claude Design 出力は必ず蒸留して取り込む。
3. 生成物は read-back 検証＋ルーブリック採点してから「完了」と報告する。
4. 既存 `brain/45_Design_Refs/` を壊さない（`wheel-pattern:` タグで共存）。

## 関連

- FAMBOX Flywheel: `docs/okr/fambox-flywheel/`
- Design Refs: `brain/45_Design_Refs/` ＋ `/design-ref` スキル
- 設計仕様: `docs/superpowers/specs/2026-06-09-design-wheel-design.md`
```

- [ ] **Step 3: 検証**

Run: `grep -E "## 目的|## パターン一覧|## 運用ルール|corporate" docs/design-wheel/README.md`
Expected: 4行以上ヒット。

- [ ] **Step 4: コミット**

```bash
git add docs/design-wheel/README.md
git commit -m "docs(design-wheel): ハブ README（目的・アーキ・パターン一覧）"
```

---

## Task 2: PATTERN-SCHEMA.md

**Files:**
- Create: `docs/design-wheel/PATTERN-SCHEMA.md`

- [ ] **Step 1: 受け入れ基準**

grep で7セクション見出しを含むこと: `Identity`, `Color`, `Type`, `Layout`, `Components`, `Motion`, `DO / DON'T`。

- [ ] **Step 2: ファイル作成**

```markdown
# PATTERN-SCHEMA — SYSTEM.md 標準スキーマ

全パターンの `SYSTEM.md` はこの型に従う。figma-bridge が機械的に読め、
パターン間で比較できるようにするため、見出しと順序を固定する。

---

## 1. Identity
- **パターン名**: <例: corporate>
- **一言定義**: <そのパターンの世界観を1文で>
- **代表ref 3枚**: `brain/45_Design_Refs/...` への相対リンク × 3

## 2. Color
役割別トークン（HEX）。役割名は固定:
| 役割 | 値 | 用途 |
|---|---|---|
| bg | #______ | 画面背景 |
| surface | #______ | カード/面 |
| ink | #______ | 主テキスト |
| ink-muted | #______ | 副テキスト |
| accent | #______ | 強調/CTA |
| line | #______ | 罫線/境界 |

**ゾーニング規則**: <どの面にどの色を使うか。例: 背景bg / カードsurface / CTAaccent>

## 3. Type
- **書体方針**: <日本語/英語フォントの方針>
- **6段スケール**: 飾り __px / 大H1 __px / H2 __px / H3 __px / Body __px / Small __px
- **ジャンプ率**: 低 / 中 / 高 のどれか＋理由
- **行間**: __

## 4. Layout
- **グリッド**: __列 / ガター __px
- **整数比**: <例: 2:3 のレイアウト比>
- **余白 S/M/L（等比）**: S __ / M __ / L __（比率 1.5x or 2x）

## 5. Components
| 要素 | 角丸 | 影 | 状態 |
|---|---|---|---|
| ボタン | __px | __ | hover/disabled |
| カード | __px | __ | — |
| ヘッダ | — | __ | — |

## 6. Motion（任意）
- **速度**: __s
- **イージング**: __

## 7. DO / DON'T
- ✅ DO: <そのパターンらしさを保つ要素>
- ❌ DON'T: <壊す禁止事項>
```

- [ ] **Step 3: 検証**

Run: `grep -E "Identity|Color|Type|Layout|Components|Motion|DO / DON'T" docs/design-wheel/PATTERN-SCHEMA.md`
Expected: 7セクションすべてヒット。

- [ ] **Step 4: コミット**

```bash
git add docs/design-wheel/PATTERN-SCHEMA.md
git commit -m "docs(design-wheel): PATTERN-SCHEMA（SYSTEM.md 標準スキーマ）"
```

---

## Task 3: CRITIQUE-RUBRIC.md

**Files:**
- Create: `docs/design-wheel/CRITIQUE-RUBRIC.md`

- [ ] **Step 1: 受け入れ基準**

grep で `8.5` と `構造系` と 6観点すべてを含むこと。

- [ ] **Step 2: ファイル作成**

```markdown
# CRITIQUE-RUBRIC — レビュー観点と 70%到達判定

生成した Figma を参照（45_Design_Refs / Claude Design プレビュー）と比較し採点する。

## 6観点 × 各0〜2点（満点12）

| # | 観点 | 0点 | 1点 | 2点 | 構造系 |
|---|---|---|---|---|---|
| 1 | 色ゾーニング | 役割が崩壊 | 一部ズレ | トークン通り | ★ |
| 2 | タイポ階層・ジャンプ率 | 階層不明 | 弱い | 明快 | ★ |
| 3 | グリッド整列 | 不揃い | 一部ズレ | 整列 | ★ |
| 4 | コンポーネント一貫性 | バラバラ | 一部 | 一貫 | |
| 5 | 余白リズム | 等差/破綻 | 一部 | 等比リズム | ★ |
| 6 | パターンらしさ | 別物 | 近い | そのもの | |

## 70%到達（= パターン昇格条件）

- 合計 **≥ 8.5 / 12**（≒70%）**かつ**
- 構造系観点（1色ゾーニング / 2タイポ階層 / 3グリッド / 5余白）に **0点が無い**。

## 採点対象外（人間の3割仕上げ領域）

- フォント実体（figma-bridge は Inter固定 → [[feedback_figma_bridge_text_limitations]]）
- 写真・実画像の差込
- 上記は critique-log に「人間仕上げメモ」として別枠記録する。

## 記録フォーマット（critique-log.md に貼る）

\`\`\`
## v<n> 採点 YYYY-MM-DD
| 観点 | 点 | コメント |
|---|---|---|
| 1 色ゾーニング | _/2 | |
| 2 タイポ階層 | _/2 | |
| 3 グリッド | _/2 | |
| 4 コンポーネント | _/2 | |
| 5 余白 | _/2 | |
| 6 らしさ | _/2 | |
合計: _/12 ／ 構造系0点: 有/無 ／ 判定: 昇格/改訂継続
人間仕上げメモ: 
次の改訂指示: 
\`\`\`
```

- [ ] **Step 3: 検証**

Run: `grep -E "8.5|構造系|色ゾーニング|タイポ階層|グリッド整列|コンポーネント一貫性|余白リズム|パターンらしさ" docs/design-wheel/CRITIQUE-RUBRIC.md`
Expected: 全項目ヒット。

- [ ] **Step 4: コミット**

```bash
git add docs/design-wheel/CRITIQUE-RUBRIC.md
git commit -m "docs(design-wheel): CRITIQUE-RUBRIC（6観点・70%判定）"
```

---

## Task 4: LOOP.md

**Files:**
- Create: `docs/design-wheel/LOOP.md`

- [ ] **Step 1: 受け入れ基準**

grep で4フェーズ見出し `Sense`, `Systematize`, `Generate`, `Learn` を含むこと。

- [ ] **Step 2: ファイル作成**

```markdown
# LOOP — Design Wheel 4フェーズ手順書

1パターンを端から端まで貫通させる手順。AI7割 / 人間3割（D-021）。

---

## Phase 1: Sense（参照収集）🧑＋AI
1. 対象パターンの UI 画像を Pinterest 等で 10〜20枚集める（人間が選定）。
2. 各画像を `/design-ref` スキルで `brain/45_Design_Refs/` に保存。
3. 保存時に `wheel-pattern:<pattern>` タグを付与（既存 FAMBOX軸タグと併記）。
4. `patterns/<pattern>/refs.md` に索引（リンク＋一言メモ）を作る。
- **完了条件**: refs 10枚以上＋`wheel-pattern` タグ付与済。

## Phase 2: Systematize（体系化）🧑＋AI
1. 集めた画像を Claude Design に投入し、色/タイポ/コンポーネント/レイアウトを自動抽出。
2. Web 即プレビューで抽出システムの妥当性を目視確認（人間）。
3. 抽出結果を `PATTERN-SCHEMA.md` の型に**蒸留**して `patterns/<pattern>/SYSTEM.md` を作成。
4. 仮置きの値は実画像と照合して確定する（憶測値を残さない）。
- **完了条件**: SYSTEM.md が7セクション全て埋まり、空欄/TBD なし。

## Phase 3: Generate（Figma構築）AI
1. `SYSTEM.md` を読み込む。
2. **参照とは別物の題材**で1画面を設計（例: corporate なら B2Bサービス紹介LP Hero）。
3. figma-bridge で構造7割を構築（レイアウト/余白/色/階層/グレーボックス）。
   - フォントは Inter 固定で割り切る（人間が後で差替）。
4. 手順を `patterns/<pattern>/figma-recipe.md` に記録。
- **完了条件**: Figma に1画面の構造が組み上がり、export 画像を取得。

## Phase 4: Learn（採点・改訂）AI＋🧑
1. 生成 Figma を export → 参照と並べて `CRITIQUE-RUBRIC.md` で採点。
2. 結果を `patterns/<pattern>/critique-log.md` に記録。
3. 構造系の減点があれば SYSTEM.md を改訂し Phase 3 を再実行。
4. 昇格条件（≥8.5/12 かつ構造系0点なし）を満たしたら README のステータスを ✅ に。
- **完了条件**: 昇格条件達成、または少なくとも1周の改訂を記録。

---

## 横展開（パイロット完走後）
次のパターンは本 LOOP をコピーして実行。SYSTEM.md は同一スキーマなので比較・流用可能。
```

- [ ] **Step 3: 検証**

Run: `grep -E "Phase 1: Sense|Phase 2: Systematize|Phase 3: Generate|Phase 4: Learn" docs/design-wheel/LOOP.md`
Expected: 4フェーズすべてヒット。

- [ ] **Step 4: コミット**

```bash
git add docs/design-wheel/LOOP.md
git commit -m "docs(design-wheel): LOOP（4フェーズ手順書）"
```

---

## Task 5: 45_Design_Refs に wheel-pattern タグ軸を追加

**Files:**
- Modify: `brain/45_Design_Refs/README.md`
- Modify: `brain/45_Design_Refs/_index.md`（先頭の説明部に列追加方針を明記）

- [ ] **Step 1: 既存構造を確認**

Run: `sed -n '1,30p' brain/45_Design_Refs/README.md`
Expected: 既存のタグ/スタイル運用ルールが見える。

- [ ] **Step 2: README に wheel-pattern 軸の説明を追記**

README の末尾に以下のセクションを追加（既存内容は保持）:

```markdown
## wheel-pattern タグ軸（2026-06-09 追加 / Design Wheel 連携）

FAMBOX軸（意味/隠喩）とは**直交**する表層スタイルの軸。Design Wheel の
パターン在庫（`docs/design-wheel/`）と連動する。

- 値: `geometric / corporate / grid / digital / sporty / lab`
- 記法: 各 ref ファイルの front-matter またはタグ行に `wheel-pattern: <値>` を併記。
- FAMBOX軸タグは従来通り維持（2軸＝意味×スタイルで引ける）。
- `_by-style/` 仕組みとは共存（重複可）。
```

- [ ] **Step 3: _index.md の表頭に wheel-pattern 列を追加する方針を明記**

`_index.md` 冒頭（「最終更新」行の直後）に1行追記:

```markdown
> **2026-06-09 〜**: 各行に `wheel-pattern`（geometric/corporate/grid/digital/sporty/lab）を併記。新規追加分から適用、既存15件は遡及任意。
```

- [ ] **Step 4: 検証**

Run: `grep -E "wheel-pattern" brain/45_Design_Refs/README.md brain/45_Design_Refs/_index.md`
Expected: 両ファイルでヒット。

- [ ] **Step 5: コミット**

```bash
git add brain/45_Design_Refs/README.md brain/45_Design_Refs/_index.md
git commit -m "docs(design-refs): wheel-pattern タグ軸を追加（Design Wheel 連携）"
```

---

## Task 6: 🧑 Sense — corporate refs 収集

**Files:**
- Create: `docs/design-wheel/patterns/corporate/refs.md`

- [ ] **Step 1: refs.md の枠を作成**

```markdown
# corporate — 参照索引

> `wheel-pattern:corporate` の根拠画像。10〜20枚を目標に収集。

| # | タイトル | 45_Design_Refs リンク | 一言メモ | 抽出注目点 |
|---|---|---|---|---|
| 1 | | | | |
```

- [ ] **Step 2: 🧑 ユーザーに収集を依頼**

ユーザーに「corporate（コーポレート/B2B/SaaS LP系）の UI 画像を Pinterest から10〜20枚」共有を依頼。集まった各画像を `/design-ref` スキルで保存し `wheel-pattern:corporate` を付与。

- [ ] **Step 3: refs.md に索引を追記**

保存した各 ref へのリンク・一言メモ・抽出注目点（色/タイポ/グリッドのどこを見るか）を表に追記。

- [ ] **Step 4: 検証**

Run: `grep -c "45_Design_Refs" docs/design-wheel/patterns/corporate/refs.md`
Expected: 10以上（収集枚数に応じる）。不足ならユーザーに追加依頼。

- [ ] **Step 5: コミット**

```bash
git add docs/design-wheel/patterns/corporate/refs.md
git commit -m "docs(design-wheel): corporate refs 索引（Sense）"
```

---

## Task 7: 🧑 Systematize — corporate SYSTEM.md

**Files:**
- Create: `docs/design-wheel/patterns/corporate/SYSTEM.md`

- [ ] **Step 1: 🧑 Claude Design で抽出**

収集画像を Claude Design に投入 → 色/タイポ/コンポーネント/レイアウト抽出＋Web即プレビュー。ユーザーが妥当性を目視確認。

- [ ] **Step 2: PATTERN-SCHEMA の型に蒸留して SYSTEM.md 作成**

`PATTERN-SCHEMA.md` の7セクションをすべて埋める。Claude Design 抽出値＋refs実画像照合で確定。憶測値・空欄・TBD を残さない。

- [ ] **Step 3: 検証（スキーマ準拠＋空欄なし）**

Run: `grep -E "Identity|Color|Type|Layout|Components|DO / DON'T" docs/design-wheel/patterns/corporate/SYSTEM.md && grep -nE "______|TBD|<例|<そ" docs/design-wheel/patterns/corporate/SYSTEM.md`
Expected: 前半6セクションヒット、後半（未埋めプレースホルダ）は**0件**。

- [ ] **Step 4: コミット**

```bash
git add docs/design-wheel/patterns/corporate/SYSTEM.md
git commit -m "docs(design-wheel): corporate SYSTEM.md（Systematize）"
```

---

## Task 8: Generate 準備 — figma-recipe.md

**Files:**
- Create: `docs/design-wheel/patterns/corporate/figma-recipe.md`

- [ ] **Step 1: ビルド題材を決める**

参照とは別物の題材を1つ決める（推奨: 「B2B SaaS サービス紹介LP の Hero + 特徴3カード」1画面）。

- [ ] **Step 2: figma-recipe.md にビルド手順を記述**

```markdown
# corporate — Figma ビルドレシピ

## 題材
B2B SaaS サービス紹介LP: Hero（見出し＋サブ＋CTA＋グレーボックス画像）＋ 特徴3カード。

## SYSTEM.md からの適用
- グリッド: <SYSTEM.md の値>
- 色ゾーニング: 背景bg / カードsurface / CTAaccent
- タイポ: H1=飾り/大H1、本文=Body、ジャンプ率は SYSTEM.md 準拠
- 余白: S/M/L を SYSTEM.md 値で

## figma-bridge 構築手順
1. create_frame（PC幅、SYSTEM.md のグリッドに合わせる）
2. Hero: set_layout_mode(VERTICAL) + set_padding(L) + set_item_spacing(M)
3. 見出し/サブ/CTA を create_text（フォントは Inter 固定で割り切り）
4. グレーボックス画像枠 create_rectangle + set_fill_color(line/muted)
5. 特徴3カード: 横 auto-layout、各カード surface + 角丸（SYSTEM.md値）
6. export_node_as_image で確認用書き出し

## 人間仕上げ（3割）
- フォントを SYSTEM.md 指定書体へ差替
- グレーボックス → 実画像差込
```

- [ ] **Step 3: 検証**

Run: `grep -E "題材|figma-bridge 構築手順|人間仕上げ" docs/design-wheel/patterns/corporate/figma-recipe.md`
Expected: 3セクションヒット。

- [ ] **Step 4: コミット**

```bash
git add docs/design-wheel/patterns/corporate/figma-recipe.md
git commit -m "docs(design-wheel): corporate figma-recipe（Generate準備）"
```

---

## Task 9: Generate 実行 — figma-bridge で構築

**Files:**
- 出力: Figma（MCP 経由）／ export 画像

- [ ] **Step 1: figma-bridge 接続確認**

figma-bridge MCP に接続（`join_channel`）。接続切れ時は再Connect → join_channel（[[feedback_figma_bridge_text_limitations]]）。

- [ ] **Step 2: figma-recipe.md 手順で構築**

`SYSTEM.md` + `figma-recipe.md` に従い、create_frame → auto-layout → text/rectangle → カードで Hero+3カードを構築。

- [ ] **Step 3: export して確認**

`export_node_as_image` でフレームを書き出し、Read で目視。構造（色/階層/グリッド/余白）が SYSTEM.md 通りか確認。

- [ ] **Step 4: 検証**

export 画像を Read し、(a) 色ゾーニング (b) 階層 (c) グリッド整列 (d) 余白 が SYSTEM.md と一致するか自己チェック。ズレは Task 10 の採点で記録。

- [ ] **Step 5: コミット**（figma-recipe.md に実ノードID/結果メモを追記した場合）

```bash
git add docs/design-wheel/patterns/corporate/figma-recipe.md
git commit -m "docs(design-wheel): corporate Figma 構築結果メモ（Generate実行）"
```

---

## Task 10: Learn — 採点・critique-log・改訂

**Files:**
- Create: `docs/design-wheel/patterns/corporate/critique-log.md`

- [ ] **Step 1: CRITIQUE-RUBRIC で採点**

export 画像 vs refs を `CRITIQUE-RUBRIC.md` の記録フォーマットで採点。

- [ ] **Step 2: critique-log.md に記録**

```markdown
# corporate — critique log

（CRITIQUE-RUBRIC.md の記録フォーマットを各版ごとに貼る）
```
に v1 採点結果を貼り付け。合計・構造系0点有無・判定・次の改訂指示を明記。

- [ ] **Step 3: 改訂判定**

- 昇格条件（≥8.5/12 かつ構造系0点なし）達成 → README のステータスを ✅ に更新。
- 未達 → SYSTEM.md を改訂し Task 9 を再実行（最低1周は回す）。

- [ ] **Step 4: 純構築時間を記録**

figma-bridge 着手→7割完成の所要時間を critique-log に記録（横展開の基準値）。

- [ ] **Step 5: 検証**

Run: `grep -E "合計|判定|純構築時間" docs/design-wheel/patterns/corporate/critique-log.md`
Expected: 全項目ヒット。

- [ ] **Step 6: コミット**

```bash
git add docs/design-wheel/patterns/corporate/critique-log.md docs/design-wheel/README.md
git commit -m "docs(design-wheel): corporate v1 採点・学び（Learn）"
```

---

## Task 11: メモリ更新（プロジェクト記録）

**Files:**
- Create: `~/.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_design_wheel.md`
- Modify: `~/.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/MEMORY.md`（1行ポインタ追加）

- [ ] **Step 1: project メモリを作成**

front-matter（type: project）＋ Purpose（非デザイナー70%・多パターン在庫）＋ ハブ場所（`docs/design-wheel/`）＋ アーキ案A＋パイロット corporate の到達状況＋ `fambox-flywheel` との関係（一般化版・別ハブ）を記録。

- [ ] **Step 2: MEMORY.md にポインタを1行追加**

`## Active Development` に `- [project_design_wheel.md](project_design_wheel.md) — Design Wheel（非デザイナー70%の多パターン在庫）。corporate パイロット…` を追記。

- [ ] **Step 3: 検証**

Run: `grep -c "project_design_wheel" ~/.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/MEMORY.md`
Expected: 1以上。

---

## Self-Review（プラン作成者チェック済み）

- **Spec coverage**: spec §3構造→Task1-4、§5タグ軸→Task5、§4ループ4フェーズ→Task6-10、§6スキーマ→Task2/7、§7ルーブリック→Task3/10、§8パイロットDoD→Task6-10、計測→Task10。全カバー。
- **Placeholder scan**: 各ドキュメントは完全な本文を記載。SYSTEM.md/refs.md/critique-log.md は"収集・抽出結果待ち"の正当な空欄（人間ゲート Task）で、Task内に埋め方と検証 grep を明記済。
- **Type consistency**: 役割トークン名（bg/surface/ink/ink-muted/accent/line）・6観点・昇格条件（8.5/12・構造系0点なし）を全Taskで統一。
```
