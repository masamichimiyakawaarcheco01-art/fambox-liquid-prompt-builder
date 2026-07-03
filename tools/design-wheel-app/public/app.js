const $ = s => document.querySelector(s);
let state = { pattern: null, rating: 0, lastHtml: null, mode: 'page' };

// 形態トグル
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

async function init() {
  const r = await fetch('/api/patterns').then(r => r.json());
  // key tag
  const kt = $('#keytag');
  kt.textContent = r.hasKey ? 'API: 接続OK' : 'API: 未設定';
  kt.classList.toggle('ok', r.hasKey);
  $('#keyhint').style.display = r.hasKey ? 'none' : 'block';

  // patterns
  const wrap = $('#patterns'); wrap.innerHTML = '';
  for (const p of r.patterns) {
    const el = document.createElement('div');
    el.className = 'pat' + (p.available ? '' : ' off');
    el.innerHTML = `<div class="nm">${p.label}</div><div class="tg">${p.tagline}</div>`;
    if (p.available) el.onclick = () => selectPattern(p.id, el);
    wrap.appendChild(el);
  }
  // sizes
  const sel = $('#size'); sel.innerHTML = '';
  for (const [k, v] of Object.entries(r.sizes)) {
    const o = document.createElement('option'); o.value = k; o.textContent = v.label; sel.appendChild(o);
  }
}

function selectPattern(id, el) {
  state.pattern = id;
  document.querySelectorAll('.pat').forEach(x => x.classList.remove('on'));
  el.classList.add('on');
}

$('#gen').onclick = async () => {
  const prompt = $('#prompt').value.trim();
  if (!state.pattern) return alert('パターンを選んでください');
  if (!prompt) return alert('作りたいものを入力してください');
  const btn = $('#gen'); const orig = btn.textContent;
  btn.disabled = true; btn.innerHTML = '<span class="spin"></span>生成中…';
  try {
    const res = await fetch('/api/generate', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pattern: state.pattern, prompt, size: $('#size').value, mode: state.mode }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.message || data.error);
    showHtml(data.html);
  } catch (e) {
    alert('生成に失敗: ' + e.message);
  } finally {
    btn.disabled = false; btn.textContent = orig;
  }
};

function showHtml(html) {
  state.lastHtml = html;
  $('#empty').style.display = 'none';
  const f = $('#frame'); f.style.display = 'block'; f.srcdoc = html;
  $('#export').disabled = false;
  if (state.mode === 'flyer') $('#exportPdf').disabled = false;
  $('#chatbar').style.display = 'flex';
}

// チャット改善: 前回HTMLを引き継いで修正
$('#reviseBtn').onclick = async () => {
  const instr = $('#revise').value.trim();
  if (!instr) return;
  if (!state.lastHtml) return alert('先に叩き台を生成してください');
  const btn = $('#reviseBtn'); const orig = btn.textContent;
  btn.disabled = true; btn.innerHTML = '<span class="spin"></span>修正中…';
  try {
    const res = await fetch('/api/generate', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        pattern: state.pattern, prompt: instr, size: $('#size').value,
        mode: state.mode, previousHtml: state.lastHtml,
      }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.message || data.error);
    showHtml(data.html);
    $('#revise').value = '';
  } catch (e) {
    alert('修正に失敗: ' + e.message);
  } finally {
    btn.disabled = false; btn.textContent = orig;
  }
};

$('#export').onclick = async () => {
  if (!state.lastHtml) return;
  const btn = $('#export'); btn.disabled = true; const orig = btn.textContent; btn.innerHTML = '<span class="spin"></span>書き出し中…';
  try {
    const res = await fetch('/api/export', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ html: state.lastHtml, size: $('#size').value }),
    });
    if (!res.ok) { const d = await res.json(); throw new Error(d.message || d.error); }
    const blob = await res.blob();
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `design-wheel-${state.pattern}-${$('#size').value}@2x.png`;
    a.click(); URL.revokeObjectURL(a.href);
  } catch (e) {
    alert('書き出し失敗: ' + e.message);
  } finally {
    btn.disabled = false; btn.textContent = orig;
  }
};

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

// stars
document.querySelectorAll('#stars span').forEach(s => {
  s.onclick = () => {
    state.rating = +s.dataset.v;
    document.querySelectorAll('#stars span').forEach(x => x.classList.toggle('on', +x.dataset.v <= state.rating));
  };
});

$('#sendfb').onclick = async () => {
  if (!state.pattern && !state.rating && !$('#hard').value) return;
  await fetch('/api/feedback', {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      pattern: state.pattern, rating: state.rating,
      hard: $('#hard').value, prompt: $('#prompt').value, size: $('#size').value,
    }),
  });
  $('#hard').value = ''; state.rating = 0;
  document.querySelectorAll('#stars span').forEach(x => x.classList.remove('on'));
  const b = $('#sendfb'); b.textContent = '記録した ✓'; setTimeout(() => b.textContent = '記録', 1500);
};

init();
