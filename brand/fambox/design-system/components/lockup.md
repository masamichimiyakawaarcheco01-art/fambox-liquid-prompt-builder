---
title: FAMBOX Component — Lockup (L4-14)
type: design-system
layer: L4-Components
component: Lockup
version: 0.1
status: planning
owner: 宮川
created: 2026-05-27
deadline: v1.1 Phase 2（Figma 素材生成 + 全資産展開）
source: ADR-024（L4-14 ロックアップ詳細 10 項目確定 / 2026-05-22）+ ADR-033（v1.0 後 Figma 実装着手）
brand_alignment:
  - 独立ブランド方針（ADR-015）: FAM BOX 単独使用が原則
  - Anti（ADR-024 ⑥）: 比率変形 / 回転 / 色改変 / エフェクト / 枠囲み / 低解像度 を厳禁
related:
  - brand/fambox/brand-dna/current.md#l4-14
  - brand/fambox/brand-dna/decisions/decisions-log.md#adr-024
  - brand/fambox/brand-dna/decisions/decisions-log.md#adr-033（予約番号）
  - brand/fambox/assets/logos/INDEX.md
  - Figma: https://www.figma.com/design/QsiBrc2v20BYw76YHI9x3e/FAMBOX-Design-System
---

# Lockup — Component（L4-14）

ADR-024 で確定したロックアップ 10 項目を Figma で Component 化する実装計画書 + Component Spec。**ADR-033 の実装計画**。

## 概要

FAMBOX 独立ブランド方針（ADR-015）に基づき、Logo ロックアップを **3 バリエーション × 3 カラー = 9 種** + 4 形式（SVG / PNG / AI / EPS）で展開。Figma マスター（`QsiBrc2v20BYw76YHI9x3e`）の **3. Primitives** ページに Component Set として登録し、Variables（Drive `#FB4C15` / Ink `#1B1D1A` / White `#FFFFFF`）に紐付ける。

---

## ADR-024 10 項目 → Figma 実装マッピング

### ① ロックアップ・バリエーション

| Variant | Figma Component 名 | サイズ目安 |
|---|---|---|
| 横組み（wordmark） | `lockup/wordmark` | 高さ 24-48px（Web） |
| 縦組み（vertical） | `lockup/vertical` | 高さ 64-96px |
| シンボル単体（symbol） | `lockup/symbol` | 24-48px 正方形 |
| ワードマーク単体（wordmark-only） | `lockup/wordmark-only` | B2B 資料・名刺用 / 高さ 32-48px |

**Component Set 構造**:
```
Lockup
├── type=wordmark
│   ├── color=fullcolor
│   ├── color=monochrome-black
│   └── color=monochrome-white
├── type=vertical
│   ├── color=fullcolor
│   ├── color=monochrome-black
│   └── color=monochrome-white
├── type=symbol
│   └── ...（同様）
└── type=wordmark-only
    └── ...（同様）
```

= 4 type × 3 color = **12 variants**

### ② クリアスペース（最小余白）

- **規律**: ロゴ高さの **0.5 倍** を周囲に確保（文字「X」の高さ基準）
- **Figma 表現**: Component 内に `clear-space-guide` レイヤーを 0.5 倍 padding で配置（参照用、export 時に hidden）
- **Component property**: `show-clear-space` (boolean, default: false)

### ③ 最小サイズ

| 媒体 | 最小サイズ |
|---|---|
| Web（横組み） | 高さ 24px / 幅 80px 以上 |
| Web（シンボル） | 高さ 24px |
| 印刷 | 高さ 8mm 以上 |

**Figma 表現**: Documentation page に「Minimum Size」アートボードで実寸表示

### ④ カラーバリエーション

| Color | Variable | Hex |
|---|---|---|
| フルカラー（Drive 主体） | `FAMBOX/color/brand/drive` | `#FB4C15` |
| モノクロ黒 | `FAMBOX/color/ink/ink` | `#1B1D1A` |
| 白抜き | `FAMBOX/color/ink/white` | `#FFFFFF` |

❌ **不採用**: 金・銀（"アシックス的本質主義"と整合せず）

**Figma 実装**: 既存 Variables Collection の 3 トークンに紐付け（Auto-swap で同 Component 内で切替可能）

### ⑤ 背景コントラストルール

| 背景 | 使用 Logo |
|---|---|
| 白 / 薄グレー（`#ECECEC` 以下） | monochrome-black or fullcolor |
| Drive 色 (`#FB4C15`) | monochrome-white |
| Deep Blue（`#0A2540` 等の暗背景） | monochrome-white |
| 写真上 | **白帯フォールバック**（背景に 80% opacity 白帯を挿入してから配置） |
| コントラスト不足時 | 白抜き優先 |

**Figma 表現**: Documentation page に「Background Combinations」マトリクス（6 背景 × 3 logo color）

### ⑥ 禁止事項（Don'ts）

| # | 禁止 | Figma 表現 |
|---|---|---|
| 1 | 比率変形・引き伸ばし | ❌ 例: 横 200% に extend |
| 2 | 回転（角度付き配置） | ❌ 例: 15° rotation |
| 3 | 色改変（ブランドパレット外） | ❌ 例: 紫やシアンに変更 |
| 4 | エフェクト（ドロップシャドウ / グラデ / アウトライン） | ❌ 例: shadow 4px / gradient fill |
| 5 | 枠囲み・他要素と合体 | ❌ 例: border 2px / 矩形と重ねる |
| 6 | 低解像度 | ❌ 例: 16px 以下 / blur |

**Figma 実装**: Documentation page に「Don'ts」アートボード（6 例を視覚化、× 印で禁止明示）

### ⑦ Co-branding ルール（FAM 母体 × FAM BOX 事業）

| 用途 | 表記 |
|---|---|
| プレスリリース・会社紹介 | 「FAM / FAM BOX」（スラッシュ区切り） |
| 公式名 | 「株式会社 FAM の FAM BOX 事業」 |
| FAM BOX 主役接点 | **FAM BOX 単独使用が原則** |

**Figma 実装**: 共同表記用 Component `lockup/cobranding` を別途作成（`lockup/wordmark` と FAM ロゴを横並び）

### ⑧ パートナー連携時の表示

- スポンサー企業・連携チーム並置: 「in partnership with」or「presented by」書式
- FAM BOX を **主役に維持**

**Figma 実装**: Documentation page に「Partnership 例」（FAM BOX × TOYOTA RED CRUISERS 等の実例ベース）

### ⑨ 配置・用途

- **推奨配置**: 左上主・右下副
- 適用先: ヘッダー / フッター / 名刺 / 封筒 / パッケージ

**Figma 実装**: Templates ページに以下 5 サンプル:
- Header（実装済 — Header v0.2 と整合）
- Footer
- 名刺（91×55mm）
- 封筒（長形 3 号）
- パッケージ（FAMBOX 製品箱の表面）

### ⑩ 納品形式

| Format | 用途 | export |
|---|---|---|
| SVG | Web（推奨） | Figma export PNG/SVG |
| PNG（透過） | Web フォールバック / 各解像度 256/512/1024/2048 | Figma export PNG 1x/2x/3x/4x |
| AI / EPS | 印刷 | Illustrator export（**user 作業**） |
| PDF | 汎用 | Figma export PDF |

**マスタ一覧**: Lockup Component 12 variants × 4 format = **48 ファイル**を `brand/fambox/assets/logos/exports/` 配下に書き出し

---

## 実装フェーズ

### Phase A: Figma Component 化（今セッション可能 / user の Figma plugin 接続が必要）

1. Figma マスター（`QsiBrc2v20BYw76YHI9x3e`）の **3. Primitives** ページに `Lockup` Component Set を作成
2. 既存ロゴアセット（`brand/fambox/assets/logos/fambox/fambox-wordmark-black.svg`）を取り込み
3. 4 type × 3 color = 12 variants の Component Property を設定
4. Variables（drive / ink / white）に紐付け
5. Documentation page にクリアスペース / 最小サイズ / 背景コントラスト / Don'ts のアートボード追加

### Phase B: 不足アセットの収集（大前さん / 制作元への依頼）

M1 不足分（`brand/fambox/assets/logos/INDEX.md` 参照）:
- フルカラー SVG（`#FB4C15` 適用版）
- AI / EPS（印刷用）
- 縦組み版（horizontal → vertical 化）
- シンボル単体（"FAM BOX" wordmark から「F」マーク等を抽出）

### Phase C: 全資産展開（v1.1 以降）

- 名刺テンプレ（Figma + Illustrator）
- 封筒テンプレ
- パッケージデザイン（FAMBOX 製品箱の表面）
- 営業資料の表紙テンプレ
- LP / Blog のヒーローバナーテンプレ

---

## 検証チェックリスト（v1.1 完了時）

- [ ] Figma マスターに `Lockup` Component Set が登録されている
- [ ] 12 variants が Variables に正しく紐付いている（自動カラー切替が機能）
- [ ] クリアスペース guide が `show-clear-space=true` で表示される
- [ ] Documentation page に 6 種のページ（Variations / Clear Space / Min Size / Color / Background / Don'ts）がある
- [ ] 5 種のテンプレート（Header / Footer / 名刺 / 封筒 / パッケージ）が Templates ページにある
- [ ] 全 48 export ファイル（12 variants × 4 format）が `brand/fambox/assets/logos/exports/` に書き出し済
- [ ] L4-14 規律（ADR-024 ⑥ Don'ts）に違反する使用例がない（社内 / 外部レビュー）

---

## 関連

- [Brand DNA v1.0 L4-14](../../brand-dna/current.md#l4-14)
- [ADR-024 ロックアップ詳細 10 項目](../../brand-dna/decisions/decisions-log.md#adr-024)
- [M1 ロゴ master INDEX](../../assets/logos/INDEX.md)
- [Figma Design System file](https://www.figma.com/design/QsiBrc2v20BYw76YHI9x3e/FAMBOX-Design-System)

## 変更履歴

- 2026-05-27: Initial planning — ADR-024 10 項目の Figma 実装計画（ADR-033 候補ベース / Phase A〜C 整理）
