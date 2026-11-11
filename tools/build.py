#!/usr/bin/env python3
"""Writes the site's HTML pages from tools/projects.py and tools/photos.json.

The site itself has no build step: Vercel serves the committed HTML as it is. This script only
saves writing 35 project pages by hand. Run `python3 tools/build.py` and commit what it writes.
`python3 tools/build.py --images /path/to/their/site/mirror` also exports the photographs.
"""
import html, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from projects import P, CATS  # noqa: E402

if "--images" in sys.argv:  # export first, so the pages are built from the fresh list
    from images import export

    export(sys.argv[sys.argv.index("--images") + 1])

SITE = "https://epicbuildinggroup.com.au"  # canonical host for when it goes live
PHOTOS = json.load(open(os.path.join(ROOT, "tools", "photos.json")))
BY = {p["slug"]: p for p in P}
e = html.escape

import hashlib


def ver(path):
    """A short fingerprint of a file, so a changed stylesheet or script gets a new address."""
    return hashlib.md5(open(os.path.join(ROOT, path), "rb").read()).hexdigest()[:8]


CSS_V, JS_V = ver("assets/css/epic.css"), ver("assets/js/epic.js")

ARROW = '<svg class="arrow" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="square" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>'
BEAM = '<i class="beam" aria-hidden="true"></i>'
NAV = [("/projects", "Projects"), ("/services", "Services"), ("/process", "Process"), ("/about", "About"), ("/contact", "Contact")]
STAGE_NAMES = dict(site="At the start", frame="Frame and structure", lockup="Lock-up", fitout="Fit out")

BUSINESS = {
    "@type": "GeneralContractor",
    "@id": SITE + "/#business",
    "name": "Epic Building Group",
    "legalName": "Epic Building Group Pty Ltd trading as Peter Tsoukalas General Builders",
    "url": SITE + "/",
    "telephone": "+61881520948",
    "email": "contact@epicbuildinggroup.com.au",
    "address": {"@type": "PostalAddress", "streetAddress": "220 Richmond Rd", "addressLocality": "Marleston", "addressRegion": "SA", "postalCode": "5033", "addressCountry": "AU"},
    "areaServed": {"@type": "City", "name": "Adelaide"},
    "founder": {"@type": "Person", "name": "Peter Tsoukalas"},
    "award": "Master Builders Association of South Australia, Best Renovation (renovations up to $600,000), 2011",
    "hasCredential": {"@type": "EducationalOccupationalCredential", "credentialCategory": "Builder's Licence", "identifier": "GL185386 GL/SGL56932"},
}


# ---------- photographs ----------
def photo(slug, file):
    """(src 740, src 370, alt, w, h) for one of a project's photographs, by its original file name."""
    ph = PHOTOS[slug]
    i = ph["files"].index(file)
    m = ph["meta"][i]
    return dict(src=f"/assets/img/projects/{slug}/{i + 1:02d}.webp", small=f"/assets/img/projects/{slug}/{i + 1:02d}-s.webp", alt=m["alt"], w=m["w"], h=m["h"], kind=m["kind"], stage=m.get("stage", ""))


def img(ph, cls="", lazy=True, sizes="(min-width: 1000px) 46vw, 100vw", small=False):
    lz = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    if small:
        return f'<img{c} src="{ph["small"]}" srcset="{ph["small"]} 370w, {ph["src"]} 740w" sizes="{sizes}" width="{ph["w"]}" height="{ph["h"]}" alt="{e(ph["alt"])}"{lz} decoding="async">'
    return f'<img{c} src="{ph["src"]}" width="{ph["w"]}" height="{ph["h"]}" alt="{e(ph["alt"])}"{lz} decoding="async">'


def hero_of(slug):
    return photo(slug, PHOTOS[slug]["hero"])


def todo(text):
    return f'<span class="todo" title="Not published on the current site. Listed in research/gaps.md.">To confirm: {e(text)}</span>'


def built(p):
    b = p.get("built")
    if b == "TODO":
        return todo("dates")
    return e(b) if b else ""


# ---------- shared page parts ----------
def head(title, desc, path, ld=None, preload=""):
    lds = ""
    if ld:
        lds = '\n<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": ld}, separators=(",", ":")) + "</script>"
    return f"""<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta name="theme-color" content="#0e1011">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<link rel="icon" href="/assets/img/brand/epic-mark.png" type="image/png">
<link rel="preload" href="/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>{preload}
<link rel="stylesheet" href="/assets/css/epic.css?v={CSS_V}">
<script>document.documentElement.classList.add("js")</script>{lds}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(current=""):
    def a(h, t):
        return f'<a href="{h}"' + (' aria-current="page"' if h == current else "") + f">{t}</a>"

    nav = "\n      ".join(a(h, t) for h, t in NAV)
    mnav = "\n          ".join(f'<a href="{h}">{t} <span class="label">0{i + 1}</span></a>' for i, (h, t) in enumerate(NAV))
    return f"""
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/" aria-label="Epic Building Group, home">
      <img src="/assets/img/brand/epic-logo.png" alt="Epic Building Group" width="390" height="83">
    </a>
    <nav class="nav" aria-label="Main">
      {nav}
    </nav>
    <div class="head-actions">
      <a class="head-call tel" href="tel:+61411510558" aria-label="Call Peter on 0411 510 558">{PHONE}<span>0411 510 558</span></a>
      <a class="btn btn--small head-start" href="/contact">Start a project</a>
      <details class="menu">
        <summary aria-label="Menu">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square" aria-hidden="true"><line x1="4" y1="8" x2="20" y2="8"/><line x1="4" y1="16" x2="20" y2="16"/></svg>
        </summary>
        <nav class="menu-panel" aria-label="Main, phone">
          {mnav}
        </nav>
      </details>
    </div>
  </div>
</header>
"""


def cta(title="Have a project to talk about?", text="Tell us what you are planning, or call Peter. We will arrange a time to meet, on site where we can.", type_=""):
    q = f"?type={type_}" if type_ else ""
    return f"""
<section class="cta" aria-labelledby="cta-title">
  <div class="wrap">
    <p class="label" data-reveal>{BEAM}Start a project conversation</p>
    <h2 class="shout" id="cta-title" data-reveal>{title}</h2>
    <div class="cta-row" data-reveal>
      <p class="lede">{text}</p>
      <div class="hero-actions">
        <a class="btn" href="/contact{q}">Start a project conversation {ARROW}</a>
        <a class="btn btn--line tel" href="tel:+61411510558">Call Peter&ensp;0411 510 558</a>
      </div>
    </div>
  </div>
</section>
"""


def footer(scripts=""):
    nav = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    feats = "".join(f'<li><a href="/projects/{p["slug"]}">{e(p["name"])}</a></li>' for p in P if p.get("feature"))
    return f"""
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img class="foot-logo" src="/assets/img/brand/epic-logo.png" alt="Epic Building Group" width="390" height="83" loading="lazy">
        <p>Traditional South Australian Master Builders. Home renovations and extensions, kitchens and bathrooms, new homes, residential developments and commercial building.</p>
      </div>
      <nav aria-label="Footer">
        <p class="label">Site</p>
        <ul>{nav}</ul>
      </nav>
      <div>
        <p class="label">Feature projects</p>
        <ul>{feats}</ul>
      </div>
      <div>
        <p class="label">Contact</p>
        <ul>
          <li><a class="tel" href="tel:+61411510558">Peter 0411 510 558</a></li>
          <li><a class="tel" href="tel:+61881520948">Office 08 8152 0948</a></li>
          <li><a href="mailto:contact@epicbuildinggroup.com.au">contact@epicbuildinggroup.com.au</a></li>
          <li>220 Richmond Rd, Marleston SA 5033</li>
        </ul>
      </div>
    </div>
    <p class="foot-award"><b>Master Builders Association Award Winner.</b> Awarded Best Renovation, in the category for renovations up to $600,000, by the Master Builders Association of South Australia in 2011.</p>
    <p class="foot-legal">Epic Building Group Pty Ltd trading as Peter Tsoukalas General Builders. Builder's Licence GL185386 GL/SGL56932. PO Box 301, Marleston SA 5033. Photography by Karen Roberts Photography. Demo by <a href="https://www.lumenadl.com">Lumen adl</a>: not the live site.</p>
  </div>
</footer>

<div class="bar" id="bar">
  <a class="btn btn--line tel" href="tel:+61411510558">{PHONE} Call Peter</a>
  <a class="btn" href="/contact">Start a project</a>
</div>

<script src="/assets/js/epic.js?v={JS_V}" defer></script>{scripts}
</body>
</html>
"""


def page_head(label, title, lede, crumbs=None):
    c = ""
    if crumbs:
        c = '<nav class="crumbs label" aria-label="Breadcrumb">' + " <span aria-hidden=\"true\">/</span> ".join(f'<a href="{h}">{t}</a>' if h else f"<span>{t}</span>" for h, t in crumbs) + "</nav>"
    return f"""
<section class="page-head">
  <div class="wrap">
    {c}
    <p class="label kick">{BEAM}{label}</p>
    <h1 class="shout">{title}</h1>
    <p class="lede">{lede}</p>
  </div>
</section>
"""


def card(p, i=0, lazy=True):
    ph = hero_of(p["slug"])
    b = built(p) if p.get("built") and p["built"] != "TODO" else ""
    meta = e(p["type"]) + (f" · {b}" if b else "")
    return f"""<a class="card" href="/projects/{p['slug']}" data-cat="{p['cat']}" data-reveal style="--i:{i % 3}">
        <figure>{img(ph, small=True, lazy=lazy, sizes="(min-width: 1000px) 30vw, (min-width: 640px) 46vw, 100vw")}</figure>
        <span class="card-body"><b>{e(p.get('short') or p['name'])}</b><span class="label">{meta}</span></span>
      </a>"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, "w") as f:
        f.write(content)


def crumb_ld(items):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + h} for i, (h, n) in enumerate(items)]}


PAYNEHAM = [
    "My husband and I cannot express, how fantastic our experience was with Peter and his amazing team at Epic Building Group.",
    "Peter was there every step of the way, from consultation about the purchase of the land, and all the possibilities available to us through his experienced and established company.",
    "We never felt forced or pressured into making decisions, but were encouraged to make decisions about our home that we would enjoy. Any obstacles that we faced, we responded to together, as a team. Peter provided us with his valued opinion, at every stage of the build, providing us with the flexibility to make changes, to ensure we were 100% satisfied with the outcome. It's a rarity these days, to receive such genuine and honest service and quality. Our house was built exactly as specified, and completely within the discussed time frame. The final product exceeded our expectations, and we were absolutely thrilled to have been a real part of this project.",
    "There have been many occasions where the Epic Building Group team have put in extra time to ensure that my husband and I were satisfied with the service we were receiving, but this was already evident due to the hard work that was being put into our home. Peter and his team have gone above and beyond with giving guidance, answering questions, and just making the building process stress free and exciting.",
    "I would highly recommend Epic Building Group to anyone looking to build a new home, or looking to restore and renovate an existing property. Building this home with Epic was the best decision we have ever made. Our property is constantly complimented, and we have been approached by several people in the area asking for contact details for our builder. We are so proud to call this our home, it is everything we could have ever dreamed of, and a perfect place to raise our family.",
]
ZOITAKIS = "I am writing this as a testimonial for all the hard work you have done on our extension at Westbourne Park. The extension was approximately 160 square metres and included a large area at the back of our existing house, an ensuite and a large laundry area. Both Soula and myself were very happy with your work on our renovation/extension. Your work ethic, punctuality and attention to detail was amazing. All the guys that worked with/for you were also exceptional and had the same drive and passion as you. I remember those early morning starts and waiting for you to come up our driveway singing cheerfully. Peter, you were always cheerful and accommodating with all the changes/alterations we required. We would not hesitate in using your company again in the future."


def payneham_quote(full=True):
    rest = "".join(f"<p>{e(x)}</p>" for x in PAYNEHAM[1:])
    more = f'<details class="more"><summary><span>Read the whole letter</span>{ARROW}</summary><div class="more-body">{rest}</div></details>' if full else ""
    return f"""
<section class="quote section" aria-labelledby="quote-title">
  <div class="wrap">
    <p class="label" data-reveal id="quote-title">{BEAM}Client testimonial</p>
    <figure data-reveal>
      <blockquote>
        <p class="quote-lead">{e(PAYNEHAM[0])}</p>
        {more}
      </blockquote>
      <figcaption><b>Owner</b><span class="label">Payneham new build</span> <a class="text-link" href="/projects/payneham">See the home {ARROW}</a></figcaption>
    </figure>
  </div>
</section>
"""


def pair_block(slug, earlier, finished, label, caption, heading="During and after"):
    a, b = photo(slug, earlier), photo(slug, finished)
    return f"""
    <div class="pair" data-reveal>
      <figure class="pair-side pair-side--old">
        {img(a)}
        <figcaption class="label">{label}</figcaption>
      </figure>
      <i class="pair-beam" aria-hidden="true"></i>
      <figure class="pair-side pair-side--new">
        {img(b)}
        <figcaption class="label">Finished</figcaption>
      </figure>
    </div>
    <p class="pair-note">{caption}</p>"""


# ---------- pages ----------
from pages import build_all  # noqa: E402

if __name__ == "__main__":
    n = build_all(sys.modules[__name__])
    print("wrote", n, "pages")
