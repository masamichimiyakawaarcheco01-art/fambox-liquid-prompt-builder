# Design Wheel

> 非デザイナーが **70%以上の品質のデザイン成果物**を素早く作れるようにするための、
> デザインパターン在庫を体系化・蓄積する仕組み。FAMBOX Flywheel の Purpose（D-015）を
> 多パターン対応へ一般化したもの。FAM BOX とは独立。

## 目的

`幾何学 / コーポレート / グリッド / デジタル / スポーティ / Lab` 等のパターンを、
Pinterest収集 → Claude Design体系化 → Figma別UI生成 → レビュー学習 のループで
"在庫"として積み上げ、誰でもパターンを選べば7割の土台が出る状態を作る。

## アーキテクチャ（案A）

```
Pinterest画像 → Claude Design（抽出＋Web即プレビュー）→蒸留→ patterns/<p>/SYSTEM.md（真ソース）
                                                                  → figma-bridge → Figma 7割構築 → レビュー → SYSTEM.md改訂
```

- **真ソース** = `patterns/<p>/SYSTEM.md`（git版管理）。Claude Design は使い捨て抽出、Figma は出力。
- Claude Design の `Publish`（組織1公開制約）は在庫管理に使わない。

## パターン一覧

| パターン | ステータス | パック |
|---|---|---|
| corporate | ✅ 在庫入り（2026-06-10 昇格 / 11/12） | [patterns/corporate/](patterns/corporate/) |
| geometric | ⬜ 未着手 | — |
| grid | ⬜ 未着手 | — |
| digital | ⬜ 未着手 | — |
| sporty | 🟡 シード収集中（2026-06-10〜） | [patterns/sporty/](patterns/sporty/) |
| lab | ⬜ 未着手 | — |

## ファイル構成

- `LOOP.md` — 4フェーズ手順書
- `PATTERN-SCHEMA.md` — SYSTEM.md の型
- `CRITIQUE-RUBRIC.md` — レビュー・70%判定
- `LAYER-NAMING.md` — Figma レイヤー命名規則（チラシ制作と共通 / HTML クラス名と1対1対応）
- `patterns/<p>/` — 各パターンのパック（SYSTEM.md / refs.md / figma-recipe.md / critique-log.md）

## 運用ルール

1. 1パターンずつループを貫通させてから次へ（YAGNI）。
2. `SYSTEM.md` が唯一の真ソース。Claude Design 出力は必ず蒸留して取り込む。
3. 生成物は read-back 検証＋ルーブリック採点してから「完了」と報告する。
4. 既存 `brain/45_Design_Refs/` を壊さない（`wheel-pattern:` タグで共存）。

## 関連

- FAMBOX Flywheel: `docs/okr/fambox-flywheel/`
- Design Refs: `brain/45_Design_Refs/` ＋ `/design-ref` スキル
- 設計仕様: `docs/superpowers/specs/2026-06-09-design-wheel-design.md`
