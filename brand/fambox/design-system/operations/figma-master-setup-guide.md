---
title: FAMBOX Figma マスターファイル 作成・運用手順書
type: design-system-operations
layer: L7-Operations / L8-Tools
status: active
last_updated: 2026-04-20
owner: 宮川
purpose: Figma マスターファイル「FAMBOX Design System」を最短で立ち上げ、Tokens/Components/Templates を一元管理する
figma_file: https://www.figma.com/design/QsiBrc2v20BYw76YHI9x3e/FAMBOX-Design-System
figma_file_id: QsiBrc2v20BYw76YHI9x3e
---

## 🔗 Figma ファイル（2026-04-20 立ち上げ済）
- **URL**: https://www.figma.com/design/QsiBrc2v20BYw76YHI9x3e/FAMBOX-Design-System
- **File ID**: `QsiBrc2v20BYw76YHI9x3e`
- **Tokens Studio JSON**: [tokens-figma.json](../tokens/tokens-figma.json)（インポート用）


# FAMBOX Figma マスターファイル — 作成・運用手順書

「Claude Design 消費可能な構造」を Figma 側で実現するための実務ガイド。

---

## 0. 全体像

```
┌─────────────────────────────────────┐
│ FAMBOX Design System (Figma File)   │
├─────────────────────────────────────┤
│ Pages:                              │
│  0. Cover                           │
│  1. Foundation                      │
│  2. Tokens         ← Variables      │
│  3. Primitives                      │
│  4. Patterns                        │
│  5. Components                      │
│  6. Templates                       │
│  7. Changelog                       │
└─────────────────────────────────────┘
        ↓ Library 公開
┌─────────────────────────────────────┐
│ FAMBOX [Project] Files              │
│ - LP / 定期便 / 問合せ / 食事診断…  │
│   Library から Insert で利用       │
└─────────────────────────────────────┘
```

---

## ステップ1: ファイル新規作成（**5分**）

### 操作
1. Figma にログイン
2. Team を選択（「FAMBOX」または既存 Team）
3. 「+ New design file」をクリック
4. ファイル名: **`FAMBOX Design System`**
5. Cover Page を確認（自動作成される最初のページ）

### Cover Page に書く内容
- ファイル名・バージョン（v0.2）
- 最終更新日
- Owner（宮川）
- 関連ドキュメントへのリンク
  - `brand/INDEX.md`
  - `brand/fambox/design-system/current.md`
- 簡単な使い方（「Library を Publish して各プロジェクトから Insert」）

---

## ステップ2: ページ構成（**10分**）

左サイドバーから「+」で **8ページ** 追加:

| # | ページ名 | 用途 |
|---|---|---|
| 0 | **Cover** | バージョン情報・更新履歴 |
| 1 | **Foundation** | 視覚軸6軸の説明・原則 |
| 2 | **Tokens** | 色・タイポ・余白・モーション・Layer Stack |
| 3 | **Primitives** | Button / Input / Icon / Avatar / FormControls / Progress / Badge |
| 4 | **Patterns** | FormField / Card / Tooltip / Alert |
| 5 | **Components** | Header / Drawer / Footer / Modal / Contact Form / Plan Card / Case Study |
| 6 | **Templates** | TOP / 定期便 / 問合せ / 購入完了 / 食事診断 |
| 7 | **Changelog** | 変更履歴 |

### Tip
- ページ名先頭に番号を付ける（`0. Cover`）→ 並び順固定
- 各ページの最初に大きな見出し Frame を配置（移動時の目印）

---

## ステップ3: Variables（Tokens）登録（**1-2時間 / CSV利用で60分**）

### 3-A. Local Variables 作成
1. 右サイドバー「Local variables」アイコン
2. 「+ Create variable collection」
3. Collection 名: **`FAMBOX Tokens`**
4. Modes: 単一 mode（後で Light/Dark 拡張可能）

### 3-B. カテゴリ別グループ化（推奨命名）

```
FAMBOX Tokens
├── color/
│   ├── brand/
│   │   ├── drive
│   │   ├── drive-light
│   │   ├── sky
│   │   └── deep
│   ├── ink/
│   │   ├── ink
│   │   ├── sub
│   │   ├── caption
│   │   ├── placeholder
│   │   └── white
│   ├── bg/
│   │   ├── primary
│   │   ├── secondary
│   │   └── tertiary
│   ├── border/
│   │   ├── light
│   │   ├── base
│   │   └── subtle
│   ├── semantic/
│   │   ├── success
│   │   ├── warning
│   │   ├── error
│   │   └── info
│   └── alias/
│       ├── cta
│       ├── focus-ring
│       ├── link-on-light
│       ├── link-on-dark
│       ├── link-on-drive
│       ├── price-accent
│       └── error-text
├── space/
│   ├── 1 (8px)
│   ├── 2 (16px)
│   └── ... 8 (160px)
├── radius/
│   ├── sm (4px)
│   ├── md (8px)
│   ├── pill-cta (50px)
│   └── pill (9999px)
├── layer/
│   ├── base (0)
│   ├── 1, 2, 3, 4, 5, 6
│   └── legacy-sticky-cta (9990)
└── motion/
    ├── duration-fast (150)
    ├── duration-base (300)
    ├── duration-slow (600)
    └── duration-breath (2000)
```

### 3-C. CSV 一括インポート（時短）
Figma Plugin **「Variables Import」** または **「Tokens Studio」** を使う。

#### 推奨: Tokens Studio for Figma
1. Figma Community Plugin 「Tokens Studio for Figma」インストール
2. Plugin で `tokens.css` を JSON 形式に変換してインポート
3. Figma Variables に同期

#### 手作業時の効率化
- 色は HEX 16進数を直接入力（例: `#FB4C15`）
- スペーシング・モーション等の数値は CSV で持ち込み Figma 内コピペ

→ 私が「**Figma Variables 用 JSON ファイル**」を生成可能。下記コマンドで投入可能形式にします。

---

## ステップ4: Text Styles 登録（**30分**）

`typography.md` の Preset を Text Style 化:

| Preset | Figma Style 名 |
|---|---|
| Display | `text/display` |
| H1 | `text/h1` |
| H2 | `text/h2` |
| H3 | `text/h3` |
| Lead | `text/lead` |
| Body | `text/body` |
| Body Small | `text/body-sm` |
| Caption | `text/caption` |
| Stat | `text/stat` |

各 Style:
- Font: Poppins (英) / Hiragino Sans (日) — 別Style or Font 切替可能ノード
- Size, Weight, Line Height, Letter Spacing を設定
- 「+ Save as style」で保存

---

## ステップ5: Effect Styles 登録（**15分**）

`tokens.css` の Shadow を Effect Style に:

| Style 名 | 値 |
|---|---|
| `shadow/1` | 0 1px 2px rgba(0,0,0,0.04) |
| `shadow/2` | 0 2px 8px rgba(0,0,0,0.06) |
| `shadow/3` | 0 4px 16px rgba(0,0,0,0.08) |
| `shadow/4` | 0 8px 32px rgba(0,0,0,0.12) |
| `shadow/5` | 0 16px 64px rgba(0,0,0,0.16) |

---

## ステップ6: Icon Component 取り込み（**2-3時間**）

### 方法A: 一括インポート（推奨）
1. **Figma Community Plugin「SVG to Component」** インストール
2. Page `3. Primitives` に Icon Frame グループを作る
3. 9カテゴリ別にセクション分割
4. `brand/shared/icons/{category}/` の SVG を一括ドラッグ&ドロップ
5. 全選択 → 「Create Component」

### 命名規則（重要）
Figma 内のコンポーネント名は **スラッシュ `/` で階層化**:

```
icon/nav/close-ink
icon/nav/close-white
icon/nav/close-drive
icon/nav/back-ink
...
icon/domain/athlete-ink
icon/domain/athlete-white
icon/domain/athlete-drive
```

→ Figma Assets パネルで自動的にフォルダ階層化される

### 方法B: 手作業（時間あり時）
1. SVG を1個ずつドラッグ
2. Component化（Cmd+Alt+K）
3. 命名規則で名前付け

---

## ステップ7: Library 公開（**5分**）

1. 右サイドバー「Assets」
2. 「Publish styles and components」
3. Library 名: **`FAMBOX Design System`**
4. Description 記入: バージョン・更新内容
5. 「Publish」

### 利用方法（各プロジェクトファイル）
1. プロジェクトファイルで「Assets」パネル
2. 「Library を有効化」
3. `FAMBOX Design System` をオン
4. Component を Insert で利用可能

---

## 想定スケジュール

| 段階 | 想定時間 | 推奨実施日 |
|---|---|---|
| ステップ1-2（枠作り） | 30分 | 今週中 |
| ステップ3（Variables / CSV利用） | 60分 | 今週中 |
| ステップ4-5（Text/Effect Styles） | 45分 | 今週中 |
| ステップ6（Icon Components） | 2-3時間 | 来週前半 |
| ステップ7（Library公開） | 5分 | 来週前半 |
| Primitive デザイン追加 | 4-6時間 | 来週後半 |
| Pattern デザイン追加 | 3-4時間 | 5月第1週 |
| Component デザイン追加 | 6-8時間 | 5月第2週 |
| **合計** | **18-24時間** | **5月中旬完成** |

---

## CSV / JSON 出力依頼（Claude側）

宮川さんが「Variables 用 CSV/JSON が欲しい」と言えば、**私が tokens.css から Tokens Studio 互換 JSON を即時生成**します。

例:
```json
{
  "color": {
    "drive": { "value": "#FB4C15", "type": "color" },
    "sky": { "value": "#3DB8E8", "type": "color" }
  },
  "space": {
    "1": { "value": "8px", "type": "spacing" },
    "2": { "value": "16px", "type": "spacing" }
  }
}
```

---

## 運用ルール

### Tokens 変更時
1. 必ず `tokens.css` を先に更新（SSoT）
2. Figma Variables を tokens.css に合わせて更新
3. 各 Style の値を更新
4. CHANGELOG.md に記録

### 新Component 追加時
1. `components/{name}.md` 仕様書を先に作成
2. Figma で Component 化
3. 命名規則に沿った名称で公開
4. INDEX.md / CHANGELOG.md 更新

### 廃止 (Deprecate) 時
1. Figma で Component 名を `_deprecated/` 配下に移動
2. 2バージョン並存後に削除
3. CHANGELOG.md に記録

---

## トラブルシューティング

### Variables が反映されない
- Library を再 Publish
- プロジェクト側で Library の Update を承認

### Component の差分が大きい
- Component の "Reset" で Master に戻す
- Override が必要な場合は Variant を作る

### Icon の色が変えられない
- Layer に「Vector」しか含まれていないか確認
- Vector の Stroke を Solid → Variable 参照に変更

---

## 関連ファイル
- [tokens/tokens.css](../tokens/tokens.css) — SSoT
- [tokens/colors.md](../tokens/colors.md) — 色仕様
- [tokens/typography.md](../tokens/typography.md) — タイポ仕様
- [tokens/icon-creation-spec.md](../tokens/icon-creation-spec.md) — アイコン作成仕様
- [shared/icons/README.md](../../../shared/icons/README.md) — アイコンライブラリ
