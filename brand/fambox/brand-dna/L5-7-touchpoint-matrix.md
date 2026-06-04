---
title: L5-7 接点 4 象限マトリクス（KEEP / REFINE / CREATE / IGNORE）
type: brand-dna
brand: fambox
version: 1.0
status: confirmed
last_updated: 2026-05-27
owner: 宮川
adr: ADR-034
related:
  - current.md#l5-7
  - current.md#l5-2
  - decisions/decisions-log.md#adr-034
  - ../../MATERIALS_TIER1/M4-competitors/OVERVIEW.md
---

# L5-7. 接点 4 象限マトリクス

DNA v1.0 公式昇格（ADR-031）に伴う既存接点棚卸し。L5-2 接点リスト + M4 競合分析（OVERVIEW.md / nosh office LP / GREEN SPOON 写真ディレクション統一 等）の知見を反映し、**KEEP / REFINE / CREATE / IGNORE** の 4 象限に分類。

## 4 象限の定義

| 象限 | 定義 | アクション |
|---|---|---|
| **KEEP** | DS v0.2 適用済 + DNA 整合済。ブランド貢献度高く維持優先 | 監視 + 微調整のみ。次の DS バージョン更新時に同期 |
| **REFINE** | 既存だが DNA 反映不十分 / 競合より弱い / DS v0.2 未適用 | 半期内に DNA / DS 反映の改善実装。優先順位は影響範囲で決定 |
| **CREATE** | M4 観察 / OKR 目標 / DNA v1.0 で必要と判明した未存在の接点 | 新規企画 → spec → 実装の順で着手。リソース配分計画必須 |
| **IGNORE** | FAM legacy / 重複 / 用途消失 / fam-jp.com 移行ターゲット | 段階退役。新規工数投入禁止。代替接点へのリダイレクト後に削除 |

---

## 🟢 KEEP — 維持優先（DS v0.2 + DNA 整合済）

| 接点 | 現状 | ブランド整合 |
|---|---|---|
| **Header v0.2**（fambox-header / header.liquid） | PR #2 視覚回帰 GO 判定済 | Drive Pill CTA / Logo 左固定 / Anti 回避すべて準拠 |
| **fambox-modal**（v0.2 達成 / Phase B-5 Token 化済） | OKR KR1-2 完成基準到達 | Token フル準拠 |
| **fambox-stat-grid**（Stat Card v0.2） | OKR KR1-2 完成基準到達 | h2 Ink 価格 + 数値ジャンプ率 |
| **fambox-footer / footer.liquid**（L4 Footer v0.2） | 3 variants + Ink background + Legal essential | Ink 背景の規律準拠 |
| **fambox-bento-grid**（L4 Bento Grid v0.2） | DNA 5 sizes + 12 col system | 視覚軸 1「静の信頼 — Lab × Editorial」整合 |
| **fambox-contact-form** | OKR KR2-1 完成基準対応 | 10 フィールド・inline 確認・カスタム自動返信 |
| **/pages/tokusetsu-jisseki**（導入実績） | 2026-05-22 公開済 | TOYOTA / テイ・エステック / 大前さん監修連携、Hero ジグザグアニメ |
| **守屋選手企画ページ**（fambox-interview 連動） | 個人契約 + 夏合宿シーズン展開 | a 層差別化軸（トップアスリート監修）と整合 |
| **Seal Subscriptions メール 12 種** | 統一刷新済（2026-04-23 投入） | Verbal v1.0/v1.1 準拠 |
| **食事診断ウィザード**（fambox-food-diagnosis） | 大前さん文言チェック完了 | Verbal Identity v1.0/v1.1 準拠・4 画面構成 |
| **FAMBOX Design System Figma**（QsiBrc2v20BYw76YHI9x3e） | 117 Variables + 213 Components 公開済 | DNA L1 Token と一対一マッピング |

**合計**: 11 接点

---

## 🟡 REFINE — 改善対象（既存だが DNA / DS 反映不十分）

| 接点 | 現状の課題 | 改善方向 | 優先 |
|---|---|---|---|
| **Shopify TOP**（index.html / fambox-hero-v17/v18） | Hero v17 系で複数バージョン履歴・Token 未統一 / 視覚軸 1「Lab × Editorial」反映弱い | Hero v18 リファクタで Token 統一 + GREEN SPOON ライク写真ディレクション統一度向上 | 🔴 High |
| **商品詳細 LP**（main-product / featured-product） | Drive Pill CTA は適用済だが数値訴求のジャンプ率が弱い（筋肉食堂 DELI 比） | Stat Grid 流用で「タンパク質 ◯g」「カロリー ◯kcal」を超ジャンプ率で打ち出し | 🔴 High |
| **問合せフォーム → 商談動線** | L5-5 で「営業日翌日中の初回返信」と確定（24h 以内は将来目標）/ 自動返信は POP #2 整備領域 | 受信確認自動返信を **即時化**（システム整備の最優先項目） | 🔴 High |
| **fambox-faq** | bulk maintenance 適用済だが Q&A 内容が a 層（法人プロ）向けに最適化されていない | 法人 FAQ / 個人 FAQ を分離 + Drive CTA で「話を聞いてみる」誘導 | 🟡 Mid |
| **Blog 記事テンプレ**（case-standard / case-featured / NEWS） | LLMO 8 項目準拠 + Verbal v1.1 準拠だが、a 層差別化軸（トップ栄養士・トップアスリート監修）の見える化が弱い | 監修クレジット表示の標準化 / 「FAM スポーツ栄養アドバイザー」キャラ登場ルール | 🟡 Mid |
| **fambox-spirit**（FAMBOX / fam-spirit 並存） | 並存状態・FAM 版が legacy | fambox-spirit 単独に統一 + fam-spirit を IGNORE 領域へ | 🟡 Mid |
| **fambox-active-plans v1 / v2 並存** | v1 と v2 が並存 | v2 へ統一 + v1 退役 | 🟡 Mid |
| **fambox-value-proposition** | 価値訴求コンテンツが Messaging Pillar 確定前のもの | Pillar 1「栄養で、可能性の確度を上げる」/ Pillar 2「支えるではなく、共に創る」を反映 | 🟡 Mid |
| **fambox-easy-cooking** | 単独使用 / DNA v0.5 対応未見直し | DNA v1.0 反映 + Editorial × Wellness 路線整合 | 🟢 Low |
| **Instagram（@fambox）** | スティッキー CTA / bio リンクは tokusetsu-jisseki に統一済 | 投稿テンプレを moritani-content-generator skill 経由で標準化 | 🟢 Low |
| **fambox-nutrition-service**（大前さんアドバイザー紹介） | 写真 master 待ち（M1 不足分依存） | M1 不足分回収後に写真差替 + Editorial 路線整合 | 🟢 Low |
| **物理接点 — 定期便パッケージ / 同梱物 / 納品書 / サンプル / アフターケアチラシ**（POP #2 整備優先領域） | L2-7 で整備優先領域として明示済（現状未熟） | ADR-033 L4-14 ロックアップ実装後に Phase C で展開 | 🔴 High（OKR KR2-2 連動） |

**合計**: 12 接点（High 3 / Mid 5 / Low 3 + 物理接点バンドル 1）

---

## 🔵 CREATE — 新設候補（M4 観察 + DNA v1.0 + OKR で必要と判明）

| 接点 | 必要性の根拠 | 仕様の方向 | 優先 |
|---|---|---|---|
| **B2B 独立 LP**（office.fambox.jp 想定） | M4: nosh office / 筋肉食堂Office が独立ドメイン LP で B2B 営業の手本。OKR KR1-5 直結 | 別ドメイン or `/pages/corporate` で B2C ノイズ排除 + 資料 DL 1 本集中 + 縦組大型コピー | 🔴 High |
| **法人提案資料テンプレ**（PPT or PDF） | a 層営業面談（三宅・深澤・井上経由）の標準化が未整備 | pptx-generator + pptx-presenter-prep skill 経由 / 游ゴシック / 1 スライド 6 行以内 | 🔴 High |
| **YouTube チャンネル**（owned media 強化） | L5-2 接点リストには含まれているが現状空欄 | 守屋選手企画 / 大前さん monitor インタビューを軸に半年で 8 本目標 | 🟡 Mid |
| **アカデミー / セミナー LP**（c 層 Influencer 経路） | L5-2 で「将来」だが、c 層を Influencer 層として育てる Champion 戦略の中核 | 月次セミナー予約フォーム + Blog 連動 + 栄養士向け Newsletter | 🟡 Mid |
| **Press Release テンプレ**（FAM × FAMBOX co-branding） | ADR-024 ⑦ Co-branding ルールの実装版が未整備 | 「FAM / FAM BOX」表記 + Press Release 配信先リスト + 統一テンプレ | 🟡 Mid |
| **ブランド運用ガイド**（社内 / 外部協力者向け） | ADR-035 候補。L5-9 v1.0 後着手予定 | 「これだけは守って」10 項目 + ロックアップルール + Tone of Voice | 🟢 Low（ADR-035 で着手） |
| **a 層差別化見える化ページ**（監修・実績の一覧） | a 層 POD #1「トップ栄養士・トップアスリート監修」の見える化集約点 | /pages/credibility (案) — 監修者一覧 + 実績バッジ + 学術的根拠 | 🟢 Low |
| **アフターケアチラシ**（同梱物） | L5-2 物理接点リストに記載・現状未制作 | 開封後の食生活アドバイス + FAQ 抜粋 + 次回お届け案内 + 問合せ QR | 🟡 Mid |

**合計**: 8 接点（High 2 / Mid 4 / Low 2）

---

## 🔴 IGNORE — 退役対象（FAM legacy / 重複 / 用途消失）

| 接点 | 退役理由 | 退役方法 |
|---|---|---|
| **fam-corp-***（10 sections: contact-channels / faq / features / hero / interview / issues / mission / nutrition-service / solution / steps / supervisor / text-block） | FAM 法人ページ用 / fam-jp.com 移行ターゲット | fam-jp.com 移行完了後に削除 |
| **fam-active-plans v1 / v2** | FAMBOX 版に統合済 | fam-jp.com 移行後 |
| **fam-blog-hero / fam-blog-posts** | FAM ブログ用 | fam-jp.com 移行後 |
| **fam-collection-plan / fam-collection-tabs** | fambox 版との重複 | fambox-* に統一後削除 |
| **fam-footer-test / fam-footer-v2** | テスト用 / v2 は legacy | 即座に削除可（commit で removal） |
| **fam-header-menu**（fambox / fam 両方） | Header v0.2 に統合済 | Header v0.2 正式採用後に削除 |
| **fam-item / fam-item-plans** | FAM 専用商品 / fambox-* への置換 | 置換後 |
| **fam-nav / fam-nav-panels** | Header v0.2 で置換 | Header v0.2 正式採用後 |
| **fam-plan-features / fam-solution** | fambox-* への置換 | 置換後 |
| **fam-spirit / fam-voices / fam-voices-message** | fambox 版に統合 or アスリート voices に統合 | 統合後 |
| **fam-subscription-plan** | Seal + fambox-* に統合 | 統合後 |
| **fam-achievement** | tokusetsu-jisseki と整合させる方向 | tokusetsu-jisseki 強化後に削除 |
| **fam-sticky-cta** | DS v0.2 button.md と整合させた fambox-sticky-cta が候補 | 置換後 |
| **custom-blog-carousel** | fambox-blog-carousel と重複 | fambox-* に統一 |
| **layouthub_header / pagefly-section / pagefly-app-header** | 外部アプリ依存 / 既存テーマで未使用 | 削除候補（要動作確認） |
| **マッスルデリ式 旧 EC 風 UI** | M4 でシンプルミール / 旧 EC 路線を FAMBOX が避けるべきと判定 | 既存 fambox 内に旧パターン残骸がないか確認 |
| **ピヨピヨ層への寄り添い表現** | ADR-014 で Anti として扱う方針確定 | 既存 Blog / SNS / メールテンプレで該当箇所があれば修正（Verbal v1.1 監査） |

**合計**: 17 接点（M2 重複統合候補と完全に整合）

---

## サマリ（4 象限件数）

| 象限 | 件数 | 割合 |
|---|:---:|:---:|
| 🟢 KEEP（維持） | 11 | 23% |
| 🟡 REFINE（改善） | 12 | 25% |
| 🔵 CREATE（新設） | 8 | 17% |
| 🔴 IGNORE（退役） | 17 | 35% |
| **合計** | **48** | 100% |

## カスタマージャーニー 6 ステージとの対応

L5-1 の 6 ステージ × 4 象限のクロス分析:

| ステージ | KEEP | REFINE | CREATE | IGNORE |
|---|---|---|---|---|
| 1. 認知（SNS / 紹介 / 検索） | Instagram | Blog 記事テンプレ | a 層差別化見える化ページ / Press Release テンプレ | （該当なし） |
| 2. 情報収集（LP / Blog / YT） | tokusetsu-jisseki / Seal メール | Shopify TOP / Blog テンプレ | YouTube / 法人 LP | fam-blog-* |
| 3. 比較検討（診断 / 競合比較） | 食事診断 / Bento Grid | 商品詳細 LP / fambox-faq | アカデミー LP | fam-* legacy |
| 4. 問合せ（フォーム / メール） | fambox-contact-form | 問合せ → 商談動線 | 法人提案資料テンプレ | （該当なし） |
| 5. 商談〜契約（面談 / 提案 / 試食） | 守屋選手企画 | fambox-nutrition-service | 法人提案資料 / 監修見える化 | （該当なし） |
| 6. 運用〜継続（定期便 / サポート） | Seal メール / fambox-modal | 物理接点（POP #2 整備） | アフターケアチラシ | fam-active-plans-* |

## OKR 連動

| 象限 | 連動 OKR | 達成寄与 |
|---|---|---|
| **KEEP** | KR1-2 DS 完成 / KR2-1 4 画面 DNA 反映 | DS v0.2 / DNA v1.0 公式昇格の維持 |
| **REFINE**（特に High 3 件） | KR1-2 DS Phase B / KR2-1 / KR2-2 | Hero v18 + 商品詳細 + 問合せ動線の改善が CVR 3% 達成のクリティカルパス |
| **CREATE**（特に B2B LP + 法人提案資料） | **KR1-5 B2B チャネル設計** | B2B 営業の標準化が KR1-5 達成の前提 |
| **IGNORE**（FAM legacy 大量退役） | fam-jp.com 移行（KR1-7 別建て） | 2 年共存移行（L0〜L5）の進捗を加速 |

## 次のアクション（半期計画）

### 🔴 High 優先（6 月内着手）

1. **REFINE**: Hero v18 リファクタ（Token 統一 + 写真ディレクション統一）
2. **REFINE**: 商品詳細 LP の数値ジャンプ率強化（Stat Grid 流用）
3. **REFINE**: 問合せフォーム受信確認の **即時自動返信化**（POP #2 整備優先）
4. **CREATE**: B2B 独立 LP 設計 → 実装（office.fambox.jp 案 / KR1-5 直結）
5. **CREATE**: 法人提案資料テンプレ（pptx-generator skill 経由 / a 層営業の標準化）

### 🟡 Mid 優先（7-8 月内着手）

6. **REFINE**: Blog 記事テンプレに監修クレジット表示標準化
7. **REFINE**: fambox-spirit / active-plans / value-proposition の統合 + Pillar 反映
8. **CREATE**: YouTube チャンネル運用開始（半年で 8 本目標）
9. **CREATE**: アカデミー / セミナー LP（c 層 Influencer 経路）
10. **CREATE**: Press Release テンプレ + 配信先リスト整備

### 🟢 Low 優先（9 月以降）

11. **IGNORE**: fam-* legacy 大量退役（fam-jp.com 移行と並行）
12. **CREATE**: ブランド運用ガイド（ADR-035 で着手）
13. **CREATE**: a 層差別化見える化ページ

## 関連

- [Brand DNA v1.0 L5-1〜6](current.md)
- [ADR-031 v1.0 公式昇格](decisions/decisions-log.md#adr-031)
- [ADR-034 L5-7 4 象限実施](decisions/decisions-log.md#adr-034)
- [M4 競合 UI 観察結果](../MATERIALS_TIER1/M4-competitors/OVERVIEW.md)
- [M2 全 136 sections 棚卸し](../MATERIALS_TIER1/M2-sections-inventory.md)
- [OKR KR1-2 / KR1-5 / KR2-1 / KR2-2](../../docs/okr/)

## 変更履歴

- 2026-05-27: Initial matrix — 48 接点を 4 象限に分類 + カスタマージャーニー × 4 象限クロス分析 + 半期アクション 13 項目（宮川 / Claude）
