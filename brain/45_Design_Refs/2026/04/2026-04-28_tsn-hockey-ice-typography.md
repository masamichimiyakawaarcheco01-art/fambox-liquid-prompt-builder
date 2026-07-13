---
title: "TSN Hockey Rebrand — 氷で組まれたタイポグラフィ"
url: https://jp.pinterest.com/pin/116460340361341085/
type: pinterest-pin
format: static
date_added: 2026-04-28
author: Two Fresh Creative
original_source: twofresh.tv（TSN Hockey Rebrand プロジェクト）
image: https://i.pinimg.com/736x/8c/d0/8a/8cd08a7f46a139200fc9401b1acf23d8.jpg
styles: [typography-graphic, hybrid-composition, photography, monochrome, lab-scientific]
components: [typography-treatment, ice-imagery, hybrid-graphic, brand-identity, hero-typography, noise-texture]
mood: crystallized-effort
board: Interface Design
keywords: [fambox-aligned, axis-bridge, axis-3-candidate, ice-crystal, sweat-crystallization, achievement, transparent, curved-bg, noise-texture, hybrid-real-graphic, sports-branding]
status: reviewed
candidate_axis: "軸3候補: 努力の結晶 — Crystallized Effort"
---

# TSN Hockey Rebrand — 氷で組まれたタイポグラフィ

## なぜ保存したか

> **アスリートの努力と汗の結晶を表現するとき** に参考になりそう。
> 実写の氷と背景のグラフィックとの **ギャップ**、こすれた **ノイズ加工**、
> 氷の **半透明から湾曲した背景** が美しくまとまっている。
> アスリートの **実績、デザインにおける背景** として参考になるかも。

→ FAMBOX軸の **新たな次元** を提示する可能性のあるピン。

## ブランドDNA軸での位置づけ — **軸3候補**

これまでの2軸（静の信頼 × 動の発火）に **収まらない要素** を含む：

| 既存軸との関係 | 評価 |
|---|---|
| 軸1（静の信頼 — Lab × Editorial） | 部分的に該当（タイポブランディング、結晶質感） |
| 軸2（動の発火 — Ignition × Calm Resolve） | 部分的に該当（スポーツ文脈・アスリート） |
| **新次元** | **「努力の結晶化」「実績の凝縮」「汗の結晶」** ← 既存2軸では捉えきれない |

### 提案: 軸3候補「努力の結晶 — Crystallized Effort」

軸2「発火」の **時間的続き** として位置づけられる：

```
[軸1] 静の信頼      → 科学・データの土台
        ↓
[軸2] 動の発火      → 一歩踏み出す瞬間（火花→発火）
        ↓
[軸3 候補] 努力の結晶 → 努力が結晶化した姿（汗の結晶・実績）
```

軸3はFAMBOXの **「アスリートの達成」「継続が積み重なった結果」** を視覚化する側面。
ただし現時点では1件のみのため、**追加refsが集まれば正式昇格を検討** する候補状態。

## 注目ポイント
- **氷で組まれたタイポ**: テキスト "LEAD" が氷キューブ + プラスチックラップで構成される実写素材
- **実写 × グラフィックのギャップ**: 物理素材（氷）と抽象的グラフィック（湾曲背景）の対比が美しい
- **半透明と光の屈折**: 氷とラップの透過性が「内側を見せる」表現を可能に
- **ノイズ・テクスチャ**: プラスチックのしわ・反射、こすれた質感がリアリティを強化
- **湾曲した背景**: 直線的構成ではなく流動的なフォルムで動と静を統合
- **冷色トーン**: 静謐さと精度を演出
- **ホッケーの冷たさ・速度感** をブランド要素に翻訳した好例

## ARCHECO/FAMBOXでの応用案

### 1. アスリートの「結晶」表現
- **守屋選手の実績ビジュアル**: 試合数・年数・栄養への投資年月を「氷の結晶」として可視化
- **顧客実績ページ**: FAMBOX利用者の継続日数・改善成果を結晶モチーフで表現
- **記事のヘッダービジュアル**: 「努力の結晶」を象徴する氷タイポグラフィ

### 2. ハイブリッド合成技法（実写 × グラフィック）
- **食材の実写 + 抽象的グラフィック背景**: 食材を主役に、湾曲した抽象的背景で「栄養の流れ」を演出
- **氷 + 食材**: 鮮度・保管・冷凍配送の信頼性を視覚化（FAMBOXの配送特性と合致）

### 3. 軸2との接続（発火の余熱）
- 砂塵が飛散した（発火）後、**汗が結晶化** する瞬間 = FAMBOXが伴走するアスリートの軌跡
- 「発火の火種（粒子）」と「汗の結晶（氷）」は **エネルギー変換の前後** として連続する

### 4. Liquid/CSS実装研究
- **氷タイポ**: 画像で実装、`text-shadow` + `backdrop-filter` で氷っぽさを補強
- **湾曲背景**: SVG `<path>` + グラデーション、または CSS `clip-path`
- **ノイズ加工**: `feedback_fambox_visual_effects.md` の制限内で、軽微なグレイン or `filter: contrast()` の組み合わせ
- **半透明**: `backdrop-filter: blur()` + 半透明色

## 構成要素の整理（再現に向けて）

| レイヤー | 要素 |
|---|---|
| 1. 背景 | 湾曲した抽象的グラフィック（流動的フォルム） |
| 2. 中景 | こすれたノイズ・テクスチャレイヤー |
| 3. 主役 | 実写の氷+プラスチックラップで構成された素材 |
| 4. 主役上 | テキスト or ロゴ（オプション） |

→ FAMBOXのキービジュアル組み立て時、この4層構造を **テンプレ** として参照可能。

## 元情報
- URL: https://jp.pinterest.com/pin/116460340361341085/
- og:image: https://i.pinimg.com/736x/8c/d0/8a/8cd08a7f46a139200fc9401b1acf23d8.jpg
- 投稿者: Two Fresh Creative
- 元プロジェクト: TSN Hockey Rebrand（twofresh.tv）
- ピン説明: "ice cubes and plastic wrap" で構成された "LEAD" テキスト
- ボード: Interface Design（321ピン）

## Wiki
- [[../../_by-style/typography-graphic.md]]
- [[../../_by-style/hybrid-composition.md]]
- [[../../_by-style/photography.md]]
- [[../../_by-style/monochrome.md]]
- [[../../_by-style/lab-scientific.md]]
- [[../../_by-component/typography-treatment.md]]
- [[../../_by-component/ice-imagery.md]]
- [[../../_by-component/hybrid-graphic.md]]
- [[../../_by-component/brand-identity.md]]
- [[../../_by-component/hero-typography.md]]
- [[../../_by-component/noise-texture.md]]
- [[../../../50_Business_Context/fambox-brand-dna-axes.md]]
