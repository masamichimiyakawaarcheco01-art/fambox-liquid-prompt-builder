---
title: FAMBOX Icon Inventory
type: design-system-reference
layer: L1-Tokens-Icon
status: in_progress
last_updated: 2026-04-20
owner: 宮川
purpose: FAMBOX で使うアイコンを洗い出し、Claude/デザイナーが迷わず引けるようにする
---

# FAMBOX — Icon Inventory（必要アイコン洗い出し）

**Worksheet §5 の「必要なアイコンを洗い出したい」への対応**。
この表を埋めれば、最終的な Icon Set の選定判断（Lucide / Phosphor / Heroicons / 自作）を精度高く行える。

---

## 1. Icon のカテゴリ別必要リスト

### A. Navigation / Structure（ナビゲーション）

| ID | 用途 | 必要度 | 既存使用箇所 | Notes |
|---|---|---|---|---|
| nav-menu | ハンバーガー（代替：横スクロール採用中） | ★☆ | — | v0.5で不採用だが B2B 資料等で使用候補 |
| nav-close | 閉じる（Drawer / Modal） | ★★★ | Shopify drawer | 必須 |
| nav-search | 検索 | ★★ | Header検索欄 | 必須 |
| nav-cart | カート | ★★★ | Header | 既存 |
| nav-user | アカウント | ★★ | Header | 既存 |
| nav-back | 戻る（矢印左） | ★★ | Blog記事等 | 既存 |
| nav-forward | 進む（矢印右） | ★★ | Pagination | 必須 |
| nav-external | 外部リンク矢印 | ★★ | 資料DLリンク等 | 必須 |

### B. Action（操作）

| ID | 用途 | 必要度 | Notes |
|---|---|---|---|
| action-plus | 追加 | ★★ | Form系 |
| action-minus | 削除 | ★★ | Form系 |
| action-edit | 編集 | ★★ | 管理系 |
| action-trash | 削除・破棄 | ★★ | 管理系 |
| action-download | ダウンロード | ★★★ | **資料DL CTA 必須** |
| action-upload | アップロード | ★ | Form系 |
| action-share | 共有・SNSシェア | ★★ | Blog 記事 |
| action-copy | コピー | ★ | 共有URL等 |
| action-filter | フィルタ | ★★ | 商品一覧・Blog |
| action-sort | 並び替え | ★★ | 商品一覧 |

### C. Content / Media（コンテンツ）

| ID | 用途 | 必要度 | Notes |
|---|---|---|---|
| content-play | 動画再生 | ★★★ | YouTube動画埋め込み・Hero動画 |
| content-pause | 一時停止 | ★★ | 動画 |
| content-mute | ミュート | ★★ | Hero動画 |
| content-volume | 音量 | ★ | — |
| content-image | 画像 | ★ | プレースホルダ |
| content-document | 資料・PDF | ★★★ | **資料DL CTA 必須** |
| content-video | 動画アイコン | ★★ | YouTubeリンク |

### D. Status / Feedback（状態通知）

| ID | 用途 | 必要度 | Notes |
|---|---|---|---|
| status-check | 成功・完了 | ★★★ | Form送信成功・チェックボックス |
| status-alert-warning | 警告（！） | ★★ | Alert |
| status-alert-error | エラー（×） | ★★★ | Form バリデーション |
| status-info | 情報（i） | ★★ | Tooltip・ヒント |
| status-question | 疑問（？） | ★★ | FAQ / Help |
| status-loading | ローディング（円形スピナー） | ★★★ | Form送信中 |
| status-new | 新規バッジ（●） | ★ | 新商品バッジ |

### E. Communication / Contact（連絡）

| ID | 用途 | 必要度 | Notes |
|---|---|---|---|
| comm-mail | メール | ★★★ | Footer・問合せ |
| comm-phone | 電話 | ★★ | Footer |
| comm-chat | チャット | ★★ | 問合せCTA |
| comm-calendar | 日程調整 | ★★ | 商談予約 |
| comm-location | 所在地・地図 | ★ | Footer |
| comm-send | 送信（紙飛行機） | ★★ | Form送信ボタン |

### F. Social（SNS）

| ID | 用途 | 必要度 | Notes |
|---|---|---|---|
| social-instagram | Instagram | ★★★ | Footer |
| social-twitter-x | X (旧Twitter) | ★★ | Footer |
| social-youtube | YouTube | ★★★ | Footer |
| social-note | note | ★★ | Footer |
| social-facebook | Facebook | ★ | Footer |
| social-line | LINE（B2B連絡候補） | ★★ | 要検討 |

### G. Sports / Nutrition（ドメイン特化）★ FAMBOXの独自性

| ID | 用途 | 必要度 | Notes |
|---|---|---|---|
| domain-athlete | アスリート・走る人 | ★★★ | **FAMBOX固有・Hero** |
| domain-team | チーム・人複数 | ★★★ | **B2B訴求** |
| domain-coach | 監督・コーチ | ★★★ | ターゲット |
| domain-nutritionist | 栄養士 | ★★ | ターゲット |
| domain-meal | 食事・お皿 | ★★★ | プラン訴求 |
| domain-nutrient | 栄養素（円形） | ★★ | データ可視化 |
| domain-protein | タンパク質 | ★★ | 成分訴求 |
| domain-calorie | カロリー | ★★ | 成分訴求 |
| domain-water | 水分補給 | ★★ | 栄養戦略 |
| domain-supplement | サプリメント | ★★ | 栄養戦略 |
| domain-timing | タイミング（時計） | ★★ | 摂取タイミング |
| domain-schedule | 定期・スケジュール | ★★ | 定期便 |
| domain-target | ターゲット・目標 | ★★★ | "勝ち筋" 訴求 |
| domain-trophy | 達成・勝利 | ★★★ | 実績・Case Study |
| domain-science | 研究・サイエンス（ビーカー） | ★★ | Scientific軸 |
| domain-data | データ・グラフ | ★★ | エビデンス訴求 |

### H. Commerce（EC操作）

| ID | 用途 | 必要度 | Notes |
|---|---|---|---|
| commerce-cart-add | カート追加 | ★★★ | Shopify必須 |
| commerce-price | 価格・金額 | ★ | — |
| commerce-gift | ギフト | ★ | 法人ギフト候補 |
| commerce-truck | 配送 | ★★★ | 配送情報訴求 |
| commerce-package | パッケージ・箱 | ★★★ | "FAMBOX"の象徴 |
| commerce-credit-card | クレジット決済 | ★★ | 決済ページ |
| commerce-receipt | 領収書 | ★★ | 法人請求 |

### I. Misc

| ID | 用途 | 必要度 | Notes |
|---|---|---|---|
| misc-star | 評価・お気に入り | ★★ | レビュー |
| misc-heart | いいね | ★ | Blog |
| misc-bookmark | ブックマーク | ★ | Blog |
| misc-bell | 通知 | ★ | 管理系 |
| misc-settings | 設定（歯車） | ★★ | 管理系 |
| misc-lock | セキュリティ | ★★ | プライバシー訴求 |
| misc-shield | 安心・保証 | ★★ | HACCP訴求 |

---

## 2. 必要度合計と推奨セット判定

| 必要度 | 件数 |
|---|---|
| ★★★（必須） | 約20個 |
| ★★（強く推奨） | 約30個 |
| ★（あれば） | 約15個 |
| **合計候補** | **約65個** |

## 3. Icon Set 候補との適合度

### Lucide Icons（推奨候補）
- A-F カテゴリ: **100% カバー可能**（標準的な UI セット）
- G ドメイン特化: **約40%カバー**（athlete/team/coach/trophy/data等あり。meal/nutrient等は代替表現必要）
- H Commerce: **80%カバー**
- **判定**: ★★★ — Lucide 基本＋Gカテゴリの一部を **FAMBOX 独自 SVG** で補完するハイブリッドが現実解

### Phosphor Icons
- G カテゴリのカバー率が Lucide より高い（6ウェイトで表現幅も広い）
- **判定**: ★★★ — weight の使い分けで Scientific 感を出せる

### Heroicons
- A-F は十分カバー
- G ドメイン特化は弱い
- **判定**: ★★ — B2B SaaS 寄りで FAMBOX の現場感に合わない恐れ

### 自作
- G ドメイン特化は独自で作れる（★4つ）
- A-F は既存で代替可能（時間の無駄）
- **判定**: ★ — 全自作はROIが悪い。**Gドメイン特化 15-20個のみ自作**が最適

---

## 4. 推奨採用案（3択）

### Case 1: Lucide + FAMBOX Domain SVG（推奨）
- 基本セット: Lucide（A-F + H-I 全て）= 約45個
- カスタム: Gドメイン 10-15個を SVG で自作（meal / nutrient / protein 等）
- **メリット**: 軽量・オープンソース・独自性も確保
- **デメリット**: 自作の制作コスト 1-2日

### Case 2: Phosphor Regular（全依存）
- 全て Phosphor の Regular weight
- **メリット**: 選定迷いなし・weight でバリエーション
- **デメリット**: G ドメインで一部妥協（meal→fork-knife 等）

### Case 3: ハイブリッド自作
- Button内 / SNS / Navigation は Lucide
- ドメイン特化は全自作（15個）＋ データ可視化 F章の8コアと整合

---

## 5. 次のステップ

1. **宮川さん**: この表の ★必要度 を見直す（過不足）
2. **宮川さん**: 推奨採用案 Case 1 / 2 / 3 から選ぶ
3. **Claude**: 選定後、各アイコン ID → Lucide/Phosphor のマッピング表を作成
4. **Claude**: 自作が必要な Gドメインアイコンの SVG spec（形状ガイド）を出力

---

## チェックリスト（宮川さんの判断）

- [ ] A-I カテゴリの必要度を確認・調整
- [ ] 推奨採用案 Case 1 / 2 / 3 のいずれかを選択: [ 回答: ]
- [ ] 追加が必要なアイコンがあれば記入: [ 回答: ]
- [ ] 削除してよいアイコンがあれば記入: [ 回答: ]
