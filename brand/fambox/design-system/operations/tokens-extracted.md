# Tokens Extracted from fambox-* Liquid（de facto Token 抽出表）

**生成**: 2026-05-18 / Session #47
**目的**: 既存 fambox-* Liquid section（7 ファイル / 5,294 行）に直値展開されている値を grep 抽出し、**de facto Token 表**として集約。L1 Tokens 化（CSS 変数 snippet 化 / Figma Variables 入力）の起点とする。
**手法**: 「実装が spec を追い越している現状では、spec を先に作るより実装から逆抽出する方が手戻りゼロ」（推奨ルートの 1 行要約）

## 抽出対象
- `sections/fambox-modal.liquid` (672)
- `sections/fambox-footer.liquid` (665)
- `sections/fambox-stat-grid.liquid` (454)
- `sections/fambox-case-study.liquid` (1,102)
- `sections/fambox-contact-form.liquid` (942)
- `sections/fambox-header.liquid` (719)
- `sections/fambox-bento-grid.liquid` (740)

---

## 1. Color Tokens（hex + rgba）

### 1-A. 主要 hex（出現頻度ランク）

| 出現 | hex | 想定 Token | spec § | Status |
|---:|---|---|---|---|
| 88 | `#1B1D1A` | `--color-ink` | §1-A 1-3 Ink/Text | ✅ spec 整合 |
| 64 | `#FFF` | `--color-white` | §1-A 1-4 Background | ✅（`#FFFFFF` 10 件と重複統合）|
| 39 | `#FC5214` | `--color-drive` | §1-A 1-1 Primary | ⚠ **#FB4C15 と表記揺れ** |
| 24 | `#FB4C15` | `--color-drive` | §1-A 1-1 Primary | ⚠ **重複** — 統一すべき |
| 20 | `#5C5F58` | `--color-sub` | §1-A 1-3 Ink/Text | ✅ |
| 18 | `#FAFAFA` | `--bg-secondary` | §1-A 1-4 Background | ✅ |
| 10 | `#FFFFFF` | `--color-white` | §1-A 1-4 | ✅（`#FFF` と重複統合）|
| 8 | `#E14710` | `--color-drive-hover` | （仕様外）| ⚠ **spec 追加候補** |
| 7 | `#DDD` | `--color-placeholder` | （仕様外）| ⚠ **spec 追加候補** |
| 6 | `#FF7A51` | `--color-drive-light` | §1-A 1-1（light）| 🟡 確認要 |
| 5 | `#ECECEC` | `--border-base` ? | §1-A 1-5 Border | 🟡 用途確認 |
| 5 | `#D0D1DB` | （未定）| — | 🟡 マジック |
| 5 | `#8A8D87` | `--color-caption` | §1-A 1-3 Ink/Text | ✅ |
| 4 | `#F3F3F3` | `--bg-tertiary` | §1-A 1-4 | ✅ |
| 4 | `#92939C` | （未定）| — | 🟡 マジック |
| 4 | `#545655` | （未定）| — | 🟡 マジック |
| 3 | `#D32F2F` | `--color-error` | §1-A 1-6 Semantic | ✅ |
| 3 | `#2C2E2B` | `--color-ink-darker` ? | §1-A 1-3 | 🟡 |
| 2 | `#E8E8E8` | `--border-light` ? | §1-A 1-5 | 🟡 |
| 2 | `#CCC` | `--border-base` ? | §1-A 1-5 | 🟡 |
| 2 | `#B3B5B0` | `--color-disabled` ? | （仕様外）| ⚠ spec 追加候補 |
| 2 | `#999` | （未定）| — | 🟡 マジック |
| 2 | `#2A2C2A` | `--color-ink-dark` ? | §1-A 1-3 | 🟡 |
| 1 | `#FF4A00` | （未定）| — | 🟡 |
| 1 | `#E71422` | （未定）| — | 🟡 |
| 1 | `#666` `#333` `#2E7D32` 等 | — | — | 🟡 |

**結論**: 上位 8 色で **80% カバー**。`#1B1D1A` / `#FFF` / `#FC5214` / `#5C5F58` / `#FAFAFA` の 5 色だけで **229 / 332 = 69% カバー**。

#### 🚨 即修正候補
- **Drive 色の表記揺れ**: `#FC5214` (39) vs `#FB4C15` (24) → どちらかに統一が必要。spec §1-A 1-1 で **`#FC5214` を正**として宣言、`#FB4C15` を sed 一括置換すべき。
- **マジックナンバー**: `#D0D1DB` / `#92939C` / `#545655` 等は spec にない → 用途を Liquid から逆引きして Token 化 or 排除

### 1-B. RGBA（alpha 付き色）

| 出現 | rgba | 想定 Token | 備考 |
|---:|---|---|---|
| 8 | `rgba(255,255,255,0.15)` | `--white-15` | white overlay 系 |
| 8 | `rgba(255,255,255,0.1)` | `--white-10` | white overlay 系 |
| 7 | `rgba(0, 0, 0, 0.08)` | `--ink-overlay-08` | 影 / 仕切り |
| 5 | `rgba(255,255,255,0.9)` | `--white-90` | |
| 5 | `rgba(255,255,255,0.3)` | `--white-30` | |
| 5 | `rgba(251,76,21,0.95)` | `--drive-95`（`#FB4C15` ベース）| ⚠ Drive 表記揺れの alpha 版 |
| 5 | `rgba(251,76,21,0.90)` | `--drive-90` | ⚠ 同上 |
| 4 | `rgba(27, 29, 26, 0.08)` | `--ink-overlay-08`（= `#1B1D1A` の alpha）| **`rgba(0,0,0,0.08)` と意味が同じ** |
| 4 | `rgba(251,76,21,0.35)` | `--drive-35` | ⚠ 同上 |
| 3 | `rgba(27, 29, 26, 0.04)` | `--ink-overlay-04` | |
| 3 | `rgba(255,255,255,0.04/0.08/0.85)` 等 | `--white-X` | overlay scale |

**結論**: Glass 5 階調（spec §1-A 1-8）に対応する **white-overlay scale**（0.04/0.08/0.1/0.15/0.3/0.6/0.85/0.9）と **ink-overlay scale**（0.04/0.08/0.16/0.2）が de facto で確立されている。これを **`--glass-N`** / **`--ink-overlay-N`** / **`--white-overlay-N`** の 3 系統に整理可能。

---

## 2. Spacing Tokens（px 値）

### 2-A. 出現頻度

| 出現 | 値 | spec §1-C scale | Token 候補 |
|---:|---|---|---|
| 128 | 16px | ✅ 1-18 | `--space-2`（16）|
| 102 | 24px | ✅ 1-18 | `--space-3`（24）|
| 68 | 32px | ✅ 1-18 | `--space-4`（32）|
| 60 | 8px | ✅ 1-17 base unit | `--space-1`（8）|
| 59 | 12px | ⚠ **仕様外** | `--space-1.5`（spec 追加候補）|
| 51 | 64px | ✅ 1-18 | `--space-6`（64）|
| 48 | 40px | ⚠ **仕様外** | `--space-5`（仕様の 48 と中間）|
| 48 | 14px | （font-size 用途）| Typography で処理 |
| 46 | 4px | ⚠ **仕様外** | `--space-0.5`（spec 追加候補 / 細部用）|
| 42 | 48px | ✅ 1-18 | `--space-5`（48）|
| 42 | 1px | （border-width 用途）| `--border-thin` |
| 40 | 2px | （border-width 用途）| `--border-medium` |
| 31 | 56px | ⚠ **仕様外** | typography 用途（font-size 56px）|
| 30 | 1440px | （breakpoint / container-max）| `--container-max` |
| 28 | 767px | （breakpoint SP 上限）| `--bp-sp-max` |
| 28 | 20px | （font-size 用途）| Typography |
| 22 | 120px | （hero spacing 用途）| 確認要 |
| 19 | 768px | （breakpoint Tablet 下限）| `--bp-tablet` |
| 19 | 28px | （font-size 用途）| Typography |
| 17 | 96px | ✅ 1-18 / 1-19 SP section | `--space-7`（96）|
| 17 | 480px | （breakpoint SP small）| `--bp-sp-sm` ⚠ 仕様外 |
| 16 | 80px | ⚠ 仕様外 | Header height default |
| 14 | 13px | （font-size 用途）| Typography |
| 13 | 18px | （font-size 用途）| Typography |
| 13 | 320px | （max-width 用途）| Brand area |
| 13 | 15px | （font-size 用途）| Typography |

**結論**: spec §1-C の Scale `8/16/24/32/48/64/96/160` に加え、**実装で `4/12/40` が頻出**。これは spec への追加候補:
- `--space-0.5` = 4px（細かい padding / icon spacing）
- `--space-1.5` = 12px（中間 padding）
- `--space-4.5` = 40px（hero / large icon）

160px は実装ではほぼ出現せず、代わりに **120px が 22 回**（Hero / Section spacing 用）。

---

## 3. Typography Tokens

### 3-A. font-family

| 出現 | 値 | Token | spec § |
|---:|---|---|---|
| 93 | `'Hiragino Sans'` | `--font-ja` | §1-B 1-11 ✅ |
| 38 | `'Poppins'` | `--font-en` | §1-B 1-10 ✅ |

**結論**: spec と完全整合。**フォールバック**（`'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif`）も全 section で一貫。CSS 変数化で集約しやすい。

### 3-B. font-weight

| 出現 | 値 | Token | spec § |
|---:|---|---|---|
| 53 | 500 | `--fw-medium` | §1-B 1-13 ✅ |
| 52 | 600 | `--fw-semibold` | §1-B 1-13 ✅ |
| 20 | 400 | `--fw-regular` | §1-B 1-13 ✅ |
| 12 | 700 | `--fw-bold` | §1-B 1-13 ✅ |

**結論**: 仕様の 4 段階と完全一致。即 Token 化可能。

### 3-C. font-size（px 値から typography 用途を抽出）

| 出現 | 値 | 用途 | spec § |
|---:|---|---|---|
| 14 | 14px | body-sm / form label | §1-B 1-12 ✅ |
| 28 | 20px | h3 / large body | §1-B 1-12 ✅ |
| 19 | 28px | h2 mobile | ⚠ spec scale にない |
| 14 | 13px | caption-lg | ⚠ spec scale にない |
| 13 | 18px | quote / body-lg | ⚠ spec scale にない |
| 13 | 15px | body | ⚠ spec scale にない |
| 31 | 56px | stat-focus value | ⚠ spec の 48/64 の中間 |
| 12 | 12px | caption | §1-B 1-12 ✅ |
| 19 | 28px | section title mobile | ⚠ |
| 16 | 32px | title default | ✅ |
| 8 | 40px | title PC | ✅（spec の 32→48 の中間）|
| 8 | 48px | hero h1 | ✅ |
| 8 | 96px | mega numbers | ✅ |
| 6 | 64px | hero stat | ✅ |
| 1 | 16px | body | ✅ |

**結論**: spec の Scale `12/14/16/20/24/32/48/64/96/128` に対し、実装では **13/15/18/28/40/56** が散見。これは「**8px 倍数のステップ間に細かい段階を入れる**」運用が de facto で発生している。

#### 🚨 統制 vs 拡張の判断必要
- 案 A: spec を厳格運用 → 13/15/18/28/40/56 を **20/24/32/48 に丸める**
- 案 B: 実装に合わせて spec を拡張 → spec scale を **12/13/14/15/16/18/20/24/28/32/40/48/56/64/96/128** にする
- 推奨: **案 A（spec 厳格）** + 各値を 1-2 箇所で例外許可

### 3-D. line-height

| 出現 | 値 | 用途 | spec §1-B 1-14 |
|---:|---|---|---|
| 30 | 180% | 大本文 | ⚠ spec body 1.75 と乖離 |
| 18 | 1.5 | caption / heading | ✅ spec caption 1.5 |
| 16 | 1 | stat value（line-height: 1）| 数字専用 |
| 8 | 170% | quote / 強調本文 | ⚠ |
| 8 | 1.75 | body 標準 | ✅ spec body 1.75 |
| 6 | 1.8 | 大段落 | ⚠ 180% と表記揺れ |
| 5 | 1.7 | 中本文 | ⚠ 170% と表記揺れ |
| 5 | 1.6 | サブテキスト | ⚠ |
| 5 | 1.4 | heading | ⚠ spec heading 1.2 と乖離 |

**結論**: spec は **heading 1.2 / body 1.75 / caption 1.5** の 3 段階。実装は **1.4-1.8 の 6 段階**で揺れている。

#### 🚨 統一が必要
- spec を 5 段階に拡張: `--lh-tight` 1.2 / `--lh-heading` 1.4 / `--lh-base` 1.5 / `--lh-body` 1.75 / `--lh-relaxed` 1.8
- または実装を 3 段階に丸める

---

## 4. Radius Tokens

| 出現 | 値 | Token | spec §1-F 1-25 |
|---:|---|---|---|
| 14 | 4px | `--radius-sm` | ✅ |
| 12 | 50% | `--radius-circle` | （avatar 用 / spec 拡張候補）|
| 11 | 8px | `--radius-md` | ✅ |
| 2 | 9999px | `--radius-pill` | ✅ |
| 2 | 42px | `--radius-pill-cta` ? | 🟡 spec の 50px との差 |
| 1 | 2px | `--radius-xs` | （仕様外、軽量 badge 等）|
| 1 | 16px 16px 0 0 | sheet modal 上端のみ | 特殊 |

**結論**: 4 / 8 / 50% / 9999px の **4 スケール**が de facto。spec の `pill-cta(50px)` が **42px と乖離**（要修正）。

---

## 5. Motion Tokens

### 5-A. duration

| 出現 | 値 | Token | spec §1-D 1-21 |
|---:|---|---|---|
| 23 | 150ms | `--duration-fast` | ✅ |
| 8 | 250ms | `--duration-base` | ⚠ spec の 300ms と乖離 |
| 3 | 200ms | `--duration-quick` | ⚠ 仕様外 |
| 1 | 350ms | `--duration-slow` | ⚠ spec の 600ms と乖離 |

**結論**: 実装の中心は **150-350ms 帯**。spec の `150/300/600` とは中域が乖離。

#### 🚨 spec を実装に追従させる候補
- `--duration-fast`: 150ms（spec 既定）
- `--duration-base`: **250ms**（spec を 300 → 250 に更新検討）
- `--duration-slow`: **350ms**（spec を 600 → 350 に更新検討）

理由: 学び 73「SKILL 適用済 / 実装が動いているものは正」原則。

### 5-B. easing

`ease-out` が圧倒的に多用 → spec `easing: ease-in/out/inout` を `--ease-out` に集約推奨。

---

## 6. Breakpoint Tokens

| 出現 | 値 | Token | spec §1-G 1-26 |
|---:|---|---|---|
| 28 | 767px | `--bp-sp-max` | ✅ |
| 19 | 768px | `--bp-tablet` | ✅ |
| 17 | 480px | `--bp-sp-sm-max` | ⚠ 仕様外 |
| - | 1024px | `--bp-pc` | ✅ |

**結論**: spec の SP/Tablet/PC（〜767/768-1023/1024+）に加え、**480px が SP small** として実装で多用。`--bp-sp-sm` 追加が望ましい。

---

## 7. Shadow Tokens（spec §1-E 1-24 / 5 段階想定）

実装 grep で box-shadow を抽出:
- `0 1px 2px rgba(0, 0, 0, 0.04)` → `--shadow-1`（hairline）
- `0 4px 8px rgba(0, 0, 0, 0.08)` → `--shadow-2`
- `0 8px 16px rgba(0, 0, 0, 0.08-0.12)` → `--shadow-3`
- `0 12px 24px rgba(0, 0, 0, 0.08-0.16)` → `--shadow-4`
- `0 24px 48px rgba(0, 0, 0, 0.24)` → `--shadow-5`（modal）

**結論**: 5 段階の box-shadow scale が de facto で確立。spec §1-E 1-24 と整合。

---

## 8. Sumary（要約 + 集計）

### 全カテゴリ集計

| カテゴリ | de facto Token 数 | spec 整合 | spec 追加候補 | マジックナンバー |
|---|---|---|---|---|
| Color hex | 5 主要 + 15 副次 | 12 | 5 | 3 (#D0D1DB / #92939C / #545655) |
| Color rgba | 3 系統（glass / ink-overlay / white-overlay）| ✅ | 8 階調明確化 | 0 |
| Spacing | 7 段階 (4/8/12/16/24/32/48/64/96) | 5 | 3 (4/12/40) | 0 |
| Typography font-family | 2 (jp/en) | ✅ | 0 | 0 |
| Typography font-weight | 4 (400/500/600/700) | ✅ | 0 | 0 |
| Typography font-size | 11 段階 | 7 | 4 (13/15/18/28) | 2 (40 中間 / 56 中間) |
| Typography line-height | 6 段階 | 3 | 3 (1.4/1.6/1.7) | 0 |
| Radius | 4 段階 (4/8/50%/9999) | ✅ | 0 | 1 (42px) |
| Motion duration | 4 段階 (150/200/250/350) | 1 | 3 (200/250/350) | 0 |
| Shadow | 5 段階 | ✅ | 0 | 0 |
| Breakpoint | 4 段階 (480/767/768/1024) | 3 | 1 (480) | 0 |

### 🚨 即修正候補（次セッションで解消）

1. **Drive 色の表記揺れ**: `#FB4C15` (24 件) → `#FC5214` 全件統一（sed 一括置換）
2. **`#FFF` と `#FFFFFF` の統一**: 表記を `#fff` に統一
3. **マジックナンバー 3 色**: `#D0D1DB` / `#92939C` / `#545655` の用途を逆引きして Token 化 or 排除
4. **`42px` radius**: spec の `pill-cta` を `50px` から `42px` に更新 or 実装側を `50px` に統一

### 📋 spec 追加候補

- **Color**: `--color-drive-hover`（#E14710）/ `--color-placeholder`（#DDD）/ `--color-disabled`（#B3B5B0）
- **Spacing**: `--space-0.5`（4px）/ `--space-1.5`（12px）/ `--space-4.5`（40px）
- **Typography**: font-size に `13/15/18/28` を追加検討
- **Line-height**: 5 段階に拡張（1.2/1.4/1.5/1.75/1.8）
- **Duration**: spec を **150/250/350** に更新（現状 150/300/600 は実装と乖離）
- **Breakpoint**: `--bp-sp-sm` (480px) 追加
- **Radius**: `--radius-circle` (50%) 追加

---

## 次セッション（Session #48）の作業案

### Phase B-1: Liquid 内表記統一（30 min）

```bash
# Drive 色の表記揺れ修正
grep -l "#FB4C15" sections/fambox-*.liquid | xargs sed -i '' 's/#FB4C15/#FC5214/g'

# #FFF と #FFFFFF を小文字 #fff に統一
grep -l "#FFFFFF\|#FFF" sections/fambox-*.liquid | xargs sed -i '' 's/#FFFFFF/#fff/g; s/#FFF\b/#fff/g'

# 検証
grep -ohE "#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}" sections/fambox-*.liquid | sort | uniq -c | sort -rn | head -10
```

### Phase B-2: マジックナンバー逆引き（30 min）

`#D0D1DB` / `#92939C` / `#545655` を grep して使用箇所を確認、用途を Token 名と紐付け。

### Phase B-3: spec md（current.md §1-A〜§1-J）の更新（60 min）

学び抜粋:
- 学び 73: SKILL 適用済 / 実装が動いているものは正
- 学び 95: 機能カテゴリ単位で md を統合

実装に揃える方針で current.md §1 を更新（spec の `--duration-base: 300ms` → `250ms` 等）。

### Phase B-4: CSS 変数 snippet 化（60-90 min）

`snippets/fambox-tokens.css.liquid` を新規作成、本表に基づき全 Token を `:root` 宣言:

```liquid
{%- comment -%} FAMBOX Design System — Tokens v0.5 {%- endcomment -%}
<style>
:root {
  /* Color */
  --color-drive: #FC5214;
  --color-drive-hover: #E14710;
  --color-ink: #1B1D1A;
  --color-sub: #5C5F58;
  --color-caption: #8A8D87;
  --color-white: #fff;
  --bg-primary: #fff;
  --bg-secondary: #FAFAFA;
  --bg-tertiary: #F3F3F3;
  --color-error: #D32F2F;

  /* Glass overlay 5 階調 */
  --glass-1: rgba(0, 0, 0, 0.05);
  --glass-2: rgba(0, 0, 0, 0.1);
  --glass-3: rgba(0, 0, 0, 0.3);
  --glass-4: rgba(0, 0, 0, 0.6);
  --glass-5: rgba(0, 0, 0, 0.8);

  /* Spacing */
  --space-0-5: 4px;
  --space-1: 8px;
  --space-1-5: 12px;
  --space-2: 16px;
  --space-3: 24px;
  --space-4: 32px;
  --space-4-5: 40px;
  --space-5: 48px;
  --space-6: 64px;
  --space-7: 96px;
  --space-8: 120px;

  /* Typography */
  --font-ja: 'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;
  --font-en: 'Poppins', sans-serif;
  --fw-regular: 400;
  --fw-medium: 500;
  --fw-semibold: 600;
  --fw-bold: 700;
  --lh-tight: 1.2;
  --lh-heading: 1.4;
  --lh-base: 1.5;
  --lh-body: 1.75;
  --lh-relaxed: 1.8;

  /* Radius */
  --radius-xs: 2px;
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-circle: 50%;
  --radius-pill: 9999px;

  /* Motion */
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 350ms;
  --ease-out: ease-out;

  /* Shadow */
  --shadow-1: 0 1px 2px rgba(0, 0, 0, 0.04);
  --shadow-2: 0 4px 8px rgba(0, 0, 0, 0.08);
  --shadow-3: 0 8px 16px rgba(0, 0, 0, 0.12);
  --shadow-4: 0 12px 24px rgba(0, 0, 0, 0.16);
  --shadow-5: 0 24px 48px rgba(0, 0, 0, 0.24);

  /* Breakpoint (CSS では使えないが、container queries 等で参照可能) */
  --bp-sp-sm: 480px;
  --bp-sp-max: 767px;
  --bp-tablet: 768px;
  --bp-pc: 1024px;
  --container-max: 1440px;
}
</style>
```

### Phase B-5: 既存 7 sections を Variable 参照に段階置換（60-90 min × N セッション）

最初に **fambox-modal.liquid**（最小・依存少）で実証 → パターン確立後に他 6 sections へ展開。

---

## 関連

- `current.md §1-A〜§1-J` — L1 Tokens 仕様（v0.2）
- `figma-build-log.md` — Audit 履歴 / 学び 73, 95
- `2026-05-18-session-summary.md` — Session #27-46 マラソン総括
- `operations/scripts/generate-dashboard.py` — ダッシュボード自動生成（Phase 1）

## Status

- ✅ Step 1-3 完了（grep 抽出 → de facto Token 表）
- ✅ Step 4: spec gap 検出（本ファイル §8 サマリで網羅）
- ✅ Step 5: 次セッション引き継ぎ（本ファイル末尾 Phase B-1〜B-5）

---

## Session #48 実行ログ（2026-05-18）

### Phase B-1 完全版（実施）

`#FB4C15` 24件 → `#FC5214` に統一、その後 Python で全 hex を**小文字統一**（21 files / 565 chars 置換）:

```
files changed: 21
chars replaced: 565
```

**Before/After**:
- Before: `#FB4C15` 24 / `#FFFFFF` 10 / `#FFF` 64 件
- After:  `#FB4C15` 0 / `#FFFFFF` 0 / `#FFF` 0 / `#FC5214` 63 / `#fff` 64 件
- 副産物: `#FAFAFA` → `#fafafa` / `#ECECEC` → `#ececec` 等の全 hex も小文字化

### Phase B-2 マジックナンバー逆引き（実施）

| Color | 出現箇所 | 用途 | 判断 |
|---|---|---|---|
| `#d0d1db` (5) | fambox-blog-carousel / value-proposition / menu-showcase | 区切り線 (divider 1-2px) | **新規 `--border-soft` 追加**（spec §1-A 1-5 に追加済）|
| `#92939c` (4) | fambox-active-plans / active-plans-v2 / menu-showcase | カード sub text (color, 13px) | `--color-caption` #8a8d87 に集約（視覚的に区別なし）|
| `#545655` (4) | fambox-active-plans / active-plans-v2 / model-case | カード本文 (color) | `--color-sub` #5c5f58 に集約（視覚的に区別なし）|

### Phase B-3 spec 更新（実施）

current.md §1-A / §1-C / §1-D / §1-G を v0.5 実装に揃えて更新:

- §1-A Primary: 3値 → **4値**（`--color-drive-hover #E14710` 追加）
- §1-A Ink/Text: placeholder #DDD を明示
- §1-A Border: 3値 → **4値**（`--border-soft #D0D1DB` 追加）
- §1-A Semantic Alias: **`--color-disabled #B3B5B0`** 追加
- §1-C Spacing: scale を 8/16/24/32/48/64/96/160 → **4/8/12/16/24/32/40/48/64/96/120** に拡張（11 段階）
- §1-C Section spacing: PC 160 → **120**（実装に整合）
- §1-D duration: 150/300/600 → **150/250/350** に修正
- §1-D easing: ease-out 中心に集約
- §1-D line-height: 3 → **5 段階拡張**（tight 1.2 / heading 1.4 / base 1.5 / body 1.75 / relaxed 1.8）
- §1-G breakpoint: 3 → **4 段階拡張**（SP-sm 480 追加）

---

## 次セッション（Session #49）の作業案

### Phase B-4: `snippets/fambox-tokens.css.liquid` 新規作成（60-90 min）✅ Session #49 実施完了

Session #47 §Phase B-4 のテンプレに従って実装。Session #48 で確定した命名（`--space-0.5` 〜 `--space-8`、`--duration-fast/base/slow` 等）を使う。

**実装結果（Session #49）**:
- ファイル: `snippets/fambox-tokens.css.liquid`（255 行）
- 宣言された CSS 変数: **137 declarations / 133 unique tokens**
- 内訳:
  - §1-A Color: 50+ tokens（Drive 4 / Secondary 2 / Ink 5 / Background 3 / Border 4 / Semantic 4 / Data 6 / Glass 5 / White overlay 8 / Ink overlay 5 / Alias 6）
  - §1-B Typography: 25 tokens（font-family 2 / weight 4 / size 14 / line-height 5 / letter-spacing 4）
  - §1-C Spacing: 13 tokens（11段階 + section-spacing-sp/pc）
  - §1-D Motion: 7 tokens（3 duration + 3 easing + breathing）
  - §1-E Shadow: 6 tokens（5段階 + drive-glow）
  - §1-F Radius: 7 tokens
  - §1-G Breakpoint: 5 tokens
  - §1-H Z-index: 7 tokens
  - §1-I Icon: 6 tokens

**使い方**:
```liquid
{%- comment -%} theme.liquid の <head> 内に配置 {%- endcomment -%}
{% render 'fambox-tokens.css' %}
```

すべての fambox-* section が `var(--color-drive)` 等で参照可能になる。`prefers-reduced-motion: reduce` で duration を 0 に強制するフォールバックも同梱。

### Phase B-5: 既存 7 sections の Variable 参照置換（60-90 min × N）

優先順:
1. `fambox-modal.liquid`（最小 / 依存少 / 実証用）
2. `fambox-footer.liquid`（実証で得たパターンを横展開）
3. `fambox-bento-grid.liquid` / `fambox-header.liquid`
4. `fambox-contact-form.liquid` / `fambox-case-study.liquid`（大規模）
5. `fambox-stat-grid.liquid`（後回し）

各セッションで **1-2 sections を置換 → screenshot で視覚不変を確認 → commit**。
