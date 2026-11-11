# Builders who do homes and commercial: competitor review

Segment: boutique residential developers and design-and-construct builders, and small-to-mid commercial builders (hospitality fit-outs, adaptive reuse, retail), with attention to builders who present BOTH homes and commercial on one site.
Date: 11 Nov 2026. Method: Playwright Chromium, 1440x900 desktop and 390x844 phone, screenshots viewed, DOM inspected. Nothing submitted.

Honest note on the field: search surfaced few strong, genuinely mixed-use boutique builders. Several candidate domains failed to load or blocked automated access (mancini made, BTI, Melegant, Pamment, Lifestyle Building, Cobild returned 502/403/no connection). Built.com.au served a Cloudflare challenge. RC Construction turned out to be civil/concrete work, so it is out of segment.

Chosen: BEST = Helix Group, SQ Projects, Hamilton Group. WORST = Synergize Constructions.
Screenshots kept in this folder as `<slug>-desktop-first / phone-first / desktop-scroll-2 / project / contact.jpg` (slugs: helix, sq, hamilton, synergize).

---

## 1. Helix Group (BEST, and the key example for a homes-plus-commercial builder)
https://www.helix.group, Sydney NSW (Wix site).

**First screen**
- Desktop: dark-overlaid photo of a commercial office interior (still image; no `<video>` in DOM). Small line "Licensed NSW builder · Est. 2020". Headline "One Builder. Every Kind of Space." Sub: "Office and hospitality fit-outs, industrial makegoods and residential builds. Planned properly, priced transparently and handed over as promised." Buttons: outlined phone pill "0408 683 134" and white "View Projects". A stat strip sits on the hero: "29 Projects delivered", "$200K-$5M jobs from $200K to $5M", "Over 20 Five-Star Reviews", "NSW Sydney, NSW | Australia-wide". Header also has an outlined "Send your scope" button.
- Phone: same headline and copy, phone number button and View Projects side by side, hamburger menu. The hero photo is cropped to a short band (about 360px) and the stat strip is not visible in the first screen. Phone number is tappable (`tel:`) on the first screen.

**How it handles both sides (the main finding)**
- One brand line covering everything ("One Builder. Every Kind of Space.") rather than two sub-brands.
- Four services, each its own page, listed equally: Commercial Office Fit-Out, Hospitality & Retail Fit-Out, Industrial Makegoods, Residential Construction. Residential is last of four but described in the same card format ("New homes, duplexes, extensions and NDIS-related accessible home modifications").
- Portfolio is one grid with filter chips: All / Commercial Office Fit-out / Hospitality & Retail / Industrial Makegoods / Residential Construction. Residential entries are named by suburb ("Mosman Residence, Mosman, Heritage renovation", "Lidcombe Residence, Duplex", "Bronte Residence"). About 29 items, most commercial; 10 residential (counted in the filtered list: Mosman, Vaucluse, Bronte, Kellyville, Bondi, Lidcombe, Dee Why, NDIS home, Corrimal boarding house, Allambie Heights).
- Page furniture changes by sector: a residential project ends with "Considering a renovation of your own? ... Discuss Your Home" and a separate "Residential Capability Statement (PDF, 24 pages)", while commercial pages use the "Send your scope" language and a 53-page general capability statement. So each audience gets its own call to action and PDF, while the header stays shared.
- Testimonials mix both: hospitality owners (Kin Cafe, Brooklyn Boy Bagels, Cowboys Bar & Grill) alongside a duplex client in Ryde.

**Projects**
- Home page shows five recent projects as cards with type and a facts line: "Kin Cafe & Wine Bar, Hospitality fit-out, Lane Cove · $800K · 6 months"; "Bronte Residence, Renovation & extension, 410 sqm · $1.9m · 9 months".
- Project page (checked 120 Sussex Street and Bronte Residence): full-bleed hero, then a fact bar with Type / Location / Size / Value / Year / Duration (client contract value is published), then a two-paragraph description, a gallery (18 images in the page DOM), related projects, CTA. No architect named, no before/after, no plans or video seen.

**Trust**
- Licence number in the footer of every page and in the FAQ: "Lic. 386657C", ABN 30 641 549 082. FAQ has a "Licensing: Insurance & Warranties" group.
- No memberships or awards seen (company est. 2020). Testimonials page with attributed quotes by name and business ("Michael Chaffron, Director & Dough Raiser, Brooklyn Boy Bagels"); a few are name-only. Team: contact page names "Josh or Ben" who reply "within one business day". Process explained in FAQ ("Projects & Process", "Getting Started").

**Enquiry path**
- "Send your scope" in the header on every page, phone in hero, repeated CTA band ("Have a project on the table?") and a footer "Start Your Project" plus phone.
- Contact form fields: First name*, Last name, Phone*, Email*, "What type of project are you planning?" (dropdown), Project details*, Company, Project location, Estimated budget (dropdown), Target start date, File upload, consent checkbox*. Promise of a reply within one business day and "an indicative budget range". Phone and email shown beside the form. Single step, not multi-step.

**Motion and interaction**
- Wix Thunderbolt. No GSAP, Lenis, Swiper or video found. Content fades in on scroll (the phone screenshot caught project images mid-fade). "Scroll to explore" prompt on page heroes. Restrained; the motion does not get in the way. Exact animation types not individually verified.

**Weaknesses**
- Hero image is dark and generic (an office corridor); the home page opens with commercial and the residential side is thin on the first screen.
- Residential page heroes still use dark overlays that dull the photography.
- One broken link in the portfolio grid: the "Doo Doo Kids Cafe" card links to `helxix.group` (typo), seen in the DOM.
- No awards, no named architects, no before/after, little process detail beyond FAQ; very young firm.
- `/about-us` is a 404 (the real path is `/aboutus`), so a guessed URL fails.

---

## 2. SQ Projects (BEST for residential and adaptive-reuse craft)
https://www.sqprojects.com.au, Summer Hill / Balmain, Sydney. Hand-built static site, Swiper for the slider. Residential only, so it does not show the dual-sector problem, but it is the best proof-led heritage and adaptive-reuse presentation found.

**First screen**
- Desktop: white page, thin condensed "SQ PROJECTS" wordmark, small uppercase nav (Home, Projects, About, Team, Testimonials, Awards, Media, Contact), then one large photo (a timber-clad modern extension against blue sky) in a 5-dot slider. No headline, no buttons.
- Phone: wordmark, hamburger, the same slider, then the footer; the page is essentially a slideshow and a blank space. No phone number or CTA on the first screen.

**Projects**
- Index: a 3-column grid of 15 plain photos, project names only in the link text (The Cake Factory, Annandale Warehouse, Darlinghurst Terrace...). Images are strong.
- Project page (Annandale Warehouse): left column with name, suburb, a long paragraph on the story (director's own warehouse, who drew DA plans, which architect assisted, salvaged materials, what was kept), then award line "Winner of 2016 MBA Excellence in Housing Award, NSW, Adaptive re-use up to $1 million", Year 2015, Status Completed, Type "Design & Construct". Right: 15 photos in a two-column grid. No plans, no before/after, no video, no cost or duration.

**Trust**
- Awards page lists about 12 wins and nominations by category (Adaptive re-use, House Restorations & Additions, Town Houses / Dual Occupancy, Contract Houses). Testimonials page: 7 quotes, strongly attributed (architects, a property buyers' advocate who co-hosts a TV show, landscaper, clients, with firm names). Team page and Media page exist. Licence number: not seen on the pages I opened (uncertain whether it is elsewhere).

**Enquiry path**
- No form at all. Contact page: phone +61 (2) 9555 5190, two emails (general; "New build enquiries"), postal and street address, Google map. No CTA elsewhere. No `tel:` link in the DOM (the number is plain text), so it is not tap-to-call.

**Motion**: Swiper slider only; no scroll effects.

**Weaknesses**
- Phone experience is thin (slideshow plus blank space); no enquiry form, no tap-to-call, no budget or timing question, no reason to act. Copyright "2024". Descriptions and facts vary by page. Index has no captions, so you must click to learn anything.

---

## 3. Hamilton Group (BEST for adaptive reuse and developer-builder positioning)
https://www.hamilton.net.au, Geelong VIC (WordPress; Swiper and AOS loaded). Commercial only (builder, developer and landlord); no homes. Relevant for how a developer-builder shows heritage and warehouse conversion.

**First screen**
- Desktop: aerial photo of the restored Federal Mills warehouse precinct at sunset (video not detected in DOM, so treated as image), serif headline "Geelong's most exciting projects and properties." Sub: "Hamilton Group is an award-winning commercial building company specialising in construction, fitouts, property and leasing." Buttons: "Explore Projects", "View Vacancies" (teal pills). Nav: Leasing, Projects, Billboard Advertising, About, Contact Us, social icons.
- Phone: same copy and both buttons fit; then straight into "Feature vacancies". Phone number is not in the first screen (appears on the contact page and is `tel:` linked in DOM).

**Projects**
- Index has filters (Commercial Construction / Government & Health Fitouts / In Development / Retail & Hospitality Fitouts / Workplace Fitouts) over large image cards titled by client and suburb ("RB Sellars Office, North Geelong"). A project (property) page, Federal Mills: short history ("Originally built in 1915..." "Since 2013 we've revitalised the once-derelict complex"), awards named, features (4,000 sqm gardens, NABERS 5.5), gallery, vacancies. Real stories about heritage reuse; facts such as year built, garden area and NABERS rating, but no cost or duration.

**Trust**: footer awards (2022 UDIA National Best Urban Renewal Project; 2021 UDIA wins; 2024 shortlist), heritage award mentioned. Copyright "2009-2026" shows longevity. No builder licence number seen. Testimonials: not seen.

**Enquiry path**: Contact page: phone (03) 5224 2788, email, address; form Name*, Email*, Mobile*, Message*. Simple, not multi-step. The home page leads with vacancies, so a builder client has to hunt.

**Motion**: AOS (scroll fade reveals), Swiper, a full-screen hero image. Decorative but light.

**Weaknesses**
- The site is a leasing portal first, builder second. The sticky header is cramped (large round logo, two-row nav) and overlaps content on scroll: in the scroll screenshot the logo sits on top of the "Feature vacancies" heading. Project card titles in teal over photos have weak contrast. Contact hero is a large photo with the form below the fold.

---

## 4. Synergize Constructions (WORST)
https://synergizeconstructions.com.au, eastern suburbs Sydney (WordPress). The one boutique builder found doing both homes and commercial in the same breath, and the clearest picture of how not to do it.

**First screen**
- Desktop: black header with logo, nav of only "gallery" and "contact us". A very pale beige archway photo covered with a white veil; centred white text "Building your vision." then "We are a boutique construction company based in the eastern suburbs of Sydney specialising in residential & commercial developments, high end renovations & new builds." Button (gold): "tell us about your vision today!"
- Phone: same, white text on pale beige is hard to read; no phone number; a three-dot menu icon; a TrustedSite badge floats over the content.

**Projects**
- No project pages. A single "Gallery" of about 30 mixed thumbnails (restaurant interiors with hanging flowers, kitchens, a concrete pump, a staircase, a site-worker shot) with no captions, suburbs, scope or dates. Homes and commercial are mixed together with nothing to tell them apart.

**Trust**: one quote from the director (Mark Nicholas) in pale gold on pale grey, a TrustedSite badge. No licence number seen, no awards, no testimonials, no team, no process.

**Enquiry path**: the contact page's form is long and made for a project: Name*, Email*, Phone*, address, budget (free text: "enter value or write n/a if you do not have a budget"), a dropdown, a radio list of six options plus Other, message, another dropdown, file upload, consent, and a reCAPTCHA. No phone number or `tel:` link on the site (none found in the DOM). Light gold labels on grey are low contrast.

**Motion**: a carousel with bright blue circular arrows that clash with the gold palette; sections fade in from white veils, which made some screenshots look washed out. Decorative.

**Weaknesses**: very low contrast text on both desktop and phone, no phone number, no project pages, unlabelled gallery, no credentials, the form asks for a budget with no guidance, only two nav items.

---

## Other sites opened (not kept)
| Site | City | Verdict |
|---|---|---|
| Helix Group (helix.group) | Sydney | Best mixed-sector example: one brand line, sector filters, real facts per project, licence in footer, strong form. |
| SQ Projects | Sydney | Best craft and awards proof (adaptive reuse, heritage); no form, thin phone page. |
| Hamilton Group | Geelong | Good heritage and warehouse reuse story; leasing-led, cramped header. |
| Synergize Constructions | Sydney | Both sectors but washed-out, unlabelled, no credentials. |
| Growthbuilt (growthbuilt.com.au) | Sydney | Large developer-builder. Full-bleed hero image with big headline "Shaping the way future Australians live, work and play - today"; project pages show Client / Architect / Location / Status. Corporate, apartment-scale, no phone or tel, a simple 5-field enquiry form (name, phone, email, enquiry type, message). Not a boutique match. |
| Pivotal Constructions | Sydney | Wix, 2018; hero shows a waterfront house with text overlaid illegibly, three-item nav (Home, Media, Contact), plain contact form (name, email, phone, address, subject, message); phone is shown (mobile and landline). Thin. |
| Hickory | Melbourne | Large builder-developer. Video hero (GSAP 3.8.0 present), headline "At Hickory, everything we do is MADE for LIFE."; long nav; corporate. Out of scale. |
| Lipman | Sydney | 60-year commercial builder; video hero, "Building Together"; sector nav (retail & hospitality, fitout, aged care); long enquiry form (name, company, job title, suburb, etc.). Commercial only. |
| Total Construction | Sydney / Melbourne / Brisbane | Commercial; hero video of concrete pour, "Delivering Excellence"; three office phone numbers; 169 images on page; heavy. |
| RC Construction | WA (civil) | Out of segment (civil, labour and plant hire); older template slider. |
| Buildcorp / Maxcon | various | Probed for reachability only; large or outside the segment, not reviewed. |
| Mancini Made, BTI, Melegant, Pamment, Lifestyle Building, Cobild | various | Blocked, 502, or unreachable from this environment; not reviewed. |

---

## Patterns the best share
- A plain statement of what the firm builds, in the first screen, including both sectors (Helix: "One Builder. Every Kind of Space.").
- Project facts stated as data: type, suburb, size, value, year, duration (Helix), design-and-construct and award category (SQ).
- Sector filters over one portfolio, with the suburb in every title, instead of two separate sites.
- Credentials with checkable detail: licence number and ABN in the footer (Helix), named awards by category and year (SQ, Hamilton).
- Testimonials attributed by name, role and business or firm, including architects (SQ).
- A visible phone number and a plain CTA in the header or hero (Helix); a fast promise of reply ("within one business day").
- Real stories of reuse and what was kept (SQ Annandale Warehouse: salvaged steel and brick; Hamilton Federal Mills: restored 1915 site).
- Light, mostly decorative motion: fades and simple sliders, no scroll hijacking.

## What none of them do well
- Present homes and commercial as two audiences with two promises, equal in weight, on one shared brand. Helix comes closest but still leads with commercial and has a thin residential side; SQ and Hamilton are single-sector.
- Show heritage work with before and after, plans or process photos; none had any.
- Explain the process in a visual way (stages, who you deal with, how a quote is built); Helix only has an FAQ and no one has a timeline.
- Use phone-first design: SQ's phone home is a slideshow with a gap, Hamilton and Synergize lack a phone number on the first screen, Synergize is hard to read.
- Name the people (site supervisor, owner, licensed builder) with photos on project pages; only SQ has a team page, and none tie people to projects.
- Show warranty, insurance and variation handling plainly (Helix has an FAQ group, not seen elsewhere).
