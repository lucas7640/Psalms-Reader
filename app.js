/**
 * app.js – Psalms: Ancient Voices
 * Loads psalm data, renders stacked verse blocks with phonetics,
 * and handles audio playback via the Web Speech API.
 */

// ── State ──────────────────────────────────────────────────────────────────
let psalmsData   = [];
let currentPsalm = null;
let showHebrew   = true;
let showLatin    = true;
let showKJV      = true;
let showESV      = true;
let showRSV      = false;   // off by default to keep layout tidy
let speechQueue  = [];
let isSpeaking   = false;

// ── Boot ───────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', async () => {
  await loadData();
  buildSidebar();
  buildOverlay();          // populate the overlay grid
  const hash = parseInt(location.hash.replace('#psalm-', '')) || 1;
  renderPsalm(hash);
  setupScrollTop();
  setupOverlayKeyboard();  // Esc to close
});

// ── Data loading ───────────────────────────────────────────────────────────
async function loadData() {
  try {
    const resp = await fetch('data/psalms.json');
    if (!resp.ok) throw new Error('Network response was not ok');
    psalmsData = await resp.json();
  } catch (e) {
    console.error('Could not load psalms.json:', e);
    document.getElementById('verse-list').innerHTML =
      `<p class="loading-msg">⚠ Could not load psalm data. Make sure <code>data/psalms.json</code> exists.<br><br>
       Run <code>python generate_data.py</code> to generate it.</p>`;
  }
}

// ── Sidebar ────────────────────────────────────────────────────────────────
function buildSidebar() {
  const list = document.getElementById('psalm-list');
  list.innerHTML = '';
  psalmsData.forEach(p => {
    const li  = document.createElement('li');
    const a   = document.createElement('a');
    a.href    = `#psalm-${p.psalm}`;
    a.dataset.num = p.psalm;
    a.innerHTML   = `<span class="num">${p.psalm}</span> ${getPsalmName(p.psalm)}`;
    a.addEventListener('click', e => {
      e.preventDefault();
      renderPsalm(p.psalm);
      history.pushState(null, '', `#psalm-${p.psalm}`);
    });
    li.appendChild(a);
    list.appendChild(li);
  });
}

// Famous psalm short-names for the sidebar
const PSALM_NAMES = {
  1:'Beatus vir',2:'Quare fremuerunt',3:'Domine quid',4:'Cum invocarem',
  5:'Verba mea',6:'Domine ne',7:'Domine Deus',8:'Domine Dominus',
  9:'Confitebor',10:'Ut quid',11:'In Domino',12:'Salvum me fac',
  13:'Usquequo',14:'Dixit insipiens',15:'Domine quis',16:'Conserva me',
  17:'Exaudi',18:'Diligam te',19:'Caeli enarrant',20:'Exaudiat te',
  21:'Domine in virtute',22:'Deus Deus meus',23:'Dominus regit me',
  24:'Domini est terra',25:'Ad te Domine',26:'Dominus illuminatio',
  27:'Dominus illuminatio',28:'Ad te Domine',29:'Afferte Domino',
  30:'Exaltabo te',31:'In te Domine',32:'Beati quorum',33:'Exultate iusti',
  34:'Benedicam Dominum',35:'Iudica Domine',36:'Dixit iniustus',
  37:'Noli aemulari',38:'Domine ne in furore',39:'Dixi custodiam',
  40:'Expectans expectavi',41:'Beatus qui',42:'Quemadmodum',43:'Iudica me',
  44:'Deus auribus',45:'Eructavit',46:'Deus noster',47:'Omnes gentes',
  48:'Magnus Dominus',49:'Audite haec',50:'Deus deorum',51:'Miserere',
  52:'Quid gloriaris',53:'Dixit insipiens',54:'Deus in nomine',
  55:'Exaudi Deus',56:'Miserere mei',57:'Miserere mei',58:'Si vere',
  59:'Eripe me',60:'Deus reppulisti',61:'Exaudi Deus',62:'Nonne Deo',
  63:'Deus Deus meus',64:'Exaudi Deus',65:'Te decet',66:'Iubilate Deo',
  67:'Deus misereatur',68:'Exsurgat Deus',69:'Salvum me fac',70:'Deus in adiutorium',
  71:'In te Domine',72:'Deus iudicium',73:'Quam bonus',74:'Ut quid Deus',
  75:'Confitebimur',76:'Notus in Iudaea',77:'Voce mea',78:'Attendite',
  79:'Deus venerunt',80:'Qui regis',81:'Exultate Deo',82:'Deus stetit',
  83:'Deus quis similis',84:'Quam dilecta',85:'Benedixisti',86:'Inclina Domine',
  87:'Fundamenta eius',88:'Domine Deus',89:'Misericordias',90:'Domine refugium',
  91:'Qui habitat',92:'Bonum est',93:'Dominus regnavit',94:'Deus ultionum',
  95:'Venite exultemus',96:'Cantate Domino',97:'Dominus regnavit',
  98:'Cantate Domino',99:'Dominus regnavit',100:'Iubilate Deo',
  101:'Misericordiam',102:'Domine exaudi',103:'Benedic anima mea',
  104:'Benedic anima mea',105:'Confitemini Domino',106:'Confitemini Domino',
  107:'Confitemini Domino',108:'Paratum cor',109:'Deus laudem',110:'Dixit Dominus',
  111:'Confitebor Domino',112:'Beatus vir',113:'Laudate pueri',114:'In exitu',
  115:'Non nobis',116:'Dilexi',117:'Laudate Dominum',118:'Confitemini Domino',
  119:'Beati immaculati',120:'Ad Dominum',121:'Levavi oculos',122:'Laetatus sum',
  123:'Ad te levavi',124:'Nisi quia',125:'Qui confidunt',126:'In convertendo',
  127:'Nisi Dominus',128:'Beati omnes',129:'Saepe expugnaverunt',130:'De profundis',
  131:'Domine non est',132:'Memento Domine',133:'Ecce quam bonum',134:'Ecce nunc',
  135:'Laudate nomen',136:'Confitemini Domino',137:'Super flumina',138:'Confitebor tibi',
  139:'Domine probasti',140:'Eripe me Domine',141:'Domine clamavi',142:'Voce mea',
  143:'Domine exaudi',144:'Benedictus Dominus',145:'Exaltabo te Deus',
  146:'Lauda anima mea',147:'Laudate Dominum',148:'Laudate Dominum',
  149:'Cantate Domino',150:'Laudate Dominum',
};

function getPsalmName(num) {
  return PSALM_NAMES[num] || `Psalm ${num}`;
}

// ── Render a psalm ─────────────────────────────────────────────────────────
function renderPsalm(num) {
  stopSpeaking();
  const psalm = psalmsData.find(p => p.psalm === num);
  currentPsalm = psalm || null;

  // Update sidebar active state
  document.querySelectorAll('#psalm-list a').forEach(a => {
    a.classList.toggle('active', parseInt(a.dataset.num) === num);
  });

  // Scroll sidebar item into view
  const activeLink = document.querySelector(`#psalm-list a[data-num="${num}"]`);
  if (activeLink) activeLink.scrollIntoView({ block: 'nearest', behavior: 'smooth' });

  const header    = document.getElementById('psalm-header');
  const verseList = document.getElementById('verse-list');

  if (!psalm) {
    header.innerHTML    = `<h2>Psalm ${num}</h2>`;
    verseList.innerHTML = `<p class="loading-msg">No data available for Psalm ${num}.</p>`;
    return;
  }

  header.innerHTML = `
    <h2>Psalm ${num} &mdash; ${getPsalmName(num)}</h2>
    <p class="psalm-tagline">${psalm.superscript || ''}</p>
  `;

  verseList.innerHTML = '';
  psalm.verses.forEach(v => {
    verseList.appendChild(buildVerseBlock(v, num));
  });

  updateNavButtons(num);
  updateOverlayCurrent(num);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ── Build a verse block ────────────────────────────────────────────────────
function buildVerseBlock(verse, psalmNum) {
  const block = document.createElement('div');
  block.className = 'verse-block';
  block.dataset.verse = verse.verse;

  // Top bar with verse number + play button
  const bar = document.createElement('div');
  bar.className = 'verse-num-bar';
  bar.innerHTML = `
    <span class="v-num">v. ${verse.verse}</span>
    <div style="display:flex;gap:0.5rem;align-items:center">
      <button class="play-verse-btn" title="Hear Hebrew" onclick="speakVerse(${psalmNum},${verse.verse},'he')">🔊 Heb</button>
      <button class="play-verse-btn" title="Hear Latin"  onclick="speakVerse(${psalmNum},${verse.verse},'la')">🔊 Lat</button>
    </div>
  `;
  block.appendChild(bar);

  // Hebrew panel
  if (verse.hebrew) {
    const hePanel = buildLangPanel('hebrew-panel', 'heb', 'Hebrew (Masoretic)', verse.hebrew, phoneticizeHebrew(verse.hebrew));
    hePanel.classList.toggle('hidden', !showHebrew);
    block.appendChild(hePanel);
  }

  // Latin panel
  if (verse.latin) {
    const latPanel = buildLangPanel('latin-panel', 'lat', 'Latin (Vulgate)', verse.latin, phoneticizeLatin(verse.latin));
    latPanel.classList.toggle('hidden', !showLatin);
    block.appendChild(latPanel);
  }

  // KJV panel
  if (verse.kjv) {
    const kjvPanel = buildLangPanel('kjv-panel', 'kjv', 'English — KJV (1611)', verse.kjv, null);
    kjvPanel.classList.toggle('hidden', !showKJV);
    block.appendChild(kjvPanel);
  }

  // ESV panel
  if (verse.esv) {
    const esvPanel = buildLangPanel('esv-panel', 'esv', 'English — ESV (2001)', verse.esv, null);
    esvPanel.classList.toggle('hidden', !showESV);
    block.appendChild(esvPanel);
  }

  // RSV panel
  if (verse.rsv) {
    const rsvPanel = buildLangPanel('rsv-panel', 'rsv', 'English — RSV (1952)', verse.rsv, null);
    rsvPanel.classList.toggle('hidden', !showRSV);
    block.appendChild(rsvPanel);
  }

  return block;
}

function buildLangPanel(panelClass, dotClass, label, originalText, phonetic) {
  const panel = document.createElement('div');
  panel.className = `lang-panel ${panelClass}`;
  panel.innerHTML = `
    <div class="lang-label">
      <span class="lang-dot ${dotClass}"></span>${label}
    </div>
    <div class="original-text">${escapeHtml(originalText)}</div>
    ${phonetic ? `<div class="phonetic-line">${formatPhonetic(phonetic)}</div>` : ''}
  `;
  return panel;
}

// ── Phonetics ──────────────────────────────────────────────────────────────

/**
 * Convert a Hebrew verse string to a phonetic display string.
 * Uses the transliterate.js engine if loaded, else falls back to basic rules.
 */
function phoneticizeHebrew(text) {
  if (!text) return '';
  // Use transliterate.js if available (loaded via <script>)
  if (typeof transliterateHebrewVerse === 'function') {
    return transliterateHebrewVerse(text)
      .map(w => w.display)
      .join('  ');
  }
  return '[phonetics require transliterate.js]';
}

function phoneticizeLatin(text) {
  if (!text) return '';
  if (typeof transliterateLatinVerse === 'function') {
    return transliterateLatinVerse(text)
      .map(w => w.display)
      .join('  ');
  }
  return '[phonetics require transliterate.js]';
}

/**
 * Mark up stress markers (ˈ) and syllable breaks (·) in the HTML.
 */
function formatPhonetic(ph) {
  if (!ph) return '';
  return escapeHtml(ph)
    .replace(/ˈ/g,  '<span class="phonetic-stress">ˈ</span>')
    .replace(/·/g,  '<span class="phonetic-break">·</span>');
}

// ── Language toggles ───────────────────────────────────────────────────────
function toggleLang(lang) {
  const map = {
    he:  { state: () => showHebrew  = !showHebrew,  val: () => showHebrew,  cls: 'hebrew-panel',  btn: 'btn-he'  },
    la:  { state: () => showLatin   = !showLatin,   val: () => showLatin,   cls: 'latin-panel',   btn: 'btn-la'  },
    kjv: { state: () => showKJV     = !showKJV,     val: () => showKJV,     cls: 'kjv-panel',     btn: 'btn-kjv' },
    esv: { state: () => showESV     = !showESV,     val: () => showESV,     cls: 'esv-panel',     btn: 'btn-esv' },
    rsv: { state: () => showRSV     = !showRSV,     val: () => showRSV,     cls: 'rsv-panel',     btn: 'btn-rsv' },
  };
  const entry = map[lang];
  if (!entry) return;
  entry.state();
  const visible = entry.val();
  document.querySelectorAll(`.${entry.cls}`).forEach(p => p.classList.toggle('hidden', !visible));
  document.getElementById(entry.btn)?.classList.toggle('active', visible);
}

// ── Audio / Speech ─────────────────────────────────────────────────────────
function speakVerse(psalmNum, verseNum, lang) {
  const psalm = psalmsData.find(p => p.psalm === psalmNum);
  const verse = psalm?.verses.find(v => v.verse === verseNum);
  if (!verse) return;

  const text    = lang === 'he' ? verse.hebrew : verse.latin;
  const voiceLang = lang === 'he' ? 'he-IL' : 'it-IT'; // Hebrew / Ecclesiastical (Italian proxy)
  if (!text) return;

  stopSpeaking();
  const utt     = new SpeechSynthesisUtterance(text);
  utt.lang      = voiceLang;
  utt.rate      = 0.78;
  utt.pitch     = 1.0;

  const block = document.querySelector(`.verse-block[data-verse="${verseNum}"]`);
  if (block) block.classList.add('speaking');
  utt.onend = () => { if (block) block.classList.remove('speaking'); isSpeaking = false; };

  isSpeaking = true;
  speechSynthesis.speak(utt);
}

function speakAllVerses(lang) {
  if (!currentPsalm) return;
  stopSpeaking();
  const verses = currentPsalm.verses;
  let idx = 0;

  function next() {
    if (idx >= verses.length) { isSpeaking = false; return; }
    const v = verses[idx++];
    const text = lang === 'he' ? v.hebrew : v.latin;
    if (!text) { next(); return; }

    const utt     = new SpeechSynthesisUtterance(text);
    utt.lang      = lang === 'he' ? 'he-IL' : 'it-IT';
    utt.rate      = 0.78;
    const block   = document.querySelector(`.verse-block[data-verse="${v.verse}"]`);
    document.querySelectorAll('.verse-block').forEach(b => b.classList.remove('speaking'));
    if (block) { block.classList.add('speaking'); block.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }
    utt.onend = next;
    speechSynthesis.speak(utt);
  }
  isSpeaking = true;
  next();
}

function stopSpeaking() {
  speechSynthesis.cancel();
  isSpeaking = false;
  document.querySelectorAll('.verse-block').forEach(b => b.classList.remove('speaking'));
}

// ── Navigation ─────────────────────────────────────────────────────────────
function updateNavButtons(num) {
  const prev = document.getElementById('nav-prev');
  const next = document.getElementById('nav-next');
  if (!prev || !next) return;
  prev.disabled = num <= 1;
  next.disabled = num >= 150;
  prev.onclick  = () => { if (num > 1)   renderPsalm(num - 1); };
  next.onclick  = () => { if (num < 150) renderPsalm(num + 1); };
}

// ── Scroll to top button ───────────────────────────────────────────────────
function setupScrollTop() {
  const btn = document.getElementById('back-top');
  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 400);
  });
  btn.onclick = () => window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ── Utilities ──────────────────────────────────────────────────────────────
function escapeHtml(str) {
  return (str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ══════════════════════════════════════════════════════════════════════════════
// PSALM SELECTION OVERLAY
// ══════════════════════════════════════════════════════════════════════════════

/**
 * The five traditional Books of Psalms.
 * Each psalm number falls into exactly one book.
 */
const PSALM_BOOKS = [
  { label: 'Book I',   roman: 'I',   range: [1,   41]  },
  { label: 'Book II',  roman: 'II',  range: [42,  72]  },
  { label: 'Book III', roman: 'III', range: [73,  89]  },
  { label: 'Book IV',  roman: 'IV',  range: [90,  106] },
  { label: 'Book V',   roman: 'V',   range: [107, 150] },
];

/**
 * Short Latin incipits for every psalm (first 1–2 words, for the cell label).
 * Drawn from the Clementine Vulgate tradition.
 */
const INCIPITS = {
  1:'Beatus vir',2:'Quare fremuerunt',3:'Domine quid',4:'Cum invocarem',
  5:'Verba mea',6:'Domine ne',7:'Domine Deus',8:'Domine Dominus',
  9:'Confitebor tibi',10:'Ut quid Domine',11:'In Domino',12:'Salvum me fac',
  13:'Usquequo',14:'Dixit insipiens',15:'Domine quis',16:'Conserva me',
  17:'Exaudi Domine',18:'Diligam te',19:'Caeli enarrant',20:'Exaudiat te',
  21:'Domine in virtute',22:'Deus Deus meus',23:'Dominus regit',24:'Domini est',
  25:'Ad te Domine',26:'Dominus illuminatio',27:'Dominus illuminatio',28:'Ad te Domine',
  29:'Afferte Domino',30:'Exaltabo te',31:'In te Domine',32:'Beati quorum',
  33:'Exultate iusti',34:'Benedicam Dominum',35:'Iudica Domine',36:'Dixit iniustus',
  37:'Noli aemulari',38:'Domine ne',39:'Dixi custodiam',40:'Expectans expectavi',
  41:'Beatus qui intelligit',42:'Quemadmodum',43:'Iudica me Deus',44:'Deus auribus',
  45:'Eructavit cor',46:'Deus noster',47:'Omnes gentes',48:'Magnus Dominus',
  49:'Audite haec',50:'Deus deorum',51:'Miserere mei',52:'Quid gloriaris',
  53:'Dixit insipiens',54:'Deus in nomine',55:'Exaudi Deus',56:'Miserere mei Deus',
  57:'Miserere mei',58:'Si vere utique',59:'Eripe me',60:'Deus reppulisti',
  61:'Exaudi Deus',62:'Nonne Deo',63:'Deus Deus meus',64:'Exaudi Deus vocem',
  65:'Te decet hymnus',66:'Iubilate Deo',67:'Deus misereatur',68:'Exsurgat Deus',
  69:'Salvum me fac',70:'Deus in adiutorium',71:'In te Domine',72:'Deus iudicium',
  73:'Quam bonus Israel',74:'Ut quid Deus',75:'Confitebimur',76:'Notus in Iudaea',
  77:'Voce mea ad Deum',78:'Attendite popule',79:'Deus venerunt',80:'Qui regis Israel',
  81:'Exultate Deo',82:'Deus stetit',83:'Deus quis similis',84:'Quam dilecta',
  85:'Benedixisti Domine',86:'Inclina Domine',87:'Fundamenta eius',88:'Domine Deus salutis',
  89:'Misericordias Domini',90:'Domine refugium',91:'Qui habitat',92:'Bonum est confiteri',
  93:'Dominus regnavit',94:'Deus ultionum',95:'Venite exultemus',96:'Cantate Domino',
  97:'Dominus regnavit',98:'Cantate Domino',99:'Dominus regnavit',100:'Iubilate Deo',
  101:'Misericordiam',102:'Domine exaudi',103:'Benedic anima',104:'Benedic anima mea',
  105:'Confitemini Domino',106:'Confitemini Domino',107:'Confitemini Domino',
  108:'Paratum cor meum',109:'Deus laudem meam',110:'Dixit Dominus',
  111:'Confitebor Domino',112:'Beatus vir',113:'Laudate pueri',114:'In exitu Israel',
  115:'Non nobis Domine',116:'Dilexi quoniam',117:'Laudate Dominum',
  118:'Confitemini Domino',119:'Beati immaculati',120:'Ad Dominum',
  121:'Levavi oculos',122:'Laetatus sum',123:'Ad te levavi',124:'Nisi quia',
  125:'Qui confidunt',126:'In convertendo',127:'Nisi Dominus',128:'Beati omnes',
  129:'Saepe expugnaverunt',130:'De profundis',131:'Domine non est',132:'Memento Domine',
  133:'Ecce quam bonum',134:'Ecce nunc',135:'Laudate nomen',136:'Confitemini Domino',
  137:'Super flumina',138:'Confitebor tibi',139:'Domine probasti',140:'Eripe me Domine',
  141:'Domine clamavi',142:'Voce mea ad Dominum',143:'Domine exaudi',
  144:'Benedictus Dominus',145:'Exaltabo te Deus',146:'Lauda anima mea',
  147:'Laudate Dominum',148:'Laudate Dominum',149:'Cantate Domino',150:'Laudate Dominum',
};

/**
 * Build the overlay grid content.
 * Called once after data loads; cells reflect actual psalms available in psalmsData.
 */
function buildOverlay() {
  const body = document.getElementById('overlay-body');
  if (!body) return;
  body.innerHTML = '';

  // Build a set of psalm numbers we have data for
  const available = new Set(psalmsData.map(p => p.psalm));

  PSALM_BOOKS.forEach(book => {
    const section = document.createElement('div');
    section.className = 'psalm-book';

    // Book heading
    const heading = document.createElement('div');
    heading.className = 'book-heading';
    heading.innerHTML = `
      <span class="book-roman">${book.roman}</span>
      <span class="book-label">${book.label} &nbsp;·&nbsp; Psalms ${book.range[0]}–${book.range[1]}</span>
    `;
    section.appendChild(heading);

    // Grid of numbers
    const grid = document.createElement('div');
    grid.className = 'psalm-number-grid';

    for (let n = book.range[0]; n <= book.range[1]; n++) {
      const cell = document.createElement('a');
      cell.className = 'psalm-cell';
      cell.href = `#psalm-${n}`;
      cell.dataset.psalmNum = n;
      cell.title = INCIPITS[n] || `Psalm ${n}`;

      if (!available.has(n)) {
        cell.style.opacity = '0.45';
        cell.style.cursor  = 'default';
        cell.title += ' (not yet loaded — run generate_data.py)';
      }

      cell.innerHTML = `
        <span class="cell-num">${n}</span>
        <span class="cell-name">${(INCIPITS[n] || '').split(' ').slice(0,2).join(' ')}</span>
      `;

      cell.addEventListener('click', e => {
        e.preventDefault();
        if (available.has(n)) {
          renderPsalm(n);
          history.pushState(null, '', `#psalm-${n}`);
        }
        closeOverlay();
      });

      grid.appendChild(cell);
    }

    section.appendChild(grid);
    body.appendChild(section);
  });
}

/**
 * Sync the "current" highlight on every psalm cell whenever a psalm is rendered.
 */
function updateOverlayCurrent(num) {
  document.querySelectorAll('.psalm-cell').forEach(cell => {
    cell.classList.toggle('current', parseInt(cell.dataset.psalmNum) === num);
  });
}

/** Open the overlay. */
function openOverlay() {
  document.getElementById('overlay-backdrop').classList.add('open');
  document.getElementById('overlay-panel').classList.add('open');
  document.body.style.overflow = 'hidden'; // prevent background scroll

  // Scroll the current psalm cell into view inside the overlay
  requestAnimationFrame(() => {
    const active = document.querySelector('.psalm-cell.current');
    if (active) active.scrollIntoView({ block: 'center', behavior: 'smooth' });
  });
}

/** Close the overlay. */
function closeOverlay() {
  document.getElementById('overlay-backdrop').classList.remove('open');
  document.getElementById('overlay-panel').classList.remove('open');
  document.body.style.overflow = '';
}

/** Close on Escape key. */
function setupOverlayKeyboard() {
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeOverlay();
  });
}
