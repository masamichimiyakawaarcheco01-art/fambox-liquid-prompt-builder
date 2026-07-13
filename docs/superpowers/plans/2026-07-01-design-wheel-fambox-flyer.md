# Design Wheel FAMBOX チラシ対応 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Design Wheel に FAM ブランド（SNS/Web/印刷）を HTML キャプチャで生成できる `fambox` パターンを追加し、あわせて A4 チラシ用 `flyer` モード＋PDF書き出しを実装する。パターンは3つの配色サブスタイル（SNS-Poster / Web-DNA / Print-Flyer）を持つ。

**真ソース（ブランド）:** `brand/fam/brand-dna/current.md`（v0.5・確定色/タイポ）＋ 印刷は `.claude/skills/fambox-flyer-builder/references/taste-and-tokens.md`。マレルFB(2026-07)の正hex・写真/配色/タイポ規律を反映。

**Architecture:** 既存の Design Wheel（Node+Express / Anthropic SDK 生成 / Chrome ヘッドレス書き出し / 素HTMLフロント）に、新パターン SYSTEM.md、印刷レイアウト foundation、flyer モード分岐、A4サイズ＋PDF書き出しを**追加**する。既存パターン・モードの挙動は変えない。真ソースは git の `patterns/fambox/SYSTEM.md`（ADR-001 不変条件）。

**Tech Stack:** Node.js (ESM) / Express / @anthropic-ai/sdk (claude-opus-4-8) / Chrome headless (`--screenshot` / `--print-to-pdf`) / Google Fonts。

**検証方針:** このコードは単体テスト基盤を持たない。検証は「サーバー起動 → curl/node で API 実行 → PNG/PDF を目視」で行う（既存の実証方法に準拠）。API 生成は宮川さんの `.env` の専用キーを消費する点に留意（コスト）。

**作業ディレクトリ:** リポジトリルート = `/Users/archecoinc./Desktop/Claude_1`。アプリ = `tools/design-wheel-app/`。

---

## Task 1: 印刷レイアウト foundation を作成

**Files:**
- Create: `docs/design-wheel/foundations/PRINT-LAYOUT.md`

- [ ] **Step 1: ファイルを作成**

以下の内容で `docs/design-wheel/foundations/PRINT-LAYOUT.md` を作成する（flyer モード時のみ注入される印刷固有の作法。FOUNDATIONS の上乗せ）:

```markdown
# PRINT-LAYOUT — 印刷物（チラシ）の作法（flyer モード時のみ）

> FOUNDATIONS（普遍の骨格）に上乗せする、A4 1枚チラシ固有の作法。
> 出典: fambox-flyer-builder build-playbook の HTML 版蒸留。

## 出力の絶対条件
- **A4 縦1枚に収める**。`<body>` と最外要素を A4 比率（794×1123px 相当）に固定し、スクロール・改ページを作らない。
- CSS に `@page{size:A4;margin:0}` と `html,body{margin:0;padding:0}` を入れる（PDF 書き出しで余白ゼロ・単一ページにするため）。
- 最外コンテナは `width:794px;height:1123px;overflow:hidden;position:relative`。

## 作る順番（ブロッキング先行）
1. **面積で情報優先度を分割**（色でなく面積の%ブロッキング）。まず帯・カラムで大きく割る。
2. プレースホルダを置いて俯瞰。
3. **収まらない情報は削る**（A4 1枚に詰め込まない。優先度の低い情報は落とす）。
4. 優先度の高い順に精緻化。

## 印刷レイアウトの語彙
- **マストヘッド全ブリード**: 最重要の帯（ロゴ/キャッチ）は紙端までフルブリード（余白ゼロ・`width:100%`・左右いっぱい）。
- **背景の帯でゾーニング**: 濃い面＝impact（掴み）、淡い面＝reading（本文）。レイヤーを重ねて境界をまたぎ、影で立体に。
- **画像はグレーボックス**（`#D9D9D9` / `#E2E2E2`）でプレースホルダ。汎用写真が要れば images.unsplash.com。実写真は宮川さんの仕上げ工程。
- **余白は8の倍数**（4/8/12/16/20/24/32/40/56）。内側 padding は 32 基準。
- **本文行間170%**、英字 eyebrow ラベル、オレンジ罫の線アクセント。
- **斜体＝エネルギー**。数字・実績・価格・栄養価は特大スタッツ化。
- 彩度の高いベタ面を2つ隣接させない。1色=1役割を全面で一貫。

## 仕上げの締め（必ず提示）
> ✅ ここまで約70%。仕上げに：① 実写真の差し替え（今はグレーbox）② 文言・数値の最終確認 ③ 入稿する場合は Figma（fambox-flyer-builder）で塗り足し・CMYK化。
```

- [ ] **Step 2: 作成を確認**

Run: `wc -l docs/design-wheel/foundations/PRINT-LAYOUT.md && head -3 docs/design-wheel/foundations/PRINT-LAYOUT.md`
Expected: 行数が出力され、1行目が `# PRINT-LAYOUT — 印刷物（チラシ）の作法（flyer モード時のみ）`

- [ ] **Step 3: コミット**

```bash
cd /Users/archecoinc./Desktop/Claude_1
git add docs/design-wheel/foundations/PRINT-LAYOUT.md
git commit -m "feat(design-wheel): 印刷レイアウト作法 PRINT-LAYOUT.md 追加"
```

---

## Task 2: fambox パターンの SYSTEM.md を作成

**Files:**
- Create: `docs/design-wheel/patterns/fambox/SYSTEM.md`

真ソース = `brand/fam/brand-dna/current.md`（v0.5 確定色/タイポ）＋ 印刷は `.claude/skills/fambox-flyer-builder/references/taste-and-tokens.md`。マレルFB(2026-07)の正hex・写真/配色/タイポ規律を反映。

- [ ] **Step 1: ディレクトリとファイルを作成**

`docs/design-wheel/patterns/fambox/SYSTEM.md` を以下の内容で作成する:

```markdown
# FAM — パターン SYSTEM（FAM ブランド共通：SNS / Web / 印刷）

> 用途: FAM / FAM BOX ブランドの制作物。非デザイナーが70%品質の叩き台を出す。
> 真ソース: `brand/fam/brand-dna/current.md`（v0.5 確定色/タイポ）＋ 印刷は `fambox-flyer-builder/taste-and-tokens.md`。マレルFB(2026-07)反映。
> page / banner(SNS) / flyer の全モードで使える。

## FAM 絶対ルール（全サブスタイル共通・世界観ガイド。これを破ると FAM でなくなる）
- **写真はカラーそのまま**。デュオトーン/モノトーン/カラーオーバーレイ/スクリム暗化を**かけない・提案しない**（FAM世界観違反）。調整は"良い写真を選ぶ／軽い補正"側で。
- **オレンジ `#FB4C15` は CTA・アクション専用**。見出しや広い面に多用しない。
- **暗背景×オレンジ文字を避ける**。CTA は「**オレンジ地＋白文字**」を標準。
- **タイポは抑制**：Poppins（英）＋Hiragino Sans（和）。コンデンス体・ALL CAPS の多用を避ける。メリハリは数値/実績サイズで作る。
- 権威性（プロ選手・監修）を前面に。左端揃えの骨格。装飾過多にしない（装飾過多で中身が見えない＝FAMっぽくない）。

## サブスタイル（配色系統。既定 = A SNS/Poster）
### A. SNS / Poster（既定・banner / リール / 投稿向け）
- ベース: **黄 `#F5C842` × ダーク `#1A1A1A`**。
- 文字色: ダーク面は白 `#FFFFFF`、黄面は `#1A1A1A`。
- CTA: **オレンジ `#FB4C15` 地＋白文字**（画面で1点のみ）。
- 用途: Instagram リール表紙・フィード・ストーリー。権威性の前出し。

### B. Web / DNA（page 向け・ブランドDNA v0.5準拠）
- 色: Drive Orange `#FB4C15`(CTA/達成値) / Sky Blue `#3DB8E8`(データ) / Deep Blue `#0F2A5C`(信頼/ヒーロー深部) / Ink `#1B1D1A`(本文) / Off-White `#FFFFFF`・`#FAFAFA`・`#F3F3F3`。
- Bento Grid＋部分ガラス、Editorial×Lab、余白大。
- 用途: Web LP・ダッシュボード・商品紹介。

### C. Print / Flyer（flyer 向け・印刷DNA）
- 色: Drive Orange `#FB4C15`(CTA/効果音) / Deep Blue `#0F2A5C` / アンバー `#FFA41A`・イエロー `#FFCC24`(データ/実績) / 暖ブラックインク `#252726`(純黒にしない) / オフホワイト `#F7F6F4`。
- 印刷フレーバー（プロンプトで選ぶ・既定 Editorial）: **Editorial**（雑誌的・データ可視化）/ **Manga**（掴み・極太見出し Dela Gothic One・斜めコマ）/ **Corporate**（B2B図解・帯・2本柱）。
- A4固定（PRINT-LAYOUT準拠）。梱包同梱チラシは Editorial 主体。

## タイポグラフィ（Google Fonts で実レンダリング）
- 英数字 = **Poppins**（wght 400/500/600/700）。
- 日本語 = **Hiragino Sans** system stack: `'Hiragino Sans','Hiragino Kaku Gothic ProN','Noto Sans JP','Meiryo',sans-serif`（HTMLキャプチャ環境に Hiragino が無ければ Noto Sans JP に自動フォールバック。Noto Sans JP は Google Fonts で読み込む）。
- 明朝的箇所 = Noto Serif JP。C の極太コミック見出しのみ = Dela Gothic One（Google Fonts）。
- スケール(px): `12/14/16/20/24/32/48/64/96/128`。行間: 見出し1.2 / 本文1.75 / キャプション1.5。字間: 英 -0.02em / 和 0.02em。
- ジャンプ率は高め（display 64-96 ↔ body 14-16）だが **コンデンス/ALL CAPS に頼らない**。数値・実績・価格・栄養価は特大スタッツ化。

## レイアウト / グリッド
- 12カラム / gutter 24px / 8px baseline。余白は8の倍数（8/16/24/32/48/64/96/160）。印刷は 4/8/12/16/20/24/32/40/56 も可、内側 padding 32基準。
- 主構図: 左下→右上の対角線、**左端揃え**。二項対置（Your/Our）。
- 角R: カード8px / 小4px / **CTAピル 50px** / バッジ 9999px。ボタンPrimary = Drive色・白文字・ピル50px。

## 写真・イメージ
- 主題: 決定的瞬間・息遣い・汗・上を向く視線・前方への躍動。動きの途中（静止写真は避ける）。タイポと重ね合わせOK。
- 処理: **カラーそのまま**（オーバーレイ/デュオトーン禁止）。彩度やや抑制・コントラスト高めは"素材選び・軽い補正"で。
- 権威性: プロ選手・監修（大前恵・和田毅）を前面に。
- 素材が無い場合はグレーボックス `#D0D0D0` プレースホルダ＋「実写真差し替え」を仕上げに明記。

## 言葉遣い
- 短く前向き・動詞中心（"次へ""動かす""続ける""積み上げる""挑む""駆動"）。命令形・上から目線・"頑張って"・曖昧応援は禁止。見出しで英字主役＋日本語サポート可。

## 確定マスターデータ（差し替えマスター・そのまま使う）
- ブランド名: **FAM**（親）/ **FAM BOX**（冷凍宅配・スペース有）。文脈で使い分け。
- クーポン: `B8483HVWMNEZ`（30%OFF）／初回50%引き定期
- 公式: fam-athletefood-frozen.com ／ fam-jp.com
- 電話: 03-6433-5306 ／ メール: fam.athletefood.frozen@gmail.com
- 製造所: 花かがみ（福岡県北九州市小倉北区熊谷1-29-22）
- 運営: 株式会社ARCHECO（〒150-0001 東京都渋谷区神宮前1-15-4 Barbizon76 3F）
- 監修: 大前 恵・和田 毅

## 出力ルール
- 上の絶対ルール・色・フォント・確定情報を厳守（創作しない）。写真加工（デュオトーン/オーバーレイ）は提案も適用もしない。
- flyer は PRINT-LAYOUT の A4固定条件（`@page`・794×1123px・overflow:hidden）を満たす。banner はサイズ枠に固定。page はレスポンシブ。
```

- [ ] **Step 2: 作成を確認**

Run: `wc -l docs/design-wheel/patterns/fambox/SYSTEM.md && head -1 docs/design-wheel/patterns/fambox/SYSTEM.md`
Expected: 1行目が `# FAM — パターン SYSTEM（FAM ブランド共通：SNS / Web / 印刷）`

- [ ] **Step 3: コミット**

```bash
cd /Users/archecoinc./Desktop/Claude_1
git add docs/design-wheel/patterns/fambox/SYSTEM.md
git commit -m "feat(design-wheel): fambox パターン SYSTEM.md 追加（3サブスタイル）"
```

---

## Task 3: CATALOG に fambox を追加

**Files:**
- Modify: `tools/design-wheel-app/lib/patterns.js:10-15`

- [ ] **Step 1: CATALOG 配列に fambox を追加**

`lib/patterns.js` の CATALOG（10〜15行目）の sporty の次に1行足す:

```javascript
export const CATALOG = [
  { id: 'corporate', label: 'コーポレート', tagline: '余白の信頼', use: '士業・BtoB・きちんと感' },
  { id: 'digital',   label: 'デジタル',     tagline: '精度の説得', use: 'アプリ・SaaS・IoT・テック' },
  { id: 'gradient',  label: 'グラデーション', tagline: '感性の説得', use: 'ブランド・コスメ・食・やわらかさ' },
  { id: 'sporty',    label: 'スポーティ',   tagline: '運動量の説得', use: 'スポーツ・ジム・アプリUI（2系統）' },
  { id: 'fambox',    label: 'FAM / FAM BOX', tagline: 'ブランドの説得', use: 'FAM SNS・Web・チラシ（3配色）' },
];
```

- [ ] **Step 2: 認識を確認**

Run: `cd /Users/archecoinc./Desktop/Claude_1/tools/design-wheel-app && node -e "import('./lib/patterns.js').then(m=>console.log(m.listPatterns().find(p=>p.id==='fambox')))"`
Expected: `{ id: 'fambox', label: 'FAM BOX', ... available: true }`（available:true = SYSTEM.md を認識）

- [ ] **Step 3: コミット**

```bash
cd /Users/archecoinc./Desktop/Claude_1
git add tools/design-wheel-app/lib/patterns.js
git commit -m "feat(design-wheel-app): CATALOG に fambox パターン追加"
```

---

## Task 4: generate.js に flyer モード分岐＋PRINT-LAYOUT 注入

**Files:**
- Modify: `tools/design-wheel-app/lib/generate.js`

- [ ] **Step 1: PRINT-LAYOUT をロードする定数を追加**

`generate.js` の FOUNDATIONS ロード直後（`try{...}catch{}` ブロックの後）に追記:

```javascript
let PRINT_LAYOUT = '';
try {
  PRINT_LAYOUT = readFileSync(
    join(__dir, '../../../docs/design-wheel/foundations/PRINT-LAYOUT.md'),
    'utf8'
  );
} catch { /* 無くても継続 */ }
```

- [ ] **Step 2: buildSystemPrompt の form 分岐に flyer を追加**

`buildSystemPrompt` 内の `if (mode === 'banner' && s) { ... } else { ... }` を、flyer を含む3分岐に置き換える:

```javascript
  let form;
  if (mode === 'flyer') {
    form = `# 出力形態: チラシ（A4 縦・1枚）
- A4 縦1枚。<body>と最外要素を **794px × 1123px（A4比率）に固定**し、スクロール・改ページを作らない。
- CSS に \`@page{size:A4;margin:0}\` と \`html,body{margin:0;padding:0}\` を必ず入れる。
- 最外コンテナは \`width:794px;height:1123px;overflow:hidden;position:relative\`。
- 下の PRINT-LAYOUT（印刷の作法）を厳守する。`;
  } else if (mode === 'banner' && s) {
    form = `# 出力形態: バナー1枚（${s.label}）
- これは1枚のバナー。<body> と最外要素を**正確に ${s.w}px × ${s.h}px に固定**し、スクロールを生まない。
- 全要素をこの枠の中に収める（はみ出し・余白の出しすぎを避け、構図を枠に最適化する）。
- レスポンシブにしなくてよい。この固定サイズ専用の単一構図にする。`;
  } else {
    form = `# 出力形態: Webページ（レスポンシブ。縦に長くてよい）`;
  }
```

- [ ] **Step 3: flyer 時に PRINT-LAYOUT を注入**

`buildSystemPrompt` の return 文で、FOUNDATIONS ブロックの直後・SYSTEM ブロックの前に PRINT-LAYOUT を差し込む。既存の FOUNDATIONS ブロックの直後に次を追加する（`# 厳守する設計書（SYSTEM / Layer ②）` の直前）:

```javascript
${mode === 'flyer' && PRINT_LAYOUT ? `# 印刷レイアウトの作法（PRINT-LAYOUT）— flyer 専用
${PRINT_LAYOUT}
` : ''}
```

具体的には return テンプレート内の並びを `${form}` → FOUNDATIONS ブロック → **PRINT-LAYOUT ブロック（上記）** → `# 厳守する設計書（SYSTEM / Layer ②）` の順にする。

- [ ] **Step 4: 構文チェック**

Run: `cd /Users/archecoinc./Desktop/Claude_1/tools/design-wheel-app && node --check lib/generate.js`
Expected: エラーなし（何も出力されなければ OK）

- [ ] **Step 5: コミット**

```bash
cd /Users/archecoinc./Desktop/Claude_1
git add tools/design-wheel-app/lib/generate.js
git commit -m "feat(design-wheel-app): flyer モード分岐＋PRINT-LAYOUT 注入"
```

---

## Task 5: export-png.js に A4 サイズ＋PDF 書き出しを追加

**Files:**
- Modify: `tools/design-wheel-app/lib/export-png.js`

- [ ] **Step 1: SIZES に a4 を追加**

`SIZES` オブジェクト（10〜16行目）の末尾に1行足す:

```javascript
export const SIZES = {
  '1x1':   { w: 1080, h: 1080, label: 'Instagram フィード (1:1)' },
  '4x5':   { w: 1080, h: 1350, label: 'IG 縦長 (4:5)' },
  '9x16':  { w: 1080, h: 1920, label: 'TikTok・ストーリー (9:16)' },
  '16x9':  { w: 1280, h: 720,  label: 'YouTube サムネ (16:9)' },
  '191x1': { w: 1200, h: 630,  label: 'Blog OGP・シェア (1.91:1)' },
  'a4':    { w: 794,  h: 1123, label: 'A4 チラシ（縦）' },
};
```

- [ ] **Step 2: exportPdf 関数を追加**

`export-png.js` の末尾（exportPng 関数の後）に追加:

```javascript
export function exportPdf({ html }) {
  return new Promise((resolve, reject) => {
    const dir = mkdtempSync(join(tmpdir(), 'dw-pdf-'));
    const htmlFile = join(dir, 'page.html');
    const outFile = join(dir, 'out.pdf');
    writeFileSync(htmlFile, html, 'utf8');
    const args = [
      '--headless=new', '--disable-gpu',
      '--no-pdf-header-footer',
      '--virtual-time-budget=2500',
      `--print-to-pdf=${outFile}`,
      'file://' + htmlFile,
    ];
    execFile(CHROME, args, { timeout: 20000 }, (err) => {
      try {
        if (err) return reject(err);
        const buf = readFileSync(outFile);
        resolve({ buffer: buf });
      } catch (e) {
        reject(e);
      } finally {
        try { rmSync(dir, { recursive: true, force: true }); } catch {}
      }
    });
  });
}
```

- [ ] **Step 3: 構文チェック**

Run: `cd /Users/archecoinc./Desktop/Claude_1/tools/design-wheel-app && node --check lib/export-png.js`
Expected: エラーなし

- [ ] **Step 4: コミット**

```bash
cd /Users/archecoinc./Desktop/Claude_1
git add tools/design-wheel-app/lib/export-png.js
git commit -m "feat(design-wheel-app): A4サイズ＋PDF書き出し(exportPdf)追加"
```

---

## Task 6: server.js の /api/export に format=pdf 対応

**Files:**
- Modify: `tools/design-wheel-app/server.js:8`（import）, `server.js:37-49`（/api/export）

- [ ] **Step 1: exportPdf を import**

8行目を次に変更:

```javascript
import { exportPng, exportPdf, SIZES } from './lib/export-png.js';
```

- [ ] **Step 2: /api/export に format 分岐を追加**

37〜49行目の `/api/export` ハンドラを次に置き換える:

```javascript
app.post('/api/export', async (req, res) => {
  const { html, size, format } = req.body || {};
  if (!html) return res.status(400).json({ error: 'html は必須です' });
  try {
    if (format === 'pdf') {
      const { buffer } = await exportPdf({ html });
      res.setHeader('Content-Type', 'application/pdf');
      res.setHeader('Content-Disposition', `attachment; filename="design-wheel-flyer.pdf"`);
      return res.send(buffer);
    }
    const { buffer } = await exportPng({ html, size });
    res.setHeader('Content-Type', 'image/png');
    res.setHeader('Content-Disposition', `attachment; filename="design-wheel-${size || '1x1'}@2x.png"`);
    res.send(buffer);
  } catch (e) {
    console.error(e);
    res.status(500).json({ error: 'export_failed', message: String(e.message || e) });
  }
});
```

- [ ] **Step 3: 構文チェック**

Run: `cd /Users/archecoinc./Desktop/Claude_1/tools/design-wheel-app && node --check server.js`
Expected: エラーなし

- [ ] **Step 4: コミット**

```bash
cd /Users/archecoinc./Desktop/Claude_1
git add tools/design-wheel-app/server.js
git commit -m "feat(design-wheel-app): /api/export に format=pdf 対応"
```

---

## Task 7: フロントに flyer トグル＋PDF ボタンを追加

**Files:**
- Modify: `tools/design-wheel-app/public/index.html:65-69`（modes）, `:87`（export ボタン）
- Modify: `tools/design-wheel-app/public/app.js`

- [ ] **Step 1: モードトグルに flyer を追加**

index.html の `#modes`（65〜69行目付近）に3つ目を追加:

```html
        <div class="modes" id="modes">
          <div class="mode on" data-mode="page">Webページ<small>縦長LP</small></div>
          <div class="mode" data-mode="banner">バナー1枚<small>選んだサイズちょうど</small></div>
          <div class="mode" data-mode="flyer">チラシ<small>A4縦・PDF可</small></div>
        </div>
```

- [ ] **Step 2: 書き出しツールバーに PDF ボタンを追加**

index.html の export ボタン（87行目付近）を次に置き換える:

```html
        <button class="btn btn-ghost" id="exportPdf" disabled style="display:none">PDF書き出し</button>
        <button class="btn btn-ghost" id="export" disabled>PNG書き出し</button>
```

- [ ] **Step 3: app.js のモード切替で flyer 時に A4 固定＋PDFボタン表示**

app.js の modes クリックハンドラ（5〜10行目）を次に置き換える:

```javascript
document.querySelectorAll('#modes .mode').forEach(m => {
  m.onclick = () => {
    state.mode = m.dataset.mode;
    document.querySelectorAll('#modes .mode').forEach(x => x.classList.toggle('on', x === m));
    const isFlyer = state.mode === 'flyer';
    const sizeSel = $('#size');
    if (isFlyer) { sizeSel.value = 'a4'; sizeSel.disabled = true; }
    else { sizeSel.disabled = false; }
    $('#exportPdf').style.display = isFlyer ? 'inline-block' : 'none';
  };
});
```

- [ ] **Step 4: showHtml で PDF ボタンを有効化**

app.js の showHtml 関数（63〜69行目）の `$('#export').disabled = false;` の次の行に追加:

```javascript
  if (state.mode === 'flyer') $('#exportPdf').disabled = false;
```

- [ ] **Step 5: PDF 書き出しハンドラを追加**

app.js の export ハンドラ（`$('#export').onclick = ...`）の直後に追加:

```javascript
$('#exportPdf').onclick = async () => {
  if (!state.lastHtml) return;
  const btn = $('#exportPdf'); btn.disabled = true; const orig = btn.textContent;
  btn.innerHTML = '<span class="spin"></span>PDF書き出し中…';
  try {
    const res = await fetch('/api/export', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ html: state.lastHtml, size: 'a4', format: 'pdf' }),
    });
    if (!res.ok) { const d = await res.json(); throw new Error(d.message || d.error); }
    const blob = await res.blob();
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `design-wheel-${state.pattern}-flyer.pdf`;
    a.click(); URL.revokeObjectURL(a.href);
  } catch (e) {
    alert('PDF書き出し失敗: ' + e.message);
  } finally {
    btn.disabled = false; btn.textContent = orig;
  }
};
```

- [ ] **Step 6: 手動確認（サーバー起動 → ブラウザ）**

Run: `cd /Users/archecoinc./Desktop/Claude_1/tools/design-wheel-app && (node server.js > /tmp/dw.log 2>&1 &) ; sleep 2 && curl -s localhost:8750/api/patterns | node -e "let d='';process.stdin.on('data',c=>d+=c).on('end',()=>{const j=JSON.parse(d);console.log('fambox:',!!j.patterns.find(p=>p.id==='fambox'),'/ a4:',!!j.sizes.a4)})"`
Expected: `fambox: true / a4: true`

- [ ] **Step 7: コミット**

```bash
cd /Users/archecoinc./Desktop/Claude_1
git add tools/design-wheel-app/public/index.html tools/design-wheel-app/public/app.js
git commit -m "feat(design-wheel-app): flyer トグル＋PDF書き出しボタン追加"
```

---

## Task 8: 実機検証（生成 → PDF/PNG → 目視 → 回帰）

**Files:** なし（検証のみ）。サーバーは Task 7 Step 6 で起動済みとする（停止していれば再起動）。

- [ ] **Step 1: fambox × flyer × Editorial でチラシ生成**

Run:
```bash
curl -s -X POST localhost:8750/api/generate -H 'Content-Type: application/json' \
 -d '{"pattern":"fambox","mode":"flyer","size":"a4","prompt":"アスリート向け冷凍宅配「FAM BOX」の梱包同梱チラシ。Editorialモード。キャッチ＋初回50%引き＋栄養価データ＋クーポン＋監修（大前恵・和田毅）＋連絡先。"}' \
 -o /tmp/dw-flyer.json -w "HTTP %{http_code} / %{time_total}s\n"
node -e "const d=require('/tmp/dw-flyer.json'); require('fs').writeFileSync('/tmp/dw-flyer.html',d.html); const h=d.html; console.log('chars:',h.length,'/ @page:',h.includes('@page'),'/ 794:',h.includes('794'),'/ FAM BOX:',h.includes('FAM BOX'),'/ coupon:',h.includes('B8483HVWMNEZ'))"
```
Expected: HTTP 200。`@page: true / 794: true / FAM BOX: true / coupon: true`（A4固定条件と確定情報が入っている）

- [ ] **Step 2: PDF 書き出し**

Run:
```bash
node -e "const d=require('/tmp/dw-flyer.json'); fetch('http://localhost:8750/api/export',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({html:d.html,format:'pdf'})}).then(async r=>{if(!r.ok){console.log('fail',r.status,await r.text());return;}const b=Buffer.from(await r.arrayBuffer());require('fs').writeFileSync('/tmp/dw-flyer.pdf',b);console.log('PDF bytes:',b.length)})"
```
Expected: `PDF bytes:` に正の数（数万〜数十万）。`file /tmp/dw-flyer.pdf` で PDF と確認できる。

- [ ] **Step 3: PNG 書き出し（目視用）**

Run:
```bash
node -e "const d=require('/tmp/dw-flyer.json'); fetch('http://localhost:8750/api/export',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({html:d.html,size:'a4'})}).then(async r=>{const b=Buffer.from(await r.arrayBuffer());require('fs').writeFileSync('/tmp/dw-flyer.png',b);console.log('PNG bytes:',b.length)})"
```
Expected: `PNG bytes:` に正の数。

- [ ] **Step 4: 目視チェック（Read で PNG を開く）**

`/tmp/dw-flyer.png` を Read tool で開き、次を確認:
- FAM の色（Drive Orange 中心）・Noto Sans JP/Poppins が効いている
- マストヘッド全ブリード・帯ゾーニング・8の倍数余白感・行間ゆったり
- 確定情報（FAM BOX / クーポン / 連絡先 / 監修）が入っている
- A4縦1枚に収まり切れている（見切れ・スカスカでない）

問題があれば該当ファイル（SYSTEM.md / PRINT-LAYOUT.md）を直して Step 1 から再検証。

- [ ] **Step 4.5: SNS Poster 検証（マレルFBの実ケース＝大竹選手リール表紙）**

Run:
```bash
curl -s -X POST localhost:8750/api/generate -H 'Content-Type: application/json' \
 -d '{"pattern":"fambox","mode":"banner","size":"9x16","prompt":"大竹耕太郎選手インタビューリールのフィード投稿1枚目（表紙）。SNS/Posterサブスタイル。本気で結果を出したいアマチュア〜社会人アスリート向け。プロ選手の権威性を前面に。人物写真はグレーボックスで（加工しない）。CTAは1点。ブランドはFAM。"}' \
 -o /tmp/dw-reel.json -w "HTTP %{http_code}\n"
node -e "const d=require('/tmp/dw-reel.json'); const h=d.html; fetch('http://localhost:8750/api/export',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({html:h,size:'9x16'})}).then(async r=>{const b=Buffer.from(await r.arrayBuffer());require('fs').writeFileSync('/tmp/dw-reel.png',b);console.log('PNG bytes:',b.length,'/ F5C842:',h.includes('F5C842'),'/ 1A1A1A:',/1A1A1A/i.test(h),'/ overlay?:',/duotone|mix-blend|grayscale|sepia/i.test(h))})"
```
Expected: HTTP 200 / `F5C842: true`（黄）/ `1A1A1A: true`（黒ベース）/ `overlay?: false`（写真加工が入っていない）。

`/tmp/dw-reel.png` を Read で開き目視: 黄×黒ベース・オレンジはCTA1点・写真そのまま（デュオトーン無し）・オレンジ地＋白文字CTA・抑制タイポ（ALL CAPS/コンデンスでない）・左端揃え・権威性前出し。マレルFBの改善4点が満たされているか確認。

- [ ] **Step 5: 回帰確認（既存パターン×既存モードが壊れていない）**

Run:
```bash
curl -s -X POST localhost:8750/api/generate -H 'Content-Type: application/json' \
 -d '{"pattern":"corporate","mode":"page","size":"191x1","prompt":"クラウド会計サービスのLP。信頼感。"}' \
 -o /tmp/dw-reg.json -w "HTTP %{http_code}\n"
node -e "const d=require('/tmp/dw-reg.json'); console.log('ok:', d.html && d.html.includes('<!DOCTYPE'))"
```
Expected: HTTP 200 / `ok: true`（既存 page モードが正常）

- [ ] **Step 6: サーバー停止**

Run: `pkill -f "node server.js"; echo stopped`

---

## Task 9: claude.ai Project へ両面反映

**Files:**
- Create: `docs/design-wheel/share/claude-project-v0/knowledge/fambox-SYSTEM.md`（コピー）
- Create: `docs/design-wheel/share/claude-project-v0/knowledge/PRINT-LAYOUT.md`（コピー）
- Modify: `docs/design-wheel/share/claude-project-v0/PROJECT-INSTRUCTIONS.md`
- Modify: `docs/design-wheel/share/claude-project-v0/KNOWLEDGE-MANIFEST.md`

- [ ] **Step 1: SYSTEM と PRINT-LAYOUT を knowledge にコピー**

Run:
```bash
cd /Users/archecoinc./Desktop/Claude_1
cp docs/design-wheel/patterns/fambox/SYSTEM.md docs/design-wheel/share/claude-project-v0/knowledge/fambox-SYSTEM.md
cp docs/design-wheel/foundations/PRINT-LAYOUT.md docs/design-wheel/share/claude-project-v0/knowledge/PRINT-LAYOUT.md
ls docs/design-wheel/share/claude-project-v0/knowledge/
```
Expected: `fambox-SYSTEM.md` と `PRINT-LAYOUT.md` が一覧に出る。

- [ ] **Step 2: PROJECT-INSTRUCTIONS.md のパターン早見表に fambox を追加**

「### 2. パターンを1つ推薦（選び方の早見表）」の表に行を追加:

```markdown
| FAM / FAM BOX の制作物（SNS・Web・チラシ） | **fambox** | ブランドの説得（3配色サブスタイル） |
```

さらに「## sporty を選んだ時だけ」の節の後に次の節を追加:

```markdown
## fambox（FAM）を選んだ時
- **FAM 絶対ルールを厳守**: 写真はカラーそのまま（デュオトーン/オーバーレイ禁止・提案しない）／オレンジ#FB4C15はCTA専用・オレンジ地＋白文字（暗背景×オレンジ文字は避ける）／Poppins＋Hiragino Sansの抑制タイポ（コンデンス/ALL CAPS多用しない）／権威性を前面・左端揃え。
- サブスタイル（配色）を先に決める:
  - **A SNS/Poster（既定）**: 黄#F5C842×黒#1A1A1A、banner/リール/投稿向け。
  - **B Web/DNA**: Drive Orange＋Sky/Deep Blue、page向け。
  - **C Print/Flyer**: 印刷DNA、flyer向け（A4）。Editorial/Manga/Corporate から選ぶ。
- flyer 時は A4固定（794×1123px・`@page{size:A4;margin:0}`・overflow:hidden）、`PRINT-LAYOUT.md` を使う。画像はグレーボックス。
- 締めに「実写真差し替え・文言確認・（入稿する場合は）Figma仕上げ」を仕上げ3チェックとして提示。
```

- [ ] **Step 3: KNOWLEDGE-MANIFEST.md に登録ファイルを追加**

「## まず登録する土台（全パターン共通・最優先）」の表に行を追加:

```markdown
| ①印刷 | `foundations/PRINT-LAYOUT.md` | チラシ（flyer）時の印刷レイアウト作法 |
```

「## v0 で登録するファイル（在庫4パターン＝Layer ②）」の表（パターン行）に追加:

```markdown
| fambox | `patterns/fambox/SYSTEM.md`（3サブスタイル・チラシ用） |
```

- [ ] **Step 4: コミット**

```bash
cd /Users/archecoinc./Desktop/Claude_1
git add docs/design-wheel/share/claude-project-v0/
git commit -m "feat(design-wheel): Project に fambox＋PRINT-LAYOUT 反映（チラシ対応）"
```

- [ ] **Step 5: 宮川さんへの反映依頼（人手）**

宮川さんに以下を伝える（claude.ai 側の手動作業）:
- Design Wheel Project の指示を `PROJECT-INSTRUCTIONS.md` 最新版で上書き
- ナレッジに `fambox-SYSTEM.md` と `PRINT-LAYOUT.md` を追加アップロード
- テスト: 「FAM BOX の梱包同梱チラシ（A4）を Editorial で作って」で判型・確定情報を確認

---

## Self-Review（記入済み）

- **Spec coverage:** ①新パターン=Task2,3 / ②flyerモード=Task4,7 / ③PRINT-LAYOUT=Task1,4 / ④A4+PDF=Task5,6 / ⑤両面反映=Task9 / ⑥棲み分け=Task2冒頭とPRINT-LAYOUT仕上げに明記。全項目にタスクあり。
- **Placeholder scan:** コード・ファイル内容は全て実体を記載。TODO/TBD なし。
- **Type consistency:** `exportPdf({html})`（Task5）↔ import と呼び出し（Task6）↔ フロント fetch `format:'pdf'`（Task7）で一致。SIZES key `'a4'`（Task5）↔ フロント `sizeSel.value='a4'`（Task7）↔ 検証（Task8）で一致。`state.mode==='flyer'`（Task7）↔ generate.js `mode==='flyer'`（Task4）で一致。
- **検証の現実性:** テスト基盤が無いため実機生成＋目視。API コスト（宮川さんの専用キー消費）を Task8 冒頭に注記。
