/**
 * transliterate.js
 * Phonetic transliteration engines for Biblical Hebrew and Ecclesiastical Latin.
 * Produces simplified English-letter phonetics with syllable breaks (·) and stress marks (ˈ).
 */

// ─── HEBREW ──────────────────────────────────────────────────────────────────

/**
 * Map of Hebrew Unicode characters (consonants + nikkud vowels) to their
 * phonetic equivalents using an intuitive English-letter system.
 */
const HEBREW_CONSONANTS = {
  'א': '',      // aleph – silent / glottal (omitted in phonetics unless word-initial)
  'בּ': 'b',   // bet with dagesh
  'ב': 'v',    // vet
  'גּ': 'g',   // gimel with dagesh
  'ג': 'g',
  'דּ': 'd',   // dalet with dagesh
  'ד': 'd',
  'ה': 'h',
  'ו': 'v',    // vav (consonantal)
  'זּ': 'z',
  'ז': 'z',
  'ח': 'kh',   // chet
  'טּ': 't',
  'ט': 't',
  'י': 'y',    // yod (consonantal)
  'כּ': 'k',   // kaf with dagesh
  'כ': 'kh',   // khaf
  'ךּ': 'k',
  'ך': 'kh',   // final khaf
  'לּ': 'l',
  'ל': 'l',
  'מּ': 'm',
  'מ': 'm',
  'ם': 'm',    // final mem
  'נּ': 'n',
  'נ': 'n',
  'ן': 'n',    // final nun
  'סּ': 's',
  'ס': 's',
  'ע': '',     // ayin – guttural (omitted in simplified phonetics)
  'פּ': 'p',   // pe with dagesh
  'פ': 'f',    // fe
  'ף': 'f',    // final fe
  'צ': 'ts',
  'ץ': 'ts',   // final tsadi
  'קּ': 'k',
  'ק': 'k',
  'רּ': 'r',
  'ר': 'r',
  'שׁ': 'sh',  // shin
  'שׂ': 's',   // sin
  'ש': 'sh',
  'תּ': 't',   // tav with dagesh
  'ת': 't',
};

const HEBREW_VOWELS = {
  'ְ': 'e',   // sheva (reduced)
  'ֱ': 'e',   // hataf segol
  'ֲ': 'a',   // hataf patah
  'ֳ': 'o',   // hataf qamats
  'ִ': 'i',   // hiriq
  'ֵ': 'e',   // tsere
  'ֶ': 'e',   // segol
  'ַ': 'a',   // patah
  'ָ': 'a',   // qamats (gadol = "a")
  'ֹ': 'o',   // holam
  'ֺ': 'o',   // holam haser
  'ֻ': 'u',   // qibbuts
  'ּ': '',    // dagesh (consonant doubling marker – handled separately)
  'ֽ': '',    // meteg (secondary stress – ignored)
  '־': '-',   // maqaf (word joiner)
  'ֿ': '',    // rafe
  'ׁ': '',    // shin dot (already handled via שׁ)
  'ׂ': '',    // sin dot
};

// Vav + holam = "o"; vav + shuruk = "u"
const SHURUK = 'ּ'; // dagesh in vav = shuruk
const HOLAM  = 'ֹ';
const VAV    = 'ו';

/**
 * Transliterate a single Hebrew word (with nikkud) into phonetic English.
 * Returns { phonetic, syllables, stressed } where:
 *   phonetic  – plain phonetic string ("adonai")
 *   syllables – array of syllable strings (["a", "do", "nai"])
 *   display   – formatted string with breaks and stress ("a·do·ˈnai")
 */
function transliterateHebrewWord(word) {
  if (!word || !word.trim()) return { phonetic: '', display: '' };

  // Decompose to NFD so combining marks appear after their base char
  const chars = [...word.normalize('NFD')];
  let result = '';
  let i = 0;

  while (i < chars.length) {
    const ch = chars[i];
    const cp = ch.codePointAt(0);

    // Skip cantillation marks (U+0591–U+05AF) and other non-phonetic marks
    if (cp >= 0x0591 && cp <= 0x05AF) { i++; continue; }
    // Skip already-processed combining marks
    if (cp >= 0x05B0 && cp <= 0x05C7 && cp !== 0x05D5) { i++; continue; }

    // Hebrew letter range
    if (cp >= 0x05D0 && cp <= 0x05EA) {
      // Collect any combining marks that follow
      let base = ch;
      let vowel = '';
      let hasDagesh = false;
      let j = i + 1;

      while (j < chars.length) {
        const next = chars[j];
        const ncp = next.codePointAt(0);
        if (ncp >= 0x05B0 && ncp <= 0x05C7) {
          if (ncp === 0x05BC) hasDagesh = true;     // dagesh
          else if (HEBREW_VOWELS[next] !== undefined) {
            vowel = HEBREW_VOWELS[next];
          }
          j++;
        } else if (ncp >= 0x0591 && ncp <= 0x05AF) {
          j++; // skip cantillation
        } else {
          break;
        }
      }

      // Special case: vav with dagesh (shuruk) = "u"
      if (ch === VAV && hasDagesh) {
        result += 'u';
        i = j;
        continue;
      }
      // Vav + holam = "o" (holam male)
      if (ch === VAV && chars.slice(i+1, j).some(c => c === HOLAM)) {
        result += 'o';
        i = j;
        continue;
      }

      // Shin/Sin distinction
      let cons = '';
      if (ch === 'ש') {
        const marks = chars.slice(i+1, j).map(c => c.codePointAt(0));
        if (marks.includes(0x05C1)) cons = 'sh';
        else if (marks.includes(0x05C2)) cons = 's';
        else cons = 'sh'; // default to shin
      } else {
        // Try dagesh variant first
        const withDagesh = ch + 'ּ';
        cons = HEBREW_CONSONANTS[withDagesh] ?? HEBREW_CONSONANTS[ch] ?? '';
        if (hasDagesh && cons && !['b','g','d','k','p','t'].includes(cons)) {
          // Double the consonant for gemination (simplified: skip in phonetics)
        }
      }

      // Silent aleph/ayin at start only produce a vowel
      if ((ch === 'א' || ch === 'ע') && vowel) {
        result += vowel;
      } else {
        result += cons + vowel;
      }

      i = j;
      continue;
    }

    // Maqaf (hyphen joiner) → space
    if (cp === 0x05BE) { result += ' '; i++; continue; }

    // Pass through spaces and ASCII
    if (ch === ' ' || cp < 0x0590) { result += ch === ' ' ? ' ' : ''; i++; continue; }

    i++;
  }

  // Build syllable display (naive CV-split for visual chunking)
  const display = buildHebrewDisplay(result.trim());
  return { phonetic: result.trim(), display };
}

function buildHebrewDisplay(phonetic) {
  if (!phonetic) return '';
  // Split on vowel boundaries to approximate syllables
  // Pattern: consonant cluster + vowel = one syllable
  const syllables = phonetic.match(/[^aeiou]*[aeiou]+(?:[^aeiou]*(?=[aeiou])|[^aeiou]*$)/gi) || [phonetic];
  if (syllables.length === 0) return phonetic;
  // Stress on penultimate syllable (milra') as default in Biblical Hebrew
  const stressIdx = syllables.length > 1 ? syllables.length - 1 : 0;
  return syllables
    .map((s, idx) => (idx === stressIdx ? 'ˈ' + s : s))
    .join('·');
}

/**
 * Transliterate a full Hebrew verse (string of words with nikkud).
 * Returns an array of word objects: { hebrew, phonetic, display }
 */
function transliterateHebrewVerse(verse) {
  if (!verse) return [];
  return verse.split(/\s+/).filter(Boolean).map(word => {
    const { phonetic, display } = transliterateHebrewWord(word);
    return { hebrew: word, phonetic, display };
  });
}

// ─── LATIN ───────────────────────────────────────────────────────────────────

/**
 * Ecclesiastical Latin pronunciation rules.
 * Based on the Roman Catholic/Church pronunciation used in liturgy.
 */

const LATIN_DIGRAPHS = [
  // Must be checked before single-letter rules
  { re: /ae/gi,   ph: 'ay' },
  { re: /oe/gi,   ph: 'ay' },
  { re: /qu/gi,   ph: 'kw' },
  { re: /ch/gi,   ph: 'k'  },
  { re: /ph/gi,   ph: 'f'  },
  { re: /th/gi,   ph: 't'  },
  { re: /gn/gi,   ph: 'ny' },
  { re: /ngu(?=[aeiou])/gi, ph: 'ngw' },
  { re: /ti(?=[aeiou])/gi,  ph: 'tsee' }, // tio → tsio
  { re: /xc(?=[ei])/gi,     ph: 'ksh' },
];

const LATIN_SINGLES = [
  { re: /c(?=[eiéí])/gi, ph: 'ch' },  // ce, ci → che, chi
  { re: /g(?=[ei])/gi,              ph: 'j'  },  // ge, gi → soft g
  { re: /j/gi,                      ph: 'y'  },  // j → y (consonantal)
  { re: /v/gi,                      ph: 'v'  },  // v (classical = w, eccl. = v)
  { re: /y/gi,                      ph: 'ee' },  // y → ee (Greek loan)
  { re: /x/gi,                      ph: 'ks' },
  { re: /z/gi,                      ph: 'dz' },
];

/**
 * Transliterate a Latin word to phonetic English (Ecclesiastical).
 */
function transliterateLatinWord(word) {
  if (!word || !word.trim()) return { latin: word, phonetic: '', display: '' };

  let ph = word.toLowerCase();

  // Apply digraph rules first
  for (const rule of LATIN_DIGRAPHS) ph = ph.replace(rule.re, rule.ph);
  // Then single-letter rules
  for (const rule of LATIN_SINGLES)  ph = ph.replace(rule.re, rule.ph);

  // Remove any punctuation carry-over
  ph = ph.replace(/[^a-z·ˈ\s]/gi, '');

  const display = buildLatinDisplay(ph, word);
  return { latin: word, phonetic: ph, display };
}

/**
 * Estimate Latin syllable breaks and stress.
 * Stress rule: if penultimate syllable is long (has long vowel or ends in consonant
 * cluster), stress it; otherwise stress the antepenultimate.
 */
function buildLatinDisplay(phonetic, originalWord) {
  if (!phonetic) return '';

  // Split into syllables: each vowel cluster = nucleus
  const syllables = phonetic.match(/[^aeiou]*[aeiou]+(?:[^aeiou]*(?=[aeiou])|[^aeiou]*$)/gi);
  if (!syllables || syllables.length === 0) return phonetic;
  if (syllables.length === 1) return 'ˈ' + syllables[0];

  // Penultimate stress heuristic
  let stressIdx = syllables.length - 2;
  // If penultimate ends in a single consonant (light), move stress to antepenultimate
  const penult = syllables[syllables.length - 2];
  const trailingCons = penult.match(/[^aeiou]+$/);
  if (syllables.length >= 3 && (!trailingCons || trailingCons[0].length === 1)) {
    stressIdx = syllables.length - 3;
  }

  return syllables
    .map((s, idx) => (idx === stressIdx ? 'ˈ' + s : s))
    .join('·');
}

/**
 * Transliterate a full Latin verse string.
 * Returns array of word objects: { latin, phonetic, display }
 */
function transliterateLatinVerse(verse) {
  if (!verse) return [];
  // Split on spaces but keep punctuation attached to words
  return verse.split(/\s+/).filter(Boolean).map(word => transliterateLatinWord(word));
}

// ─── EXPORTS ─────────────────────────────────────────────────────────────────

if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    transliterateHebrewWord,
    transliterateHebrewVerse,
    transliterateLatinWord,
    transliterateLatinVerse,
  };
}
