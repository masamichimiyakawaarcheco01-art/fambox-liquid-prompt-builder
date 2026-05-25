# ARCHITECTURE — FAMBOX Design Flywheel

> 4層構造の正典。新規設計や実装判断はここを基準にする。
> このファイルが「真実の単一ソース（Single Source of Truth）」。

---

## 全体図

```
┌─────────────────────────────────────────────────────────────────┐
│  Brand Layer（ブランド設定 — 入れ替え可能）                     │
│                                                                 │
│   ┌────────────┐  ┌────────────┐  ┌────────────┐                │
│   │  FAMBOX    │  │  Brand B   │  │  Brand C   │  ...           │
│   │ ・Brand DNA│  │ ・Brand DNA│  │ ・Brand DNA│                │
│   │ ・DS v0.x  │  │ ・DS       │  │ ・DS       │                │
│   │ ・Templates│  │ ・Templates│  │ ・Templates│                │
│   └─────┬──────┘  └────────────┘  └────────────┘                │
└─────────┼───────────────────────────────────────────────────────┘
          │
┌─────────┼───────────────────────────────────────────────────────┐
│  Engine Layer（ブランド非依存 — 共通コア）                      │
│         ↓                                                       │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │ Sense    │ →  │ Generate │ →  │ Reach    │ →  │ Learn    │  │
│  │          │    │          │    │          │    │          │  │
│  │GA4       │    │Claude    │    │Shopify   │    │ KPI 追跡  │  │
│  │Shopify   │    │Brand     │    │Canva     │    │ A/B結果   │  │
│  │SNS API   │    │Brain     │    │SNS API   │    │ アセット  │  │
│  │User行動  │    │+ DS      │    │メール    │    │ 履歴      │  │
│  │Insight   │    │+ Bugs    │    │PDF       │    │ 反省ログ  │  │
│  │Engine    │    │+ DNA     │    │          │    │          │  │
│  └──────────┘    └──────────┘    └──────────┘    └──────┬───┘  │
│       ↑                                                  │      │
│       └──────────────────────────────────────────────────┘      │
│            （Learn の結果が次の Sense にフィードバック）        │
└─────────────────────────────────────────────────────────────────┘
          │
┌─────────┼───────────────────────────────────────────────────────┐
│  Data Layer（長期記憶 — Second Brain）                          │
│                                                                 │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│   │ Performance  │  │ Asset Library│  │ Brand Memory │          │
│   │ History      │  │              │  │ Graph        │          │
│   │ ・CTR/CVR    │  │ ・過去画像   │  │ ・bugs.md    │          │
│   │ ・売上連動   │  │ ・過去Liquid │  │ ・feedback   │          │
│   │ ・SNS反応    │  │ ・過去コピー │  │ ・DNA        │          │
│   └──────────────┘  └──────────────┘  └──────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3つの設計原則

### 原則 1：ブランド層とエンジン層を完全に分離

| 層 | 例 | 配置 |
|---|---|---|
| Brand Layer | FAMBOX 色 / Poppins / Editorial × Lab | `brand/fambox/` |
| Engine Layer | 生成ロジック / API 呼び出し / Lint | `engine/` または `scripts/` |

**ルール：** エンジン層のコードに「FAMBOX 固有の文字列・値」を埋め込まない。すべて Brand Layer の設定ファイルから読む。

### 原則 2：Data Layer がホイールを回す燃料

各層が単体で動いても意味がなく、「ホイールを回した記録」が積み重なる場所が要る。
- 何を作ったか → Asset Library
- どう機能したか → Performance History
- 何を学んだか → Brand Memory Graph

既存の [brain/](../../../brain/) ディレクトリと memory システムをこの Data Layer として活用する。

### 原則 3：人間 + AI ハイブリッドから始める

最初から全自動を狙わない。各層で「人間の介在ポイント」を明示し、徐々に AI に置き換えていく。

| 層 | 初期（Phase 1） | 完成形 |
|---|---|---|
| Sense | AI が一次解釈 → 人間が確認 → 指示 | AI が異常検知し自動指示 |
| Generate | AI が選択肢生成 → 人間がピック | AI が自動選択 + 人間が承認 |
| Reach | 人間が手動配信 | パイプライン自動配信 |
| Learn | AI が集計 → 人間がインサイト記述 | AI が自動学習 → memory 更新 |

---

## 層別詳細

### 1. Brand Layer

#### 構成要素

| 要素 | 内容 | 既存資産 |
|---|---|---|
| Brand DNA | 視覚言語 + Verbal Identity | `brand/fambox/FAM_brand_DNA_v0.3.md` / Verbal v1.0 |
| Design System | tokens + components + patterns | `brand/fambox/design-system/` (DS v0.5) |
| Templates | 用途別テンプレ（Liquid / SNS画像 / 紙 等） | 部分的に存在 |

#### 4階層 DS 設計（マルチブランド化を見据えた抽象化）

```
tokens     → 色 / フォント / スペーシング / シャドウ等の基底値
components → ボタン / カード / フォーム等の再利用部品
patterns   → ヒーローセクション / FAQ / カルーセル等の構成パターン
templates  → ページ全体・配信フォーマット完成形
```

この4階層は **すべてのブランドが同じ階層を持つ**。中身（値）だけが入れ替わる。

### 2. Engine Layer

#### Sense（感知・発見）

**役割：** Web上のシグナル・自社データ・競合動向を常時監視し、人間が見落とす兆候を検知する。

**入力：**
- Shopify Analytics（売上 / コンバージョン / ファネル）
- GA4（行動 / 流入 / セッション）
- SNS API（Instagram / X など）
- ユーザー定性データ（レビュー / 問い合わせ / アンケート）

**既存資産：**
- 月曜08:03 自動実行の Design Insight Engine（FAMレモン君環境）
- 自動レポートシステム（[project_analytics_reporter.md](../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_analytics_reporter.md)）

**出力：** Generate 層への指示書（JSON）
```json
{
  "trigger": "weekly-review",
  "signals": [
    { "type": "low-ctr", "asset": "hero-banner-2026-05", "score": 0.3 }
  ],
  "request": "ヒーローバナーの新バリアントを3つ生成"
}
```

#### Generate（生成・解決）

**役割：** Sense からの指示に対し、ブランドルールに従い最適な解決策を自動生成する。

**入力：** Sense からの指示書 + Brand Layer 設定

**処理：**
1. Brand DNA を「世界観の制約」として読み込む
2. DS v0.5 を「実装の語彙」として読み込む
3. bugs.md 28規律を「禁止事項」として適用
4. Claude API で生成

**出力：** 用途別アセット
- Liquid セクションコード
- SNS 画像（PNG / JPG）
- 紙印刷物 PDF
- メール HTML
- プレゼン PPTX

**既存資産：**
- LPB v4.1（プロンプトビルダー）
- FAMBOX DS v0.5
- bugs.md 28規律

**マレルチーム向けの操作レイヤー：**
- フォーム入力 UI（Web）→ 内部で LPB プロンプトに変換
- 出力を Canva / Figma にコピペできる形式で返す

#### Reach（到達・サポート）

**役割：** 生成されたアセットを顧客との接点に配信する。

**配信先：**
- Shopify（直接 push）
- Canva（テンプレ反映）
- メール（Klaviyo / Seal）
- SNS（Instagram / X、API or 手動）
- 印刷物（PDF → 印刷会社）

**既存資産：** 上記すべて単体では稼働済み。**パイプライン化が未着手**。

#### Learn（学習・再発見）

**役割：** エンゲージメントから得たシグナルを継続学習し、次の Sense へ繋げる。

**学習対象：**
- どのアセットを使ったか（手動記録 → 自動記録へ）
- どの KPI が改善 / 悪化したか
- ユーザーからの反応（コメント / DM / レビュー）
- 反省ログ（うまくいかなかった理由）

**出力先：** Data Layer の Performance History + Brand Memory Graph

**既存資産：**
- brain/40_Bookmarks（X取込）
- sessions index（過去セッション）

### 3. Data Layer

#### 構成

| 種別 | 内容 | 既存配置 |
|---|---|---|
| Performance History | KPI 履歴 / A/B 結果 / 売上連動 | Google Sheets（要構造化） |
| Asset Library | 過去アセット（画像 / Liquid / コピー） | `brain/` + Shopify Files |
| Brand Memory Graph | bugs.md / feedback / DNA | `~/.claude/projects/*/memory/` |

#### アクセス API

エンジン層から Data Layer へのアクセスは抽象化する：
```
read_performance(asset_id, period) → KPI履歴
read_assets(filter)               → 過去アセット
read_brand_memory(query)          → Brand 知識
write_outcome(asset_id, result)   → 結果記録
```

これにより、データの実体（Sheets / DB / ファイル）が変わってもエンジン側は影響を受けない。

---

## マルチブランド化への布石

設計時から守るべき3つの原則：

1. **Brand-specific 情報は外部設定ファイルに切り出す**
2. **DS は 4階層（tokens / components / patterns / templates）で抽象化**
3. **Output adapter は ブランド・フォーマット非依存** に設計（[project_brand_output_expansion.md](../../../.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_brand_output_expansion.md) ストリーム E と整合）

ただし **FAMBOX を完璧に回してから抽象化する**（Linear / Vercel / Stripe の DS 進化パターンに倣う）。

---

## バージョン履歴

| バージョン | 日付 | 内容 |
|---|---|---|
| v0.1 | 2026-05-22 | 初稿。キックオフブレストの結論を記録 |
