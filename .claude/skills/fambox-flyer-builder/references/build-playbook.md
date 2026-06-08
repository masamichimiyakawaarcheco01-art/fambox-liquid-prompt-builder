# Figma 構築プレイブック（FAM BOX 印刷物）

Figma 上で印刷物を組む際の手続き知見と既知の罠。実機検証で確立済。

## 目次
1. 接続（figma-bridge / 公式 Figma MCP）
2. フォントの壁と代替
3. 写真・QR を入れる（upload_assets）
4. 箱(auto-layout)の組み方
5. 背景バンドの作り方
6. 既知の罠
7. 自己検証チェックリスト

---

## 1. 接続

- **figma-bridge**（Cursor Talk To Figma Plugin）：構造を直接組む。socket は `bunx cursor-talk-to-figma-socket` を background 起動して代行可。プラグインで Connect→チャンネルID→`join_channel`。切れたら再 Connect→新ID で join。
- **公式 Figma MCP（use_figma）**：fileKey 必須（URL から抽出）。JS で fontName/サイズ/色/塗り変更・`get_screenshot`・`upload_assets` が可能。**フォント名指定・写真配置・スクショ検証はこちら**。
- 使い分け：素早い構造＝figma-bridge、フォント/写真/検証＝use_figma。両方同じデスクトップファイルを編集できる。

## 2. フォントの壁と代替（重要）

- **figma-bridge の create_text は fontFamily 指定不可**（全て Inter）。
- **公式 MCP 実行環境に Hiragino / F910-Shin-comic-tai / YuMincho が未インストール** → `loadFontAsync` 失敗。使えるのは **Poppins / Noto Sans JP** 等の Google 系のみ。
- **対応**：構築時は 日本語=Noto Sans JP、英字=Poppins で組む（行間/サイズ/階層は正しく当てる）。**ブランド日本語フォント（Hiragino/F910/YuMincho）の適用は宮川さんの Mac 上 Figma で1クリック差し替え**＝人間仕上げ。
- テキスト変更（characters/fontSize/fontName/letterSpacing/lineHeight）は**対象ノードの現フォントを loadFontAsync 済**が前提。未ロードだとエラー（スクリプトは原子的＝未適用）。冒頭で必要フォントを全 load。

## 3. 写真・QR を入れる（upload_assets）

写真は人間専用ではない。配置可能：

1. `upload_assets(fileKey, nodeId, scaleMode)` で single-use URL 取得（scaleMode: FILL/CROP/FIT）。
2. `curl -X POST -F "file=@path.png;type=image/png" "<submitUrl>"` で POST → imageHash と placedOnNodeId が返る。
3. **placedOnNodeId が返らない場合**（小さい枠で起きがち）は、返った imageHash を使って use_figma で明示設定：`node.fills=[{type:"IMAGE",imageHash:"<hash>",scaleMode:"FILL"}]`。
4. 対応形式 PNG/JPG/GIF/WebP・10MB まで。**SVG 不可**（ロゴ SVG は別途）。
5. **QR は公開 API で生成**して配置可：`curl "https://api.qrserver.com/v1/create-qr-code/?size=600x600&margin=8&data=<URL>" -o qr.png` → upload。URL は表示テキストと一致させ、印刷前に最終URLを確認（暫定なら明記）。
6. 素材在庫例：`/Users/archecoinc./Desktop/Claude_1/Asset/`（Mask group.png=大前+和田、【明治】大前写真.png、Wada_01.png 等）。内容不明な多数画像は PIL でコンタクトシート化して Read すると効率的。
7. **写真が無い枠はグレーボックスのまま**（無理に合成しない）。

## 4. 箱(auto-layout)の組み方

- セクション＝箱。`figma.createFrame()` → **resize(w,10) を先に** → その後 `layoutMode/primaryAxisSizingMode/counterAxisSizingMode` を設定（順序重要、下記の罠参照）。
- パディング 32 基準、`itemSpacing` は 8系（8/16/24）。
- 本文テキストは箱幅に合わせ自動折返し：append 後に `layoutSizingHorizontal="FILL"` + `textAutoResize="HEIGHT"`。手動改行に頼らない。
- 等幅カラム（3点/2本柱）：横 auto-layout に子を append → 各子 `layoutSizingHorizontal="FILL"`。
- 全面バンド（full-bleed）と padding 付き本文が混在する版は、**背景は絶対配置の矩形、本文は x32 で上に乗せる**方式が確実（auto-layout の padding と全面ベタは両立しにくい）。

## 5. 背景バンドの作り方

- ルート frame は `layoutMode=NONE`・`clipsContent=true`。
- バンド＝全幅矩形を**先に**（背後に）作る：橙(Hero)/Ink濃/淡グラデ/Deep Blue/白。`insertChild(0, rect)` で最背面。
- 淡グラデ：`fills=[{type:"GRADIENT_LINEAR", gradientTransform:[[0,1,0],[-1,0,1]], gradientStops:[{position:0,color:{r:.99,g:.99,b:.99,a:1}},{position:1,color:{r:.94,g:.94,b:.94,a:1}}]}]`（縦・微）。
- 図版は**境界をまたぐブリッジ**で奥行き（バンド作成後に上へ）。ただし Hero 本文と重ねない（サブコピー被り注意）。

## 6. 既知の罠

- **resize() は sizing mode を FIXED に戻す**。auto-layout の AUTO(hug) は **resize の後に再設定**。順序を誤ると高さ10pxで固定され子が clip されて消える。
- **子座標はフレーム相対**（親内 0 始まり）。`parent.x` を足すと3万px飛ぶ。
- **created ≠ visible**：API 戻り値でなく必ずスクショで終える。
- **export/focus 系は接続が新鮮な時のみ成功**、再接続直後に。create/set は安定。
- **テキスト見切れ**：HUG 幅の長文がフレーム外へ。FILL 折返し or 幅固定 or 改行。生成後に右端 rightEdge を必ず確認。
- **濃背景上の暗要素**（グレーアバター等）は埋もれる → 明るいグレー/白に。

## 6.5 画像加工レシピ（use_figma・同一 imageHash に適用）

配置した画像は Figma 上で加工して魅力を上げる。**できる**：トリミング/色調/モノクロ/デュオトーン/スクリム/マスク/影/傾け。**できない**：ピクセルレタッチ・AI背景切り抜き（透過PNGは素材側で用意）・新規生成。

```js
const img=(ex={})=>({type:"IMAGE",imageHash:H,scaleMode:"FILL",...ex});
// ② トリミング/リフレーム ★必ず被写体を読んでから（機械的中央クロップ禁止）
//   手順：(1) 画像を Read して顔/被写体の正規化中心 (fx,fy) を読み取る
//        (2) タイル比に合う窓を作る：正方タイルなら sw=sh*(imgH/imgW)。被写体の周りに余白を持たせ窓は小さすぎない
//        (3) 窓を被写体中心に：transX=fx-sw/2, transY=fy-sh/2 を [0,1-窓] にクランプ
//   例：顔(0.68,0.30)・2912x1632・正方タイル → sh=0.55, sw=0.55*1632/2912=0.308
node.fills=[{type:"IMAGE",imageHash:H,scaleMode:"CROP",imageTransform:[[0.308,0,0.526],[0,0.55,0.025]]}];
// 検証：配置後スクショで「顔/被写体が中央・頭上に余白・見切れ無し」を確認。ズレたら fx,fy,窓を調整
// ★FILL の罠：scaleMode FILL は画像“全体”を中央化するため、被写体が端にある写真は被写体が寄ってしまう。
//   被写体を枠中央に置きたい時は（色調/マスク/スクリム等どの加工でも）fills[0] を上記 CROP+被写体中心transform にする。
//   「もっと引く」= 窓 sh を大きく（例 0.78→0.90）。「寄る」= sh を小さく。
// ③ モノクロ（filters 各 -1..1：exposure/contrast/saturation/temperature/tint/highlights/shadows）
node.fills=[img({filters:{saturation:-1,contrast:0.05}})];
// ④ 橙デュオトーン（モノクロ画像＋Drive橙を乗算オーバーレイ。fills[0]=下）
node.fills=[img({filters:{saturation:-1,contrast:0.1}}),{type:"SOLID",color:DRIVE,opacity:0.6,blendMode:"MULTIPLY"}];
// ⑤ スクリム（写真上の文字可読化：下方向に黒0→0.75 グラデを重ねる）
node.fills=[img(),{type:"GRADIENT_LINEAR",gradientTransform:[[0,1,0],[-1,0,1]],gradientStops:[{position:0.4,color:{r:0,g:0,b:0,a:0}},{position:1,color:{r:0,g:0,b:0,a:0.75}}]}];
// ⑥ 円マスク＋影（矩形を cornerRadius=幅/2 で円に）
node.cornerRadius=node.width/2; node.fills=[img()]; node.effects=[{type:"DROP_SHADOW",color:{r:0,g:0,b:0,a:0.3},offset:{x:0,y:10},radius:24,visible:true,blendMode:"NORMAL"}];
// ⑦ 傾けコマ風（モードB）
node.rotation=-6; node.effects=[{type:"DROP_SHADOW",color:{r:0,g:0,b:0,a:0.25},offset:{x:0,y:8},radius:18,visible:true,blendMode:"NORMAL"}];
```
用途：③④=ブランドトーン統一/特集 ⑤=写真Hero見出し ⑥=監修者アバター/浮遊前景 ⑦=マンガ調コマ ②=顔/料理の寄せ。任意シェイプmaskは図形と画像で boolean/mask group。

## 7. 自己検証チェックリスト（報告前に必須）

- [ ] 右端/下端のはみ出し無し（rightEdge < frame幅、最終要素 bottom < frame高）
- [ ] 要素衝突・重なり無し（特にブリッジ画像 × Hero 本文）
- [ ] 濃背景上のコントラスト十分（白抜き文字・明アバター）
- [ ] 押し売り/空語が無い（Words-first）
- [ ] FAM BOX（スペース有）表記・大前 恵/和田 毅 スペース表記
- [ ] グレーボックスの位置/サイズが意図的（大きく・流れに沿って）
- [ ] スクショを撮って参照画像と差分を3点以上自己批評→修正済
