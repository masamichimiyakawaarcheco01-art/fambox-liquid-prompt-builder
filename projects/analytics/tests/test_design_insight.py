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


# ===========================
# スプレッドシート読み込み
# ===========================

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
