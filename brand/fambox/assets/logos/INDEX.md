---
title: FAMBOX Brand Logos — Master Inventory
date: 2026-05-26
owner: 宮川（ARCHECO）
status: tier-1-partial
material_id: M1
---

# Brand Logos Master Inventory

MATERIALS_CHECKLIST.md M1（Tier 1 最優先）に対応する**ロゴアセット集約点**です。`brand/fambox/assets/logos/` 配下に格納されたすべてのロゴ master を一覧化します。

## 現状（2026-05-26 時点）

| ブランド | 用途 | Black | White | カラー | 縦組み | シンボル単体 | AI / EPS |
|---|---|---|---|---|---|---|---|
| **FAMBOX**（メイン） | ストア・ヘッダー・印刷 | SVG + PNG ✅ | SVG + PNG ✅ | ❌ 未収集 | ❌ 未収集 | ❌ 未収集 | ❌ 未収集 |
| **FAM**（親ブランド） | 親ブランド表示 | PNG ✅ | PNG ✅ | ❌ 未収集 | ❌ 未収集 | ❌ 未収集 | ❌ 未収集 |
| **FSNL**（FAM SCHOOL?） | サブブランド | PNG ✅ | PNG ✅ | ❌ 未収集 | ❌ 未収集 | ❌ 未収集 | ❌ 未収集 |

## ファイル一覧

### FAMBOX
- `fambox/fambox-wordmark-black.svg` — ベクター / ヘッダー・サイト用
- `fambox/fambox-wordmark-black.png` — ラスター / プレビュー用
- `fambox/fambox-wordmark-white.svg` — Ink 背景・暗色背景用
- `fambox/fambox-wordmark-white.png` — Ink 背景プレビュー

### FAM
- `fam/fam-wordmark-black.png`
- `fam/fam-wordmark-white.png`

### FSNL（FAM SCHOOL?）
- `fsnl/fsnl-wordmark-black.png`
- `fsnl/fsnl-wordmark-white.png`

## 命名規約

`{brand}/{brand}-{type}-{color}.{ext}`

- `{brand}`: `fambox` / `fam` / `fsnl`
- `{type}`: `wordmark`（横組み文字ロゴ） / `vertical`（縦組み） / `symbol`（シンボル単体） / `lockup`（組み合わせ）
- `{color}`: `black` / `white` / `color`（フルカラー）
- `{ext}`: `svg`（ベクター推奨） / `png` / `ai` / `eps`

## 不足分（Tier 1 完了に向けて要収集）

| 優先度 | 不足項目 | 取得元 / 依頼先 | 期限案 |
|---|---|---|---|
| 🔴 High | FAMBOX フルカラー版 SVG | 大前さん / 制作元に依頼 | 5/29 |
| 🔴 High | FAMBOX AI / EPS 印刷用 | 大前さん / 制作元 | 5/29 |
| 🟡 Mid | FAMBOX 縦組み / シンボル単体 | 制作元発注 or 内製判断 | 6/5 |
| 🟡 Mid | FAM / FSNL の SVG 版 | 制作元 / 旧資料探索 | 6/5 |
| 🟢 Low | 全 4 解像度 PNG（256/512/1024/2048） | SVG から自動生成可能 | 6/12 |

## 使用ガイド（暫定）

- **デフォルト**: FAMBOX wordmark black on light background
- **暗色背景時**: white 版を使用
- **印刷物**: SVG → AI / EPS 変換が必要（未整備）
- **クリアスペース / 最小サイズ**: 仕様未確定（M1 完了時に追加）

## 関連

- [MATERIALS_CHECKLIST.md M1](../../MATERIALS_CHECKLIST.md#m1-ロゴ-master-ファイルsvg--ai--png)
- [Brand DNA current.md L4-14 ロゴ運用](../../brand-dna/current.md)
- TS Tech ブランドマニュアル参照（FAMBOX 実績掲載時にロゴ／社名利用）

## 変更履歴

- 2026-05-26: Initial inventory — リポジトリルートに散らばっていた LMLT_*.png/svg を集約 + 命名規約整備（宮川 / Claude）
