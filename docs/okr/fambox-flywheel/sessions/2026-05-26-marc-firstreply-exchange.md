# Marc First Reply Exchange — 2026-05-26

> 初回 Slack 共有への Marc の返信と、それへの返信を記録。

参加：宮川 ↔ Marc-Antoine Lecat
媒体：Slack

---

## Marc からの返信（受信）

```
今回の課題は、非デザイナーに対してブランド品質をスケールさせるという点で、私自身まだ完全には解けていない問題なので、むしろこちらも多く学ばせてもらうことになると思っています。

GitHubのドキュメントはいつでも送ってください。急ぎではありません。届いたらアーキテクチャと20の意思決定をしっかり読み込みます。

すでに私のやり方にもかなり近い部分があるので、共有できるポイントを2つだけ書きます。

1. フライホイールで一番難しいのは "Generate" ではなく "Learn" です。
   70%レベルのアウトプットを素早く作るのは比較的簡単ですが、価値が積み上がるかどうかは、失敗がどれだけルールに変換されるかで決まります。
   私のシステムでも最も重要なのはデザインのドクトリンではなく、"バグログ"です。実際の失敗とその修正を記録したもので、これがすべての中核になっています。
   チェックリストは静的なルール集ではなく、「FAMっぽくない」というような修正がすべて蓄積されていく"記憶のログ"に進化させるのが重要で、それが本当の学習になります。

2. ガードレールはレビューよりも強いです。これも私のやり方そのものです。
   Adobe的な"brand intelligence"（人の後追いレビューではなく、システム側に制約を埋め込む発想）は正しい方向性ですし、今ボトルネックが生まれている理由もそこにあります。品質判断がまだ個人の頭の中にあるためです。
   私のやり方は、判断を頭の外に出し、システムが直接読むファイルに落とし込むことです。すでにMoemiさんの .md ファイル（哲学とチェックリスト）はその方向にあります。
   シンプルな基準として、同じ修正を2回説明した場合、それはレビューではなくルールとしてファイルに入れるべきです。

もう1つ重要なのは、まだ起きていない問題に対してルールを作りすぎないことです。システムは予測ではなく、実際の摩擦から育てるべきで、良いルールのほとんどは失敗の後に生まれます。

Moemiさんにとっての"FAMっぽさ"を中心軸に置くのはとても良い判断だと思います。Figmaを頻繁に使わないチームでこの一貫性を保つのは本質的にシステム問題であり、.mdベースのアプローチは非常に適しています。

もしよければ、ぜひその2つのファイルを見せてください。ドキュメントが届いたらすぐに読みますので、急がなくて大丈夫です。ありがとうございます。
```

---

## Marc メッセージから抽出した重要な洞察（決定ログ候補）

将来 DECISIONS.md に追加すべき内容：

### Insight M1：「Learn」が Flywheel の最難関
- Generate（70%作る）は比較的簡単
- 価値の蓄積は「失敗がルールに変換される速度」で決まる
- バグログ = システムの中核

### Insight M2：「2回説明したらルール化」原則
- 同じ修正を2回説明した時点で、レビューではなくルールにする
- 判断を頭の外に出し、システムが読むファイルへ

### Insight M3：「予測で作らない」原則
- 起きていない問題にルールを作りすぎない
- システムは予測ではなく実際の摩擦から育てる
- 良いルールは失敗の後に生まれる

### Insight M4：FAM っぽさを中心軸にした判断は正しい
- Figma を頻繁に使わないチームで一貫性を保つ = システム問題
- .md ベースのアプローチは適している

→ **次回 DECISIONS.md 更新時に D-021〜D-024 として追加**

---

## こちらからの返信（送信予定）

### English 版（送信用）

```
Hey Marc, thank you for this — honestly couldn't have hoped for a better response.

The "Learn > Generate" framing landed hard. You named exactly the thing I keep underestimating.

Some resonance with your points:

**1. On the bug log being the core**
This maps directly to what's already in motion on my side. The bugs.md I mentioned (28 entries) is exactly that — every entry is a real failure I encountered (anti-patterns, brand drift, my own mistakes). It started as a personal "don't do this again" note and grew into the de facto FAMBOX quality standard.

In parallel, my Claude memory system holds ~28 feedback*.md files — every time I repeat a mistake, it becomes a feedback file that auto-loads in future sessions. So the "explain it twice = make it a rule" principle you described is something I'm already doing in a primitive way. Your formulation gives me a sharper standard to apply more deliberately from now on.

**2. On guardrails > reviews**
Already implemented on the code side — schema-lint.py, pre-commit hooks, and GitHub Actions all block commits that violate brand rules. But you're right: for the parts that aren't yet machine-readable — "FAM-ness" judgment, copy tone, photo selection — the bottleneck still lives in my head.

That's the part I need to externalize next. The bridge from human judgment → machine-readable rule is exactly where I'd love your eye most.

**3. On not over-predicting rules**
This caught me. My LPB v4 (Liquid Prompt Builder) has accumulated rules from imagined edge cases as much as from real failures. I'll prune it back to "rules that emerged from actual friction." Thank you for that.

**The two files you asked about**
I believe they are:
- Philosophy: brand/fambox/brand-dna/FAM_brand_DNA_v0.3.md (+ STRATEGY.md)
- Checklist: brand/fambox/design-system/bugs.md (28 entries)

I'll include direct GitHub links to both in the follow-up shortly, alongside the architecture docs — so you can see them in context.

Looking forward to the deeper exchange once you've had time to read through. Genuinely grateful 🙏
```

### 日本語参考（理解用）

```
Hey Marc、本当にありがとう ── これ以上望めない返信です。

「Learn > Generate」のフレーミングは強く刺さりました。自分がずっと過小評価していたところを的確に言語化してくれました。

2つの洞察への反応：

**1. バグログが中核**

これは実は私がやっていることと直結します。前のメッセージで触れた bugs.md（28エントリ）は、まさにそれです。すべて私が実際に遭遇した失敗（アンチパターン・ブランド逸脱・自分のミス）。最初は「同じ失敗を繰り返さないため」の個人メモだったのが、いつの間にか事実上の FAMBOX 品質基準になっていました。

それに加えて Claude の memory システムに ~28 個の feedback*.md ファイルがあります。同じミスを繰り返したら feedback ファイルに変換して、次のセッションで自動ロードされるようにしています。Marc が言う「2回説明したらルール化する」原則 ── 私もプリミティブな形ですでにやっていて、Marc の定式化でより明確な基準が得られました。これからはこの基準を意識的に適用していきます。

**2. ガードレール > レビュー**

コード側ではこれを既に実装しています（schema-lint.py / pre-commit / GitHub Actions が全部ブランドルール違反のコミットをブロック）。でも、機械可読化できていない部分 ──「FAMっぽさ」の判断、コピーのトーン、写真選定 ── は確かにまだ私の頭の中にあります。

ここを次に外部化したい。人間の判断 → 機械可読ルールへの橋渡しが、Marc に最も見てもらいたい領域です。

**3. ルールを予測で作りすぎない**

これは刺さりました。私の LPB v4（Liquid Prompt Builder）は、実際の摩擦より「想像された edge case」からルールが蓄積されている部分があります。「実際の摩擦から生まれたルールだけ」に整理し直します。ありがとう。

**Marc が言っていた2つの .md ファイル**

おそらくこの2つだと思います：
- 哲学（Philosophy）：brand/fambox/brand-dna/FAM_brand_DNA_v0.3.md（+ STRATEGY.md）
- チェックリスト：brand/fambox/design-system/bugs.md（28エントリ）

フォローアップに両方の GitHub リンクを含めます。アーキテクチャと合わせて文脈の中で見られるようにします。

読んでもらった後の深い意見交換、楽しみにしています。本当に感謝です 🙏
```

---

## 送信後のフォローアップ計画

push 完了後、以下を1つの Slack メッセージにまとめて送る：

```
Here are the docs 👇

【The two you asked about】
• Philosophy (Brand DNA): [GitHub link]
• Checklist (bugs.md, 28 entries): [GitHub link]

【Broader context】
• Project overview (README): [GitHub link]
• Architecture (4-layer): [GitHub link]
• Decision log D-001~D-020: [GitHub link]
• My current env audit: [GitHub link]

If short on time, the bugs.md + decisions log alone will give you a strong gist of how the system thinks. The architecture doc is the higher-level frame.
```

---

## 次のアクション（今日 / 明日）

1. **🟡 今すぐ：** 上記英語返信を Slack で送信
2. **⚪ 続いて：** B 案 commit 実行（新ブランチ feat/flywheel-week-1）
3. **⚪ commit 後：** Push & GitHub URL 取得（合計6リンク）
4. **⚪ URL 取得後：** フォローアップメッセージを Slack で送信
5. **⚪ 後日：** Marc の Insight M1〜M4 を D-021〜D-024 として DECISIONS.md に追加
