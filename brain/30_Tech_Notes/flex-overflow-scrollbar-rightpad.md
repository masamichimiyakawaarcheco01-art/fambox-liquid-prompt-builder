---
title: flex + overflow-x の padding-right が効かない既知挙動と回避パターン
date: 2026-05-25
tags: [css, flex, overflow-x, horizontal-scroll, chrome, safari, browser-quirks, liquid]
status: active
priority: high
source:
  - sections/fambox-faq.liquid:84-97 (commit 65ac176)
  - sections/fambox-faq.liquid:218-230 (SP overrides)
related:
  - ./liquid-z-index-fix-patterns.md
  - ../../sections/fambox-blog-carousel.liquid
  - ../../sections/fambox-active-plans-v2.liquid
---

# flex + overflow-x の padding-right が効かない既知挙動

横スクロール UI を作る時に **何度も再発見してデバッグしていた問題** をここに固定する。

## TL;DR

**症状**: `display: flex` + `overflow-x: auto` のコンテナで `padding-right` がスクロール終端で消える。
**原因**: **Chrome / Safari の既知挙動** — flex の `padding-right` がスクロール領域に含まれない（scroll viewport から計算されない）。
**回避**: 子要素として `::after` の **スペーサー（透明 flex item）** を入れる。

## ❌ 期待通り動かないコード

```css
.scroll-track {
  display: flex;
  gap: 32px;
  padding-left: 64px;
  padding-right: 64px;  /* ← Chrome/Safari でスクロール終端に余白が出ない */
  overflow-x: auto;
}
```

スクロール終端でカードがビューポート右端に張り付き、視覚的に「途切れた」印象になる。

## ✅ 正しいパターン

```css
.scroll-track {
  display: flex;
  gap: 32px;
  padding-left: 64px;
  /* padding-right は使わない */
}

/* 右側スペーサー: スクロール終端に左と同等の余白 */
.scroll-track::after {
  content: '';
  flex: 0 0 64px;  /* ← 確保したい右余白幅と同じ */
  height: 1px;
  align-self: stretch;
}
```

ポイント:
- `::after` は flex item なのでスクロール領域に含まれる
- `flex: 0 0 [幅]` で幅を固定（伸縮させない）
- `height: 1px` + `align-self: stretch` で見えないが寸法は持つ

## 実装例（FAMBOX FAQ section）

`sections/fambox-faq.liquid:84-97` で本パターンを採用。1440px 基準のレスポンシブ計算を含む完全版:

```liquid
/* PC: 中央寄せ + 左右 64px 余白 */
#{{ sec_id }} .faq__scroll-track {
  display: flex;
  gap: 32px;
  padding-left: max(64px, calc((100% - 1440px) / 2 + 64px));
}
#{{ sec_id }} .faq__scroll-track::after {
  content: '';
  flex: 0 0 max(64px, calc((100% - 1440px) / 2 + 64px));
  height: 1px;
  align-self: stretch;
}

/* SP: 24px 余白 */
@media (max-width: 750px) {
  #{{ sec_id }} .faq__scroll-track {
    padding-left: 24px;
  }
  #{{ sec_id }} .faq__scroll-track::after {
    flex: 0 0 1px;  /* 既存のスナップ用ダミーと統合 */
  }
}
```

## 関連する別パターン: scroll-snap との併用

`scroll-snap-type: x mandatory` で最後のカードを左寄せスナップさせたい場合、右側スペーサーは **1px 幅で十分**:

```css
.scroll-track {
  scroll-snap-type: x mandatory;
}
.scroll-track > * {
  scroll-snap-align: start;
}
.scroll-track::after {
  flex: 0 0 1px;  /* 視覚的余白は不要、スナップだけ目的 */
  width: 1px;
}
```

「視覚的右余白」と「スナップ用ダミー」は **目的が違う** ことに注意。

## なぜ Chrome/Safari でだけ起きるか

仕様上は曖昧で、Chrome/Safari は **scrollWidth の計算に padding-right を含めない** 実装になっている。Firefox は含めるので問題が出ない。

WebKit Bug: https://bugs.webkit.org/show_bug.cgi?id=129441 (2014 から open）
Chromium Bug: https://issues.chromium.org/issues/40065222

**「ブラウザバグ」ではなく「仕様の解釈差」**として 10 年以上残っている。今後も直る予定なし。

## チェックリスト（横スクロール UI を作る時）

新しい横スクロールセクションを作る前に必ず確認:

- [ ] `padding-right` で右余白を作っていないか? → `::after` スペーサーに置き換える
- [ ] Chrome / Safari で実機確認したか? → Firefox では問題が出ないので発見が遅れる
- [ ] スクロール終端でカードが右端ピッタリになっていないか?
- [ ] scroll-snap を使う場合、スナップ用ダミーと視覚的余白用スペーサーを区別したか?

## 適用済セクション

- ✅ `sections/fambox-faq.liquid`（commit 65ac176 で対応）
- ⚠ `sections/fambox-active-plans-v2.liquid` — 同パターン使用、要確認
- ⚠ `sections/fambox-blog-carousel.liquid` — bc__track-wrap で関連実装

新規セクション作成時に **同じ罠を踏まないように本ノートを参照する**。

---

## 出典

- **commit 65ac176** — chore(sections): bulk maintenance (2026-05-25)
  - sections/fambox-faq.liquid のスクロール終端余白修正
  - 旧: `padding-right: max(0px, calc((100% - 1440px) / 2))`（効かない）
  - 新: `.faq__scroll-track::after` スペーサー（効く）
