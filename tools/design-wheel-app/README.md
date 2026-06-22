# Design Wheel App（ローカル Web アプリ MVP）

ADR-001 段階2。非デザイナーが「パターンを選ぶ → 言葉で指示 → 叩き台が出る → 書き出す」を
1画面で行うローカル Web アプリ。真ソース = `docs/design-wheel/patterns/<p>/SYSTEM.md`。

## できること（MVP）
1. **パターン選択**（在庫4: corporate / digital / gradient / sporty）
2. **チャット指示 → HTML 生成**（Claude API が該当 SYSTEM.md を厳守して生成）
3. **ライブプレビュー**（iframe）
4. **PNG 書き出し**（Chrome ヘッドレス・正確サイズ・Retina×2。5アスペクト比）
5. **フィードバック記録**（★評価＋困った点 → `feedback.jsonl`）＝ Learn ループ

## 起動
```bash
cd tools/design-wheel-app
npm install                 # 初回のみ
cp .env.example .env        # APIキーを入れる
npm start                   # → http://localhost:8750
```

## API キー
- 生成には Anthropic API キーが必要（`console.anthropic.com` で発行）。
- `.env` に `ANTHROPIC_API_KEY=sk-ant-...` を設定。**専用キーを推奨**
  （Claude Code セッションのキーを流用すると意図しない課金になり得る）。
- 既定モデル = `claude-opus-4-8`。コスト優先は `.env` に `DW_MODEL=claude-sonnet-4-6`。
- キー未設定でも **プレビュー枠/PNG書き出し/フィードバックは動作**（生成のみ無効）。

## 技術
- Node + Express / `@anthropic-ai/sdk` / システム Chrome（書き出し・追加インストール不要）。
- 重いフレームワーク無し（素 HTML/JS）。SYSTEM.md は git の真ソースを直読み。

## 構成
```
server.js          エンドポイント（/api/patterns /generate /export /feedback）
lib/patterns.js    SYSTEM.md 読み込み・カタログ
lib/generate.js    Claude API 生成（SYSTEM を system prompt に注入）
lib/export-png.js  Chrome ヘッドレス PNG 書き出し（5サイズ）
public/            フロント（index.html / app.js）
feedback.jsonl     フィードバックログ（git管理外）
```

## ステータス
v0.1 MVP。UI・パターン読込・PNG書き出し・フィードバックを実機確認済み。
生成は API キー設定で点灯。次 = 実キーで1本通す → マレルに使ってもらう。
