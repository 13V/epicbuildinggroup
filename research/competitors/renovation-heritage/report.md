# Renovation, extension and heritage-home builders: website research

Date: 11 November 2026. Method: WebSearch to find candidates, then Playwright (Chromium) at 1440x900 and 390x844 phone. I looked at screenshots and read each page's DOM. Anything I did not see is marked "uncertain". Search results were thin (mostly award lists and directories), so I found most candidates by checking likely domains. Nothing was submitted or contacted.

Note on coverage: I opened 10 sites. Several known builders (Thomasz, Soutter Built, Technique Construction Group, Visioneer, Modify Homes, Ryan Jones) did not load through the proxy and were skipped. Awwwards-style winners in this niche did not turn up: the genuinely strong sites in this segment are mostly modest WordPress builds, not showpieces.

## The four sites kept (screenshots in this folder)

### BEST 1. Fortem Projects (Melbourne, Oakleigh South), https://www.fortemprojects.com/
Period renovations and architect-designed new homes. Winner, 2025 HIA Victorian Renovation/Addition $2-5m (stated on the home page).

**First screen**
- Desktop: headline "BUILDING A UNITED VISION" (second half in yellow), subline "We partner with owners and architects to build award-winning homes in Melbourne's finest suburbs." then "Winner of the 2025 HIA Victorian Renovation/Addition Project $2-5 million". Full-bleed photo of a curved Edwardian facade under a dark overlay (a video element exists in the DOM, so the hero may be a looping video; the still I captured showed the facade). The only button is a boxed "Contact" in the top right. No call to action in the hero itself.
- Phone: a different hero image (modern two-storey extension), same headline and awards line, hamburger menu, no button, no phone number.

**Projects**
- Index: "FEATURED PROJECTS", 16 projects as large image tiles with only a one-word name (Surrey, The Pines, Lewisham, Quamby...). No suburb or scope on the tile.
- Project page (Surrey): full-screen photo hero with the name and "Location South Yarra / Type Renovations". Then a client-style quote credited to the architect ("Careful collaboration with the building team was required to reinstate period features..." Sarah Bryant, Bryant Alsop Architects), two paragraphs of scope (Victorian terrace, narrow site, strict heritage constraints, reinstated plasterwork, staircase and tessellated tiles, two-storey rear addition, steel-framed bay window, lift) and an "In collaboration with" credit. About 26 images on the page, no plans, no before/after, no duration or cost. Some projects (Quamby) are a Vimeo film page.
- Renovations service page (3,400 characters): "A passion for preservation", then labelled blocks for Cost planning (Early Builder Involvement, preliminary estimates, fixed price or cost-plus), Project planning (limited projects per year, strict construction sequence, help obtaining permits for a period renovation) and In-house carpenters.

**Trust**
- Awards page lists HIA wins (2025, 2024 twice), Master Builders Victoria nominations and finalist entries, each linking to a project.
- Team page: directors Chris Curtain and Stuart McFarland, "over 50 years of experience between them", in-house carpenters.
- Testimonials page with several long quotes (one describes a "tired double fronted Victorian" turned into a gallery home); I did not count them. Attribution style not verified.
- No builder licence number seen in the footer (footer reads copyright and agency credits only). Process explained only as the planning blocks above, not as numbered stages.

**Enquiry path**
- Contact button top right, page "The vision starts here". Says "we only take on a select number of projects at any time". Names the director to call.
- Form fields: first name, last name, email, phone, "What best describes your enquiry?" (select: thinking of renovating but don't know where to start / ready to start design and need guidance / have a design concept and want to talk buildability (time and costs) / have detailed plans and want to talk buildability / other), postcode, message. Cloudflare Turnstile check. The enquiry-stage select is a good qualifier.
- Phone number is in the footer and on the contact page only. Not in the header, nothing sticky on mobile.

**Motion and interaction**
- GSAP, ScrollTrigger and Swiper are loaded (checked in the DOM). Visible effects: content fades in on scroll, split image/text panels, bouncing scroll chevrons. In my screenshots the page background rendered a flat mid-grey, which may be a fade-in still in progress (uncertain). It reads as restrained and helps pacing; it is decoration more than information.

**Weaknesses**
- Hero has no call to action and no phone number. Project tiles carry no facts. No before/after anywhere I saw. No licence number visible. Body text is small (13px base) and light grey on mid-grey, low contrast on desktop and phone. Project pages carry no duration, cost band or process story.

### BEST 2. Period Extensions & Designs (Melbourne, Camberwell), https://www.periodextensions.com.au/
Extensions and renovations to Victorian, Edwardian, Federation and post-war homes, in-house design plus build, est. 2002.

**First screen**
- Desktop: headline "Award-Winning Home Extensions & Renovations Across Melbourne" over a bright photo of a new rear living space; buttons "DOWNLOAD BROCHURE" and "FREE CONSULTATION". Black header carries the phone number (03) 9882 5255 prominently. Under the hero a five-item trust strip: Award-Winning Builder, In-House design & Architecture, 20+ years heritage expertise, Fixed price no surprises, Free Consultation.
- Phone: same headline and both buttons, phone number top left, and a sticky bottom bar "CALL NOW" / "FREE CONSULT" (confirmed fixed-position in the DOM).

**Projects**
- Index: grid of projects, each tile showing suburb, era ("Victorian Terrace", "Edwardian Home", "Post War") and scope ("Upper Storey Extension + Full Home Renovation + New Pavilion"). This is the best project-tile labelling I saw.
- Project page (Toorak): hero, a brief paragraph by paragraph story (the brief, the old hallway with cornices, the new open-plan kitchen, a fireplace discovered behind plasterboard and restored), a gallery, then a labelled "Before And after" section built from paired images (before-1/after-1 to before-3/after-3; how the pairs are displayed, slider or static, not verified). About 33 images, about 6,000 characters of text. No duration or cost shown; location appears only as the suburb name.
- 55+ suburb and house-style pages exist (areas, "Californian Bungalow", "Double fronted homes", "Heritage Homes" etc.), which is an SEO structure.

**Trust**
- Footer states ABN, HIA membership number (516961) and BPC registration (DB-U 52952): the clearest licence disclosure of any site I opened.
- Awards section on About, Reviews page headed "EXCELLENT, Based on 22 reviews" with named reviewers and "8 months ago" style dates, a Houzz link, a free "Home Renovation Transformations" magazine download.
- Process: "How We Work", "Our 8 Step Process to Bring Your Extension to Life": 01 Let's unlock your home's potential (designer consult), 02 design consult and quote, 03 Documentation (soil test, engineering, working drawings, town planning, interior design), 04 The contract (HIA contract), 05 Building permit (done in-house), 06 Building works commence (site supervisor, in-house carpenters), 07 Completion (handover, walk-through), 08 The service doesn't stop there (3-month maintenance period plus a 12-month extra period). Presented as a numbered circular infographic with short paragraphs; the paragraph text is small and tight, but the staging is genuinely clear.
- Team: not examined in detail.

**Enquiry path**
- Phone in header on every page, sticky call/consult bar on mobile, "Free consultation" and "Download brochure" in the hero, a form at the foot of every page.
- Form fields: name, email, phone, location, "How did you hear about us" (select with 12 options including Site Sign, Car Signage), message. reCAPTCHA. No budget or stage question.

**Motion and interaction**
- jQuery only; no GSAP or Lenis. Hover overlays on project tiles, sticky header that shrinks, back-to-top button. Little motion, and nothing gets in the way.

**Weaknesses**
- Dated look in places (small-caps serif headings throughout, stock-style icons, heavy header). Process infographic has tiny text. Page is very long (about 10,000px on the home page) with a very large footer link list. Mobile text sizes are small. No duration or cost facts on project pages.

### BEST 3. Kitchen & Bath Co. (Melbourne), https://kitchenandbath.com.au/
Kitchen, bathroom, laundry, full-home and extension renovations. Included for the segment's kitchen/bath end and for its enquiry design.

**First screen**
- Desktop: split layout, headline "Melbourne's Trusted Kitchen & Bathroom Renovation Specialists", a short line ("Over 25 years of experience transforming Melbourne homes"), buttons "BOOK CONSULTATION" and "GET A COST ESTIMATE", photo of a finished kitchen on the right. Trust strip under it: 5-Star Google Rating, VBA Registered Building Practitioner, Featured in a magazine, 25 Years Experience, 10-Year Builders Warranty. Header has "BOOK CONSULTATION" and a round phone icon button.
- Phone: headline, then the kitchen photo, then paragraph, then black buttons (the first is cut off below the fold at 844px). The phone icon button is not in the phone header (hamburger only); a phone number sits further down the page. A phone number is not above the fold.

**Projects**
- Index: 25+ projects listed with suburb, scope ("Carlton, Kitchen, Bath & Laundry Renovation"; "Thornbury, Full Home Renovation & Extension") and "VIEW PROJECT".
- Project page (Thornbury): large 2-column photo gallery (about 18 images) plus a short fact block: Location, **Duration "8 Weeks"**, Key features ("Cabinetry, Flooring, Bathtub, Tiling & Tapware"). Duration on each project is a good idea. No story, no before/after, no cost. Closes with "Book In-Home Consultation" and "Download Free Renovation Guide".

**Trust and process**
- Home page "How We Work With You": Personalised design, Transparent Process ("From your first consultation to final walkthrough... detailed project timelines, clear communication, honest budgeting"), and a third point. This is a benefits list, not staged steps.
- Contact page carries 3 named testimonials (first name + initial, suburb), an FAQ, VBA registration claim, 10-year warranty claim. Licence number not seen (uncertain).

**Enquiry path**
- Best form of the sites I looked at. Fields: first name, last name, email, phone, suburb, "I'm interested in" (Kitchen, Bathroom, Laundry, Full Home, Extension, Interior Design, tap to select), **estimated budget range** (Below $25k up to $300k+, Not sure yet), **project stage** (Just exploring / Actively researching / Ready to start soon / Ready to start now), how did you hear, **file upload for photos and plans**, "BOOK FREE CONSULTATION". Phone 1300 255 234 with hours (Mon-Fri 8am-5pm) beside the form. Two calls to action in the hero (consultation versus cost estimate) give a low-commitment path.

**Motion and interaction**
- WordPress/Elementor with Swiper and jQuery. Essentially static; no scroll tricks. Fast and legible.

**Weaknesses**
- Template-feeling; no before/after; thin project pages for a premium audience; light-grey body text is low contrast; not heritage-specific (Melbourne reno generalist). Budget-first form is a lead filter that can deter some enquirers (judgement, not verified).

### WORST. SAS Builders (Melbourne, Taylors Hill), https://sasbuilders.com.au/
Large-scale industrial/commercial and residential developer. **Off-segment** (warehouses and factories, not renovations); I include it only as an example of what to avoid, since no genuinely renovation-focused site I opened was worse. Note this when weighing the verdict.

- **First screen:** header with phone, address, hours; a blurred-split carousel of a warehouse project card ("COMPLETE, 89 Elm Park Drive, Hoppers Crossing, Warehouse, Factory & Industrial") with "View More". Below it: "Looking for a quality and affordable constructor for your next project?" with "Contact Us" and "CHECK OUR PROJECTS". No headline stating who they are.
- **Phone:** header block of phone, address and hours takes the first screen before any content; carousel is a small slice. The phone number is plain text, not a tap-to-call link (no `tel:` link found). A "LIVE CHAT" bubble overlaps the buttons.
- **Projects:** tabs by street address; a wall of 12+ site-progress snapshots with little editing (concrete aprons, blue sky). No story, scope, duration, architect.
- **Trust:** generic "Why Choose SAS Builders" copy ("Expertise and Experience", "Comprehensive Services"), no licence number seen, no testimonials or awards seen. No process.
- **Enquiry:** form with name, email, subject, message only; generic.
- **Motion:** auto-rotating carousel; an old WordPress theme look (gradients, drop-shadows, dark-grey).
- **Weaknesses:** nothing says what they do or for whom; low-grade photography; no human faces; no tap-to-call; heavy dark grey with small low-contrast grey text.

## Other sites opened (not kept)

| Site | City | Verdict |
|---|---|---|
| Fortem Projects, fortemprojects.com | Melbourne | Best for heritage tone and awards; project tiles bare, no CTA in hero. Kept. |
| Period Extensions & Designs, periodextensions.com.au | Melbourne | Best explained process (8 steps), clearest licence block, mobile sticky call bar, before/after on project pages. Kept. |
| Kitchen & Bath Co., kitchenandbath.com.au | Melbourne | Best enquiry design (stage, budget, upload); clean and fast; thin project pages. Kept. |
| SAS Builders, sasbuilders.com.au | Melbourne | Off-segment, dated, no clear message, no tap-to-call. Kept as worst. |
| Cumberland Building, cumberlandbuilding.com.au | Sydney | Strongest photography and heritage project write-ups (Millers Point colonial building, Woollahra, Darling Point) on a clean Framer site; shows Builders Lic No. 84913C and an iCIRT 4.5 star rating; but there is no enquiry form at all (phone and email only), project pages have no scope facts beyond architect, and the hero is a full-height photo with no headline or button. Runner-up. |
| Humphrey Homes, humphreyhomes.com.au | Perth | Architects + builders; bold black sans-serif type, full-width video hero, "Let's talk" pill. Hero has no real headline until you scroll; project grid images had not loaded at scroll (lazy-loaded, blank panels in my capture). Awards/testimonials/open-house pages exist. Not examined further. |
| Hedger Constructions, hedgerconstructions.com.au | Melbourne | Custom luxury homes, not renovation. Video hero "Building with Distinction", GSAP and Swiper, a vertical "BOOK A CONSULT" side tab, 20 portfolio items split by country, coastal, city. Polished but new-build. |
| Inside and Out Builders, insideandoutgroup.com.au | Melbourne | Squarespace; "INSIDE AND OUT BUILDERS / YOUR FOREVER HOME, BUILT AROUND YOU", "PROJECT ENQUIRY" and phone number as hero buttons (good), but a tiny logo, a black announcement bar and generic copy. Competent, forgettable. |
| Garth Chapman Traditional Queenslanders, traditionalqueenslanders.com.au | Brisbane | New traditional-style homes, not renovation. Dark green nav, small-caps serif, carousel with pause button, "7 THINGS YOU MUST KNOW" banner. Cohesive for its audience, but dated and a project-home catalogue. |
| Renotech Building, renotechbuilding.com.au | Sydney (Bronte) | Wix site; hero is an embedded video thumbnail with a play button, no headline; navigation "Our Work" points back to the home page. Thin. |
| Manteena, manteena.com.au | Canberra | Loaded, not examined (outside priority). |

Not loaded through the proxy (so unreviewed): Thomasz Design & Construction, Technique Construction Group, Visioneer Builders, Soutter Built, Modify Homes, Ryan Jones Building, constructmelbourne.com.au (Squarespace site expired).

## Patterns the best share
1. A hero that states the specialism in one line and carries an award or credential right beside it (Fortem "Winner of the 2025 HIA..."; Period "Award-Winning" plus a five-point strip).
2. Real photography of finished homes, large, with period facades next to new rear additions (the heritage-meets-contemporary contrast is the story).
3. Project tiles that say suburb, era and scope (Period) or suburb and scope (Kitchen & Bath Co.), not just a name. Duration on the project page (Kitchen & Bath Co.: "8 Weeks") is a rare, useful fact.
4. A short project narrative naming what was kept (cornices, fireplace, plasterwork, staircase) and what was added, credited to the architect (Fortem, Cumberland, Period).
5. Credentials shown as numbers: HIA number, BPC registration, VBA registered, builder licence (Period footer, Cumberland footer, K&B strip).
6. Process stated in stages (Period's eight steps with named contract, permit, 3-month plus 12-month maintenance) or at least a planning approach (Fortem cost planning, project planning, in-house carpenters).
7. Enquiry forms that ask what stage the client is at (Fortem's "thinking of renovating... have detailed plans", K&B's project stage and budget) and two ways in: call and a low-commitment consult.
8. Phone number in the header and a sticky call bar on mobile (Period). Motion is restrained: fade-ins, hover overlays, nothing that hijacks scroll.

## What none of them do well
1. Before and after. Only Period shows it, as paired images at the foot of a project page; none uses it as a headline proof, and none shows the stages between (demolition, structure, lock-up, fit-out) with dates. A heritage builder could tell "what we found and what we kept" with photos.
2. Showing the process as a visual, staged story with real timeframes. Period's eight steps are the best and still a small-text infographic with no durations per stage; Fortem has no stage list; K&B only gives benefits.
3. Project pages with hard facts: suburb, house era, scope, duration, architect, size, cost band, and heritage approval type together. Each site gives one or two, none gives all.
4. Heritage competence made explicit: how heritage overlays, council and permit approval are handled, what is conserved versus replaced. Fortem mentions "understand the required building approvals" in one sentence; nobody explains it.
5. Phone-first usability and legibility: body text 12 to 15px, grey on grey, hero CTAs missing on phone (Fortem, Cumberland), phone numbers buried (Fortem, K&B on mobile).
