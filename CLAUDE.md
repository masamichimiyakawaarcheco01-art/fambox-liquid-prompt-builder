# Liquid Prompt Builder v4

## プロジェクト概要

Shopify Liquidセクションファイルを効率的に生成するためのプロンプトビルダーアプリ。
FigmaデザインからShopify Liquidコードへの変換作業において、Claudeへの指示プロンプトを構造化・標準化することで、品質の高いLiquidコードを一貫して生成できるようにする。

v4ではFigma MCPからのデザインコンテキスト自動取り込みと、PDCA検証システムを統合。手動入力では捉えきれなかったデザイン詳細（不透明度、グラデーション、ブラー、要素階層）をプロンプトに含めることで、デザイン再現精度を37%→84%に向上させた。

## 対象ユーザー

- UIデザイナー / フロントエンドエンジニア
- Shopifyテーマ開発者
- FigmaデザインをShopify Liquidに変換する作業者

## 現在の機能（v4）

### 8タブ構成

#### 0. Import（Figma取り込み）★v4新機能
- Figma URL入力（fileKey + nodeId自動抽出）
- FigmaDesignToken JSON貼り付け
- バリデーション + 取り込み結果サマリ
- 全フォームフィールドの自動入力

#### 1. Basic（基本設定）
- テンプレート選択（Hero / Features / Carousel / FAQ / Profile / Custom）
- セクション名・目的
- レイアウト比率（1:1, 1:2, 1:3, 2:3, Full）
- レイアウト構成（PC/SP）
- PC最大幅・SPブレイクポイント
- 機能要件チップ（10種）
- **要素階層** textarea ★v4新機能

#### 2. Taste（デザインテイスト）
- デザインテイスト名（世界観の言語化）
- 形状（丸み / 角ばり / 幾何学 / 有機的）
- ジャンプ率（低=高級感 / 中間 / 高=躍動感）
- エフェクト（ドロップシャドウ, 背景ブラー, グラス効果 等7種）
- 必須構成要素（テイスト維持に不可欠な要素）
- 写真/イラスト方針
- 背景の扱い
- **グラデーション定義** textarea ★v4新機能
- **ブラー値** textarea ★v4新機能
- **不透明度マップ** textarea ★v4新機能

#### 3. Type（タイポグラフィ）
- フォントファミリ（日本語5種 / 英語5種）
- 6段階フォントスケール（飾り / 大H1 / 大中H2 / 中H3 / 中小Body / 最小Small）
- 行間（1.4〜2.0）
- font-weightポリシー（細め / 標準 / 太め）

#### 4. Spacing（スペーシング）
- S/M/Lスケール定義（等比率: 1.5x / 2x / カスタム）
- ビジュアルプレビューバー
- スペーシングポリシー（コンテナ→子 / 兄弟間 / コンポーネント内）

#### 5. Color（カラーシステム）
- 4色ブランドカラー（Primary / Secondary / Inactive / Error）
- 4段階グレースケール（Gray1〜4）
- カラーピッカー付き
- 画像上テキスト処理（グラデOL / 単色OL / テキストシャドウ / なし）

#### 6. Parts（コンポーネント仕様）
- 状態表現（Hover暗化, Hover拡大, Hover影, Disabled透過, Pressedハロー, Focusリング）
- 角丸パターン（0px / 4px / 8px / 12px / Pill）
- **border-radius variants** textarea ★v4新機能
- シャドウレベル（なし / 微細 / 中程度 / 強め）
- **シャドウ詳細** textarea ★v4新機能
- ボタン種類（Filled / Outlined / Text Only / Icon）
- アニメーション方針（なし / 控えめ / 遊び心 / ドラマチック）
- トランジション速度（0.15s / 0.3s / 0.5s / 0.8s）

#### 7. Schema（カスタマイザー設定）
- 設定項目チップ（12種）
- ブロックタイプ定義
- コーディングルール（7種）

### 出力機能
- 構造化プロンプトのリアルタイム生成（最大127行/3364文字）
- `## 詳細デザイン仕様（Figma抽出）` セクション自動追加
- 行数・文字数カウント表示
- クリップボードコピー（プレーン / Markdown）

### PDCA検証システム（v3〜）

#### 検証パネル（3カラム目）
- **Figma画像取り込み**: ドラッグ&ドロップ / クリック / Cmd+V対応。PC/SPタブ切替
- **コードプレビュー**: Liquid構文を自動除去してiframe内にレンダリング。PC/SP切替
- **自動チェックリスト**: 25ルール（v3の19+v4の6）から検証項目を動的生成
- **差分レポート**: 未チェック項目から改善指示を自動生成

#### LLM連携（3種のプロンプト自動生成）
- **Claude Code**: コード修正指示（現在のコード + 不一致項目 + デザイン仕様 + 詳細仕様）
- **Gemini**: デザイン画像比較レビュー（9観点: +グラデーション/ブラー/不透明度/階層）
- **ChatGPT**: 原因分析（5観点: +エフェクト記述/階層指示の十分性）

#### PDCAステータスバー
- Plan → Do → Check → Act の4フェーズ自動遷移
- サイクルカウント + 履歴管理（localStorage、最大20サイクル）

## 技術スタック

- HTML / CSS / JavaScript（単一ファイル、外部依存なし）
- Google Fonts（Poppins）

## FigmaDesignToken JSON形式

Figma MCPの `get_design_context()` 出力から変換するJSON形式:

```json
{
  "meta": { "nodeId": "3:625", "nodeName": "PC1_1" },
  "colors": {
    "primary": "#06c352",
    "secondary": "#020214",
    "grays": ["#1a1a2e", "#2a2a3e", "#494955", "#888899"],
    "additional": [{ "name": "card-bg", "hex": "#FFFFFF", "opacity": 0.1 }]
  },
  "typography": {
    "fontFamilyJA": "Hiragino Kaku Gothic Pro",
    "fontFamilyEN": "Inter",
    "scale": {
      "display": { "size": "28px", "weight": 700, "lineHeight": 1.7 },
      "h1": { "size": "24px", "weight": 700 },
      "body": { "size": "14px", "weight": 700 }
    }
  },
  "spacing": { "s": "16px", "m": "24px", "l": "32px", "ratio": "1.5" },
  "effects": {
    "shadows": [{ "name": "card", "x": 0, "y": 4, "blur": 12, "spread": 0, "color": "rgba(0,0,0,0.1)" }],
    "blurs": [{ "name": "glass", "type": "background", "radius": 12 }],
    "gradients": [{ "name": "badge", "type": "linear", "angle": 135, "stops": [
      { "color": "rgb(5,181,75)", "position": 3 },
      { "color": "rgb(5,222,92)", "position": 100 }
    ]}]
  },
  "borderRadius": { "default": "16px", "variants": { "card": "16px", "pill": "60px" } },
  "taste": { "name": "ダークグラスモーフィズム", "shape": "rounded", "jumpRate": "high" },
  "opacity": { "card-bg": "0.1", "sidebar-bg": "0.3" },
  "hierarchy": [
    { "depth": 0, "name": "wrapper", "type": "FRAME", "w": 1920, "h": 1080, "fill": "#020214" },
    { "depth": 1, "name": "card", "type": "FRAME", "w": 1192, "h": 268, "fill": "rgba(255,255,255,0.1)" }
  ]
}
```

## 精度検証結果

### PC1_1（バッテリーマーケットプレイス）での検証

| バージョン | 精度 | 主な改善点 |
|---|---|---|
| v3（手動入力） | 約37% | 基本色・フォント・リングチャートのみ一致 |
| v4（Figma取込） | 約84% | ピル型コンテナ、不透明度、border-radius variants、要素階層が一致 |

### 残存課題（v5で対応予定）
- **ぼかし・ガラス加工**: backdrop-filter + 複雑な半透明レイヤー重ねの再現精度が低い
- **放射状グロー**: radial-gradient による背景エフェクトの正確な位置・サイズ指定
- **複合エフェクト**: 複数のblur + gradient + opacityが重なった表現の指示方法
- **SVGアセット**: Figmaのベクターアイコンを正確にSVGコードに変換する仕組み
- **レスポンシブ詳細**: SP版レイアウトの自動取り込み（現在はPC版のみ）

### 改善の方向性
1. エフェクト定義をCSS値ではなく「レイヤー構造」として記述する（どの要素の上に何が重なるか）
2. Figma MCPの画像アセットURLをプロンプトに含め、LLMが参照できるようにする
3. Geminiのビジュアル比較結果を自動的にPrompt Builderにフィードバックする仕組み

## デザインリファレンス

以下のARCHECO教材に基づく:
- UIデザインの基本原則（シリーズ1〜7、計80+スライド）
- UIコンポーネントモジュール仕様（Colors, Fonts, Buttons, Cards, Tabs等20+モジュール）

### 主要な設計原則
- **平面構成**: シンプルな整数比（1:1, 1:2, 2:3等）でレイアウトを定義
- **スペーシング**: 等比率（1.5x/2x）でS/M/Lを定義、等差は避ける
- **タイポグラフィ**: ジャンプ率でデザインテイストを制御
- **キャラクターライン**: コンテナ境界とオブジェクト整列で視覚構造を作る
- **デザインテイスト**: パラメータ化して必須/代替可能を区別

## FAMBOXプロジェクトとの関連

このツールは、FAM/FAMBOXのShopifyストア開発で使用するLiquidセクションの生成を効率化するために作成された。
