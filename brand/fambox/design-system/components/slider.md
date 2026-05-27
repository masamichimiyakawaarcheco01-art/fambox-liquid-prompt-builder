---
title: FAMBOX Primitive — Slider
type: design-system
layer: L2-Primitives
component: Slider
version: 0.3
status: confirmed
last_updated: 2026-05-08
owner: 宮川
source: 食事診断 Quiz画面 Q3（体重スライダー）からの抽出
brand_alignment:
  - Drive: Drive Orange thumb で操作箇所を明示
  - Light(300): 大型値表示で視覚補正を適用（光学補正ガイドラインの最初の実装例）
related:
  - components/form-controls.md
  - tokens/typography.md
---

# Slider — Primitive Component

数値を**範囲指定で選択**する Primitive。
体重 / 年齢 / 予算 / 評価点など連続値の入力に使用。

## ブランド整合性
- **Drive**: thumb は Drive Orange 固定（操作箇所の明示）
- **Light(300)**: 大型値表示は **`--fw-light: 300`** を使用（typography.md 光学補正ガイドラインの実装例）

---

## 構造

```html
<div class="slider">
  <div class="slider__display">
    <span class="slider__value">65</span><span class="slider__unit">kg</span>
  </div>
  <input type="range" min="40" max="120" value="65" class="slider__input">
  <div class="slider__range">
    <span>40 kg</span>
    <span>120 kg</span>
  </div>
</div>
```

---

## 仕様

### Container
| 項目 | 値 |
|---|---|
| padding | 32px |
| background | `--bg-primary` |
| border | 1.5px `--border-light` |
| border-radius | `--radius-lg`（12px） |

### Display（大型値表示）
| 項目 | 値 |
|---|---|
| font-family | `--font-en`（Poppins） |
| value font-size | **80px** |
| value font-weight | **`--fw-light`（300）** ★ |
| value letter-spacing | -0.02em |
| value color | `--color-drive` |
| unit font-size | 24px |
| unit font-weight | `--fw-medium` |
| unit color | `--color-sub` |
| unit margin-left | 8px |

### Track（バー）
| 項目 | 値 |
|---|---|
| height | 6px |
| background | `--bg-tertiary` |
| border-radius | 999px（pill） |

### Thumb（つまみ）
| 項目 | 値 |
|---|---|
| size | 28×28 |
| background | `--color-drive` |
| border | 4px solid white |
| box-shadow | `--shadow-2` |
| border-radius | 50% |
| cursor | pointer |

### Range Labels（min/max 表示）
| 項目 | 値 |
|---|---|
| font-family | `--font-en`（Poppins） |
| font-size | 12px |
| color | `--color-caption` |
| margin-top | 12px |

---

## CSS（実装）

```css
.slider {
  background: var(--bg-primary);
  border: 1.5px solid var(--border-light);
  border-radius: var(--radius-lg);
  padding: 32px;
}
.slider__display {
  text-align: center;
  margin-bottom: 32px;
}
.slider__value {
  font-family: var(--font-en);
  font-size: 80px;
  font-weight: var(--fw-light);  /* 光学補正 */
  letter-spacing: -0.02em;
  line-height: 1;
  color: var(--color-drive);
}
.slider__unit {
  font-family: var(--font-en);
  font-size: 24px;
  font-weight: var(--fw-medium);
  color: var(--color-sub);
  margin-left: 8px;
}
.slider__input {
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  height: 6px;
  background: var(--bg-tertiary);
  border-radius: 999px;
  outline: none;
}
.slider__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 28px;
  height: 28px;
  background: var(--color-drive);
  border-radius: 50%;
  cursor: pointer;
  border: 4px solid white;
  box-shadow: var(--shadow-2);
}
.slider__input::-moz-range-thumb {
  width: 28px;
  height: 28px;
  background: var(--color-drive);
  border-radius: 50%;
  cursor: pointer;
  border: 4px solid white;
  box-shadow: var(--shadow-2);
}
.slider__range {
  display: flex;
  justify-content: space-between;
  margin-top: 12px;
  font-family: var(--font-en);
  font-size: 12px;
  color: var(--color-caption);
}
```

---

## Variants（拡張余地）

| Variant | 用途 |
|---|---|
| `slider--with-display` ★ 既定 | 大型値表示あり（体重・年齢等） |
| `slider--minimal` | 値表示なし、バーとつまみのみ |
| `slider--dual` | 範囲選択（min/max 両つまみ） |

v0.3 時点では `slider--with-display` のみ確定。

---

## Accessibility

| 項目 | 仕様 |
|---|---|
| 操作 | キーボード矢印キーで増減 |
| ARIA | `aria-valuenow` / `aria-valuemin` / `aria-valuemax` / `aria-label` |
| Focus | thumb に `:focus-visible` で Drive 2px outline |
| label 連携 | `<label>` で input と紐付け |

---

## Do / Don't

### ✅ Do
- 数値表示は **Light(300)** で（白文字でなくとも、80pxサイズでは Regular より細く見せる）
- thumb は常に Drive Orange（操作箇所の明示）
- Range labels で min/max を表示

### ✕ Don't
- thumb を派手な色や複数色にしない
- value 表示を Bold にしない（**Anti: 太すぎ**）
- track の色を Drive にしない（操作前/後の混乱）

---

## Change Log

- v0.3 (2026-05-08): Quiz画面 Q3 体重スライダーから抽出して新規策定
