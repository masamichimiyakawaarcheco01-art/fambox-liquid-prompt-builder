# sporty — Figma ビルドレシピ

> [SYSTEM.md](SYSTEM.md) を Figma に落とす手順。figma-bridge で構造7割を組む。
> **レイヤー命名は [LAYER-NAMING.md](../../LAYER-NAMING.md) v1.0 準拠**（v2 ビルドから適用。
> v1 フレーム `138:100` は規則制定前のため未準拠。命名規則 §6 に本フレームの準拠版ツリー例あり）。

## 題材（参照と別物）
**STRIDE — ランニングクラブ** LP 上部1画面。
- Hero: フルブリード写真プレースホルダ（ダーク）＋ Display「RUN THE CITY.」＋ accent 色帯横断 ＋ 白ピルCTA
- 統計3カード: 12K+ members / 48 weekly sessions / 92% goal completion
- 写真3カード: グレーボックス（±回転は人間仕上げ）

## SYSTEM.md からの適用値
- bg #FFFFFF / surface #F4F5F6 / ink #0E0E12 / ink-muted #8A8A90 / **accent #FF4D1F** / line #ECECEE
- Display 88/800 uppercase 行間1.0 ／ H1(数値) 56/800 ／ Body 14 ／ Small 11/600 uppercase
- ヒーロー=フルブリード(マージン0) ／ 本文=外マージン80 ／ 余白 S16 M32 L64 ／ カード角丸20

## figma-bridge 構築手順
1. `join_channel`（接続確認）
2. ページ: `create_frame` W1440, VERTICAL, padding 0, spacing 0, fill #FFFFFF, HUG
3. **Hero**（`create_frame` W1440 H620, layoutMode **NONE**＝絶対配置, fill #1A1A1D ←写真プレースホルダ兼用）
   - 色帯: `create_rectangle` W1440 H96 @(0,400), fill accent #FF4D1F
   - eyebrow: `create_text` "STRIDE RUNNING CLUB" 11/600 white @(80,120)
   - Display: `create_text` "RUN THE\nCITY." 88/800 white @(80,160)
   - CTA: `create_frame` pill（HORIZONTAL, padding 24x14, radius 999, fill #FFF）@(80,520) → 内 text "Join the club ↗" 14/600 ink
4. **本文セクション**（`create_frame` VERTICAL, padding 80, spacing 64, fill #FFF, HUG）
   - 統計行: HORIZONTAL spacing 24 → 統計カード×3（VERTICAL, surface, radius 20, padding 32, spacing 8: 数値 56/800 ink ＋ ラベル 11/600 muted uppercase）
   - 写真行: HORIZONTAL spacing 24 → `create_rectangle` 410×280 radius 20 fill line ×3
5. `export_node_as_image` → Read 目視 → canvas の孤児ゴミ確認（学び3）
6. 結果を「## 構築ログ」に追記

## 人間仕上げ（3割）— sporty は corporate より仕上げ依存が大きい
- **写真差込が最重要**: ヒーローのダーク面 → モーションブラーのアクション写真。深度（Display の一部を被写体の奥へ）は写真合成時にマスクで実現
- 写真3カードに実画像 ＋ **±3〜6° 回転**（bridge に rotate なし）
- デュオトーン処理（accent 反転）
- letter-spacing .1em（bridge 指定不可）／ フォントのコンデンス化

## 構築ログ

### v1（2026-06-10 / channel 6ccjwqtf / 純構築 5分59秒・自己修正2回込み）
- ページ: `138:100` sporty-stride（VERTICAL, HUG）
- Hero: `138:101`（NONE=絶対配置, ダーク写真プレースホルダ兼用）/ 帯 `138:102` / Display `138:104` / CTA `138:105`
- 本文: `138:107`（VERTICAL padding 80）/ 統計行 `138:108`（カード 109/112/115）/ 写真行 `138:118`（119/120/121）
- **学び4**: 兄弟ノードの z-order は**作成順**で固定（`move_node` で重ねても変わらない）。帯→文字の順に作ったため文字が帯の奥へ — 結果的に NIKE 型深度になったが、前後関係は作成順で設計するのが正攻法
- **学び5**: 統計カードを `layoutSizingVertical: HUG` で作成 → corporate v1 の固定高さ余白ムラ問題が再発せず（critique 5観点 2/2）。**カード類は常に HUG** をレシピ標準にする
- **学び6**: 絶対配置（layoutMode NONE）のヒーローは要素間隔の検算が必要（band y400 / CTA y520 など手計算）。auto-layout 区画より調整コストが高く、純構築時間 +1分44秒の主因
- export: PNG scale 0.5 で2回目視（修正→再export）。ID 採番 138:100〜121 連番＝孤児なし（学び3 の検算）
