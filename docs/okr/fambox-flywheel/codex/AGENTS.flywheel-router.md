<!--
これは「草案」です。レビュー後、以下のどちらかに貼り付けて有効化してください：
  (A) リポジトリルート /Users/archecoinc./Desktop/Claude_1/AGENTS.md（このフォルダで Codex 起動時に自動読込）
  (B) ~/.codex/AGENTS.md（全プロジェクト共通。~/.codex 書込は承認制＝/tmp 経由+cp）
Claude Code の「スキル自動発火」を Codex 側で再現するためのルーター。Codex はキーワードでスキルを自動起動しないため、AGENTS.md に「どの入力で何を読むか」を明示する。
-->

# FAMBOX Design Flywheel — Codex Router

このリポジトリ（`Claude_1`）で FAMBOX / FAM BOX の制作・運用を行うときは、作業前に該当する真実源を **Read してから** 着手する。抽象ルールより living docs と実機検証を優先する（Claude Code の Skill 機構と同じ規律）。

## 共通ハードルール（全 FAMBOX 作業）
- ブランド表記は **FAM BOX**（スペース有）。監修者は **大前 恵 / 和田 毅**（スペース有）。
- 日本語フォント＝Hiragino、英字＝Poppins（印刷物は F910/YuMincho を例外で追加）。構築時は Noto Sans JP 代替→Mac で差し替え。
- ファイル生成後は必ず読み戻し／スクショで証拠検証。「保存しました」だけの報告禁止。
- 同じ修正が3回失敗したら対処療法を止め根本原因へ。
- `~/.codex` / `~/.claude` 配下はハーネス自己改変扱い → 直接書かず /tmp 経由＋cp 承認制。

## トリガー → 読むファイル（Read してから着手）

### 1. 印刷物（チラシ/パンフ/ポスター/カタログ/梱包同梱/B2B提案）
トリガー語：「チラシ」「flyer」「パンフレット」「ポスター」「カタログ」「梱包同梱」「印刷物」「提案資料」＋FAM/FAMBOX
→ 次を順に Read：
1. `.claude/skills/fambox-flyer-builder/SKILL.md`（ワークフロー／3モード／Anti）
2. `.claude/skills/fambox-flyer-builder/references/build-playbook.md`（Figma手続き：upload_assets/箱/加工/罠/節点）
3. `.claude/skills/fambox-flyer-builder/references/taste-and-tokens.md`（3モード＋トークン）
4. `.claude/skills/fambox-flyer-builder/references/asset-index.md`（画像索引 v3：スロット→実写真）
5. `brand/fambox/design-system/bugs.md`（DOCTRINE-006〜009・PROC）
6. `docs/okr/fambox-flywheel/projects/flyer-packaging/PRINT-DESIGN-DNA-research-2026-06-04.md` / `TEMPLATE-fambox-flyer-v1.md`
- 必須手順：モード宣言→比率ブロッキング→俯瞰→主役から精緻化→生成後スクショ自己検証（build-playbook §7）。
- 画像は構造をグレーボックスで確定 → 索引でスロットに合う実写真を `upload_assets(nodeId)` で配置。索引に無い/質不足はグレーのまま＋素材依頼。人物の個人名同定・肖像/契約・チーム許諾は人間確定。

### 2. Shopify Liquid セクション（新規/修正/デバッグ）
トリガー語：「Liquid」「Shopify」「Section」「テーマカスタマイザー」「CSS効かない」「richtext」「inline style」
→ Read：`brand/fambox/design-system/bugs.md` ＋ memory の `feedback_shopify_liquid_specificity` / `feedback_design_system_liquid_patterns` 相当。
- 「CSS変えても変わらない」報告時の確認順序：inline style→richtext `<p>`ネスト→CDNキャッシュ→テーマ取違え→ブラウザキャッシュ。
- 変更後は grep で出力HTMLとCSSセレクタ一致を検証。本番は curl で grep 確認（プレビュー≠本番）。

### 3. ブランド UI（食事診断/ウィザード/ダッシュボード/新規 section）
→ Read：`.claude/skills/fambox-design/SKILL.md`（FAM BOX 視覚言語）、必要なら `fambox-diagnosis-builder`。

### 4. ブログ/メール/アンバサダー等のコンテンツ
→ Read：`docs/okr/FAMBOX_Verbal_Guideline_v1.0.md` ＋ 該当スキル（`fambox-blog-publisher` / `seal-email-builder` / `moritani-content-generator`）。

### 5. デザイントークン整合性
→ `snippets/fambox-tokens.css.liquid` を真ソースに var(--xxx) 実在 grep 検証（仮置きトークン名禁止）。

## MCP（Codex 側で利用可能）
- 設定済（`~/.codex/config.toml`）：`figma`（公式・upload_assets/get_screenshot/get_metadata）／`figma-bridge`（socketプラグイン・要 Connect+join_channel）／`iconify`／`lottie`／`notion`。
- 未設定（必要時に追加）：Slack / Google Drive / Gmail / Calendar / Chrome。

## 成長ループ（Learn→Generate）
作業中の学び・罠・好FBは散逸させず即、次のいずれかに追記：①再利用規律→`bugs.md` DOCTRINE/PROC ②モード/トークン→PRINT-DESIGN-DNA＋taste-and-tokens ③Figma手続き→build-playbook ④型→TEMPLATE。Claude/Codex どちらで作業しても同じファイルを真実源として同期する。
