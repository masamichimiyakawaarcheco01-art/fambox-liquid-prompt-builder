# Design Wheel — Project v0 スターターキット

> ADR-001（`../../DECISIONS.md`）段階1。claude.ai 共有 Project を「Design Wheel ツール v0」にする4点セット。
> 目的 = マレル1〜2人 × 実案件で1周回し、Webアプリ化前に**実使用の痛点を取る**。

## 中身（4点）
| ファイル | 役割 |
|---|---|
| `PROJECT-INSTRUCTIONS.md` | Project のカスタム指示（ツールの頭脳：選び方→HTML生成→仕上げ→FB促し） |
| `KNOWLEDGE-MANIFEST.md` | Project に登録する知識ファイルの一覧（在庫4パターンの SYSTEM） |
| `PUBLISH.md` | 宮川さんの更新の儀式（git改訂→Project差し替え） |
| `FEEDBACK.md` | マレルが1行で返す型（Slack #design-wheel） |

## セットアップ手順（宮川さん・15分）
1. claude.ai で**新規 Project**「Design Wheel」を作る（チームに共有）
2. `PROJECT-INSTRUCTIONS.md` の中身を Project の**カスタム指示**に貼る
3. `KNOWLEDGE-MANIFEST.md` に沿って **SYSTEM ファイルをナレッジに登録**（MVP は digital + sporty の2つでも可）
4. Slack に **#design-wheel** チャンネルを作る（FEEDBACK 集約先）
5. 自分で1回テスト → マレル1〜2人に「実案件で使ってみて」と渡す

## 回し方（PDCA）
```
マレルが使う → #design-wheel に1行FB → 宮川が週1で集計
  → 弱いパターンの SYSTEM を改訂(git) → PUBLISH で Project 更新 → 全員が次から良くなる
```

## 卒業条件（→ 段階2: Web アプリ）
- 「毎回同じ操作が面倒」「exact サイズ書き出しが要る」「FBがSlackだと流れる」等の痛点が溜まったら、
  それを解く薄い Web アプリへ。エンジン（SYSTEM.md + HTMLキャプチャ）はそのまま流用。
