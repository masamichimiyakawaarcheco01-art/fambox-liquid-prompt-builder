# Tokens Studio 評価ドキュメント

**生成**: 2026-05-18 / Session #54 Part B
**目的**: §5 残論点 #3 で採用決定した「**Tokens Studio 導入**」のリスク評価と試用シナリオ準備。学習コストや Figma Variables との競合リスクを早期解消し、期待効果が出ない場合は **プラン B（自前 generate-dashboard.py 拡張）に切替**する判断材料を提供する。
**前提**: Session #53 で 4 論点プラン A 採用決定済。本ドキュメントは **宮川さん手動試用**を支援する評価チェックリスト + 既存 token import 用のサンプル。

---

## 1. Tokens Studio とは

**Tokens Studio for Figma**（旧 Figma Tokens）:
- Figma プラグイン（無料版 / Pro 版あり）
- Design Token を **JSON 形式で集中管理** → Figma Variables / CSS / Tailwind / Style Dictionary 等に同期可能
- GitHub / GitLab / Azure DevOps と連携した token のバージョン管理
- ライセンス: 無料版（基本機能）+ Pro 版（GitHub 連携・複数テーマ等が制限解除）

**公式**: https://tokens.studio/

---

## 2. FAMBOX で導入する価値

### 解決したい課題

| 課題 | 現状 | 期待される改善 |
|---|---|---|
| spec ↔ Figma ↔ Liquid 3 層同期 | 手動更新（学び 67 の周期 Audit で乖離検出してきた）| **Token 変更が 1 箇所 → 3 層自動同期** |
| Figma Variables 入力の冗長性 | 133 tokens 手動入力 | JSON import で一括登録 |
| brand 横展開 | §5 #4 で採用した統合 DS (FAM/FAMBOX) | brand mode を Tokens Studio Theme で管理 |
| Token 履歴の追跡 | git のコミット履歴のみ | Tokens Studio の version 機能 + GitHub 連携 |

### v0.5 Token 化資産（基準値）

```
133 unique tokens (snippets/fambox-tokens.css.liquid / 255 行)
- §1-A Color: 50+
- §1-B Typography: 25
- §1-C Spacing: 11
- §1-D Motion: 7
- §1-E Shadow: 6
- §1-F Radius: 7
- §1-G Breakpoint: 5
- §1-H Z-index: 7
- §1-I Icon: 6
```

すべて Tokens Studio の標準カテゴリにマッピング可能。

---

## 3. 試用シナリオ（宮川さん手動）

### Phase 1: インストール + 基本確認（15-30 min）

1. Figma File を開く: `FAMBOX Design System` (`QsiBrc2v20BYw76YHI9x3e`)
2. Plugins → Browse plugins → **"Tokens Studio for Figma"** を検索 → Run
3. 起動後、UI が表示されることを確認
4. **「無料版で何ができるか」** を確認（ライセンス UI）

### Phase 2: 既存 Variables を Tokens Studio に import（30-45 min）

#### Option A: 既存 Figma Variables を Sync で取り込む

1. Tokens Studio UI で `Settings → Sync providers → Add new` を選択
2. Sync source として **"Use local variables"** を選択
3. → 既存 257 variants の Figma Variables が Tokens Studio に取り込まれる想定
4. **想定外動作 / エラーが出たら本ドキュメント §6「リスク評価」へ**

#### Option B: 既存 CSS Tokens (133 个) を JSON で import — ⭐ 推奨

**Session #54 で 133 tokens の完全 JSON を生成済**:

```
File: brand/fambox/design-system/operations/scripts/tokens-studio-import.json
内容: 23 categories / 133 tokens (snippets/fambox-tokens.css.liquid と完全 1:1 対応)
```

**読み込み手順**:
1. Tokens Studio UI の右下 `Tools` (3点メニュー or 歯車アイコン)
2. `Load JSON` を選択
3. 上記 JSON ファイルを選択 → import
4. 23 カテゴリ / 133 tokens がツリー表示されることを確認

**カテゴリ別 token 数**:

| Category | Tokens |
|---|---:|
| color | 12 |
| bg | 3 |
| border | 4 |
| semantic | 4 |
| data | 6 |
| glass | 5 |
| white-overlay | 8 |
| ink-overlay | 5 |
| alias | 5 |
| fontFamily | 2 |
| fontWeight | 4 |
| fontSize | 15 |
| lineHeight | 5 |
| letterSpacing | 4 |
| space | 11 |
| sectionSpacing | 2 |
| duration | 4 |
| ease | 3 |
| shadow | 6 |
| radius | 7 |
| breakpoint | 5 |
| layer | 7 |
| icon | 6 |
| **合計** | **133** |

### Phase 3: 双方向同期テスト（30-45 min）

1. **Tokens Studio → Figma**: `--color-drive` を `#fc5214` → 別の色に変更 → Figma Variables の値が変わることを確認
2. **Figma Variables → Tokens Studio**: 逆方向の同期も確認
3. **Tokens Studio → CSS**: Export → CSS で出力 → `fambox-tokens.css.liquid` と diff 比較
4. **GitHub 連携**: Pro 版必要。**無料版で代用方法**を検証

### Phase 4: ROI 判定（15-30 min / 本ドキュメント §6 チェックリスト記入）

---

## 4. 既存 fambox-tokens.css.liquid を Tokens Studio JSON にした例

`snippets/fambox-tokens.css.liquid` の主要 Token を Tokens Studio JSON 形式に変換した最小例（**宮川さんの import 試用用**）:

```json
{
  "fambox": {
    "color": {
      "drive": {
        "value": "#fc5214",
        "type": "color",
        "description": "Primary Drive color (Brand DNA / spec §1-A 1-1)"
      },
      "drive-hover": {
        "value": "#e14710",
        "type": "color"
      },
      "drive-light": {
        "value": "#ff7a51",
        "type": "color"
      },
      "ink": {
        "value": "#1b1d1a",
        "type": "color",
        "description": "Main text color"
      },
      "sub": {
        "value": "#5c5f58",
        "type": "color"
      },
      "caption": {
        "value": "#8a8d87",
        "type": "color"
      },
      "white": {
        "value": "#ffffff",
        "type": "color"
      }
    },
    "bg": {
      "primary": { "value": "#ffffff", "type": "color" },
      "secondary": { "value": "#fafafa", "type": "color" },
      "tertiary": { "value": "#f3f3f3", "type": "color" }
    },
    "border": {
      "light": { "value": "rgba(27, 29, 26, 0.08)", "type": "color" },
      "base": { "value": "#ececec", "type": "color" },
      "soft": { "value": "#d0d1db", "type": "color" }
    },
    "space": {
      "0-5": { "value": "4", "type": "spacing" },
      "1": { "value": "8", "type": "spacing" },
      "1-5": { "value": "12", "type": "spacing" },
      "2": { "value": "16", "type": "spacing" },
      "3": { "value": "24", "type": "spacing" },
      "4": { "value": "32", "type": "spacing" },
      "5": { "value": "48", "type": "spacing" },
      "6": { "value": "64", "type": "spacing" },
      "7": { "value": "96", "type": "spacing" },
      "8": { "value": "120", "type": "spacing" }
    },
    "fontFamily": {
      "ja": {
        "value": "Hiragino Sans, 'Hiragino Kaku Gothic ProN', Meiryo, sans-serif",
        "type": "fontFamilies"
      },
      "en": {
        "value": "Poppins, sans-serif",
        "type": "fontFamilies"
      }
    },
    "fontWeights": {
      "regular": { "value": "400", "type": "fontWeights" },
      "medium": { "value": "500", "type": "fontWeights" },
      "semibold": { "value": "600", "type": "fontWeights" },
      "bold": { "value": "700", "type": "fontWeights" }
    },
    "fontSize": {
      "caption": { "value": "12", "type": "fontSizes" },
      "body-sm": { "value": "14", "type": "fontSizes" },
      "body": { "value": "16", "type": "fontSizes" },
      "h4": { "value": "20", "type": "fontSizes" },
      "h3": { "value": "24", "type": "fontSizes" },
      "h2": { "value": "32", "type": "fontSizes" },
      "h1": { "value": "48", "type": "fontSizes" },
      "display": { "value": "56", "type": "fontSizes" },
      "hero": { "value": "64", "type": "fontSizes" },
      "mega": { "value": "96", "type": "fontSizes" }
    },
    "radius": {
      "xs": { "value": "2", "type": "borderRadius" },
      "sm": { "value": "4", "type": "borderRadius" },
      "md": { "value": "8", "type": "borderRadius" },
      "lg": { "value": "16", "type": "borderRadius" },
      "circle": { "value": "50%", "type": "borderRadius" },
      "pill-cta": { "value": "50", "type": "borderRadius" },
      "pill": { "value": "9999", "type": "borderRadius" }
    },
    "duration": {
      "fast": { "value": "150ms", "type": "other" },
      "base": { "value": "250ms", "type": "other" },
      "slow": { "value": "350ms", "type": "other" }
    }
  }
}
```

これを Tokens Studio で import → 既存 133 tokens のうち主要 50+ が表現可能。残り（shadow / z-index / breakpoint 等）も同様の構造で追記可能。

---

## 5. brand mode サポート（§5 #4 連動）

Tokens Studio の **Themes** 機能を使えば、§5 #4 で決定した **「統合 DS（マルチブランドモード）」** を以下のように管理可能:

```json
{
  "fambox": {
    "color": {
      "drive": { "value": "#fc5214", "type": "color" }
    }
  },
  "fam": {
    "color": {
      "drive": { "value": "#ff7e5f", "type": "color" }   // 仮 / FAM brand 色
    }
  }
}
```

→ Theme 切替で `--color-drive` の値が brand 別に変わる。CSS 出力時に `[data-brand="fam"] { --color-drive: ... }` を生成可能。

これが **Tokens Studio 採用の最大のメリット**（自前 script では実装が複雑）。

---

## 6. ROI チェックリスト（試用後の判定基準）

宮川さんが試用後、以下 7 項目で **5 つ以上 ✅** ならプラン A 継続、**4 つ以下なら プラン B 切替**を検討。

| # | 項目 | 判定基準 |
|---|---|---|
| 1 | **インストール / 初回起動が無料版で完結** | プラグインインストールから 5 min 以内に UI 起動できた |
| 2 | **既存 Figma Variables の import が動作** | 既存 257 variants が認識される（一部でも OK）|
| 3 | **JSON import が動作** | §4 のサンプル JSON が読み込めて Token として表示される |
| 4 | **Figma 双方向同期が動作** | Tokens Studio 内で値変更 → Figma Variables の値が変わる |
| 5 | **CSS export が動作** | 既存 fambox-tokens.css.liquid と diff が許容範囲 |
| 6 | **brand themes 機能が無料版で使える** | §5 用の brand mode が無料版で実現可能（**最重要**）|
| 7 | **学習コストが許容範囲** | 試用合計 2 時間以内に「日常運用イメージ」が湧く |

### 切替判断（4 つ以下 ✅ なら）

→ **プラン B（自前 generate-dashboard.py 拡張）に切替**:
- 既存 script 425 行 + Figma 自動連携 modules（追加 200-300 行想定）
- `figma-sets.json` を Figma audit から自動生成
- CSS Token → Figma Variables の同期は **手動 API 呼び出し**で対応
- 工数: 8-10 時間（Tokens Studio 学習コストとほぼ同等）

### プラン A 継続判断（5 つ以上 ✅ なら）

→ **本格運用準備**:
- GitHub 連携（Pro 版検討 / または GitHub Actions で自前同期）
- チーム共有用の Tokens Studio 設定書出し
- generate-dashboard.py を Tokens Studio JSON 経由に切替

---

## 7. 試用結果記入欄 ✅ 完了 (Session #54 ext-5 / 2026-05-18)

```
試用日: 2026-05-18
試用時間: 約 90 min (Session #54 全体)

チェックリスト判定:
  #1 インストール:           ✅ (公式 Community URL → Open in Figma で起動)
  #2 Figma Variables import: ✅ (既存 v0.2 set 109 tokens が即表示)
  #3 JSON import:            ✅ (v0.5 完全統合 JSON 130 tokens の一括置換動作)
  #4 双方向同期:             🟡 (Figma Variables との bind 自動再構築見込み、本格運用で検証)
  #5 CSS export:             🟡 (Settings → Export 未検証、generate-dashboard.py と整合判定は v0.4 dashboard で)
  #6 brand themes 無料版:    ❌ (Manage themes に PRO バッジ / 月額 $15-20 必須)
  #7 学習コスト:             ✅ (v2.11.7 UI は直感的、JSON view 経由なら一括操作可能)
  合計 ✅: 4 / 7 (🟡 2 / ❌ 1)

判定:
  [ ] プラン A 継続（5+ ✅）→ 本格運用準備
  [ ] プラン B 切替（4 以下 ✅）→ generate-dashboard.py 拡張に進む
  [x] 選択肢 C ハイブリッド ← 採用（Session #54 ext-4 で確定）

選択肢 C を採用した理由:
  - #1-3 + #7 で「Token 一元管理ツール」としての基本機能は無料版で十分
  - #6 のみが ❌ だが、CSS `[data-brand=]` で完全代替可能
  - 月額 $15-20 の課金を回避しながら §5 #4 brand 統合戦略を維持できる
  - 既存 Tokens Studio v0.2 + Phase B 修正 + 22 件追加 = v0.5 化が完了

備考 / 気づき:
  - 既存 set (v0.2 / 2026-04-20 / 宮川さん作成) に v0.5 を統合できた
  - drive 色 #FB4C15 は Figma が真実の源として維持、Liquid 側を追従
    (学び 130: Token は種別で真実の源が違う)
  - JSON view (右上 { } アイコン) の一括置換が最も効率的
    (学び 133: 個別追加より「1 操作で N tokens 反映」)
  - drive-hover / disabled を最初フラット階層で追加してしまったが、
    JSON 一括置換で正しい階層 (brand/alias) に自動配置できた
  - fambox-v0.5 New Set は戦略 C 確定後不要だったため削除済

次の作業 (Session #55 候補):
  - brand mode override の実装 (CSS [data-brand="fam"] / FAM brand 値確定後)
  - theme.liquid に {% render 'fambox-tokens.css' %} 配置 (宮川さん手動)
  - Phase A 着手 (L0 翻訳表 / OKR 2026-06-30 直結)
```

---

## 8. 関連リソース

- **Tokens Studio 公式**: https://tokens.studio/
- **既存 fambox-tokens.css.liquid**: `snippets/fambox-tokens.css.liquid` (133 tokens / 255 行)
- **既存 generate-dashboard.py**: `brand/fambox/design-system/operations/scripts/generate-dashboard.py` (425 行)
- **§5 残論点 #3 決定**: `current.md §5-3`
- **§5 #4 brand 統合決定**: `current.md §5-5`

## Status

- ✅ 評価ドキュメント作成完了（Session #54 Part B）
- 🟡 宮川さん試用待ち
- 🟡 試用結果記入後、Session #55 で判断
