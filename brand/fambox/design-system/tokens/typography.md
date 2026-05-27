---
title: FAMBOX Design Tokens — Typography
type: design-system
layer: L1-Tokens-Typography
version: 0.2
status: seed
last_updated: 2026-04-20
owner: 宮川
source: FAM Brand DNA v0.5 E章（継承）
---

# FAMBOX — Typography Tokens

## 設計原則
- **ジャンプ率「中〜高」**: display 56-96px ↔ body 16px（エディトリアル感、過度ではない）
- **英数字は Poppins、日本語は Hiragino Sans**（固定）
- **Display用の追加フォントは入れない**（シンプルさ優先）
- **見出しは英字主役＋日本語サポート**（視覚的インパクト）
- **基本8の倍数・16以下は4の倍数を推奨**（Worksheet §3 確定）
  - body-sm 14px は FAM v0.5 継承の例外。v0.3 で 12 or 16 への移行を検討

## Font Family

| 用途 | CSS Variable | 値 |
|---|---|---|
| 英数字（全用途） | `--font-en` | `'Poppins', sans-serif` |
| 日本語（全用途） | `--font-ja` | `'Hiragino Sans', 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif` |

### Weight
- Poppins: 400 / 500 / 600 / 700
- Hiragino: 300 / 400 / 600（W3 / W4 / W6 相当）

## Font Size Scale（10段階）

| CSS Variable | Value | 主な用途 | 倍数 |
|---|---|---|---|
| `--fs-caption` | `12px` | キャプション・細かな注釈 | 4倍 |
| `--fs-body-sm` | `14px` | 小テキスト・サブ情報 | ⚠️例外 |
| `--fs-body` | `16px` | 本文・標準UI | 8倍 |
| `--fs-lg` | `20px` | リード文 | 4倍 |
| `--fs-h3` | `24px` | 見出し H3 | 8倍 |
| `--fs-h2` | `32px` | 見出し H2 | 8倍 |
| `--fs-h1` | `48px` | 見出し H1 | 8倍 |
| `--fs-display` | `56px` | Display（落ち着いた主役）| 8倍 |
| `--fs-hero` | `64px` | Hero見出し（推奨）| 8倍 |
| `--fs-mega` | `96px` | Mega（超迫力・LP主役）| 8倍 |

## Weight / Line Height / Letter Spacing

| Token | 値 | 用途 |
|---|---|---|
| `--fw-regular` | 400 | 本文 |
| `--fw-medium` | 500 | 強調本文 |
| `--fw-semibold` | 600 | サブ見出し |
| `--fw-bold` | 700 | 見出し |
| `--lh-heading` | 1.2 | 見出し |
| `--lh-body` | 1.75 | 本文 |
| `--lh-caption` | 1.5 | キャプション |
| `--ls-en` | -0.02em | 英字（詰める） |
| `--ls-ja` | 0.02em | 日本語（開ける） |

## Text Style Preset ★ FAMBOX独自

よく使う組み合わせを preset 化して、命名で迷わないようにする。

```css
/* Display（B2B LP Hero等） */
.text-display {
  font-family: var(--font-en);
  font-size: var(--fs-hero);      /* 96px */
  font-weight: var(--fw-bold);
  line-height: var(--lh-heading);
  letter-spacing: var(--ls-en);
}

/* H1 */
.text-h1 {
  font-family: var(--font-en);
  font-size: var(--fs-h1);        /* 48px */
  font-weight: var(--fw-bold);
  line-height: var(--lh-heading);
  letter-spacing: var(--ls-en);
}

/* H2 */
.text-h2 {
  font-size: var(--fs-h2);        /* 32px */
  font-weight: var(--fw-bold);
  line-height: var(--lh-heading);
}

/* H3 */
.text-h3 {
  font-size: var(--fs-h3);        /* 24px */
  font-weight: var(--fw-semibold);
  line-height: var(--lh-heading);
}

/* Lead（リード文） */
.text-lead {
  font-family: var(--font-ja);
  font-size: var(--fs-lg);        /* 20px */
  font-weight: var(--fw-regular);
  line-height: var(--lh-body);
  letter-spacing: var(--ls-ja);
}

/* Body */
.text-body {
  font-family: var(--font-ja);
  font-size: var(--fs-body);      /* 16px */
  font-weight: var(--fw-regular);
  line-height: var(--lh-body);
  letter-spacing: var(--ls-ja);
}

/* Body Small */
.text-body-sm {
  font-family: var(--font-ja);
  font-size: var(--fs-body-sm);   /* 14px */
  line-height: var(--lh-body);
}

/* Caption */
.text-caption {
  font-family: var(--font-ja);
  font-size: var(--fs-caption);   /* 12px */
  color: var(--color-caption);
  line-height: var(--lh-caption);
}

/* Data Big Stat（数値強調） */
.text-stat {
  font-family: var(--font-en);
  font-size: var(--fs-display);   /* 64px */
  font-weight: var(--fw-bold);
  line-height: 1;
  letter-spacing: var(--ls-en);
}
```

## Do / Don't

### ✅ Do
- 見出しは英字主役＋日本語サポート（例: `<h1>FAMBOX <span class="sub">チーム栄養ソリューション</span></h1>`）
- 数字は半角・単位小さく・大数字は太く
- 本文は必ず日本語ベース、英字が混じったら `var(--ls-en)` を部分適用

### ✕ Don't
- Poppins と Hiragino 以外のフォントを追加しない（Display フォントも不要）
- Display 用に派手なサンセリフや手書き風を使わない
- `font-size: 10px` 等、`--fs-caption` より小さい値は使わない
- キャプションの背景コントラストが不足する場所に配置しない
