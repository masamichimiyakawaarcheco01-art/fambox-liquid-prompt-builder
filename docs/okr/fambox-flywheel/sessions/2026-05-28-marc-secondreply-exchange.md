# Marc Second Reply Exchange — 2026-05-28

> Marc が GitHub 共有 + DNA/bugs.md を読み込んだ後の本格 review。peer 関係が完全に成立した瞬間。

参加：宮川 ↔ Marc-Antoine Lecat ↔（参考）稲井さん
媒体：Slack

---

## Marc からの返信（受信）

```
Masamichi san, Inai san, I properly reread all the documents.
Honestly, I'm really impressed by what both of you are building.

Sharing a few main reactions here, along with what we shipped on our side this week.

For Masamichi

What's working especially well
• The Brand / Engine / Data separation is excellent. It's very close to the
  logic I've been trying to build in Archeco, but expressed more clearly.
  I'll probably adopt the vocabulary moving forward.
• The D-NNN decision log with revision tracking is also very solid and more
  structured than what I currently use. I added it as a reference candidate
  in our EXTERNAL-INFLUENCES.md.
• Your bugs.md is probably one of the most important files in the system.
  The real Learn loop lives there: documenting mistakes and evolving the
  methodology from them.

A few areas I'd watch carefully
• D-020 (70/30 AI/Human split): I think the principle is very strong, but
  percentages quickly become abstract. In the long run, I think it's more
  sustainable to frame it as categories of work: "AI proposes", "human
  validates / adjusts".
• The Flywheel: Sense and Learn are probably doing most of the real work.
  Generate and Reach are the most visible parts, but also the easiest. If
  Learn isn't protected, the system risks producing faster without actually
  learning better.
• Brand DNA v1.0: I think it would help to explicitly define what triggers
  a future v1.1 (new audience, new market, new direction, etc.), otherwise
  the document may slowly fossilize over time.

One important suggestion
I think your biggest challenge will arrive when you open the system to
non-designers. What really scales is not only the quality of the rules,
but the clarity of what has already been decided for each project.

In Archeco, we handle this with: `projects/<client>/CLAUDE.md` → one single
file explaining:
* the client rules,
* visual direction,
* AI/Human boundaries,
* vocabulary,
* exclusions.

I genuinely think building an equivalent before your Q1 2027 milestone
would save you a huge amount of time.

[... For Inai san section ...]

What we shipped this week (v7.33 → v7.37)
Both of your work directly influenced several evolutions inside Archeco:

v7.34 — 2026-05-29
• Template + surfaces + hard rules + bugs index + pastilles + quickstart
  Six universal additions in one release.
  - projects/_TEMPLATE/CLAUDE.md (86 lines) — canonical template
  - art-direction/10-surfaces.md (203 lines) — 6 surfaces formalized
  - technical/06-workflow.md — Hard rules header (10 non-negotiable rules)
  - technical/bugs.md — Index V1-V51 table inserted in the head
  - claude-global/CLAUDE.md — Response format / progressive disclosure
  - README.md + install.sh at repo root — Quickstart in 6 steps

v7.33 — 2026-05-29
• Add AI/Human boundary doctrine to 06-ai-integration
  Every project must declare its AI/Human boundary explicitly per surface.
  The boundary is not universal — it varies by deliverable type and audience.
  Includes 11 default categories, declaration template, and the
  'declining = re-declaring' principle.

v7.32 — 2026-05-29
• Vendor cursor-talk-to-figma-mcp as bridge/ snapshot

Happy to add both of you as collaborators on the repo if useful for
cross-reference.

Very interesting to see our three systems evolving in different but
complementary directions:
* Masamichi → infrastructure for scaling a team
* Inai → brand fidelity across distributed production
* Marc-A → multi-surface production speed and consistency

Different problems, but in the end all orbiting the same challenge:
making decisions explicit and transmissible.

Thank you again for sharing your work. z
```

---

## Marc メッセージから抽出した重要洞察

### 評価（Validate）— このまま維持

1. **Brand / Engine / Data 分離** = excellent。Marc 自身が採用予定
2. **D-NNN decision log** = very solid、`EXTERNAL-INFLUENCES.md` に参考追加
3. **bugs.md** = "the real Learn loop lives there"（最重要視）

### 改善提案（Adopt）— D-021〜D-025 として反映

**Insight M5（→ D-021）：** 「70%/30%」の代わりに **「AI proposes / Human validates / adjusts」のカテゴリ** で定義
- 理由：パーセンテージは時間が経つと曖昧になる、カテゴリは長持ち

**Insight M6（→ D-022）：** **Learn 層を Step 1 から保護** すべき
- 警告：「**If Learn isn't protected, the system risks producing faster without actually learning better.**」
- Sense と Learn が実は最も難しい。Generate と Reach は visible だが easy

**Insight M7（→ D-023）：** DNA v1.0 に **Evolution Triggers** を明文化
- 化石化防止のため、何が起きたら v1.1 / v2.0 へ進むかを定義

**Insight M8（→ D-024）：** **`projects/<client>/CLAUDE.md` パターン** を採用
- 非デザイナーが入ってくる時に「すでに決まっていることの明確さ」がスケールに直結
- 「Q1 2027 マイルストーン前に作っておけば膨大な時間が節約できる」（Marc 予言）

**Insight M9（→ D-025）：** Archeco repo へのコラボ招待
- 「Happy to add both of you as collaborators if useful for cross-reference」

### 構造的気付き

Marc の最後の reframe：
> 「3つのシステムが **異なる問題を解いているが、同じ challenge を中心に進化** している」
> - Masamichi → infrastructure for scaling a team
> - Inai → brand fidelity across distributed production
> - Marc-A → multi-surface production speed and consistency
> 「Different problems, but in the end all orbiting the same challenge: **making decisions explicit and transmissible.**」

これは **peer ネットワークの存在意義の言語化**。3つの仕組みが補完関係にあるという認識が共有された。

---

## こちらからの返信（送信用）

### English（送信用）

```
Marc, this means a lot — thank you for the depth of reading and the very actionable feedback. I've already started incorporating it. Quick rundown:

**What you flagged, now reflected in the plan:**

1. **D-020 → D-021**: Reframed the AI/Human split from "70/30 percentages" to **categories of work**: AI proposes / Human validates / Human adjusts / Human decides. You're right — percentages would have rotted into abstract noise. Categories will survive Step 2/3 scaling.

2. **D-022: Learn layer protected from Step 1**: I had Learn as a Step 3 target. Your warning ("the system risks producing faster without actually learning better") shifted it. Learn now runs in minimum form from Step 1 — every Generate failure feeds bugs.md, every "explain twice" becomes a rule, and "this week's Learn progress" is now a permanent agenda item in our Friday business-dev meeting.

3. **D-023: DNA Evolution Triggers**: Added an explicit "when to bump to v1.1 / v2.0" section to the Brand DNA file. Bi-annual review scheduled. Big save — without this, I'd have happily let v1.0 fossilize.

4. **D-024: `brand/fambox/CLAUDE.md`**: Drafted v0.1 today, modeled on your `_TEMPLATE/CLAUDE.md` pattern. Identity / Surfaces / Hard Rules / AI-Human Boundary / Vocabulary / Exclusions / Decision-Log-Pointer. Will iterate toward v1.0 before Step 2 starts.

5. **D-025: Repo collaboration — YES please.** Reading your v7.32–v7.37 directly would accelerate things significantly. My GitHub username: [GitHub username を入れる]

**On your v7.33–v7.37 shipped this week:**
The Surfaces concept (v7.34) maps directly to my long-term multi-output goal — currently I'm Liquid-heavy, but Surfaces is the right abstraction for Web / Print / SNS / Email / etc. The "declining = re-declaring" principle (v7.33) is now embedded in CLAUDE.md §4.3.

I really appreciate the framing at the end — "three systems orbiting the same challenge: making decisions explicit and transmissible." That captures it perfectly. Different problems, complementary patterns, same core discipline.

Going to keep our exchange asynchronous and as-needed, but expect occasional pings as I hit specific friction — especially around the **bridge from human judgment → machine-readable rule** for the parts that aren't yet in bugs.md (copy soul, photo selection, "FAM-ness").

Thanks again 🙏
```

### 日本語参考（理解用）

```
Marc、本当にありがとう。読み込みの深さと、超実践的なフィードバックに感謝です。
既に反映を始めています。要点：

【Marc が指摘 → プランに反映済】

1. D-020 → D-021：AI/Human の境界を「70/30 のパーセンテージ」から「作業カテゴリ
   （AI proposes / Human validates / adjusts / decides）」に再定義。
   Marc の言う通り、パーセンテージは抽象的なノイズに化けたはず。
   カテゴリなら Step 2/3 のスケーリングに耐える。

2. D-022：Learn 層を Step 1 から保護。元プランでは Learn を Step 3 のゴールとして
   いたが、Marc の警告（「速くなるが学習しなくなるリスク」）でずらした。
   Learn は最小機構で Step 1 から稼働。Generate 失敗 → bugs.md 候補。
   「2回説明したらルール化」原則。「今週の Learn 進捗」は金曜事業開発の
   恒久発表項目に。

3. D-023：DNA Evolution Triggers。「いつ v1.1 / v2.0 へ上げるか」を明文化。
   半年ごとのレビューを設定。これがないと v1.0 をそのまま化石化させていた。

4. D-024：`brand/fambox/CLAUDE.md`。Marc の `_TEMPLATE/CLAUDE.md` パターンを
   参考に、今日 v0.1 を起こした。Identity / Surfaces / Hard Rules /
   AI-Human Boundary / Vocabulary / Exclusions / Decision-Log-Pointer。
   Step 2 開始前に v1.0 へ。

5. D-025：repo コラボ — YES。Marc の v7.32〜v7.37 を直接読めると一気に加速する。
   GitHub username: [GitHub username を入れる]

【Marc が今週リリースした v7.33〜v7.37 について】
Surfaces 概念（v7.34）は私の長期ゴール（多出力対応）と完全に整合。今は Liquid 中心
だけど、Web / Print / SNS / Email を統一する抽象として Surfaces は正解。
「declining = re-declaring」原則（v7.33）も CLAUDE.md §4.3 に既に組み込み済。

最後のフレーミングが特に良かった：「3つのシステムが同じ challenge を中心に進化し
ている — making decisions explicit and transmissible」。これが完璧に的を射ている。
異なる問題、補完的なパターン、同じコアの discipline。

非同期＆必要時に pings、で進めさせてください。特に
「人間の判断 → 機械可読ルールへの橋渡し」── まだ bugs.md に入っていない部分
（コピーの魂、写真選定、"FAM らしさ"）について詰まったら相談します。

改めてありがとう 🙏
```

---

## 採用した決定（DECISIONS.md より）

| ID | 内容 | 上書き対象 |
|---|---|---|
| **D-021** | AI/Human のカテゴリベース定義 | D-020 を上書き |
| **D-022** | Learn 層を Step 1 から保護機構必須化 | D-016 + D-005 補完 |
| **D-023** | DNA Evolution Triggers 明文化 | DNA v1.0 補完 |
| **D-024** | brand/fambox/CLAUDE.md 採用 | D-018 上位フレーム |
| **D-025** | Marc コラボ招待受諾 | 新規 |

---

## 反映ファイル

- `docs/okr/fambox-flywheel/DECISIONS.md` — D-021〜D-025 追加 + 上書き記録更新
- `brand/fambox/brand-dna/current.md` — Evolution Triggers セクション追加（D-023）
- `brand/fambox/CLAUDE.md` — 新規作成 v0.1（D-024）
- `docs/okr/fambox-flywheel/friday-presentation-2026-05-30.md` — 「2.5 Marc からの即時 peer フィードバック」セクション追加

---

## 次のアクション

1. 上の英語返信を Slack で Marc に送信（GitHub username を埋める）
2. 全変更を git commit + push
3. 金曜事業開発で「Marc 即時フィードバック → 既に反映」を発表
4. Marc の Archeco repo collaborator 招待が来たら受諾、`EXTERNAL-INFLUENCES-fambox.md`（仮）を作って Marc の影響を逆参照記録
