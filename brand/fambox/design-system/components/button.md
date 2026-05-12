---
title: FAMBOX Primitive — Button
type: design-system
layer: L2-Primitives
component: Button
version: 0.3
status: stable
last_updated: 2026-04-27
owner: 宮川
source: FAM Brand DNA v0.5 K章（継承）+ Worksheet §6 確定（2026-04-27）
brand_alignment:
  - Integrity（誠実）: 派手な装飾を排除
  - Drive（推進）: Pill型で動きを示唆
  - Co-driven（対等）: 押しつけでない CTA
---

# Button — Primitive Component

## 概要

FAMBOX で最重要の Primitive。**5 Variant × 3 Size × 6 State** で構成。
Pill型 radius 50px（FAM 既存 corp-btn 継承、Link を除く）。

## ブランド整合性

- **Integrity**: 無駄な装飾・エフェクトを排除。形状はシンプルな Pill、影は軽微のみ
- **Drive**: Drive Orange を Primary に使い、ホバーで前方向へ 2px せり出す
- **Co-driven**: 「押しつけがましくない」トーン — 角丸 Pill で柔らかさ、文言で対等さ

---

## Variants（5種）

| Variant | クラス | 背景 | 文字色 | 枠線 | 形状 | 用途 |
|---|---|---|---|---|---|---|
| **Primary** | `btn-primary` | `--color-drive` | `--color-white` | none | Pill 50px | 主役 CTA（1画面に原則1つ） |
| **Secondary Outline Ink** | `btn-secondary-ink` | transparent | `--color-ink` | 2px `--color-ink` | Pill 50px | 中性的な副 CTA・並列ボタン |
| **Secondary Outline Drive** | `btn-secondary-drive` | transparent | `--color-drive` | 2px `--color-drive` | Pill 50px | Primary に並ぶ副選択肢で「色は揃えたいが主役は譲る」 |
| **Ghost** | `btn-ghost` | transparent | `--color-ink` | none | Pill 50px | キャンセル・閉じる・三次操作 |
| **Link** | `btn-link` | transparent | `--color-link-on-light`（drive） | none | flat（Pillなし） | 「詳細を見る →」等のテキスト型導線 |

### Variant 選択フロー

```
このボタンは1画面の主役か？
├─ Yes → Primary
└─ No → 並列ボタンか？
        ├─ Yes → Secondary Outline Ink（中立）/ Drive（主役寄り）
        └─ No  → 三次操作？
                ├─ Yes（モーダルCancel等）→ Ghost
                └─ No（インライン誘導）  → Link
```

### Anti-pattern
- 1画面に Primary を2つ以上 → 階層崩壊
- Destructive（赤Pill）の使用 → モーダル＋Cancel/OK で代替
- Pill を Link に適用 → Pillはアクション型のシグナル、テキスト誘導には過剰

---

## Sizes（3段階）

| Size | クラス | padding | font-size | 使用文脈 |
|---|---|---|---|---|
| **SM** | `btn-sm` | `8px 16px` | `--fs-body-sm`（14px） | Card内・密なフォーム |
| **MD** ★既定 | `btn-md` | `12px 32px` | `--fs-body`（16px） | 標準（Hero以外の大半） |
| **LG** | `btn-lg` | `16px 40px` | `--fs-lg`（20px） | LP Hero・主役 CTA |

※ MD/LG の padding は FAM corp-btn 既存値を継承。SM のみ新規追加。

### Touch Target
全 Size で **min-height 44px** を確保（WCAG）。SM は padding と line-height で 44px 達成。

---

## States（6状態）

### default
基準状態。Variant 標準色を表示。

### hover
- **Primary**: `background: var(--color-drive-light)` + `transform: translateY(-2px)` + shadow-2
- **Secondary**: `background: var(--color-ink) / var(--color-drive)` (反転)、文字色を白に
- **Ghost**: `background: rgba(27,29,26,0.06)`（subtle Ink overlay）
- **Link**: `text-decoration: underline` + `color: var(--color-link-hover)`

```css
.btn { transition: background var(--duration-fast) var(--ease-out),
                   transform var(--duration-fast) var(--ease-out); }
```

### focus（focus-visible のみ）
全 Variant 共通: `outline: 2px solid var(--color-focus-ring); outline-offset: 2px;`
WCAG 2.1 AA 準拠。マウス操作では非表示、キーボード操作でのみ可視化。

### active
- Pill系: `transform: translateY(0)` + 背景を default 色へ即時戻す
- Link: 一瞬 `opacity: 0.85`

### disabled
- `background: var(--border-base)` / `color: var(--color-caption)` / `cursor: not-allowed` / 影なし / transform 無効
- `aria-disabled="true"` 必須（または `disabled` 属性）

### loading
- 文字を透明化（`color: transparent`）してスピナーを `::after` で重ねる
- `pointer-events: none` でクリック無効化
- `aria-busy="true"` 必須

```css
.btn.is-loading::after {
  content: '';
  position: absolute;
  width: 16px; height: 16px;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
```

---

## Icon Button（2形態）

### `btn-icon-only`（アイコン単独）
正方形ボタン。文字なし・アイコンのみ。

| Size | サイズ |
|---|---|
| SM | 32×32 px |
| MD | 44×44 px ★既定 |
| LG | 56×56 px |

**必須ルール**: `aria-label` でアクション名を必ず指定。
```html
<button class="btn btn-icon-only btn-md" aria-label="閉じる">
  {%- render 'icon', name: 'nav-close', size: 24 -%}
</button>
```

### `btn-with-icon`（アイコン + テキスト）
通常 Button と同形状。アイコンは leading（先頭）または trailing（末尾）に配置。

```html
<a class="btn btn-primary btn-md btn-with-icon" href="...">
  {%- render 'icon', name: 'action-download', size: 16 -%}
  <span>資料を受け取る</span>
</a>
```

| 配置 | gap | 用途 |
|---|---|---|
| leading | `var(--space-1)`（8px） | アクション系（download / share / external） |
| trailing | `var(--space-1)` | 進行系（→ 次へ・詳細を見る） |

---

## Liquid 実装例

### 標準 Primary CTA
```liquid
{% raw %}<a href="{{ contact_url }}" class="btn btn-primary btn-md">
  プライマリCTA文言
</a>{% endraw %}
```
※ 文言は `cta-wording-proposal.md` 参照（別タスクで確定予定）。

### 並列 Secondary
```liquid
{% raw %}<div class="btn-group">
  <a class="btn btn-primary btn-md" href="...">主操作</a>
  <a class="btn btn-secondary-ink btn-md" href="...">副操作</a>
</div>{% endraw %}
```

### Icon-only（閉じる）
```liquid
{% raw %}<button class="btn btn-icon-only btn-md" aria-label="閉じる" data-modal-close>
  {%- render 'icon', name: 'nav-close', size: 24 -%}
</button>{% endraw %}
```

### Link 型（詳細を見る）
```liquid
{% raw %}<a href="{{ link_url }}" class="btn btn-link">
  詳細を見る
  {%- render 'icon', name: 'nav-forward', size: 16 -%}
</a>{% endraw %}
```

---

## CSS（v0.3 実装）

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-1);
  font-family: var(--font-en);
  font-weight: var(--fw-semibold);
  letter-spacing: var(--ls-en);
  text-align: center;
  text-decoration: none;
  white-space: nowrap;
  border-radius: var(--radius-pill-cta);
  border: none;
  cursor: pointer;
  position: relative;
  min-height: 44px;
  transition:
    background var(--duration-fast) var(--ease-out),
    color var(--duration-fast) var(--ease-out),
    transform var(--duration-fast) var(--ease-out),
    box-shadow var(--duration-fast) var(--ease-out);
}

/* === Variants === */
.btn-primary {
  background: var(--color-drive);
  color: var(--color-white);
}
.btn-primary:hover {
  background: var(--color-drive-light);
  transform: translateY(-2px);
  box-shadow: var(--shadow-2);
}
.btn-primary:active { transform: translateY(0); background: var(--color-drive); box-shadow: none; }

.btn-secondary-ink {
  background: transparent;
  color: var(--color-ink);
  border: var(--bw-thick) solid var(--color-ink);
}
.btn-secondary-ink:hover {
  background: var(--color-ink);
  color: var(--color-white);
}

.btn-secondary-drive {
  background: transparent;
  color: var(--color-drive);
  border: var(--bw-thick) solid var(--color-drive);
}
.btn-secondary-drive:hover {
  background: var(--color-drive);
  color: var(--color-white);
}

.btn-ghost {
  background: transparent;
  color: var(--color-ink);
}
.btn-ghost:hover {
  background: rgba(27, 29, 26, 0.06);
}

.btn-link {
  background: transparent;
  color: var(--color-link-on-light);
  border-radius: 0;
  min-height: auto;
  padding: 0;
  font-weight: var(--fw-medium);
}
.btn-link:hover {
  color: var(--color-link-hover);
  text-decoration: underline;
}

/* === Sizes === */
.btn-sm { padding: var(--space-1) var(--space-2); font-size: var(--fs-body-sm); }
.btn-md { padding: 12px var(--space-4); font-size: var(--fs-body); }
.btn-lg { padding: var(--space-2) 40px; font-size: var(--fs-lg); }

/* === Focus（共通）=== */
.btn:focus-visible {
  outline: var(--bw-thick) solid var(--color-focus-ring);
  outline-offset: 2px;
}

/* === Disabled（共通）=== */
.btn:disabled,
.btn[aria-disabled="true"] {
  background: var(--border-base);
  color: var(--color-caption);
  border-color: var(--border-base);
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
  pointer-events: none;
}

/* === Loading（共通）=== */
.btn.is-loading {
  color: transparent;
  pointer-events: none;
}
.btn.is-loading::after {
  content: '';
  position: absolute;
  width: 16px; height: 16px;
  border: 2px solid currentColor;
  border-top-color: transparent;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* === Icon Button === */
.btn-icon-only {
  padding: 0;
  aspect-ratio: 1 / 1;
}
.btn-icon-only.btn-sm { width: 32px; height: 32px; min-height: 32px; }
.btn-icon-only.btn-md { width: 44px; height: 44px; }
.btn-icon-only.btn-lg { width: 56px; height: 56px; }

.btn-with-icon { gap: var(--space-1); }
```

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| Touch Target | 全 Size で min 44×44 px（SM `btn-icon-only` のみ 32px、密なUI例外） |
| Focus | `:focus-visible` で Drive 2px outline（WCAG 2.1 AA） |
| Contrast | 白 on Drive = 3.8:1（AAは要セミボールド以上で担保） |
| aria-label | `btn-icon-only` は必須 |
| aria-disabled | disabled 時に明示（属性 `disabled` でも可） |
| aria-busy | loading 時に必須 |
| keyboard | space / enter で押下、tab で focus（HTML標準） |

---

## Do / Don't

### ✅ Do
- 1画面1 Primary を厳守
- Secondary は Ink（中立）と Drive（主役寄り）を文脈で使い分け
- アイコン併用時はテキストが主、アイコンが副（gap 8px）
- 文字数 10 文字以内（MD/LG共通の運用ルール）
- Pill 形状は Link 以外で必ず維持

### ✕ Don't
- Primary を1画面に2つ以上置く
- Destructive（赤Pill）の使用 → モーダル＋確認で代替
- 直書き色（`background: red`）→ 必ず token 経由
- Link variant に Pill 適用 → 形状ノイズ
- Icon-only に aria-label を付け忘れる

---

## Brand DNA Anti との照合

本コンポは以下の Anti を踏まない:
- 表面的／派手 → radius で柔らかさ、装飾なし
- エセ高級 → グラデ／ゴールドなし
- 媚びた広告 → 誇張なし、静かに主役

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `0. Cover`（v0.4 で `3. Primitives` へ移動予定 — figma-build-log の所在表記と一時的に不一致）
- **Component Set ID**: `46:32` ✅ 自動生成済 + v0.3 state 拡張済（2026-05-12）
- 生成スキル: `figma-component-from-spec` v0.1 + v0.3 incremental 拡張
- **実装済 variants**: **60**（`variant` × `size` × `state`）
  - variant: primary / secondary-ink / secondary-drive / ghost / link（5）
  - size: sm / md / lg（3）
  - state: default / hover / disabled / loading（4）
- **未実装 variants（v0.4 で追加予定）**:
  - state: **focus / active**（残 2 状態）
  - with-icon: leading / trailing / icon-only（INSTANCE_SWAP property 化を検討中）
- **state 別仕様**:
  - default: 既存 v0.2 のまま
  - hover: primary → `drive-light` / secondary-ink → ink 反転 + 白文字 / secondary-drive → drive 反転 + 白文字 / ghost → `rgba(27,29,26,0.06)` 直値 / link → underline + `link-hover` alias
  - disabled: 全 variant → bg `border/base` + text `ink/caption` + stroke 除去
  - loading: text opacity 0 + 中央に variant 色の dashed ring（sm14 / md16 / lg20px、暫定 — Spinner v0.3 で arc curve 化予定）
- Variables バインド: color (bg/border/text/disabled/hover/loading-ring) / radius (pill-cta) / border-width (thick) / font-size (body-sm/body/lg)
- 配置: state ごとに横方向ブロック（x offset 0 / 700 / 1400 / 2100、各ブロック 626 幅、Component Set 全幅 2726）

---

## Change Log

- v0.3-figma (2026-05-12): Figma で state property 拡張完了（45 variants 追加 / 15 → 60）。default 既存維持・hover / disabled / loading を Variable bind 込みで実装。残 v0.4 = focus / active state + with-icon
- v0.2-figma (2026-05-12): Figma Component Set 自動生成（15 variants / `variant` × `size`）
- v0.3 (2026-04-27): Worksheet §6 確定反映 — 5 Variant 採用（Primary / Secondary Ink / Secondary Drive / Ghost / Link）/ 3 Size 全採用 / 6 State / Icon-only & With-icon 両形態 / Destructive 不採用
- v0.2 (2026-04-20): Seed ドキュメント作成（FAM v0.5 K章継承ベース）
- （予定）v1.0: Figma Library とリンク、Storybook 実装、CTA 文言確定
