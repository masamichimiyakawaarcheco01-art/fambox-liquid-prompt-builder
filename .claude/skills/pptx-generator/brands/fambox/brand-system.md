# FAM BOX — Brand System

> 出典：FAMBOX Brand DNA v1.0（`brand/fambox/brand-dna/current.md`）

---

## デザイン哲学

### コア原則（4つ）

1. **Editorial × Lab**
   - Editorial：丁寧に編集された情報の信頼感
   - Lab：科学的な検証性、データに基づく語り
   - 両者を二軸として常に意識する

2. **Light over Dark**
   - 基本は白背景・濃ダーク文字
   - 「健康」「清潔」「信頼」の世界観を維持
   - ダーク使用は意図的な強調のみ（ヒーロー深部・主訴求 CTA 周辺）

3. **Restraint over Flash**
   - 派手なエフェクト・グラデ・ノイズは避ける
   - 落ち着いた色使い、控えめなシャドウ
   - 「派手で目を引く」ではなく「信頼できて読みやすい」

4. **Numbers over Adjectives**
   - 「最高」より「13チーム / 130名」
   - 「すごい」より「30% 改善」
   - 形容詞より数値で語る

---

## カラーシステム

### Brand カラー

| 色 | HEX | 役割 |
|---|---|---|
| **Drive Orange** | `#FB4C15` | Primary。CTA・達成値・推進表現 |
| Drive Light | `#FC825B` | ホバー・ハイライト |
| **Sky Blue** | `#3DB8E8` | Secondary A。データ可視化・情報カテゴリ |
| **Deep Blue** | `#0F2A5C` | Secondary B。ヒーロー深部・信頼領域 |

### 使用ルール

- **Drive Orange を最優先**：CTA・主訴求は必ず Drive
- **Sky / Deep Blue で信頼領域を作る**
- **純緑・純赤は使わない**（Drive と色相衝突を回避）

### Text Grayscale

| 段階 | HEX | 用途 |
|---|---|---|
| Ink | `#1B1D1A` | 本文・見出し |
| Sub | `#545655` | サブテキスト |
| Caption | `#888888` | キャプション |
| Placeholder | `#D0D0D0` | プレースホルダ |
| White | `#FFFFFF` | 白 |

### Background

| 役割 | HEX |
|---|---|
| Primary | `#FFFFFF` |
| Secondary | `#FAFAFA` |
| Tertiary | `#F3F3F3` |

### Semantic（状態色）

| 役割 | HEX | 選定理由 |
|---|---|---|
| Success | `#10B981` | Sky Blue 調和、純緑より洗練 |
| Warning | `#F59E0B` | Drive Orange と色相距離を確保 |
| Error | `#DC2626` | Drive Orange との混同回避、深赤で識別性 |
| Info | `#3DB8E8` | Sky Blue 兼用 |

---

## タイポグラフィ

### Web/UI（参考。PPT 以外）

- 英字：**Poppins**（heading） + Poppins / Inter（body）
- 和字：**Hiragino Kaku Gothic Pro**（heading / body 両方）

### PPT / Keynote / Word 等の資料

- **Yu Gothic UI** 統一（`feedback_document_font` 規律）
- 理由：Windows / Mac / Office 環境で安定して描画される唯一の選択肢
- 欧文混じり：Yu Gothic UI（自動的に Latin はシステム代替）

### ウェイト・サイズの方針

- 見出し：太め（Bold / SemiBold）
- 本文：Regular
- ジャンプ率（H1 vs body）は **中〜大**（Editorial 寄り）

---

## レイアウト原則

### 平面構成

- 整数比（1:1, 1:2, 2:3 等）で構造化
- 余白は等比率（1.5x / 2x）で S/M/L を定義
- 等差スペーシングは避ける

### キャラクターライン

- コンテナ境界とオブジェクト整列で視覚構造を作る
- 行頭・余白の揃えを徹底
- 「揃ってるか」を最優先（派手なレイアウトより重要）

### ヒエラルキー

- ジャンプ率でヒエラルキーを作る
- 大きさ・太さ・色の3軸で区別（色は最小限）
- 「3 階層まで」を目安（深くしすぎない）

---

## 写真・画像のガイド

### 推奨

- **アスリート・チームの実写**（許諾済）
- **食事・献立の俯瞰写真**（自然光、過度な彩度調整なし）
- **栄養成分・データのグラフ**（控えめなアクセント色）

### 避ける

- ストックフォト感の強い「いかにも」な笑顔写真
- 過度に編集された SNS 風の写真（彩度爆上げ）
- スポ根・根性論的なイメージ写真
- 競合の写真の使用

---

## エフェクト・モーション

### 推奨

- 控えめなシャドウ（card など）
- フェード・スライド程度のシンプルなトランジション
- 1〜3 段階のスクロールリビール

### 避ける（[feedback_fambox_visual_effects](../../../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_fambox_visual_effects.md)）

- 輪郭歪み・noise-bloom・グリッチ
- 派手な3D 回転・パララックス
- 過度なグラデーション
- ネオングロー・サイバー感

---

## シグネチャー要素

FAMBOX らしい視覚的シグネチャー：

- **Drive Orange のアクセント**（CTA・矢印・強調記号）
- **白背景 + 黒文字** のクラシックな読みやすさ
- **データ可視化**（バーチャート・比較表）への適度な依存
- **第三者の声**（選手・監督・専門家）を引用枠で見せる
- **数値ファースト**の主訴求

---

## NG事例（具体）

| NG | なぜ |
|---|---|
| ネオングリーンのアクセント | Drive Orange と衝突、純緑禁止 |
| ダーク背景 + ネオン文字 | FAMBOX の信頼トーンと逆 |
| 「業界 No.1」と書く | 根拠なき superlative |
| ストックフォトのスマイル | アスリート世界観と乖離 |
| 「今すぐ申し込み！」CTA | 押し売り表現 |
| 4階層以上のヒエラルキー | 視認性低下 |

---

## 参照

- [FAMBOX Brand DNA v1.0](../../../../../brand/fambox/brand-dna/current.md)
- [Color Tokens](../../../../../brand/fambox/design-system/tokens/colors.md)
- [bugs.md（28 規律）](../../../../../brand/fambox/design-system/bugs.md)
- [FAMBOX Project CLAUDE.md](../../../../../brand/fambox/CLAUDE.md)
- [FAMBOX Visual Effects 避けるべき技法](../../../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/feedback_fambox_visual_effects.md)
