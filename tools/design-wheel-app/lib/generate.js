import Anthropic from '@anthropic-ai/sdk';
import { readSystem, readExtraSpecs, CATALOG } from './patterns.js';

const MODEL = process.env.DW_MODEL || 'claude-opus-4-8';

export function hasKey() {
  return Boolean(process.env.ANTHROPIC_API_KEY);
}

function buildSystemPrompt(patternId, sizeHint) {
  const meta = CATALOG.find(p => p.id === patternId);
  const system = readSystem(patternId);
  const extra = readExtraSpecs(patternId);
  return `あなたは「Design Wheel」のHTML生成エンジン。非デザイナーの指示から、指定パターンの設計書(SYSTEM)を厳守した完成度の高いHTMLを1ファイルで出力する。

# 出力するパターン: ${meta.label}（${meta.tagline}）

# 厳守する設計書（SYSTEM）
${system}

${extra ? `# 追加仕様（参考）\n${extra}` : ''}

# 出力ルール（必ず守る）
- SYSTEMの色・フォント・余白・コンポーネントの値を厳守する。値を創作しない。
- 1ファイル完結のHTML（<!DOCTYPE html>から</html>まで）。外部依存はGoogle Fontsのみ可。
- レスポンシブにする。${sizeHint ? `主な想定サイズ: ${sizeHint}。` : ''}
- パターンの語彙を混ぜない（例: sporty product-UIにgrain/斜め/グランジを足さない）。
- 写真が要る場合は images.unsplash.com の実URLを使う。
- 説明やコメントは出力せず、HTMLコードだけを返す（前後の地の文・\`\`\`は不要）。`;
}

export async function generateHtml({ pattern, prompt, size }) {
  if (!hasKey()) {
    const err = new Error('NO_API_KEY');
    err.code = 'NO_API_KEY';
    throw err;
  }
  const client = new Anthropic();
  const msg = await client.messages.create({
    model: MODEL,
    max_tokens: 8000,
    system: buildSystemPrompt(pattern, size),
    messages: [{ role: 'user', content: prompt }],
  });
  let text = (msg.content || []).filter(b => b.type === 'text').map(b => b.text).join('');
  // 念のため ```html フェンスを除去
  text = text.replace(/^\s*```(?:html)?\s*/i, '').replace(/```\s*$/i, '').trim();
  return { html: text, model: MODEL };
}
