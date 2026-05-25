---
title: FAMBOX Pattern — Loading
type: design-system
layer: L3-Patterns
component: Loading
version: 0.3
status: confirmed
last_updated: 2026-05-08
owner: 宮川
source: 食事診断 Loading画面実装からの抽出
brand_alignment:
  - Drive: 進行中の Drive Orange パルス
  - Continuity: 待機時間を「積み上げ」で可視化
  - Anti: 派手な祝祭演出を排除
related:
  - components/progress.md
  - tokens/motion.md
---

# Loading — Pattern Component

待機・解析中の状態を伝える Pattern。
**過剰演出を避け、進行を誠実に表現**する。

## ブランド整合性
- **Drive**: 中央コアが Drive Orange でパルス
- **Continuity**: ステップリストで進行を積み上げ表現
- **Anti**: 「キラキラ」「もう少し！」等の煽りは禁止

---

## Variants（3 種）

| Variant | 用途 |
|---|---|
| **page** ★ | フル画面の待機（診断中・結果生成中） |
| **inline** | コンポーネント内の部分待機（カード内・リスト内） |
| **button** | ボタン内の処理中（btn.is-loading 既存） |

このドキュメントでは主に `loading-page` を扱う。

---

## Loading Page 構造

```html
<main class="loading-page">
  <!-- 背景装飾モニュメント (オプション) -->
  <span class="monument m1"></span>
  ...
  
  <div class="loading-page__inner">
    <!-- アニメーション: 同心円パルス + コア -->
    <div class="loading-anim">
      <span class="loading-anim__pulse"></span>
      <span class="loading-anim__pulse"></span>
      <span class="loading-anim__pulse"></span>
      <div class="loading-anim__core">
        <img src="assets/icons/state-loading-core.svg" alt="">
      </div>
    </div>
    
    <!-- テキスト -->
    <p class="loading-page__eyebrow">ANALYZING YOUR DATA</p>
    <h1 class="loading-page__title">あなたの診断結果を分析しています...</h1>
    
    <!-- ステップ進行（progress-steps を再利用） -->
    <ol class="progress-steps">...</ol>
    
    <!-- 入力サマリー（オプション） -->
    <div class="loading-summary">...</div>
  </div>
</main>
```

---

## アニメーション仕様

### 同心円パルス（3層）

| 項目 | 値 |
|---|---|
| 円サイズ | 200×200（PC） / 160×160（SP） |
| border | 2px solid `--color-drive` |
| キーフレーム | scale(0.3 → 1.0) + opacity(0 → 0.9 → 0) |
| duration | **2.4s** |
| timing | `ease-out` |
| ループ | `infinite` |
| 遅延スタガー | 0s / 0.8s / 1.6s（`--duration-pulse-ring / 3` 単位） |

```css
.loading-anim__pulse {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  height: 100%;
  border-radius: 50%;
  border: 2px solid var(--color-drive);
  opacity: 0;
  animation: pulseRing var(--duration-pulse-ring) ease-out infinite;
}
.loading-anim__pulse:nth-child(2) { animation-delay: calc(var(--duration-pulse-ring) / 3); }
.loading-anim__pulse:nth-child(3) { animation-delay: calc(var(--duration-pulse-ring) * 2 / 3); }

@keyframes pulseRing {
  0%   { transform: translate(-50%, -50%) scale(0.3); opacity: 0; }
  20%  { opacity: 0.9; }
  100% { transform: translate(-50%, -50%) scale(1); opacity: 0; }
}
```

### 中央コア

| 項目 | 値 |
|---|---|
| サイズ | 60×60 |
| background | `--color-drive` |
| アイコンサイズ | 28×28 |
| アイコン色 | `--color-white` |
| pulse | scale(1 → 1.08) 2s ease-in-out alternate |
| アイコン回転 | spin 4s linear（オプション） |

---

## テキスト仕様

| 要素 | スタイル |
|---|---|
| Eyebrow（"ANALYZING YOUR DATA"） | Poppins 14M / letter-spacing 0.16em / Drive Orange |
| Title | Hiragino W5 32px（PC）/ 24px（SP）/ line-height 1.5 |
| 進捗ステップ | `progress-steps` を使用（progress.md v0.3 参照） |

---

## 入力サマリー（オプション）

ユーザーが入力した内容を chip 形式で表示することで、**待機中の信頼感**を高める:

```html
<div class="loading-summary">
  <p class="loading-summary__title">YOUR INPUT</p>
  <div class="loading-summary__items">
    <span class="summary-chip"><strong>男性</strong> / 19-22歳</span>
    <span class="summary-chip"><strong>65kg</strong></span>
    <span class="summary-chip">目標: <strong>筋肉量増加</strong></span>
    ...
  </div>
</div>
```

### Summary Chip 仕様
| 項目 | 値 |
|---|---|
| padding | 6px 12px |
| background | `--bg-primary` |
| border | 1px `--border-light` |
| border-radius | 9999px |
| font-size | 12px |
| color | `--color-sub`（label 部）/ `--color-ink`（strong 部） |

---

## 背景装飾（オプション）

Result / Intro / Loading 画面で**統一感**を持たせるため、浮遊モニュメント4〜5体を背景に配置可能:

```html
<span class="monument m1"></span>
<span class="monument m2"></span>
...
```

詳細は **`tokens/motion.md`** の "Decoration Motion" 参照。

---

## prefers-reduced-motion 対応（必須）

```css
@media (prefers-reduced-motion: reduce) {
  .monument,
  .loading-anim__pulse,
  .loading-anim__core,
  .progress-step__indicator::after { animation: none !important; }
}
```

---

## Do / Don't

### ✅ Do
- 進行を誠実に表現（実際の処理に同期）
- ステップは 3〜5個（多すぎは認知負荷）
- 入力サマリーで「あなたの情報」を見せて待機の意義を伝える

### ✕ Don't
- 「もう少しで完成です！」等の煽り文言
- 5秒以上待たせる場合、**何もしない loading 画面**を作らない（必ずステップ等の進捗を見せる）
- 派手な祝祭演出（紙吹雪・キラキラ）を完了時に出さない（Brand Anti）

---

## Change Log

- v0.3 (2026-05-08): Loading画面実装から抽出して新規策定
