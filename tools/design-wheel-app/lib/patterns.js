import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
// tools/design-wheel-app/lib → リポジトリの patterns へ
export const PATTERNS_DIR = join(__dirname, '..', '..', '..', 'docs', 'design-wheel', 'patterns');

// 在庫パターン（README ステータス準拠）。一言定義は選び方UI用。
export const CATALOG = [
  { id: 'corporate', label: 'コーポレート', tagline: '余白の信頼', use: '士業・BtoB・きちんと感' },
  { id: 'digital',   label: 'デジタル',     tagline: '精度の説得', use: 'アプリ・SaaS・IoT・テック' },
  { id: 'gradient',  label: 'グラデーション', tagline: '感性の説得', use: 'ブランド・コスメ・食・やわらかさ' },
  { id: 'sporty',    label: 'スポーティ',   tagline: '運動量の説得', use: 'スポーツ・ジム・アプリUI（2系統）' },
  { id: 'fambox',    label: 'FAM / FAM BOX', tagline: 'ブランドの説得', use: 'FAM SNS・Web・チラシ（3配色）' },
  { id: 'ohbag',     label: 'ohbag',        tagline: '旅の相棒', use: 'ohbag 現地チラシ・名刺（AIトラベル）' },
];

export function listPatterns() {
  return CATALOG.map(p => ({ ...p, available: existsSync(join(PATTERNS_DIR, p.id, 'SYSTEM.md')) }));
}

export function readSystem(id) {
  const safe = CATALOG.find(p => p.id === id);
  if (!safe) throw new Error('unknown pattern: ' + id);
  const file = join(PATTERNS_DIR, id, 'SYSTEM.md');
  if (!existsSync(file)) throw new Error('SYSTEM.md not found for ' + id);
  return readFileSync(file, 'utf8');
}

// 追加の spec（あれば連結して文脈を厚くする）
export function readExtraSpecs(id) {
  const out = [];
  const bundleDirs = [
    join(PATTERNS_DIR, '..', 'ds-bundle', id),
    join(PATTERNS_DIR, '..', 'ds-bundle', 'sporty-product-ui'),
  ];
  for (const d of bundleDirs) {
    if (!existsSync(d)) continue;
    for (const f of readdirSync(d)) {
      if (f.endsWith('-spec.md') || f.endsWith('SYSTEM-spec.md')) {
        try { out.push(readFileSync(join(d, f), 'utf8')); } catch {}
      }
    }
  }
  return out.join('\n\n---\n\n');
}
