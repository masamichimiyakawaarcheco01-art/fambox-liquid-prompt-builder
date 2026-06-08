# 梱包チラシ Figma 構築ログ + 学び — 2026-06-02

> **第一弾プロジェクト**：梱包用チラシ自動化の **4ステップループ ③ レビュー修正（Figma 構築）** 実行ログ
> ベース：[v1-output-2026-06-02.md](./v1-output-2026-06-02.md)
> 構築方法：figma-bridge（Cursor Talk To Figma MCP Plugin）で Claude が直接組成

最終更新：2026-06-02

---

## ✅ 構築完了したもの

C向け・B向け **両タイプ × 表面/裏面 = 計4フレーム**を A4 縦（595×842pt）で構築。

| フレーム | Node ID | 内容 |
|---|---|---|
| `01-C-front` | 1:2 | Hero（橙塊+FAMBOX+見出し+画像枠）/ FAMBOX とは / OUR STORY / 魅力の3ポイント / 監修者（大前+和田）/ CAMPAIGN 橙帯 |
| `02-C-back` | 3:28 | 上部橙アクセント+ロゴ / 調理3STEPカード / 保管方法 / ご注文 CTA+QR枠 / Instagram+QR枠 / お問い合わせ / フッター |
| `03-B-front` | 3:65 | Hero（橙塊+実績バッジ）/ ISSUES 4課題 / SOLUTION 帯3点 / 監修者 / CAMPAIGN（無料トライアル）橙帯 |
| `04-B-back` | 3:100 | アスリートの声 3カード / OPERATIONS 4ステップ box / 法人窓口 CTA+QR枠 / Instagram / フッター |

**配置**：Figma 上で 2×2 グリッド（C 上段、B 下段／表面が左、裏面が右）。

### 適用済みの規律（v1 仕様準拠）
- 色：DS v0.5 トークンのみ（drive `#FB4C15` / ink `#1B1D1A` / sub `#545655` / deep `#0F2A5C` / bg-secondary `#FAFAFA`）
- レイヤー命名：v1 の命名規則に準拠（`hero-bg` / `section-*` / `qr-*` 等）
- セクションラベルは英字オレンジ（OUR STORY / ISSUES / SOLUTION 等）= MENU CATALOG 踏襲
- superlative・押し売り表現なし、大前 恵 / 和田 毅 スペース表記

---

## 🔍 学び（④ → bugs.md / フロー文書へ反映候補）

### 学び①：figma-bridge は fontFamily を指定できない（最重要）

`mcp__figma-bridge__create_text` の引数は **fontSize / fontWeight / fontColor のみ**。
フォントファミリは指定不可で、生成テキストはすべて **Inter** になる（日本語も Inter フォールバック表示）。

**影響**：FAMBOX ブランドフォント（Poppins / Hiragino Kaku Gothic Pro）は**この経路では適用できない**。
**対処**：構築後に Figma 上で手動適用（テキスト全選択 → 英字 Poppins / 日本語 Hiragino）。これが「3割」の人間仕上げ工程に該当。
**意味**：D-021（AI proposes / Human adjusts）の実例。**AI = 構造・色・コピー配置（7割）／ 人間 = フォント適用・アセット差し込み・微調整（3割）** という分業が、紙媒体パイプラインでも成立すると実証。

### 学び②：socket 接続が切れやすい

プラグイン窓が非アクティブ／Figma スリープで channel から切断され、`export`・`set_focus` 等の read 系がタイムアウトする事象が複数回発生。
**対処**：切断時はプラグインで Connect を押し直し → 新 channel ID で `join_channel` し直す。socket サーバー自体は Claude 側で `bunx cursor-talk-to-figma-socket` を background 起動して代行可能（ユーザー操作を1ステップ削減）。
**運用Tips**：構築中は Figma プラグイン窓を開いたまま、Figma をアクティブに保つ。

### 学び③：長文段落は手動改行が確実

`create_text` に width 引数がなく、テキストは HUG（自動幅）で生成されるため長文がフレームをはみ出す。
**対処**：段落は `\n` を事前に挿入して改行を作り込む。リサイズ／auto-resize 切替ツールに頼らない方が安定。

### 学び④：read 系より create/set 系が安定

`create_frame` / `create_text` / `create_rectangle` / `set_fill_color` / `set_corner_radius` は安定動作。`export_node_as_image` は接続が新鮮な時のみ成功（再接続直後は通る）。
**対処**：検証スクショは要所のみ（各フレーム完成時）。ユーザーの Figma 画面を「目」として併用するとロバスト。

### 学び⑤：子要素の座標はフレーム相対

`parentId` 指定時、子の x/y は**親フレーム原点からの相対座標**。frame をキャンバス上のどこに置いても、子は相対座標で記述すれば良い（B フレームを y=920 に置いても子は y=0 起点）。

---

## ⏭ 残りの人間仕上げ工程（3割）

1. **フォント適用**：英字 Poppins（Bold/Medium）、日本語 Hiragino Kaku Gothic Pro。Hero タイトル「FAMBOX」は Poppins Bold。
2. **アセット差し込み**（v1 ⚠️ 項目）：
   - `Mask group.png`（大前+和田 ペア）→ Hero 画像枠
   - 大前・和田 顔写真 → 監修者プレースホルダ（グレー円/角丸）
   - QR コード（FAMBOX サイト / Instagram / 法人窓口）→ QR 枠
   - 黒版 FAM BOX ロゴ → 左上ロゴ文字を差し替え
   - 商品写真・調理 step 写真 / アイコン
3. **三角コーナーアクセント**（橙）の追加 — MENU CATALOG 踏襲要素、未実装
4. **クーポンコード確定**（C向け：個人定期 ○% / コード文字列）
5. **裁ち落とし 3mm** 設定（印刷入稿時）

---

## ⏱ 制作時間ログ（Before/After）

- **After（AI パイプライン）**：v1 コピー・レイアウト確定済みの状態から、figma-bridge で 4 フレームの構造組成 ≈ 1 セッション内（接続トラブル含む）。純構築は約 30–40 分相当。
- **Before（想定）**：同等の A4 両面 ×2 タイプを手動で Figma 組成 = 半日〜1日（4〜8 時間）の体感。
- **メモ**：「7割品質の骨組み」までを高速化できることを確認。残り3割（フォント/アセット/微調整）は人間。次サイクルで純構築時間を計測して数値を確定する。

---

## 🔄 4ステップループ進捗

```
✅ ① インプット    完了（brief filled-in v1）
✅ ② 生成         完了（v1-output）
✅ ③ レビュー修正  Figma 構築完了（このログ）← 人間のフォント/アセット仕上げが残る
🟡 ④ 学び         本ログに記録。bugs.md / フロー文書へ反映 → 次サイクルへ
```

---

## バージョン履歴

| 版 | 日付 | 内容 |
|---|---|---|
| v2 | 2026-06-02 | figma-bridge で4フレーム構造構築。学び5点を記録。フォント・アセットは人間仕上げ工程として分離 |
