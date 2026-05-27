---
title: FAMBOX Pattern — Card
type: design-system
layer: L3-Patterns
component: Card
version: 0.2
status: confirmed
last_updated: 2026-04-27
owner: 宮川
source: Worksheet §16（2026-04-27 確定）+ 既存 Liquid 実測（fam-achievement / card-product / subscription-plan-card / case-study）
brand_alignment:
  - Integrity（誠実）: 装飾過多を避け、情報構造で勝負
  - Co-driven（対等）: コンテンツが主役、Card は器
  - Anti: エセ高級・煽りバッジ・派手影を回避
related:
  - components/button.md
  - components/subscription-plan-card.md
  - components/case-study.md
  - tokens/colors.md
extensible: true  # v0.3 以降でカスタム Variant 追加余地あり
---

# Card — Pattern Component

## 概要

FAMBOX の最頻出 Pattern。**4 Variants × 6 State** で構成。L4 Component（Subscription Plan Card / Case Study Card / Header Nav Card 等）の **基盤**として継承される。

すべて `--radius-md`（8px）固定。Pill 型は Button 専用、Card には適用しない。

## ブランド整合性

- **Integrity**: 影は軽微（shadow-1 / hover で shadow-3）、Pill や派手装飾なし
- **Co-driven**: コンテンツ（画像・テキスト・データ）が主役、Card は読みやすい器
- **Anti 回避**: ゴールド・エセ高級グラデ・煽りバッジは禁止

---

## Variants（4 種 / 拡張可）

| Variant | クラス | 構造 | 使用例 |
|---|---|---|---|
| **Standard** | `card card-standard` | 縦型・画像上・タイトル・本文・CTA下 | 商品カード / Voice / 一般 |
| **Featured** | `card card-featured` | standard + Drive 2px 枠線 + 「おすすめ」バッジ | Subscription Plan の推奨プラン |
| **Horizontal** | `card card-horizontal` | 横型・画像左30% / テキスト右70%（SP も維持） | Case Study カード一覧 / Article List |
| **Flat** | `card card-flat` | 画像なし・テキストのみ・`--bg-secondary` 薄背景 | Stat Card / Quote / 通知パネル |

### 拡張ルール（v0.3 以降）

新しい Card Variant が必要な場合は以下を満たす:
1. **境界 4 ルール**: `--radius-md` 固定 / `1px solid --border-light` 既定 / padding は `--space-3` ベース / 影は shadow-1 〜 3 範囲
2. **CTA 必須**: 1 個以上の Button を持つ
3. **DNA Anti を踏まない**: Pill / Drive 背景 / shadow-4 以上 / ゴールド・派手グラデ禁止
4. **命名**: `card card-{variant-name}`（kebab-case）

---

## 共通 Props

| プロパティ | 値 |
|---|---|
| background | Standard/Featured/Horizontal: `--bg-primary` / Flat: `--bg-secondary` |
| border | `1px solid --border-light` 既定 / Featured: `2px solid --color-drive` / Selected: `2px solid --color-drive` |
| border-radius | `--radius-md`（8px） |
| padding | `--space-3`（24px） |
| 内部 gap | `--space-2`（16px） |
| shadow（default） | `--shadow-1` |
| shadow（hover） | `--shadow-3` + `transform: translateY(-2px)` |
| transition | `box-shadow / transform var(--duration-base) var(--ease-out)` |

---

## CTA 必須ルール

**全 Variants で CTA 1 個以上を必須**（Worksheet §16 Q3 A 採択）。

- Standard / Featured: Primary または Secondary を底面に
- Horizontal: テキスト末尾に Link 型 CTA（「詳細を見る →」）
- Flat: Link 型 CTA または Ghost ボタンを 1 個

「情報のみで CTA なし」の Card は **作らない**。情報単体なら `<section>` や `<article>` で素直に組む（DS の Card として成立させない）。

---

## States（6状態）

### default
基準。`--shadow-1` + `--border-light`。

### hover
```css
.card:hover {
  box-shadow: var(--shadow-3);
  transform: translateY(-2px);
  transition: box-shadow var(--duration-base) var(--ease-out),
              transform var(--duration-base) var(--ease-out);
}
```

### focus-visible
キーボード focus 時のみ outline。Card 全体がリンク化されている場合に重要。
```css
.card:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}
```

### active
hover の `translateY(-2px)` を一旦 0 に戻して押下感。
```css
.card:active { transform: translateY(0); }
```

### disabled
グレーアウト + ポインタ無効。あまり使わないが、SOLD OUT の商品 Card 等で。
```css
.card.is-disabled {
  opacity: 0.5;
  pointer-events: none;
}
```

### selected（`.is-selected` / Q4 A 採択）
Subscription / Plan 選択時、フィルタ選択時など。
```css
.card.is-selected {
  border: 2px solid var(--color-drive);
  /* padding を 1px 削って枠線分の差を吸収 */
  padding: calc(var(--space-3) - 1px);
}
```

---

## Horizontal 詳細（Q2 B 採択）

**SP でも横並び維持**: 画像 30% / テキスト 70% を全画面幅で保つ。

理由:
- Case Study / Article List で視線移動が読みやすい
- 一覧密度が上がる（縦長になりにくい）
- ただし画像が極端に小さくならないよう、min-width で下限を切る

```css
.card-horizontal {
  display: grid;
  grid-template-columns: 30% 70%;
  gap: var(--space-2);
  align-items: stretch;
}

.card-horizontal__media {
  min-width: 100px;  /* SP で潰れない下限 */
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border-radius: var(--radius-sm);
  overflow: hidden;
}

.card-horizontal__body {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  justify-content: space-between;
}

@media (max-width: 480px) {
  /* 極小 SP のみ縦折り返しの逃げ道（Q2 B 規律維持しつつ品質下限）*/
  .card-horizontal { grid-template-columns: 1fr; }
  .card-horizontal__media { aspect-ratio: 16 / 9; min-width: auto; }
}
```

---

## Liquid 実装例

### Standard
```liquid
{% raw %}<article class="card card-standard">
  <img src="{{ card.image | img_url: '600x' }}" alt="{{ card.image_alt }}"
       class="card__media" loading="lazy" width="600" height="400">
  <div class="card__body">
    <h3 class="card__title">{{ card.title }}</h3>
    <p class="card__text">{{ card.body }}</p>
    <a href="{{ card.url }}" class="btn btn-primary btn-md">
      {{ card.cta_label }}
    </a>
  </div>
</article>{% endraw %}
```

### Featured（Subscription Plan 等）
```liquid
{% raw %}<article class="card card-featured">
  <span class="card__badge">おすすめ</span>
  <h3 class="card__title">{{ plan.name }}</h3>
  <p class="card__price">¥{{ plan.price | money_without_currency }}/月</p>
  <ul class="card__features">
    {% for f in plan.features %}<li>✓ {{ f }}</li>{% endfor %}
  </ul>
  <a href="{{ plan.url }}" class="btn btn-primary btn-lg">このプランで始めてみる</a>
</article>{% endraw %}
```

### Horizontal（Case Study 一覧）
```liquid
{% raw %}<a href="{{ case.url }}" class="card card-horizontal">
  <img src="{{ case.image | img_url: '400x' }}" alt="{{ case.team }}"
       class="card-horizontal__media" loading="lazy">
  <div class="card-horizontal__body">
    <p class="card__eyebrow">CASE</p>
    <h3 class="card__title">{{ case.team }}</h3>
    <p class="card__text">{{ case.summary | truncate: 80 }}</p>
    <span class="btn btn-link">詳細を見る →</span>
  </div>
</a>{% endraw %}
```

### Flat（Stat / Quote）
```liquid
{% raw %}<div class="card card-flat">
  <p class="card__big-stat">-3.2<span>kg</span></p>
  <p class="card__label">3 ヶ月で平均減量</p>
  <a href="/case-studies" class="btn btn-link">事例を見る →</a>
</div>{% endraw %}
```

---

## CSS（v0.2 実装）

```css
/* === Card 基本 === */
.card {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  background: var(--bg-primary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--space-3);
  box-shadow: var(--shadow-1);
  transition: box-shadow var(--duration-base) var(--ease-out),
              transform var(--duration-base) var(--ease-out);
  text-decoration: none;
  color: inherit;
}

.card:hover {
  box-shadow: var(--shadow-3);
  transform: translateY(-2px);
}

.card:focus-visible {
  outline: 2px solid var(--color-focus-ring);
  outline-offset: 2px;
}

.card:active { transform: translateY(0); }

.card.is-disabled {
  opacity: 0.5;
  pointer-events: none;
}

.card.is-selected {
  border: 2px solid var(--color-drive);
  padding: calc(var(--space-3) - 1px);
}

/* === 内部要素 === */
.card__media {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  border-radius: var(--radius-sm);
}

.card__title {
  font-family: var(--font-ja);
  font-size: var(--fs-h3);
  font-weight: var(--fw-bold);
  color: var(--color-ink);
  letter-spacing: var(--ls-ja);
  line-height: var(--lh-heading);
}

.card__text {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-sub);
  line-height: var(--lh-body);
  letter-spacing: var(--ls-ja);
}

.card__eyebrow {
  font-family: var(--font-en);
  font-size: var(--fs-caption);
  font-weight: var(--fw-semibold);
  color: var(--color-drive);
  letter-spacing: var(--ls-en);
  text-transform: uppercase;
}

.card__badge {
  position: absolute;
  top: -12px;
  right: var(--space-3);
  padding: var(--space-1) var(--space-2);
  background: var(--color-drive);
  color: var(--color-white);
  border-radius: var(--radius-pill);
  font-family: var(--font-ja);
  font-size: var(--fs-caption);
  font-weight: var(--fw-semibold);
}

/* === Variants === */
.card-featured {
  position: relative;
  border: 2px solid var(--color-drive);
  padding: calc(var(--space-3) - 1px);
}

.card-flat {
  background: var(--bg-secondary);
  box-shadow: none;
  border: none;
}

.card-flat:hover {
  box-shadow: var(--shadow-1);
  transform: translateY(-1px);
}

/* === Horizontal（上記§Horizontal詳細を再掲）=== */
.card-horizontal {
  display: grid;
  grid-template-columns: 30% 70%;
  gap: var(--space-2);
  align-items: stretch;
}

.card-horizontal__media {
  min-width: 100px;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  border-radius: var(--radius-sm);
  overflow: hidden;
}

.card-horizontal__body {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  justify-content: space-between;
}

@media (max-width: 480px) {
  .card-horizontal { grid-template-columns: 1fr; }
  .card-horizontal__media { aspect-ratio: 16 / 9; min-width: auto; }
}
```

---

## Accessibility

- **Card 全体がリンクの場合**: `<a class="card">` で囲み、内部 Button は使わない（リンク内リンク禁止）
- **複数アクションがある場合**: Card 全体は `<article>`、内部に複数 `<a>`/`<button>` を持つ
- **focus-visible**: キーボード操作時のみ outline 表示
- **alt 属性**: `card__media` の `<img>` には必ず意味ある alt
- **見出し階層**: Card 内の `card__title` は文脈に応じて h2/h3/h4 を選ぶ（直接 h3 固定にしない）
- **selected 状態**: `aria-selected="true"` または `aria-pressed="true"` を補助で付与

---

## Do / Don't

### ✅ Do
- 全 Variants で CTA を 1 個以上配置（情報のみ Card は作らない）
- 影は `--shadow-1` 既定、hover で `--shadow-3` まで
- `--radius-md` を厳守（Pill は Button 専用）
- Featured バッジは 1 Card につき 1 個まで
- Horizontal は SP でも 30/70 を維持（極小 SP のみ縦折返し）

### ✕ Don't
- Pill radius を Card に使わない（Card は `--radius-md`）
- Drive 色を Card 背景にしない（Drive は CTA 専用）
- shadow-4/5 を使わない（エセ高級・Anti 違反）
- 「限定」「今だけ」等の煽りバッジを置かない
- Card 内に `<a>` を入れ子にしない（リンクネスト禁止）
- 全 Card に Featured 枠線を付けない（強調が消失）

---

## L4 Component への継承関係

| L4 Component | 継承する Variant | 追加要素 |
|---|---|---|
| Subscription Plan Card | Featured（推奨プラン）/ Standard（他プラン）| 価格 h2 / 食数 / 特典リスト / 2 CTA |
| Case Study Card（一覧）| Horizontal | チーム名 / 競技 / 主要数値 / Link CTA |
| Article Card | Standard | 公開日 / 著者 Avatar |
| Stat Card | Flat | BigStat 数値 / ラベル / 期間 |
| Hero Card（Bento Tile）| Standard / Horizontal | 大型画像 / Eyebrow ラベル |

L4 Component を作る際は **Card の上に拡張**する形で書く。Card の共通 CSS を上書きしない。

---

## Change Log
- v0.2 (2026-04-27): Worksheet §16 確定（4 Variants / SP 維持横長 / CTA 必須 / `.is-selected` Drive 枠 / 拡張余地あり）。既存 Liquid（fam-achievement / card-product / subscription-plan-card / case-study）の実測抽出をベースに L3 Pattern 化
