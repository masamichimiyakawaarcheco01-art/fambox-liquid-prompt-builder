import { execFile } from 'node:child_process';
import { writeFileSync, readFileSync, mkdtempSync, rmSync } from 'node:fs';
import { join } from 'node:path';
import { tmpdir } from 'node:os';

const CHROME = process.env.DW_CHROME ||
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

// プラットフォーム別サイズ（4プラットフォーム=5アスペクト比）
export const SIZES = {
  '1x1':   { w: 1080, h: 1080, label: 'Instagram フィード (1:1)' },
  '4x5':   { w: 1080, h: 1350, label: 'IG 縦長 (4:5)' },
  '9x16':  { w: 1080, h: 1920, label: 'TikTok・ストーリー (9:16)' },
  '16x9':  { w: 1280, h: 720,  label: 'YouTube サムネ (16:9)' },
  '191x1': { w: 1200, h: 630,  label: 'Blog OGP・シェア (1.91:1)' },
  'a4':    { w: 794,  h: 1123, label: 'A4 チラシ（縦）' },
  'card':  { w: 344,  h: 208,  label: '名刺カード（91×55mm）' },
};

export function exportPng({ html, size, scale = 2 }) {
  const s = SIZES[size] || SIZES['1x1'];
  return new Promise((resolve, reject) => {
    const dir = mkdtempSync(join(tmpdir(), 'dw-export-'));
    const htmlFile = join(dir, 'page.html');
    const outFile = join(dir, 'out.png');
    writeFileSync(htmlFile, html, 'utf8');
    const args = [
      '--headless=new', '--disable-gpu', '--hide-scrollbars',
      `--force-device-scale-factor=${scale}`,
      `--window-size=${s.w},${s.h}`,
      '--default-background-color=00000000',
      '--virtual-time-budget=2500',
      `--screenshot=${outFile}`,
      'file://' + htmlFile,
    ];
    execFile(CHROME, args, { timeout: 20000 }, (err) => {
      try {
        if (err) return reject(err);
        const buf = readFileSync(outFile);
        resolve({ buffer: buf, w: s.w * scale, h: s.h * scale });
      } catch (e) {
        reject(e);
      } finally {
        try { rmSync(dir, { recursive: true, force: true }); } catch {}
      }
    });
  });
}

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
