# PUBLISH — 宮川さんの「アップデートの儀式」

> SYSTEM.md（真ソース）を改善したら、この手順で Project に反映する。
> これが「アプリのアップデート」。マレルは次のチャットから自動で最新版になる。

## 手順
1. **真ソースを改訂**（Claude Code）
   - `docs/design-wheel/patterns/<p>/SYSTEM.md` を編集
   - 必要なら spec を再生成（`ds-bundle/<p>/...spec.md`）
   - `git add` → `git commit`（変更履歴が残る＝いつでも戻せる）
2. **Project の知識を差し替え**（claude.ai）
   - Design Wheel Project を開く → ナレッジ（添付）
   - 該当パターンの**古いファイルを削除** → 改訂版をアップロード
   - ファイル名は同じにする（混乱防止）
3. **動作確認**（自分で1回）
   - 「<パターン>でテスト用LPを作って」と打ち、改善が反映されているか確認
4. **必要なら告知**
   - Slack #design-wheel に「<パターン> を更新しました（変更点1行）」

## 更新の判断材料
- FEEDBACK ログ（#design-wheel）で**評価が低い／同じ困りごとが繰り返す**パターンを優先改訂。
- 「らしさ（taste 一致）」が低い指摘は、refs を足してから SYSTEM を直す（即興で直さない）。

## 原則
- **真ソースは常に git**。Project は配布コピー。両者をズラさない（PUBLISH を必ず通す）。
- 大きな仕様変更は SYSTEM の version を上げる（v0 → v1 …）。
