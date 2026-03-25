# Liquid Prompt Builder

## プロジェクト概要

Shopify Liquidセクションファイルを効率的に生成するためのプロンプトビルダーアプリ。
FigmaデザインからShopify Liquidコードへの変換作業において、Claudeへの指示プロンプトを構造化・標準化することで、品質の高いLiquidコードを一貫して生成できるようにする。

## 対象ユーザー

- UIデザイナー / フロントエンドエンジニア
- Shopifyテーマ開発者
- FigmaデザインをShopify Liquidに変換する作業者

## 現在の機能

### テンプレート選択
- **Hero**: ビデオ/画像ヒーローバナー
- **Features**: 特徴・バリュー訴求カード
- **Carousel**: 横スクロールカルーセル
- **FAQ**: アコーディオンFAQ
- **Profile**: 人物紹介・プロフィール
- **Custom**: 自由入力

### デザイン仕様入力
- 背景色・テキスト色・アクセントカラー
- PC最大幅・SPブレイクポイント
- レイアウト構成（PC/SP）

### 機能要件チップ
- スクロールアニメーション
- 動画背景
- アコーディオン
- カルーセル
- タブ切替
- モーダル
- 遅延読込（Lazy Load）
- パララックス

### Schema設定
- カスタマイザー設定項目の選択（見出し、画像、色、余白など）
- ブロックタイプの定義

### コーディングルール
- Scoped CSS（section.idベース）
- 外部JS不使用（Vanilla JS）
- レスポンシブ対応
- 日本語コメント
- Intersection Observer
- CSS変数

### 出力機能
- 構造化プロンプトのリアルタイム生成
- クリップボードコピー（プレーン / Markdown）

## 技術スタック

- HTML / CSS / JavaScript（単一ファイル、外部依存なし）
- Google Fonts（Poppins）

## FAMBOXプロジェクトとの関連

このツールは、FAM/FAMBOXのShopifyストア開発で使用するLiquidセクションの生成を効率化するために作成された。`sections/` ディレクトリにある既存のLiquidファイル群のパターンに基づいてテンプレートが設計されている。
