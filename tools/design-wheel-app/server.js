import 'dotenv/config';
import express from 'express';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { appendFileSync } from 'node:fs';
import { listPatterns } from './lib/patterns.js';
import { generateHtml, hasKey } from './lib/generate.js';
import { exportPng, exportPdf, SIZES } from './lib/export-png.js';

const __dirname = dirname(fileURLToPath(import.meta.url));
const app = express();
app.use(express.json({ limit: '4mb' }));
app.use(express.static(join(__dirname, 'public')));

const PORT = process.env.PORT || 8750;
const FEEDBACK_LOG = join(__dirname, 'feedback.jsonl');

app.get('/api/patterns', (req, res) => {
  res.json({ patterns: listPatterns(), sizes: SIZES, hasKey: hasKey() });
});

app.post('/api/generate', async (req, res) => {
  const { pattern, prompt, size, mode, previousHtml } = req.body || {};
  if (!pattern || !prompt) return res.status(400).json({ error: 'pattern と prompt は必須です' });
  try {
    const out = await generateHtml({ pattern, prompt, size, mode, previousHtml });
    res.json(out);
  } catch (e) {
    if (e.code === 'NO_API_KEY') {
      return res.status(503).json({ error: 'NO_API_KEY', message: 'ANTHROPIC_API_KEY が未設定です。.env に設定して再起動してください。' });
    }
    console.error(e);
    res.status(500).json({ error: 'generate_failed', message: String(e.message || e) });
  }
});

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

app.post('/api/feedback', (req, res) => {
  const entry = { ts: new Date().toISOString(), ...(req.body || {}) };
  try {
    appendFileSync(FEEDBACK_LOG, JSON.stringify(entry) + '\n', 'utf8');
    res.json({ ok: true });
  } catch (e) {
    res.status(500).json({ error: 'feedback_failed' });
  }
});

app.listen(PORT, () => {
  console.log(`Design Wheel app → http://localhost:${PORT}  (API key: ${hasKey() ? 'OK' : '未設定'})`);
});
