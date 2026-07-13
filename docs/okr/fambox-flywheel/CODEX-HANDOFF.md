# FAMBOX Design Flywheel — Codex 引き継ぎ手順書 v1.0

> 作成：2026-06-09 / 目的：Claude Code で構築した FAMBOX Design Flywheel の全資産を **OpenAI Codex CLI** 側でも同等に使えるようにする手順。
> 方針：**非破壊・段階適用**。リポジトリ内ファイルはコピー不要（共有）。`~/.codex` 配下への書込はハーネス自己改変扱いのため **/tmp 経由＋cp で承認制**。

---

## 0. TL;DR（最重要・3行）
1. Flywheel の中核知識は**リポジトリ内ファイル**。Codex を同じフォルダ `Claude_1/` で起動すれば**移行作業ゼロで読める**。
2. 本当に引き継ぐのは「配線」だけ＝**①スキル設置 ②メモリ移植 ③AGENTS.md ルーター**（自動発火の代替）。
3. MCP（Figma/figma-bridge/iconify/lottie/notion）は Codex に**設定済み**。追加が要るのは Slack/Drive 等のみ。

---

## 1. Codex 側の現状（確認済み 2026-06-09）
| 機構 | Codex の受け皿 | 状態 |
|---|---|---|
| スキル | `~/.codex/skills/`（`skill-installer` 有・`.system` は予約） | 形式は Claude と同一（name/description frontmatter）。ユーザースキル未設置 |
| メモリ | `~/.codex/memories/`（MEMORY.md＋git管理） | 稼働中 |
| グローバル指示 | `~/.codex/AGENTS.md`（CLAUDE.md 相当・76行） | 稼働中 |
| MCP | `~/.codex/config.toml` | `figma / figma-bridge / iconify / lottie / notion` 設定済 |
| カスタムプロンプト | `~/.codex/prompts/`（slash command 相当） | **未作成**（コマンド移行時に作る） |

---

## 2. 引き継ぎ対象と方法（4 Tier）

### Tier 0 — リポジトリ知識（コピー不要・最優先）
同じリポジトリ `Claude_1/` を Codex の作業ディレクトリにすれば、以下はそのまま読める。**移行不要**。
- `brand/fambox/design-system/bugs.md`（DOCTRINE/PROC）
- `.claude/skills/fambox-flyer-builder/`（SKILL.md＋references 3本：build-playbook / taste-and-tokens / asset-index）
- `docs/okr/fambox-flywheel/`（projects/flyer-packaging の PRINT-DESIGN-DNA / TEMPLATE / 検証ログ、asset-library/MANIFEST.md、weekly-declarations）
- `Asset/`（索引 v3 でリネーム済の実写真）

→ **やること：Codex をこのフォルダで起動するだけ。** 残り Tier は「自動で読ませる／メモリに持たせる」ための配線。

### Tier 1 — スキル設置（`~/.codex/skills/`）
Codex はスキルを**自動発火しない**が、設置すれば `skill-installer` 経由や AGENTS.md ルーターから呼べる。SKILL.md 形式はほぼ同一（`Claude's capabilities`→`Codex's capabilities` の文言差のみ）。

対象（Flywheel コア）：
- `fambox-flyer-builder`（印刷物・今回の主役）
- `fambox-design`（FAM BOX 視覚言語・UI）
- 任意で：`fambox-diagnosis-builder` / `fambox-blog-publisher` / `seal-email-builder` / `section-refactor-helper` / `token-integrity-fixer`

手順（承認制・/tmp 経由）：
```bash
# 1) 配布物を /tmp に組み立て（リポジトリから読み取りのみ）
mkdir -p /tmp/codex-flywheel/skills
cp -R "/Users/archecoinc./Desktop/Claude_1/.claude/skills/fambox-flyer-builder" /tmp/codex-flywheel/skills/
cp -R "/Users/archecoinc./Desktop/Claude_1/.claude/skills/fambox-design"        /tmp/codex-flywheel/skills/
# 2) frontmatter の文言を Codex 向けに微修正（任意・description の "Claude" 表現等）
# 3) 宮川さん承認後、~/.codex/skills/ へ配置
cp -R /tmp/codex-flywheel/skills/fambox-flyer-builder ~/.codex/skills/
cp -R /tmp/codex-flywheel/skills/fambox-design        ~/.codex/skills/
```
注意：references 内の**絶対パス**（`/Users/archecoinc./Desktop/Claude_1/...`）はそのまま有効（同一マシン）。リポジトリ相対で書かれた箇所は Codex の作業ディレクトリ基準で解決される。

### Tier 2 — メモリ移植（`~/.codex/memories/`）
Flywheel 関連の Claude memory を Codex memory に取り込む。Codex の `memories/` は git 管理なので追記して commit。

対象 memory（`~/.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/`）：
- `project_fambox_flywheel.md`（Flywheel 全体構造・Phase）
- `project_fambox_flyer_builder_2026-06-08.md`（チラシ仕組み化・索引v3・本日の学び）
- `project_fambox_dna_v1.0_promotion_2026-05-27.md`（DNA v1.0）
- `project_references_findings.md` / `project_references_subline.md`（外部リファレンス規律）
- 関連 feedback：`feedback_figma_bridge_text_limitations` / `feedback_fam_typography` / `feedback_visual_design_video_first` / `feedback_shopify_liquid_specificity` / `feedback_design_system_liquid_patterns`

手順（要約を MEMORY.md に index、本文は memories/ へ）：
```bash
mkdir -p /tmp/codex-flywheel/memories
cp "/Users/archecoinc./.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_fambox_flywheel.md" /tmp/codex-flywheel/memories/
cp "/Users/archecoinc./.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_fambox_flyer_builder_2026-06-08.md" /tmp/codex-flywheel/memories/
# …（上記対象を順次）。承認後 ~/.codex/memories/ へ cp → MEMORY.md に1行 index 追記 → git -C ~/.codex/memories add/commit
```
※ Claude 固有の frontmatter（node_type 等）は Codex で無害だが、必要なら除去。

### Tier 3 — AGENTS.md ルーター（自動発火の代替・最重要配線）
Claude の「キーワードで Skill 起動」を Codex で再現する核。草案を用意済み：
- `docs/okr/fambox-flywheel/codex/AGENTS.flywheel-router.md`

適用先の選択：
- (A) **リポジトリルート `Claude_1/AGENTS.md`**（このフォルダで Codex 起動時に自動読込）＝Flywheel 専用に最適・非ハーネス改変。**推奨**。
- (B) `~/.codex/AGENTS.md` 末尾に追記（全プロジェクト共通・要承認制書込）。

```bash
# (A) 推奨：リポジトリルートに設置（git 管理に乗る）
cp "docs/okr/fambox-flywheel/codex/AGENTS.flywheel-router.md" "/Users/archecoinc./Desktop/Claude_1/AGENTS.md"
# （既存 AGENTS.md があれば追記でマージ。CLAUDE.md とは別ファイルとして共存可）
```

### Tier 4 —（任意）コマンド／フック
- `.claude/commands/`（8本）→ `~/.codex/prompts/` を作成し markdown を配置（slash command 相当）。Flywheel 必須ではない。
- `.claude/hooks/`（6本）：**pre-commit / GitHub Actions（audit.yml）は git レベル＝ハーネス非依存**で既に有効。Codex 固有のツールフックは別途要検討（Liquid 構文チェック等）。AI 自己監視系ルールは Tier 3 ルーターに内包済。

---

## 3. MCP の状況
| サーバ | Codex 設定 | 用途 |
|---|---|---|
| figma（公式） | ✅ 済 | upload_assets / get_screenshot / get_metadata（チラシ画像配置・検証） |
| figma-bridge | ✅ 済 | 構造組立（要 Connect→join_channel） |
| iconify / lottie | ✅ 済 | アイコン / モーション |
| notion | ✅ 済 | ドキュメント |
| Slack / Drive / Gmail / Calendar / Chrome | ❌ 未 | 共有・素材・配信が要るとき追加 |

→ Flywheel の制作系（Figma/icon/lottie）は**そのまま使える**。Slack 共有まで Codex で完結させたい場合のみ追加設定。

---

## 4. 既知の差分（Claude → Codex で変わる挙動）
1. **スキル自動発火なし** → AGENTS.md ルーター（Tier 3）で「この入力ならこのファイルを読む」を明示。これが最重要。
2. **自動メモリ読込の差** → Codex は MEMORY.md を参照。セッション開始時に何を読むかを AGENTS.md にも明記しておく。
3. **フックの差** → git レベル（pre-commit/Actions）は共通で生きる。ツールフックは要移植。
4. **絶対パス依存** → 同一 Mac なら有効。別マシンに移すときはパス置換が必要。

---

## 5. 検証チェックリスト（適用後）
- [ ] Codex を `Claude_1/` で起動し、`bugs.md` / `asset-index.md` を読めるか
- [ ] 「FAMBOX チラシ作って」で AGENTS.md ルーターが SKILL.md＋references＋bugs.md を読みに行くか
- [ ] Figma MCP で `get_metadata`/`upload_assets` が動くか（今回 Claude 側で実証済の手順がそのまま通るか）
- [ ] `~/.codex/skills/fambox-flyer-builder` が認識されるか（skill-installer / 一覧）
- [ ] メモリに Flywheel index が出るか
- [ ] 成長ループ：Codex で得た学びを `bugs.md` / references に書き戻せるか（双方向同期）

---

## 6. 推奨実行順（最小で動かす）
1. **Tier 0**：Codex を `Claude_1/` で起動（即・無コスト）
2. **Tier 3(A)**：リポジトリルート `AGENTS.md` にルーター設置（git 管理・非破壊）← これだけで実用レベル
3. **Tier 1**：`fambox-flyer-builder` を `~/.codex/skills/` へ（承認制）
4. **Tier 2**：Flywheel memory を移植（承認制）
5. 必要に応じ Tier 4 / Slack MCP

> Tier 0＋3 だけで「Codex が同じ知識を同じ規律で使う」状態になる。Tier 1/2 は自動発火と記憶の質を上げる強化。
