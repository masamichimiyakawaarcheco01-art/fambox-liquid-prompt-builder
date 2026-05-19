---
title: fambox-menu-showcase tokens.css 適用ガイド (実装計画書 Tier 2 #11)
type: operations
date: 2026-05-12
status: 改修ガイド（本番 Shopify テーマリポジトリで手動転記）
purpose: menu-showcase は spec 上「専用 Pattern として保持・構造変更なし」と確定。tokens.css 適用のみで DNA 準拠化する手順
target: 本番テーマ `sections/fambox-menu-showcase.liquid` (264 行、worktree 内には存在せず本番リポジトリ管理)
---

# fambox-menu-showcase tokens.css 適用ガイド

## 背景

実装計画書 §1 Tier 2 #11 の方針:
> | 11 | `fambox-menu-showcase` | 264 | 専用 Pattern として保持（横スクロール track）/ 部分的にトークン適用 | tokens.css 適用のみ（構造変更なし）| 1h |

menu-showcase は **横スクロール track** という独自レイアウトで、Bento Grid / Card Pattern のいずれにも収まらない。**構造変更なし** で進めるのが spec 確定方針。

## 適用すべき置換（直値 → Variable）

### 色

| 直値 | 置換先 |
|---|---|
| `#FB4C15` / `#fb4c15` | `var(--color-drive)` |
| `#1B1D1A` / `#1b1d1a` | `var(--color-ink)` |
| `#545655` | `var(--color-sub)` |
| `#888888` | `var(--color-caption)` |
| `#D0D0D0` | `var(--color-placeholder)` |
| `#FFFFFF` / `#ffffff` | `var(--color-white)` |
| `#FAFAFA` / `#fafafa` | `var(--bg-secondary)` |
| `#ECECEC` / `#ececec` | `var(--border-light)` |

### 余白（直値 → spacing token）

| 直値 | 置換先 |
|---|---|
| `8px` | `var(--space-1)` |
| `16px` | `var(--space-2)` |
| `24px` | `var(--space-3)` |
| `32px` | `var(--space-4)` |
| `48px` | `var(--space-5)` |
| `56px` | `var(--space-6)` |
| `64px` | `var(--space-7)` |

### radius

| 直値 | 置換先 |
|---|---|
| `4px` | `var(--radius-sm)` |
| `8px` | `var(--radius-md)` |
| `9999px` / `50%` | `var(--radius-pill)` |

### フォント

| 直値 | 置換先 |
|---|---|
| `'Hiragino Sans'...` | `var(--font-ja)` |
| `'Poppins'...` | `var(--font-en)` |
| `font-weight: 400` | `var(--fw-regular)` |
| `font-weight: 500` | `var(--fw-medium)` |
| `font-weight: 600` | `var(--fw-semibold)` |
| `font-weight: 700` | `var(--fw-bold)` |

### フォントサイズ

| 直値 | 置換先 |
|---|---|
| `12px` | `var(--fs-caption)` |
| `14px` | `var(--fs-body-sm)` |
| `16px` | `var(--fs-body)` |
| `20px` | `var(--fs-lg)` |
| `24px` | `var(--fs-h3)` |
| `32px` | `var(--fs-h2)` |
| `48px` | `var(--fs-h1)` |

### Shadow

| 直値（例）| 置換先 |
|---|---|
| `box-shadow: 0 1px 2px rgba(0,0,0,0.04)` | Effect Style `--shadow-1` 参照 |
| `box-shadow: 0 4px 16px rgba(0,0,0,0.08)` | `--shadow-3` |

## 改修フロー（本番テーマ操作）

1. **既存ファイルバックアップ**: `cp sections/fambox-menu-showcase.liquid sections/_archive/fambox-menu-showcase.liquid.bak`
2. **置換実行**: sed -i または手動で上記マッピングに従い置換
3. **fallback 値を付与**: `var(--color-drive)` → `var(--color-drive, #fb4c15)` のように fallback 付き（Variables 未定義環境でも壊れない）
4. **動作確認**: Shopify エディタプレビューで token 反映確認
5. **grep 検証**: `grep -E '#[0-9a-fA-F]{6}|[0-9]+px' sections/fambox-menu-showcase.liquid` で残存直値を確認

## 注意点

- 横スクロール track の構造（`overflow-x: auto`, `scrollbar-width: none`）は維持
- card 内の独自 layout（画像 + テキスト）はそのまま
- GA4 イベント（`data-gtag-*`）は必ず保持

## 完了後の更新

- spec md (`components/` 配下に未作成) を必要なら新規作成、Pattern として正式記録
- `brand/fambox/design-system/current.md` の milestone に追加
- `figma-build-log.md` に Session 記録（Phase 4 コンテンツ最適化に類似する補修フェーズ）

## 関連

- spec: Pattern として未確定（実装計画書 §1 Tier 2 で「専用 Pattern」と分類のみ）
- v0.3 候補: spec md 新規作成（`brand/fambox/design-system/components/menu-showcase.md`）
- 既存実装: 本番テーマ `sections/fambox-menu-showcase.liquid` (264 行)
