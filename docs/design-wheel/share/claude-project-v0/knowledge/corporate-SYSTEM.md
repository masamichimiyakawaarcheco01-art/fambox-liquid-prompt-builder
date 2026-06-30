# corporate — SYSTEM.md (v0)

> 真ソース。3枚の参照（[refs.md](refs.md)）を実画像解析し PATTERN-SCHEMA に統合した v0。
> figma-bridge はこのファイルを読んで構築する。値は v0（critique で改訂）。

## 1. Identity
- **パターン名**: corporate
- **一言定義**: neutral 基調＋1アクセントの禁欲的な配色で、超高ジャンプ率のタイポと番号付きセクションが「信頼感・先進性」を作る、B2B/SaaS/法人サイトの様式。
- **代表ref 3枚**:
  1. [Security, Reinforced（fintech / 1アクセント）](../../../../brain/45_Design_Refs/2026/06/2026-06-10_arrasel-corporate-ui.md)
  2. [Pharmacy Automation（healthcare / 明るい・ほぼモノクロ）](../../../../brain/45_Design_Refs/2026/06/2026-06-10_pharmacy-automation-corporate.md)
  3. [RIDEQUEST（transport / ダーク・赤アクセント）](../../../../brain/45_Design_Refs/2026/06/2026-06-10_ridequest-transport-corporate.md)

## 2. Color
3枚共通の規律＝**neutral ベース + 最大1つの暖色アクセント**。明・暗の2モードを持つ。

**Light（主）**
| 役割 | 値 | 用途 |
|---|---|---|
| bg | #F4F5F6 | 画面背景（極薄グレー） |
| surface | #FFFFFF | カード/面 |
| ink | #111114 | 見出し・主テキスト |
| ink-muted | #8A8A90 | 副テキスト・ラベル |
| accent | #E8431F | CTA・データ強調（**1色のみ**） |
| line | #ECECEE | 罫線・カード境界（hairline） |

**Dark（副 / RIDEQUEST 系）**
| 役割 | 値 | 用途 |
|---|---|---|
| bg-dark | #0E0E10 | 暗セクション背景 |
| surface-dark | #1A1A1D | 暗面 |
| ink-on-dark | #FFFFFF | 暗面上テキスト |
| accent | #E8431F | 共通（明暗で同一アクセント） |

**ゾーニング規則**: 背景=bg（または黒白交互ブロック）／カード=surface／見出し・本文=ink／**accent は CTA・数値・極小ラベルの1点強調のみ**（面塗りに多用しない）／区切り=line の hairline。

## 3. Type
- **書体方針**: クリーンなグロテスク sans 1ファミリで wght を振る（Inter / Helvetica Now 系）。日本語は Noto Sans JP / Hiragino Kaku Gothic。装飾書体は使わない。
- **6段スケール（PC）**: 飾り/Display 64px(w700) / 大H1 44px(w700) / H2 28px(w600) / H3 18px(w600) / Body 14px(w400) / Small 11px(w500・uppercase・letter-spacing .08em)
- **ジャンプ率**: **高**（Display 64 ÷ Body 14 ≒ 4.6x）。corporate の信頼感は「特大見出し × 極小 uppercase ラベル」のコントラストで作る。中間サイズの乱用禁止。
- **行間**: 見出し 1.05–1.1 ／ 本文 1.6

## 4. Layout
- **グリッド**: 12カラム / ガター 24px / 外マージン広め（PC 80px 目安）。セクションは 2〜4 カラムの可変ブロック。
- **整数比**: ヒーローは 1:1 または 5:7 の split（画像 : テキスト）。
- **余白 S/M/L（等比 2x）**: S 16px / M 32px / L 64px（セクション縦パディングは L〜96px）。

## 5. Components
| 要素 | 角丸 | 影 | 状態 |
|---|---|---|---|
| ボタン（pill） | 999px | なし | hover 暗化（ink→#000）／↗アイコン付 |
| カード | 16px | なし〜極微(0 1px 2px rgba(0,0,0,.04)) | hover 微浮き(translateY -2px) |
| ヘッダ | — | なし | 透明/白・丸アイコンボタン（≡/検索）・細下線リンク |
| 円形マスク画像 | 50% | なし | hover 拡大（scale 1.03） |
| 番号ラベル | — | — | ● + uppercase（●ABOUT US / 01・02・03） |

## 6. Motion
- **速度**: 0.3s
- **イージング**: cubic-bezier(.2,.6,.2,1)（ease-out 寄り）

## 7. DO / DON'T
- ✅ DO: neutral×1アクセント厳守／番号付きマイクロラベルでセクションを刻む／超高ジャンプ率（特大見出し×極小ラベル）／円形マスク画像をアクセントに／ピルCTA＋↗矢印／徹底した余白／明 or 暗のどちらかに寄せる。
- ❌ DON'T: アクセント2色以上／パステル多用／太い装飾枠・多重シャドウ／密なテキスト／中間サイズ見出しの乱用でジャンプ率を殺す／明暗を1画面で中途半端に混ぜる。
