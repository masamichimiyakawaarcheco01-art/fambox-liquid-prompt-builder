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


# ===========================
# スプレッドシート読み込み
# ===========================

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
