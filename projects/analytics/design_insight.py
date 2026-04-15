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


# ===========================
# Claude APIラッパー
# ===========================

def _build_client(config):
    import anthropic
    api_key = os.environ.get(config["claude"]["api_key_env"], "")
    if not api_key:
        raise RuntimeError(f"環境変数 {config['claude']['api_key_env']} が未設定です")
    return anthropic.Anthropic(api_key=api_key)


def _strip_code_fences(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        # 最初の行（```json など）と最後の ``` を除去
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


# ===========================
# シート書き込み
# ===========================

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


# ===========================
# メインフロー
# ===========================

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

    sheet_url = f"https://docs.google.com/spreadsheets/d/{config['spreadsheet']['id']}/edit"

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

    return result


def main():
    if len(sys.argv) > 1:
        ref = date.fromisoformat(sys.argv[1])
    else:
        # 直近完了週（先週の日曜を含む週）
        today = date.today()
        ref = today - timedelta(days=today.weekday() + 1)
    result = run(ref, verbose=True)
    # スクリプト末尾で結果をJSONとして標準出力
    print("---RESULT_JSON_BEGIN---")
    print(json.dumps(result, ensure_ascii=False))
    print("---RESULT_JSON_END---")


if __name__ == "__main__":
    main()
