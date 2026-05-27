---
title: FAMBOX Component — Subscription Plan Card
type: design-system
layer: L4-Components
component: SubscriptionPlanCard
version: 0.3
status: confirmed
last_updated: 2026-04-27
owner: 宮川
deadline: 2026-06-12（OKR Task 2-1-b 定期便ページ）
source: Worksheet §13（2026-04-20 確定 + 2026-04-27 S3 縮小：最低契約期間・初月特典 不採用）
brand_alignment:
  - Integrity: 価格を煽らず、ベネフィット訴求を主役に
  - Co-driven: 2CTAで「即決」「相談」両方をフォロー
  - Anti: Drive色64px価格は煽り → Ink色h2で誠実に
related:
  - components/button.md
  - components/cta-wording-proposal.md
---

# Subscription Plan Card — Component

定期便プランの選択肢を提示する Component。**OKR Task 2-1-b で6月期限**。Brand DNA Integrity を価格訴求でも体現。

## ブランド整合性
- **Integrity**: 価格は誠実に、煽らない（h2サイズ・Ink色）
- **Co-driven**: 「即決派」「相談派」の両方に2CTA を提供
- **Anti**: 「今だけ！」「限定！」等の煽りは使わない

---

## 表示情報（8項目 / 2026-04-27 確定）

| # | 項目 | 表示位置 | 補足 |
|---|---|---|---|
| 1 | プラン名 | カード上部・h3 | 例: "Pro Athlete Plan" |
| 2 | 価格（税込） | 上部 | h2 32px / Ink色 |
| 3 | 提供頻度 | 価格隣 | 「月1回 / 週2回」等 |
| 4 | 1回あたりの食数 | 中部 | 例: 「7食 × 4回 = 28食/月」 |
| 5 | カスタマイズ可否 | 中部 | 「○ 個別対応可」「△ 限定」「× 不可」 |
| 6 | 推奨対象 | 中部 | 「ジュニア / 大学生 / プロ」 |
| 7 | 特典・サポート内容 | 下部リスト | チェックリスト形式 |
| 8 | CTA × 2 | 最下部 | Primary + Ghost |

### 不採用（2026-04-27 §13.1.a C 採択）
- ✕ **最低契約期間** — カード内では非表示。FAQ ページ・規約ページ・問合せ時の説明で扱う
- ✕ **初月特典** — カード内では非表示。キャンペーン施策（バナー / メールマガジン / LP セクション別建て）で扱う

---

## レイアウト構造

```
┌────────────────────────────────────────┐
│ [おすすめバッジ] ← 1プランのみ          │
│                                        │
│ Pro Athlete Plan          ← h3         │
│                                        │
│ ¥48,000 / 月              ← h2 Ink     │
│                                        │
│ ─────────────────────────────────────  │
│ 食数: 7食 × 4回 = 28食/月              │
│ カスタマイズ: ○ 個別対応可             │
│ 推奨対象: プロ・実業団                  │
│                                        │
│ ─────────────────────────────────────  │
│ 含まれるもの                            │
│ ✓ 個別栄養設計                          │
│ ✓ 月1回の栄養相談                       │
│ ✓ 配送時の体調ヒアリング                │
│                                        │
│ ─────────────────────────────────────  │
│ [このプランで始めてみる]   ← Primary    │
│ [話を聞いてみる]           ← Ghost      │
└────────────────────────────────────────┘
```

---

## 価格訴求（§13 Q2 確定）

**🎯 確定: 中くらい（`--fs-h2` 32px / Ink色）**

```css
.plan-price {
  font-family: var(--font-en);
  font-size: var(--fs-h2);          /* 32px */
  font-weight: var(--fw-bold);
  color: var(--color-ink);          /* Drive色は使わない */
  letter-spacing: var(--ls-en);
  line-height: 1;
}

.plan-price__unit {
  font-size: var(--fs-body);        /* 16px 「/月」など */
  font-weight: var(--fw-regular);
  color: var(--color-sub);
  margin-left: var(--space-1);
}
```

### 理由
- Drive色64pxは「煽り」になり Anti違反
- Brand DNA Integrity = 結果保証ではなく **価値で選ばれる立場**
- 価格は誠実に提示、ベネフィット訴求を主役に

---

## CTA配置（§13 Q3 確定）

**🎯 確定: カード下部・複数CTA（2つ）**

| 階層 | 文言 | スタイル |
|---|---|---|
| Primary | **このプランで始めてみる** | Pill / Drive色 / LG |
| Secondary | **話を聞いてみる** | Ghost / Ink色 |

```html
<div class="plan-card__actions">
  <a href="{{ subscribe_url }}" class="btn btn-primary btn-lg">
    このプランで始めてみる
  </a>
  <a href="/contact" class="btn btn-ghost">
    話を聞いてみる
  </a>
</div>
```

```css
.plan-card__actions {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin-top: var(--space-4);
}
```

### 理由
- 比較検討段階のユーザーに2選択肢提示
- 即決派（Primary CTA）と相談派（Secondary CTA）の両方をフォロー
- Co-driven 思想と整合

---

## バッジ（§13 Q4 確定）

**🎯 確定: 「おすすめ」バッジ Drive色 — 1プランのみ表示**

```html
<div class="plan-card plan-card--featured">
  <span class="plan-card__badge">おすすめ</span>
  <!-- ... -->
</div>
```

```css
.plan-card__badge {
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
  letter-spacing: var(--ls-ja);
}
```

### 理由
- **1プランのみ**に付ける。全プランに付けると意味が消失
- 「人気」「新規」等は併用しない（迷い増加）
- 「限定」「お得」は Brand DNA Anti で禁止

---

## カード全体スタイル

```css
.plan-card {
  position: relative;
  background: var(--bg-primary);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  transition: box-shadow var(--duration-base) var(--ease-out),
              transform var(--duration-base) var(--ease-out);
}

.plan-card:hover {
  box-shadow: var(--shadow-3);
  transform: translateY(-2px);
}

.plan-card--featured {
  border: 2px solid var(--color-drive);
  /* バッジ突出のため z-index */
  z-index: var(--layer-1);
}
```

---

## 一覧レイアウト（複数プラン並列）

| デバイス | カラム数 | ガター |
|---|---|---|
| SP (〜767px) | 1 | - |
| Tablet (768-1023px) | 2 | `var(--space-3)` 24px |
| PC (1024px〜) | 3 | `var(--space-4)` 32px |

```css
.plan-grid {
  display: grid;
  gap: var(--space-3);
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .plan-grid { grid-template-columns: repeat(2, 1fr); gap: var(--space-3); }
}

@media (min-width: 1024px) {
  .plan-grid { grid-template-columns: repeat(3, 1fr); gap: var(--space-4); }
}
```

---

## Liquid 例

```liquid
{% raw %}<article class="plan-card{% if plan.featured %} plan-card--featured{% endif %}">
  {% if plan.featured %}
    <span class="plan-card__badge">おすすめ</span>
  {% endif %}

  <h3 class="text-h3">{{ plan.name }}</h3>

  <p class="plan-price">
    ¥{{ plan.price | money_without_currency }}<span class="plan-price__unit">/月（税込）</span>
  </p>

  <dl class="plan-card__specs">
    <dt>食数</dt><dd>{{ plan.meal_count }}食 × {{ plan.frequency }}回 = {{ plan.total }}食/月</dd>
    <dt>カスタマイズ</dt><dd>{{ plan.customizable }}</dd>
    <dt>推奨対象</dt><dd>{{ plan.target }}</dd>
  </dl>

  <ul class="plan-card__features">
    {% for feature in plan.features %}
      <li>✓ {{ feature }}</li>
    {% endfor %}
  </ul>

  <div class="plan-card__actions">
    <a href="{{ plan.subscribe_url }}" class="btn btn-primary btn-lg">
      このプランで始めてみる
    </a>
    <a href="/contact" class="btn btn-ghost">
      話を聞いてみる
    </a>
  </div>
</article>{% endraw %}
```

---

## Accessibility
- ✅ 各 Card に `<article>` タグ・h3 で見出し階層維持
- ✅ 価格は SR 用に「48000円 月額」など読み上げを意識
- ✅ Featured カードは `aria-label="おすすめプラン"` 等補足

---

## Do / Don't

### ✅ Do
- 価格は **h2 / Ink色** で誠実に
- 推奨は **1プランのみ**
- 契約条件・特典はカード内に詰め込まず、FAQ / 別建てセクションで扱う

### ✕ Don't
- 価格を Drive色 64px の煽り表現にしない
- 「期間限定」「今だけ」等の煽り文言を入れない
- 全プランに「おすすめ」「人気」等のバッジを付けない
- ベネフィットを箇条書き10個以上で並べない（読まれない）

---

## Change Log
- v0.3 (2026-04-27): Worksheet §13 縮小（10→8項目）— 最低契約期間・初月特典をカードから外し FAQ/キャンペーン側へ移管（§13.1.a C 採択）
- v0.2 (2026-04-20): Worksheet §13 確定（10項目構成・h2 Ink価格・2CTA・1バッジ）
