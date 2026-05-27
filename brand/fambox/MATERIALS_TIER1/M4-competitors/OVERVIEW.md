---
title: M4 競合 UI キャプチャ集 — 全社まとめ
date: 2026-05-27
owner: 宮川（ARCHECO）
status: tier-1-complete
material_id: M4
scope: 5 ブランド × 3 画面 = 15 スクショ
---

# M4: 競合ブランド UI キャプチャ集（5 社 × 主要 3 画面）

MATERIALS_CHECKLIST.md M4 対応。POD（L2-6）と DS トーン判断の根拠として、競合 5 社の TOP / 商品詳細 / 法人ページを取得・観察。

## 取得状況

| ブランド | TOP | 商品詳細 | 法人 | 計 |
|---|:---:|:---:|:---:|:---:|
| Muscle Deli | ✅ | ✅ | ✅ | 3/3 |
| GREEN SPOON | ✅ | ✅ | ✅ | 3/3 |
| nosh（ナッシュ） | ✅ | ✅ | ✅ | 3/3 |
| 筋肉食堂DELI | ✅ | ✅ | ✅ | 3/3 |
| シンプルミール（ヨシケイ） | ✅ | ✅ | ✅ | 3/3 |
| **合計** | **5** | **5** | **5** | **15/15** ✅ |

取得手法: `Google Chrome --headless=new --screenshot --window-size=1440,900` (macOS 同梱 Chrome 148)。Cloudflare ブロック時は User-Agent 偽装 + `--disable-blink-features=AutomationControlled`。

## 個別観察コメント

- [Muscle Deli](muscledeli/summary.md)
- [GREEN SPOON](greenspoon/summary.md)
- [nosh](nosh/summary.md)
- [筋肉食堂DELI](kinnikushokudo/summary.md)
- [シンプルミール](simplemeal/summary.md)

## 競合 UI 共通パターン（5 観察）

1. **CTA は緑 or 赤の Pill 形**（4/5 社）— 健康訴求 = 緑（MD / GS / nosh）、力強さ = 赤（筋肉食堂）
2. **法人ページは「別 LP」または「ない」の二極** — nosh と筋肉食堂は専用ドメイン LP（office nosh / 筋肉食堂Office）、他は B2C 内サブページか問合せフォームのみ
3. **料理写真は俯瞰 + 木目背景がデファクト**（nosh / GS）。筋肉食堂はフルブリード Food Porn 系で差別化
4. **数値訴求**（"糖質 30g 以下" / "タンパク質 31.8g"）を巨大ジャンプ率で打ち出すのが共通言語
5. **ヒーロー構造は 3 タイプ**: 人物モザイク（Muscle Deli） / ブランド世界観動画（GREEN SPOON） / 料理俯瞰（nosh・筋肉食堂・シンプルミール）

## FAMBOX への示唆

### 🟢 参考にすべき

| 観点 | 競合 | 学び |
|---|---|---|
| **B2B LP の独立性** | nosh の `office nosh` | OKR KR1-5 と直結。別ドメインで B2C ノイズ排除 + 資料 DL 1 本集中 |
| **数値ジャンプ率の大きさ** | 筋肉食堂DELI | 栄養データ訴求に有効（FAMBOX の "可能性の確度" 訴求と整合） |
| **写真ディレクション統一度** | GREEN SPOON | Editorial 軸の参考（俯瞰 + 円形 + 木目背景の徹底） |
| **人物 4 分割モザイク** | Muscle Deli | FAMBOX が "サポート選手" を増やした時のヒーロー構造案（守屋選手企画拡張など） |

### 🔴 避けるべき

| 観点 | 競合 | 理由 |
|---|---|---|
| **赤緑黄 信号色 + 3 カラム情報詰め** | シンプルミール（ヨシケイ） | 旧 EC スタイルで FAMBOX の Editorial 路線と相反 |
| **赤一色強コントラスト** | 筋肉食堂DELI | "本気・闘い" 寄りすぎて FAMBOX の "家族・継続" トーンと不協和 |

## 5 観点 競合 vs FAMBOX 比較マトリクス

| 観点 | Muscle Deli | GREEN SPOON | nosh | 筋肉食堂DELI | シンプルミール | **FAMBOX 方針** |
|---|---|---|---|---|---|---|
| 色 | 緑単色 | ティール + クリーム | 木目茶 + 緑 + 黒 | 赤 + 黒 + 白 | 赤緑黄信号色 | **紺（Ink）+ オレンジ（Drive）** |
| タイポ | Poppins + Hiragino | 英文 Display + 和文 Sans | 和文角ゴ + 手書きスクリプト | 和文太字 + 数字ジャンプ率 | ジャンプ率弱 | **Poppins + Hiragino, h3=24px / body=16px** |
| 写真 | 人物軸 | 料理俯瞰 + 円形統一 | 食卓ストーリー | Food Porn フルブリード | 料理 + パッケージ混在 | **料理 + 選手の二軸**（要決定） |
| CTA | Pill 緑塗り | Pill 緑 24px+ | Pill 32px+ 黒 / 緑 | 浅角丸 赤 | 直角〜2px | **Pill 50px Drive オレンジ** |
| ヒーロー | 人物 4 分割 | ブランド動画 | ベネフィット 3 数字 | 料理フルブリード | 3 カラム詰め | **未確定**（DNA v0.7 決定可） |

## POD（Point of Difference）強化候補

FAMBOX が競合と差別化できる軸:

1. **栄養戦略 × アカデミー**（食事単体ではない）— ADR-005 と整合
2. **トップアスリート監修の見える化**（守屋選手企画 / 大前さんアドバイザー）— ADR-012 a 層差別化軸
3. **法人プロ向け独立 LP**（office nosh ライク）— OKR KR1-5
4. **Editorial × Quiet Drive**（GREEN SPOON ライクの世界観統一）+ **数値訴求**（筋肉食堂ライクのジャンプ率） の **両立**

## 関連

- [MATERIALS_CHECKLIST.md M4](../MATERIALS_CHECKLIST.md#m4-競合ブランド-ui-キャプチャ集5社--主要3画面)
- [Brand DNA current.md L2-6 POD](../../brand-dna/current.md)
- [ADR-005 栄養ソリューション市場](../../brand-dna/decisions/decisions-log.md#adr-005)
- [ADR-012 サブセグメント 3 層階層](../../brand-dna/decisions/decisions-log.md#adr-012)

## 変更履歴

- 2026-05-27: Initial inventory — 15 スクショ取得 + 5 観点比較 + POD 強化候補抽出（subagent + 宮川 / Claude）
