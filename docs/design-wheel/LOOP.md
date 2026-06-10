# LOOP — Design Wheel 4フェーズ手順書

1パターンを端から端まで貫通させる手順。AI7割 / 人間3割（D-021）。

---

## Phase 1: Sense（参照収集）🧑＋AI
1. 対象パターンの UI 画像を Pinterest 等で 10〜20枚集める（人間が選定）。
2. 各画像を `/design-ref` スキルで `brain/45_Design_Refs/` に保存。
3. 保存時に `wheel-pattern:<pattern>` タグを付与（既存 FAMBOX軸タグと併記）。
4. `patterns/<pattern>/refs.md` に索引（リンク＋一言メモ）を作る。
- **完了条件**: refs 10枚以上＋`wheel-pattern` タグ付与済。

## Phase 2: Systematize（体系化）🧑＋AI
1. 集めた画像を Claude Design に投入し、色/タイポ/コンポーネント/レイアウトを自動抽出。
2. Web 即プレビューで抽出システムの妥当性を目視確認（人間）。
3. 抽出結果を `PATTERN-SCHEMA.md` の型に**蒸留**して `patterns/<pattern>/SYSTEM.md` を作成。
4. 仮置きの値は実画像と照合して確定する（憶測値を残さない）。
- **完了条件**: SYSTEM.md が7セクション全て埋まり、空欄/TBD なし。

## Phase 3: Generate（Figma構築）AI
1. `SYSTEM.md` と **`LAYER-NAMING.md`（命名規則）** を読み込む。
2. **参照とは別物の題材**で1画面を設計（例: corporate なら B2Bサービス紹介LP Hero）。
3. チャネルを選択: Figma（後編集性重視）or HTML（表現再現度・写真/動勢依存パターン向き）。
4. figma-bridge で構造7割を構築（レイアウト/余白/色/階層/グレーボックス）。
   - フォントは Inter 固定で割り切る（人間が後で差替）。
   - **全ノードを LAYER-NAMING 準拠の `name` 付きで作成**（bridge に rename 無し＝作成時が唯一のチャンス）。
   - 前後深度が要る場合は z-order=作成順で設計（学び4）。
5. 手順を `patterns/<pattern>/figma-recipe.md` に記録。
- **完了条件**: Figma に1画面の構造が組み上がり、export 画像を取得。**命名検収**（デフォルト名 0件）と孤児フレーム検査（ID 欠番確認）を通過。

## Phase 4: Learn（採点・改訂）AI＋🧑
1. 生成 Figma を export → 参照と並べて `CRITIQUE-RUBRIC.md` で採点。
2. 結果を `patterns/<pattern>/critique-log.md` に記録。
3. 構造系の減点があれば SYSTEM.md を改訂し Phase 3 を再実行。
4. 昇格条件（≥8.5/12 かつ構造系0点なし）を満たしたら README のステータスを ✅ に。
- **完了条件**: 昇格条件達成、または少なくとも1周の改訂を記録。

---

## 横展開（パイロット完走後）
次のパターンは本 LOOP をコピーして実行。SYSTEM.md は同一スキーマなので比較・流用可能。
