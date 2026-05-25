---
title: "段ボール箱が落ちて積み上がる 3D 物理シミュレーション（Brik Tool）"
url: https://brik.space/ToolViewer?slug=remix-of-cardboard-boxes-falling-remix-mp2hsixh
type: site
format: 3d-physics-animation
date_added: 2026-05-21
author: Brik コミュニティ（remix）
original_source: Brik by Wix
styles: [motion-graphic, lab-scientific, dynamic]
components: [hero-visual, load-accumulation]
mood: physical-realism, weight-burden, accumulation
keywords: [fambox-aligned-candidate, axis-4-candidate, 3d, physics, accumulation-metaphor, before-state, fatigue-load]
status: reviewed
priority: high
candidate_axis: "軸4 候補: 蓄積する負荷（Accumulating Load） — 軸2「動の発火」の前提状況（before）として機能"
related:
  - 2026-05-21_brik-showroom-typography.md
  - ../../../50_Business_Context/fambox-brand-dna-axes.md
  - ../../../30_Tech_Notes/brik-showroom-typography-2026-05.md
---

# 段ボール箱が落ちて積み上がる 3D 物理シミュレーション

## なぜ保存したか

**「積み上がる疲労」** を視覚化する canonical 候補。Lab 感のある中性的な背景の上に、重しとなる貨物（段ボール箱）が次々と落下し堆積していく 3D 物理シミュレーション。

FAMBOX が **解決する側の問題（before）** を表現する素材として強い。

## 注目ポイント（推定）

- **3D + 物理エンジン**: 落下・衝突・転倒・摩擦が物理法則どおりに動く → リアリティが高い
- **背景**: ラボ的・中性的・抑制された色数（暗示: 軸1「静の信頼」と地続きの土台）
- **質感**: 段ボールのテクスチャ・影の落ち方・反射 — モック感ではなく現実感
- **時間軸**: 「1 個 → 数個 → 山」と段階的に増加する単方向の動き
- **配色**: 単色〜2色程度に抑制（焦点を「重さ」と「数」に集中させる）
- **モーション**: 落下のタイミングがランダム → 単調にならず、観察を促す

## FAMBOX 軸との関連性

### A. 軸2「動の発火」の前提状況（before）として使う
> アスリートが日々蓄積する疲労・負荷 → そこから「次の一歩」を踏み出す瞬間（発火）。
> **箱が積み上がる映像 → カット → 火花が立ち上がる KV** の構成で、軸2の発火の重みが増す。

### B. 軸4 候補「蓄積する負荷（Accumulating Load）」
これは現時点では新軸の候補。**同方向の refs が追加2件以上集まった時点で正式昇格** ([fambox-brand-dna-axes.md](../../../50_Business_Context/fambox-brand-dna-axes.md) の軸3 候補昇格ルールに準拠)。

| 要素 | 表現 |
|---|---|
| キーワード | 蓄積 × 負荷 × 重さ × 疲労 × 反復 × 物理的リアリティ × 段ボール / 箱 / 鉛 / 鎖 |
| 視覚特徴 | 3D 物理シミュレーション / 中性的な背景 / 単方向の単調な増加 / 抑制された配色 |
| 担う機能 | FAMBOX が解決する問題側の可視化 / アスリート以外の文脈で「日常の負担」も表現可能 |
| 観察元 refs | 本 ref（cardboard-boxes-falling）— **シード 1件目** |
| 昇格条件 | 同方向の refs を **追加2件以上** で正式な「軸4」昇格 |

### C. 軸の時間アーク（更新案）
```
[軸4 候補] 蓄積する負荷  →  [軸2] 動の発火  →  [軸3 候補] 努力の結晶
Accumulating Load       Ignition × Calm        Crystallized Effort
   ↑                          ↑                       ↑
 蓄積された疲労          一歩踏み出す瞬間          努力が結晶化した姿
 (before / 問題)         (moment / 解決)          (outcome / 報酬)
   |                          |                       |
   +── 疲労が積もる → FAMBOX が燃料 → 発火 → 継続 → 結晶化 ──+
```

→ 軸4 候補が立つと、FAMBOX のストーリーは **「問題 → 介入 → 解決 → 結果」** の4段アーク（point of departure 含む）に進化する。

## ARCHECO / FAMBOX での応用案

### 即実装候補（Liquid / Web）
1. **商品ページ Hero before-after 構造**:
   - 上半分: 3D 箱が積み上がる短いループ動画（疲労）
   - 下半分: 火花が立ち上がるグラフィック（FAMBOX 介入後）
2. **食事診断ウィザード 冒頭**: 「あなたの今の負担は？」の問いとともに箱の積み上がり演出
3. **守屋選手企画**: 合宿シーズン冒頭の「日々の積み重ね」セクションで採用
4. **LP のスクロール演出**: 上から箱が落ちる物理アニメ → スクロール進行で減っていく演出（介入の効果可視化）

### 技法ライブラリ（実装候補）
- **Three.js + Cannon.js / Rapier.js**: 3D 物理エンジンで段ボール堆積を再現
- **Lottie**: 軽量化のため事前にレンダリング済みの mp4/webm を Lottie プレースホルダで再生
- **CSS3D + clip-path**: 軽量代替 — 完全 3D は無理だがフェイクで雰囲気再現
- **動画素材**: Brik 由来の素材を編集してそのまま Shopify Liquid に埋め込み（最速）

### Anti-pattern (避けるべき)
- 箱の数が少なすぎて「軽量化」が伝わらない
- 派手な色 / 派手な照明 → 軸1「静の信頼」と矛盾する
- ループの境目が露骨に見える（自然な物理シミュ感を損なう）

## 元情報

- URL: https://brik.space/ToolViewer?slug=remix-of-cardboard-boxes-falling-remix-mp2hsixh
- プラットフォーム: Brik by Wix（3D / モーション / インタラクション素材集）
- 種別: Tool Viewer 上のリミックス作品
- og:image: 取得不可（SPA / メタタグ未提供）
- 関連: [Brik Showroom タイポグラフィ実験11種](2026-05-21_brik-showroom-typography.md) — 同プラットフォーム

## Wiki

- [[../_by-style/motion-graphic.md]]
- [[../_by-style/lab-scientific.md]]
- [[../_by-style/dynamic.md]]
- [[../_by-component/hero-visual.md]]
- [[../_by-component/load-accumulation.md]] ★新設

## 関連

- [[../../../50_Business_Context/fambox-brand-dna-axes.md]] — 軸4 候補追加検討対象
- [[../../../brand/fambox/animation-library-v0.1.md]] — Animation Library への組込候補
- [[2026-05-21_brik-showroom-typography.md]] — 同 Brik プラットフォーム
- [[../2026/04/2026-04-28_nike-first-step-ignition.md]] — 軸2 発火の canonical（時間アーク後段）
