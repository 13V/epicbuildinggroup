"""The pages. Each function returns a whole HTML document; build_all writes them."""
import os

SERVICES = [
    dict(id="renovations-extensions", type="renovation", name="Renovations and extensions",
         text=["Whether you are looking to update, expand or improve the functionality and comfort of your home, we will help you maximise your space.",
               "We are able to marry the new building to existing buildings and surroundings, and can work in a heritage environment, as can be seen in our range of projects."],
         egs=["ovingham", "mile-end", "torrensville"]),
    dict(id="kitchens-bathrooms", type="kitchen-bathroom", name="Kitchens and bathrooms",
         text=["We offer a complete service, from design, construction, plumbing and electrics to assistance with the selection of the latest products.",
               "Our in-house designer is available to all clients to assist in the selection of fixtures, finishes and colour schemes for every room in the house."],
         egs=["unley", "parkside", "goodwood-new-home"]),
    dict(id="new-homes", type="new-home", name="New homes",
         text=["Applying our extensive industry knowledge and attention to detail, we ensure a smooth transition from design to your finished home.",
               "We can work from architectural drawings, or we can be involved from the initial design and planning stage, through approval to construction and completion."],
         egs=["torrens-park", "goodwood-new-home", "payneham"]),
    dict(id="developments", type="development", name="Residential developments",
         text=["Regardless of the size of your development, we consistently deliver exceptional workmanship and cutting edge building solutions.",
               "Duplexes, townhouses and groups of homes on one block, including our own developments at Highgate."],
         egs=["highgate", "newton", "eliza-street"]),
    dict(id="commercial", type="commercial", name="Commercial",
         text=["Our skilled team constantly research new building products to create truly functional commercial spaces, delivered on budget and on time.",
               "Our commercial projects are completed seamlessly, with internal works and fit out completed with the appropriate wet areas and services as required."],
         egs=["field-street", "velo-victoria-park", "fullarton-dental-surgery"]),
]
ALSO = [
    ("Project management", "Let us manage the budget, the site and procure sub-contractors, making sure that your project comes in on time and within budget."),
    ("In-house designer", "Available to all clients to assist in the selection of fixtures, finishes and colour schemes for every room in the house."),
    ("Carpentry services", "Our carpentry division is ready for any residential or commercial job."),
    ("Concrete and civil works", "Concrete cutting, coring and wall removals, solid concrete commercial grade construction, pools and retaining walls."),
    ("School works", "From major capital works to one off projects like bridges, walls and toilets."),
    ("Builders supervision", "Our building supervisors can provide the degree of supervision necessary for work on your site to be carried out safely."),
]
STAGES = [
    ("Consultation", "We start by listening",
     ["We explore all options up front with you, to define precisely what is to be built.",
      "You can come with a full set of architectural drawings, a rough sketch or a folder of magazine pictures. We have built from all three."],
     None),
    ("Design", "Drawn to suit the house and the budget",
     ["We can work from your architect's drawings, or be involved from the initial design and planning stage.",
      "Our architectural design team and in-house interior designer help with the selection of fixtures, finishes and colour schemes for every room."],
     None),
    ("Approvals", "Through approval, including heritage areas",
     ["We take projects through approval to construction, and we can work in a heritage environment: several of our projects kept a heritage street frontage and built new behind it."],
     "who lodges the application, and how long approvals usually take"),
    ("Build", "On site, with regular site meetings",
     ["Our clients deal with real Master Builders, with regular on site meetings and a hands on approach to keep the project on schedule and budget.",
      "We manage the budget, the site and the sub-contractors. Changes are talked through on site, as they come up."],
     "how often site meetings are held, and who attends"),
    ("Handover", "Finished, as specified",
     ["Our primary goal is a quality result, delivered on time and within budget, while meeting all construction specifications."],
     "what happens after handover (maintenance period, warranty)"),
]
QUESTIONS = {
    "extension": ("An extension", "Do you have drawings yet, or are you starting from an idea?"),
    "renovation": ("A renovation", "How old is the house, and what do you want to keep?"),
    "kitchen-bathroom": ("A kitchen or bathroom", "Which rooms, and are any walls or plumbing moving?"),
    "new-home": ("A new home", "Do you have the land, and do you have a design?"),
    "development": ("A development", "How many homes, and is the site approved yet?"),
    "commercial": ("A commercial project", "What is the building now, and when do you need to open?"),
}


def build_all(B):
    e, P, BY, CATS, PHOTOS = B.e, B.P, B.BY, B.CATS, B.PHOTOS
    ARROW, BEAM = B.ARROW, B.BEAM
    n = 0

    def doc(path, file, title, desc, body, current="", ld=None, preload="", scripts=""):
        nonlocal n
        B.write(file, B.head(title, desc, path, ld, preload) + B.header(current) + '\n<main id="main">\n' + body + "\n</main>\n" + B.footer(scripts))
        n += 1

    # ---------------- Home ----------------
    hero = open(os.path.join(B.ROOT, "tools", "partials", "hero.html")).read()
    plan = [
        ("extension", "An extension", "tranmere", "/images/pr_tranmere/image-1.jpg", "Tranmere", "Rear extension<br> to a 1940s home", "A new living room and a master bedroom, behind a 1940s home",
         "A new living room, a master bedroom with ensuite and walk in robe, a new laundry and patio, and a separate double garage. The new walls are interlocking panel cladding, set against the original red brick."),
        ("renovation", "A renovation", "mile-end", "/images/pr_mileend/mileend_1.jpg", "Mile End", "Renovation<br> and extension", "A derelict villa, fully renovated and extended",
         "An architecturally designed addition and a full renovation. The high ceilings are carried through, and a central garden with viewing glass makes a light filled break from old to new."),
        ("kitchen-bathroom", "A kitchen or bathroom", "unley", "/images/pr_unley/unley_5.jpg", "Unley", "Renovation<br> and extension, 2014", "A complete service, from design to the last fitting",
         "Design, construction, plumbing and electrics, and help choosing the products. Our in-house designer can help with fixtures, finishes and colour schemes for every room."),
        ("new-home", "A new home", "torrens-park", "/images/pr_torrenspark/torrenspark_2.jpg", "Torrens Park", "550 sqm ·<br> Dec 2012 to Dec 2013", "A classic home, detailed with its owner",
         "Built in close cooperation with the owner, who chose the exterior moulding, the cornices and skirting, the hallway bulkheads and archways, and custom designed sash windows."),
        ("development", "A development", "highgate", "/images/pr_highgate/highgate_18.jpg", "Highgate", "4 homes ·<br> 2015 to 2016", "Four designer homes on one site",
         "Designed by Peter Tsoukalas and his design team. The facades mix brick, render and natural timber, and the ceilings are at three metres."),
        ("commercial", "A commercial project", "field-street", "/images/pr_fieldst/fieldst_15.jpg", "Field Street", "500 sqm ·<br> Oct 2013 to Apr 2014", "A derelict cold store, rebuilt as five restaurants",
         "The warehouse was gutted and rebuilt with new structural walls, services, wet areas and rear mezzanine floors, on a congested city site. We also completed the fit out for three of the five restaurants."),
    ]
    radios = "\n".join(f'        <input type="radio" name="type" id="plan-{k}" value="{k}"{" checked" if i == 0 else ""}>' for i, (k, *_) in enumerate(plan))
    choices = "\n".join(f'            <label for="plan-{k}"><span class="n">0{i + 1}</span>{lab}{BEAM}</label>' for i, (k, lab, *_) in enumerate(plan))
    panels = ""
    for k, lab, slug, file, place, fact, h, text in plan:
        ph = B.photo(slug, file)
        panels += f"""
            <div class="panel panel--{k}">
              <figure class="panel-photo">
                {B.img(ph, sizes="(min-width: 1000px) 54vw, 100vw")}
                <figcaption><b>{place}</b><span class="label">{fact}</span></figcaption>
              </figure>
              <div class="panel-body">
                <div>
                  <h3 class="h3">{h}</h3>
                  <p>{text} <a class="text-link" href="/projects/{slug}">See the project</a></p>
                </div>
                <div class="first-q" style="--w:1">
                  <span class="label">The first thing we will ask</span>
                  <strong>{QUESTIONS[k][1]}</strong>
                </div>
                <div class="panel-actions" style="--w:2">
                  <button class="btn" type="submit">Talk to us about {lab[0].lower() + lab[1:]} {ARROW}</button>
                </div>
              </div>
            </div>
"""
    feats = ""
    for p in sorted([p for p in P if p.get("feature")], key=lambda p: p["feature"]):
        ph = B.hero_of(p["slug"])
        facts = "".join(f"<li><span class='label'>{a}</span>{b}</li>" for a, b in [("Type", e(p["type"])), ("Built", B.built(p)), ("Size", e(p.get("size", "")))] if b)
        feats += f"""
      <article class="feature" data-reveal>
        <a class="feature-photo" href="/projects/{p['slug']}" tabindex="-1" aria-hidden="true">{B.img(ph)}</a>
        <div class="feature-body">
          <p class="label"><span class="n">0{p['feature']}</span> {e(p['type'])}</p>
          <h3 class="h2"><a href="/projects/{p['slug']}">{e(p.get('short') or p['name'])}</a></h3>
          <p class="lede">{e(p['lede'])}</p>
          <ul class="mini-facts">{facts}</ul>
          <a class="btn btn--line" href="/projects/{p['slug']}">See how it was built {ARROW}</a>
        </div>
      </article>"""
    stages_home = "".join(f'<li data-reveal style="--i:{i}"><span class="label">0{i + 1}</span><b>{s[0]}</b><span>{s[1]}</span></li>' for i, s in enumerate(STAGES))
    svc = "".join(f'<li><a href="/services#{s["id"]}"><span class="n label">0{i + 1}</span>{s["name"]}{ARROW}</a></li>' for i, s in enumerate(SERVICES))
    home = hero + """
<!-- Phones: the hero carries only the headline and the two actions. Its sentence and the note on
     the photograph sit here, straight under it. -->
<div class="hero-after dark">
  <div class="wrap">
    <p class="lede">On site and hands on. Second generation Adelaide builders of renovations and extensions, new homes, developments and commercial work, run with regular on site meetings.</p>
    <p class="label">Pictured: new home, Torrens Park, 550 sqm, built Dec 2012 to Dec 2013</p>
  </div>
</div>
""" + f"""
<!-- 2. The record: facts as their own site states them -->
<section class="record" aria-label="Epic Building Group at a glance">
  <div class="wrap">
    <ul>
      <li data-reveal><b>GL185386</b><span class="label">Builder's licence</span><small>Also GL/SGL56932</small></li>
      <li data-reveal style="--i:1"><b>2011</b><span class="label">Master Builders SA award</span><small>Best Renovation, up to $600,000</small></li>
      <li data-reveal style="--i:2"><b>14</b><span class="label">Full time team</span><small>Plus preferred contractors</small></li>
      <li data-reveal style="--i:3"><b>25+</b><span class="label">Years of projects</span><small>Across Adelaide</small></li>
      <li data-reveal style="--i:4"><b>2nd</b><span class="label">Generation</span><small>A family building company</small></li>
    </ul>
  </div>
</section>

<!-- 3. What are you planning? Works without JavaScript: radio buttons and CSS. -->
<section class="section planner on-light" id="planning" aria-labelledby="planning-title">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <p class="label">{BEAM}Start here</p>
      <h2 class="h2" id="planning-title">What are you planning?</h2>
      <p class="lede">Pick the closest fit. You will see a job like it that we have built, and the first thing we will ask you.</p>
    </div>
    <form action="/contact" method="get" data-reveal>
      <fieldset>
        <legend class="vh">Type of project</legend>
{radios}
        <div class="planner-grid">
          <div class="choices">
{choices}
          </div>
          <div class="panels" aria-live="polite">
{panels}
          </div>
        </div>
      </fieldset>
    </form>
  </div>
</section>

<!-- 4. Feature projects -->
<section class="section dark" aria-labelledby="features-title">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <p class="label">{BEAM}Feature projects</p>
      <h2 class="h2" id="features-title">Four jobs, four kinds of building.</h2>
      <p class="lede">A new home, a commercial rebuild, a heritage renovation and a development of our own. Each page shows the build in order.</p>
    </div>
    <div class="features">{feats}
    </div>
    <p class="section-foot" data-reveal><a class="btn" href="/projects">All {len(P)} projects {ARROW}</a></p>
  </div>
</section>

<!-- 5. During and after: a still pair -->
<section class="section on-light" aria-labelledby="pair-title">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <p class="label">{BEAM}During and after</p>
      <h2 class="h2" id="pair-title">The same corner, six months apart.</h2>
      <p class="lede">Field Street, Adelaide. A derelict cold store in October 2013; five restaurants by April 2014.</p>
    </div>
    {B.pair_block("field-street", "/images/pr_fieldst/fieldst_5.jpg", "/images/pr_fieldst/fieldst_10.jpg", "During", 'Both photographs are from the Field Street project. <a class="text-link" href="/projects/field-street">See the whole build</a>')}
  </div>
</section>

<!-- 6. How a build runs -->
<section class="section dark" aria-labelledby="how-title">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <p class="label">{BEAM}How a build runs</p>
      <h2 class="h2" id="how-title">Five stages. We are on site for all of them.</h2>
      <p class="lede">Regular on site meetings and a hands on approach keep a project on schedule and budget.</p>
    </div>
    <ol class="steps">{stages_home}</ol>
    <p class="section-foot" data-reveal><a class="btn btn--line" href="/process">The process in full {ARROW}</a></p>
  </div>
</section>
""" + B.payneham_quote() + f"""
<!-- 8. Services -->
<section class="section on-light svc-home" aria-labelledby="svc-title">
  <div class="wrap">
    <div class="section-head" data-reveal>
      <p class="label">{BEAM}What we build</p>
      <h2 class="h2" id="svc-title">All aspects of residential and commercial construction.</h2>
    </div>
    <ul class="biglist" data-reveal>{svc}</ul>
  </div>
</section>
""" + B.cta()
    pre = """
<link rel="preload" as="image" type="image/avif" href="/assets/img/hero/torrens-park-phone.avif" media="(max-width: 899px)" fetchpriority="high">
<link rel="preload" as="image" type="image/avif" imagesrcset="/assets/img/hero/torrens-park-1280.avif 1280w, /assets/img/hero/torrens-park-1920.avif 1920w" imagesizes="max(100vw, 220vh)" media="(min-width: 900px)" fetchpriority="high">"""
    doc("/", "index.html", "Epic Building Group | Master Builders, Adelaide",
        "Traditional South Australian Master Builders. Home renovations and extensions, kitchens and bathrooms, new homes, residential developments and commercial building across Adelaide.",
        home, ld=[B.BUSINESS, {"@type": "WebSite", "@id": B.SITE + "/#website", "url": B.SITE + "/", "name": "Epic Building Group", "publisher": {"@id": B.SITE + "/#business"}}], preload=pre)

    # ---------------- Projects index ----------------
    counts = {c: sum(1 for p in P if p["cat"] == c) for c in CATS}
    fr = '<input type="radio" name="f" id="f-all" checked>' + "".join(f'<input type="radio" name="f" id="f-{c}">' for c in CATS)
    fl = f'<label for="f-all">All <span>{len(P)}</span></label>' + "".join(f'<label for="f-{c}">{CATS[c]} <span>{counts[c]}</span></label>' for c in CATS)
    cards = "\n      ".join(B.card(p, i, lazy=i > 2) for i, p in enumerate(P))
    body = B.page_head("Projects", "Built by Epic.", f"{len(P)} projects across Adelaide: new homes, renovations and extensions, developments and commercial work. Every one is ours, and every photograph is of the job itself.") + f"""
<section class="section on-light index" aria-label="All projects">
  <div class="wrap">
    <form class="filter" aria-label="Filter projects">
      {fr}
      <div class="filter-bar" role="group" aria-label="Kind of project">{fl}</div>
      <div class="cards">
      {cards}
      </div>
    </form>
  </div>
</section>
""" + B.cta()
    doc("/projects", "projects.html", "Projects | Epic Building Group, Adelaide",
        "New homes, renovations and extensions, residential developments and commercial projects built by Epic Building Group across Adelaide.", body, current="/projects",
        ld=[B.crumb_ld([("/", "Home"), ("/projects", "Projects")]), {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{B.SITE}/projects/{p['slug']}", "name": p["name"]} for i, p in enumerate(P)]}])

    # ---------------- Project pages ----------------
    for idx, p in enumerate(P):
        slug, ph = p["slug"], PHOTOS[p["slug"]]
        hp = B.hero_of(slug)
        facts = [("Type", e(p["type"])), ("Built", B.built(p)), ("Duration", e(p.get("duration", ""))), ("Size", e(p.get("size", ""))), ("Rooms", e(p.get("rooms", ""))),
                 ("Our part", e(p.get("scope", ""))), ("With", e(p.get("credit", ""))), ("Award", e(p.get("award", "")))]
        facts = [(a, b) for a, b in facts if b]
        if not p.get("built"):
            facts.insert(1, ("Built", B.todo("year")))
        fx = "".join(f"<div><dt class='label'>{a}</dt><dd>{b}</dd></div>" for a, b in facts)
        story = "".join(f"<p>{e(t)}</p>" for t in p["paras"]) or f"<p>{B.todo('more about this project')}</p>"
        blocks = ""
        # the real floor plan, where they published one
        if slug == "tranmere":
            pl = B.photo(slug, "/images/pr_tranmere/image-6.jpg")
            blocks += f"""
<section class="section on-light plan" aria-labelledby="plan-title">
  <div class="wrap">
    <div class="section-head" data-reveal><p class="label">{BEAM}The plan</p><h2 class="h2" id="plan-title">Old house in front, new rooms behind.</h2></div>
    <figure class="plan-sheet" data-draw><a href="{pl['src']}" data-zoom>{B.img(pl)}</a><figcaption class="label">The floor plan as published with the project</figcaption></figure>
  </div>
</section>"""
        if ph["pair"]:
            pr = ph["pair"]
            blocks += f"""
<section class="section on-light" aria-labelledby="pair-title">
  <div class="wrap">
    <div class="section-head" data-reveal><p class="label">{BEAM}{pr['earlier_label']} and after</p><h2 class="h2" id="pair-title">The same view, {('before work began' if pr['earlier_label'] == 'Before' else 'part way through')} and finished.</h2></div>
    {B.pair_block(slug, pr['earlier'], pr['finished'], pr['earlier_label'], 'Both photographs are from this project.')}
  </div>
</section>"""
        if ph["stages"]:
            groups, seen = "", []
            for f in ph["stages"]:
                s = B.photo(slug, f)["stage"] or "site"
                if s not in seen:
                    seen.append(s)
            for gi, s in enumerate(seen):
                shots = "".join(f'<a class="shot" href="{x["src"]}" data-zoom data-reveal style="--i:{j}">{B.img(x, small=True, sizes="(min-width: 900px) 28vw, 80vw")}</a>' for j, x in enumerate(B.photo(slug, f) for f in ph["stages"] if (B.photo(slug, f)["stage"] or "site") == s))
                groups += f"""
      <li class="stage">
        <div class="stage-mark" data-reveal><span class="label">Stage 0{gi + 1}</span><h3 class="h3">{B.STAGE_NAMES[s]}</h3></div>
        <div class="stage-shots">{shots}</div>
      </li>"""
            blocks += f"""
<section class="section dark build" aria-labelledby="build-title">
  <div class="wrap">
    <div class="section-head" data-reveal><p class="label">{BEAM}The build</p><h2 class="h2" id="build-title">How it went up.</h2><p class="lede">Photographs taken on site during the job, in order.</p></div>
    <ol class="stages-rail" data-rail>{groups}
    </ol>
  </div>
</section>"""
        if ph["order"]:
            g = "".join(f'<a class="shot" href="{x["src"]}" data-zoom data-reveal style="--i:{j % 3}">{B.img(x, small=True, sizes="(min-width: 900px) 31vw, 48vw")}</a>' for j, x in enumerate(B.photo(slug, f) for f in ph["order"]))
            blocks += f"""
<section class="section on-light" aria-labelledby="gallery-title">
  <div class="wrap">
    <div class="section-head" data-reveal><p class="label">{BEAM}Finished</p><h2 class="h2" id="gallery-title">The result.</h2><p class="lede">{len(ph['order'])} photographs. Select one to see it full screen.</p></div>
    <div class="gallery">{g}</div>
  </div>
</section>"""
        else:
            blocks += f"""
<section class="section on-light"><div class="wrap"><p class="lede">{B.todo('photographs of the finished work. The current site shows this project only before and during the build.')}</p></div></section>"""
        if p.get("video"):
            blocks += f"""
<section class="section on-light slim"><div class="wrap"><a class="btn btn--line" href="https://www.youtube.com/watch?v={p['video']}" rel="noopener">Take the video tour on YouTube {ARROW}</a></div></section>"""
        if p.get("testimonial"):
            blocks += B.payneham_quote()
        nx = P[(idx + 1) % len(P)]
        nph = B.hero_of(nx["slug"])
        blocks += f"""
<section class="next dark" aria-label="Next project">
  <a href="/projects/{nx['slug']}">
    <span class="next-text"><span class="label">Next project</span><b class="h2">{e(nx.get('short') or nx['name'])}</b><span class="label">{e(nx['type'])}</span></span>
    <span class="next-photo">{B.img(nph, small=True, sizes="(min-width: 900px) 30vw, 100vw")}</span>
  </a>
</section>"""
        body = f"""
<section class="p-hero">
  <div class="p-hero-text">
    <nav class="crumbs label" aria-label="Breadcrumb"><a href="/projects">Projects</a> <span aria-hidden="true">/</span> <span>{CATS[p['cat']]}</span></nav>
    <p class="label kick">{BEAM}{e(p['type'])}</p>
    <h1 class="shout">{e(p['name'])}</h1>
    <p class="lede">{e(p['lede'])}</p>
  </div>
  <figure class="p-hero-photo"><a href="{hp['src']}" data-zoom>{B.img(hp, lazy=False)}</a></figure>
</section>
<section class="p-facts dark" aria-label="Project facts"><div class="wrap"><dl>{fx}</dl></div></section>
<section class="section on-light story">
  <div class="wrap story-grid">
    <h2 class="h3" data-reveal>What we did</h2>
    <div class="prose" data-reveal>{story}</div>
  </div>
</section>""" + blocks + B.cta("Planning something like this?", "Tell us about it, or call Peter. We will arrange a time to meet, on site where we can.", {"new": "new-home", "reno": "renovation", "dev": "development", "com": "commercial"}[p["cat"]])
        ld = [B.crumb_ld([("/", "Home"), ("/projects", "Projects"), (f"/projects/{slug}", p["name"])]),
              {"@type": "CreativeWork", "name": f"{p['name']}: {p['type']}", "description": p["lede"], "url": f"{B.SITE}/projects/{slug}", "creator": {"@id": B.SITE + "/#business"},
               "image": [B.SITE + B.photo(slug, f)["src"] for f in ([ph["hero"]] + ph["order"][:3])], "locationCreated": {"@type": "Place", "name": p["name"] + ", South Australia"}}]
        pre = f'\n<link rel="preload" as="image" href="{hp["src"]}" fetchpriority="high">'
        doc(f"/projects/{slug}", f"projects/{slug}.html", f"{p['name']}: {p['type'].lower()} | Epic Building Group", p["lede"], body, current="/projects", ld=ld, preload=pre)

    # ---------------- Services ----------------
    secs = ""
    for i, s in enumerate(SERVICES):
        egs = "\n      ".join(B.card(BY[x], j) for j, x in enumerate(s["egs"]))
        secs += f"""
<section class="section {'on-light' if i % 2 == 0 else 'dark'} svc" id="{s['id']}" aria-labelledby="{s['id']}-t">
  <div class="wrap">
    <div class="svc-head" data-reveal>
      <p class="label">{BEAM}Service 0{i + 1}</p>
      <h2 class="h2" id="{s['id']}-t">{s['name']}</h2>
      <div class="prose">{''.join(f'<p>{e(t)}</p>' for t in s['text'])}</div>
      <a class="btn" href="/contact?type={s['type']}">Talk to us about {s['name'].lower()} {ARROW}</a>
    </div>
    <p class="label eg" data-reveal>Jobs like this</p>
    <div class="cards">
      {egs}
    </div>
  </div>
</section>"""
    also = "".join(f"<li data-reveal><b>{a}</b><span>{e(b)}</span></li>" for a, b in ALSO)
    jump = "".join(f'<li><a href="#{s["id"]}">{s["name"]}</a></li>' for s in SERVICES)
    body = B.page_head("Services", "What we build.", "We specialise in all aspects of residential and commercial construction, with a full time team of 14 and regular preferred contractors and suppliers.") + f"""
<nav class="jump dark" aria-label="Services on this page"><div class="wrap"><ul>{jump}</ul></div></nav>
{secs}
<section class="section dark also" aria-labelledby="also-t">
  <div class="wrap">
    <div class="section-head" data-reveal><p class="label">{BEAM}Also</p><h2 class="h2" id="also-t">In-house trades and management.</h2></div>
    <ul class="also-list">{also}</ul>
  </div>
</section>
""" + B.cta()
    doc("/services", "services.html", "Services | Epic Building Group, Master Builders Adelaide",
        "Renovations and extensions, kitchens and bathrooms, new homes, residential developments and commercial construction and fit outs in Adelaide.", body, current="/services",
        ld=[B.crumb_ld([("/", "Home"), ("/services", "Services")])] + [{"@type": "Service", "name": s["name"], "provider": {"@id": B.SITE + "/#business"}, "areaServed": "Adelaide", "description": s["text"][0]} for s in SERVICES])

    # ---------------- Process ----------------
    rail = ""
    for i, (name, head, paras, gap) in enumerate(STAGES):
        meet = ""
        if name == "Build":
            ticks = "".join(f'<i style="--i:{k}"></i>' for k in range(8))
            meet = f'<div class="meetings" aria-hidden="true"><span class="label">Site meetings</span><div class="ticks">{ticks}</div></div><p class="vh">Site meetings run through the whole of the build stage.</p>'
        g = f"<p>{B.todo(gap)}</p>" if gap else ""
        rail += f"""
      <li class="proc" data-stage>
        <div class="proc-n"><span class="shout">0{i + 1}</span></div>
        <div class="proc-body">
          <p class="label">{name}</p>
          <h2 class="h3">{head}</h2>
          {''.join(f'<p>{e(t)}</p>' for t in paras)}
          {meet}{g}
        </div>
      </li>"""
    body = B.page_head("Process", "How a build runs.", "From the first conversation to the keys. The same five stages for an ensuite or a row of townhouses, with a Master Builder on site through all of it.") + f"""
<section class="section on-light" aria-label="The five stages">
  <div class="wrap">
    <ol class="proc-rail" data-rail>{rail}
    </ol>
  </div>
</section>
<section class="section dark" aria-labelledby="said-t">
  <div class="wrap">
    <p class="label" data-reveal>{BEAM}What a client said about it</p>
    <blockquote class="pull" data-reveal><p id="said-t">&ldquo;Peter provided us with his valued opinion, at every stage of the build, providing us with the flexibility to make changes, to ensure we were 100% satisfied with the outcome.&rdquo;</p><footer><b>Owner</b> <span class="label">Payneham new build</span></footer></blockquote>
  </div>
</section>
""" + B.cta("Ready to start at stage one?", "The first conversation costs nothing. Tell us what you are planning, or call Peter.")
    doc("/process", "process.html", "Our process | Epic Building Group, Adelaide", "How Epic Building Group runs a project: consultation, design, approvals, build and handover, with regular on site meetings.", body, current="/process", ld=[B.crumb_ld([("/", "Home"), ("/process", "Process")])])

    # ---------------- About ----------------
    roles = "".join(f"<li data-reveal style='--i:{i % 4}'>{r}</li>" for i, r in enumerate(["Master Builders", "Project Managers", "Civil Contractors", "Carpentry Division", "Architectural Design Team", "In-House Interior Designer", "General Labourers"]))
    body = B.page_head("About", "Real Master Builders.", "Epic Building Group is a second generation building company. Our clients deal with traditional builders who have regular on site meetings and a hands on approach, to keep a project on schedule and budget.") + f"""
<section class="record" aria-label="Epic Building Group at a glance">
  <div class="wrap">
    <ul>
      <li data-reveal><b>GL185386</b><span class="label">Builder's licence</span><small>Also GL/SGL56932</small></li>
      <li data-reveal style="--i:1"><b>2011</b><span class="label">Master Builders SA award</span><small>Best Renovation, up to $600,000</small></li>
      <li data-reveal style="--i:2"><b>14</b><span class="label">Full time team</span><small>Plus preferred contractors</small></li>
      <li data-reveal style="--i:3"><b>25+</b><span class="label">Years of projects</span><small>Across Adelaide</small></li>
      <li data-reveal style="--i:4"><b>2nd</b><span class="label">Generation</span><small>A family building company</small></li>
    </ul>
  </div>
</section>
<section class="section on-light">
  <div class="wrap two">
    <div data-reveal><p class="label">{BEAM}Proven results</p><h2 class="h2">On time, within budget, to specification.</h2></div>
    <div class="prose" data-reveal>
      <p>Our gallery of ongoing and completed projects reflects our results. They show innovation in construction methods and materials, and excellent product knowledge. Our primary goal is to produce a quality result, delivered on time and within budget, while meeting all construction specifications.</p>
      <p>Through realistic quoting, estimating, scheduling and construction times, and by taking the client's wishes into consideration throughout the entire process, we believe we can meet and exceed our clients' expectations.</p>
      <p><a class="btn btn--line" href="/projects">See the projects {ARROW}</a></p>
    </div>
  </div>
</section>
<section class="section dark">
  <div class="wrap two">
    <div data-reveal><p class="label">{BEAM}Quality and flexibility</p><h2 class="h2">From your drawings, or from the first sketch.</h2></div>
    <div class="prose" data-reveal>
      <p>We can work from architectural drawings, or we can be involved from the initial design and planning stage, through approval to construction and completion.</p>
      <p>We are able to marry the new building to existing buildings and surroundings, and can work in a heritage environment, as can be seen in our range of projects.</p>
      <p>To produce one off designs of the highest quality, we explore all options up front with our clients to precisely define the specifications. We then choose the most appropriate materials and construction methods, and select from our highly skilled staff and subcontractors.</p>
    </div>
  </div>
</section>
<section class="section on-light team" aria-labelledby="team-t">
  <div class="wrap">
    <div class="section-head" data-reveal><p class="label">{BEAM}The team</p><h2 class="h2" id="team-t">A full time team of 14.</h2><p class="lede">Led by Peter Tsoukalas, with regular preferred contractors and suppliers where required.</p></div>
    <ul class="roles">{roles}</ul>
    <p class="lede" data-reveal>{B.todo("names, roles and portraits of the team, starting with Peter")}</p>
  </div>
</section>
<section class="section dark" aria-labelledby="award-t">
  <div class="wrap two">
    <div data-reveal><p class="label">{BEAM}Recognition</p><h2 class="h2" id="award-t">Best Renovation, 2011.</h2></div>
    <div class="prose" data-reveal>
      <p>In recognition of our high standard of quality, we were awarded Best Renovation, in the category for renovations up to $600,000, by the Master Builders Association of South Australia in 2011.</p>
      <p><a class="btn btn--line" href="/projects/parkside">See the Parkside renovation {ARROW}</a></p>
    </div>
  </div>
</section>
<section class="quote section" aria-labelledby="z-t">
  <div class="wrap">
    <p class="label" data-reveal id="z-t">{BEAM}Client testimonial</p>
    <figure data-reveal>
      <blockquote>
        <p class="quote-lead">Your work ethic, punctuality and attention to detail was amazing. All the guys that worked with/for you were also exceptional and had the same drive and passion as you.</p>
        <details class="more"><summary><span>Read the whole letter</span>{ARROW}</summary><div class="more-body"><p>&ldquo;{e(B.ZOITAKIS)}&rdquo;</p></div></details>
      </blockquote>
      <figcaption><b>Andrew Zoitakis</b><span class="label">Extension, Westbourne Park</span></figcaption>
    </figure>
  </div>
</section>
""" + B.cta()
    doc("/about", "about.html", "About | Epic Building Group, second generation Master Builders", "Epic Building Group is a second generation Adelaide building company with a full time team of 14, led by Peter Tsoukalas.", body, current="/about",
        ld=[B.crumb_ld([("/", "Home"), ("/about", "About")]), B.BUSINESS])

    # ---------------- Contact ----------------
    types = "".join(f'<label class="chip"><input type="radio" name="type" value="{k}" data-q="{e(q)}" required><span>{lab}</span></label>' for k, (lab, q) in QUESTIONS.items())
    body = f"""
<section class="contact">
  <div class="wrap contact-grid">
    <div class="contact-side">
      <p class="label kick">{BEAM}Contact</p>
      <h1 class="shout">Start a project conversation.</h1>
      <p class="lede">Three short steps. Or skip the form and call: Peter answers his own phone.</p>
      <ul class="contact-list">
        <li><span class="label">Enquiries</span><a class="tel big" href="tel:+61411510558">Peter 0411 510 558</a></li>
        <li><span class="label">Office</span><a class="tel" href="tel:+61881520948">08 8152 0948</a></li>
        <li><span class="label">Email</span><a href="mailto:contact@epicbuildinggroup.com.au">contact@epicbuildinggroup.com.au</a></li>
        <li><span class="label">Office address</span>220 Richmond Rd, Marleston SA 5033</li>
        <li><span class="label">Post</span>PO Box 301, Marleston SA 5033</li>
        <li><span class="label">Builder's licence</span>GL185386 GL/SGL56932</li>
      </ul>
    </div>

    <!-- The enquiry form. It validates and shows its success state, but sends nowhere yet.
         HOOK: epic.js, function sendEnquiry(data). Post `data` as JSON to the real endpoint there
         and resolve only when the enquiry has been received. -->
    <form class="form on-light" id="enquiry" novalidate aria-labelledby="form-title">
      <div class="form-top">
        <h2 class="h3" id="form-title">Tell us about the project</h2>
        <ol class="form-steps" aria-hidden="true"><li class="is-on">Project</li><li>Details</li><li>You</li></ol>
        <p class="form-count label" aria-live="polite"></p>
      </div>

      <fieldset class="step" data-step>
        <legend>What are you planning?</legend>
        <div class="chips">{types}</div>
        <p class="err" data-err="type" hidden>Choose the closest fit.</p>
      </fieldset>

      <fieldset class="step" data-step>
        <legend>About the project</legend>
        <label class="field field--wide"><span id="q-label">Tell us a little about it</span>
          <textarea name="answer" rows="3" required aria-describedby="q-hint"></textarea>
          <small id="q-hint">A sentence or two is plenty.</small>
          <span class="err" hidden>Add a sentence or two so we know where to start.</span></label>
        <label class="field"><span>Suburb of the project</span><input type="text" name="suburb" autocomplete="address-level2" required><span class="err" hidden>Add the suburb.</span></label>
        <label class="field"><span>How far along are you?</span>
          <select name="stage" required>
            <option value="">Choose one</option>
            <option>Just an idea</option>
            <option>I have a sketch or concept</option>
            <option>I have drawings</option>
            <option>I have approval</option>
          </select><span class="err" hidden>Choose the closest.</span></label>
      </fieldset>

      <fieldset class="step" data-step>
        <legend>How do we reach you?</legend>
        <label class="field"><span>Your name</span><input type="text" name="name" autocomplete="name" required><span class="err" hidden>Add your name.</span></label>
        <label class="field"><span>Phone</span><input type="tel" name="phone" autocomplete="tel" inputmode="tel" required pattern="[0-9 +]{{8,16}}"><span class="err" hidden>Add a phone number we can call, digits only.</span></label>
        <label class="field field--wide"><span>Email <em>(optional)</em></span><input type="email" name="email" autocomplete="email"><span class="err" hidden>That email address does not look right.</span></label>
      </fieldset>

      <div class="form-nav">
        <button class="btn btn--line" type="button" data-back hidden>Back</button>
        <button class="btn" type="button" data-next>Next {ARROW}</button>
        <button class="btn" type="submit" data-send>Send to Peter {ARROW}</button>
      </div>
      <p class="form-fail" role="alert" hidden>That did not send. Please call Peter on <a class="tel" href="tel:+61411510558">0411 510 558</a>.</p>
      <noscript><p class="form-fail">This form needs JavaScript to send. Please call Peter on 0411 510 558 or email contact@epicbuildinggroup.com.au.</p></noscript>

      <div class="form-done" role="status" tabindex="-1" hidden>
        {BEAM}
        <h2 class="h2">Thank you<span data-done-name></span>.</h2>
        <p class="lede">Your enquiry is ready for Peter. He will call you on <b data-done-phone></b>.</p>
        <p class="demo-note">{B.todo("this demo does not send anything yet. The real site will post to Peter here.")}</p>
        <a class="btn btn--line" href="/projects">Look through the projects {ARROW}</a>
      </div>
    </form>
  </div>
</section>
"""
    doc("/contact", "contact.html", "Contact | Epic Building Group, Marleston SA", "Start a project conversation with Epic Building Group. Call Peter on 0411 510 558 or send a short enquiry.", body, current="/contact",
        ld=[B.crumb_ld([("/", "Home"), ("/contact", "Contact")]), B.BUSINESS])

    # ---------------- 404 ----------------
    body = B.page_head("Page not found", "Nothing built here.", "That page does not exist, or has moved.") + f"""
<section class="section on-light"><div class="wrap"><div class="hero-actions"><a class="btn" href="/projects">See the projects {ARROW}</a><a class="btn btn--line" href="/">Back to the homepage</a></div></div></section>"""
    doc("/404", "404.html", "Page not found | Epic Building Group", "That page does not exist.", body)
    return n
