# Epic Building Group: demo site

A private demo by Lumen adl for Epic Building Group (Master Builders, Adelaide). Not their live
site. Every page is `noindex`, there is no sitemap, and `vercel.json` sends `X-Robots-Tag: noindex`.

- Static HTML, CSS and JS. No framework, no build step. Vercel serves the repo root.
- `vercel.json` sets `cleanUrls`, so `/contact` is served from `contact.html`. Preview locally with
  `npx serve .` (it serves clean URLs the same way).
- `assets/css/epic.css` holds the tokens and every style; `assets/js/epic.js` is optional polish.
- `research/` is the brief's paper trail (client facts, competitors, Mobbin references, direction,
  gaps). It is in `.vercelignore`, so it is never served.

Status: phase 3 built. Home, projects index, 35 project pages, services, process, about, contact
and 404.

The 35 project pages share one layout, so they are written by a small script rather than by hand:
`python3 tools/build.py` rewrites every page from `tools/projects.py` (the facts), `tools/pages.py`
(the layouts) and `tools/photos.json` (which photograph goes where, with alt text). The HTML it
writes is committed and is what Vercel serves; nothing is built at deploy time. `tools/` is in
`.vercelignore`.

Rules: only facts from epicbuildinggroup.com.au; their own photographs; anything missing goes in
`research/gaps.md`, never invented.
