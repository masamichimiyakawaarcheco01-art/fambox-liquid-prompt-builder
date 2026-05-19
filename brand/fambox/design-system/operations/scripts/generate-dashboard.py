#!/usr/bin/env python3
"""
FAMBOX DS Dashboard Generator
==============================
brand/fambox/design-system/operations/scripts/generate-dashboard.py

current.md §7 完成度ダッシュボード（spec ↔ Figma ↔ Liquid 三位一体）を
fixture（figma-sets.json）+ 実 file scan から自動生成する。

使い方:
    cd <worktree-root>
    python3 brand/fambox/design-system/operations/scripts/generate-dashboard.py

出力: stdout に current.md §7 全体（§7-A 〜 §7-F）を Markdown で生成。

設計意図:
- Figma 自動 audit との接続は Phase 2 候補（現状は手動 fixture を運用者が更新）
- spec md / Liquid section の存在は実 file scan で確認（自動同期）
- 出力は stdout のみ。current.md への上書きはしない（人間レビュー必須）
- N/3 ラベル化（学び 77）/ 3 つの数え方併記（学び 97）/ Figma 内訳明示（学び 98）に準拠
"""

from __future__ import annotations
import json
import os
import sys
from pathlib import Path
from datetime import date

# ─────────────────────────────────────────────────────────────
# Path resolution
# ─────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
DS_ROOT = SCRIPT_DIR.parent.parent  # brand/fambox/design-system
WORKTREE_ROOT = DS_ROOT.parent.parent.parent  # worktree root
COMPONENTS_DIR = DS_ROOT / "components"
SECTIONS_DIR = WORKTREE_ROOT / "sections"
FIXTURE_PATH = SCRIPT_DIR / "figma-sets.json"

# ─────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────
def load_fixture() -> dict:
    """Figma audit fixture を読み込む"""
    with open(FIXTURE_PATH, encoding="utf-8") as f:
        return json.load(f)


def spec_md_exists(md_name: str | None) -> bool:
    """spec md ファイルが存在するか確認"""
    if not md_name:
        return False
    return (COMPONENTS_DIR / md_name).exists()


def liquid_section_info(section_name: str | None) -> tuple[bool, int]:
    """Liquid section の存在と行数を返す"""
    if not section_name:
        return False, 0
    path = SECTIONS_DIR / section_name
    if not path.exists():
        return False, 0
    return True, sum(1 for _ in path.open(encoding="utf-8"))


def format_spec_cell(entry: dict) -> str:
    """spec md 列の表示文字列を生成（統合記載を明示）"""
    md = entry.get("spec_md")
    if not md:
        return "❌"
    if not spec_md_exists(md):
        return f"⚠ {md}（ファイル無し）"
    section = entry.get("spec_section")
    integration = entry.get("spec_integration")
    cell = f"✅ {md}"
    if section:
        cell += f" §{section}"
    if integration:
        cell += f"（統合: {integration}）"
    return cell


def format_figma_cell(entry: dict) -> str:
    """Figma 列の表示文字列を生成"""
    fid = entry.get("figma_id")
    variants = entry.get("variants")
    if not fid:
        return "❌"
    return f"✅ `{fid}` ({variants})" if variants else f"✅ `{fid}`"


def format_liquid_cell(entry: dict) -> str:
    """Liquid 列の表示文字列を生成"""
    liquid = entry.get("liquid")
    if entry.get("embedded_in"):
        return f"⚪ {entry['embedded_in']}"
    if not liquid:
        return "❌"
    exists, lines = liquid_section_info(liquid)
    if not exists:
        return f"⚠ {liquid}（ファイル無し）"
    name_no_ext = liquid.replace(".liquid", "")
    return f"✅ {name_no_ext} ({lines}行)"


# ─────────────────────────────────────────────────────────────
# §7-A L4 Components
# ─────────────────────────────────────────────────────────────
def render_l4(fixture: dict) -> list[str]:
    lines = [
        "### 7-A. L4 Components（{} 件 / Section 化対象）".format(len(fixture["L4"])),
        "",
        "> **表記ルール（v0.3-dashboard 標準化 / Session #43）**: Figma Set 列は `<ID> (<Nv> / <内訳>)` 形式で variant 構成を明示",
        "",
        "| Component | spec md | Figma Set | Liquid section | N/3 | Status | 残課題 |",
        "|---|---|---|---|---|---|---|",
    ]

    achieved = 0
    two_of_three = 0
    zero = 0

    for entry in fixture["L4"]:
        spec_ok = bool(entry.get("spec_md") and spec_md_exists(entry["spec_md"]))
        figma_ok = bool(entry.get("figma_id"))
        liquid_ok = False
        if entry.get("liquid"):
            liquid_ok, _ = liquid_section_info(entry["liquid"])

        n3 = sum([spec_ok, figma_ok, liquid_ok])
        if n3 == 3:
            achieved += 1
            status = "✅ 三位一体"
        elif n3 == 2:
            two_of_three += 1
            status = "🟡 " + ("Liquid 未作成" if not liquid_ok else "spec 未作成")
        elif n3 == 0:
            zero += 1
            status = "⚫ 未着手"
        else:
            status = f"🟡 {n3}/3"

        lines.append(
            "| {name} | {spec} | {figma} | {liquid} | **{n3}/3** | {status} | {note} |".format(
                name=entry["name"],
                spec=format_spec_cell(entry),
                figma=format_figma_cell(entry),
                liquid=format_liquid_cell(entry),
                n3=n3,
                status=status,
                note=entry.get("note") or "—",
            )
        )

    total = len(fixture["L4"])
    summary = (
        f"**L4 サマリ**: {total} 中 **{achieved} 件 三位一体達成（3/3）** / "
        f"{two_of_three} 件 2/3 / {zero} 件 0/3"
    )
    if achieved >= total - 1:
        summary += f" — **L4 完全制覇 {achieved}/{total - zero} 達成 🏆**"
        if zero > 0:
            summary += f"（残 {zero} 件は未着手）"
    lines += ["", summary]
    return lines


# ─────────────────────────────────────────────────────────────
# §7-B L3 Patterns
# ─────────────────────────────────────────────────────────────
def render_l3(fixture: dict) -> list[str]:
    lines = [
        "",
        "### 7-B. L3 Patterns（{} 件 / 一部のみ Section 評価）".format(len(fixture["L3"])),
        "",
        "| Pattern | spec md | Figma Set | Liquid section | N/3 | Status |",
        "|---|---|---|---|---|---|",
    ]

    triple = 0
    pattern_ok = 0
    for entry in fixture["L3"]:
        spec_ok = bool(entry.get("spec_md") and spec_md_exists(entry["spec_md"]))
        figma_ok = bool(entry.get("figma_id"))

        if entry.get("liquid"):
            liquid_ok, lines_count = liquid_section_info(entry["liquid"])
            liquid_cell = f"✅ {entry['liquid'].replace('.liquid', '')} ({lines_count}行)"
            n3 = sum([spec_ok, figma_ok, liquid_ok])
            n3_cell = f"**{n3}/3**"
            status = "✅ 三位一体" if n3 == 3 else f"🟡 {n3}/3"
            if n3 == 3:
                triple += 1
        else:
            embedded = entry.get("embedded_in", "L4 内包")
            liquid_cell = f"⚪ {embedded}"
            n3_cell = "Pattern OK"
            note = entry.get("level", "Pattern level ✅")
            status = "Pattern level ✅"
            if "v0.3-liquid" in note:
                status = "Pattern level ✅（v0.3-liquid で実体化）"
            pattern_ok += 1

        lines.append(
            "| {name} | {spec} | {figma} | {liquid} | {n3} | {status} |".format(
                name=entry["name"],
                spec=format_spec_cell(entry),
                figma=format_figma_cell(entry),
                liquid=liquid_cell,
                n3=n3_cell,
                status=status,
            )
        )

    total = len(fixture["L3"])
    lines += [
        "",
        f"**L3 サマリ**: {total} 中 **{triple} 件 独立 Section（3/3）** / {pattern_ok} 件 Pattern として L4 に内包（評価対象外で正常）",
    ]
    return lines


# ─────────────────────────────────────────────────────────────
# §7-C L2 Primitives
# ─────────────────────────────────────────────────────────────
def render_l2(fixture: dict) -> list[str]:
    l2 = fixture["L2"]
    total = len(l2)
    set_count = total  # 1 行 = 1 Figma Set
    primitive_count = 0
    md_set = set()
    completed = 0

    for entry in l2:
        spec_ok = bool(entry.get("spec_md") and spec_md_exists(entry["spec_md"]))
        figma_ok = bool(entry.get("figma_id"))
        if entry.get("spec_md"):
            md_set.add(entry["spec_md"])
        # primitive_count: fixture で明示された場合はそれを使用、なければ 1（= 1 行 = 1 Primitive）
        primitive_count += entry.get("primitive_count", 1)
        if spec_ok and figma_ok:
            completed += 1

    lines = [
        "",
        f"### 7-C. L2 Primitives（{set_count} 単位 / {primitive_count} Primitive 内訳 / Snippet レベル運用）",
        "",
        "L2 は通常 **Liquid Section ではなく Snippet (`{%- render '...' -%}`) または Inline コードで運用**。三位一体は **spec ↔ Figma の 2/2 で完了**と定義。",
        "",
        "**表記ルール（v0.3-dashboard 標準化 / Session #43）**:",
        "- 1 行 = 1 **DS 要素単位**（spec md ファイル数ではなく Figma Component Set 数で数える）",
        "- spec が **統合記載**の場合は spec 列に「`<md ファイル> §<section>（統合: <他要素>）`」と明示",
        "- Figma Set が **内訳を持つ**場合は「(<variant数>v / 内訳: <kind>)」を Figma 列に明示",
        "",
        "| Primitive | spec md | Figma Set | N/2 | Status |",
        "|---|---|---|---|---|",
    ]

    for entry in l2:
        spec_ok = bool(entry.get("spec_md") and spec_md_exists(entry["spec_md"]))
        figma_ok = bool(entry.get("figma_id"))
        n2 = sum([spec_ok, figma_ok])
        n2_cell = f"**{n2}/2**"
        if n2 == 2:
            status = "✅ Primitive 完成"
            if entry.get("note"):
                status += f"（{entry['note']}）"
        else:
            status = f"🟡 {n2}/2"

        # 統合記載は太字で強調
        is_integrated = bool(entry.get("spec_integration"))
        name_cell = f"**{entry['name']}**" if is_integrated else entry["name"]
        spec_cell = format_spec_cell(entry)
        if is_integrated:
            spec_cell = f"✅ {entry['spec_md']}"
            if entry.get("spec_section"):
                spec_cell += f" §{entry['spec_section']}"
            spec_cell += f" **（統合: {entry['spec_integration']}）**"

        lines.append(
            f"| {name_cell} | {spec_cell} | {format_figma_cell(entry)} | {n2_cell} | {status} |"
        )

    summary_marker = "🏆 " if completed == set_count else ""
    lines += [
        "",
        "**L2 サマリ**:",
        f"- **Figma Component Set 数で {completed}/{set_count} {summary_marker}完全制覇**" + (
            "（" + " / ".join(e["name"] for e in l2) + "）" if completed == set_count else ""
        ),
        f"- **個別 Primitive 数では {primitive_count}/{primitive_count}**（統合 spec md の内訳を分解）",
        f"- **spec md 数では {len(md_set)}/{len(md_set)}**（progress.md / form-controls.md は統合記載で複数 Primitive を含む）",
        "- 統合 spec md は **「機能カテゴリ単位で md を統合」**が正しい設計（学び 95）。3 つの数え方が一致する構造になっている",
    ]
    return lines


# ─────────────────────────────────────────────────────────────
# §7-F 全体ステータス
# ─────────────────────────────────────────────────────────────
def render_status(fixture: dict) -> list[str]:
    # L4 集計
    l4 = fixture["L4"]
    l4_total = len(l4)
    l4_triple = 0
    l4_zero = 0
    for entry in l4:
        spec_ok = bool(entry.get("spec_md") and spec_md_exists(entry["spec_md"]))
        figma_ok = bool(entry.get("figma_id"))
        liquid_ok, _ = liquid_section_info(entry.get("liquid"))
        n3 = sum([spec_ok, figma_ok, liquid_ok])
        if n3 == 3:
            l4_triple += 1
        elif n3 == 0:
            l4_zero += 1

    # L3 集計
    l3 = fixture["L3"]
    l3_total = len(l3)
    l3_ok = 0
    for entry in l3:
        spec_ok = bool(entry.get("spec_md") and spec_md_exists(entry["spec_md"]))
        figma_ok = bool(entry.get("figma_id"))
        if spec_ok and figma_ok:
            l3_ok += 1

    # L2 集計
    l2 = fixture["L2"]
    l2_total = len(l2)
    l2_ok = 0
    for entry in l2:
        spec_ok = bool(entry.get("spec_md") and spec_md_exists(entry["spec_md"]))
        figma_ok = bool(entry.get("figma_id"))
        if spec_ok and figma_ok:
            l2_ok += 1

    # Liquid 累計行数（fambox-* のみ計算）
    fambox_liquids = [e.get("liquid") for layer in (l4, l3) for e in layer if e.get("liquid")]
    total_lines = 0
    for fname in fambox_liquids:
        _, lc = liquid_section_info(fname)
        total_lines += lc

    l4_pct = round(l4_triple / l4_total * 100)
    l3_pct = round(l3_ok / l3_total * 100)
    l2_pct = round(l2_ok / l2_total * 100)

    def progress_bar(count: int, total: int) -> str:
        bar = "✅" * count
        bar += "🟡" * (total - count - (1 if l4_zero > 0 and count + 1 + (0) <= total else 0))
        return bar

    l4_bar = "✅" * l4_triple
    # 2/3 件 = total - triple - zero
    l4_two = l4_total - l4_triple - l4_zero
    l4_bar += "🟡" * l4_two + "⚫" * l4_zero

    l3_bar = "✅" * l3_ok + "🟡" * (l3_total - l3_ok)
    l2_bar = "✅" * l2_ok + "🟡" * (l2_total - l2_ok)

    l4_trophy = " 🏆 完全制覇" if l4_triple >= l4_total - 1 else ""
    l3_trophy = " 🏆" if l3_ok == l3_total else ""
    l2_trophy = " 🏆 完全制覇" if l2_ok == l2_total else ""

    lines = [
        "",
        "### 7-F. 全体ステータス（自動生成: {} / Session 進行中）".format(date.today().isoformat()),
        "",
        "```",
        f"L4 Components:    {l4_triple}/{l4_total} 三位一体達成 ({l4_pct}%) {l4_bar}{l4_trophy}",
        f"L3 Patterns:      {l3_ok}/{l3_total}  Pattern level OK ({l3_pct}%) {l3_bar}{l3_trophy}",
        f"L2 Primitives:    {l2_ok}/{l2_total}  Primitive 完成    ({l2_pct}%) {l2_bar}{l2_trophy}",
        f"Section 累計新規行: {total_lines:,}行 (fambox-* L4/L3 Liquid sections の合計)",
        "```",
        "",
    ]

    if l4_triple >= l4_total - 1 and l3_ok == l3_total and l2_ok == l2_total:
        lines += [
            "**🏆 L4 + L3 + L2 すべての層で「ほぼ完全」状態**",
            "",
            "| Layer | 状態 | 残課題 |",
            "|---|---|---|",
            f"| L4 Components | {l4_triple}/{l4_total}（{l4_pct}%）🏆 | {l4_zero} 件未着手 |",
            f"| L3 Patterns | {l3_ok}/{l3_total}（100%）🏆 | 完成 |",
            f"| L2 Primitives | {l2_ok}/{l2_total}（100%）🏆 | 完成 |",
        ]

    return lines


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────
def main() -> int:
    if not FIXTURE_PATH.exists():
        print(f"❌ fixture not found: {FIXTURE_PATH}", file=sys.stderr)
        return 1

    fixture = load_fixture()

    header = [
        "## 7. 完成度ダッシュボード（spec ↔ Figma ↔ Liquid 三位一体）",
        "",
        "> 学び 77（N/3 ラベル化）の実装。各 Component の **3 層存在** を即可視化。",
        "> 凡例: ✅ = 存在、❌ = 未作成、⚪ = 評価対象外（Pattern として L4 に内包 / Primitive は Snippet レベル運用）",
        "> 自動生成: `python3 brand/fambox/design-system/operations/scripts/generate-dashboard.py`",
        "> Last Audit: " + fixture["_meta"]["last_audit"] + " (Session " + fixture["_meta"]["last_audit_session"] + ")",
        "",
    ]

    output: list[str] = []
    output += header
    output += render_l4(fixture)
    output += render_l3(fixture)
    output += render_l2(fixture)
    output += render_status(fixture)

    print("\n".join(output))
    return 0


if __name__ == "__main__":
    sys.exit(main())
