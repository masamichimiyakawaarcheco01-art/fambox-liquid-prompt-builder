import Anthropic from '@anthropic-ai/sdk';
import { readSystem, readExtraSpecs, CATALOG } from './patterns.js';
import { SIZES } from './export-png.js';

const MODEL = process.env.DW_MODEL || 'claude-opus-4-8';

export function hasKey() {
  return Boolean(process.env.ANTHROPIC_API_KEY);
}

function buildSystemPrompt(patternId, { size, mode } = {}) {
  const meta = CATALOG.find(p => p.id === patternId);
  const system = readSystem(patternId);
  const extra = readExtraSpecs(patternId);
  const s = SIZES[size];

  let form;
  if (mode === 'banner' && s) {
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

# 厳守する設計書（SYSTEM）
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
