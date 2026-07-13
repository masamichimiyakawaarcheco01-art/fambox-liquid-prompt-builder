# Marc 向け Slack メッセージ（送信用最終版）

> **使い方：** 下のメッセージ本文をそのまま Slack にコピペ。
> **送信者：** 宮川さん本人が送信。
> **送信タイミング：** 2026-06-01（月）朝が推奨

最終更新：2026-05-26

---

## ⚠️ 送信前にやること（重要）

このメッセージには **GitHub URL** が4箇所あります。送信前に：

1. ターミナルで以下を実行（GitHub にブランチ push）：
   ```bash
   cd /Users/archecoinc./Desktop/Claude_1
   git push -u origin feat/flywheel-week-1
   ```

2. GitHub のリポジトリで以下の URL を取得：
   - `README.md` → `https://github.com/<org>/<repo>/blob/feat/flywheel-week-1/docs/okr/fambox-flywheel/README.md`
   - `ARCHITECTURE.md`
   - `environment-audit-v0.1.md`
   - `DECISIONS.md`

3. 下のメッセージ本文の `[GitHub link]` 4箇所を実 URL に置き換える

---

## 📨 メッセージ本文（日本語版）

> Marc が日本語読めるならこちら推奨。

```
Hi Marc!

宮川です。先日 須藤さんから「Marc と繋がってもらって個人的にゴリゴリやって」と勧められたので、メッセージしてます。

私もちょうど Marc みたいに AI と Design のインフラを作ろうとしていて、ARCHECO の左側（FAM 01 / FAMBOX）でやってます。目指してるのは：

「誰でも 7割の質のアウトプットを早く出せる仕組み（インフラ）を作る」

Marc と同じ目標だと思います。違うのは領域だけ：
• Marc：Wide & Fast(多サービスに浅く広く)
• 私:Middle & Fast(FAM 等の関連ブランド群に深く、ただし速く)

進め方は3 step：
1. 私個人のインフラ(10倍速) — 2026-07 目標
2. 須藤・松浦・マレル等が Slack 指示書で動かす運用 — 2026-10 目標
3. 誰でも使える = Flywheel MVP 完成 — 2027-Q1 目標

既に持ってる資産:
• FAMBOX Design System v0.5(tokens / components / patterns)
• bugs.md(28個の Anti-pattern 回避規律)
• Brand DNA v0.3 / Verbal Identity v1.0
• LPB v4.1(Figma → 構造化プロンプト変換、37%→84%精度向上の実績)
• Shopify Liquid セクション 100+ / Custom Claude Skill 19+
• 検証スタック(schema-lint / pre-commit / GitHub Actions audit)

詳しい構想と現状の棚卸しをドキュメントにまとめました：
• README(プロジェクト全体): [GitHub link]
• ARCHITECTURE(4層構造): [GitHub link]
• environment-audit-v0.1(私の現状): [GitHub link]
• DECISIONS(意思決定ログ D-001〜D-020): [GitHub link]

詳細な質問は私が手を動かす過程で詰まった時に都度投げますが、まず流し読みしてフィードバックもらえると嬉しいです。
「peer として情報交換」する関係でやらせてもらえると最高です(弟子-師匠じゃなく)。

返信は気が向いた時で OK です。よろしくお願いします 🙏
```

---

## 📨 メッセージ本文（English 版）

> Marc が英語のほうが読みやすそうならこちら。

```
Hi Marc!

宮川 here. 須藤 suggested I reach out and connect directly with you, so here we go.

I'm also building AI + Design infrastructure - similar to what you're doing - but on the left side of ARCHECO (FAM 01 / FAMBOX). My goal:

"Build infrastructure where anyone can produce 70%-quality output fast."

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

I'll ping you with specific questions as they come up while I'm working, but it'd be amazing if you could skim through and share initial thoughts.
Would love a "peer info-exchange" relationship rather than student-teacher.

Reply whenever feels right. Thanks! 🙏
```

---

## ✅ 送信前チェックリスト

- [ ] GitHub に `feat/flywheel-week-1` push 済み
- [ ] 4本の URL を実 URL に置き換えた
- [ ] 日本語版 / 英語版 のどちらを送るか決めた
- [ ] Marc の DM か #design チャンネル等、適切な場所
- [ ] 平日朝の時間帯（月曜午前推奨）

---

## 送信後の運用ルール（D-019 整合）

- Marc から返信が来たら `sessions/2026-06-XX-marc-review-1.md` に記録
- 詳細質問は手を動かす過程で出てきた時に投げる（一度に1つずつ）
- 重要な学びは DECISIONS.md に追加（D-021 以降）
