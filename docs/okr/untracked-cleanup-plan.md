---
title: Untracked ファイル整理計画 — .gitignore 戦略ドラフト
date: 2026-05-25
status: draft
owner: 宮川
purpose: 9,561 個の untracked ファイル / 約 4.5GB を整理し、repo 取込・個人領域・除外の 3 区分に整理する
implementation: 別セッションで段階実行（本ファイルは方針書）
related:
  - ../../.gitignore
  - ../../brain/README.md
  - 本セッション commit 5ab01dd (brain hybrid 取込)
---

# Untracked ファイル整理計画

## 1. 現状

| 指標 | 値 |
|---|---|
| Untracked ファイル数 | **9,561** |
| Top-level 配下総サイズ（概算） | **4.5 GB+** |
| 主因 | `reference/` 3.0GB + `tools/fam-reel-pdca` 301M + `tools/liquid-pipeline` 162M + `scripts/x_bookmark` 157M（node_modules / 撮影素材） |

## 2. 整理方針 — 3 区分

### カテゴリ A: 絶対 .gitignore（機密 / 巨大 / 一時ファイル）

| パターン | 理由 |
|---|---|
| `*.rtf` | 個人ノート系（API Key.rtf / Claude コマンド.rtf / Google Cloud Console のサービスアカウント.rtf）→ **機密含むので絶対 push 不可** |
| `reference/` | 3.0GB（外部参考素材・動画）→ Git LFS 対象外でも巨大すぎ |
| `clients/` | 撮影素材 MP4 / クライアント機密情報 |
| `*.mp4`, `*.MP4`, `*.mov`, `*.MOV` | 動画ファイル全般（既に *.MOV / *.mov は ignore 済、追加） |
| `~$*` | Office 一時ファイル（~$brandwork_04.pptx 等） |
| `*_backup_*.xlsx`, `*_backup_*` | バックアップファイル（OKR.xlsx の v6.6/v6.7/v6.8/v6.9 等） |
| `*.zip` | ZIP アーカイブ（中身が個別ファイルとして既にある可能性） |
| `**/node_modules/` | Node.js 依存（既に gitignore グローバルにある想定だが明示） |
| `**/__pycache__/` | Python キャッシュ |
| `**/*.pyc` | Python コンパイル済 |
| `**/.DS_Store` | macOS メタデータ（既に gitignore 済） |
| `**/logs/` | 動的生成ログ |
| `**/dist/`, `**/build/` | ビルド成果物 |
| ルート直下 `スクリーンショット *.png` | スクショ作業残骸 |

### カテゴリ B: repo 取込推奨（業務再利用される）

| パス | サイズ | 内容 |
|---|---|---|
| `brand/fam/` | (小) | FAM 親ブランド資料 |
| `brand/fambox/STRATEGY.md` | (小) | 「入口の支配 × 出口の独占」戦略フレーム |
| `brand/fambox/brand-dna/` | (中) | DNA v0.7 + ADR-011〜026 詳細 |
| `brand/fambox/design-system/bugs.md` | (小) | 28 エントリの規律源 |
| `brand/fambox/design-system/operations/audit-first-protocol.md` | (小) | 新規追加前プロトコル |
| `brand/fambox/design-system/operations/promotion-rule.md` | (小) | ad-hoc → 正式ルール昇格基準 |
| `brand/fambox/animation-library-v0.1.md` | (小) | Animation Library v0.1 |
| `brand/fambox/prototypes/` | (中) | DS prototypes |
| `brand/shared/` | (小) | 共有ブランド資料 |
| `docs/mcp/` | (小) | MCP 採用計画 v0.3 |
| `docs/proposals/` | (中) | 提案資料 |
| `docs/ux/` | (中) | UX 設計資料 |
| `docs/setup-git-hooks.md` | (小) | Git Hooks 設定手順 |
| `docs/okr/FAMBOX_DS_*.md` 等 | (小) | DS 設計ドキュメント |
| `docs/okr/references/` | (中) | LLMo / Linear / Vercel / Arc リファレンス |
| `docs/okr/_archive/` | (中) | 過去 OKR / 提案アーカイブ |
| `scripts/fambox-new-section` | 16K | audit-first 強制スクリプト |
| `scripts/templates/` | 12K | section.liquid + component.md テンプレ |
| `tools/audit/` | 56K | liquid-section-lint.sh 等 |
| `tools/dashboard/` | 28K | ダッシュボード |
| `tools/git-hooks/` | (小) | Git hooks |
| `tools/maintenance/` | (小) | メンテツール |
| `tools/memory/` | 120K | memory システム関連 |
| `prototypes/` | 356K | UI prototypes |
| `preview/` | 344K | プレビュー HTML |
| `projects/fambox/sections/` | 118 ファイル | Shopify テーマ section（本番反映済 Liquid）|
| `projects/fambox/snippets/` | (中) | テーマ snippets |
| `projects/fambox/layout/` | (小) | テーマ layout |
| `projects/fambox/templates/` | (小) | テーマ templates |
| `projects/fambox/config/` | (小) | テーマ config |
| `projects/fambox/assets/` | (中) | テーマ assets |
| `projects/fambox/data/` | (小) | テーマ data |
| `projects/fambox/locales/` | (小) | i18n |
| `projects/fam/sections/`, `templates/`, `wireframe.html` | (中) | FAM EC テーマ |
| `projects/食事診断/` | (中) | 食事診断プロトタイプ |
| `projects/花かがみ/` | (中) | 花かがみ案件 |
| `tasks/` | 8K | タスク管理 |
| `.github/` | (小) | GitHub Actions / templates |

### カテゴリ C: 重量物除外して中身だけ取込（条件付き）

| パス | 全体サイズ | 取込対象 | 除外対象 |
|---|---|---|---|
| `tools/fam-reel-pdca` | 301M | ソースコード | node_modules / dist |
| `tools/liquid-pipeline` | 162M | ソースコード | node_modules / dist |
| `scripts/x_bookmark` | 157M | スクリプト本体 | output / harvest log（個人領域）|
| `projects/analytics/` | (重) | Python ソースのみ | __pycache__ / logs / *.plist / *.json (token) |
| `output/` | 3.3M | スクリプト出力先 → **全除外**（生成物は git 不要）| 全体 |

### カテゴリ D: 判断保留（ユーザー意向次第）

| パス | 候補 |
|---|---|
| ルート直下のロゴ (LMLT_*.png/svg) | `brand/shared/logos/` に **移動**してから取込 |
| `brandwork_04.pptx` | Excel/PPT は repo 価値低い → 除外推奨 |
| `UIUX改修タスク管理表.xlsx` | tasks/ に移動か除外 |
| `TSTech_Brand Manual_240208.pdf` | brand/parent/ に移動か個人領域 |
| `~$brandwork_04.pptx` | 一時ファイル → 必ず除外 |
| `preview-whitespace-animations.html` | preview/ に移動か除外 |
| ルート直下のスクショ 3 個 | 個人領域へ移動 |

## 3. 実行手順案（別セッション）

### Phase 0: バックアップ確認
- [ ] 重要な個人ノート（API Key.rtf 等）を `~/Documents/_personal/` 等に退避
- [ ] reference/ や clients/ の機密素材を別ドライブ / iCloud に退避（必要なら）

### Phase 1: .gitignore 更新（破壊的変更なし）
- [ ] カテゴリ A のパターンを .gitignore に追加
- [ ] カテゴリ C の subdir パターン (node_modules / dist / logs / __pycache__) を追加
- [ ] git status で untracked が劇的に減ることを確認

### Phase 2: 機密ファイル隔離（重要）
- [ ] `API Key.rtf` → `~/Documents/_personal/API Key.rtf` に **移動**（コピーではなく）
- [ ] `Google Cloud Console のサービスアカウント.rtf` → 同上
- [ ] 確認: ルート直下から .rtf が消えていること

### Phase 3: カテゴリ B 段階取込（分割コミット推奨）
1. `brand/` 配下 → 1 コミット（DS 拡張）
2. `docs/mcp/`, `docs/proposals/`, `docs/ux/` → 1 コミット（docs 拡張）
3. `scripts/`, `tools/audit/`, `tools/dashboard/`, `tools/memory/` → 1 コミット（運用ツール）
4. `projects/fambox/sections/` 118 ファイル → 1 コミット（Shopify テーマ本体）
5. `projects/fambox/snippets/`, `templates/`, `layout/`, `config/`, `assets/` → 1 コミット
6. `projects/fam/`, `projects/食事診断/`, `projects/花かがみ/` → 1 コミット
7. `prototypes/`, `preview/`, `tasks/`, `.github/` → 1 コミット

### Phase 4: カテゴリ D 移動と判定
- [ ] ロゴ画像を `brand/shared/logos/` に移動
- [ ] PPTX を `docs/_materials/` 等に移動 or 除外判定
- [ ] スクショは個人領域に移動

### Phase 5: 最終確認
- [ ] `git status` で意図しない untracked が残っていないか確認
- [ ] `git ls-files` で取込ファイル数を確認
- [ ] Repo サイズが妥当（500MB 以下推奨）か確認

## 4. リスク評価

| リスク | 緩和策 |
|---|---|
| 機密ファイル誤 push | Phase 2 を Phase 3 より**前**に必ず実施 / push 前に `git diff --stat` で名前確認 |
| 巨大ファイル混入で push 失敗 | Phase 1 の .gitignore 追加で node_modules 等を確実に除外 / `git ls-files \| xargs du -h \| sort -hr \| head` で push 前確認 |
| Shopify テーマファイル取込 → Git 履歴が肥大化 | 118 ファイル分は `feat(theme): import full fambox Shopify theme` の 1 コミットに集約 |
| 個人ノートが repo に流出 | Phase 2 の隔離を厳格に / カテゴリ A の `*.rtf` パターンで二重防御 |

## 5. 推定効果

- Untracked **9,561 → 0-50** (ignore された個人領域のみ残る)
- Repo 取込ファイル: 推定 **300-500 ファイル追加**
- Repo サイズ: 取込後でも数十 MB 程度（巨大物は除外）
- ローカル `git status` の応答性が劇的に改善

## 6. 次セッションでの起動コマンド案

```bash
cd /Users/archecoinc./Desktop/Claude_1
# Phase 1: .gitignore 更新
# Phase 2: 機密ファイル隔離（mv 操作）
# Phase 3: 段階コミット（上記 7 段階）
```

別セッションで本ファイルを最初に Read してから Phase 0 → 5 を順次実行する。

---

## 出典

- 本計画書は 2026-05-25 セッション（OS アップデート復旧）の Step 6 で策定
- 関連 commit: 5ab01dd (brain hybrid 取込), 56590e7 (cool-leavitt spec 救出)
- 関連 brain ノート: [fambox-shipping-sla.md](../../brain/50_Business_Context/fambox-shipping-sla.md) / [flex-overflow-scrollbar-rightpad.md](../../brain/30_Tech_Notes/flex-overflow-scrollbar-rightpad.md)
