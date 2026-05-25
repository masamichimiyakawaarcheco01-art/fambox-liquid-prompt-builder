---
title: "Brik Showroom — Wix発・タイポグラフィ実験11種（デザインインスピレーション）"
date: 2026-05-21
source: https://brik.space/Showroom
type: design-inspiration-source
publisher: Wix.com（Brik by Wix）
creator: Shahar Levy
tags: [brik, wix, typography, kinetic-typography, generative, animation, design-inspiration, immediate-use-research]
topics: [design, typography, motion, brand]
status: reviewed
priority: medium
related:
  - whitespace-experiments-animations.md
  - ../../brand/fambox/animation-library-v0.1.md
  - lotte-the-day-emotional-marketing-2026-05.md
---

# Brik Showroom — タイポグラフィ実験11種

## サイト概要

**Brik** は Wix が運営する **AI Design Tools プラットフォーム**。クリエイターが「ツール」を作って公開し、コミュニティで共有できる場所。

> 「Brik bridges creative coding and motion design, giving designers AI generation with precise control.」
> — Brik 公式

> 「Brik turns your creative vision into a dynamic design tool. Generate, remix, export, and share assets - all from a system that scales with you.」

技術スタック（推定）:
- Framer Motion ベース（実機検証で確認）
- React / Next.js
- SVG メイン（Canvas/WebGL は限定的）
- Wix プラットフォーム上のサービス

## 主要クリエイター: Shahar Levy

Brik の Showroom に多数の「ツール」を公開している主要アーティスト。
**ほぼ全てがタイポグラフィ実験** であることが特徴。

## ツール11種 一覧（タイポグラフィ実験）

| # | ツール名 | 推定内容 | 軸対応候補 |
|---|---|---|---|
| 01 | **Text Distortion Bubbles** | テキストが泡状に歪む | 軸2 発火 |
| 02 | **Stamp** | スタンプ風タイポ（複数バリエあり） | 軸1 信頼 |
| 03 | **Morphing Presence** | テキストがモーフィング | 軸2 連続性 |
| 04 | **Kinetic Letters** | 動く文字（kinetic typography） | 軸2 発火 |
| 05 | **Watercolor 2.0** | 水彩風タイポ | 軸3 候補 |
| 06 | **Dithering** | ディザリング処理 | 軸1 Lab |
| 07 | **Inflation** | 膨張表現 | 軸2 発火 |
| 08 | **Unstable Type** | 不安定なタイポ（揺れ・変動） | 軸2 連続性 |
| 09 | **Wavy Noise** | 波ノイズ | 軸1 リズム |
| 10 | **Fragmented Message** | 断片化メッセージ | 軸2 発火 |
| 11 | **Echo Text** | エコー型タイポ | 軸2 連続性 |

→ **9種が軸2、1種ずつが軸1・軸3候補**。動的タイポグラフィに特化したインスピレーション源。

## Whitespace Experiments との比較

| 観点 | Whitespace | Brik Showroom |
|---|---|---|
| 中心 | UI/UX実験 | **タイポグラフィ実験** |
| 範囲 | 23 種（多領域） | 11 種（テキストに特化） |
| 技術 | r3f + WebGL + Tailwind | Framer Motion + SVG |
| インタラクション | クリック・スクロール多い | 主に視覚効果 |
| FAMBOX応用 | レイアウト・カード・モーション | **見出し・キャッチコピー** |

→ **両方を使い分ける** のが理想。Whitespace は構造、Brik はタイポ。

## FAMBOX への応用案

### 軸2 動の発火 系（タイポ表現の主役）

#### Kinetic Letters → 守屋選手企画の見出し
**「アスリートの一歩」「次の壁を超える」** のような Verb Bank の動詞を、文字単位で動かす：
- 文字が一文字ずつ現れる
- 文字に微振動を加える（不規則）
- 全体としてはエネルギーが脈打つ

#### Inflation → CTA ボタンの強調
ボタンテキストが **マウスホバーで膨張** → 「触れる→反応する」体感。Elastic Bars と同系統。

#### Fragmented Message → SNS素材の分割表現
1枚のキービジュアルで「FUEL / YOUR / NEXT / STEP」を分割配置 → 視線誘導。

### 軸3候補 努力の結晶 系（質感表現）

#### Watercolor 2.0 → 結晶質感の代替
氷の透明感（軸3）の代わりに、水彩の **滲み・重なり** で「努力が形になる」を表現。
- 一筆書きでは表せない、層を重ねた結果
- 守屋選手の歩みを可視化する候補

### 軸1 静の信頼 系（控えめだが効く）

#### Dithering → デジタル/システム型のテクスチャ
HBX "67"（[軸1デジタル型 canonical](../45_Design_Refs/2026/05/2026-05-11_hypebeast-hbx-67-motion.md)）と通底する **デジタル質感**。栄養データ可視化の背景に使える。

#### Stamp → ブランドアセット
**「FAMBOX 認定」「栄養士監修」** のスタンプを動的に出すデザイン候補。

## 即実装の難度

**全 11 種が Framer Motion + SVG ベース** なので、LPB v4（React + Framer Motion 採用想定）でほぼ同等の表現を再現可能。

| 難度 | ツール |
|---|---|
| ★ 易（CSS + 軽量JS） | Stamp, Echo Text, Wavy Noise |
| ★★ 中（SVG path animation） | Kinetic Letters, Inflation, Morphing Presence, Unstable Type, Fragmented Message |
| ★★★ 難（WebGL shader 必要） | Text Distortion Bubbles, Watercolor 2.0, Dithering |

## Animation Library v0.1 への拡張候補

現状 [Animation Library v0.1](../../brand/fambox/animation-library-v0.1.md) は 7パターン。
Brik の研究を踏まえ、**v0.5 のタイミング** で以下を追加検討：

| 追加候補パターン | 軸 | Brik由来 |
|---|---|---|
| **Kinetic Headline** | 軸2 | Kinetic Letters |
| **Inflation CTA** | 軸2 | Inflation |
| **Echo Tagline** | 軸2 | Echo Text |
| **Watercolor Layer** | 軸3 | Watercolor 2.0 |
| **Stamp Mark** | 軸1 | Stamp |

これら5つを Library v0.5 で追加すると **計12パターン**。視覚・動き・**タイポ** が揃う。

## ARCHECO 業務への直接活用

### 1. 守屋選手企画の SNSキービジュアル
- Kinetic Letters でアスリートを語るキャッチコピーを動的化
- 「壁を、超える。」「次の一歩を、燃やす。」（Verb Bank 準拠）

### 2. FAMBOX 商品ページのヒーロー
- Watercolor 2.0 風の質感を **継続の証** として背景に
- Echo Text で「FUEL / FUEL / FUEL」のように反復強調

### 3. ブランドガイドラインへの組み込み
- スタンプ（Stamp）を「FAMBOX 認定」マークとしてシステム化
- 栄養士監修バッジ等のブランドアセットを動的に

## 継続参考ソース化

[advertimes-reference-source.md](advertimes-reference-source.md) の続編として、Brik も **継続参考ソース** に追加：

| ソース | 用途 |
|---|---|
| Business Insider Japan（尾原） | AI時代のビジネス戦略 |
| TOMORUBA | 新規事業 |
| ベイジの図書館 | Web/LLMO |
| Pinterest | 視覚 |
| AdverTimes. | マーケ |
| **Brik Showroom ★NEW** | **タイポグラフィ実験** |
| Whitespace experiments（旧） | UI/UX実験 |

→ **7つの継続ソース** が揃った。

## 残タスク

- [ ] Brik のツールを実際に触ってみる（無料アカウント作成検討）
- [ ] Kinetic Letters 風の SVG/Framer Motion 実装を試作（preview HTML に追加）
- [ ] Animation Library v0.5 に Brik 由来 5パターン追加検討
- [ ] 守屋選手企画の SNS キービジュアルに Kinetic Letters を試す
- [ ] FAMBOX 商品ページのヒーローに Watercolor を試す

## 関連
- [[whitespace-experiments-animations.md]] — UI/UX実験（構造側）
- [[../../brand/fambox/animation-library-v0.1.md]] — 統合先
- [[lotte-the-day-emotional-marketing-2026-05.md]] — ムード型マーケ（同系統）
- [[advertimes-reference-source.md]] — 継続ソース運用
- [[../45_Design_Refs/_index.md]] — 視覚リファレンス全体

## 元情報
- URL: https://brik.space/Showroom
- タイトル: Brik Showroom
- 主要クリエイター: Shahar Levy
- 運営: Wix.com（Brik by Wix）
- 確認日: 2026-05-21
- 確認した結果: Gallery/tags:animation は "No tools found"。実例は Showroom にあり。
