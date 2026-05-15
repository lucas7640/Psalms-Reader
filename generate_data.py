#!/usr/bin/env python3
"""
generate_data.py  —  Psalms: Ancient Voices
=============================================
Downloads all 150 Psalms in five translations from Sefaria's free API
and writes data/psalms.json.

Run this on your local machine (requires internet):
    pip install requests
    python generate_data.py

Source:
    Hebrew  — Westminster Leningrad Codex with nikkud  (Sefaria, public domain)
    Latin   — Clementine Vulgate                        (Sefaria, public domain)
    KJV     — King James Version 1611                   (Sefaria, public domain)
    ESV     — English Standard Version 2001             (Sefaria, fair-use excerpts)
    RSV     — Revised Standard Version 1952             (Sefaria, fair-use excerpts)
"""

import json
import re
import time
import pathlib
import sys

try:
    import requests
except ImportError:
    sys.exit("Install requests first:  pip install requests")

OUT = pathlib.Path("data/psalms.json")
OUT.parent.mkdir(exist_ok=True)

SEFARIA = "https://www.sefaria.org/api/texts"

VERSION_MAP = {
    "hebrew": ("he", "Tanakh+with+Nikkud"),
    "latin":  ("en", "The+Latin+Vulgate"),
    "kjv":    ("en", "King+James+Version"),
    "esv":    ("en", "English+Standard+Version"),
    "rsv":    ("en", "Revised+Standard+Version+1952"),
}

def clean(text):
    if not text:
        return ""
    # Strip HTML tags that Sefaria sometimes wraps text in
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()

def fetch_verses(num, lang_key, lang_code, version):
    url = f"{SEFARIA}/Psalms.{num}?lang={lang_code}&version={version}"
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=20)
            r.raise_for_status()
            data = r.json()
            key = "he" if lang_code == "he" else "text"
            raw = data.get(key, [])
            verses = []
            for v in raw:
                if isinstance(v, list):
                    verses.extend(v)
                else:
                    verses.append(v)
            return [clean(v) for v in verses]
        except Exception as e:
            if attempt == 2:
                print(f"    Warning: {lang_key} failed for Psalm {num}: {e}")
                return []
            time.sleep(1.5)

PSALM_NAMES = {
    1:'The Two Ways', 22:'My God, My God', 23:'The Lord Is My Shepherd',
    51:'Miserere', 91:'He Who Dwells in the Shelter',
    100:'Jubilate Deo', 110:'The Lord Said to My Lord',
    119:'Blessed Are the Undefiled', 121:'I Lift Up My Eyes',
    130:'De Profundis', 150:'Laudate Dominum',
}

def main():
    psalms = []
    print(f"Downloading 150 Psalms × 5 translations from Sefaria…")
    print("This takes ~5 minutes. Please be patient.\n")

    for num in range(1, 151):
        print(f"  Psalm {num}/150…", end=" ")
        verse_sets = {}
        for key, (lang_code, version) in VERSION_MAP.items():
            verse_sets[key] = fetch_verses(num, key, lang_code, version)
            time.sleep(0.25)  # be polite

        n = max((len(v) for v in verse_sets.values()), default=0)
        def pad(lst): return (lst + [''] * n)[:n]

        verses = [
            {
                "verse":  i + 1,
                "hebrew": pad(verse_sets["hebrew"])[i],
                "latin":  pad(verse_sets["latin"])[i],
                "kjv":    pad(verse_sets["kjv"])[i],
                "esv":    pad(verse_sets["esv"])[i],
                "rsv":    pad(verse_sets["rsv"])[i],
            }
            for i in range(n)
        ]

        psalms.append({
            "psalm":       num,
            "title":       f"Psalm {num}",
            "superscript": PSALM_NAMES.get(num, ""),
            "verses":      verses,
        })
        print(f"{n} verses ✓")
        time.sleep(0.3)

    OUT.write_text(json.dumps(psalms, ensure_ascii=False, indent=2), encoding="utf-8")
    total = sum(len(p["verses"]) for p in psalms)
    print(f"\n✓ Done! {len(psalms)} psalms, {total} verses → {OUT}")

if __name__ == "__main__":
    main()
