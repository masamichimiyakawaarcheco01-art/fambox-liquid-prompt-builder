# 金曜事業開発 発表ドラフト（2026-05-30）— Voice-ready v2

> **目的：** Week 1 進捗共有 + Marc との peer 関係構築 + Week 2 コミット
> **想定参加者：** 須藤さん、Marc、アフタブ、角田、松浦、マレル等
> **想定時間：** 12〜15分（質疑5分含む）
> **方針（D-011 マーク流レビュー文化）：** 「手ぶらで行けない」レベルで挑む

最終更新：2026-05-28（v2 = voice-ready / Marc 2nd reply 反映）

---

## 全体構成

```
1. オープニング           1分
2. Week 1 成果            2分
3. Marc との peer 関係    3分  ★今週の最大の収穫
4. ポジショニング + 3段階  3分
5. Week 2 コミット        2分
6. 質疑                  5分
─────────────────────────
                        16分
```

---

## 1. オープニング（1分）

### 話す内容（声に出して読みやすい形）

> 本日の発表、FAMBOX Design Flywheel プロジェクトの Week 1 進捗共有です。
>
> 現状を一言で言うと、FAMBOX のデザインがすべて私のところに集中しています。
>
> マレルが回す SNS と動画コンテンツ、須藤さんと松浦さんが進める法人ページ改善、すべて最終的に「FAMBOX らしさ」のチェックで私を通ります。これが事業のスピード上限になっています。
>
> やることは一つ。**「誰でも 7割の質のアウトプットを早く出せる、AI と Design のインフラを作る」**。
>
> Marc が ARCHECO の右側でやっていることと同じ目標です。違うのは領域だけ。だから peer として情報交換しながら進めます。

### Marc 向け30秒英語サマリ（最初に添える）

> Quick context for Marc — this is the Week 1 update for FAMBOX Design Flywheel: building AI + Design infrastructure where anyone can produce 70%-quality output fast. Same direction as yours, just on the FAM brand cluster. I'll share what's done, what I learned from your feedback this week, and Week 2 commitments.

### スライド

```
┌──────────────────────────────────────────────┐
│  Purpose                                      │
│                                              │
│  「誰でも 7割の質のアウトプットを早く出せる、 │
│    AI と Design の仕組み(インフラ)を作る」    │
│                                              │
│  Marc と同じ目標、領域だけ違う                │
└──────────────────────────────────────────────┘
```

---

## 2. Week 1 成果（2分）

### 話す内容

> 今週やったことは3つです。
>
> **1つ目、構想の言語化。**
> Purpose と Goal Image を確定しました。3段階で進めます。詳しくは後で。
>
> **2つ目、永続化基盤の構築。**
> `docs/okr/fambox-flywheel/` にプロジェクト全体を置きました。意思決定 25個、議事録、進捗管理、すべて文書化。半年から2年の長期プロジェクトなので、**文脈を絶対に失わないこと**を最優先しました。
>
> **3つ目、自分の現状を棚卸し + Marc 接続。**
> 持っている資産を全部書き出しました。Design System v0.5、bugs.md 28規律、LPB v4.1、Brand DNA、Custom Skills 19本、自動検証スタック。これを Marc に共有してレビューを依頼しました。

### スライド

```
┌──────────────────────────────────────────────┐
│ Week 1 成果(3つ)                              │
│                                              │
│ ✅ 構想の言語化                               │
│    Purpose / Goal Image / 3段階モデル        │
│                                              │
│ ✅ 永続化基盤の構築                           │
│    意思決定 25 / 議事録 / 進捗管理            │
│                                              │
│ ✅ 環境棚卸し + Marc 接続                     │
│    既存資産マッピング + peer 相談             │
└──────────────────────────────────────────────┘
```

### 補足データポイント（聞かれたら）

- 全 commit: Phase 0 + Week 1 で 4 commit、約 2000行追加
- ブランチ：`feat/flywheel-week-1` に集約
- **構造的発見**: マレルチームの実態（動画・SNS 主体）と当初前提（Shopify セクション）に乖離があり、ターゲットを段階化

---

## 3. Marc との peer 関係構築（3分）★今週の最大の収穫

### 話す内容

> ここが今週最大の収穫です。
>
> Marc に Slack でプロジェクトを共有したら、**1日でディープなレビューが返ってきました**。peer 関係が成立した瞬間です。
>
> Marc がそのまま使えると評価してくれたもの：
> - Brand / Engine / Data の3層分離 ──「excellent、自分も採用したい」
> - D-NNN 意思決定ログ ──「自分のより構造化されている、参考に取り込む」
> - **bugs.md ──「the real Learn loop lives there」**、最重要視
>
> Marc が改善案を5つくれて、**全部今日中にプランに反映済**です：
>
> **D-021** ── AI と人間の境界を「70%/30%」のパーセンテージから「**AI が提案・人間が検証・人間が調整・人間が決定**」のカテゴリベースに再定義。Marc いわく「パーセンテージは時間が経つと抽象的なノイズになる」。確かにその通り。
>
> **D-022** ── Learn 層を Step 3 まで放置せず、**Step 1 から保護機構を必須化**。Marc の警告：「**Learn を保護しないと、システムは速くなるが学習しなくなる**」。これが一番刺さりました。
>
> **D-023** ── Brand DNA に **Evolution Triggers** を明文化。「いつ v1.1 / v2.0 に上げるか」を書く。Marc いわく「これがないとドキュメントが化石化する」。
>
> **D-024** ── Marc の `_TEMPLATE/CLAUDE.md` パターンを採用して、**`brand/fambox/CLAUDE.md`** を本日作成。これが Step 2 で非デザイナーが入ってくる時の起点になります。Marc 予言：「Q1 2027 前に作っておけば膨大な時間が節約できる」。
>
> **D-025** ── Marc が repo へのコラボ招待をくれました。受諾しました。Archeco の最新仕様を直接見られるようになります。
>
> Marc 側も今週 v7.32〜v7.37 をリリースしていて、私と稲井さんの仕事から複数の影響を受けたと書いてくれました。
>
> Marc いわく ──「3つのシステムが、**異なる問題を解いているが、同じ challenge を中心に進化している ── decisions explicit and transmissible（決定を明示化・伝達可能化）にすること**」。これが peer ネットワークの本質だと思います。

### スライド

```
┌─────────────────────────────────────────────────┐
│ Marc 即時フィードバック → 全部反映済             │
│                                                 │
│ Marc validate:                                  │
│  ✅ Brand/Engine/Data 分離                       │
│  ✅ D-NNN 意思決定ログ                            │
│  ✅ bugs.md = "the real Learn loop"             │
│                                                 │
│ Marc 提案 → 採用:                                │
│  D-021 AI/Human をカテゴリベース                 │
│  D-022 Learn 層を Step 1 から保護                │
│  D-023 DNA Evolution Triggers                  │
│  D-024 brand/fambox/CLAUDE.md 作成済            │
│  D-025 Marc コラボ受諾                           │
└─────────────────────────────────────────────────┘
```

### 3つのシステムの reframe（Marc から）

```
宮川 → infrastructure for scaling a team
稲井 → brand fidelity across distributed production
Marc → multi-surface production speed and consistency

共通の challenge:
  making decisions explicit and transmissible
```

---

## 4. ポジショニング + 3段階モデル（3分）

### 話す内容

> 私の目指すポジションは **Middle & Fast** です。
>
> Marc は **Wide & Fast** ── 多サービスに浅く広く、高速でプロトタイプを作る。
> 私は **Middle & Fast** ── FAM のような関連ブランド群に深く、ただし速い。
>
> 両者は得意領域が違うだけで、目標は同じ。Marc から環境とプロンプト技術を学んで、左側用に翻訳します。
>
> **3段階モデル**は須藤さんの提案を採用しました。
>
> - **Step 1** ── 私個人のインフラ完成。10倍速で作れる状態。2026年7月目標。
> - **Step 2** ── 須藤さん・松浦さん・三宅さん・マレル・安原さんが Slack で指示書を書くと、数時間で初稿が返る。2026年10月目標。
> - **Step 3** ── 誰でも使える状態 = Flywheel MVP 完成。2027 Q1 目標。
>
> 須藤さんの大事な言葉：**「3段階目から始めない」**。Step 1 から積み上げます。今週は Step 1 のスタート地点です。

### スライド

```
┌──────────────────────────────────────────────┐
│ ポジショニング: Middle & Fast                 │
│                                              │
│  Marc:  Wide & Fast  (多サービス・浅く)       │
│  宮川:  Middle & Fast (FAM 群・深く・速く)   │
│                                              │
├──────────────────────────────────────────────┤
│ 3段階モデル                                   │
│                                              │
│  Step 1 (〜2026-07) 私個人インフラ 10倍速     │
│       ↓                                      │
│  Step 2 (〜2026-10) 指示書ドライブ運用        │
│       ↓                                      │
│  Step 3 (〜2027-Q1) 誰でも使える = MVP        │
│                                              │
│  「3段階目から始めない」(須藤)                │
└──────────────────────────────────────────────┘
```

---

## 5. Week 2 コミット（2分）

### 話す内容

> 来週は **実案件着手** の週です。3つコミットします。
>
> **1つ目** ── Marc からの repo invite を待ちつつ、Archeco の最新仕様を読み込みます。特に `_TEMPLATE/CLAUDE.md` と Surfaces 概念。これを FAMBOX 用にさらに進化させます。
>
> **2つ目** ── 法人ページ 1セクションを AI パイプラインで作ります。松浦さんと相談してセクション選定。AI で初稿生成、**制作時間を Before/After で計測**します。
>
> **3つ目** ── 来週金曜の事業開発で Before/After 報告します。「○時間 → ○時間に短縮」の実例を見せます。
>
> もし来週中に、須藤さんか松浦さんから「これ作って」と Slack で投げてもらえれば、それが **Step 2 試作の起点** になります。

### スライド

```
┌──────────────────────────────────────────────┐
│ Week 2 コミット (2026-06-01 〜 2026-06-05)    │
│                                              │
│  月  Marc Archeco repo を読み込む             │
│      (Surfaces / _TEMPLATE/CLAUDE.md)         │
│                                              │
│  火-木  法人ページ 1セクション制作            │
│         (AI パイプライン / 時間ログ)          │
│                                              │
│  金  Before/After 報告                       │
│                                              │
│  ※ Slack で「これ作って」依頼があれば         │
│     Step 2 試作の起点に                       │
└──────────────────────────────────────────────┘
```

---

## 6. 質疑応答用の備え（5分）

### Q1: 「マレルチームは結局どこで関わる？」

> マレルは Step 3、2026年10月以降からの対象です。マレル自身が既に SNS・動画コンテンツで自走しているので、私と須藤さん・松浦さんのループが回ってから接続します。早く接続しすぎると仕組みが未完成で混乱します。

### Q2: 「3段階モデル、本当に2027 Q1 で完成する？」

> 正直、Step 1 が 2026年7月に完成できるかが鍵です。週次マイクロデリバラブルで進めるので、4週間ごとに軌道修正できます。遅れる場合は、Step 1 を伸ばして Step 2-3 を圧縮するか、スコープを縮める判断をします。ウォーターフォール型の硬直は避けられる設計です。

### Q3: 「Marc と被るんじゃない？」

> ポジショニングが違います。Marc は Wide & Fast、私は Middle & Fast。Marc は ARCHECO の右側、私は左側。peer として情報交換するので、被るのではなく **二輪化** します。共通インフラは共有して、ブランド固有データだけ別管理にします。

### Q4: 「英語の壁、本当に問題ないの？」

> Slack ベースなので、Claude で翻訳しながら書けます。対面英語の即時性は不要。文書化された議論なら、私のほうが深く考えられます。Marc とのキャッチボールの議事録も日本語に翻訳して残します。

### Q5: 「Tier 1 cleanup ブランチはどうなる？」

> `feat/materials-tier1-cleanup` に保管済み。Flywheel が落ち着いたら戻って完了させます。今は Flywheel の方が事業インパクトが大きいので優先します。

### Q6: 「これ、いつ収益化される？」

> MVP の外側の議論です。Step 3 完成、2027 Q1 後にマルチブランド展開で他案件にも適用可能になります。ARCHECO 全体のデザイン生産性 10倍化 = 案件数増 = 収益増、というロジック。今は MVP 完成を最優先で、収益化計画は後段で詰めます。

### Q7 ★新規: 「Learn 層を Step 1 から保護、具体的に何をする？」

> 3つです。
> 1. **Generate で失敗が出るたびに bugs.md に候補エントリ追加**
> 2. **同じ修正を2回説明したら、即ルール化**（Marc の M2 原則）
> 3. **bugs.md の追加件数を月1回可視化**して、停滞を検知
>
> さらに、**この金曜事業開発の「今週の Learn 進捗」を恒久発表項目** にします。

### Q8 ★新規: 「`brand/fambox/CLAUDE.md` って何が書いてある？」

> 1ファイルで FAMBOX のすべての判断基準を集約した、**Step 2 で非デザイナーが最初に読む単一ファイル** です。Marc の `_TEMPLATE/CLAUDE.md` 構造を参考に、本日 v0.1 → v0.2 に強化済（**591行 / 11セクション**）。
>
> 主要セクション：
> - **🚀 Quick Orientation**（5分オリエンテーション + 30秒サマリ + 5ステップ手順）
> - **Identity**（ブランドの中核 + 「らしい / らしくない」見分け方）
> - **Surfaces**（9種類の出力面 + Surface 別の典型ワークフロー 6件）
> - **Hard Rules**（絶対守るルール、**「ルール + 反例」ペアリング** で記述）
> - **AI/Human Boundary**（4カテゴリ + **「declining = re-declaring」実例3件**）
> - **Vocabulary**（重要用語）
> - **Exclusions**（過去の失敗を **具体例 A〜H** で記述）
> - **Learn Loop**（Step 1 から保護する仕組み）
> - **Onboarding Flow**（新メンバーの最初の30分、5フェーズ + 完了判定7項目）
> - **Decision Log Pointer**（DECISIONS.md への参照）
> - **テンプレ集**（持ってこい資料 / Good-Bad コピー対比 / boundary 宣言 / Friday Learn 進捗）
>
> Marc のコメント「Q1 2027 前に作っておけば膨大な時間が節約できる」を受けて、当初 Step 2 開始前（2026-09）目標だった v1.0 への進化を前倒し中。**Step 2 開始前に v1.0 確定**。

### Q9 ★新規: 「peer ネットワーク、実際の運用はどうなる？」

> Slack ベースの asynchronous + as-needed です。
> - 詳細質問は手を動かす過程で都度
> - 重要な学びは DECISIONS.md に追加
> - 議事録は sessions/ に蓄積
> - 月1回くらい、レベル合わせのまとめ会も検討
>
> Marc 達のチーム会（毎週金曜の発表）への留学も、過激ですが選択肢にあります。

---

## 発表前のセルフレビュー

発表前に以下をチェック：

- [ ] 各パートを声に出して読んで、時間配分を確認（特にセクション3が3分以内に収まるか）
- [ ] Marc が出る場合、英語サマリ（最初の30秒）を準備
- [ ] スライド共有方法を確認（PPTX か README + DECISIONS を画面共有）
- [ ] 「Learn 層保護」「カテゴリベース境界」「Evolution Triggers」「CLAUDE.md」が説明できる
- [ ] 緊張感を保つ：「手ぶらでは行けない」の精神を体現

### 当日の流れ（簡易リハーサル）

```
1. オープニング (1:00)
   "本日の発表、FAMBOX Design Flywheel ..."
2. (Marc いれば) 英語サマリ (0:30)
   "Quick context for Marc — ..."
3. Week 1 成果 (2:00)
4. Marc peer 関係 (3:00) ★メイン
5. ポジショニング + 3段階 (3:00)
6. Week 2 コミット (2:00)
7. 質疑 (5:00)
```

---

## 発表後にやること

- [ ] フィードバックを `sessions/2026-05-30-business-dev-review.md` に記録
- [ ] 質疑で出た新しい問いを `OPEN_QUESTIONS.md` に追加
- [ ] 重要な決定は DECISIONS.md に D-026 以降として追加
- [ ] Week 2 計画を PROGRESS.md に反映（フィードバックを受けて調整）

---

## 補足：必要なら参照する資料

発表時に画面共有や添付で使える資料：

| 資料 | 用途 |
|---|---|
| [README.md](./README.md) | プロジェクト全体像 |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 4層構造の図 |
| [DECISIONS.md](./DECISIONS.md) | 意思決定 D-001〜D-025 |
| [PROGRESS.md](./PROGRESS.md) | 週次進捗 |
| [environment-audit-v0.1.md](./environment-audit-v0.1.md) | 現環境スナップショット |
| [../../brand/fambox/CLAUDE.md](../../../brand/fambox/CLAUDE.md) | FAMBOX Project CLAUDE.md（D-024 で作成）|
| [../../brand/fambox/brand-dna/current.md](../../../brand/fambox/brand-dna/current.md) | Brand DNA v1.0 + Evolution Triggers |
| [../../brand/fambox/design-system/bugs.md](../../../brand/fambox/design-system/bugs.md) | bugs.md（Marc 最重要視）|
| [sessions/2026-05-26-marc-firstreply-exchange.md](./sessions/2026-05-26-marc-firstreply-exchange.md) | Marc 初回 reply 議事録 |
| [sessions/2026-05-28-marc-secondreply-exchange.md](./sessions/2026-05-28-marc-secondreply-exchange.md) | Marc 2回目 reply 議事録 |

---

## バージョン履歴

| 版 | 日付 | 内容 |
|---|---|---|
| v1 | 2026-05-26 | 初稿。発表構成、各パート + Q&A 6件 |
| v2 | 2026-05-28 | **voice-ready 化** + Marc 2nd reply 反映 + Q7-9 追加 + Section 3 を「Marc との peer 関係」に昇格 |
