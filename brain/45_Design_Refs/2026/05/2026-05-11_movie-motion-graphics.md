---
title: "Movie Motion Graphics — 中央横線基準の上下切替トランジション"
url: https://jp.pinterest.com/pin/68749335936/
type: pinterest-pin
format: motion
date_added: 2026-05-11
author: Rodrigo Mendes（ピン投稿）/ Jamaal Purcell-Edwards（作者）
original_source: Pinterest（ボード「3d」2000ピン）
styles: [motion-graphic, typography-graphic, editorial, dynamic]
components: [motion-design, typography-treatment, kinetic-typography, horizontal-split-transition, content-switcher]
mood: smooth-rhythmic
board: 3d
keywords: [transition, kinetic-typography, horizontal-line-split, content-switching, rhythmic-animation, ui-pattern]
status: reviewed
candidate_axis: "技法参考（軸補助）— ナビ/コンテンツ切替"
---

# Movie Motion Graphics — 中央横線基準の上下切替トランジション

## なぜ保存したか

> **トランジションの参考になる**。
> 複数のコンテンツを **中央の横線から上下に切り替わる** ことで何のコンテンツが含まれているか分かりやすく、
> **タイポグラフィと直線的な緩急のアニメーション** が心地よい。

→ FAMBOXのナビゲーション・コンテンツカテゴリ切替・情報階層の遷移に直接応用できるトランジション技法。

## ブランドDNA軸での位置づけ — 技法参考（軸補助）

軸そのものではないが、**軸間の遷移**や **軸内のコンテンツ切替** を演出する補助技法：
- 軸1の「論理的整理」を動きで見せたいとき
- 複数の食事カテゴリを切り替えるUI
- 診断ウィザードのステップ遷移

特に HBX "67"（軸1: デジタル/システム型）と組み合わせると、**機械的スムーズ × 横線切替** で科学的論理性を動きで語れる。

## 注目ポイント
- **トランジション手法**: 中央の横線を基準に、コンテンツが上下に切り替わる
- **明確性**: 何のコンテンツに切り替わったかが瞬時に分かる
- **タイポと動き**: タイポグラフィ + 直線的な動きの緩急 = 心地よいリズム
- **Kinetic Typography**: 文字そのものが意味を運ぶ表現
- **緩急**: 直線的だが、リズム感のあるイージング

## ARCHECO/FAMBOXでの応用案

### 1. 商品カテゴリ切替UI
- メニュー（朝食/昼食/夕食/補食）を **横線基準の上下スライド** で切り替え
- 切替時にタイポグラフィが先導するアニメーション
- 「何のコンテンツに切り替わったか」が一目で分かる導線

### 2. FAMBOX診断ウィザード
- ステップ間の遷移を **横線基準スライド** で表現
- Q1 → Q2 への遷移で、上が結果サマリ・下が新質問の構造

### 3. ナビゲーション
- グローバルナビのカテゴリ切替（栄養知識 / アスリート事例 / 商品 / 診断）
- ヘッダーの記事一覧切替

### 4. Liquid/CSS実装
- `transform: translateY()` + `transition: cubic-bezier(.4, 0, .2, 1)` で滑らかさ
- 中央に固定の横線（border）→ その上下で `clip-path` or `overflow: hidden` の二領域
- 直線的な緩急 = `linear` ではなく `ease-out` 系のイージング
- 切替時にタイポが先に動き、コンテンツが追従する2段階アニメーション

### 5. HBX "67" との組み合わせ
- HBX = 「機械的スムーズなトランジション」
- このピン = 「横線基準の切替パターン」
- 組み合わせで「**機械的スムーズ × 横線切替**」の科学的論理性UIが構築可能

## 元情報
- URL: https://jp.pinterest.com/pin/68749335936/
- ピン投稿者: Rodrigo Mendes
- 作者: Jamaal Purcell-Edwards
- ボード: 3d（2000ピン）

## Wiki
- [[../../_by-style/motion-graphic.md]]
- [[../../_by-style/typography-graphic.md]]
- [[../../_by-component/motion-design.md]]
- [[../../_by-component/kinetic-typography.md]]
- [[../../_by-component/horizontal-split-transition.md]]
- [[../../_by-component/content-switcher.md]]
