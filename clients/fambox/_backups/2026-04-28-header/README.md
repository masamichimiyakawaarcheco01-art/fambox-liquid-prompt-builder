---
title: Header Liquid Backup — 2026-04-28
type: backup
created: 2026-04-28
purpose: DS v0.2 Header Spec 適用前の Liquid バックアップ。EC 機能（Cart / Account / Search / Localization）を保護するための復元元。
related_branch: feat/ds-header-v0.2
related_pr: TBD
---

# Header Liquid Backup（2026-04-28）

## 目的

`projects/fambox/sections/header.liquid` および `projects/fam/sections/header.liquid` を **DS v0.2 Header Spec 適用前の状態**で保管。

EC 機能（Cart / Account / Search / Localization）が DS 適用後に壊れた場合、このバックアップから即座に復元するための安全弁。

## バックアップ内容

| ファイル | 元のパス | 行数 | 取得日時 |
|---|---|---|---|
| `header.liquid.bak` | `projects/fambox/sections/header.liquid` | 621 | 2026-04-28 |
| `header_fam.liquid.bak` | `projects/fam/sections/header.liquid` | 621 | 2026-04-28 |

## 復元手順

問題発生時:

```bash
# fambox 側を復元
cp clients/fambox/_backups/2026-04-28-header/header.liquid.bak \
   projects/fambox/sections/header.liquid

# fam 側を復元
cp clients/fambox/_backups/2026-04-28-header/header_fam.liquid.bak \
   projects/fam/sections/header.liquid

# git で確認
git diff projects/fambox/sections/header.liquid
git diff projects/fam/sections/header.liquid
```

または Git revert:

```bash
# 該当 commit を特定
git log --oneline projects/fambox/sections/header.liquid

# 直前の改修 commit を revert
git revert <commit-hash>
```

## 保管期間

DS v0.2 Header の本番反映から **30 日間** はこのバックアップを保持。
問題なく稼働確認できたら `clients/fambox/_backups/_archive/` 配下に移動可。

## 関連ドキュメント

- DS Spec: `brand/fambox/design-system/components/header.md`（v0.2 confirmed）
- 実装計画: `brand/fambox/design-system/operations/2026-04-28-top-implementation-plan.md`
- 改修ブランチ: `feat/ds-header-v0.2`

## EC 機能保護チェックリスト（DS 適用後の検証必須項目）

- [ ] Cart drawer の開閉
- [ ] Cart icon bubble のカウント表示
- [ ] Account login / logout フロー
- [ ] Search drawer の開閉 + 検索結果遷移
- [ ] Localization（国・言語）切替
- [ ] Sticky header on scroll の挙動
- [ ] PC / SP / Tablet 全レンジで動作確認
- [ ] 1 商品の購入完了まで通す（決済テスト）
