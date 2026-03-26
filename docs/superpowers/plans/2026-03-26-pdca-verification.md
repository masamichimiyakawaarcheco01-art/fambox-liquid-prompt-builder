# PDCA検証機能 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prompt Builder v2に検証パネルを統合し、Figmaデザインと生成コードの一致度をPDCAサイクルで検証・改善できるようにする。

**Architecture:** 単一HTML（index.html）を2カラム→3カラムに拡張。検証パネルに画像取り込み・コードプレビュー・チェックリスト・差分レポート・LLM連携を統合。localStorageでサイクル履歴管理。

**Tech Stack:** HTML / CSS / Vanilla JS / FileReader API / sandbox iframe / localStorage

**Spec:** `docs/superpowers/specs/2026-03-26-pdca-verification-design.md`

---

## 既存ヘルパー関数（v2で定義済み）

以下の関数はv2のindex.htmlに既に存在する。新規タスクで定義不要:
- `getVal(id)` - input要素の値をtrimして返す
- `showToast(msg)` - 画面下部にトースト通知を表示
- `getToggleValue(groupId)` - toggle-rowの選択値を返す
- `getActiveChips(containerId)` - チップの選択テキストを配列で返す
- `generatePrompt()` - プロンプト生成（末尾にgenerateChecklist()呼び出しを追加する）

## File Map

全て `index.html` 内で完結（単一ファイル制約）。変更は以下のセクション:

| セクション | 変更内容 |
|---|---|
| `<style>` | 3カラムレイアウト、検証パネルCSS、PDCAバーCSS追加 |
| `.app` グリッド | `1fr 1fr` → `3fr 3fr 4fr` に変更 |
| HTML: 検証パネル | 新規追加（画像ドロップ、コードエリア、チェックリスト、レポート） |
| HTML: PDCAバー | 新規追加（フッター固定） |
| `<script>` | Liquid置換、チェックリスト生成、差分レポート、LLMプロンプト、PDCA状態管理 |

---

### Task 1: レイアウトを3カラムに変更

**Files:**
- Modify: `index.html` (CSS: `.app` グリッド、レスポンシブ、パネルスタイル)

- [ ] **Step 1: CSSグリッドを3カラムに変更**

`.app` のgrid-template-columnsを `3fr 3fr 4fr` に変更。新しい `.panel--verify` スタイルを追加。レスポンシブブレイクポイントを3段階に:
```css
.app { grid-template-columns: 3fr 3fr 4fr; }
@media (max-width: 1440px) { .app { grid-template-columns: 1fr 1fr; } }
@media (max-width: 960px) { .app { grid-template-columns: 1fr; } }
```
パネルのmax-heightを `calc(100vh - 56px - 48px)` に変更（48px = PDCAバー）。

- [ ] **Step 2: 検証パネルのHTML骨格を追加**

`.panel--output` の後に空の `.panel--verify` を追加:
```html
<div class="panel panel--verify">
  <div class="output-header">
    <div class="output-header__title">Verify</div>
  </div>
  <!-- Task 2-6 で中身を追加 -->
</div>
```

- [ ] **Step 3: ブラウザで3カラム表示を確認**

index.htmlをブラウザで開き、3カラムが正しく表示されることを確認。1440px以下でプロンプト+入力の2カラムになり、960px以下で1カラムになることを確認。

- [ ] **Step 4: コミット**
```bash
git add index.html && git commit -m "feat: expand layout to 3 columns for verify panel"
```

---

### Task 2: Figma画像取り込み機能

**Files:**
- Modify: `index.html` (HTML: 検証パネル内、CSS: ドロップゾーン、JS: FileReader)

- [ ] **Step 1: ドロップゾーンHTML/CSSを追加**

検証パネル内にドロップゾーンを追加:
```html
<div class="verify-section">
  <div class="section-label">Design Image</div>
  <div class="image-tabs">
    <button class="image-tab active" onclick="switchImageTab('pc')">PC</button>
    <button class="image-tab" onclick="switchImageTab('sp')">SP</button>
  </div>
  <div class="drop-zone" id="dropZone">
    <div class="drop-zone__text">Figma画像をドロップ<br>またはクリック / Cmd+V</div>
    <input type="file" id="imageInput" accept="image/png,image/jpeg,image/webp" hidden>
  </div>
  <div class="design-preview-wrap" id="designPreviewWrap" hidden>
    <img class="design-preview" id="designPreview">
    <button class="design-preview__clear" onclick="clearDesignImage()" title="画像を削除">✕</button>
  </div>
</div>
```

CSS: `.drop-zone` に破線ボーダー、ドラッグオーバー時のハイライト、`.design-preview` にmax-width:100%。

- [ ] **Step 2: ドラッグ&ドロップ + クリック + ペースト JS**

```javascript
// ドラッグ&ドロップ
const dropZone = document.getElementById('dropZone');
dropZone.addEventListener('dragover', e => { e.preventDefault(); dropZone.classList.add('drag-over'); });
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('drag-over'));
dropZone.addEventListener('drop', e => { e.preventDefault(); dropZone.classList.remove('drag-over'); handleImageFile(e.dataTransfer.files[0]); });

// クリック
dropZone.addEventListener('click', () => document.getElementById('imageInput').click());
document.getElementById('imageInput').addEventListener('change', e => handleImageFile(e.target.files[0]));

// Cmd+V（テキスト入力欄にフォーカス中は無視）
document.addEventListener('paste', e => {
  if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT') return;
  const item = Array.from(e.clipboardData.items).find(i => i.type.startsWith('image/'));
  if (item) handleImageFile(item.getAsFile());
});

// 画像処理（5MB制限）
const designImages = { pc: null, sp: null };
let currentImageTab = 'pc';
function handleImageFile(file) {
  if (!file) return;
  if (!file.type.match(/^image\/(png|jpeg|webp)$/)) { showToast('PNG/JPEG/WebP画像のみ対応'); return; }
  if (file.size > 5 * 1024 * 1024) { showToast('5MB以下の画像を選択してください'); return; }
  const reader = new FileReader();
  reader.onload = e => {
    designImages[currentImageTab] = e.target.result;
    showDesignImage();
    updatePDCA();
  };
  reader.readAsDataURL(file);
}
function showDesignImage() {
  const img = document.getElementById('designPreview');
  const wrap = document.getElementById('designPreviewWrap');
  const src = designImages[currentImageTab];
  if (src) { img.src = src; wrap.hidden = false; dropZone.hidden = true; }
  else { wrap.hidden = true; dropZone.hidden = false; }
}
function clearDesignImage() {
  designImages[currentImageTab] = null;
  showDesignImage();
}
function switchImageTab(tab) {
  currentImageTab = tab;
  document.querySelectorAll('.image-tab').forEach(t => t.classList.toggle('active', t.textContent.toLowerCase() === tab));
  showDesignImage();
}
```

- [ ] **Step 3: 画像の表示確認**

ブラウザでFigmaスクリーンショットをドロップし、PC/SPタブ切替で表示されることを確認。5MB超のファイルでエラートーストが出ることを確認。

- [ ] **Step 4: コミット**
```bash
git add index.html && git commit -m "feat: add Figma image drop zone with PC/SP tabs"
```

---

### Task 3: コードプレビュー（iframe + Liquid置換）

**Files:**
- Modify: `index.html` (HTML: テキストエリア+iframe、JS: Liquid置換ロジック)

- [ ] **Step 1: コードエリアHTML追加**

検証パネルに:
```html
<div class="verify-section">
  <div class="section-label">Code Preview</div>
  <div class="preview-size-toggle">
    <button class="toggle-item active" onclick="setPreviewSize('pc')">PC (1200px)</button>
    <button class="toggle-item" onclick="setPreviewSize('sp')">SP (375px)</button>
  </div>
  <textarea class="field__textarea" id="codeInput" placeholder="生成されたコードを貼り付け" style="min-height:100px;font-family:monospace;font-size:11px"></textarea>
  <div class="preview-frame-wrap">
    <iframe id="previewFrame" sandbox="allow-scripts" class="preview-frame"></iframe>
  </div>
  <div class="preview-notice">外部リソース（フォント・画像URL）はsandbox内で読み込まれません</div>
</div>
```

- [ ] **Step 2: Liquid置換関数**

```javascript
function stripLiquid(code) {
  let c = code;
  // schema除去
  c = c.replace(/\{%-?\s*schema\s*-?%\}[\s\S]*?\{%-?\s*endschema\s*-?%\}/g, '');
  // liquid tag除去
  c = c.replace(/\{%-?\s*liquid[\s\S]*?-?%\}/g, '');
  // for → 中身3回
  c = c.replace(/\{%-?\s*for\s+\w+\s+in\s+[\w.]+\s*-?%\}([\s\S]*?)\{%-?\s*endfor\s*-?%\}/g, (_, inner) => inner.repeat(3));
  // if/unless → タグ除去、中身残す
  c = c.replace(/\{%-?\s*(?:if|unless|elsif|else|endif|endunless)\s*.*?-?%\}/g, '');
  // render/include
  c = c.replace(/\{%-?\s*(?:render|include)\s+'([^']+)'.*?-?%\}/g, '[partial: $1]');
  // asset_url
  c = c.replace(/\{\{\s*'[^']*'\s*\|\s*asset_url\s*\}\}/g, '#');
  // 残りの output tags
  c = c.replace(/\{\{\s*(?:section\.settings\.)?(\w+)[\w.]*\s*(?:\|[^}]*)?\}\}/g, '[$1]');
  // 残りの liquid tags
  c = c.replace(/\{%-?.*?-?%\}/g, '');
  return c;
}
```

- [ ] **Step 3: iframeプレビュー更新**

```javascript
function updatePreview() {
  const code = document.getElementById('codeInput').value;
  if (!code.trim()) return;
  const stripped = stripLiquid(code);
  const frame = document.getElementById('previewFrame');
  const doc = frame.contentDocument || frame.contentWindow.document;
  doc.open();
  doc.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>' + stripped + '</body></html>');
  doc.close();
  updatePDCA();
}

document.getElementById('codeInput').addEventListener('input', updatePreview);

function setPreviewSize(size) {
  const frame = document.getElementById('previewFrame');
  frame.style.width = size === 'pc' ? '1200px' : '375px';
  document.querySelectorAll('.preview-size-toggle .toggle-item').forEach(b => b.classList.toggle('active', b.textContent.includes(size.toUpperCase())));
}
```

- [ ] **Step 4: Liquidコードの貼り付けテスト**

既存のsections/fambox-faq.liquidの内容をコードエリアに貼り付け、Liquid構文が除去されiframe内にHTMLがレンダリングされることを確認。

- [ ] **Step 5: コミット**
```bash
git add index.html && git commit -m "feat: add code preview with Liquid stripping"
```

---

### Task 4: 自動チェックリスト生成

**Files:**
- Modify: `index.html` (HTML: チェックリストUI、JS: checklistRulesマッピング + 生成ロジック)

- [ ] **Step 1: チェックリストHTML追加**

```html
<div class="verify-section">
  <div class="section-label">Checklist <span class="check-count" id="checkCount">0/0</span></div>
  <div class="checklist" id="checklist">
    <div class="checklist__empty">入力フォームに値を設定するとチェック項目が生成されます</div>
  </div>
</div>
```

CSS:
```css
.checklist-item { display:flex; align-items:flex-start; gap:8px; padding:6px 0; border-bottom:1px solid var(--border); font-size:12px; }
.checklist-item input[type="checkbox"] { margin-top:2px; accent-color:var(--green); }
.checklist-item.checked label { color:var(--gray); text-decoration:line-through; }
.checklist-item .badge { font-size:9px; padding:1px 6px; border-radius:8px; background:var(--light); color:var(--gray); }
.checklist-item .badge--visual { background:#FFF3E0; color:#E65100; }
.check-count { font-size:11px; color:var(--gray); font-weight:400; }
```

- [ ] **Step 2: checklistRulesデータ + 生成関数**

設計書のchecklistRules配列をそのまま実装。さらに:

```javascript
function generateChecklist() {
  const container = document.getElementById('checklist');
  const items = [];

  checklistRules.forEach(rule => {
    let value = '', label = '';

    if (rule.field) {
      value = getVal(rule.field);
      if (!value) return;
      if (rule.skipDefault && value === rule.skipDefault) return;
      label = value;
    } else if (rule.toggle) {
      const active = document.querySelector(`#${rule.toggle} .toggle-item.active`);
      if (!active) return;
      value = active.dataset.value;
      label = active.textContent.trim();
    } else if (rule.select) {
      const sel = document.getElementById(rule.select);
      if (!sel || !sel.value) return;
      value = sel.value;
      label = sel.value;
    }

    const text = rule.template.replace('{value}', value).replace('{label}', label);
    items.push({ text, category: rule.category, type: rule.type || 'numeric', checked: false, id: `check-${items.length}` });
  });

  if (items.length === 0) {
    container.innerHTML = '<div class="checklist__empty">入力フォームに値を設定するとチェック項目が生成されます</div>';
    document.getElementById('checkCount').textContent = '0/0';
    return;
  }

  container.innerHTML = items.map(item => `
    <div class="checklist-item" data-id="${item.id}">
      <input type="checkbox" id="${item.id}" onchange="toggleCheck(this)">
      <label for="${item.id}">${item.text}</label>
      <span class="badge ${item.type === 'visual' ? 'badge--visual' : ''}">${item.type === 'visual' ? '目視' : '数値'}</span>
    </div>
  `).join('');

  updateCheckCount();
}

function toggleCheck(cb) {
  cb.closest('.checklist-item').classList.toggle('checked', cb.checked);
  updateCheckCount();
  updatePDCA();
}

function updateCheckCount() {
  const all = document.querySelectorAll('#checklist input[type="checkbox"]');
  const checked = document.querySelectorAll('#checklist input[type="checkbox"]:checked');
  document.getElementById('checkCount').textContent = `${checked.length}/${all.length}`;
}
```

- [ ] **Step 3: generatePromptの末尾でgenerateChecklist()を呼び出す**

既存のgeneratePrompt関数の最後に `generateChecklist();` を追加。フォーム入力が変わるたびにチェックリストも再生成される。

- [ ] **Step 4: チェックリスト動作確認**

テンプレート「Hero」を選択し、Color/Type/Spacingタブに値を入れた状態でチェックリストが自動生成されることを確認。チェックを入れるとカウントが更新されることを確認。

- [ ] **Step 5: コミット**
```bash
git add index.html && git commit -m "feat: add auto-generated checklist from form values"
```

---

### Task 5: 差分レポート + LLM連携プロンプト

**Files:**
- Modify: `index.html` (HTML: レポートUI + コピーボタン、JS: レポート生成 + LLMプロンプト組立)

- [ ] **Step 1: レポートUI HTML追加**

```html
<div class="verify-section">
  <div class="section-label">Diff Report</div>
  <div class="diff-report" id="diffReport">
    <div class="checklist__empty">チェックリストの未チェック項目から差分レポートを生成します</div>
  </div>
  <div class="btn-group" style="margin-top:12px">
    <button class="btn btn--secondary" onclick="copyForClaude()" title="修正指示">Claude</button>
    <button class="btn btn--ghost" onclick="copyForGemini()" title="デザイン比較">Gemini</button>
    <button class="btn btn--ghost" onclick="copyForChatGPT()" title="原因分析">ChatGPT</button>
  </div>
</div>
```

- [ ] **Step 2: 差分レポート生成関数**

```javascript
function generateDiffReport() {
  const unchecked = Array.from(document.querySelectorAll('#checklist input[type="checkbox"]:not(:checked)'))
    .map(cb => cb.nextElementSibling.textContent.trim());
  const container = document.getElementById('diffReport');

  if (unchecked.length === 0) {
    container.innerHTML = '<div style="color:var(--green);font-weight:600">全項目合格</div>';
    return unchecked;
  }

  container.innerHTML = '<div style="font-size:12px;line-height:1.8">' +
    unchecked.map(item => `<div style="color:#E53E3E">- ${item}</div>`).join('') +
    '</div>';
  return unchecked;
}
```

- [ ] **Step 3: LLMプロンプト生成関数3種**

設計書のテンプレートをそのまま実装。`collectFormData()`の結果 + コードエリア + 未チェック項目を組み合わせる:

```javascript
function getDesignSpec() {
  // 既存のgeneratePrompt()と同じ構造化出力を返す（プロンプト出力欄のテキスト）
  return document.getElementById('outputBox').textContent;
}

function copyForClaude() {
  const unchecked = generateDiffReport();
  if (unchecked.length === 0) { showToast('全項目合格です'); return; }
  const code = document.getElementById('codeInput').value;
  const prompt = `以下のコードを修正してください。\n\n## 現在のコード\n${code}\n\n## 修正が必要な項目\n${unchecked.map(i => '- ' + i).join('\n')}\n\n## デザイン仕様\n${getDesignSpec()}\n\n元のコードを直接編集し、修正済みコードを出力してください。`;
  navigator.clipboard.writeText(prompt).then(() => { enterActPhase(); showToast('Claude用プロンプトをコピー'); });
}

function copyForGemini() {
  const unchecked = generateDiffReport();
  const prompt = `以下のUIデザイン画像と実装コードのスクリーンショットを比較し、差異を列挙してください。\n\n## デザイン仕様\n${getDesignSpec()}\n\n## チェック観点\n1. カラーの一致\n2. フォントサイズ・ウェイトの一致\n3. 余白・スペーシングの一致\n4. レイアウト比率の一致\n5. 角丸・シャドウの一致\n6. 全体的な印象・世界観の一致\n\n差異ごとに「箇所」「期待値」「実際の値」「重要度(高/中/低)」を表形式で出力してください。\n\n※ Figmaデザイン画像とプレビューのスクリーンショットを添付してください。`;
  navigator.clipboard.writeText(prompt).then(() => { enterActPhase(); showToast('Gemini用プロンプトをコピー'); });
}

function copyForChatGPT() {
  const unchecked = generateDiffReport();
  if (unchecked.length === 0) { showToast('全項目合格です'); return; }
  const prompt = `UIの実装コードがデザイン仕様と一致しない原因を分析してください。\n\n## 不一致項目\n${unchecked.map(i => '- ' + i).join('\n')}\n\n## 使用したプロンプト\n${getDesignSpec()}\n\n以下を分析してください:\n1. プロンプトのどの記述が不十分だったか\n2. どう書き換えればLLMが正確に実装するか\n3. Prompt Builderの入力項目として何を追加すべきか\n\n改善案を具体的に提示してください。`;
  navigator.clipboard.writeText(prompt).then(() => { enterActPhase(); showToast('ChatGPT用プロンプトをコピー'); });
}
```

- [ ] **Step 4: レポート + コピー動作確認**

チェックリストの一部を未チェックにした状態で各ボタンをクリックし、クリップボードに正しいプロンプトがコピーされることを確認。

- [ ] **Step 5: コミット**
```bash
git add index.html && git commit -m "feat: add diff report and LLM prompt generation"
```

---

### Task 6: PDCAステータスバー + サイクル管理

**Files:**
- Modify: `index.html` (HTML: フッターバー、CSS: 固定配置、JS: 状態管理 + localStorage)

- [ ] **Step 1: PDCAバー HTML/CSS追加**

```html
<!-- .app の後、</body> の前に -->
<div class="pdca-bar" id="pdcaBar">
  <div class="pdca-steps">
    <span class="pdca-step active" data-phase="plan">Plan</span>
    <span class="pdca-connector">━━</span>
    <span class="pdca-step" data-phase="do">Do</span>
    <span class="pdca-connector">━━</span>
    <span class="pdca-step" data-phase="check">Check</span>
    <span class="pdca-connector">━━</span>
    <span class="pdca-step" data-phase="act">Act</span>
  </div>
  <div class="pdca-info">
    <span id="cycleCount">Cycle #1</span>
    <button class="btn btn--ghost" style="padding:4px 12px;font-size:11px" id="completeCycleBtn" onclick="completeCycle()" disabled>サイクル完了</button>
    <button class="btn btn--ghost" style="padding:4px 12px;font-size:11px" onclick="resetPDCA()">リセット</button>
  </div>
</div>
```

CSS:
```css
.pdca-bar {
  position:fixed; bottom:0; left:0; right:0; height:48px; background:var(--dark); color:#fff;
  display:flex; align-items:center; justify-content:space-between; padding:0 32px; z-index:100;
}
.pdca-steps { display:flex; align-items:center; gap:4px; }
.pdca-step { font-size:12px; font-weight:600; padding:4px 12px; border-radius:12px; opacity:0.4; }
.pdca-step.active { opacity:1; background:var(--orange); }
.pdca-step.done { opacity:1; color:var(--green); }
.pdca-connector { color:rgba(255,255,255,0.2); font-size:10px; }
.pdca-info { display:flex; align-items:center; gap:12px; font-size:12px; }
```

- [ ] **Step 2: PDCA状態管理JS**

```javascript
let pdcaState = JSON.parse(localStorage.getItem('pdca_history')) || {
  currentCycle: 1,
  phase: 'plan',
  cycles: []
};

function updatePDCA() {
  const hasPrompt = !document.getElementById('outputBox').textContent.includes('左のフォームに入力すると');
  const hasCode = (document.getElementById('codeInput')?.value || '').trim().length > 0;
  const allChecks = document.querySelectorAll('#checklist input[type="checkbox"]');
  const checkedCount = document.querySelectorAll('#checklist input[type="checkbox"]:checked').length;
  const allPassed = allChecks.length > 0 && checkedCount === allChecks.length;
  const hasUnchecked = allChecks.length > 0 && checkedCount < allChecks.length;

  // 状態遷移（前のフェーズの完了条件を満たした場合のみ次へ進む）
  // Plan: プロンプトが生成されたら完了 → Do へ
  if (pdcaState.phase === 'plan' && hasPrompt) {
    pdcaState.phase = 'do';
  }
  // Do: コードが貼り付けられたら完了 → Check へ
  if (pdcaState.phase === 'do' && hasCode) {
    pdcaState.phase = 'check';
  }
  // Check: 全チェック完了 → complete（Actスキップ）、未チェックあり → Act へ
  // ※ Act への遷移は generateDiffReport() 呼び出し時に行う
  if (pdcaState.phase === 'check' && allPassed) {
    pdcaState.phase = 'complete';
  }

  renderPDCA();
  savePDCA();
}

// Act フェーズへの遷移: LLMコピーボタン押下時に呼ばれる
function enterActPhase() {
  if (pdcaState.phase === 'check') {
    pdcaState.phase = 'act';
    renderPDCA();
    savePDCA();
  }
}

function renderPDCA() {
  const phases = ['plan', 'do', 'check', 'act'];
  const currentIdx = phases.indexOf(pdcaState.phase);
  document.querySelectorAll('.pdca-step').forEach(step => {
    const idx = phases.indexOf(step.dataset.phase);
    step.classList.remove('active', 'done');
    if (idx < currentIdx) step.classList.add('done');
    else if (idx === currentIdx) step.classList.add('active');
  });
  if (pdcaState.phase === 'complete') {
    document.querySelectorAll('.pdca-step').forEach(s => s.classList.add('done'));
  }
  document.getElementById('cycleCount').textContent = `Cycle #${pdcaState.currentCycle}`;

  // サイクル完了ボタンは act または complete フェーズのみ有効
  const completeBtn = document.getElementById('completeCycleBtn');
  if (completeBtn) {
    completeBtn.disabled = !['act', 'complete'].includes(pdcaState.phase);
    completeBtn.style.opacity = completeBtn.disabled ? '0.3' : '1';
  }
}

function completeCycle() {
  const unchecked = Array.from(document.querySelectorAll('#checklist input[type="checkbox"]:not(:checked)'))
    .map(cb => cb.nextElementSibling.textContent.trim());
  const all = document.querySelectorAll('#checklist input[type="checkbox"]');

  pdcaState.cycles.push({
    id: pdcaState.currentCycle,
    timestamp: new Date().toISOString(),
    phase: pdcaState.phase,
    totalChecks: all.length,
    passedChecks: all.length - unchecked.length,
    failedItems: unchecked,
    sectionName: getVal('sectionName')
  });

  pdcaState.currentCycle++;
  pdcaState.phase = 'plan';

  // チェックリストリセット
  document.querySelectorAll('#checklist input[type="checkbox"]').forEach(cb => { cb.checked = false; cb.closest('.checklist-item').classList.remove('checked'); });
  updateCheckCount();

  savePDCA();
  renderPDCA();
  showToast(`Cycle #${pdcaState.currentCycle - 1} 完了 → Cycle #${pdcaState.currentCycle} 開始`);
}

function resetPDCA() {
  pdcaState = { currentCycle: 1, phase: 'plan', cycles: [] };
  savePDCA();
  renderPDCA();
  showToast('PDCA履歴をリセットしました');
}

function savePDCA() {
  // 最新20サイクルのみ保持
  if (pdcaState.cycles.length > 20) pdcaState.cycles = pdcaState.cycles.slice(-20);
  localStorage.setItem('pdca_history', JSON.stringify(pdcaState));
}
```

- [ ] **Step 3: 初期化時にPDCA状態を復元**

scriptの末尾に:
```javascript
renderPDCA();
```

- [ ] **Step 4: PDCAバー動作確認**

Plan→Do→Check→Actの遷移をテスト。サイクル完了ボタンでカウントが増えることを確認。リロード後にlocalStorageから状態が復元されることを確認。

- [ ] **Step 5: コミット**
```bash
git add index.html && git commit -m "feat: add PDCA status bar with cycle management"
```

---

### Task 7: 中間幅レスポンシブ（ドロワー対応）

**Files:**
- Modify: `index.html` (CSS: 960-1440pxドロワー、JS: ドロワー開閉)

- [ ] **Step 1: 960-1440pxでの検証パネルドロワー化**

```css
@media (max-width: 1440px) and (min-width: 961px) {
  .app { grid-template-columns: 1fr 1fr; }
  .panel--verify {
    position: fixed; bottom: 48px; left: 0; right: 0; max-height: 50vh;
    transform: translateY(100%); transition: transform 0.3s;
    z-index: 50; border-top: 2px solid var(--orange); box-shadow: 0 -4px 20px rgba(0,0,0,0.15);
  }
  .panel--verify.drawer-open { transform: translateY(0); }
}
```

ドロワートグルボタン（PDCAバー内に追加）:
```html
<button class="btn btn--primary drawer-toggle" style="padding:4px 12px;font-size:11px" onclick="toggleDrawer()">検証パネル</button>
```

```javascript
function toggleDrawer() {
  document.querySelector('.panel--verify').classList.toggle('drawer-open');
}
```

- [ ] **Step 2: 動作確認**

ウィンドウ幅を1200px程度にして、ドロワーが正しく開閉すること、3カラム・1カラムへの遷移が滑らかなことを確認。

- [ ] **Step 3: コミット**
```bash
git add index.html && git commit -m "feat: add responsive drawer for verify panel at mid-width"
```

---

### Task 8: 最終統合 + ヘッダー/タイトル更新 + push

**Files:**
- Modify: `index.html` (タイトル更新、v3バッジ)
- Modify: `CLAUDE.md` (v3機能追加)

- [ ] **Step 1: タイトル・バッジ更新**

```html
<title>Liquid Prompt Builder v3 - PDCA Design Verification</title>
```
ヘッダーバッジを `v3` に。サブタイトルを `PDCA Design Verification System` に。

- [ ] **Step 2: CLAUDE.md に v3 機能を追記**

v3セクションを追加: PDCA検証機能の概要、3カラムレイアウト、LLM連携を記載。

- [ ] **Step 3: 全機能の統合テスト**

以下のフローを通して確認:
1. テンプレート「Hero」を選択 → プロンプト生成確認
2. 既存のfambox-hero-v17-video.liquidをコードエリアに貼り付け → プレビュー確認
3. Figma画像をドロップ → 表示確認
4. チェックリスト生成確認 → いくつかをチェック
5. 差分レポート生成 → 3種コピーボタン確認
6. PDCAバーの遷移確認
7. サイクル完了 → Cycle #2 に遷移確認

- [ ] **Step 4: コミット + push**
```bash
git add index.html CLAUDE.md && git commit -m "feat: Liquid Prompt Builder v3 - PDCA verification system

- 3カラムレイアウト（入力/プロンプト/検証）
- Figma画像ドラッグ&ドロップ（PC/SP切替）
- コードプレビュー（Liquid自動置換 + sandbox iframe）
- 自動チェックリスト（入力値から動的生成）
- 差分レポート + LLM連携プロンプト（Claude/Gemini/ChatGPT）
- PDCAステータスバー + サイクル管理

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>" && git push origin main
```
