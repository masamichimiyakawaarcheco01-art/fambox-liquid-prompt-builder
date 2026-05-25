---
title: "whitespace experiments — 23 アニメーション技法集（即実装ガイド）"
date: 2026-05-20
source: https://experiments.thisiswhitespace.com/
type: design-tech-reference
author: Whitespace Studio
tags: [animation, design-tech, react, threejs, r3f, tailwind, framer-motion, shaders, html-in-canvas, immediate-use]
topics: [design, engineering, frontend]
status: active
priority: high
applicability:
  - fambox-product-pages
  - fambox-diagnosis-wizard
  - moritani-ambassador-sns
  - lpb-liquid-pipeline-output
related:
  - ../50_Business_Context/fambox-brand-dna-axes.md
  - design-acceptance-parameters.md
---

# whitespace experiments — アニメーション技法集（即実装ガイド）

[Whitespace Studio](https://thisiswhitespace.com) が運営する [experiments.thisiswhitespace.com](https://experiments.thisiswhitespace.com/) は、Next.js + Tailwind + Framer Motion + React Three Fiber を組み合わせた **23 の実験的UI/アニメーション** の宝庫。FAMBOX/守屋企画/LPB に **今すぐ転用可能** な技法を抽出する。

## 技術スタック（共通）

| 層 | 採用 |
|---|---|
| ビルド | Next.js（Turbopack） |
| スタイリング | **Tailwind CSS v4** |
| 動き | **Framer Motion**（will-change: transform を多用） |
| 3D / シェーダ | **React Three Fiber + Three.js + GLSL shader** |
| HTML in Canvas | **WICG html-in-canvas（実験的API）** |
| カラー | OKLCH / `color(srgb …)` 関数表記 |

→ **Liquid Pipeline / LPB v4** にも全て統合可能（既にReact + TS + Tailwind v4 採用済）。

---

## 全23実験 — 一覧マップ（タグ別）

| 実験 | URL slug | タグ | 即実装難度 | FAMBOX軸 |
|---|---|---|---|---|
| **Pattern Cards** ⭐ | pattern-cards | layout / cards / static | ★ 易（CSS+SVG） | 軸1 適用型 |
| Twisting Ribbons | twisting-ribbons | r3f / shader | ★★★ 難 | — |
| **Glass Hero** ⭐ | glass-hero | r3f / glass / dispersion | ★★★ 難（要 WebGL） | 軸2 Calm Resolve |
| Dot Form 3D | dot-form | html-in-canvas / 3d / transition | ★★★ | — |
| Shader Deck | shader-deck | r3f / carousel | ★★★ | — |
| Code Slice Hero | code-slice-hero | r3f / shader / landing | ★★★ | 軸1 デジタル/システム |
| **Dot Phone Carousel** ⭐ | dot-phone-carousel | canvas / carousel / transition | ★★ 中 | 軸2 動 |
| **Cursor Nav** ⭐ | cursor-nav | interactive / ui / 3d | ★★ 中 | UX技法 |
| Particle Phones | particle-phones | particles / 3d / scroll | ★★★ | 軸2 発火（粒子） |
| **Dot Hover Cards** ⭐⭐ | dot-hover-cards | interactive / cards / pattern | ★ 易（CSS+JS） | **軸1 適用型** |
| Curtain Sidebar | curtain-sidebar | transition / ui / shader | ★★ | UI技法 |
| Mobius Strip | mobius-strip | r3f / html-in-canvas | ★★★ | — |
| Shader Cards | shader-cards | particles / shader | ★★★ | 軸2 結晶 |
| HTML in Canvas | html-in-canvas | experimental / r3f | ★★★ | — |
| **Shape Cards** ⭐ | shape-cards | layout / shapes / static | ★ 易（CSS+SVG） | 軸1 適用型 |
| Viewport Transition | viewport-transition | r3f / transition / 3d | ★★★ | — |
| Folder Gallery | folder-gallery | transition / interactive | ★★ | UI技法 |
| Neural Burst | neural-burst | r3f / 3d / network | ★★★ | 軸1 概念図 |
| **Clay Toggle** ⭐ | clay-toggle | r3f / ui / 3d | ★★ | UI技法 |
| **Morph Blob** ⭐ | morph-blob | svg / perlin-noise | ★★ 中 | 軸2 発火 |
| Creativity Dial | creativity-dial | interactive / ui / shader | ★★ | 軸1 デジタル |
| **Elastic Bars** ⭐ | elastic-bars | svg / elastic / interactive | ★ 易（SVG+JS） | 軸2 火花 |
| Microchip Viewer | microchip-viewer | r3f / 3d / interactive | ★★★ | 軸1 デジタル |

⭐ = FAMBOX/守屋企画に **即転用すべき優先候補**。⭐⭐ = 最優先。

---

## 即実装パターン（CSS / Tailwind / SVG のみ）

### 1. **Pattern Cards** — ドットパターン + カラーカード

**実装ヒント**（実機調査結果）：

```tsx
{/* Tailwind v4 + 単純なTSX */}
<div className="h-screen flex">
  {/* Card 1: Black with arrow-wedge dot pattern */}
  <div
    className="relative shrink-0 overflow-hidden bg-[#0a0a0a]"
    style={{
      width: 324,
      height: 414,
      borderRadius: '44.875px',
    }}
  >
    {/* SVG ドットパターン（127×335 viewBox 推奨） */}
    <svg
      className="absolute inset-0 w-full h-full"
      viewBox="0 0 127 334.57"
      preserveAspectRatio="xMidYMid slice"
    >
      <g fill="rgba(255,255,255,0.18)">
        {Array.from({length: 12*32}).map((_, i) => {
          const col = i % 12;
          const row = Math.floor(i / 12);
          // 矢印くさび型: row が増えるほど中心に近づく
          const cx = (col + 0.5) * 10 + Math.sin(row * 0.2) * 4;
          const cy = (row + 0.5) * 10;
          return <circle key={i} cx={cx} cy={cy} r="1.2" />;
        })}
      </g>
    </svg>

    {/* タイトルは bottom-left に配置 */}
    <h2 className="absolute bottom-6 left-6 text-white text-2xl font-bold">
      Pattern Cards
    </h2>
  </div>

  {/* Card 2: Orange / Card 3: Warm gray も同パターン */}
</div>
```

**ポイント**:
- 角丸 **44.875px**（≈45px）= モダンなソフト感
- 背景: `bg-[#0a0a0a]`（黒）/ オレンジ / 暖グレー（`rgb(224, 223, 221)`）
- ドットパターンは **SVG `<circle>`** を `Array.from` でループ生成
- タイトルは絶対配置で bottom-left

**FAMBOX応用**: 食材カード・診断結果カード・メニュー紹介カードの **静的ブランド表現**。軸1 適用型に直結。

---

### 2. **Dot Hover Cards** — グレードット背景 × ホバーで色変化

**コンセプト**: 全画面グレードット → カードホバー時にそのエリアだけ **色付きドット + 拡大** に変化。

**最小実装**:

```tsx
<div className="min-h-screen bg-neutral-900 relative">
  {/* 背景: 全画面ドット（CSS radial-gradient で実現） */}
  <div
    className="absolute inset-0 pointer-events-none"
    style={{
      backgroundImage: 'radial-gradient(circle, #444 1px, transparent 1px)',
      backgroundSize: '14px 14px',
    }}
  />

  {/* カードのグリッド */}
  <div className="relative grid grid-cols-3 gap-6 p-12">
    {items.map((item, i) => (
      <div
        key={i}
        className="group relative aspect-[3/4] rounded-3xl overflow-hidden
                   transition-transform duration-500 hover:scale-105"
      >
        {/* カードエリアのドットを置き換えるオーバーレイ（ホバー時に表示） */}
        <div
          className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
          style={{
            backgroundImage: 'radial-gradient(circle, #06c352 1.5px, transparent 1.5px)',
            backgroundSize: '12px 12px',
            backgroundColor: '#0a0a0a',
          }}
        />
        <h3 className="absolute bottom-6 left-6 text-white text-xl z-10">{item.title}</h3>
      </div>
    ))}
  </div>
</div>
```

**FAMBOX応用 ⭐⭐**: 食材一覧グリッド・診断ステップ・メニュー比較。**軸1適用型の最有力候補**。

---

### 3. **Shape Cards** — ランダム幾何学カード

**コンセプト**: 複数の幾何形（円・矩形・三角）を重ねた装飾的カード。Curated color palette を使う。

**最小実装**:

```tsx
const palette = ['#0a0a0a', '#06c352', '#e0dfdd', '#fff'];

function ShapeCard() {
  return (
    <div className="relative aspect-square rounded-3xl overflow-hidden bg-[#e0dfdd]">
      {/* 大きな円（左上から） */}
      <div className="absolute -top-12 -left-12 w-48 h-48 rounded-full bg-[#06c352]" />
      {/* 矩形（右下） */}
      <div className="absolute bottom-0 right-0 w-32 h-20 bg-[#0a0a0a]" />
      {/* 小さな円（中央） */}
      <div className="absolute top-1/2 left-1/3 w-12 h-12 rounded-full bg-white -translate-x-1/2 -translate-y-1/2" />
      {/* タイトル */}
      <h3 className="absolute bottom-6 left-6 text-2xl font-bold text-[#0a0a0a]">Shape</h3>
    </div>
  );
}
```

**FAMBOX応用**: ブランドカード・記事サムネ・OGP用画像。軸1の **「整理された散らばり」** トーンに合致。

---

### 4. **Elastic Bars** — マウス追従でSVGバーが弾性変形

**コンセプト**: 縦バーの並び。マウスが近づいた箇所だけ高さが伸び縮みする。

**最小実装**:

```tsx
'use client';
import { useState } from 'react';

function ElasticBars() {
  const [mouseX, setMouseX] = useState(-1000);
  const bars = 40;

  return (
    <svg
      viewBox="0 0 800 200"
      className="w-full h-48 cursor-crosshair"
      onMouseMove={(e) => {
        const r = e.currentTarget.getBoundingClientRect();
        setMouseX(((e.clientX - r.left) / r.width) * 800);
      }}
      onMouseLeave={() => setMouseX(-1000)}
    >
      {Array.from({length: bars}).map((_, i) => {
        const x = (i + 0.5) * (800 / bars);
        const dist = Math.abs(x - mouseX);
        const influence = Math.max(0, 1 - dist / 200);
        const height = 40 + influence * 120;
        return (
          <rect
            key={i}
            x={x - 4}
            y={(200 - height) / 2}
            width={8}
            height={height}
            rx={4}
            fill="#06c352"
            style={{ transition: 'all 0.15s cubic-bezier(.4, 0, .2, 1)' }}
          />
        );
      })}
    </svg>
  );
}
```

**FAMBOX応用**: **軸2 火花** の「次の一歩」表現。カーソルが触れたところがエネルギーで弾む = アスリートの動的感覚を喚起。

---

### 5. **Morph Blob** — Perlin noise でSVGパスが有機的に変形

**コンセプト**: 円が時間と共に有機的に変形し続ける。ホバーでさらに脈動。

**最小実装**:

```tsx
'use client';
import { useEffect, useRef } from 'react';

function MorphBlob() {
  const pathRef = useRef<SVGPathElement>(null);

  useEffect(() => {
    let t = 0;
    let raf: number;
    const points = 8;
    const radius = 80;

    const animate = () => {
      t += 0.01;
      const path: string[] = [];
      for (let i = 0; i < points; i++) {
        const angle = (i / points) * Math.PI * 2;
        // 各ポイントが独立に sin で揺らぐ = 擬似Perlin
        const r = radius + Math.sin(t + i * 1.7) * 12 + Math.cos(t * 0.7 + i) * 8;
        const x = Math.cos(angle) * r;
        const y = Math.sin(angle) * r;
        path.push(`${i === 0 ? 'M' : 'L'}${x.toFixed(2)} ${y.toFixed(2)}`);
      }
      path.push('Z');
      pathRef.current?.setAttribute('d', path.join(' '));
      raf = requestAnimationFrame(animate);
    };
    animate();
    return () => cancelAnimationFrame(raf);
  }, []);

  return (
    <svg viewBox="-120 -120 240 240" className="w-64 h-64">
      <defs>
        <radialGradient id="blobGradient">
          <stop offset="0%" stopColor="#06c352" />
          <stop offset="100%" stopColor="#0a0a0a" />
        </radialGradient>
      </defs>
      <path ref={pathRef} fill="url(#blobGradient)" />
    </svg>
  );
}
```

**FAMBOX応用**: **軸2 発火** の連続性表現。アスリートのエネルギーが内側から脈打つ可視化。診断結果ページのキービジュアル候補。

---

### 6. **Cursor Nav** — フェイクカーソル + 3D展開

**コンセプト**: 偽カーソルが追従し、クリックで3Dナビに展開。「驚き」のインタラクション。

**最小実装（CSS only バージョン）**:

```tsx
'use client';
import { useEffect, useState } from 'react';

function CursorNav() {
  const [pos, setPos] = useState({x: 0, y: 0});
  const [expanded, setExpanded] = useState(false);

  useEffect(() => {
    const onMove = (e: MouseEvent) => setPos({x: e.clientX, y: e.clientY});
    window.addEventListener('mousemove', onMove);
    return () => window.removeEventListener('mousemove', onMove);
  }, []);

  return (
    <>
      <div
        className="fixed pointer-events-none z-50 transition-transform"
        style={{
          transform: `translate(${pos.x}px, ${pos.y}px) scale(${expanded ? 4 : 1})`,
          willChange: 'transform',
        }}
      >
        <div className="-translate-x-1/2 -translate-y-1/2 w-3 h-3 rounded-full bg-[#06c352]
                        shadow-[0_0_20px_rgba(6,195,82,0.6)]" />
      </div>
      <button onClick={() => setExpanded(!expanded)}>Toggle nav</button>
    </>
  );
}
```

**FAMBOX応用**: 診断ウィザード・アスリート向けLPの **「次に動かす」誘導** に使える。

---

## WebGL/R3F が必要な高難度パターン（参考）

### Glass Hero（軸2 Calm Resolve の最有力）

**MeshPhysicalMaterial で IOR + dispersion**：背後のHTMLヒーローセクションを **ガラス越し** に見せ、光を **クロマチック分散** させる。

```tsx
// 概念コード（要 R3F + Three.js）
import { MeshPhysicalMaterial } from 'three';

<mesh>
  <icosahedronGeometry args={[1, 4]} />
  <MeshPhysicalMaterial
    transmission={1}
    ior={1.5}
    thickness={2}
    roughness={0}
    chromaticAberration={0.05}
  />
</mesh>
```

→ Liquid Pipeline の **Phase 120% 超越** で検証する候補。実装は重いが視覚インパクトが圧倒的。

### Particle Phones（軸2 発火 / 粒子飛散）

**Nike Pin の砂塵飛散 = 発火の火種** の WebGL版。スマホシルエットを粒子の集合で再現し、スクロールで集まる/散る。

```tsx
// R3F の Points + ShaderMaterial で実装
<points>
  <bufferGeometry>
    {/* 数千個の頂点 */}
  </bufferGeometry>
  <shaderMaterial
    vertexShader={particleVertex}
    fragmentShader={particleFragment}
  />
</points>
```

→ **軸2 物理的隠喩** のWeb実装決定版。守屋選手企画のキービジュアル候補。

---

## FAMBOX軸 × 即実装マップ（優先順位）

### 軸1（静の信頼）— 即実装候補
| 技法 | 用途 | 実装難度 |
|---|---|---|
| **Pattern Cards** | ブランドカード・記事サムネ | ★ |
| **Shape Cards** | OGP・商品紹介 | ★ |
| **Dot Hover Cards** ⭐⭐ | 食材一覧・診断ステップ | ★ |
| Code Slice Hero（R3F） | デジタル/システム型 ヒーロー | ★★★ |
| Neural Burst | 栄養概念図 | ★★★ |
| Creativity Dial | パラメータ調整UI | ★★ |

### 軸2（動の発火）— 即実装候補
| 技法 | 用途 | 実装難度 |
|---|---|---|
| **Elastic Bars** ⭐ | 「次の一歩」喚起 | ★ |
| **Morph Blob** ⭐ | 内なるエネルギー脈動 | ★★ |
| Particle Phones | 砂塵飛散（軸2 canonical） | ★★★ |
| Shader Cards | 粒子の雨（軸2 発火） | ★★★ |

### 軸3候補（努力の結晶）— 即実装候補
| 技法 | 用途 | 実装難度 |
|---|---|---|
| Glass Hero | 氷的素材・透明感 | ★★★ |
| Shader Cards | 結晶質感 | ★★★ |

### UX技法（軸非依存）
| 技法 | 用途 | 実装難度 |
|---|---|---|
| **Cursor Nav** | カーソル誘導 | ★★ |
| Curtain Sidebar | サイドバー演出 | ★★ |
| Folder Gallery | 画像ギャラリー | ★★ |
| Clay Toggle | フォームUI | ★★ |

---

## 今週から使える 3 つの即実装タスク

### Task 1: FAMBOX 食材グリッドに「Dot Hover Cards」を適用
- **目的**: 食材一覧の視覚インパクトUP（軸1 適用型）
- **工数**: 2-3時間
- **ファイル**: FAMBOX Shopify section（既存 `sections/collection-products.liquid` 等）
- **置換**: `radial-gradient` のドット背景 + ホバーで色変化

### Task 2: 守屋選手企画 LP に「Elastic Bars」をヒーロー下に配置
- **目的**: 「次の一歩」を動的に喚起（軸2 火花）
- **工数**: 1-2時間
- **ファイル**: 新規 React コンポーネント（FAMBOXテーマで使う場合は Liquid+JS で同等実装可）
- **配色**: FAM緑 `#06c352` + 黒背景

### Task 3: 診断ウィザード結果ページに「Morph Blob」配置
- **目的**: アスリートの「内なるエネルギー」可視化（軸2 発火連続性）
- **工数**: 2-3時間
- **ファイル**: 食事診断 Liquid化プロジェクト（[project_fam_diagnosis_liquid](memory)）
- **配色**: グラデーション緑→黒

---

## LPB v4 への組み込み候補

[lpb-human-on-the-loop-roadmap.md](lpb-human-on-the-loop-roadmap.md) のPhase 120% 超越（AI Studio拡張）で：

- **Pattern / Shape Cards** をテンプレートライブラリに追加
- **Morph Blob / Elastic Bars** を「軸2向け推奨アニメ」として登録
- 生成後の品質チェックに **「軸該当性」** 観点を追加（軸1のクールさ / 軸2の躍動感）

---

## デザイン承認パラメータ への追加候補

[design-acceptance-parameters.md](design-acceptance-parameters.md) に **「アニメーション」セクション** を新設する候補：

| 項目 | 合格基準 |
|---|---|
| トランジション速度 | 0.15s / 0.3s / 0.5s / 0.8s のいずれか |
| イージング | `cubic-bezier(.4, 0, .2, 1)` 系（Material・Whitespace 系） |
| `prefers-reduced-motion` 対応 | 必須 |
| `will-change` の使用 | transform / opacity のみ（過剰指定NG） |
| Lottie / GIF 重量 | 1ファイルあたり 300KB 以下 |

---

## 関連
- [[../50_Business_Context/fambox-brand-dna-axes.md]] — 軸1/2/3 視覚言語
- [[design-acceptance-parameters.md]] — ガードレール仕様
- [[lpb-human-on-the-loop-roadmap.md]] — Liquid Pipeline ロードマップ
- [[../45_Design_Refs/_index.md]] — 視覚リファレンス全体
- 元サイト: https://experiments.thisiswhitespace.com/
- Whitespace Studio: https://thisiswhitespace.com

## 元情報
- URL: https://experiments.thisiswhitespace.com/
- 確認日: 2026-05-20
- 実験件数: 23
- 採用技術: Next.js + Tailwind v4 + Framer Motion + React Three Fiber + GLSL Shader
