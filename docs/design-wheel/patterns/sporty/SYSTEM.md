# sporty — SYSTEM.md (v1)

> 真ソース。figma-bridge / HTML はこのファイルを読んで構築する。
> **v1 改訂（2026-06-18）**: ユーザー提供 refs（Nike Run+ / PLAYPAD / NestEgg）により
> sporty に**2つの sub-style** があると判明。詳細な抽出根拠は [REF-EXTRACTION-v1.md](REF-EXTRACTION-v1.md)。

## 0. 2つの sub-style（必ず最初に選ぶ）

sporty は「運動量の説得」だが、その表現に2系統ある。**題材で必ずどちらかを選ぶ**。

| sub-style | 一言 | 使う場面 | 代表 ref |
|---|---|---|---|
| **A. product-UI**（推奨デフォルト）| ダーク×電光アクセント×データ可視化で**精度・先端**を説得 | アプリ/SaaS/会員制/EC/ダッシュボード LP | Nike Run+ / PLAYPAD / NestEgg |
| **B. poster**（写真主役）| アクション写真＋深度＋デュオトーンで**熱量**を説得 | キャンペーン/ブランド/イベント LP | TENISTA / NIKE GUANGZHOU / Nike First Step |

> ⚠️ 混ぜない。product-UI に grain/斜め/回転/グランジを足すと**雑に見える**（v1/v2 の失敗）。
> poster に整然カード/データ可視化を足すと熱量が死ぬ。

---

# sub-style A: product-UI 🔒（v3 で実証・凍結）

> プロト= `prototypes/pulse-v3.html`。Nike Run Club 級の洗練が目標。

## A-1. Color
| 役割 | 値 | 用途 |
|---|---|---|
| bg | #0A0C0B | 近黒（純黒でなく僅かに緑寄り） |
| surface | #14171A | カード面 |
| surface-2 | #1C2024 | 入れ子の面・チップ |
| line | #272C30 | 罫線・カード境界 1px |
| ink | #FFFFFF | 主テキスト |
| muted | #8C949C | 副テキスト・ラベル |
| **accent** | **#C6FF3A（volt）** | 電光色。CTA・データ・1ハイライト。**この色が product-UI の signature**（orange/blue より「アプリらしさ」が出る） |

- グロー= `radial-gradient(circle, rgba(198,255,58,.22), transparent 62%)` を hero/CTA 背面に。**grain は使わない**。

## A-2. Type
- **見出し**: Space Grotesk 700（幾何 grotesk・letter-spacing -.03em・line-height 1.02）
- **本文**: Inter 400–500
- **数字**: Space Grotesk 700。2桁目を accent 着色（例 24<accent>/7</accent>）
- アウトライン見出し（`-webkit-text-stroke:1.5px accent` + transparent）を1語だけ効かせる
- コンデンス grunge（Anton 等）は **使わない**

## A-3. Layout
- max-width 1200px / 外パディング 32px
- hero= 1.15 : 0.85 の2カラム（左コピー / 右データカード）
- カードグリッド= 整然と 3列 or 4列。**回転・斜め・グリッド破りは禁止**
- 余白= セクション L80px / グループ内 tight

## A-4. Components（データ可視化が主役 UI）
| 要素 | 仕様 |
|---|---|
| データカード | surface グラデ・角丸28・1px line。リング＋スタッツ＋チップ＋ミニバー |
| プログレスリング | SVG・stroke 12・accent・stroke-linecap round。中央に %とラベル |
| ミニバーチャート | flex 末尾整列・1本だけ accent(.hot)・他は surface-2 |
| ステータスチップ | 角丸999・選択中は accent 塗り |
| スタッツタイル | surface カード・特大数字・2桁目 accent |
| 機能カード | 角丸20・1px line・hover で border を accent 化・line アイコン(stroke accent) |
| ボタン | pill。primary=accent 塗り/暗文字、ghost=surface-2＋line |

## A-5. Motion
- 0.2s cubic-bezier(.16,1,.3,1)。hover= translateY(-2〜4px)。数字はカウントアップ可。

---

# sub-style B: poster（写真主役）

> プロト= `prototypes/pulse-retest.html` / `_sample-stride-LP.html`。**写真必須**。

## B-1. Color
| 役割 | 値 | 用途 |
|---|---|---|
| bg | #FFFFFF | 写真を立たせる白（または #0B0B0E 黒） |
| surface | #F2F3F4 | カード/面 |
| ink | #0B0B0E | 見出し・主テキスト |
| muted | #86868C | 副テキスト |
| accent | #FF3B14（energy）or #2E6BE6（court）| **1作品1色のみ**。色帯・CTA・数値 |
| line | #E6E6E8 | 罫線・グリッド下地 |

## B-2. Type
- Display: **コンデンス grotesk**（無料は Oswald 多ウェイト / Barlow Condensed / Bebas Neue）。Anton は1ウェイトで体系が組めず非推奨
- ALL CAPS・letter-spacing -.02〜-.04em・行間 0.86–1.0
- 深度規則: Display を写真と前後に重ねる（被写体の奥に潜らせる）

## B-3. Layout
- ヒーロー= フルブリード写真。本文= 外マージン 56–80px
- **タイトクロップ**: 全身でなく動作の一部（手/筋肉/踏み込み）を寄りで断つ
- 動勢: 写真カード ±3〜6° 回転・斜め color帯・誌面型1大2小の非対称

## B-4. Components
- pill ボタン / 統計カード（特大数値）/ accent 色帯横断 / 番号バッジ #01 / アウトライン番号 / グリッド下地
- **デュオトーン**: `filter: grayscale(.4-.5) brightness(.4-.6) contrast(1.1)` + accent overlay（大面積 accent の唯一の例外）

## B-5. Motion
- 0.2s cubic-bezier(.16,1,.3,1)。写真カード hover で回転 0° 戻し。

---

## 共通 DO / DON'T
- ✅ DO: 最初に sub-style を選ぶ／accent は1色を画面内3〜4回まで／余白の緩急で premium。
- ❌ DON'T: 2 sub-style の語彙を混ぜる／accent 多色／product-UI に grain・斜め・グランジ／poster で写真を小さく置く。

## 昇格ステータス
- product-UI（A）: v3 で実機確認・高評価方向。**写真不要で完結**＝非デザイナー運用に最適。
- poster（B）: 写真ありで Hero 良好（再テスト合格）。写真調達が前提。
- 推奨チャネル: 両 sub-style とも **HTML 優位**（データ可視化・深度・デュオトーンが AI 側で完結）。
