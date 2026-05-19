---
title: FAMBOX Design Tokens — Spacing & Layout
type: design-system
layer: L1-Tokens-Spacing
version: 0.2
status: seed
last_updated: 2026-04-20
owner: 宮川
source: FAM Brand DNA v0.5 C章（継承）
---

# FAMBOX — Spacing & Layout Tokens

## 設計原則
- **8px baseline グリッド**: 全ての余白は 8px の倍数
- **ジャンプのある等比スケール**: 等差（8/12/16）ではなく等比（8/16/24/32…）で密度差をつける
- **TNF級に大きな余白**（Editorial × Lab メタファー）

## Spacing Scale（8px baseline）

| Token | Value | 主な用途 |
|---|---|---|
| `--space-1` | `8px` | 極小ギャップ・Icon×Text間 |
| `--space-2` | `16px` | 標準ギャップ・Card内余白 |
| `--space-3` | `24px` | ゆったりギャップ |
| `--space-4` | `32px` | Section内コンテンツ間 |
| `--space-5` | `48px` | Section内大ブロック間 |
| `--space-6` | `64px` | Section間（小）・Card外余白 |
| `--space-7` | `96px` | **SPセクション間標準** |
| `--space-8` | `160px` | **PCセクション間標準** |

## Grid

| 項目 | Value | CSS Variable |
|---|---|---|
| カラム数 | 12 | `--grid-columns` |
| ガター | `24px` | `--grid-gutter` |
| ベースライン | `8px` | `--grid-baseline` |
| コンテナ最大幅（標準） | `1440px` | `--container-max` |
| コンテナ最大幅（狭） | `1200px` | `--container-narrow` |

## Breakpoint

| 名称 | 範囲 | CSS Variable（上限）|
|---|---|---|
| SP | 〜767px | `--bp-sp` |
| Tablet | 768px〜1023px | `--bp-tablet` |
| PC | 1024px〜 | `--bp-pc` |

### Media Query 推奨
```css
/* Mobile First */
@media (min-width: 768px) { /* Tablet以上 */ }
@media (min-width: 1024px) { /* PC以上 */ }
```

## Bento Grid（FAM v0.5 継承）

### タイルサイズ 5種
| サイズ | 用途 |
|---|---|
| 1x1 | 基本要素（Stat単体） |
| 2x1 | 横長（List） |
| 1x2 | 縦長（Card） |
| 2x2 | 主役タイル（写真+タイポ重ね合わせ） |
| 3x2 | 超主役（Hero相当） |

### タイル間スペーシング
| 密度 | Value |
|---|---|
| 密 | `16px`（`--space-2`） |
| 標準 | `24px`（`--space-3`） |
| ゆったり | `32px`（`--space-4`） |

## Section Spacing 運用

| デバイス | セクション間標準 | 例外（密コンテンツ） |
|---|---|---|
| SP | `--space-7`（96px）| `--space-6`（64px） |
| PC | `--space-8`（160px）| `--space-7`（96px） |

## Container 運用

| 用途 | Container |
|---|---|
| 標準 LP / 商品ページ | `--container-max`（1440px）|
| 記事本文 / 読み物 | `--container-narrow`（1200px）|
| Form / 問合せ | `--container-narrow`（1200px）|

## Do / Don't

### ✅ Do
- 余白は必ず `--space-*` のいずれかを使う
- セクション間は SP 96px / PC 160px を基本とする
- 8px baseline に合わない値が必要になったら、DS追加議論する

### ✕ Don't
- `margin: 15px` や `padding: 20px` 等、8px baseline外の値を使わない
- セクション間に `40px` 等の中途半端な値を使わない（空間の弱さの原因）
- Hero に `--container-narrow` を使わない（迫力が出ない）
