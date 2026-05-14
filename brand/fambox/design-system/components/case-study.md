---
title: FAMBOX Component — Case Study / Testimonial
type: design-system
layer: L4-Components
component: CaseStudy
version: 0.2
status: confirmed
last_updated: 2026-04-20
owner: 宮川
deadline: 2026-09-30（OKR Task 3-1-g 実績コンテンツ）
source: Worksheet §14（2026-04-20 確定）
brand_alignment:
  - Integrity: 結果より「取り組みの質と継続」を伝える
  - Co-driven: チームと FAMBOX の対等な関係を表現
  - Anti: ブランド借り（有名選手起用のみ）を避け、実績の幅を見せる
related:
  - components/avatar.md
  - components/cta-wording-proposal.md
---

# Case Study / Testimonial — Component

実績・事例の Component。**Brand DNA Integrity「確率を上げる」を体現する最重要コンテンツ**。

## ブランド整合性
- **Integrity**: 「結果は言い切らない、取り組みの質を語る」
- **Co-driven**: チームと FAMBOX の **共創ストーリー** として描く
- **Scientific**: 数値データで根拠を示す（NutrientRing / TrendLine）
- **Anti**: 「必ず勝てる」「劇的に変わった」等の煽り表現禁止

---

## 表示項目（10項目）

| # | 項目 | 必須? | 表示位置 | 補足 |
|---|---|---|---|---|
| 1 | チーム名・競技 | ✅必須 | 上部 | 例: "○○高校サッカー部" |
| 2 | 選手写真（許諾済）| 状況依存 | Hero | 顔出しNGなら背中・俯瞰 |
| 3 | 監督・栄養士名 | 任意 | 上部 | Avatar併用 |
| 4 | 導入前の課題 | ✅必須 | Before | 具体的に |
| 5 | 導入後の変化 | ✅必須 | After | 数字あれば添える |
| 6 | 具体データ | ✅推奨 | Data Viz | 体重/体脂肪/コンディション等 |
| 7 | 推薦コメント（引用）| ✅推奨 | 中部 | 監督 or 栄養士の声 |
| 8 | 継続期間 | ✅必須 | メタ | 「導入から12ヶ月」等 |
| 9 | **食事戦略の概要** ★追加 | ✅推奨 | 中部 | 手段の透明性 = Integrity体現 |
| 10 | 関連事例リンク | 任意 | 下部 | 他Case Study への動線 |

---

## レイアウトパターン（複数組み合わせ）

**🎯 確定: 3パターンを併用（用途別）**

### パターン1: カード一覧（タイル）
**用途**: 一覧ページ・関連事例エリア

```
┌─────────┐ ┌─────────┐ ┌─────────┐
│ [写真]  │ │ [写真]  │ │ [写真]  │
│ チーム名 │ │ チーム名 │ │ チーム名 │
│ 競技     │ │ 競技     │ │ 競技     │
│ 主要数値 │ │ 主要数値 │ │ 主要数値 │
└─────────┘ └─────────┘ └─────────┘
```

### パターン2: ストーリー形式（縦長記事）
**用途**: 詳細ページ（1事例 1ページ）

```
┌────────────────────────────────────┐
│ [Hero 写真 全幅]                    │
│                                    │
│ ○○高校サッカー部                    │
│ 12ヶ月の食事改革                    │
│                                    │
│ ─────────────────────────────────  │
│ Before（導入前の課題）              │
│ 「練習後の集中力が...」              │
│                                    │
│ After（導入後の変化）               │
│ 「シーズン最後まで...」              │
│                                    │
│ [Data Viz: TrendLine 12ヶ月]        │
│                                    │
│ 食事戦略のポイント                   │
│ - タンパク質...                     │
│ - 試合前24h...                      │
│                                    │
│ 監督の声                            │
│ 「FAMBOXと出会って...」              │
│                                    │
│ [話を聞いてみる]                    │
└────────────────────────────────────┘
```

### パターン3: ロゴリスト
**用途**: TOPページ実績エリア（社会的証明）

```
社会的証明セクション
ご利用チーム

[Logo] [Logo] [Logo] [Logo] [Logo]
[Logo] [Logo] [Logo] [Logo] [Logo]
```

---

## データ可視化の併用（§14 Q3 確定）

**🎯 確定: 全部活用（用途別）**

| Viz | 用途 | 表示場所 |
|---|---|---|
| **NutrientRing** | 栄養バランス改善（前後比較）| ストーリー形式詳細 |
| **TrendLine** | 体重・体脂肪率の継続データ | ストーリー形式詳細 |
| **BigStat** | 主要数値ハイライト（「-3kg / 3か月」等）| カード一覧 + ストーリー両方 |

### BigStat 例
```html
<div class="big-stat">
  <span class="big-stat__value">-3.2<span class="big-stat__unit">kg</span></span>
  <span class="big-stat__label">体脂肪率</span>
  <span class="big-stat__period">3ヶ月</span>
</div>
```

```css
.big-stat {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-1);
}

.big-stat__value {
  font-family: var(--font-en);
  font-size: var(--fs-display);   /* 56px */
  font-weight: var(--fw-bold);
  color: var(--color-drive);
  line-height: 1;
  letter-spacing: var(--ls-en);
}

.big-stat__unit {
  font-size: 0.4em;
  color: var(--color-sub);
  margin-left: var(--space-1);
}

.big-stat__label {
  font-family: var(--font-ja);
  font-size: var(--fs-body);
  color: var(--color-ink);
}

.big-stat__period {
  font-size: var(--fs-caption);
  color: var(--color-caption);
}
```

---

## 匿名化の扱い（§14 Q4 確定）

**🎯 確定: 混在（公表OKを優先・NGは匿名）**

### 公表OK（許諾取得済）
- 実名で表記: 「○○高校サッカー部」「監督 ○○氏」
- Hero 事例として上位表示
- 写真も顔出し可能

### 匿名扱い
- 「A高校サッカー部・関東地方」レベル
- データは出すが個人特定不可レベルに留める
- Avatar はイニシャル fallback

### マークアップ規則
```liquid
{% raw %}{% if case.public %}
  <h3>{{ case.team_name }}</h3>
  <p>監督: {{ case.coach_name }}</p>
{% else %}
  <h3>{{ case.team_initial }}{{ case.category }}・{{ case.region }}</h3>
  <p>監督: {{ case.coach_initial }}氏</p>
{% endif %}{% endraw %}
```

---

## カード一覧スタイル

```css
.case-grid {
  display: grid;
  gap: var(--space-3);
  grid-template-columns: 1fr;
}

@media (min-width: 768px) { .case-grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .case-grid { grid-template-columns: repeat(3, 1fr); } }

.case-card {
  background: var(--bg-primary);
  border-radius: var(--radius-md);
  overflow: hidden;
  box-shadow: var(--shadow-1);
  transition: transform var(--duration-base) var(--ease-out),
              box-shadow var(--duration-base) var(--ease-out);
}

.case-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-3);
}

.case-card__image {
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

.case-card__body {
  padding: var(--space-3);
}
```

---

## ストーリー形式（詳細ページ）

```liquid
{% raw %}<article class="case-story">
  <header class="case-story__hero">
    <img src="{{ case.hero_image | img_url: '1200x' }}" alt="{{ case.alt }}">
    <div class="case-story__hero-text">
      <p class="text-eyebrow">CASE STUDY</p>
      <h1 class="text-h1">{{ case.title }}</h1>
      <p class="text-lead">{{ case.subtitle }}</p>
    </div>
  </header>

  <section class="case-story__before-after">
    <div>
      <h2 class="text-h3">Before — 導入前の課題</h2>
      <p>{{ case.before }}</p>
    </div>
    <div>
      <h2 class="text-h3">After — 導入後の変化</h2>
      <p>{{ case.after }}</p>
    </div>
  </section>

  <section class="case-story__data">
    {% render 'big-stat', value: case.main_change, unit: case.unit, label: case.metric, period: case.period %}
    {% render 'trend-line', data: case.trend_data %}
  </section>

  <section class="case-story__strategy">
    <h2 class="text-h2">食事戦略のポイント</h2>
    <ul>
      {% for point in case.strategy_points %}<li>{{ point }}</li>{% endfor %}
    </ul>
  </section>

  <blockquote class="case-story__quote">
    <p>{{ case.testimonial }}</p>
    <cite>
      {% render 'avatar', user: case.coach, size: 'md' %}
      {{ case.coach.name }}（{{ case.team_name }} 監督）
    </cite>
  </blockquote>

  <footer class="case-story__cta">
    <a href="/contact" class="btn btn-primary btn-lg">話を聞いてみる</a>
    <a href="/case-studies" class="btn btn-ghost">他の事例を見る</a>
  </footer>
</article>{% endraw %}
```

---

## トーン規律

### ✅ Brand DNA に即した表現
- 「12ヶ月の継続で、選手のコンディションが安定しました」
- 「目に見える変化が出るまでに3ヶ月、定着までに半年かかりました」
- 「データで言うと体脂肪率が ○% 下がりました」

### ✕ 禁止表現（Anti違反）
- 「劇的に変わりました！」（誇張）
- 「FAMBOXのおかげで全国大会優勝！」（因果を断定）
- 「絶対におすすめ」（保証表現）

---

## Accessibility
- ✅ 引用は `<blockquote>` タグ・`<cite>` で出典明示
- ✅ Data Viz には alt 説明を必ず付ける
- ✅ 写真の alt は具体的に（「練習後ロッカーで食事を取る選手たち」）

---

## Do / Don't

### ✅ Do
- Before/After を **数字で示す**（誠実）
- 食事戦略の **手段を開示**（透明性）
- 公表OK事例を Hero に・匿名は補足に

### ✕ Don't
- 「劇的」「絶対」「保証」等の煽り言葉を使わない
- 因果を断定しない（「FAMBOXで優勝」ではなく「12ヶ月の継続で安定」）
- ロゴだけ並べて中身がない実績アピールはしない

---

## Figma 参照

- File: `FAMBOX Design System`（`QsiBrc2v20BYw76YHI9x3e`）
- Page: `5. Components Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study`
- **Component Set ID**: `66:91` ✅（Audit #4 で既存確認、2026-05-12）
- **実装済 variants**: 2（`variant`: tile / story）
- ⚠ Spec gap: spec §14 は「3 レイアウト併用」想定。tile/story の 2 variant で足りるか v0.3 で要レビュー
- 📝 Liquid 側では spec §14 準拠で 3 patterns（tile-grid / story / logo-list）を全て実装済。Figma 側の logo-list variant 追加が v0.3 残課題

## Liquid 実装

- **File**: `sections/fambox-case-study.liquid`（1102 行）
- **Patterns**: tile-grid / story / logo-list の 3 種を 1 file に統合（spec §レイアウトパターン 完全準拠）
- **Schema**: 35 settings + 3 block types (`case_card` / `strategy_point` / `logo_item`) + 3 presets
- **Tile Grid**: 3列レスポンシブ / Big Stat（Drive 色固定）/ カード全体リンク化（link_url 指定時に `<a>` タグ切替）
- **Story**: Hero + Before/After + Big Stat（Dark 背景）+ Strategy points (`strategy_point` block) + Quote + CTA 2 種
- **Logo List**: 2-5 列レスポンシブ / grayscale + opacity 0.7 → hover で復元（控えめな社会的証明）
- **トーン規律準拠**: preset の placeholder 文言を「煽り表現禁止」（spec §トーン規律）に準拠
  - ✅「12 ヶ月の継続で安定」「コンディションが安定」「練習強度を維持」
  - ✕「劇的」「絶対」「保証」「優勝」は使用していない
- **Accessibility**: `<blockquote>` + `<cite>` で出典明示 / 画像 alt は具体的に設定可能 / `role="list"` で grid 化
- **既存 fam-case-study.liquid との関係**: 旧ブログ記事用 story Liquid は**並存保持**（Footer と同じ判断）

## 既存 fam-case-study.liquid との関係

| 項目 | fam-case-study.liquid（旧）| fambox-case-study.liquid（新）|
|---|---|---|
| 用途 | ブログ記事テンプレ専用（1 story per article）| DS 標準（3 patterns 切替）|
| Pattern | story 1 種のみ | tile-grid / story / logo-list 3 種 |
| Block | thumbnail / 区切り / 本文ブロック | case_card / strategy_point / logo_item |
| spec 準拠 | 旧 worksheet 由来 | spec v0.2 §14 完全準拠 |
| トーン | 自由記述 | placeholder で煽り表現を排除 |
| 用途 | 個別ブログ記事 | TOP / 事例一覧 / 関連事例 / 社会的証明 |

移行戦略: 個別ブログ記事は `fam-case-study.liquid` を継続使用。TOP / 一覧ページは `fambox-case-study.liquid` の preset から選択。Week 5 QA で TOP 反映時に判断。

## Change Log
- v0.2-liquid (2026-05-14): `fambox-case-study.liquid` 三位一体達成。spec §レイアウトパターン 3 patterns（tile-grid / story / logo-list）を 1 file に統合。3 block types + 3 presets。煽り表現排除の placeholder 整備。fam-case-study.liquid とは並存（後者はブログ記事用として保持）
- v0.2-figma (2026-05-12): Audit #4 で Component Set `66:91` を既存確認。tile / story の 2 variant 実装済
- v0.2 (2026-04-20): Worksheet §14 確定（3レイアウト併用・全Data Viz活用・公表/匿名混在）
