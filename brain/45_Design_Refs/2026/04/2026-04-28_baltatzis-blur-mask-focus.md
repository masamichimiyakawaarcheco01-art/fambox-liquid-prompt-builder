---
title: "ぼかし×マスクでアスリートの集中を可視化（モーション）"
url: https://jp.pinterest.com/pin/116460340361423759/
type: pinterest-pin
format: motion-design
date_added: 2026-04-28
author: Christos Baltatzis
original_source: Dribbble
image: https://i.pinimg.com/originals/f5/4e/bc/f54ebc0d686cd519cc51625dbc8a6a8f.gif
styles: [minimal, monochrome, motion-graphic, lab-scientific]
components: [focus-visualization, blur-mask-effect, motion-design, logo-animation]
mood: focused-stillness
board: Inspiration
keywords: [fambox-aligned, axis-2, blur, mask, focus, concentration, athlete-psychology, motion-design, glass-lens-light, calm-resolve]
status: reviewed
---

# ぼかし×マスクでアスリートの集中を可視化（モーション）

## なぜ保存したか

> このピンは **アスリートにある「集中」する様を、ぼかしとマスクを活用して可視化** している。
> アスリートの心情を表す **1つの効果方法** として参考になる。

→ 軸2「動の発火」の中の **「静の冷静」「ガラス/レンズ越しの光」** の系譜を、具体的な **モーション技法** で実現している事例。

## ブランドDNA軸での位置づけ

**軸2: 動の発火 — Ignition × Calm Resolve** の **「Calm Resolve」側** を担う技法サンプル。
ACW Sport Poster（軸2 / 火花〜発火側） とは別の側面で、**集中・冷静・揺るぎなさ** を表現する技術として並走する。

| 軸2の構成要素 | 該当リファレンス |
|---|---|
| 火花 → 発火（点火・行動への立ち上がり） | [ACW Sport Poster](2026-04-28_acw-sport-poster.md) |
| **Calm Resolve（集中・静の冷静・固まった意思）** | **このピン**（ぼかし×マスク） |

軸2は単一表現ではなく、この **動 × 静の二重性** を視覚化する複合軸であることが、2件目で明確化された。

## 注目ポイント
- **技法**: ぼかし（blur） + マスク（mask）の重ね合わせで「焦点の絞り」を表現
- **モーション**: GIF形式 → 時間軸で「集中していく/解けていく」プロセスを描く可能性
- **配色**: 黒×白の高コントラスト → 余計なものを排した「集中状態」のメタファー
- **タイポ**: "FCS"（FoCuS の省略 / Focus と読める）→ 言葉自体が主題
- **ミニマル × ラボ感**: 装飾ゼロ・幾何学的フレーム

## ARCHECO/FAMBOXでの応用案

### 1. 守屋選手企画への直接応用
- **インタビュー動画/SNSショート**: 守屋選手の表情に同様のぼかし×マスク処理を重ね、「試合前の集中状態」を可視化する演出
- **キービジュアル**: 静止画でもぼかし+円形マスクで「視線の先に集中している様子」を伝える

### 2. FAMBOX UI実装の研究テーマ
**Liquid/CSSでの再現候補**:
- `filter: blur()` + `mask-image: radial-gradient()` の組み合わせ
- SVG `feGaussianBlur` + `mask` 要素
- `backdrop-filter: blur()` で背景のみぼかし、フォアグラウンドはシャープに保つ
- 注意: `feedback_fambox_visual_effects.md` の制限（輪郭歪み・noise-bloom・グリッチ禁止）の **範囲内** で運用

### 3. 「集中」を視覚化する場面
- **FAMBOX診断ウィザード**: 「あなたの目標」フォーカス時に背景をぼかして当該入力にスポットを当てる
- **栄養データ表示**: 注目している成分（例: タンパク質）を強調、その他をぼかす
- **記事内インタラクション**: スクロール連動で読んでいる箇所を強調する効果

### 4. WorRC / 化学式概念図 と組み合わせる方向性
**軸1 + 軸2の合成例**:
- 化学式風概念図（軸1: lab-scientific）の上に、ぼかし×マスクで「今ハイライトされた分子」を強調 → 静的な信頼の上に動的な集中を重ねる

## 元情報
- URL: https://jp.pinterest.com/pin/116460340361423759/
- og:image: https://i.pinimg.com/originals/f5/4e/bc/f54ebc0d686cd519cc51625dbc8a6a8f.gif
- 投稿者: Christos Baltatzis
- 元サイト: Dribbble
- ボード: Inspiration（244ピン / Art）

## Wiki
- [[../../_by-style/minimal.md]]
- [[../../_by-style/monochrome.md]]
- [[../../_by-style/motion-graphic.md]]
- [[../../_by-style/lab-scientific.md]]
- [[../../_by-component/focus-visualization.md]]
- [[../../_by-component/blur-mask-effect.md]]
- [[../../_by-component/motion-design.md]]
- [[../../_by-component/logo-animation.md]]
- [[../../../50_Business_Context/fambox-brand-dna-axes.md]]
- [[../../../20_Projects/moritani-ambassador/overview.md]]
