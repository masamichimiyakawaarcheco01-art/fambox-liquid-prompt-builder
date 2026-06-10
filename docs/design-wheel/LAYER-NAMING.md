# LAYER-NAMING — Figma レイヤー命名規則 v1.0

> Design Wheel の Figma 構築（figma-bridge）と FAMBOX チラシ制作に共通で適用する。
> 目的: `Group 1216122894` / `IMG_8563` / `Mask group` のような**読めないレイヤー**を根絶し、
> AI・人間の双方がレイヤー構造とコンポーネントを理解・管理・再利用できる状態を保つ。
>
> 参考: [Zenn — AI連携のためのレイヤー命名](https://zenn.dev/kshr/articles/7665e5a9e24462) /
> [kohimoto — 種類/用途/バリエーション](https://kohimoto.com/labo/web/design/18946/)

---

## 1. 基本形

```
[役割]/[用途]（必要なら /[バリエーション]）
```

- **英語小文字 kebab-case**、区切りは `/`
- 例: `section/hero` ／ `text/display` ／ `button/pill-primary` ／ `image/photo-duo/02`

## 2. 役割プレフィックス（固定語彙）

| 役割 | 対象 | 例 |
|---|---|---|
| `page/` | 最上位フレーム。`page/<パターン>-<題材>` | `page/corporate-flowops` `page/sporty-stride` |
| `section/` | 大区画（縦の章立て） | `section/hero` `section/features` `section/stats` |
| `group/` | 中間まとまり（auto-layout の行/列） | `group/stats-row` `group/hero-copy` |
| `card/` | カード単位 | `card/feature-01-connect` `card/stat-members` |
| `text/` | テキスト。用途は6段スケール名で | `text/display` `text/h2` `text/body` `text/label-num` |
| `button/` | ボタン/CTA | `button/pill-primary` `button/pill-ghost` |
| `image/` | 画像・プレースホルダ | `image/placeholder-circle` `image/photo-duo/02` |
| `shape/` | 装飾図形（帯・リング・下地） | `shape/band-accent` `shape/ring-bg` `shape/grid-base` |
| `icon/` | アイコン | `icon/arrow-ne` |
| `ui/` | **DS の既存コンポーネント instance**（Zenn 流） | `ui/Button` `ui/Field` |
| `local/` | このファイル限定のローカルコンポーネント | `local/StatCard` |

バリエーションが要る時だけ3階層目を足す: `/sm` `/lg` `/dark` `/hover` `/01`〜

## 3. HTML チャネルとの対応規則（Design Wheel 固有）

レイヤー名は **HTML 出力時のクラス名と1対1対応**させる（チャネル間でパリティを保つ）:

| Figma レイヤー | HTML |
|---|---|
| `section/hero` | `<section class="hero">` |
| `group/stats-row` | `<div class="stats">` |
| `text/display` | `.display` |
| `button/pill-primary` | `.cta` (class=pill-primary) |
| `shape/band-accent` | `.band` |

→ 片方のチャネルで作った構造を、もう片方へ**機械的に翻訳できる**ことが狙い。

## 4. 禁止事項（検収条件）

- ❌ Figma デフォルト名のまま放置: `Frame 123` `Group 1216122894` `Ellipse 1048` `Rectangle 12`
- ❌ 取り込みファイル名のまま: `IMG_8563` `AdobeStock_224556797 1` `スクリーンショット...`
  → 配置時に `image/photo-<被写体>-<場所>`（例 `image/photo-athlete-track`）へ改名
- ❌ `Mask group` のまま → `image/masked-<用途>`（例 `image/masked-hero-circle`）
- ❌ 日本語レイヤー名（テキスト**内容**は日本語可、レイヤー**名**は英語）
- ❌ 同一階層での名前重複（`/01` `/02` で連番化）

## 5. figma-bridge 運用ルール

1. **`create_frame` / `create_text` / `create_rectangle` は必ず `name` パラメータを本規則で渡す**（無名作成禁止）
2. **bridge に rename ツールは無い** → 命名は**作成時が唯一のチャンス**。作成順=z-order と同様、先に設計する
3. ビルド後検収: `scan_nodes_by_types` で全ノードを取得し、`Frame/Group/Ellipse/Rectangle + 数字` パターンが**0件**であることを確認（孤児フレーム検査=学び3 と同時に行う）
4. 人間が Figma 上で素材（写真等）を差し込む時も本規則で改名する（人間3割の作業に含める）

## 6. 適用例 — sporty-stride を本規則で書き直すと

```
page/sporty-stride
├── section/hero
│   ├── shape/grid-base
│   ├── shape/ring-bg
│   ├── text/label-eyebrow
│   ├── text/display
│   ├── image/runner-ghost
│   ├── image/runner-duo
│   ├── shape/band-accent
│   │   └── text/marquee
│   └── button/pill-primary
│       └── text/cta-label
└── section/content
    ├── group/stats-row
    │   ├── card/stat-members   ├ text/stat-num ├ text/label
    │   ├── card/stat-sessions  └ …
    │   └── card/stat-goal
    └── group/photos-row
        ├── image/photo-duo/01
        ├── image/photo-duo/02
        └── image/photo-duo/03
```

## 7. チラシ（fambox-flyer-builder）への適用

- 最上位: `page/flyer-<対象>-<面>`（例 `page/flyer-c-front` `page/flyer-b-back`）
- 背景バンドゾーニング: `shape/band-<位置>`（例 `shape/band-top` `shape/band-bottom`）
- グレーボックス画像: `image/placeholder-<用途>`、写真差込後 `image/photo-<被写体>` へ改名
- モジュール: `group/module-<名前>`（例 `group/module-price-table`）

---

**改訂履歴**: v1.0 2026-06-10 起草（宮川さん依頼 / Marc アドバイス起点。参考2記事＋HTML チャネル実験の知見を統合）
