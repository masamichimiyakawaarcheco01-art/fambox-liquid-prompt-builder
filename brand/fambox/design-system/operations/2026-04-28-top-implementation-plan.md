---
title: TOPページ DNA 反映 実装計画 v0.1
type: design-system-operations
layer: L7-Operations / L5-Templates
status: active
created: 2026-04-28
deadline: 2026-05-29（OKR Task 2-1-a）
owner: 宮川
purpose: DS v0.2 確定 Spec を TOPページ既存 25 sections に適用するためのタスク計画。改修の優先度・依存関係・所要時間を定義し、5/29 期限から逆算したスケジュールを提示する。
---

# TOPページ DNA 反映 実装計画（2026-04-28 作成 / 5/29 期限）

## サマリ

- **TOPページ構成**: `projects/fambox/templates/index.json` に **25 sections** 定義
- **改修対象**: 14 sections（DNA 反映必須・全て Liquid 実体ファイルあり）
- **適用 Spec**: DS v0.2 で確定済の 9 Component（Hero / Header / Footer / Bento Grid / Bento Tile / Card / Subscription Plan / Case Study / Button v0.3）
- **逆算工数**: 約 32-48 時間（30 日間で 1.5h/日 ペース）

---

## 1. Section × Spec マッピング（25 sections 全件）

### Tier 1: TOP 主役・5/29 期限直撃（7 sections / 改修必須）

| # | section type | 既存 Liquid 行数 | 適用 Spec | 改修内容 | 工数 |
|---|---|---|---|---|---|
| 1 | `fambox-hero-v17` | 578 | **Hero Section v0.2** `hero-video-split` Variant | クラス名統一（fv17-* → hero-*）/ tokens.css 適用 / parallax 設定 | 4h |
| 2 | `fam-achievement` | 306 | **Card Pattern v0.2** `card-horizontal` 派生 (ticker) | クラス名統一 / fam-achievement__card → card / トークン適用 | 2h |
| 3 | `fam-voices` | 529 | **Bento Grid v0.2 (autofit)** + Bento Tile **stat-focus** Variant | グリッド再構築 / Voice タイル化 / Avatar v0.2 適用 | 4h |
| 4 | `fam-item` | 300 | **Bento Grid v0.2 (editorial)** + Bento Tile **image-fill** Variant | 商品カード Bento 化 / Image-fill 適用 | 3h |
| 5 | `fam-subscription-plan` | 506 | **Subscription Plan Card v0.3** 直接適用 | クラス名統一 / 8 項目化（最低契約期間・初月特典 削除）/ 2 CTA 統一 | 3h |
| 6 | `fam-nav`（Footer 直前ナビ）| 208 | **Footer v0.2** または Bento Grid Standard | Footer Spec に統合 or 別 Component 化判断 | 2h |
| 7 | Header（共通 layout）| - | **Header v0.2** `header-standard header--sticky header--default` | theme.liquid から呼び出し / 横スクロールメニュー実装 / aria-label 付与 | 3h |

### Tier 2: TOP 補助・優先度中（5 sections / 改修推奨）

| # | section type | 既存 Liquid 行数 | 適用 Spec | 改修内容 | 工数 |
|---|---|---|---|---|---|
| 8 | `fam-spirit` | 841 | **Bento Grid v0.2 (editorial)** + Bento Tile **glass** Variant | spirit_card → bento-glass / 主構図対角線適用 | 5h |
| 9 | `fam-plan-features` | 396 | **Card Pattern v0.2** `card-standard` Grid | feature card 統一 / トークン適用 | 2h |
| 10 | `fambox-value-proposition` | 520 | **Bento Grid v0.2 (standard)** + Bento Tile **standard** | value_card → bento-standard / 4-6 タイル構成 | 3h |
| 11 | `fambox-menu-showcase` | 264 | 専用 Pattern として保持（横スクロール track）/ 部分的にトークン適用 | tokens.css 適用のみ（構造変更なし）| 1h |
| 12 | `fambox-easy-cooking` | 351 | **Card Pattern v0.2** `card-horizontal` または **Hero Section** `image-editorial` `tall` | レイアウト判断後に適用 | 2h |

### Tier 3: TOP 末尾コンテンツ・優先度低（2 sections / 軽微改修）

| # | section type | 既存 Liquid 行数 | 適用 Spec | 改修内容 | 工数 |
|---|---|---|---|---|---|
| 13 | `fambox-faq` | 433 | Future L3 Accordion Spec（未着手）| v0.3 Spec 化後に改修。今は tokens.css のみ適用 | 1h |
| 14 | `fambox-profile` | 380 | **Card Pattern v0.2** `card-horizontal` + Avatar v0.2 | profile-card → card 統一 | 2h |

### Tier 4: 既存維持（改修なし・11 sections）

以下は Shopify dawn 標準 / カスタム Liquid で構造変更不要（tokens.css 適用のみ・各 0.5h 程度）:

- `fam-active-plans-v2` (710 lines) — 既存 Plan ダッシュボード
- `custom-liquid` × 3 — 個別カスタム
- `rich-text` × 2 — Shopify 標準
- `collage` × 2 — Shopify 標準
- `image-with-text` × 2 — Shopify 標準
- `multirow` × 1 — Shopify 標準
- `custom-blog-carousel` — 既存ブログ一覧

合計 11 sections × 0.5h = **5.5h**

---

## 2. 工数サマリ

| Tier | sections | 工数 | 累計 |
|---|---|---|---|
| Tier 1（5/29 期限直撃）| 7 | 21h | 21h |
| Tier 2（優先度中）| 5 | 13h | 34h |
| Tier 3（優先度低）| 2 | 3h | 37h |
| Tier 4（既存維持・トークン適用のみ）| 11 | 5.5h | **42.5h** |

→ **総工数 約 42.5h**（5/29 まで 30 日 / 1.5h/日 で完了可能）

---

## 3. 推奨スケジュール（5/29 から逆算・30 日間）

### Week 1（4/28-5/4）: Tier 1 前半・基盤
- Day 1-2: Header 実装 + theme.liquid 呼び出し統一（3h）
- Day 3-4: Hero v17 改修（4h・PC/SP 動作確認）
- Day 5-6: Subscription Plan Card 改修（3h）
- Day 7: 中間レビュー・GTAG 確認

### Week 2（5/5-5/11）: Tier 1 後半・主役
- Day 8-10: fam-voices Bento 化（4h・最大の構造変更）
- Day 11-12: fam-item Bento 化（3h）
- Day 13: fam-achievement 改修（2h）
- Day 14: fam-nav 整理（2h）

### Week 3（5/12-5/18）: Tier 2 前半
- Day 15-17: fam-spirit Bento 化（5h・最も重い改修）
- Day 18-19: value-proposition Bento 化（3h）
- Day 20-21: plan-features 改修（2h）

### Week 4（5/19-5/25）: Tier 2 後半 + Tier 3
- Day 22: menu-showcase トークン適用（1h）
- Day 23-24: easy-cooking 改修（2h）
- Day 25: FAQ 軽微改修（1h）
- Day 26-27: profile 改修（2h）
- Day 28: Tier 4 全 sections の tokens.css 適用（5.5h を 1 日に圧縮）

### Week 5（5/26-5/29）: 仕上げ・QA
- Day 29: クロスブラウザ・SP 動作確認・パフォーマンス計測
- Day 30: 本番反映 / GA4 イベント確認 / OKR Excel 更新

---

## 4. クリティカルパス・依存関係

```
[Header 実装]
    ↓（theme.liquid 経由で全画面共通）
[Hero v17 改修] ━━━━━━━━━━━━━┓
                              ↓
[Subscription Plan Card 改修]  ┃
                              ↓
[fam-voices Bento 化] ━━━━━━━━┫ ※ Bento Tile / Grid Spec 必須前提
                              ↓
[fam-item Bento 化]            ┃
                              ↓
[fam-achievement 改修]         ┃
                              ↓ ※ Card Pattern Spec 必須前提
[fam-nav 整理]                 ↓
                              ━━━ Tier 1 完了（5/11 想定）
                              ↓
[Tier 2 着手 → Tier 3 → Tier 4]
                              ↓
[QA → 本番反映]（5/29）
```

---

## 5. リスク・未確定事項

### High リスク
- **Bento Tile / Grid の本番動作未検証**: Spec のみで実装サンプルなし。fam-voices で初実装の予定だが、IE 含む対応や JS パララックス挙動は要検証
- **fam-spirit の DNA 反映**: 既存 841 行の複雑な Liquid。Bento 化で構造大改変必要・工数 5h は楽観値かも

### Medium リスク
- **fam-active-plans-v2** の改修判断: Tier 4（既存維持）扱いだが、ダッシュボード UI として Bento Grid Auto-fit 適用すべきか別判断必要
- **GA4 計測の継続性**: data-gtag-cta / data-gtag-nav 属性を改修時に必ず保持。grep 検証で漏れ防止

### Low リスク
- Shopify 標準 sections（rich-text / collage 等）: tokens.css 適用のみで影響軽微
- custom-liquid × 3: 個別判断で v0.3 以降に延期可

---

## 6. 検証チェックリスト（各 section 改修時に共通）

- [ ] クラス名が DS 命名規則（`{component}-{variant}--{modifier}`）に従う
- [ ] tokens.css 変数を直書き値の代わりに使用（color / space / radius / shadow / z-index）
- [ ] Anti-pattern を踏まない（各 Spec の Don't 節を確認）
- [ ] Pre-existing data-gtag-* 属性を保持（GA4 計測継続）
- [ ] PC / Tablet / SP 全レンジで動作確認
- [ ] WCAG 2.1 AA（コントラスト 4.5:1 / Touch target 44px / Focus ring）
- [ ] `prefers-reduced-motion` 対応
- [ ] grep 検証で旧クラス名が残っていないこと

---

## 7. 並行作業（Spec 化を続ける）

実装を進めながら、以下の Spec を並行で確定させる:

- **L4 Modal**（5/12 までに）: Plan 選択確認 / Contact Form 確認で必要
- **L3 Stat Card 独立 Pattern 化**（5/14 までに）: Bento Tile stat-focus を Card 派生で抽出
- **L7 Operations 運用ルール**（5/30 以降）: v0.2 完成基準・Naming / Versioning / Contribution / Deprecate
- **L4 FAQ Accordion**（5/20 までに）: Tier 3 fambox-faq 改修の前提
- **L4 Profile Card**（5/22 までに）: Tier 3 fambox-profile 改修の前提

---

## 8. 5/29 完成判定基準

- ✅ Tier 1 全 7 sections が DS v0.2 Spec 適用済み
- ✅ Tier 2 全 5 sections が tokens.css 適用済み（構造変更も望ましい）
- ✅ Tier 4 全 sections が tokens.css 適用済み
- ✅ クロスブラウザ動作確認（Chrome / Safari / Firefox / Edge / iOS Safari / Chrome Android）
- ✅ Lighthouse スコア低下なし（Performance / A11y / SEO 各 90+ 維持）
- ✅ GA4 既存イベント発火継続（funnel_step / cta_click / page_view）
- ✅ OKR Excel `FAMBOX_OKR_宮川.xlsx` Task 2-1-a 完了マーク
