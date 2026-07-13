# Design Wheel — 設計仕様（spec）

- **作成日**: 2026-06-09
- **作成者**: 宮川真道（ARCHECO）
- **ステータス**: 設計承認済み（ユーザー承認 2026-06-09）→ 実装計画へ
- **関連**: `fambox-flywheel`（Purpose D-015 を一般化）/ `brain/45_Design_Refs/` / `/design-ref` スキル / figma-bridge / Claude Design

---

## 1. 目的（Purpose）

非デザイナーが **70%以上の品質のデザイン成果物**を素早く作れるようにする。
そのために、`幾何学 / コーポレート / グリッド / デジタル / スポーティ / Lab` 等の **デザインパターンを"在庫"として体系化・蓄積する仕組み（ホイール）**を作る。

これは FAMBOX Flywheel の Purpose（D-015「誰でも7割を早く出せる AI×Design インフラ」）を、**FAMBOX1ブランドから多パターン対応へ一般化**したもの。FAM BOX とは独立した取り組みである（チラシ制作の作業とは重なるが別物）。

### スコープ境界
- **本spec対象**: ホイールの仕組み（ディレクトリ構造・ループ手順・スキーマ・レビュー基準）＋**パイロット1パターン（corporate）を端から端まで貫通**。
- **本spec対象外（次フェーズ）**: 残り5パターンの構築、非デザイナーがSlackでパターンをリクエストするStep2/3運用、Sense/Learnの完全自動化。

---

## 2. アーキテクチャ（承認: 案A）

リポジトリの「パターンパック」を**唯一の真ソース**とし、Claude Design は抽出ワークベンチ、Figma は出力ターゲットとする。

```
Pinterest画像 ──→ Claude Design（抽出＋Web即プレビュー）──蒸留──→ patterns/<p>/SYSTEM.md（真ソース・git版管理）
                                                                      │
                                                          figma-bridge が読む
                                                                      ↓
                                                        Figma で別UIを7割構築 → レビュー → critique-log → SYSTEM.md改訂
```

### 役割分担
- **Claude Design**: 大量画像からの色/タイポ/コンポーネント/レイアウト自動抽出＋Web即プレビュー（使い捨て）。**組織1公開制約に依存しない**（`Publish` を在庫管理には使わない）。
- **SYSTEM.md（リポジトリ）**: 抽出結果を蒸留した恒久・版管理の真ソース。
- **figma-bridge**: SYSTEM.md を読んで Figma に構造7割を構築。
- **critique-log**: 生成→レビューの学習を蓄積し SYSTEM.md を改訂。

### 既存資産との接続（流用・破壊しない）
| 既存資産 | 本ホイールでの役割 |
|---|---|
| `brain/45_Design_Refs/` | Sense層の保管庫。新タグ軸 `wheel-pattern:` を追加して共存。 |
| `/design-ref` スキル | Pinterest/URL を refs として保存する入口（流用）。 |
| `fambox-flywheel` | 構造の親（Sense→Generate→Reach→Learn）。本ホイールはその一般化版で別ハブ。 |
| figma-bridge | Generate層の構築エンジン（既知制約 = フォント全て Inter → 人間3割仕上げ）。 |

---

## 3. ディレクトリ構造

FAMBOX flywheel とは別ハブ `docs/design-wheel/` を新設。

```
docs/design-wheel/
├── README.md                  # 目的・運用ルール・パターン一覧（インデックス）
├── LOOP.md                    # 4フェーズ手順書（Sense→Systematize→Generate→Learn）
├── PATTERN-SCHEMA.md          # SYSTEM.md の標準スキーマ（全パック共通の型）
├── CRITIQUE-RUBRIC.md         # レビュー観点と「70%到達」判定基準
└── patterns/
    └── corporate/             # パイロット
        ├── SYSTEM.md          # ★真ソース: トークン/タイポ/グリッド/コンポーネント規則
        ├── refs.md            # 45_Design_Refs への参照索引（根拠画像）
        ├── figma-recipe.md    # figma-bridge ビルド手順（このパターンの組み方）
        └── critique-log.md    # 生成→レビューの履歴と学び（版ごと）
```

`SYSTEM.md` が唯一の真ソース。Claude Design は抽出補助、Figma は出力、critique-log は学習蓄積。

---

## 4. ループ（4フェーズ・AI7割/人間3割）

| フェーズ | 中身 | AI(7割) | 人間(3割) |
|---|---|---|---|
| **Sense** | Pinterest等で対象パターンのUI画像を10〜20枚収集 → `/design-ref` で `45_Design_Refs` に保存（`wheel-pattern:` タグ付与） | 収集補助・タグ付け・索引化 | 画像の選定・採否 |
| **Systematize** | Claude Design に画像投入 → 色/タイポ/コンポーネント/レイアウト自動抽出＋Web即プレビュー → `SYSTEM.md` に蒸留 | 抽出・蒸留・スキーマ整形 | 抽出結果の妥当性判断 |
| **Generate** | `SYSTEM.md` を読み figma-bridge で**参照とは別物のUI**を構造7割構築 | レイアウト/余白/色/階層/グレーボックス | フォント・写真差込（3割仕上げ） |
| **Learn** | 生成Figma vs 参照を `CRITIQUE-RUBRIC` で採点 → ズレを `critique-log` に記録 → `SYSTEM.md` 改訂 | 採点・差分抽出・改訂提案 | 最終判断・パターン昇格可否 |

詳細手順は `LOOP.md` に記載（各フェーズの具体コマンド・MCP呼び出し・チェックリスト）。

---

## 5. タグ軸の拡張（45_Design_Refs）

- 既存の **FAMBOX軸**（軸1 静の信頼 … 軸4 蓄積する負荷）＝**意味/隠喩**の軸。維持。
- 新規 **`wheel-pattern:`** タグ＝**表層スタイル**の軸（直交）。値: `geometric / corporate / grid / digital / sporty / lab`。
- 既存 `_by-style/` 仕組みと共存。2軸（意味×スタイル）で参照を引けるようにする。
- `_index.md` の表に `wheel-pattern` 列を追加。

---

## 6. SYSTEM.md スキーマ（PATTERN-SCHEMA.md で定義）

全パックが同じ型に従う＝figma-bridge が機械的に読め、パターン間比較も可能。

| セクション | 内容 |
|---|---|
| **Identity** | パターン名 / 一言定義 / 代表ref 3枚（45_Design_Refsリンク） |
| **Color** | 役割別トークン（bg / surface / ink / accent / muted …）＋ ゾーニング規則 |
| **Type** | 書体方針 / 6段スケール（飾り〜Small）/ ジャンプ率 / 行間 |
| **Layout** | グリッド（列数/ガター）/ 整数比 / 余白 S/M/L（等比） |
| **Components** | ボタン / カード / ヘッダ 等の角丸・影・状態（hover/disabled等） |
| **Motion**（任意） | 速度 / イージング |
| **DO / DON'T** | そのパターンらしさを壊す禁止事項 |

---

## 7. レビュー基準（CRITIQUE-RUBRIC.md / 「70%到達」定義）

6観点 × 各0〜2点（満点12）:

1. 色ゾーニング
2. タイポ階層・ジャンプ率
3. グリッド整列
4. コンポーネント一貫性
5. 余白リズム
6. パターンらしさ

**昇格条件（= 非デザイナーが7割出せる土台が完成）**:
- 合計 ≥ 8.5/12（≒70%）**かつ**
- 構造系観点（1色ゾーニング / 2タイポ階層 / 3グリッド / 5余白）に **0点が無い**。

フォント・写真差込は人間の3割仕上げ領域のため、本ルーブリックの採点対象外（別枠メモとして critique-log に記録）。

---

## 8. パイロット: corporate

- **理由**: (1) B2B提案資料・法人LPで実需、(2) FAMBOXのLab/スポーティ系と別物でホイールの多パターン化を最初から実証、(3) 構造明快でレビュー基準を固めやすい。
- **完走の定義（Definition of Done）**:
  1. `docs/design-wheel/` 基盤4ファイル（README/LOOP/PATTERN-SCHEMA/CRITIQUE-RUBRIC）作成。
  2. `45_Design_Refs` に corporate の refs を 10〜20枚収集＋ `wheel-pattern:corporate` タグ付与。
  3. `patterns/corporate/SYSTEM.md` をスキーマ準拠で作成（Claude Design 抽出を蒸留）。
  4. figma-bridge で corporate の**別UIを1画面**構造7割構築。
  5. CRITIQUE-RUBRIC で採点し、昇格条件を満たすまで最低1周の改訂を回す。
  6. `critique-log.md` に1周分の学びを記録。
- **計測**: 純構築時間（figma-bridge着手→7割完成）を記録し、横展開時の基準値とする。

---

## 9. 未決事項（実装計画で詰める）

- Claude Design の抽出結果を SYSTEM.md に落とす**蒸留の具体手順**（手動コピペ vs 半自動）。
- figma-bridge の corporate ビルドで使う**ダミーUIの題材**（例: B2Bサービス紹介LPのHeroセクション等）。
- `wheel-pattern:` タグの `_index.md` への反映方法（列追加 or 別索引）。
