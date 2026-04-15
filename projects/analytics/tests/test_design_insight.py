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
