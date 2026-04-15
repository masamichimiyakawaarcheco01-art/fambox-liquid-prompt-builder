# GA4 Design Insight Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** GA4データからデザイン改善提案を自動生成し、Googleスプレッドシートに書き込んだ後、Slack MCPで宮川にDM通知するシステムを構築する（FAMレモン君環境のPhase 1）

**Architecture:** Claude scheduled task が毎週月曜08:00に起動 → Python script (`design_insight.py`) がSheetsからデータ読込→Claude APIに分析依頼→結果をシート書き込み→Claudeタスクが実行結果を読取り→Slack MCPでDM送信

**Tech Stack:** Python 3 / gspread / google-analytics-data / anthropic SDK / Slack MCP / scheduled-tasks MCP

---

## File Structure

**Base directory:** `/Users/archecoinc./Desktop/Claude_1/projects/analytics/`

**Create:**
- `design_insight.py` - メインスクリプト（データ収集 + Claude API呼び出し + シート書き込み）
- `section_mapping.json` - URLパス→Liquidセクションファイルのマッピング
- `prompts/design_insight_system.md` - Claude APIへ渡すシステムプロンプト
- `tests/__init__.py` - テストパッケージ初期化
- `tests/test_design_insight.py` - ユニットテスト
- `tests/fixtures/sample_daily_data.json` - テスト用サンプルデータ

**Modify:**
- `config.json` - `claude.api_key_env`, `slack.user_id_for_dm` を追加
- `requirements.txt`（存在しなければ新規作成）- `anthropic>=0.34.0` を追加

**Existing files referenced (read only):**
- `weekly_insight_report.py` - データ集計パターンの参考
- `daily_collect.py` - ラベルマップパターンの参考

---

## Task 1: 依存パッケージと設定の準備

**Files:**
- Create: `projects/analytics/requirements.txt`
- Modify: `projects/analytics/config.json`

- [ ] **Step 1: requirements.txtを作成**

```
anthropic>=0.34.0
gspread>=6.0
google-auth>=2.0
google-analytics-data>=0.18
requests>=2.30
```

- [ ] **Step 2: venvでanthropicをインストール**

Run:
```bash
/Users/archecoinc./Desktop/Claude_1/projects/analytics/venv/bin/pip install 'anthropic>=0.34.0'
```
Expected: `Successfully installed anthropic-x.x.x ...`

- [ ] **Step 3: config.jsonに設定追加**

既存の`config.json`の`slack`セクションを拡張し、`claude`セクションを追加。以下のフィールドを追加:

```json
{
  "claude": {
    "api_key_env": "ANTHROPIC_API_KEY",
    "model": "claude-opus-4-6",
    "max_tokens": 4096
  },
  "slack": {
    "webhook_url": "(既存を維持)",
    "user_id_for_dm": "U_REPLACE_ME"
  }
}
```

ユーザーがAPIキーを環境変数に設定する前提。user_id_for_dmは「DMの宛先Slack User ID」で、運用開始時に実測で設定する。

- [ ] **Step 4: .gitignoreを確認**

Run:
```bash
grep -E "config.json|service_account|token" /Users/archecoinc./Desktop/Claude_1/.gitignore
```
Expected: config.json等が含まれていない場合は秘匿情報漏洩リスク。ただし既存運用を尊重し、この時点では警告のみ。

- [ ] **Step 5: Commit**

```bash
git add projects/analytics/requirements.txt projects/analytics/config.json
git commit -m "chore: add anthropic dep and claude config for design insight engine"
```

---

## Task 2: セクションマッピング定義

**Files:**
- Create: `projects/analytics/section_mapping.json`

- [ ] **Step 1: マッピングJSON作成**

ページパス→Liquidセクションファイルの対応表。以下の内容で作成:

```json
{
  "description": "GA4のページパスとShopify Liquidセクションファイルの対応マッピング。直帰率やPVが問題のあるページを特定した際、どのセクションを改修すべきかを特定するための基礎データ。",
  "routes": [
    {
      "path": "/",
      "label": "トップページ",
      "sections": [
        "fambox-hero-v17-video.liquid",
        "fambox-plan-features.liquid",
        "fambox-menu-showcase.liquid",
        "fambox-value-proposition.liquid",
        "fambox-easy-cooking.liquid",
        "fambox-faq.liquid",
        "fambox-profile.liquid",
        "fambox-model-case.liquid",
        "fambox-interview.liquid",
        "fambox-spirit.liquid",
        "fambox-subscription-plan.liquid",
        "fambox-active-plans-v2.liquid",
        "fambox-nutrition-service.liquid",
        "fambox-blog-carousel.liquid"
      ]
    },
    {
      "path": "/pages/company",
      "label": "法人LP",
      "sections": [
        "fam-corp-hero.liquid",
        "fam-corp-issues.liquid",
        "fam-corp-solution.liquid",
        "fam-corp-supervisor.liquid",
        "fam-case-study.liquid"
      ]
    },
    {
      "path": "/pages/contact",
      "label": "お問い合わせ",
      "sections": ["fam-contact-channels.liquid"]
    },
    {
      "path": "/collections/plan30",
      "label": "プラン30",
      "sections": ["fam-collection-plan.liquid"]
    },
    {
      "path": "/collections/plan40",
      "label": "プラン40",
      "sections": ["fam-collection-plan.liquid"]
    },
    {
      "path": "/collections/plan50",
      "label": "プラン50",
      "sections": ["fam-collection-plan.liquid"]
    },
    {
      "path": "/collections/plan60",
      "label": "プラン60",
      "sections": ["fam-collection-plan.liquid"]
    },
    {
      "path": "/blogs/news",
      "label": "Blog一覧",
      "sections": ["fam-blog-posts.liquid"]
    }
  ],
  "generic_sections": {
    "header": "header.liquid",
    "footer": "fam-footer-v2.liquid"
  }
}
```

- [ ] **Step 2: Commit**

```bash
git add projects/analytics/section_mapping.json
git commit -m "feat(analytics): add URL path to Liquid section mapping"
```

---

## Task 3: システムプロンプト作成

**Files:**
- Create: `projects/analytics/prompts/design_insight_system.md`

- [ ] **Step 1: プロンプトディレクトリ作成とファイル書き込み**

```bash
mkdir -p /Users/archecoinc./Desktop/Claude_1/projects/analytics/prompts
```

以下の内容で `prompts/design_insight_system.md` を作成:

```markdown
# FAMBOX デザイン改善提案 生成プロンプト

あなたはUIデザイン改善のエキスパートです。FAMBOX（アスリート向け食事宅配サービス）のGA4/GSCデータを分析し、具体的で実行可能なデザイン改善提案を生成してください。

## 分析の原則

1. **相関ではなく因果を探す**: 「直帰率が高い」ではなく「ファーストビューでCTAが見えないため直帰している」のように仮説を立てる
2. **セクション単位で提案**: ページ全体ではなく、特定のLiquidセクションファイル名まで特定する
3. **優先度は「インパクト × 実装容易性」**: 訪問数が多く改善工数が小さいものを高優先度にする
4. **3つ以上、10件以内**: 提案を絞り込み、実行可能な数に留める

## デザイン原則（FAMBOX固有）

- 平面構成: シンプルな整数比（1:1, 1:2, 2:3）
- スペーシング: 等比率（1.5x/2x）でS/M/L
- タイポグラフィ: ジャンプ率でデザインテイスト制御
- CTAボタン: gradient背景、白テキスト、Hero v17ベース
- セクション上下余白: PC 120px / SP 80px

## Verbal Identity（法人LPは特に注意）

NG語: サポート / 支える / 伴走
推奨語: 動かす / 原動力 / 共に走り抜く / 冷静 / 情熱

## 出力形式

**必ず以下のJSONスキーマに準拠してください**:

```json
{
  "summary": "今週の全体傾向を1-2文で",
  "proposals": [
    {
      "priority": "高|中|低",
      "effort": "小|中|大",
      "page_path": "/pages/company",
      "page_label": "法人LP",
      "section_file": "fam-corp-hero.liquid",
      "metric": "直帰率",
      "current_value": "78%",
      "benchmark": "平均65%",
      "problem_hypothesis": "ファーストビューでCTAが見えない/情緒的コピーのみで行動喚起が弱い",
      "proposal": "CTAボタン（資料DLと問い合わせ）を画面上部（スクロール0地点）に移動し、`原動力を動かす`などの動詞起点コピーに変更",
      "expected_impact": "直帰率 65% 以下へ / 資料DL数 +30%",
      "kr_alignment": "KR-1 (ブランド) + KR-3 (直帰率改善)"
    }
  ]
}
```

JSONのみ出力してください。他のテキストは不要です。

## コンテキスト

以降のユーザーメッセージで以下を提供します:
- 対象週のサマリー指標（今週 vs 前週）
- ページ別パフォーマンス（PV/検索クリック/表示）
- 流入元別セッション
- 検索キーワード（GSC）
- ページパス→セクションファイルのマッピング
- OKR構造（KR1-5）

これらから上記JSON形式で改善提案を出力してください。
```

- [ ] **Step 2: Commit**

```bash
git add projects/analytics/prompts/design_insight_system.md
git commit -m "feat(analytics): add design insight system prompt"
```

---

## Task 4: テストフィクスチャ作成

**Files:**
- Create: `projects/analytics/tests/__init__.py`
- Create: `projects/analytics/tests/fixtures/sample_daily_data.json`

- [ ] **Step 1: テストディレクトリ作成**

```bash
mkdir -p /Users/archecoinc./Desktop/Claude_1/projects/analytics/tests/fixtures
touch /Users/archecoinc./Desktop/Claude_1/projects/analytics/tests/__init__.py
```

- [ ] **Step 2: サンプルデータ作成**

`tests/fixtures/sample_daily_data.json` に以下を書き込む:

```json
{
  "daily": [
    {"日付": "2026-04-08", "訪問回数（セッション）": 42, "訪問者数（ユニークユーザー）": 28, "直帰率（1ページだけ見て離脱した割合%）": 72.5, "注文数": 1, "売上（円）": 7560, "検索クリック数（GSC）": 3, "検索表示回数（GSC）": 45},
    {"日付": "2026-04-09", "訪問回数（セッション）": 38, "訪問者数（ユニークユーザー）": 25, "直帰率（1ページだけ見て離脱した割合%）": 68.2, "注文数": 2, "売上（円)": 12800, "検索クリック数（GSC）": 5, "検索表示回数（GSC）": 52},
    {"日付": "2026-04-10", "訪問回数（セッション）": 45, "訪問者数（ユニークユーザー）": 30, "直帰率（1ページだけ見て離脱した割合%）": 75.1, "注文数": 1, "売上（円）": 6420, "検索クリック数（GSC）": 2, "検索表示回数（GSC）": 48},
    {"日付": "2026-04-11", "訪問回数（セッション）": 35, "訪問者数（ユニークユーザー）": 22, "直帰率（1ページだけ見て離脱した割合%）": 70.0, "注文数": 0, "売上（円）": 0, "検索クリック数（GSC）": 4, "検索表示回数（GSC）": 55},
    {"日付": "2026-04-12", "訪問回数（セッション）": 30, "訪問者数（ユニークユーザー）": 20, "直帰率（1ページだけ見て離脱した割合%）": 73.5, "注文数": 1, "売上（円）": 8200, "検索クリック数（GSC）": 3, "検索表示回数（GSC）": 50},
    {"日付": "2026-04-13", "訪問回数（セッション）": 40, "訪問者数（ユニークユーザー）": 26, "直帰率（1ページだけ見て離脱した割合%）": 71.2, "注文数": 2, "売上（円）": 15400, "検索クリック数（GSC）": 6, "検索表示回数（GSC）": 58},
    {"日付": "2026-04-14", "訪問回数（セッション）": 37, "訪問者数（ユニークユーザー）": 24, "直帰率（1ページだけ見て離脱した割合%）": 69.8, "注文数": 1, "売上（円）": 7100, "検索クリック数（GSC）": 4, "検索表示回数（GSC）": 51}
  ],
  "page_views": [
    {"日付": "2026-04-08", "ページパス": "/pages/company", "ページ名": "法人LP", "閲覧数（PV）": 15, "閲覧者数（ユニークユーザー）": 10},
    {"日付": "2026-04-08", "ページパス": "/", "ページ名": "トップページ", "閲覧数（PV）": 20, "閲覧者数（ユニークユーザー）": 14},
    {"日付": "2026-04-08", "ページパス": "/pages/contact", "ページ名": "お問い合わせ", "閲覧数（PV）": 3, "閲覧者数（ユニークユーザー）": 3}
  ],
  "sources": [
    {"日付": "2026-04-08", "流入元": "ブックマーク・直接アクセス", "訪問回数": 18, "訪問者数": 12, "直帰率（%）": 78.5},
    {"日付": "2026-04-08", "流入元": "Google検索", "訪問回数": 14, "訪問者数": 10, "直帰率（%）": 60.2},
    {"日付": "2026-04-08", "流入元": "Instagram", "訪問回数": 6, "訪問者数": 4, "直帰率（%）": 82.3}
  ],
  "keywords": [
    {"日付": "2026-04-08", "検索キーワード": "fambox", "クリック数": 2, "表示回数": 28, "CTR(%)": 7.1, "平均掲載順位": 1.2},
    {"日付": "2026-04-08", "検索キーワード": "アスリート 食事 宅配", "クリック数": 1, "表示回数": 8, "CTR(%)": 12.5, "平均掲載順位": 2.1}
  ]
}
```

- [ ] **Step 3: Commit**

```bash
git add projects/analytics/tests/
git commit -m "test(analytics): add sample fixtures for design insight tests"
```

---

## Task 5: データ集計モジュール（TDD）

**Files:**
- Create: `projects/analytics/design_insight.py` (初版: データ集計のみ)
- Create: `projects/analytics/tests/test_design_insight.py`

- [ ] **Step 1: 失敗するテストを書く**

`tests/test_design_insight.py` に以下を書き込む:

```python
"""design_insight.py のユニットテスト"""

import json
import os
import sys
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from design_insight import aggregate_context, get_week_range


FIXTURE_PATH = os.path.join(os.path.dirname(__file__), "fixtures", "sample_daily_data.json")


def load_fixture():
    with open(FIXTURE_PATH) as f:
        return json.load(f)


def test_get_week_range_returns_monday_to_sunday():
    # 2026-04-15 (Wed) → Mon 2026-04-13 〜 Sun 2026-04-19
    monday, sunday = get_week_range(date(2026, 4, 15))
    assert monday == date(2026, 4, 13)
    assert sunday == date(2026, 4, 19)


def test_aggregate_context_summarizes_totals():
    data = load_fixture()
    ctx = aggregate_context(
        daily=data["daily"],
        page_views=data["page_views"],
        sources=data["sources"],
        keywords=data["keywords"],
    )
    assert ctx["totals"]["sessions"] == 267
    assert ctx["totals"]["users"] == 175
    assert ctx["totals"]["orders"] == 8
    # 直帰率は平均
    assert 69.0 < ctx["totals"]["avg_bounce_rate"] < 73.0


def test_aggregate_context_groups_pages():
    data = load_fixture()
    ctx = aggregate_context(
        daily=data["daily"],
        page_views=data["page_views"],
        sources=data["sources"],
        keywords=data["keywords"],
    )
    paths = {p["path"] for p in ctx["pages"]}
    assert "/pages/company" in paths
    assert "/" in paths


def test_aggregate_context_sorts_sources_by_sessions():
    data = load_fixture()
    ctx = aggregate_context(
        daily=data["daily"],
        page_views=data["page_views"],
        sources=data["sources"],
        keywords=data["keywords"],
    )
    assert ctx["sources"][0]["label"] == "ブックマーク・直接アクセス"
    assert ctx["sources"][0]["sessions"] == 18
```

- [ ] **Step 2: テストが失敗することを確認**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -m pytest tests/test_design_insight.py -v
```
Expected: FAIL（`design_insight` モジュールが未作成のため ImportError）

- [ ] **Step 3: 最小実装を書く**

`design_insight.py` を以下の内容で新規作成:

```python
"""
FAM Analytics - Design Insight Engine
GA4/GSCデータからLLMを使ってデザイン改善提案を生成し、Googleスプレッドシートに書き込む。

使い方:
  python design_insight.py              # 直近完了週のレポート生成
  python design_insight.py 2026-04-15   # 指定日を含む週
"""

import json
import os
import sys
from collections import defaultdict
from datetime import date, timedelta, datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_config():
    with open(os.path.join(BASE_DIR, "config.json")) as f:
        return json.load(f)


def get_week_range(ref_date: date):
    """月曜始まりの週範囲を返す（月〜日）"""
    monday = ref_date - timedelta(days=ref_date.weekday())
    sunday = monday + timedelta(days=6)
    return monday, sunday


def safe_float(val, default=0.0):
    try:
        return float(val) if val not in ("", None) else default
    except (ValueError, TypeError):
        return default


def safe_int(val, default=0):
    try:
        return int(float(val)) if val not in ("", None) else default
    except (ValueError, TypeError):
        return default


def col(row, *keys):
    """新旧ヘッダー両方に対応するカラム取得"""
    for k in keys:
        v = row.get(k)
        if v is not None and v != "":
            return v
    return 0


def aggregate_context(daily, page_views, sources, keywords):
    """取得済みデータを集計しLLM入力用コンテキストを返す"""
    total_sessions = sum(safe_int(col(r, "訪問回数（セッション）", "セッション")) for r in daily)
    total_users = sum(safe_int(col(r, "訪問者数（ユニークユーザー）", "ユーザー数")) for r in daily)
    total_orders = sum(safe_int(col(r, "注文数")) for r in daily)
    total_sales = sum(safe_int(col(r, "売上（円）", "売上(円)")) for r in daily)
    bounces = [safe_float(col(r, "直帰率（1ページだけ見て離脱した割合%）", "直帰率(%)")) for r in daily]
    bounces = [b for b in bounces if b > 0]
    avg_bounce = round(sum(bounces) / len(bounces), 1) if bounces else 0.0
    total_gsc_clicks = sum(safe_int(col(r, "検索クリック数（GSC）")) for r in daily)
    total_gsc_imps = sum(safe_int(col(r, "検索表示回数（GSC）")) for r in daily)

    # ページ集計
    page_agg = defaultdict(lambda: {"label": "", "views": 0, "users": 0})
    for r in page_views:
        path = r.get("ページパス", "")
        if not path:
            continue
        page_agg[path]["label"] = r.get("ページ名", path)
        page_agg[path]["views"] += safe_int(r.get("閲覧数（PV）"))
        page_agg[path]["users"] += safe_int(r.get("閲覧者数（ユニークユーザー）"))
    pages = [{"path": p, **v} for p, v in page_agg.items()]
    pages.sort(key=lambda x: x["views"], reverse=True)

    # 流入元集計
    src_agg = defaultdict(lambda: {"sessions": 0, "users": 0, "bounce": []})
    for r in sources:
        label = r.get("流入元", "不明")
        src_agg[label]["sessions"] += safe_int(r.get("訪問回数"))
        src_agg[label]["users"] += safe_int(r.get("訪問者数"))
        br = safe_float(r.get("直帰率（%）"))
        if br > 0:
            src_agg[label]["bounce"].append(br)
    src_list = []
    for label, v in src_agg.items():
        avg_br = round(sum(v["bounce"]) / len(v["bounce"]), 1) if v["bounce"] else 0.0
        src_list.append({"label": label, "sessions": v["sessions"], "users": v["users"], "bounce_rate": avg_br})
    src_list.sort(key=lambda x: x["sessions"], reverse=True)

    # キーワード集計
    kw_agg = defaultdict(lambda: {"clicks": 0, "impressions": 0, "positions": []})
    for r in keywords:
        q = r.get("検索キーワード", "")
        if not q:
            continue
        kw_agg[q]["clicks"] += safe_int(r.get("クリック数"))
        kw_agg[q]["impressions"] += safe_int(r.get("表示回数"))
        pos = safe_float(r.get("平均掲載順位"))
        if pos > 0:
            kw_agg[q]["positions"].append(pos)
    kw_list = []
    for q, v in kw_agg.items():
        avg_pos = round(sum(v["positions"]) / len(v["positions"]), 1) if v["positions"] else 0.0
        ctr = round(v["clicks"] / v["impressions"] * 100, 1) if v["impressions"] > 0 else 0.0
        kw_list.append({"query": q, "clicks": v["clicks"], "impressions": v["impressions"], "ctr": ctr, "position": avg_pos})
    kw_list.sort(key=lambda x: x["impressions"], reverse=True)

    return {
        "totals": {
            "sessions": total_sessions,
            "users": total_users,
            "orders": total_orders,
            "sales": total_sales,
            "avg_bounce_rate": avg_bounce,
            "gsc_clicks": total_gsc_clicks,
            "gsc_impressions": total_gsc_imps,
        },
        "pages": pages[:20],
        "sources": src_list[:10],
        "keywords": kw_list[:15],
    }
```

- [ ] **Step 4: テストが通ることを確認**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -m pytest tests/test_design_insight.py -v
```
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add projects/analytics/design_insight.py projects/analytics/tests/test_design_insight.py
git commit -m "feat(analytics): add data aggregation for design insight engine"
```

---

## Task 6: スプレッドシート読み込み機能

**Files:**
- Modify: `projects/analytics/design_insight.py`
- Modify: `projects/analytics/tests/test_design_insight.py`

- [ ] **Step 1: テスト追加（モックgspread）**

`tests/test_design_insight.py` の末尾に以下を追加:

```python
from unittest.mock import MagicMock


def test_collect_week_data_reads_all_sheets():
    from design_insight import collect_week_data

    mock_sheet_daily = MagicMock()
    mock_sheet_daily.get_all_records.return_value = [
        {"日付": "2026-04-08", "訪問回数（セッション）": 42},
        {"日付": "2026-04-15", "訪問回数（セッション）": 50},  # 範囲外
    ]
    mock_sheet_pv = MagicMock()
    mock_sheet_pv.get_all_records.return_value = [
        {"日付": "2026-04-08", "ページパス": "/"},
    ]
    mock_sheet_sources = MagicMock()
    mock_sheet_sources.get_all_records.return_value = []
    mock_sheet_keywords = MagicMock()
    mock_sheet_keywords.get_all_records.return_value = []

    mock_ss = MagicMock()
    def worksheet_side_effect(name):
        return {
            "デイリーログv2": mock_sheet_daily,
            "ページ別ビュー": mock_sheet_pv,
            "流入元別": mock_sheet_sources,
            "検索キーワード": mock_sheet_keywords,
        }[name]
    mock_ss.worksheet.side_effect = worksheet_side_effect

    config = {"spreadsheet": {"sheet_daily": "デイリーログv2"}}
    result = collect_week_data(mock_ss, config, date(2026, 4, 8), date(2026, 4, 14))

    assert len(result["daily"]) == 1
    assert result["daily"][0]["訪問回数（セッション）"] == 42
    assert len(result["page_views"]) == 1
```

- [ ] **Step 2: テストが失敗することを確認**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -m pytest tests/test_design_insight.py::test_collect_week_data_reads_all_sheets -v
```
Expected: FAIL (ImportError: collect_week_data)

- [ ] **Step 3: 実装追加**

`design_insight.py` の末尾（aggregate_contextの後）に以下を追加:

```python
def get_spreadsheet(config):
    import gspread
    from google.oauth2 import service_account

    sa_path = os.path.join(BASE_DIR, config["ga4"]["service_account_json"])
    credentials = service_account.Credentials.from_service_account_file(
        sa_path,
        scopes=[
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ],
    )
    gc = gspread.authorize(credentials)
    return gc.open_by_key(config["spreadsheet"]["id"])


def _filter_by_dates(rows, start: date, end: date):
    target = set()
    d = start
    while d <= end:
        target.add(d.strftime("%Y-%m-%d"))
        d += timedelta(days=1)
    return [r for r in rows if r.get("日付") in target]


def collect_week_data(spreadsheet, config, start: date, end: date):
    daily_sheet = spreadsheet.worksheet(config["spreadsheet"]["sheet_daily"])
    try:
        pv_sheet = spreadsheet.worksheet("ページ別ビュー")
        pv_rows = pv_sheet.get_all_records()
    except Exception:
        pv_rows = []
    try:
        src_sheet = spreadsheet.worksheet("流入元別")
        src_rows = src_sheet.get_all_records()
    except Exception:
        src_rows = []
    try:
        kw_sheet = spreadsheet.worksheet("検索キーワード")
        kw_rows = kw_sheet.get_all_records()
    except Exception:
        kw_rows = []

    return {
        "daily": _filter_by_dates(daily_sheet.get_all_records(), start, end),
        "page_views": _filter_by_dates(pv_rows, start, end),
        "sources": _filter_by_dates(src_rows, start, end),
        "keywords": _filter_by_dates(kw_rows, start, end),
    }
```

- [ ] **Step 4: テスト実行**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -m pytest tests/test_design_insight.py -v
```
Expected: 5 passed

- [ ] **Step 5: Commit**

```bash
git add projects/analytics/design_insight.py projects/analytics/tests/test_design_insight.py
git commit -m "feat(analytics): add spreadsheet data collection for week range"
```

---

## Task 7: Claude APIラッパー

**Files:**
- Modify: `projects/analytics/design_insight.py`
- Modify: `projects/analytics/tests/test_design_insight.py`

- [ ] **Step 1: テスト追加（モックanthropic）**

`tests/test_design_insight.py` の末尾に以下を追加:

```python
def test_generate_proposals_parses_json_response(monkeypatch):
    """Claude APIがJSON文字列を返す想定でパースできることを検証"""
    from design_insight import generate_proposals

    fake_response = MagicMock()
    fake_response.content = [MagicMock(type="text", text='{"summary":"改善点3件","proposals":[{"priority":"高","effort":"小","page_path":"/pages/company","page_label":"法人LP","section_file":"fam-corp-hero.liquid","metric":"直帰率","current_value":"78%","benchmark":"平均65%","problem_hypothesis":"CTA不在","proposal":"CTA追加","expected_impact":"直帰率-10%","kr_alignment":"KR-3"}]}')]

    fake_client = MagicMock()
    fake_client.messages.create.return_value = fake_response

    monkeypatch.setattr("design_insight._build_client", lambda cfg: fake_client)

    context = {"totals": {}, "pages": [], "sources": [], "keywords": []}
    mapping = {"routes": []}
    system_prompt = "test"
    config = {"claude": {"model": "claude-opus-4-6", "max_tokens": 1000}}

    result = generate_proposals(config, context, mapping, system_prompt)

    assert result["summary"] == "改善点3件"
    assert len(result["proposals"]) == 1
    assert result["proposals"][0]["section_file"] == "fam-corp-hero.liquid"


def test_generate_proposals_strips_markdown_fences(monkeypatch):
    """Claudeが ```json ... ``` で囲んで返した場合もパースできる"""
    from design_insight import generate_proposals

    fake_response = MagicMock()
    fake_response.content = [MagicMock(type="text", text='```json\n{"summary":"x","proposals":[]}\n```')]
    fake_client = MagicMock()
    fake_client.messages.create.return_value = fake_response
    monkeypatch.setattr("design_insight._build_client", lambda cfg: fake_client)

    result = generate_proposals(
        {"claude": {"model": "m", "max_tokens": 100}},
        {"totals": {}, "pages": [], "sources": [], "keywords": []},
        {"routes": []},
        "sys",
    )
    assert result["summary"] == "x"
```

- [ ] **Step 2: テストが失敗することを確認**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -m pytest tests/test_design_insight.py -k generate_proposals -v
```
Expected: FAIL (ImportError)

- [ ] **Step 3: 実装追加**

`design_insight.py` の末尾に以下を追加:

```python
def _build_client(config):
    import anthropic
    api_key = os.environ.get(config["claude"]["api_key_env"], "")
    if not api_key:
        raise RuntimeError(f"環境変数 {config['claude']['api_key_env']} が未設定です")
    return anthropic.Anthropic(api_key=api_key)


def _strip_code_fences(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        # 最初の行（```json）と最後の ``` を除去
        lines = t.splitlines()
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        t = "\n".join(lines)
    return t


def generate_proposals(config, context, mapping, system_prompt):
    """Claude APIを呼び出しデザイン改善提案JSONを得る"""
    client = _build_client(config)
    user_content = (
        "# 対象週データ\n\n"
        f"```json\n{json.dumps(context, ensure_ascii=False, indent=2)}\n```\n\n"
        "# セクションマッピング\n\n"
        f"```json\n{json.dumps(mapping, ensure_ascii=False, indent=2)}\n```\n\n"
        "上記データから、システムプロンプトのJSONスキーマに従って改善提案を生成してください。"
    )
    response = client.messages.create(
        model=config["claude"]["model"],
        max_tokens=config["claude"]["max_tokens"],
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )
    # content は TextBlock のリスト
    text = ""
    for block in response.content:
        if getattr(block, "type", None) == "text":
            text += block.text
    text = _strip_code_fences(text)
    return json.loads(text)
```

- [ ] **Step 4: テスト実行**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -m pytest tests/test_design_insight.py -v
```
Expected: 7 passed

- [ ] **Step 5: Commit**

```bash
git add projects/analytics/design_insight.py projects/analytics/tests/test_design_insight.py
git commit -m "feat(analytics): add Claude API wrapper for proposal generation"
```

---

## Task 8: シート書き込み機能

**Files:**
- Modify: `projects/analytics/design_insight.py`
- Modify: `projects/analytics/tests/test_design_insight.py`

- [ ] **Step 1: テスト追加**

`tests/test_design_insight.py` の末尾に以下を追加:

```python
def test_build_sheet_rows_includes_all_proposal_fields():
    from design_insight import build_sheet_rows

    proposals_data = {
        "summary": "今週は直帰率が高い傾向",
        "proposals": [
            {
                "priority": "高",
                "effort": "小",
                "page_path": "/pages/company",
                "page_label": "法人LP",
                "section_file": "fam-corp-hero.liquid",
                "metric": "直帰率",
                "current_value": "78%",
                "benchmark": "平均65%",
                "problem_hypothesis": "CTA不在",
                "proposal": "CTAボタンをFV上部に配置",
                "expected_impact": "直帰率-10%",
                "kr_alignment": "KR-3",
            }
        ],
    }

    rows = build_sheet_rows(proposals_data, week_label="W15")

    # ヘッダー + サマリー行 + 空行 + テーブルヘッダー + 1件
    assert len(rows) >= 5
    # ヘッダー行にW15を含む
    assert any("W15" in " ".join(str(c) for c in r) for r in rows)
    # 提案行に法人LPが含まれる
    assert any("fam-corp-hero.liquid" in " ".join(str(c) for c in r) for r in rows)


def test_make_sheet_name_uses_iso_week():
    from design_insight import make_sheet_name
    assert make_sheet_name(date(2026, 4, 15)) == "UI改善提案_W16"
    assert make_sheet_name(date(2026, 1, 5)) == "UI改善提案_W02"
```

- [ ] **Step 2: テスト失敗確認**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -m pytest tests/test_design_insight.py -k "build_sheet_rows or make_sheet_name" -v
```
Expected: FAIL

- [ ] **Step 3: 実装追加**

`design_insight.py` の末尾に以下を追加:

```python
SHEET_HEADERS = [
    "優先度", "工数", "ページ", "セクション", "指標",
    "今週実績", "ベンチマーク", "問題仮説", "改善案", "期待効果", "KR紐付け",
]


def make_sheet_name(ref_date: date) -> str:
    monday = ref_date - timedelta(days=ref_date.weekday())
    iso_week = monday.isocalendar()[1]
    return f"UI改善提案_W{iso_week:02d}"


def build_sheet_rows(proposals_data: dict, week_label: str) -> list:
    rows = []
    rows.append([f"FAMBOX UI改善提案 {week_label}"])
    rows.append([f"生成日時: {datetime.now().strftime('%Y-%m-%d %H:%M')}"])
    rows.append([f"サマリー: {proposals_data.get('summary', '')}"])
    rows.append([""])
    rows.append(SHEET_HEADERS)
    for p in proposals_data.get("proposals", []):
        rows.append([
            p.get("priority", ""),
            p.get("effort", ""),
            f"{p.get('page_label', '')}（{p.get('page_path', '')}）",
            p.get("section_file", ""),
            p.get("metric", ""),
            p.get("current_value", ""),
            p.get("benchmark", ""),
            p.get("problem_hypothesis", ""),
            p.get("proposal", ""),
            p.get("expected_impact", ""),
            p.get("kr_alignment", ""),
        ])
    return rows


def write_to_spreadsheet(spreadsheet, sheet_name: str, rows: list) -> str:
    """シートが存在すれば _v2, _v3 ...で重複回避"""
    final_name = sheet_name
    suffix = 2
    while True:
        try:
            spreadsheet.worksheet(final_name)
            final_name = f"{sheet_name}_v{suffix}"
            suffix += 1
        except Exception:
            break
    sheet = spreadsheet.add_worksheet(title=final_name, rows=max(50, len(rows) + 10), cols=len(SHEET_HEADERS))
    sheet.update(range_name="A1", values=rows)
    return final_name
```

- [ ] **Step 4: テスト実行**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -m pytest tests/test_design_insight.py -v
```
Expected: 9 passed

- [ ] **Step 5: Commit**

```bash
git add projects/analytics/design_insight.py projects/analytics/tests/test_design_insight.py
git commit -m "feat(analytics): add sheet row builder and writer for UI proposals"
```

---

## Task 9: メインエントリーポイント

**Files:**
- Modify: `projects/analytics/design_insight.py`

- [ ] **Step 1: mainとCLI追加**

`design_insight.py` の末尾に以下を追加:

```python
def load_system_prompt():
    path = os.path.join(BASE_DIR, "prompts", "design_insight_system.md")
    with open(path, encoding="utf-8") as f:
        return f.read()


def load_section_mapping():
    path = os.path.join(BASE_DIR, "section_mapping.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def run(ref_date: date, verbose: bool = True) -> dict:
    """メインフロー。Slack通知のため結果dictを返す"""
    config = load_config()
    monday, sunday = get_week_range(ref_date)
    sheet_name_base = make_sheet_name(ref_date)

    if verbose:
        print(f"[design_insight] 対象週: {monday} 〜 {sunday}")

    spreadsheet = get_spreadsheet(config)
    raw = collect_week_data(spreadsheet, config, monday, sunday)

    if not raw["daily"]:
        msg = f"対象週({monday}〜{sunday})のデイリーデータが見つかりません。先にdaily_collect.pyを実行してください。"
        print(msg, file=sys.stderr)
        return {"status": "no_data", "message": msg}

    context = aggregate_context(**raw)
    if verbose:
        print(f"[design_insight] セッション合計: {context['totals']['sessions']}")

    mapping = load_section_mapping()
    system_prompt = load_system_prompt()

    if verbose:
        print(f"[design_insight] Claude APIに提案生成を依頼中...")
    proposals = generate_proposals(config, context, mapping, system_prompt)

    proposal_count = len(proposals.get("proposals", []))
    if verbose:
        print(f"[design_insight] {proposal_count}件の提案を受信")

    rows = build_sheet_rows(proposals, week_label=sheet_name_base.split("_")[-1])
    final_sheet_name = write_to_spreadsheet(spreadsheet, sheet_name_base, rows)

    sheet_url = f"https://docs.google.com/spreadsheets/d/{config['spreadsheet']['id']}/edit#gid=0"

    result = {
        "status": "ok",
        "week_start": monday.isoformat(),
        "week_end": sunday.isoformat(),
        "sheet_name": final_sheet_name,
        "sheet_url": sheet_url,
        "proposal_count": proposal_count,
        "summary": proposals.get("summary", ""),
        "top_priority": [
            {
                "section": p.get("section_file"),
                "proposal": p.get("proposal"),
            }
            for p in proposals.get("proposals", [])
            if p.get("priority") == "高"
        ][:3],
    }

    if verbose:
        print(f"[design_insight] 完了: {final_sheet_name}")
        print(f"[design_insight] URL: {sheet_url}")
        print(json.dumps(result, ensure_ascii=False, indent=2))

    return result


def main():
    if len(sys.argv) > 1:
        ref = date.fromisoformat(sys.argv[1])
    else:
        # 直近完了週（先週）
        today = date.today()
        ref = today - timedelta(days=today.weekday() + 1)
    result = run(ref, verbose=True)
    # スクリプト末尾で結果をJSONとして標準出力
    print("---RESULT_JSON_BEGIN---")
    print(json.dumps(result, ensure_ascii=False))
    print("---RESULT_JSON_END---")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 構文チェック**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -c "import design_insight; print('OK')"
```
Expected: `OK`

- [ ] **Step 3: テスト再実行（既存テストに影響がないことを確認）**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python -m pytest tests/test_design_insight.py -v
```
Expected: 9 passed

- [ ] **Step 4: Commit**

```bash
git add projects/analytics/design_insight.py
git commit -m "feat(analytics): add main entry point and CLI for design insight"
```

---

## Task 10: 実環境スモークテスト（ドライラン）

**Files:** なし（実行のみ）

- [ ] **Step 1: APIキー設定確認**

ユーザーに確認:
```
環境変数 ANTHROPIC_API_KEY が設定されていますか？
未設定の場合、~/.zshrc に以下を追加してください:
  export ANTHROPIC_API_KEY="sk-ant-..."
```

Run:
```bash
echo "ANTHROPIC_API_KEY is set: $([ -n "$ANTHROPIC_API_KEY" ] && echo YES || echo NO)"
```
Expected: `YES`（NOなら後続ステップ不可、ユーザーに設定依頼）

- [ ] **Step 2: 先週分でドライラン実行**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python design_insight.py
```
Expected:
- `[design_insight] 対象週: YYYY-MM-DD 〜 YYYY-MM-DD`
- `[design_insight] セッション合計: NNN`
- `[design_insight] N件の提案を受信`
- `[design_insight] 完了: UI改善提案_WNN`
- 末尾に`---RESULT_JSON_BEGIN---`〜`---RESULT_JSON_END---`でJSON出力

- [ ] **Step 3: スプレッドシート確認**

ブラウザで以下を開き、`UI改善提案_W{NN}`シートが生成されていることを目視確認:
```
https://docs.google.com/spreadsheets/d/11tqgaX-6pRsnqSsQxln93nHlbXJwXJjudwnTbjzi-zA/edit
```

シート内容チェック:
- [ ] タイトル・サマリー・生成日時が表示されている
- [ ] テーブルヘッダー（優先度〜KR紐付け）が正しい
- [ ] 3件以上の提案行がある
- [ ] 各行に `section_file` （.liquidファイル名）が入っている

失敗時のデバッグ:
- Claude APIエラー → APIキー確認 / model名確認 / max_tokens増加
- JSONパースエラー → プロンプトのJSONスキーマ厳格化
- シート書き込みエラー → サービスアカウント権限確認

- [ ] **Step 4: ユーザーにサンプル結果共有・承認取得**

スプレッドシートURLと生成された提案内容をユーザーに見せ、以下を確認:
- 提案の質は使えるレベルか
- 改善提案の粒度は適切か
- セクションファイル名の特定精度は妥当か

承認後、次タスクへ進む。問題があればプロンプトまたはマッピングを調整して再実行。

- [ ] **Step 5: この時点ではコミット不要**

ドライラン結果は生成物のため、git管理外。

---

## Task 11: Slack User IDの実測

**Files:**
- Modify: `projects/analytics/config.json`

- [ ] **Step 1: 宮川さんのSlack User IDを取得**

実行環境にSlack MCPがあるため、Slack上で `@宮川真道` を対象にDM送信テストを行い、User IDを確認する。

ユーザーに聞く:
```
Slackで自分のプロフィールを開き、「…」メニューから「メンバーIDをコピー」でUser IDを取得してください。
形式: U01234ABCDE
```

- [ ] **Step 2: config.jsonに書き込み**

`config.json` の `slack.user_id_for_dm` を実際のIDに更新:

```json
"slack": {
  "webhook_url": "(既存)",
  "user_id_for_dm": "U_実際のID"
}
```

- [ ] **Step 3: Commit（注意: User IDは個人情報）**

```bash
git diff projects/analytics/config.json
git add projects/analytics/config.json
git commit -m "chore(analytics): set slack user id for design insight DM"
```

---

## Task 12: Claude scheduled task登録

**Files:** なし（scheduled-tasks MCPで登録）

- [ ] **Step 1: scheduled-tasks MCP で月曜08:00起動タスクを登録**

以下の内容で scheduled-tasks MCP の `create_scheduled_task` を呼ぶ:

- `taskId`: `fam-design-insight-weekly`
- `cronExpression`: `3 8 * * 1`（月曜08:03 - 0分回避）
- `description`: FAM Analytics: 週次UI改善提案の生成とSlack DM通知
- `prompt`:
```
あなたはFAMBOXのGA4データ分析エージェントです。以下を順に実行してください。

1. 以下のコマンドで design_insight.py を実行する:
   cd /Users/archecoinc./Desktop/Claude_1/projects/analytics && ./venv/bin/python design_insight.py

2. 標準出力の末尾にある `---RESULT_JSON_BEGIN---` と `---RESULT_JSON_END---` の間のJSONをパースする

3. JSONの `status` が "ok" の場合、以下の形式で宮川さん（Slack User ID: U_実際のID、config.jsonから取得）にDMを送信する（Slack MCP使用）:

---
📊 FAMBOX UI改善提案 {sheet_name} 生成完了

📅 対象期間: {week_start} 〜 {week_end}
💡 提案件数: {proposal_count}件
📝 サマリー: {summary}

🔥 優先度「高」の提案:
{top_priorityの各項目を「- {section}: {proposal}」の形式で列挙}

📋 詳細: {sheet_url}
---

4. status が "no_data" の場合、エラー内容を宮川さんにDMで通知する

5. Pythonが失敗した場合、エラーメッセージをDMで通知する
```

- [ ] **Step 2: 登録確認**

`mcp__scheduled-tasks__list_scheduled_tasks` を実行し、`fam-design-insight-weekly` が一覧に存在することを確認。

- [ ] **Step 3: 即時テスト実行**

`mcp__scheduled-tasks__update_scheduled_task` は即時実行機能が無いため、代わりに以下を実施:
- ターミナルで `./venv/bin/python design_insight.py` を手動実行
- 結果を見て宮川さんにSlack MCPで手動DM送信
- 届いたことを確認

- [ ] **Step 4: Commit（特に変更はないが進捗記録）**

変更ファイルなしのためコミットスキップ。メモリ更新のみ実施する:

```bash
# メモリ記録（次のタスクで実施）
```

---

## Task 13: メモリ更新

**Files:**
- Modify: `/Users/archecoinc./.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_analytics_reporter.md`
- Create: `/Users/archecoinc./.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/project_fam_lemon_env.md`
- Modify: `/Users/archecoinc./.claude/projects/-Users-archecoinc--Desktop-Claude-1/memory/MEMORY.md`

- [ ] **Step 1: 新規メモリ作成**

`~/.claude/projects/.../memory/project_fam_lemon_env.md`:

```markdown
---
name: FAMレモン君環境（エンバイロメントエンジニアリング）
description: GA4→改善提案→OKRレポートの一気通貫パイプライン。Phase 1 Design Insight Engineが稼働中。
type: project
updated: 2026-04-15
---

## 概要

南場会長の3段階モデル（プロンプト→コンテキスト→エンバイロメント）の第3段階を
FAMBOX OKR運用に適用した統合環境。

## コンポーネント

### Phase 1: GA4 Design Insight Engine ✅ 稼働中
- ファイル: `projects/analytics/design_insight.py`
- トリガー: 毎週月曜 08:03（scheduled-tasks: `fam-design-insight-weekly`）
- 出力: Googleスプレッドシート `UI改善提案_W{週番号}` シート
- 通知: Slack MCP経由で宮川さんにDM

### Phase 2: OKR Slack-Aware Reporter 🔲 未着手
- 既存の木曜17時タスク（`okr-weekly-report`）を拡張予定
- Slack #famコンテンツwg / #pmo / #事業開発 の直近7日発言を取得
- KR別に進捗・決定・ブロッカーを抽出

### Phase 3: Liquid Comparison Verifier 🔲 未着手
- CLIツール `projects/liquid_verifier/verify.py`
- Gemini APIで Figma vs コードプレビューの差分検出

## 関連ファイル
- 設計スペック: `docs/superpowers/specs/2026-04-15-fam-lemon-environment-design.md`
- 実装プラン: `docs/superpowers/plans/2026-04-15-design-insight-engine.md`
```

- [ ] **Step 2: 既存メモリを更新**

`project_analytics_reporter.md` の「次回タスク」末尾に追加:
```
7. **Design Insight Engine連携**: `design_insight.py`が週次で稼働中。UI改善提案_W{NN}シートを参照して改善実装する。詳細: `project_fam_lemon_env.md`
```

- [ ] **Step 3: MEMORY.md インデックス更新**

`MEMORY.md` の `## Active Development` 節に以下を追加:
```
- [project_fam_lemon_env.md](project_fam_lemon_env.md) — FAMレモン君環境。Phase 1 (Design Insight) 稼働中、Phase 2-3 未着手。
```

- [ ] **Step 4: メモリはgit管理外のため、コミットは不要**

メモリは `/Users/archecoinc./.claude/` 配下でgit管理外。ファイル保存のみで完了。

---

## Self-Review チェック結果

### Spec coverage
- ✅ Component 1 のすべての要素（データ集計・Claude API・シート書き込み・Slack DM）がTaskでカバー
- ✅ スケジュール実行（月曜08:00）もTask 12でカバー
- ✅ 連携先（okr_weekly_log.md への反映）は Phase 2 のスコープのため本プランでは対象外

### Placeholder scan
- ✅ TBD/TODO なし
- ✅ 各Taskに具体的なコード・コマンド・期待出力を記載
- ℹ️ Task 11の`U_実際のID`のみユーザー入力待ち（性質上避けられない）

### Type consistency
- ✅ `aggregate_context` → `generate_proposals` → `build_sheet_rows` → `write_to_spreadsheet` の関数名・引数名が一貫
- ✅ JSON スキーマ（proposals配列の各要素）が system prompt / test / build_sheet_rows で一致

### Scope
- ✅ Phase 1 のみにスコープ限定
- ✅ 10タスク程度に収まる粒度

---

## 実行順序

Task 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 (ユーザー承認) → 11 → 12 → 13

Task 10でユーザー承認を経てからTask 11以降へ進む。
