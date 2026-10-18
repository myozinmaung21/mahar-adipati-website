# Mahar Adipati Travel Company — website

Static landing page for Mahar Adipati Travel Company, Abu Dhabi: international air tickets, visas, passport & document services, car rental & transfers, and tour packages.

- `index.html`, `services/` — English pages (the default)
- `my/` — Burmese (မြန်မာ) pages, same layout; the EN | မြန်မာ switcher in the header links each page to its twin
- `assets/` — logo and service images (photo credits in `assets/services/CREDITS.txt`)
- `_source/content_en.py`, `_source/content_my.py` — all the text, one file per language
- `_source/build.py` — renders every page from those files. After editing text, run `python3 _source/build.py .` from this folder to rebuild. Don't edit the `.html` files directly; the next rebuild overwrites them.

Hosted on Vercel; every push to `main` redeploys automatically. `vercel.json` turns on clean URLs (`/services/visas` instead of `/services/visas.html`; old `.html` links redirect).
