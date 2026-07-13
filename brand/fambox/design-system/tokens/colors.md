---
title: FAMBOX Design Tokens — Colors
type: design-system
layer: L1-Tokens-Color
version: 0.2
status: seed
last_updated: 2026-04-20
owner: 宮川
source: FAM Brand DNA v0.5 D章（継承）
---

# FAMBOX — Color Tokens

## 設計原則
- **Drive Orange 最優先**: CTA・達成値・推進表現
- **Sky / Deep Blue** で信頼領域を作る
- **Ink 5段階** で階層を作る（濃度で重要度を表現）
- **Semantic色は Drive と色相衝突を回避**（純緑・純赤は使わない）

## ブランドカラー

| 役割 | 名称 | HEX | CSS Variable | 主な用途 |
|---|---|---|---|---|
| Primary | **Drive Orange** | `#FB4C15` | `--color-drive` | CTA・達成値・推進 |
| Primary Light | Drive Light | `#FC825B` | `--color-drive-light` | ホバー・ハイライト |
| Primary Glow | Drive Glow | `rgba(251,76,21,0.2)` | `--color-drive-glow` | フォーカスリング・グロー |
| Secondary A | **Sky Blue** | `#3DB8E8` | `--color-sky` | データ可視化・情報カテゴリ |
| Secondary B | **Deep Blue** | `#0F2A5C` | `--color-deep` | ヒーロー深部・信頼領域 |

## Text Grayscale（5段階）

| 段階 | HEX | CSS Variable | 用途 |
|---|---|---|---|
| 1 | `#1B1D1A` | `--color-ink` | 本文・見出し |
| 2 | `#545655` | `--color-sub` | サブテキスト |
| 3 | `#888888` | `--color-caption` | キャプション |
| 4 | `#D0D0D0` | `--color-placeholder` | プレースホルダ |
| 5 | `#FFFFFF` | `--color-white` | 白 |

## Background（3階層）

| 役割 | HEX | CSS Variable |
|---|---|---|
| Primary | `#FFFFFF` | `--bg-primary` |
| Secondary | `#FAFAFA` | `--bg-secondary` |
| Tertiary | `#F3F3F3` | `--bg-tertiary` |

## Border

| 役割 | HEX | CSS Variable |
|---|---|---|
| Light | `#ECECEC` | `--border-light` |
| Base | `#D0D0D0` | `--border-base` |
| Subtle | `#D0D1DB` | `--border-subtle` |

## Semantic（状態色）

| 役割 | HEX | CSS Variable | 選定理由 |
|---|---|---|---|
| Success | `#10B981` | `--color-success` | Sky Blue調和、純緑より洗練 |
| Warning | `#F59E0B` | `--color-warning` | Drive Orangeと色相距離を確保 |
| Error | `#DC2626` | `--color-error` | Drive Orangeとの混同回避、深赤で識別性 |
| Info | `#3DB8E8` | `--color-info` | Sky Blue兼用 |

## Data Visualization

| 役割 | CSS Variable |
|---|---|
| Primary | `--data-primary`（= Drive） |
| Secondary | `--data-secondary`（= Deep） |
| Tertiary | `--data-tertiary`（= Sky） |
| Zone Good | `--data-zone-good`（= Success） |
| Zone Caution | `--data-zone-caution`（= Warning） |
| Zone Danger | `--data-zone-danger`（= Error） |

## Semantic Alias（意味参照）★ FAMBOX独自

Brand DNA からの直訳として、意図を表す別名を用意。**原則: 色の意味が変わっても Alias を変えることで一括更新可能**。

Worksheet §2 で確定（2026-04-20）: **Deep Blue はリンクに使用しない**。すべて文脈依存で切替。

### 基本 Alias
| Alias | 参照先 | 用途 |
|---|---|---|
| `--color-cta` | `--color-drive` | CTA全般 |
| `--color-focus-ring` | `--color-drive` | フォーカスリング（WCAG対応） |
| `--color-link-hover` | `--color-drive-light` | リンクホバー（全文脈共通） |

### リンクの文脈別 Alias
| 背景 | Alias | 色 | 用途 |
|---|---|---|---|
| 明るい（#FFF / #FAFAFA / #F3F3F3 等） | `--color-link-on-light` | `--color-drive`（オレンジ） | 本文中リンク / ボタン以外 |
| 暗い（Ink / Drive 背景等） | `--color-link-on-dark` | `--color-white` | Hero内・ダークセクション内 |
| Drive 背景上のボタン内 | `--color-link-on-drive` | `--color-ink` | Primary Button内テキスト |

### 価格表示 Alias ★ FAMBOX新設
| 用途 | Alias | 色 |
|---|---|---|
| 目立たせる価格（主役プラン等） | `--color-price-accent` | `--color-drive` |
| 明るい背景上の標準価格 | `--color-price-default-on-light` | `--color-ink` |
| 暗い背景上の標準価格 | `--color-price-default-on-dark` | `--color-white` |

### エラーテキスト Alias ★ FAMBOX新設
| Alias | 色 | 用途 |
|---|---|---|
| `--color-error-text` | `#F91A02` | エラーメッセージ等のテキスト用赤（UI `--color-error` と分離）|

### リンク運用ルール（要点）

1. **背景が明るい** (#FFF / #FAFAFA / 薄グレー等) → テキスト色 = Drive オレンジ
2. **背景が暗い** (#1B1D1A 等) → テキスト色 = 白
3. **背景が Drive オレンジ（ボタン等）** → ボタン内テキスト = Ink系（黒）、通常テキスト = 白
4. **Deep Blue は使用しない**（B2B のトーンとしては馴染むが、FAMBOX ではリンク色として使わない）

## Opacity（Glass）

| レベル | 値 | CSS Variable | 用途 |
|---|---|---|---|
| 1 | 0.05 | `--glass-1` | 超薄オーバーレイ |
| 2 | 0.1 | `--glass-2` | ガラスタイル薄 |
| 3 | 0.3 | `--glass-3` | ガラス中 |
| 4 | 0.6 | `--glass-4` | モーダル暗化 |
| 5 | 0.8 | `--glass-5` | 強オーバーレイ |

## Accessibility（WCAG 2.1 AA）

| 組み合わせ | コントラスト比 | WCAG AA 判定 |
|---|---|---|
| `--color-ink` on `--bg-primary` | 14.8:1 | ✅ Pass |
| `--color-sub` on `--bg-primary` | 7.4:1 | ✅ Pass |
| `--color-caption` on `--bg-primary` | 4.5:1 | ⚠️ 通常本文 Pass（小文字注意） |
| `--color-white` on `--color-drive` | 3.8:1 | ⚠️ 大文字のみ Pass（小文字NG） |
| `--color-white` on `--color-deep` | 14.5:1 | ✅ Pass |
| `--color-white` on `--color-error` | 5.9:1 | ✅ Pass |

## Do / Don't

### ✅ Do
- CTAボタンには `--color-drive` のみ使う
- Semantic色（Success/Warning/Error）を状態表示に使う
- 背景は `--bg-primary` 主体、カードは `--bg-secondary` で階層を作る

### ✕ Don't
- Drive以外の色でCTAを作らない（ブランド混乱）
- `#000000` 純黒を使わない（Ink `#1B1D1A` を使う）
- Semantic色をDecorativeに使わない（状態表示専用）
- Glass-3以上をテキスト背景に使わない（可読性低下）
