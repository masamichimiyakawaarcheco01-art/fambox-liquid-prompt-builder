import { readFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import Anthropic from '@anthropic-ai/sdk';
import { readSystem, readExtraSpecs, CATALOG } from './patterns.js';
import { SIZES } from './export-png.js';

const MODEL = process.env.DW_MODEL || 'claude-opus-4-8';

// Layer ①（普遍の骨格）— 全パターン・全生成に共通注入
const __dir = dirname(fileURLToPath(import.meta.url));
let FOUNDATIONS = '';
try {
  FOUNDATIONS = readFileSync(
    join(__dir, '../../../docs/design-wheel/foundations/FOUNDATIONS.md'),
    'utf8'
  );
} catch { /* foundations が見つからなくても生成は継続 */ }

let PRINT_LAYOUT = '';
try {
  PRINT_LAYOUT = readFileSync(
    join(__dir, '../../../docs/design-wheel/foundations/PRINT-LAYOUT.md'),
    'utf8'
  );
} catch { /* 無くても継続 */ }

let CARD_LAYOUT = '';
try {
  CARD_LAYOUT = readFileSync(
    join(__dir, '../../../docs/design-wheel/foundations/CARD-LAYOUT.md'),
    'utf8'
  );
} catch { /* 無くても継続 */ }

export function hasKey() {
  return Boolean(process.env.ANTHROPIC_API_KEY);
}

function buildSystemPrompt(patternId, { size, mode } = {}) {
  const meta = CATALOG.find(p => p.id === patternId);
  const system = readSystem(patternId);
  const extra = readExtraSpecs(patternId);
  const s = SIZES[size];

  let form;
  if (mode === 'flyer') {
    form = `# 出力形態: チラシ（A4 縦・1枚）
- A4 縦1枚。<body>と最外要素を **794px × 1123px（A4比率）に固定**し、スクロール・改ページを作らない。
- CSS に \`@page{size:A4;margin:0}\` と \`html,body{margin:0;padding:0}\` を必ず入れる。
- 最外コンテナは \`width:794px;height:1123px;overflow:hidden;position:relative\`。
- 下の PRINT-LAYOUT（印刷の作法）を厳守する。`;
  } else if (mode === 'card') {
    form = `# 出力形態: 名刺カード（91×55mm 横・片面1枚）
- <body>と最外要素を **344px × 208px（91×55mm相当）に固定**し、スクロール・改ページを作らない。
- CSS に \`@page{size:91mm 55mm;margin:0}\` と \`html,body{margin:0;padding:0}\` を必ず入れる。
- 最外コンテナは \`width:344px;height:208px;overflow:hidden;position:relative\`。
- 下の CARD-LAYOUT（名刺の作法）を厳守する。`;
  } else if (mode === 'banner' && s) {
    form = `# 出力形態: バナー1枚（${s.label}）
- これは1枚のバナー。<body> と最外要素を**正確に ${s.w}px × ${s.h}px に固定**し、スクロールを生まない。
- 全要素をこの枠の中に収める（はみ出し・余白の出しすぎを避け、構図を枠に最適化する）。
- レスポンシブにしなくてよい。この固定サイズ専用の単一構図にする。`;
  } else {
    form = `# 出力形態: Webページ（レスポンシブ。縦に長くてよい）`;
  }

  return `あなたは「Design Wheel」のHTML生成エンジン。非デザイナーの指示から、指定パターンの設計書(SYSTEM)を厳守した完成度の高いHTMLを1ファイルで出力する。

# 出力するパターン: ${meta.label}（${meta.tagline}）

${form}

${FOUNDATIONS ? `# 普遍の骨格（FOUNDATIONS / Layer ①）— どのパターンでも必ず守る土台
${FOUNDATIONS}

> 上の FOUNDATIONS は土台。次の SYSTEM（色/フォント/世界観）と値が衝突したら **SYSTEM を優先**する。
` : ''}
${mode === 'flyer' && PRINT_LAYOUT ? `# 印刷レイアウトの作法（PRINT-LAYOUT）— flyer 専用
${PRINT_LAYOUT}
` : ''}
${mode === 'card' && CARD_LAYOUT ? `# 名刺レイアウトの作法（CARD-LAYOUT）— card 専用
${CARD_LAYOUT}
` : ''}
# 厳守する設計書（SYSTEM / Layer ②）
${system}

${extra ? `# 追加仕様（参考）\n${extra}` : ''}

# 出力ルール（必ず守る）
- SYSTEMの色・フォント・余白・コンポーネントの値を厳守する。値を創作しない。
- 1ファイル完結のHTML（<!DOCTYPE html>から</html>まで）。外部依存はGoogle Fontsのみ可。
- パターンの語彙を混ぜない（例: sporty product-UIにgrain/斜め/グランジを足さない）。
- 写真が要る場合は images.unsplash.com の実URLを使う。
- 説明やコメントは出力せず、HTMLコードだけを返す（前後の地の文・\`\`\`は不要）。`;
}

export async function generateHtml({ pattern, prompt, size, mode, previousHtml }) {
  if (!hasKey()) {
    const err = new Error('NO_API_KEY');
    err.code = 'NO_API_KEY';
    throw err;
  }
  const client = new Anthropic();

  let userContent;
  if (previousHtml) {
    // チャット改善: 前回HTMLを指示に従って修正
    userContent = `以下の「現在のHTML」を、次の修正指示どおりに直してください。HTML全体を返してください（一部だけでなく完全な1ファイル）。

# 修正指示
${prompt}

# 現在のHTML
${previousHtml}`;
  } else {
    userContent = prompt;
  }

  const msg = await client.messages.create({
    model: MODEL,
    max_tokens: 8000,
    system: buildSystemPrompt(pattern, { size, mode }),
    messages: [{ role: 'user', content: userContent }],
  });
  let text = (msg.content || []).filter(b => b.type === 'text').map(b => b.text).join('');
  text = text.replace(/^\s*```(?:html)?\s*/i, '').replace(/```\s*$/i, '').trim();
  return { html: text, model: MODEL };
}
