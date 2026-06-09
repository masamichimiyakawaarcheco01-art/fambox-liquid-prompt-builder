# 対話 Codex 用ビルドブリーフ — B-front（法人チラシ表）

> 使い方：対話 Codex を**リポジトリ直下**で起動し、下の「貼り付けるプロンプト」をそのまま投げる。`use_figma`（書込）や画像 POST の確認が出たら **承認（Allow/Yes）** する。ヘッドレス `codex exec` だと書込が自動キャンセルされるため、ブラッシュアップ/ビルドは対話モードが正解。

## 起動
```bash
# フルパス（PATH 未登録のため）。毎回面倒なら alias 推奨
/Applications/Codex.app/Contents/Resources/codex --cd /Users/archecoinc./Desktop/Claude_1
# alias codex="/Applications/Codex.app/Contents/Resources/codex"
```
- 起動時にリポジトリルート `AGENTS.md`（Flywheel ルーター）が自動読込される。
- 承認モードは対話なら都度確認。`use_figma` の書込・画像 `upload_assets` の POST が出たら Allow。

## 貼り付けるプロンプト（このまま投げる）

```
FAMBOX の B向け（法人/チーム向け）チラシの「表（front）」を Figma に新規作成して。fileKey=PqlR5HfCaBZuPRxW0fbzVH。fambox-flyer-builder スキルに従い、必要なら SKILL.md / references / bugs.md を読む。

参照：既存の完成版 0608（nodeId 113:8）が同じ B-front。get_metadata と get_screenshot で読み、レイアウト・テキスト・座標を参考にする（コピー可。ただし画像は自分で当て込む）。

作るもの：use_figma で新規フレーム（595x842, name="B-front-codex", x=11400, y=1377, 白背景, clipsContent=true）を作り、113:8 と同等構成を組む：
- マストヘッド：オレンジ帯(full-bleed)＋FAM BOX ロゴ＋見出し「現場の食事を、強いチームの土台に。」＋サブ＋右上にヒーロー画像枠（境界をまたぐ角丸矩形）
- stat pill「13 / チーム導入実績 プロ野球・Jリーグ等」
- ISSUES：「こんな課題はありませんか？」＋4課題（2x2）
- SOLUTION：「FAM BOX なら解決できます」＋3点（現場の食事をそのまま / 自炊負担を大幅軽減 / 優れた費用対効果）
- SUPERVISORS：濃紺の箱＋円形アバター2つ（大前 恵 / 和田 毅）＋肩書
- CAMPAIGN：帯（無料トライアル系）
- フォント：日本語=Noto Sans JP、英字=Poppins（ブランドフォントは後で人間が差し替え）

画像の当て込み（最重要）：upload_assets を nodeId 指定で使い、グレー枠に実写真を流し込む（submitURL に POST → fill。build-playbook §3）：
- ヒーロー画像枠 ← Asset/Mask group.png
- 大前アバター ← Asset/【明治】大前写真.png
- 和田アバター ← clients/明治/CL05_TSK/PJ01_FAM紹介/Wada_01.png

完了後：get_screenshot で B-front-codex 全体を撮り、build-playbook §7（はみ出し無し/衝突無し/濃背景コントラスト/FAM BOX・大前 恵・和田 毅 のスペース表記/グレー枠が画像で埋まったか）を自己検証。最後に「新アートボード nodeId」「当て込んだ3枚の placedOnNodeId」「検証結果」を報告。

注意：既存 113:8 や他アートボードは変更しない。新規 B-front-codex のみ作成・編集する。
```

## 承認ポイント（クリックする箇所）
1. `use_figma`（フレーム/テキスト/帯の作成・編集）の書込確認 → Allow
2. `upload_assets` 後の `curl`（submitURL への画像 POST）→ Allow（ネットワーク）
3. 完了後の `get_screenshot` は読取なので確認なしで通る

## 検証
Codex が報告したら、Claude（私）側でも `get_screenshot nodeId=<新ID>` を撮って before/after・索引スロット適合を確認できる。気になる点（顔の寄せ・コントラスト・はみ出し）は「§6.5 の CROP で顔中央寄せして」等と追指示すれば対話で詰められる。
