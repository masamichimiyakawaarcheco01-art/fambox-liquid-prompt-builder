# Liquid Prompt Builder v3 - PDCA検証機能 設計書

## 概要

Prompt Builder v2に検証パネルを統合し、Figmaデザインと生成コードの一致度をチェックするPDCAサイクルをワンストップで回せるようにする。

## 目的

- デザインと実装の差異を体系的に検出する
- 差異の原因を特定し、プロンプトを改善する
- 複数LLM（Claude Code / Gemini / ChatGPT）を役割分担で活用し、Claude Code使用量を最小化する
- PDCAサイクルを継続的に回し、プロンプト精度を段階的に向上させる

## 対象ユーザー

UIデザイナー。FigmaデザインからShopify Liquid等のコードを生成し、見た目の一致度を検証・改善する。

## LLM役割分担

| ツール | 役割 | PDCAフェーズ |
|---|---|---|
| Claude Code | コード実装・修正 | Do / Act |
| Gemini (Antigravity) | デザイン画像比較・視覚レビュー | Check |
| ChatGPT | 差分原因分析・プロンプト改善提案 | Check → Act |

## 画面レイアウト

3カラム構成:

```
┌─────────────────────────────────────────────────┐
│  Header: Liquid Prompt Builder v3               │
├──────────┬──────────┬───────────────────────────┤
│  入力    │ プロンプト│   検証パネル              │
│  フォーム │ 出力     │                           │
│  (7タブ)  │          │  Figma画像 | Preview     │
│  30%     │  30%     │                           │
│          │          │  チェックリスト            │
│          │          │  差分レポート              │
│          │          │  LLM連携ボタン            │
│          │          │  40%                      │
├──────────┴──────────┴───────────────────────────┤
│  PDCA ステータスバー                             │
└─────────────────────────────────────────────────┘
```

### レスポンシブブレイクポイント

| 画面幅 | レイアウト | 備考 |
|---|---|---|
| >1440px | 3カラム (30/30/40) | フル機能 |
| 960-1440px | 2カラム (50/50) + 検証パネルは下部ドロワー | 検証パネルはボタンで開閉 |
| <960px | 1カラム縦積み | 順序: 入力→プロンプト→検証 |

各パネルは独立スクロール（max-height: calc(100vh - 56px - 48px)、48pxはステータスバー）。

## 検証パネル機能

### 1. Figma画像取り込み

- ドラッグ&ドロップでアップロード
- クリップボードからペースト（Cmd+V）
- ブラウザ内のみ保持（サーバー送信なし、FileReader API使用）
- 最大2枚（PCデザイン / SPデザイン）をタブ切替で表示
- 制約: 各画像5MB以下、PNG/JPEG/WebP対応
- セッション中のみ保持（リロードで消える）

### 2. コードプレビュー

- テキストエリアにコードを貼り付け
- sandbox付きiframeでリアルタイムレンダリング
- Liquid構文はプレビュー時にプレースホルダーに自動置換（下記ルール）
- プレビューサイズ切替: PC(1200px) / SP(375px)
- sandboxのCSPにより、貼り付けコード内の外部リソース（フォント、画像URL）は読み込まれない旨を表示

#### Liquid置換ルール

| Liquid構文 | 置換結果 | 例 |
|---|---|---|
| `{{ variable }}` | `[variable名]` | `{{ section.settings.heading }}` → `[heading]` |
| `{{ 'file' \| asset_url }}` | `#` (空リンク) | 画像やCSS参照 |
| `{% if condition %}...{% endif %}` | タグ除去、中身は全て表示 | 条件分岐の全ブランチを表示 |
| `{% for item in collection %}...{% endfor %}` | 中身を3回繰り返し表示 | ループのプレビュー |
| `{% render 'partial' %}` | `[partial: partial名]` | インクルード参照 |
| `{% schema %}...{% endschema %}` | 完全に除去 | JSON設定は非表示 |
| `{%- liquid ... -%}` | 完全に除去 | assign等の制御文 |

### 3. 自動チェックリスト

入力フォームの値から検証項目を自動生成する。チェックは手動（目視確認でクリック）。

生成ルール:

| 入力タブ | 生成されるチェック項目例 |
|---|---|
| Color | `Primary #FB4C15 が使われているか` |
| Color | `Secondary #1B1D1A が使われているか` |
| Color | `画像上テキスト: グラデーションオーバーレイが適用されているか` |
| Type | `H1が32pxで表示されているか` |
| Type | `フォント: Hiragino Sans が適用されているか` |
| Type | `行間 1.6 が適用されているか` |
| Spacing | `S=16px / M=24px / L=36px のスケールか` |
| Spacing | `コンテナpadding が L で適用されているか` |
| Parts | `border-radius: 8px が適用されているか` |
| Parts | `シャドウ: 微細 (0 2px 4px) が適用されているか` |
| Parts | `Hover時に暗くなるか` |
| Taste | `ジャンプ率: 高（要素サイズ差が大きいか）` |
| Taste | `形状: 角ばった形状になっているか` |
| Basic | `レイアウト比率 1:2 になっているか` |
| Basic | `SPブレイクポイント 749px で切り替わるか` |

空欄の入力項目からはチェック項目を生成しない。

#### チェックリスト生成ロジック（フィールド→テンプレートマッピング）

```javascript
const checklistRules = [
  // Color tab - 定量チェック（値が明確）
  { field: 'colorPrimary',   template: 'Primary色 {value} がメイン要素に使われているか', category: 'color' },
  { field: 'colorSecondary', template: 'Secondary色 {value} が使われているか', category: 'color' },
  { field: 'colorInactive',  template: 'Inactive色 {value} が無効状態に使われているか', category: 'color', skipDefault: '#CCCCCC' },
  { field: 'colorError',     template: 'Error色 {value} がエラー表示に使われているか', category: 'color', skipDefault: '#E53E3E' },
  { toggle: 'textOnImage',   template: '画像上テキスト: {label} が適用されているか', category: 'color' },

  // Type tab - 定量チェック
  { field: 'typeH1',    template: 'H1が {value} で表示されているか', category: 'typography' },
  { field: 'typeH2',    template: 'H2が {value} で表示されているか', category: 'typography' },
  { field: 'typeH3',    template: 'H3が {value} で表示されているか', category: 'typography' },
  { field: 'typeBody',  template: 'Body文字が {value} で表示されているか', category: 'typography' },
  { select: 'fontJA',   template: '日本語フォント: {value} が適用されているか', category: 'typography' },
  { select: 'fontEN',   template: '英語フォント: {value} が適用されているか', category: 'typography' },
  { toggle: 'lineHeight', template: '行間 {value} が適用されているか', category: 'typography' },

  // Spacing tab - 定量チェック
  { field: 'spacingS', template: 'Small余白 {value} が使われているか', category: 'spacing', group: 'spacing-scale' },
  { field: 'spacingM', template: 'Medium余白 {value} が使われているか', category: 'spacing', group: 'spacing-scale' },
  { field: 'spacingL', template: 'Large余白 {value} が使われているか', category: 'spacing', group: 'spacing-scale' },
  { toggle: 'spacingContainer', template: 'コンテナpaddingが {value} サイズか', category: 'spacing' },
  { toggle: 'spacingSibling',   template: '兄弟要素marginが {value} サイズか', category: 'spacing' },

  // Parts tab - 定量チェック
  { toggle: 'borderRadius', template: 'border-radiusが {value}px か', category: 'parts' },
  { toggle: 'elevation',    template: 'シャドウが {label} レベルか', category: 'parts' },
  { toggle: 'transitionSpeed', template: 'トランジション速度が {value} か', category: 'parts' },

  // Taste tab - 定性チェック（目視のみ、type: 'visual' で区別）
  { toggle: 'shapeStyle', template: '形状: {label} になっているか', category: 'taste', type: 'visual' },
  { toggle: 'jumpRate',   template: 'ジャンプ率: {label} か', category: 'taste', type: 'visual' },
  { field: 'tasteName',   template: 'デザインテイスト「{value}」の世界観が表現されているか', category: 'taste', type: 'visual' },

  // Basic tab - 定量 + 定性
  { toggle: 'layoutRatio', template: 'レイアウト比率が {value} になっているか', category: 'layout' },
  { field: 'breakpoint',   template: 'SPブレイクポイント {value} で切り替わるか', category: 'layout' },
];
// type: 'visual' は「目視確認」ラベル付き、それ以外は「数値確認」ラベル付き
```

各ルールの `field` はinput要素のid、`toggle` はtoggle-rowのid、`select` はselect要素のidに対応。値が空/未選択のルールはスキップ。`skipDefault` が設定されている場合、その値と一致する場合もスキップ。

### 4. 差分レポート生成

未チェック（不一致）項目から改善指示を自動生成。

出力例:
```
以下の項目がデザインと一致していません。修正してください:
- Primary色 #FB4C15 が未使用 → ボタンとアクセントに適用
- H1が32pxではなく24pxになっている → 修正
- コンテナpadding が L(36px) ではなく20pxになっている
```

### 5. LLM連携プロンプト

3種のフォーマットでワンクリックコピー:

#### Claude Code用（修正実行）
```
以下のLiquidセクションを修正してください。

## 現在のコード
[生成済みコードを自動挿入]

## 修正が必要な項目
- [未チェック項目を自動列挙]

## デザイン仕様（参照）
[入力フォームの値を構造化して挿入]

元のコードを直接編集し、修正済みコードを出力してください。
```

#### Gemini用（デザイン比較レビュー）
```
以下のUIデザイン画像と、実装コードのスクリーンショットを比較し、
差異を具体的に列挙してください。

## デザイン仕様
[入力フォームの値を挿入]

## チェック観点
1. カラーの一致（Primary/Secondary/Gray）
2. フォントサイズ・ウェイトの一致
3. 余白・スペーシングの一致
4. レイアウト比率の一致
5. 角丸・シャドウの一致
6. 全体的な印象・世界観の一致

差異ごとに「箇所」「期待値」「実際の値」「重要度(高/中/低)」を表形式で出力してください。

※ このプロンプトとともに、Figmaデザイン画像とプレビューのスクリーンショットをGeminiに添付してください。
```

#### ChatGPT用（原因分析）
```
UIの実装コードがデザイン仕様と一致しない原因を分析してください。

## 不一致項目
[未チェック項目を挿入]

## 使用したプロンプト
[生成プロンプトを挿入]

以下を分析してください:
1. プロンプトのどの記述が不十分だったか
2. どう書き換えればLLMが正確に実装するか
3. Prompt Builderの入力項目として何を追加すべきか

改善案を具体的に提示してください。
```

## PDCAステータスバー

画面下部に常時表示。

```
[Plan] ━━● [Do] ━━○ [Check] ━━○ [Act] ━━○  Cycle #1
```

### 状態遷移

| フェーズ | 開始条件 | 完了条件 |
|---|---|---|
| Plan | 入力フォームに値がある | プロンプト生成済み |
| Do | プロンプトをコピー | コードテキストエリアに貼り付け（非空で自動遷移） |
| Check | コードプレビュー表示 | 全チェック項目を確認済み |
| Act | 未チェック項目あり | 差分レポートコピー + 「サイクル完了」押下 |

全項目チェック済みの場合、Actをスキップして「合格」表示。
サイクル回数をカウント表示。

## 技術仕様

- 単一HTML（index.html）に全て含める
- 外部依存なし（Vanilla JS + CSS）
- FileReader APIで画像処理
- sandbox iframeでコードプレビュー
- localStorageでサイクル履歴を保持

### サイクル履歴データモデル

```javascript
// localStorage key: 'pdca_history'
{
  currentCycle: 1,
  cycles: [
    {
      id: 1,
      timestamp: '2026-03-26T10:30:00',
      phase: 'check',           // plan | do | check | act | complete
      totalChecks: 15,
      passedChecks: 12,
      failedItems: ['Primary色が未使用', 'H1が24pxになっている'],
      sectionName: 'fambox-hero'
    }
  ]
}
```

リセットボタンで履歴クリア可能。

## 対象外（v3スコープ外）

- サーバーサイド処理
- LLM APIの直接呼び出し
- 自動ピクセル差分検出（将来的に検討）
- Shopify固有のLiquid構文検証
