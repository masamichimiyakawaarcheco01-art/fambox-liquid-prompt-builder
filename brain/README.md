# Second Brain — 宮川真道の外部脳

ARCHECO / FAMBOX運用のための思考蓄積リポジトリ。Qiita記事「Claude Codeが第二の脳」型とcoleam00/second-brain-skills型のハイブリッド運用。

## ディレクトリ構造（PARA派生）

| ディレクトリ | 用途 | 卒業条件 |
|---|---|---|
| `00_Inbox/` | 未整理思考・メモの一次保管 | 週次レビューで分類 |
| `10_Journal/` | 日記・振り返り・セッションログ | そのまま蓄積（時系列） |
| `20_Projects/` | ゴール指向プロジェクト（FAMBOX OKR等） | 完了後は `99_Archives/` |
| `30_Tech_Notes/` | 永続的な技術知識（Liquid, Shopify, GA4 等） | 継続参照 |
| `50_Business_Context/` | ドメイン・クライアント・市場知識 | 継続参照 |
| `90_System/` | 運用ルール・ガイドライン・メタ情報 | 継続更新 |
| `99_Archives/` | 完了プロジェクト・廃止ノート | 読み取り専用 |

## 運用フロー

1. **Capture**: 思考を `/capture` で `00_Inbox/` に投入
2. **Decompose**: `/decompose` でゴール→マイルストーン→タスク3層分解
3. **Work**: `/work` で個別タスクを実行
4. **Weekly Review**: `/weekly-review` で放置検出・整理

## 既存システムとの関係

- **`~/.claude/projects/.../memory/`** との役割分担:
  - memory = セッション横断の事実・フィードバック（短く・索引化）
  - brain = 思考プロセス・意思決定ログ・プロジェクト詳細（長く・構造化）
- **`docs/okr/`**: OKR管理は従来通り `docs/okr/` を主、`brain/20_Projects/fambox-okr/` から参照
- **`.claude/skills/`**: `second-brain-skills`（brand-voice-generator, sop-creator等）を実行エンジンとして使用

## 事実源のルール

brainに記録されたものだけを事実源とする。会話履歴の発言を「決定済み」扱いしない。
