# Epic Building Group: demo site

A private demo by Lumen adl for Epic Building Group (Master Builders, Adelaide). Not their live
site. Every page is `noindex`, there is no sitemap, and `vercel.json` sends `X-Robots-Tag: noindex`.

- Static HTML, CSS and JS. No framework, no build step. Vercel serves the repo root.
- `vercel.json` sets `cleanUrls`, so `/contact` is served from `contact.html`. Preview locally with
  `npx serve .` (it serves clean URLs the same way).
- `assets/css/epic.css` holds the tokens and every style; `assets/js/epic.js` is optional polish.
- `research/` is the brief's paper trail (client facts, competitors, Mobbin references, direction,
  gaps). It is in `.vercelignore`, so it is never served.

Status: phase 2. The homepage hero and the section under it prove the direction
(`research/direction.md`). Nothing else is built until the direction is agreed.

Rules: only facts from epicbuildinggroup.com.au; their own photographs; anything missing goes in
`research/gaps.md`, never invented.
