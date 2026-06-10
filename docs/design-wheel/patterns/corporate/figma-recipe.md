# corporate — Figma ビルドレシピ

> [SYSTEM.md](SYSTEM.md) を Figma に落とす手順。figma-bridge で構造7割を組む。
> フォントは Inter 固定（bridge 制約 / [[feedback_figma_bridge_text_limitations]]）→ 人間が3割仕上げ。

## 題材（参照と別物）
**FlowOps — 業務オートメーション基盤**（架空 B2B SaaS）の LP 上部1画面。
- Hero: 番号なし大見出し「Automate the busywork.」＋サブ＋ピルCTA「Start free ↗」＋円形マスク画像枠（右）
- 特徴3カード: 01 Connect / 02 Automate / 03 Observe（番号ラベル + 見出し + 小本文）

## SYSTEM.md からの適用値（Light モード）
- bg #F4F5F6 / surface #FFFFFF / ink #111114 / ink-muted #8A8A90 / accent #E8431F / line #ECECEE
- グリッド 12col / ガター 24 / 外マージン 80 / 余白 S16 M32 L64
- Display 64/700 行間1.05 ／ H3 18/600 ／ Body 14/400 行間1.6 ／ Small 11/500 uppercase
- カード角丸16 影なし ／ pill 角丸999 ink塗り ／ 円形マスク50%

## figma-bridge 構築手順
1. `join_channel`（接続確認。切れていたら再 Connect）
2. `create_frame` Page: W1440 H900, fill #F4F5F6（bg）, name "corporate-flowops"
3. **Hero frame**（W1280, 中央寄せ, x80 y80）
   - `set_layout_mode` HORIZONTAL, `set_item_spacing` 32, `set_padding` 0
   - 左 text block（垂直 auto-layout, item_spacing 24）:
     - `create_text` "PLATFORM" → Small 11/uppercase, fill ink-muted
     - `create_text` "Automate the busywork." → Display 64/700, fill ink, 行間1.05
     - `create_text` サブ1行 → Body 14, fill ink-muted
     - pill CTA: `create_frame` auto-layout HORIZONTAL, padding 16x12, `set_corner_radius` 999, fill ink #111114 → 内 `create_text` "Start free ↗" Body14 fill #FFF
   - 右 `create_rectangle` 円形画像枠 W520 H520, `set_corner_radius` 260, fill line #ECECEE（グレーボックス＝後で実画像）
4. **特徴3カード row**（Hero 下 y+64, W1280 横 auto-layout, item_spacing 24）
   - 各カード `create_frame` 垂直 auto-layout, W408, padding 32, `set_corner_radius` 16, fill surface #FFFFFF, 細 stroke line #ECECEE:
     - `create_text` "01"/"02"/"03" → Small 11 fill accent #E8431F
     - `create_text` 見出し(Connect/Automate/Observe) → H3 18/600 fill ink
     - `create_text` 小本文2行 → Body 14 fill ink-muted 行間1.6
5. `export_node_as_image` でページフレームを書き出し → Read で目視確認
6. 実ノードIDと結果メモを本ファイル末尾「## 構築ログ」に追記

## 人間仕上げ（3割）
- フォントを SYSTEM.md 指定（Inter→ 必要なら Helvetica系 / 日本語 Noto Sans JP）へ差替
- 円形グレーボックス → 実画像（プロダクトUI / 抽象3Dなど）差込
- accent の最終トーン微調整

## 構築ログ

### v1（2026-06-10 / channel 6ccjwqtf / 純構築 4分15秒）
- ページ: `137:77` corporate-flowops（VERTICAL, padding 80, spacing 64, HUG）
- Hero: `137:79`（HORIZONTAL spacing 32）/ 左コピー `137:80` / CTA `137:84` / 円形枠 `137:86`
- カード行: `137:87` / card-01 `137:88` / card-02 `137:92` / card-03 `137:96`
- **学び1**: `create_frame` の `layoutSizingHorizontal: FILL` は親が auto-layout でも作成時指定だとエラー → 固定 W で作成すれば OK（FILL は作成後に set する必要あり）
- **学び2**: カードは固定 H220 で作ったため本文下に余白ムラ → 次回は `layoutSizingVertical: HUG`（critique v1 の減点要因）
- **学び3**: `create_frame` がエラーを返しても**フレーム本体が孤児として canvas 直下に残る**ことがある（白 1280×520 が canvas (0,0) に残り Hero を覆い隠した / 137:78）。エラー発生時は ID 採番の欠番を確認し `get_node_info` → `delete_node` で掃除する。**構築完了後は export 目視だけでなく canvas 全体のゴミ確認も必須**（export は対象フレームしか写らないため孤児を検出できない）
- export: PNG scale 0.75 で目視確認済み（採点 11/12 → critique-log.md）
