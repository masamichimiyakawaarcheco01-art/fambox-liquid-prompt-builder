---
title: FAMBOX DS — bugs.md（過去に踏んだ罠・strict rule 候補・運用ルール集約）
type: design-system
brand: fambox
version: 0.1
status: current
last_updated: 2026-05-21
owner: 宮川
purpose: 散在する 13 個の feedback memory を統合し、Claude が session start で参照可能な構造的ナレッジに変換。BUG（過去に踏んだ罠）/ DOCTRINE（strict rule 候補）/ PROCESS（運用ルール）の 3 カテゴリで番号付き管理。
credit: Marc-Antoine Lecat (Archeco kit v7.14) の bugs.md 構造を参考に FAMBOX 構造へ適応
related:
  - operations/audit-first-protocol.md
  - operations/promotion-rule.md
  - operations/lastmile-playbook.md
  - operations/naming-convention.md
  - ../current.md
---

# FAMBOX DS — bugs.md

## 0. 目的と運用

### 0-1. なぜ bugs.md か

> "散在する feedback memory は『次回 Claude が同じ罠を踏まないため』の知識だが、memory 配下に散らばっていると **新セッションで参照されにくい**。design-system 配下に集約することで、session start の Brand sources 宣言（audit-first-protocol.md §7）と同じ経路で読まれる。"

### 0-2. 3 カテゴリの責務分担

| カテゴリ | 内容 | 昇格先 |
|---|---|---|
| **BUG** | 過去に踏んだ具体的な罠（Shopify Liquid / Tokens / Claude 運用 / Theme 干渉）| 解消されない限り **bugs.md 永住** |
| **DOCTRINE** | strict rule 候補（Typography / Anti-pattern / Specificity 戦略 等）| DNA v1.0 確定後（2026-06-30 予定）に `principles/doctrine.md` へ昇格 |
| **PROCESS** | 運用ルール（Audit-first / 3 回失敗 / 検証規律 等）| すでに operations/ に昇格済のものは出自記録、未昇格のものは promotion-rule.md §1-C で判定 |

### 0-3. 既存資産との関係

| 既存資産 | 本書との関係 |
|---|---|
| `operations/audit-first-protocol.md` | PROC-001 が出自記録として参照（昇格済正規ルール）|
| `operations/promotion-rule.md` | DOCTRINE / PROCESS の昇格判定基準を提供 |
| `operations/lastmile-playbook.md` | CORRECTION-XXX と本書 BUG-XXX は別物（前者は AI 生成残 5% 補正、後者は Claude 作業時の罠）|
| `principles/doctrine.md`（未整備 / 2026-06-30 予定）| DOCTRINE-001〜005 の正式昇格先 |

### 0-4. 参照タイミング

- **session start**: Brand sources 宣言（audit-first-protocol.md §7）と同列で本書を Component sources / Spec sources の **横位**として読む
- **「変化なし」報告受信時**: BUG-001〜004（Shopify Liquid 罠）を最優先で確認
- **新規 Liquid 提案前**: PROC-001（Audit-first）+ PROC-009（WF→Liquid サイクル）+ DOCTRINE-001〜005 を確認
- **Token 引用時**: PROC-006 + BUG-009 を確認
- **Reviewer 指摘受信時**: PROC-007 + BUG-010 を確認

---

## 1. BUG（過去に踏んだ罠）

過去に実際に発生し、複数回繰り返した／重大インシデント化した罠を番号付きで集約。**新規 BUG は番号を増やす（既存番号を改変しない）**。

### Shopify Liquid（4）

#### BUG-001: inline `style="..."` 優先で外部 CSS が効かない
- **症状**: 外部 CSS や Liquid 内 `<style>` で `!important` を付けても変化なし
- **原因**: Liquid section の HTML タグに `<element style="...">` が直接書かれていると CSS specificity 1000 で常勝
- **検出**: `grep -nE 'style="[^"]+"' projects/fam[box]?/sections/{section}.liquid`
- **対処**: inline style を削除して CSS に集約、または最新値に書き換え
- **関連**: DOCTRINE-004（Specificity 3 層戦略）
- **出自**: feedback_shopify_liquid_specificity §1

#### BUG-002: richtext 型 Schema + `<p>` コンテナで HTML 破綻
- **症状**: richtext 型設定の出力テキストにスタイルが効かない、サイズが効かない
- **原因**: richtext は `<p>...</p>` で自動ラップされる。これを外側 `<p>` で囲むとブラウザが `<p>` 内 `<p>` を不正と判定し外側 `<p>` を強制クローズ → 内側 `<p>` がスタイル継承しない
- **検出**: `curl -s {prod_url} -L | grep -A2 "{class_name}"` で `<p>` 内 `<p>` を確認
- **対処**:
  1. 外側を `<p>` → `<div>` に変更（最推奨）
  2. Schema を `"type": "text"` に変更（plain text で良ければ）
  3. `{{ value | strip_html }}` で `<p>` タグ除去
- **関連**: DOCTRINE-005（Schema 型選択ガイドライン）
- **出自**: feedback_shopify_liquid_specificity §2 / feedback_design_system_liquid_patterns パターン 1-2

#### BUG-003: Shopify CDN / ブラウザキャッシュで反映遅延
- **症状**: Liquid 修正をデプロイしたが本番に反映されない
- **原因**: Shopify CDN キャッシュ / ブラウザキャッシュ / Service Worker
- **検出**: `curl -s "{prod_url}" -L | grep "{pattern}"` で本番 HTML を直接確認
- **対処**:
  1. Theme Customizer → 何も変更せず「保存」を再実行（CDN バスト）
  2. または section ファイル名を一度変える → 元に戻す（強制再デプロイ）
  3. DevTools → Network → 「Disable cache」をオンに
  4. Service Worker は Application タブから Unregister
- **関連**: PROC-010（Liquid 検証 3 段階）
- **出自**: feedback_shopify_liquid_specificity §3, §5

#### BUG-004: 公開中テーマ vs 下書きテーマの取り違え
- **症状**: 「下書きテーマ」を編集しているのに本番 URL を見て「変化なし」と判断
- **原因**: ページは **公開中のテーマ** でレンダリングされる。下書きテーマで更新しても本番には反映されない
- **検出**:
  - Shopify Admin → テーマ → 「**現在のテーマ**」のテーマ名を確認
  - Code Editor 上部タブのテーマ名を確認
  - 両者が一致しているかを必ず確認
- **対処**: 公開中テーマで作業する。下書きで作業した場合は明示してプレビュー URL（preview_theme_id 付き）で確認
- **関連**: PROC-010（Liquid 検証 3 段階）
- **出自**: feedback_shopify_liquid_specificity §4 / feedback_design_system_liquid_patterns パターン 5

### WF→Liquid 変換 / Theme 干渉（4）

#### BUG-005: WF と異なる CSS 手法で書き換えてレイアウト崩れ
- **症状**: スタンドアロン HTML の WF では正確だったレイアウトが、Liquid 変換後に崩れる
- **原因**: WF で使った CSS 手法（absolute positioning 等）を Liquid で勝手に padding 等に変えた
- **対処**: WF と **同じ HTML 構造・CSS 手法** で Liquid 化する。手法変更は禁止
- **関連**: PROC-009（WF→Liquid 必須サイクル）
- **出自**: feedback_liquid_workflow

#### BUG-006: SP メディアクエリでの PC 基本値残存
- **症状**: SP 表示でレイアウトが想定外（高さ潰れ / 幅潰れ等）
- **原因**: 「PC 基本値 → SP で上書き」のカスケードで **上書きされない PC 値**が残存
- **要注意プロパティ**:
  - `flex: 1` → SP で `flex: none` にリセット必須
  - `min-width: 0` → SP で `min-width: auto` にリセット必須
  - `max-width: 1440px` → SP で `max-width: none`
  - `width: 720px` → SP で `width: 100%`
  - `height: 224px` → SP で明示的に上書き
- **対処**: 「PC 基本値 + SP 上書き = 最終適用値」を要素ごとに算出してから WF と比較
- **関連**: PROC-009 / PROC-010
- **出自**: feedback_liquid_workflow §比較検証

#### BUG-007: Shopify テーマ CSS の干渉
- **症状**: 自セクションの CSS が想定通り動かない（空 div が消える / シャドウが切れる / フォント上書きされる等）
- **原因**: base.css 等のテーマ CSS が干渉
- **確認済み干渉パターン**:

| テーマ CSS | 影響 | 対策 |
|---|---|---|
| `div:empty { display: none }` | 空 div が消える | Liquid コメント挿入 |
| `.section + .section { margin-top }` | セクション間余白 | padding 使用 |
| `h1-h6 { font-family: var(...) }` | フォント上書き | `!important` |
| `.shopify-section { overflow: hidden }` | シャドウ / はみ出しが切れる | 内側 padding で余白確保（overflow 変更は親で効かない）|
| `a { text-decoration: underline }` | ボタンに下線 | `text-decoration: none !important` |
| `img { max-width: 100% }` | 画像サイズ崩れ | width/height 明示 |

- **対処**: CSS セレクタは必ず `#{{ sec_id }}` でスコープする
- **出自**: feedback_implementation_discipline §3

#### BUG-008: scroll-snap + padding/mask-image の互換性問題
- **症状**: SP 版横スクロールカルーセルでセンタリング / フェード / 初期位置が崩れる
- **失敗パターン（10 回以上失敗の最重大インシデント）**:
  - ❌ `padding: 0 calc(...)` + scroll-snap → 初期位置がスキップされる
  - ❌ `scroll-padding-left` + JS `scrollTo` → ブラウザ差異・タイミング問題
  - ❌ `mask-image` on scroll container → 初期位置カードにも mask が効く
  - ❌ absolute gradient + z-index → 全カードテキストに被る
- **成功パターン**:
  - ✅ `::before` / `::after` 疑似要素でダミースペース挿入 + `scroll-snap-align: center`
  - ✅ ダミー flex 要素（幅 = タブ幅 - gap）+ scroll-snap 無効(PC) + JS `scrollLeft=0` + 4 層 z-index 構造
- **レイヤー構造（4 層 z-index）**:
  - z-index 3: タブ（absolute、最上層）
  - z-index 2: グラデーション（absolute、タブ背景の延長）
  - z-index 1: メニューブロック（absolute、横スクロール）
  - z-index 0: 背景色（セクション自体）
- **教訓**: スクロールコンテナのセンタリング・フェードは padding ではなく **構造的要素**で行う
- **関連**: PROC-002（3 回失敗ルール）/ PROC-003（指示遵守）
- **出自**: feedback_implementation_discipline §4-5

### Tokens / Claude 運用（4）

#### BUG-009: spec/plan の Token 名と実在 Token の乖離
- **症状**: spec / plan で書いた `--xxx` Token が実装時に存在しない、または値が違う
- **発生事例**（Phase A・2026-05-19）:
  - plan の `--motion-duration-*` は実在しない（実在は `--duration-*`）
  - plan の `--motion-ease-base` は実在しない（実在は `--ease-out` / `--ease-in` / `--ease-in-out`）
  - spec §3 の `--fs-display: 28px` は実在 `56px`（stat-focus value）
- **原因**: spec は作る側の頭の中で命名整理されるが、実在 Token は de facto で進化（Session #43-#52 の Token 化マラソン）→ 必ず乖離する
- **対処**: spec / plan に Token 名を書く前に必ず `grep -E "^\s*--xxx" snippets/fambox-tokens.css.liquid` で実在検証
- **関連**: PROC-006（Token 名実機検証）/ PROC-001（Audit-first）
- **出自**: feedback_token_name_verification

#### BUG-010: Reviewer subagent の Token 値ハルシネーション
- **症状**: subagent-driven-development の review フェーズで reviewer が「値 X は間違い / Y であるべき」と主張するが、grep するとすべて文書側が正しい
- **発生事例**（Phase A Task 3・2026-05-19）:
  - `--duration-base: 250ms` → reviewer「実在は 300ms」← 実際は 250ms で正
  - `--duration-slow: 350ms` → reviewer「実在は 600ms」← 実際は 350ms
  - `--duration-breathing` → reviewer「実在は `--duration-breath`」← 実際は `--duration-breathing`
  - `--ease-in-out` → reviewer「実在は `--ease-inout`」← 実際はハイフンあり
  - `--space-0-5` → reviewer「不在」← line 157 に実在
  - `--border-light: rgba(...)` → reviewer「`#ECECEC` 単色」← 実際は rgba
- **原因**: code quality reviewer はパターン認識中心で記憶 / 推測ハルシネーション率が高い
- **対処**: reviewer の具体的な値 / 名前指摘は **すべて grep で裏取り**してから受け入れる
- **関連**: PROC-007（Reviewer 指摘の実機検証）
- **出自**: feedback_reviewer_hallucination_check

#### BUG-011: ファイル生成成功 ≠ 内容反映
- **症状**: Excel / Liquid / その他ファイルを「保存しました」と報告したが実際は更新されていない
- **原因**:
  - ファイルが他プロセスで開かれている
  - パーミッション / キャッシュ
  - Write を実行せずに完了報告（実装ミス）
- **対処**:
  1. 生成後に `ls -la` でタイムスタンプ + サイズ確認
  2. 内容を読み戻して期待値が反映されているか検証
  3. 検証結果（タイムスタンプ・行数・主要セル値）を **証拠付き**で報告
  4. 「保存しました」ではなく「保存し、以下を確認:」と書く
- **関連**: PROC-004（ファイル検証規律）
- **出自**: feedback_file_verification

#### BUG-012: `~/.claude/` 配下セルフモディファイ保護でブロック
- **症状**: `~/.claude/commands/` や `~/.claude/settings.json` への Write / Edit がセキュリティ保護で拒否される
- **原因**: Claude Code 自身の設定ファイルへの直接書き込みは設計上ブロックされる
- **対処**:
  1. `/tmp/` にファイルを書き出す（Write は `/tmp/` には使える）
  2. ユーザーにターミナルで `cp /tmp/{file} ~/.claude/{target}` を実行依頼
  3. heredoc はバッククォート含有時に shell が混乱 → `python3 -c` + `pathlib` が確実
  4. 書き込み後は必ず Read で確認
- **関連**: PROC-008（`~/.claude/` 変更ワークフロー）
- **出自**: feedback_claude_config_write

#### BUG-013: CLI / MCP / API コマンド構文の推測 → 存在しないサブコマンドを提示
- **症状**: Claude がユーザーに渡したコマンド (`claude mcp reauth <name>` 等) が「unknown command」エラーで失敗。ユーザーが何度も試行して時間浪費
- **原因**: Claude が `--help` 出力や公式 docs を確認せず、CLI / MCP / API のサブコマンド構文を **記憶 / 推測**で書いてしまう。特に Claude Code / Anthropic SDK / MCP 等の比較的新しいツールは記憶が不正確
- **発生事例**（2026-05-21）:
  - 提示: `claude mcp reauth slack` ← `reauth` サブコマンドは存在しない
  - 提示: `claude mcp remove github` ← `plugin:github:github` は plugin 名前空間で `claude mcp` 管理対象外
  - 実際の正解: `/mcp` slash command を Claude Code セッション内で実行
- **検出**: ユーザーから「unknown command」「No MCP server found」等のエラーフィードバック
- **対処**:
  1. コマンドを提示する**前**に `<command> --help` で実機確認（または `WebFetch` で公式 doc）
  2. 「コマンド名」「サブコマンド」「引数構文」「scope オプション」を順に検証
  3. plugin 経由でインストールされた MCP は通常コマンドでは管理できない可能性を考慮
  4. 推測で書く場合は「（未検証）」と明示
- **関連**: PROC-005（回答前 4 点内部レビュー「前提」項目の強化）
- **出自**: 2026-05-21 セッション内で発生（ストリーム C 中の MCP 既存接続トラブル修復手順）

---

## 2. DOCTRINE（strict rule 候補）

DNA v1.0 確定後（2026-06-30 予定）に `principles/doctrine.md` へ正式昇格予定の strict rule。本書は **暫定置き場**。

### DOCTRINE-001: Typography 固定（Poppins + Hiragino）
- **ルール**: FAM / FAMBOX のタイポグラフィは **Poppins（英字）+ Hiragino Sans（日本語）** で確定。重いスポーツブランド系 Display は禁止
- **禁止フォント**: Archivo / Archivo Black / Space Grotesk / Manrope（重厚アグレッシブ系 / Tech 寄り / 差別化薄）
- **Why**:
  - FAM の「確信と熱量を兼ねた洗練」は Archivo Black 的重厚さではなく Poppins の柔らかい幾何学と親和
  - スポーツ栄養ブランドとして NBA/NFL 的アグレッシブより落ち着いた科学性 + 親しみやすさが優先
  - 既存 19 ファイルで Poppins 400/500/600 が運用中 → 破壊的変更は不要
- **How to apply**:
  - 新規 Liquid section 作成時、英字は Poppins 固定（wght 400/500/600/700 の範囲）
  - 日本語は `"Hiragino Sans", "Hiragino Kaku Gothic ProN", "Meiryo", sans-serif`
  - Editorial 感はフォント選定ではなく **大きなサイズ・ジャンプ率・レイアウト**で演出
  - Display 用別フォント追加は不要
- **Promotion Status**: ✅ 昇格対象識別済（3 回以上の却下履歴）→ `principles/doctrine.md § D1` に移管予定
- **出自**: feedback_fam_typography

### DOCTRINE-002: ビジュアル Anti-pattern（清潔・Editorial × Lab・信頼に反する技法）
- **ルール**: FAMBOX 世界観は **清潔感 / Editorial × Lab / 信頼** が核。以下の技法はそのまま採用しない
- **❌ 原則として避ける**:
  - 輪郭・エッジを強く歪ませる変形（feDisplacementMap の大きな scale、wave 系、liquify 風）
  - 荒いノイズ + 発光の合わせ技（noise-bloom 系）
  - 色収差・グリッチ的演出（Cyberpunk / 80 年代系）
  - 重いブラー + 強いグロー（Neumorphism の厚塗り、ドラマチック発光）
- **⚠️ 応用次第で採用可**:
  - 微細なノイズ / 紙質感（feTurbulence の baseFrequency 高 + opacity 極端に下げる）
  - ごく静かな揺らぎ（feDisplacementMap scale=1〜2 以下、アニメなし）
  - 薄いラジアルグロー（opacity 0.08 以下）
- **Why**:
  - 輪郭歪み技法は Editorial（誌面・本）/ Lab（実験・科学）の精度・静けさと相反
  - 強い発光 / グリッチは健康食・信頼・安心ブランド約束を弱める
  - 2026-04-22 に宮川さんから明示判断あり（`#arc-noise-bloom 不採用` / `#arc-displacement scale=8 NG`）
- **Promotion Status**: 昇格対象識別済 → `principles/doctrine.md § D4` に移管予定
- **暫定参照**: `current.md § L0 0-3 Anti` の Anti-list 拡張
- **既存連動**: `lastmile-playbook.md CORRECTION-004`（写真過剰加工）と同系
- **出自**: feedback_fambox_visual_effects

### DOCTRINE-003: 資料フォントは游ゴシック（Yu Gothic UI）
- **ルール**: Excel / PowerPoint 等の **資料**ファイル作成時は **游ゴシック (Yu Gothic UI)** 固定。UI 制作（Shopify Liquid / Web アプリ等）の Poppins + Hiragino とは別管理
- **Why**:
  - 送り先が Windows ユーザー想定。游ゴシックは Win/Mac 両対応で表示崩れなし
  - Arial / メイリオではなく游ゴシックが上品で読みやすい
- **How to apply**:
  - `openpyxl` / `python-pptx` でファイル生成時 `Font(name="Yu Gothic UI")` を適用
  - UI と資料は完全分離。混同禁止
- **将来の関連**: ストリーム E（多出力アーキテクチャ）の `output-adapters/ppt-adapter.md` で正式 Spec 化予定
- **Promotion Status**: 昇格対象（出力タイプ別 doctrine としてストリーム E に連動）
- **出自**: feedback_document_font

### DOCTRINE-004: CSS Specificity 3 層戦略
- **ルール**: Liquid section のスタイル制御は **3 層構造**で設計する
- **3 層構造**:

| 階層 | 用途 | 強度 | メディアクエリ |
|---|---|---|---|
| **L1: inline `style="..."`** | PC 基本値の確実化 | 最強（1000）| 不可 |
| **L2: Liquid 内 `<style>` タグ** | SP オーバーライド、複雑セレクタ | 中強（外部より後勝ち）| 可 |
| **L3: 外部 CSS (`assets/*.css`)** | デザイントークン、共通スタイル | 基本（10〜100）| 可 |

- **Specificity 計算**:
  - inline style = 1000
  - `#id` = 100
  - `.class[attr]` = 20
  - `.class` = 10
  - tag = 1
  - `!important` で同階層内最強
  - `element.style.setProperty('width', '50%', 'important')` = ∞（最強）
- **実装例**:
  ```liquid
  <style>
    @media (max-width: 1023px) {
      .hero__lead-body[style] { font-size: 14px !important; }
    }
  </style>
  <div class="hero__lead-body" style="font-size: 16px;">
    {{ section.settings.intro_body }}
  </div>
  ```
- **関連**: BUG-001（inline 優先）/ DOCTRINE-005（Schema 型）
- **Promotion Status**: 昇格対象（DS Spec 本体に組み込み可能）
- **出自**: feedback_design_system_liquid_patterns パターン 3

### DOCTRINE-005: Schema 型選択ガイドライン
- **ルール**: Liquid section の Schema 型は用途に応じて選択する。**特に richtext はコンテナタグ `<div>` 必須**

| Schema type | 用途 | HTML 出力 | コンテナタグ |
|---|---|---|---|
| `text` | 単純テキスト、見出し、ラベル | プレーン文字列 | 任意（改行不可）|
| `textarea` | 段落、説明文（改行あり）| プレーン文字列 + 改行 | 任意（`<br>` は手動）|
| `richtext` | フォーマット付きテキスト（リンク、太字等）| **`<p>...</p>` ラップ** | **`<div>` 必須**（`<p>` 禁止）|
| `html` | 自由な HTML | 自由 | 任意（XSS リスク・ユーザー編集非推奨）|

- **コンテナタグ選択ルール**:

| 用途 | 推奨タグ | 理由 |
|---|---|---|
| 見出し | `<h1>`〜`<h6>` | 意味的 / SEO |
| 段落 (text/textarea) | `<p>` | 標準的段落 |
| 段落 (**richtext**) | **`<div>`** | richtext の `<p>` ラップで `<p>` 内 `<p>` ネスト不可 |
| ボタン | `<button>` または `<a class="btn">` | アクセシビリティ |
| カード / ボックス | `<div>` | 汎用コンテナ |

- **関連**: BUG-002（richtext + `<p>` ネスト破綻）
- **Promotion Status**: 昇格対象（DS Spec 本体に組み込み可能）
- **出自**: feedback_design_system_liquid_patterns パターン 1-2

---

## 3. PROCESS（運用ルール）

すでに `operations/` に正式昇格済のものは **出自記録**として、未昇格のものは Claude 作業時の必須ルールとして集約。

### PROC-001: Audit-first Protocol（既存資産棚卸し必須）
- **ルール**: 新 Component / Pattern / Token / Section / Snippet を提案する前に、既存資産を必ず棚卸しする
- **正規ルール**: `operations/audit-first-protocol.md`（v0.2 confirmed）
- **本書での扱い**: 出自記録のみ。実運用は audit-first-protocol.md を参照
- **5 ステップ標準フロー**: Step 1 キーワード抽出 → Step 2 Spec 検索 → Step 3 Liquid 実装検索 → Step 4 棚卸し結果提示 → Step 5 方針決定
- **判定パス**: A. 流用（80%↑カバー）/ B. 拡張（50-80%）/ C. 新規（50%↓）/ D. 不採用（DNA 違反）
- **出自**: feedback_existing_asset_first（✅ audit-first-protocol.md に昇格済）

### PROC-002: 3 回失敗で根本原因分析・2 回でアプローチ変更
- **ルール**:
  - **2 回失敗**: 同じ種類のエラーが 2 回発生したら即停止。同じアプローチを試さない。根本原因を特定する
  - **3 回失敗**: コードを書くのをやめてユーザーに状況を正直に報告。「3 回失敗しました。私の理解が間違っています。現在の構造を正確に説明するので、指示をいただけますか？」
- **Why**: 2026-03-25 に「横スクロール + グラデーションフェード」で 10 回以上失敗・1 時間以上ユーザーの時間を浪費した最重大インシデント
- **禁止行為**:
  - 「試してみてください」「修正しました」の繰り返し
  - 自分で考えた代替案の提案（指示に従う）
- **修正後の自己検証チェック**:
  - [ ] この修正が解決する理由を 1 文で説明できるか
  - [ ] Shopify の `.shopify-section` ラッパーの影響を考慮したか
  - [ ] SP 版で `overflow: hidden` の親要素がある前提で設計したか
  - [ ] PC 版 CSS が SP 版に残存して干渉しないか確認したか
  - [ ] 過去に同種の修正で失敗したパターンと照合したか
- **関連**: BUG-008（scroll-snap + padding 10 回失敗事例）
- **出自**: feedback_implementation_discipline §0-1, §1

### PROC-003: ユーザー指示の正確実装・自己判断でアプローチ変更禁止
- **ルール**: ユーザーが「こうしてほしい」と言ったら **その通りに実装する**。「こっちの方が良いはず」と自分で判断してアプローチを変えない
- **例外**: ユーザーの指示が技術的に不可能な場合のみ、理由を説明してから代替案を提示
- **Why**: ユーザーは命を削って時間を割いている。その時間を無駄にすることは許されない
- **CSS の挙動を「推測」で書かない**:
  - `padding-left` がスクロールコンテナでどう動くか不明 → 先に小さなテストを書いて検証
  - `scroll-snap` と `padding` / ダミー要素の組み合わせが不明 → カード 1 枚の最小構成でテスト
  - 「こうなるはず」で本番コードを書くことは禁止
- **関連**: PROC-002 / BUG-008
- **出自**: feedback_implementation_discipline §0

### PROC-004: ファイル生成後の読み戻し検証（証拠付き報告）
- **ルール**: ファイルを生成・更新したと報告する前に、必ず以下を実行
- **手順**:
  1. ファイル生成後、`ls -la` でタイムスタンプ + サイズ確認
  2. 内容をサンプル読み取りし、期待する変更が反映されているか検証
  3. 検証結果（タイムスタンプ・行数・主要セル値）をユーザーに提示
  4. 「保存しました」ではなく「保存し、以下の内容を確認しました:」と証拠付きで報告
  5. Excel 等バイナリは openpyxl 等で読み戻して主要セル値を表示
- **Write 実行時の追加ルール**:
  1. Write 実行前に「📝 作成開始: ファイル名（約 N 行）」を返す
  2. Write 実行後に `ls -la` でファイル存在・サイズを確認
  3. 確認後に「✅ 作成完了: N バイト」を返す
  4. `ls` で確認するまで「完了しました」と言わない
  5. Write を実行せずに完了報告することは**絶対に許されない**
- **関連**: BUG-011（生成成功 ≠ 内容反映）
- **出自**: feedback_file_verification / feedback_implementation_discipline §7

### PROC-005: 回答前の 4 点内部レビュー（CLI / API 構文事前検証を含む）
- **ルール**: ユーザーへの回答前に、必ず以下 4 点を内部でレビューしてから出力
- **4 点**:
  1. **妥当性** — 質問に正確に答えているか、ズレていないか
  2. **最善性** — より良いアプローチ・選択肢・表現はないか
  3. **前提** — 未検証の仮定・思い込みはないか（必要なら検証してから回答）
  4. **影響範囲** — 見落とした副作用・リスク・依存関係はないか
- **適用範囲**: すべての回答・提案・実装方針の提示前。特にコード変更方針の決定 / 選択肢提示 / ファイル生成前に重点的にチェック
- **プロセス自体は毎回見せない**（冗長になるため）が、判断に迷う場合は選択肢として提示

#### PROC-005-A: CLI / MCP / API コマンド構文の事前検証（必須）
- **トリガー**: ユーザーに `claude mcp ...` / `gh ...` / `shopify ...` / `npm ...` 等のコマンドを提示する直前
- **必須手順**:
  1. **記憶に頼らず実機確認**: `<command> --help` を Bash 実行して使用可能なサブコマンド・引数を確認
  2. **公式 doc 確認**: WebFetch で公式ドキュメントから最新構文を引用
  3. **plugin / namespace の挙動考慮**: 例 `plugin:xxx:yyy` 形式は通常コマンドでは操作できない可能性
  4. **未検証部分を明示**: 確認できないコマンドは「（未検証）」マークを付ける
- **NG パターン**:
  - 「たぶんこのコマンドで動く」と推測で書く
  - 古い記憶のコマンドをそのまま転記
  - help 出力を見ずに「次のコマンドで再認証してください」と書く
- **関連**: BUG-013（コマンド推測の事故事例）
- **出自**: 2026-05-21 セッション内で `claude mcp reauth` 推測ミス発生 → 規律強化

- **出自**: feedback_answer_review（+ 2026-05-21 セッション内強化）

### PROC-006: Token 名は実装前に実機 grep 実在検証
- **ルール**: `--xxx-yyy` 形式の Token 名を spec / plan / 設計文書に書く時、その名前は **未検証の仮置き**として扱う。実装着手前に必ず実在検証
- **検証コマンド**:
  ```bash
  grep -E "^\s*--xxx" snippets/fambox-tokens.css.liquid
  ```
- **手順**:
  1. 新規 spec / plan で Token を引用する時は grep 必須
  2. plan に書く時は「(該当 token 未確認)」とマーキングし、実装 task の Step 1 で「事前確認」step を入れる
  3. 実装 task の各 implementer subagent に「Token 引用は実在検証してから書く」を明示
  4. 横断 fix：Token 名改名の発見は §1 早見表など他箇所も同時に修正対象として最終 task まで持ち越す
- **関連**: BUG-009（spec vs 実在乖離）/ PROC-001（Audit-first の延長）
- **出自**: feedback_token_name_verification

### PROC-007: Reviewer 指摘は実機検証してから受け入れる
- **ルール**: subagent-driven-development の review フェーズで reviewer が「値 X が間違っている / Y であるべき」と指摘した場合、そのまま受け入れず grep / 直接 Read で実機確認してから対応
- **手順**:
  1. reviewer が具体的な値 / 名前を「実在は X」と主張したら、必ず `grep -nE "^\s*--xxx" snippets/fambox-tokens.css.liquid` で裏取り
  2. reviewer の主張が grep 結果と矛盾したら、reviewer の指摘を**棄却**してその旨を記録（implementer に再依頼しない）
  3. **trust 度**：spec reviewer ＞ code quality reviewer（後者はパターン認識中心でハルシネーション率高）
  4. 複数 reviewer の指摘が矛盾したら、実機検証を最終判定とする
- **関連**: BUG-010（reviewer ハルシネーション事例 6 件）/ PROC-006
- **出自**: feedback_reviewer_hallucination_check

### PROC-008: `~/.claude/` 変更ワークフロー（`/tmp` 経由）
- **ルール**: `~/.claude/` 配下の設定・コマンドファイル変更は直接 Write/Edit 不可。`/tmp/` 経由で cp 依頼する
- **手順**:
  1. `/tmp/` にファイルを書き出す
  2. ユーザーにターミナルで `cp /tmp/{file} ~/.claude/{target}` を実行依頼
  3. heredoc はバッククォート含有時に shell 混乱 → `python3 -c` + `pathlib` が確実
  4. 書き込み後は必ず Read で確認
- **関連**: BUG-012（セルフモディファイ保護）
- **出自**: feedback_claude_config_write

### PROC-009: WF→承認→Liquid→比較検証→修正→書き出し 必須サイクル
- **ルール**: UI デザインから Shopify Liquid を作る際は必ず以下のサイクルを回す。一足飛びに Liquid を書かない
- **6 ステップ**:
  1. **WF 作成**: ユーザー指示を聞き、まずスタンドアロン HTML でワイヤーフレーム作成
  2. **レイアウト承認**: ユーザーにプレビューを見せて OK をもらう（ゲート）
  3. **Liquid 変換**: WF と **同じ HTML 構造・CSS 手法** で Liquid 作成
  4. **比較検証**: WF と Liquid を以下の観点で比較
     - レイアウト（余白、配置、サイズ）
     - フォント（ファミリー、ウェイト、サイズ）
     - レイヤー構造（position、z-index、absolute/relative）
     - 色（背景、テキスト、ボーダー）
  5. **修正**: 差分があれば Liquid を修正
  6. **書き出し**: 最終版をユーザーに渡す
- **重要なルール**:
  - WF で使った CSS 手法（absolute positioning 等）を Liquid で勝手に padding 等に変えない
  - CSS セレクタは必ず `#{{ sec_id }}` でスコープする
  - SVG アイコンはテキスト説明から再現しない。グレープレースホルダーか、ユーザー提供 SVG コードを使う
  - Poppins 等の外部フォントは Google Fonts 読み込みタグが必要
- **関連**: BUG-005（手法変更）/ BUG-006（PC 基本値残存）
- **出自**: feedback_liquid_workflow

### PROC-010: Liquid 検証 3 段階（ローカル / curl / DevTools）
- **ルール**: Liquid section 修正後は必ず 3 段階で検証
- **3 段階**:
  ```
  Step 1: ローカルファイル確認
    grep -nE 'pattern' /tmp/fam-liquid/sections/{section}.liquid

  Step 2: 本番反映確認（curl）
    curl -s "https://{store}.com/pages/{handle}" -L | grep "pattern"

  Step 3: ブラウザ計算値確認（DevTools Console）
    const el = document.querySelector('セレクタ');
    console.log('inline:', el.getAttribute('style') || '【なし】');
    console.log('computed:', getComputedStyle(el).fontSize);
  ```
- **ユーザーに「変化なし」と報告された瞬間、即 Step 2 → Step 3 を実行する**。CSS をさらに追加修正する前に
- **関連**: BUG-001〜004（Shopify Liquid 4 罠の検出手段）/ PROC-004
- **出自**: feedback_design_system_liquid_patterns パターン 4

---

## 4. 統合元 feedback memory 一覧（出自記録）

本書は以下 13 個の feedback memory を統合して構築。各 memory は **出自記録**として保持（削除しない）。

| # | feedback memory | 統合先（BUG / DOCTRINE / PROC）|
|---|---|---|
| 1 | feedback_liquid_workflow | BUG-005, BUG-006, PROC-009 |
| 2 | feedback_implementation_discipline | BUG-007, BUG-008, PROC-002, PROC-003, PROC-004 |
| 3 | feedback_file_verification | BUG-011, PROC-004 |
| 4 | feedback_document_font | DOCTRINE-003 |
| 5 | feedback_claude_config_write | BUG-012, PROC-008 |
| 6 | feedback_answer_review | PROC-005 |
| 7 | feedback_fam_typography | DOCTRINE-001 |
| 8 | feedback_existing_asset_first | PROC-001（audit-first-protocol.md 昇格済の出自記録）|
| 9 | feedback_fambox_visual_effects | DOCTRINE-002 |
| 10 | feedback_token_name_verification | BUG-009, PROC-006 |
| 11 | feedback_reviewer_hallucination_check | BUG-010, PROC-007 |
| 12 | feedback_shopify_liquid_specificity | BUG-001, BUG-002, BUG-003, BUG-004 |
| 13 | feedback_design_system_liquid_patterns | DOCTRINE-004, DOCTRINE-005, PROC-010（+ BUG-002 共通）|
| 14 | （セッション内事故・2026-05-21）| BUG-013 + PROC-005-A — `claude mcp reauth` 推測ミスから派生 |

---

## 5. 件数サマリ

| カテゴリ | 件数 | 構成 |
|---|---|---|
| BUG | 13 | Shopify Liquid 4 / WF→Liquid・Theme 干渉 4 / Tokens・Claude 運用 5 |
| DOCTRINE | 5 | Typography 1 / Anti-pattern 1 / 資料フォント 1 / Specificity 1 / Schema 型 1 |
| PROCESS | 10 + 1 sub | Audit-first 1 / 失敗対処 2 / 検証規律 3 / Token 検証 2 / Workflow 1 / Liquid 検証 1 / **PROC-005-A CLI 事前検証** |
| **合計** | **28** | BUG-013 と PROC-005-A は 2026-05-21 セッション内事故事例から追加 |

---

## 6. 関連ファイル

- 入口の検閲: [operations/audit-first-protocol.md](operations/audit-first-protocol.md) — 新規追加前の既存棚卸し
- 昇格判定: [operations/promotion-rule.md](operations/promotion-rule.md) — DOCTRINE 昇格基準
- 補正パターン: [operations/lastmile-playbook.md](operations/lastmile-playbook.md) — AI 生成残 5% 補正
- 命名 / SSoT: [operations/naming-convention.md](operations/naming-convention.md) — Spec の正
- DS 全体: [current.md](current.md)
- Brand DNA: [../brand-dna/current.md](../brand-dna/current.md)
- 全変更履歴: [../../CHANGELOG.md](../../CHANGELOG.md)

---

## Change Log

- v0.1 (2026-05-21): 初版。13 個の feedback memory を BUG 12 / DOCTRINE 5 / PROCESS 10 = 27 エントリに統合。ストリーム A（bugs.md 統合）成果物。Marc-Antoine Archeco kit v7.14 の bugs.md 構造を FAMBOX L0-L9 構造に適応。
- v0.2 (2026-05-21): **セッション内事故事例から 2 エントリ追加** — BUG-013（CLI/MCP/API コマンド推測の罠）+ PROC-005-A（CLI / MCP / API コマンド構文の事前検証 — 必須サブルール）。`claude mcp reauth` 推測ミス（実在しないサブコマンド）+ `plugin:github:github` の名前空間誤解で発生したユーザー時間浪費から、AI 自身の規律を強化。**bugs.md が「ユーザー罠の蓄積」だけでなく「Claude 自身の運用規律」も含むようになった点が構造的進化**。
