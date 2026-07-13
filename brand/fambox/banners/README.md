# FAMBOX バナーキット

> 非デザイナー（マレル）が Instagram / TikTok / YouTube / Blog 用バナーを
> 効率的に・ブランド統一で作るためのキット。最終仕上げは **Canva**。

## ⭐ 方式：HTML キャプチャ（Canva 再現はしない）

**Canva/Figma で再現すると「翻訳ロス」で品質が落ちる**（2026-06-18 確認）。
Claude が作る完成形 HTML を**そのまま画像書き出し**するのが最高品質・最速。

```
Claude が HTML を生成/編集  →  capture.sh で正確サイズ PNG 書き出し  →  完成
```

- `banner-export.html` — 1枚=1バナーのパラメトリック雛形（`?ar=1x1` 等でサイズ切替・`?head=...|...` で文言）
- `capture.sh` — Chrome ヘッドレスで **Retina ×2** 書き出し（**インストール不要**）
  - `./capture.sh` で5サイズ一括 / `./capture.sh 1x1` で個別 → `out/banner-<ar>@2x.png`
- 文言変更は URL パラメータ or HTML 直編集 → 再キャプチャ（秒）。**ブランド値は CSS で固定＝ズレない**。
- マレル運用: 「見出しを○○に」とチャット → Claude が雛形を編集 → capture → 完成。Canva 不要。

## 効率化の考え方
4プラットフォーム = **5アスペクト比**に集約。1レシピを5サイズに展開する。

| 比率 | 実寸 px | プラットフォーム |
|---|---|---|
| 1:1 | 1080×1080 | Instagram フィード |
| 4:5 | 1080×1350 | Instagram 縦長フィード |
| 9:16 | 1080×1920 | **TikTok** / IG ストーリー・リール |
| 16:9 | 1280×720 | **YouTube** サムネ |
| 1.91:1 | 1200×630 | **Blog** OGP / SNSシェア |

## ブランド値（Canva Brand Kit に1回だけ登録）
出典: `brand/fambox/design-system/tokens/`（colors.md / typography.md）

| 項目 | 値 |
|---|---|
| Drive Orange（主役/CTA） | `#FB4C15` |
| Drive Light（アクセント文字） | `#FC825B` |
| Deep Blue（地・信頼） | `#0F2A5C` |
| Sky Blue（情報/データ） | `#3DB8E8` |
| Ink（本文） | `#1B1D1A` |
| 英数字フォント | **Poppins**（500/600/700/800） |
| 日本語フォント | **Hiragino Sans**（W3/W4/W6） |

## レシピ（v0 = 「見出し型」1種）
- 地: Deep Blue ＋ 右上に Drive Orange の radial グロー
- 上: eyebrow（英・Drive Light）＋ FAMBOX ロゴ
- 中: 見出し（Hiragino 太・一部を Drive Light で強調）
- 下: Drive Orange の pill CTA ＋ URL
- プロト= `banner-kit-v0.html`（5サイズ実寸の縮小プレビュー）

## 差し替え部分（マレルが変える箇所だけ）
1. eyebrow 文言　2. 見出し（＋強調語）　3. CTA 文言　4. 背景写真（任意）

## 今後の拡張候補
- レシピ追加: ②ブログ記事カバー型　③商品/キャンペーン型　④実績/数値型
- 写真差し込みパターン（デュオトーン処理）
- Canva テンプレ化（ブランドキット登録 → このレシピを1回組む → 複製運用）

## ステータス
v0 = 見出し型 × 5サイズを実機確認（FAMBOX ブランド準拠）。レシピ拡張・Canva 連携は次段階。
