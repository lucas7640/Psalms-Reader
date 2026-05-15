# Deploying to GitHub Pages

Follow these steps to publish your Psalms site at  
`https://YOUR-USERNAME.github.io/psalms-ancient-voices/`

---

## 1  Create a GitHub repository

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `psalms-ancient-voices` (or anything you like)
3. Set visibility to **Public** (required for free GitHub Pages)
4. Leave "Initialize with README" **unchecked**
5. Click **Create repository**

---

## 2  Push this project

Open a terminal in this folder and run:

```bash
git init
git add .
git commit -m "Initial commit — Psalms: Ancient Voices"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/psalms-ancient-voices.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

---

## 3  Enable GitHub Pages

1. In your repo on GitHub, click **Settings → Pages**
2. Under **Source**, select **Deploy from a branch**
3. Branch: **main** / folder: **/ (root)**
4. Click **Save**

Your site will be live within ~60 seconds at:  
`https://YOUR-USERNAME.github.io/psalms-ancient-voices/`

---

## 4  Generate all 150 Psalms (optional but recommended)

The starter `data/psalms.json` includes 6 Psalms. To get all 150:

```bash
pip install requests
python generate_data.py   # ~5 minutes, downloads from Sefaria
git add data/psalms.json
git commit -m "Add all 150 Psalms"
git push
```

The site auto-refreshes from GitHub Pages within a minute of each push.

---

## 5  Updating the site

Any time you change files:

```bash
git add .
git commit -m "Describe your change"
git push
```

GitHub Pages redeploys automatically.

---

## Translations included

| Column | Translation | Year | Status |
|--------|-------------|------|--------|
| Hebrew | Westminster Leningrad Codex (nikkud) | c. 1008 | Public domain |
| Latin  | Clementine Vulgate | 1592 | Public domain |
| KJV    | King James Version | 1611 | Public domain |
| ESV    | English Standard Version | 2001 | Free non-commercial use |
| RSV    | Revised Standard Version | 1952 | Fair use / non-commercial |

## Audio

The site uses your browser's built-in **Web Speech API** — no API key needed.
- Hebrew uses the `he-IL` voice (Israeli Hebrew, closest available)
- Latin uses `it-IT` (Italian — closest to Ecclesiastical Latin pronunciation)
- Voice availability depends on your operating system and browser

---

*Built with HTML, CSS, and vanilla JavaScript — zero dependencies, zero build step.*
