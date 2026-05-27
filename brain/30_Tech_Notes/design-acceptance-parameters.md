---
title: デザイン承認 — 合格パラメーター（ガードレール仕様）
date: 2026-05-15
tags: [design-system, guardrails, acceptance-criteria, p0-foundation, ai-era, liquid, shopify, fambox]
topics: [design, engineering, ai]
status: active
priority: high
scope: "ARCHECO/FAMBOX/守屋企画 等の全UI制作物"
related:
  - skill-obsolescence-risk-audit.md
  - obara-ai-agent-era-ep1.md
  - ../50_Business_Context/fambox-brand-dna-axes.md
---

# デザイン承認 — 合格パラメーター（ガードレール仕様）

## 目的

AIエージェント時代の **「Human-on-the-Loop」** を実現するため、デザイン承認の判断基準を **パラメーター化** する。これにより：

- AI生成案を **自動評価** できる
- 人間レビューは **境界事例のみ** に絞れる
- クライアント承認フローを **基準ベース** で運用できる
- 個別判断の属人化を防ぐ

## 適用範囲

| 対象 | 必須適用 | 補助適用 |
|---|---|---|
| FAMBOX Shopify テーマ・セクション | ✅ | |
| FAMBOX 食事診断ウィザード | ✅ | |
| 守屋選手企画 営業チラシ・SNS素材 | ✅ | |
| LPB v4 で生成する全Liquid | ✅ | |
| FAM親ブランド資料 | ✅ | |
| クライアント業務（個別） | 案件ごとに合意 | |

例外（適用しない領域）：
- 試作・モックアップ段階（探索フェーズ）
- アート寄りの一点物作品
- 既存ブランドの引き継ぎ作業（既存ルールが優先）

---

## 1. カラー（必須）

| 項目 | 合格基準 | 不合格時の動作 |
|---|---|---|
| **色数（メインビジュアル全体）** | ≤ 5色 | 警告：色を統合 or 候補絞り込み |
| **アクセシビリティコントラスト** | テキスト/背景: **WCAG 2.1 AA以上**（4.5:1 通常 / 3:1 大文字） | 自動却下：色変更案を提示 |
| **FAMBOX ブランド準拠** | brand/fambox/ のカラートークンから外れない | 警告：トークン追加 or 不採用判断 |
| **画像上テキスト処理** | グラデOL / 単色OL / テキストシャドウ / 透過防止 のいずれか必須 | 警告：処理を追加 |

### FAMBOX 軸との接続
- [軸1 静の信頼](../50_Business_Context/fambox-brand-dna-axes.md) → モノトーン or 抑制された配色
- [軸2 動の発火](../50_Business_Context/fambox-brand-dna-axes.md) → 鮮やかな配色 OK
- [軸3候補 努力の結晶](../50_Business_Context/fambox-brand-dna-axes.md) → 透明感・氷色系

---

## 2. タイポグラフィ（必須）

| 項目 | 合格基準 | 不合格時の動作 |
|---|---|---|
| **使用フォントファミリー** | FAMBOXは **Poppins + Hiragino 固定**（Archivo/Space Grotesk/Manrope等の重いスポーツ系Displayは不可）<br>※ [feedback_fam_typography](memory) | 自動却下 |
| **フォントウェイトの種類** | 1セクション内で ≤ 3種類 | 警告 |
| **スケール段数** | 6段階以下（飾り/大H1/大中H2/中H3/中小Body/最小Small） | 警告 |
| **行間（line-height）** | 1.4 〜 2.0 の範囲 | 警告 |
| **最小フォントサイズ** | PC: 12px以上、SP: 11px以上 | 自動却下 |
| **ジャンプ率** | デザインテイストに応じて 低（高級）/中/高（躍動） を選択 | 警告：意図確認 |

---

## 3. レスポンシブ・レイアウト（必須）

| 項目 | 合格基準 | 不合格時の動作 |
|---|---|---|
| **ブレイクポイント** | 最低 4 段階：PC 1200+/Tablet 768〜1199/SP 360〜767/小型SP〜359 | 自動却下 |
| **PC最大幅** | 1200px 以上を想定して設計 | 警告 |
| **コンテンツ幅の比率** | 整数比（1:1, 1:2, 2:3, 1:3, full）に準拠 | 警告 |
| **SP横スクロール** | 発生させない（`overflow-x: hidden` か responsive 設計） | 自動却下 |
| **タッチターゲット最小サイズ** | 44px × 44px（モバイル） | 警告 |

---

## 4. スペーシング（必須）

| 項目 | 合格基準 | 不合格時の動作 |
|---|---|---|
| **スケール定義** | S/M/L の等比率（1.5x or 2x） | 警告：等差は避ける |
| **コンテナ→子要素** | スペーシングスケール内の値のみ | 警告 |
| **マージン崩れ** | `margin` collapse を考慮した設計 | 警告 |

---

## 5. パフォーマンス（必須）

| 項目 | 合格基準 | 不合格時の動作 |
|---|---|---|
| **Lighthouse Performance** | モバイル 70+、PC 85+ | **自動却下** |
| **Lighthouse Accessibility** | 90+ | **自動却下** |
| **Lighthouse Best Practices** | 90+ | 警告 |
| **Lighthouse SEO** | 90+ | 警告 |
| **画像サイズ** | image_url width: **1200以上**（Retina対応）<br>※ [feedback memory rules](memory) | 自動却下 |
| **画像フォーマット** | WebP 優先、JPEG/PNG はフォールバック | 警告 |
| **First Contentful Paint** | モバイル 2.0s 以下 | 警告 |
| **Cumulative Layout Shift** | 0.1 以下 | 警告 |
| **Total Blocking Time** | 200ms 以下 | 警告 |

---

## 6. アクセシビリティ（必須）

| 項目 | 合格基準 | 不合格時の動作 |
|---|---|---|
| **axe-core 自動チェック** | violations = 0（CriticalとSerious） | **自動却下** |
| **キーボード操作** | 全インタラクティブ要素が Tab で到達可能 | 自動却下 |
| **フォーカス可視** | フォーカスリング常時表示（カスタム可、ただし可視） | 警告 |
| **`alt` 属性** | 全 `<img>` に意味のある `alt`（装飾は空文字でOK） | 自動却下 |
| **見出し階層** | h1 → h2 → h3 と飛ばさない | 警告 |
| **ARIA属性** | 必要箇所のみ。誤用は逆効果 | 警告 |

---

## 7. Liquid / Shopify 特有ルール（必須）

| 項目 | 合格基準 | 不合格時の動作 |
|---|---|---|
| **ファイル全体出力** | 部分スニペット不可、必ず完全なファイルを生成<br>※ [memory開発ルール](memory) | 自動却下（再生成） |
| **コード変更後の検証** | 変更箇所を grep 等で確認可能であること | 警告 |
| **z-index 制御** | 必要な要素は ::before/::after 疑似要素で処理 | 自動却下 |
| **schema設定** | settings_schema 完備、ローカライズキー登録 | 警告 |
| **`image_url` フィルタ** | width: 1200 以上、`alt` 指定 | 自動却下 |
| **`{% liquid %}` タグ活用** | 5行以上のロジックは liquid タグでまとめる | 警告 |
| **Customizer 設定** | 12種チップ仕様の機能要件と整合 | 警告 |
| **Theme inspector 警告** | 0件 | 警告 |

---

## 8. FAMBOX 視覚効果の制約（重要）

[feedback_fambox_visual_effects.md](memory) より、FAMBOXに **そぐわない技法** を明示：

| ❌ 避ける | 理由 |
|---|---|
| 輪郭歪み（distortion） | FAMBOXの落ち着き・信頼感に反する |
| Noise-bloom効果 | グリッチ系。Lab感を損なう |
| グリッチ表現 | スポーツ栄養の科学性に合わない |

| ✅ OK（軸別） | 該当軸 |
|---|---|
| 軽微なグレイン・テクスチャ | 軸3候補（努力の結晶） |
| backdrop-filter blur（ガラス） | 軸2 Calm Resolve |
| SVG feGaussianBlur（ぼかし） | 軸2 Calm Resolve |
| Kinetic typography（機械的） | 軸1 デジタル/システム型 |

---

## 9. クライアント承認フローへの組み込み

このパラメーター文書を使った **新しい承認フロー** ：

### 旧フロー
```
[宮川さん設計] → [手動チェック] → [クライアント目視レビュー] → [合議] → 承認 or 修正依頼
```

### 新フロー（Human-on-the-Loop）
```
[AI生成 or 宮川さん設計]
     ↓
[本ガードレール自動チェック]
     ↓
合格 → [軽量レビュー（境界事例のみ）] → クライアント承認
不合格 → [自動修正案 or 人間判断]
```

### クライアントへの説明文（テンプレ）
> 弊社では AI 時代のデザイン品質保証として、**WCAG AA・Lighthouse・FAMBOXブランドガイドライン** を含む **〇〇項目** の自動検証を全成果物に適用しています。これにより属人化を排し、一貫した品質を保証しています。

---

## 10. このドキュメントの運用ルール

| 項目 | 内容 |
|---|---|
| **更新権限** | 宮川さん（最終承認） |
| **更新頻度** | 月次レビューで見直し |
| **新基準追加時** | 過去成果物への遡及適用は **しない**（移行コスト過大） |
| **クライアント別の例外** | 案件ごとに明記、本ドキュメントに追記 |
| **AIエージェントへの渡し方** | 本ドキュメントを丸ごとプロンプト/ファイルとして与える |

---

## 11. 実装ロードマップ（このドキュメントを「使える」状態にする）

### Phase 1: 文書整備（今週）
- [x] 本ファイル作成
- [ ] FAMBOX ブランドカラートークンの確定 → `brand/fambox/` に整理
- [ ] Lighthouse / axe-core の閾値を確定（暫定値の本決め）

### Phase 2: 自動チェック実装（今月）
- [ ] LPB v4 に Lighthouse CI 統合
- [ ] axe-core 自動チェック組込
- [ ] FAMBOX固有ルール（image_url width, z-index 等）の linter 作成

### Phase 3: 運用開始（来月）
- [ ] 新規Liquid生成に必ず本ガードレールを通す運用
- [ ] クライアント説明文の追加（提案資料・契約書）
- [ ] 月次でガードレール通過率レポート

---

## 関連
- [[skill-obsolescence-risk-audit.md]] — 自分のスキル戦略
- [[obara-ai-agent-era-ep1.md]] — 「ガードレール設計」の重要性の原典
- [[vibe-coding-six-principles.md]] — 本番投入前の確認項目（このドキュメントと整合）
- [[../50_Business_Context/fambox-brand-dna-axes.md]] — FAMBOX ブランド軸（カラー・スタイル判定の基準）
- `brand/fambox/` — FAMBOX 固有のカラートークン・タイポ等
- `brand/fam/` — FAM 親ブランド資産

## Escalation Status

- **Level**: L2（AI レビュー — Claude がデザイン承認時に本パラメーターを参照）
- **昇格目標**: L3 — T 監査スイートでデザイントークン整合性・軸該当性を自動チェック化
- **次レビュー**: 2026-08-21
- **詳細**: [harness-engineering-2026-03.md](harness-engineering-2026-03.md) — Escalation Status 一覧
