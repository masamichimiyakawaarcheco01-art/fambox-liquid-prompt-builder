# Marc 向け Slack メッセージドラフト v0.1

> **目的：** Marc に Flywheel 構想を peer として相談する初回メッセージ。
> **方針（D-019）：** Slack ベース / 質問は front-load しない / 概要だけ共有して詳細は都度

最終更新：2026-05-26

---

## 送信タイミング

- **来週月曜（2026-06-01）朝**
- 平日朝にすると Marc が読みやすい

---

## 共有方法の準備

Slack で文書リンクを貼るので、事前に以下のどれかで Marc がアクセスできる形にする：

| 方法 | やり方 | 推奨度 |
|---|---|---|
| **GitHub リンク** | Phase 0 で commit 済み。push してから GitHub の docs/okr/fambox-flywheel/ パスを共有 | ⭐⭐⭐ |
| **Slack ファイル添付** | .md を Slack にアップロード | ⭐⭐ |
| **Notion へ複製** | Notion にコピーしてリンク共有 | ⭐ |

**おすすめ：** GitHub にプッシュ → Slack で `https://github.com/<org>/<repo>/blob/main/docs/okr/fambox-flywheel/README.md` の形で共有

---

## 📨 メッセージ本文（日本語版）

> Marc が日本語読めるなら日本語で OK。英語必須なら下記の英語版を使う。

```
Hi Marc!

宮川です。先日 須藤さんから「Marc と繋がってもらって個人的にゴリゴリやって」と勧められたので、メッセージしてます。

私もちょうど Marc みたいに **AI と Design のインフラ** を作ろうとしていて、ARCHECO の左側（FAM 01 / FAMBOX）でやってます。目指してるのは：

> 「誰でも 7割の質のアウトプットを早く出せる仕組み（インフラ）を作る」

Marc と同じ目標だと思います。違うのは領域だけ：
• Marc：Wide & Fast（多サービスに浅く広く）
• 私：Middle & Fast（FAM 等の関連ブランド群に深く、ただし速く）

進め方は3 step：
1. 私個人のインフラ（10倍速）— 2026-07 目標
2. 須藤・松浦・マレル等が Slack 指示書で動かす運用 — 2026-10 目標
3. 誰でも使える = Flywheel MVP 完成 — 2027-Q1 目標

既に持ってる資産：
• FAMBOX Design System v0.5（tokens / components / patterns）
• bugs.md（28個の Anti-pattern 回避規律）
• Brand DNA v0.3 / Verbal Identity v1.0
• LPB v4.1（Figma → 構造化プロンプト変換、37%→84%精度向上の実績）
• Shopify Liquid セクション 100+ / Custom Claude Skill 19+
• 検証スタック（schema-lint / pre-commit / GitHub Actions audit）

詳しい構想と現状の棚卸しをドキュメントにまとめました：
• README（プロジェクト全体）：[GitHub link]
• ARCHITECTURE（4層構造）：[GitHub link]
• environment-audit-v0.1（私の現状）：[GitHub link]
• DECISIONS（意思決定ログ D-001〜D-020）：[GitHub link]

詳細な質問は私が手を動かす過程で詰まった時に都度投げますが、まず流し読みしてフィードバックもらえると嬉しいです。「peer として情報交換」する関係でやらせてもらえると最高です（弟子-師匠じゃなく）。

返信は気が向いた時で OK です！🙏
```

---

## 📨 メッセージ本文（English 版）

```
Hi Marc!

宮川 here. 須藤 suggested I reach out and connect directly with you, so here we go.

I'm also building **AI + Design infrastructure** — similar to what you're doing — but on the left side of ARCHECO (FAM 01 / FAMBOX). My goal:

> "Build infrastructure where anyone can produce 70%-quality output fast."

Same goal as yours, I think. Just a different domain:
• You: Wide & Fast (many services, shallow)
• Me: Middle & Fast (related brand cluster like FAM, deep, but still fast)

3 steps:
1. My personal infrastructure (10x speed) — target 2026-07
2. Slack-brief-driven workflow for 須藤, 松浦, Marel team etc. — target 2026-10
3. Anyone can use it = Flywheel MVP complete — target 2027-Q1

What I already have:
• FAMBOX Design System v0.5 (tokens / components / patterns)
• bugs.md (28 anti-pattern rules)
• Brand DNA v0.3 / Verbal Identity v1.0
• LPB v4.1 (Figma → structured-prompt converter, with proven 37%→84% accuracy boost)
• 100+ Shopify Liquid sections / 19+ Custom Claude Skills
• Validation stack (schema-lint / pre-commit / GitHub Actions audit)

I've put together docs that go deeper:
• README (project overview): [GitHub link]
• ARCHITECTURE (4-layer structure): [GitHub link]
• environment-audit-v0.1 (my current state): [GitHub link]
• DECISIONS (decision log D-001~D-020): [GitHub link]

I'll ping you with specific questions as they come up while I'm working, but it'd be amazing if you could skim through and share initial thoughts. Would love a "peer info-exchange" relationship rather than student-teacher.

Reply whenever feels right! 🙏
```

---

## 送信前のチェックリスト

送信する前に確認：

- [ ] GitHub に最新の docs/okr/fambox-flywheel/ を push 済み
- [ ] 4本のドキュメント（README / ARCHITECTURE / env-audit / DECISIONS）の GitHub URL が取得できる
- [ ] メッセージ本文に GitHub URL を埋めた
- [ ] Marc の日本語可否を確認（不明なら英語版が安全）
- [ ] 送信時間：平日朝（月曜朝など）

---

## 想定される Marc の反応と次手

| 反応 | 次手 |
|---|---|
| **詳細レビューしてくれる** | フィードバックを `sessions/2026-06-XX-marc-review.md` に記録 |
| **「peer 関係 OK、質問あれば」と短文返信** | 期待通り。Week 2 で実案件着手して具体的質問を準備 |
| **「興味あるけど忙しい、後で」** | リマインドせず、Week 2-3 で詰まった時に具体的質問だけ投げる |
| **返信なし（1週間以上）** | Slack で軽く「○○について短い質問だけいい？」と再アプローチ |

---

## メッセージ後の運用ルール（D-019 整合）

- 詳細質問は手を動かす過程で出てきた時に投げる
- 一度に複数の質問を投げない（Marc が返しやすいサイズに）
- やり取りの議事録は `sessions/` に保存
- 重要な学びは DECISIONS.md に追加

---

## バージョン履歴

| バージョン | 日付 | 内容 |
|---|---|---|
| v0.1 | 2026-05-26 | 初稿（日本語 + 英語）|
