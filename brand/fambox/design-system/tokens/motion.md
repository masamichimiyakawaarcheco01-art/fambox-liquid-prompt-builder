---
title: FAMBOX Design Tokens — Motion
type: design-system
layer: L1-Tokens-Motion
version: 0.2
status: seed
last_updated: 2026-04-20
owner: 宮川
source: FAM Brand DNA v0.5 H章（継承）
---

# FAMBOX — Motion Tokens

## 設計原則
- **ease-in 主体**: Drive＝加速の表現。ease-out は到達時のみ
- **Parallax限定**: ヒーロー背景のみ slow parallax（過度な演出禁止）
- **呼吸アニメで鼓動感**: 2秒サイクルで主要CTA・達成表示
- **`prefers-reduced-motion` 必須対応**: tokens.css に自動適用済み

## Duration

| Token | Value | 主な用途 |
|---|---|---|
| `--duration-fast` | `150ms` | Hover / Focus切替 |
| `--duration-base` | `300ms` | 標準遷移・カードホバー |
| `--duration-slow` | `600ms` | セクション入場・モーダル出現 |
| `--duration-breath` | `2000ms` | 呼吸アニメ（軸3 Pulsing）|

## Easing

| Token | Value | 特性 |
|---|---|---|
| `--ease-in` | `cubic-bezier(0.4, 0, 1, 1)` | 加速（主） |
| `--ease-out` | `cubic-bezier(0, 0, 0.2, 1)` | 減速・到達感 |
| `--ease-inout` | `cubic-bezier(0.4, 0, 0.2, 1)` | 両端加減速 |

## 運用パターン

### ホバー：前方向へ1-2px飛び出す（軸1 Propulsive）
```css
.button {
  transition: transform var(--duration-fast) var(--ease-out);
}
.button:hover {
  transform: translateY(-2px);
}
```

### セクション入場：下→上フェード（軸2 Ascending）
```css
.section-enter {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity var(--duration-slow) var(--ease-out),
              transform var(--duration-slow) var(--ease-out);
}
.section-enter.is-visible {
  opacity: 1;
  transform: translateY(0);
}
```

### 呼吸アニメ：主要CTA・達成演出（軸3 Pulsing）
```css
@keyframes breath {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.02); opacity: 0.95; }
}
.cta-primary {
  animation: breath var(--duration-breath) var(--ease-inout) infinite;
}
```

### データ描画：左→右 or 中央→外（F章参照）
```css
.data-bar {
  transform-origin: left center;
  transform: scaleX(0);
  transition: transform var(--duration-slow) var(--ease-out);
}
.data-bar.is-drawn {
  transform: scaleX(1);
}
```

## 8状態仕様（v0.5継承・Primitives で実装）

| 状態 | 遷移元 | 遷移先 | Duration |
|---|---|---|---|
| default | - | hover | `--duration-fast` |
| hover | default | active | `--duration-fast` |
| focus | any | default | `--duration-fast` |
| active | hover | default | `--duration-fast` |
| disabled | - | - | - |
| loading | default | success/error | `--duration-base` |
| empty | - | - | - |
| error | loading | default | `--duration-base` |
| success | loading | default | `--duration-base` |

## ページ遷移・Parallax（FAM v0.5 確定）

| 項目 | 方針 |
|---|---|
| ページ遷移 | **Shopify標準の即時遷移**（将来 View Transitions API 対応可能な構造） |
| Parallax | **ヒーロー背景画像のみ slow parallax（任意）**。過度なパララックス禁止 |

## Do / Don't

### ✅ Do
- Hover/Focus は `--duration-fast`、セクション入場は `--duration-slow` を使い分ける
- 主要CTA（問合せ・定期便加入）にのみ呼吸アニメを適用（演出過剰を避ける）
- 必ず `--ease-in` 主体（FAM Drive らしさ）

### ✕ Don't
- `ease-out` 主体にしない（FAM らしさが消える）
- Parallax をヒーロー以外に使わない
- 呼吸アニメをテキストや本文ブロックに適用しない（読みにくい）
- `transition: all 0.5s` のような非トークン直書きをしない（必ず `--duration-*` / `--ease-*`）
