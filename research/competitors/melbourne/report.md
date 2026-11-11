# Melbourne and Victoria: luxury custom, architectural and period-renovation builders

Research date: 11 Nov 2026. Method: WebSearch to find candidates, then Playwright (Chromium) at 1440x900 and 390x844 (isMobile), screenshots read by eye, plus DOM inspection. Nothing was submitted or contacted. Not verified: anything outside what loaded in headless Chromium (video autoplay is blocked or paused there, so some hero videos were seen only as a poster or not at all).

Sites opened (9 attempts): Fortem Projects, Builders of Architecture (BOA), Destination Living, Armadillo, Leone, Hedger Constructions, Marque. Construct Melbourne (Squarespace "Website Expired" page), Saltwater Builders (HTTP 502) and Carter Grange (connection failed) did not load and were dropped. cannygroup.com.au loaded but is an accounting site (wrong domain), dropped. Only 7 usable sites were opened, short of the 8 to 10 target, because of those failures.

Screenshots kept in this folder: `fortem-*`, `boa-*`, `destination-*`, `armadillo-*` (desktop-first, phone-first, desktop-scroll-2, project, contact).

Pick: THREE BEST = Fortem Projects, Builders of Architecture, Destination Living. ONE WORST = Armadillo.

---

## 1. Fortem Projects (BEST for our brief) - https://www.fortemprojects.com/ - Oakleigh South, Melbourne

Closest match to the Adelaide client: "specialists in period renovations and architecturally designed new homes".

**First screen**
- Desktop: full-bleed photo of a curved Victorian render facade under a dark overlay (autoplaying looping MP4 in the DOM, paused/static in headless, so the video itself is unverified). Yellow wordmark top-left, nav About / What We Do / Our Work / News, outlined "Contact" button top-right. Headline "BUILDING A UNITED VISION" (white and yellow). Sub-line: "We partner with owners and architects to build award-winning homes in Melbourne's finest suburbs." Then "Winner of the 2025 HIA Victorian Renovation/Addition Project $2-5 million". Only CTA on this screen is the "Contact" button; a chevron prompts scrolling.
- Phone: same headline over a different, cropped photo (modern two-storey home), hamburger menu, no CTA button and no phone number on the first screen.

**Projects**
- Index (/projects/): 17 project names (SURREY, THE PINES, LEWISHAM, MATHOURA, QUAMBY, MANNING, UMULA ...) as a list/grid of tiles; /our-work/ is a short gateway with Featured Projects and Project Videos (a /videos/ page exists).
- Project page (Quamby, Hawthorn): full-bleed hero photo with the name, "Location Hawthorn / Type Renovations". About 17 large images. One pull-quote from the project's architect (named, with firm: "Sarah Bryant, Bryant Alsop Architects"). Narrative about 200 words: circa-1897 Victorian brick home, restored ceiling roses, cornices, tessellated tiles, cast-iron lacework, plus a new first-floor addition for a family of five. Names the collaborating architect and shows the two award badges (HIA 2024 winners). No before/after pairs, no plans, no duration, no budget, no video on that page (0 video elements). Facts are thin (suburb and type only), but the story is specific to heritage work.

**Trust**
- Awards page: HIA Victorian winners 2021, 2024 (x2), 2025; MBV Excellence in Housing nominee/finalist entries 2022, 2024, 2025; each links to its project. This is the strongest awards presentation of the sites checked.
- Licence: team page states both directors are "Registered Building Practitioner (Domestic Builder - Unlimited)". No licence number seen. Founded 2016 per About page. Team page with directors (Chris Curtain, Stuart McFarland), "over 50 years of experience between them", "senior in-house carpenters".
- Testimonials: a dedicated page, long-form (multi-paragraph) client quotes, 23 images on the page. Attribution style: not confirmed (I did not capture names; the DOM has no blockquote elements). Uncertain.
- Process: About page has a "Download our guide" on early designer-builder collaboration; "What We Do" has separate Renovations and New Homes pages. A "Partnerships" page exists (not opened).
- Claim "we only take on a select number of projects at any time" (contact page).

**Enquiry path**
- "Contact" button persistently in the header. Contact page form: First Name*, Last Name*, Email*, Phone Number*, "What best describes your enquiry?"* (select: "thinking of doing a renovation / new build but I don't know where to start"; "ready to start the design process ... need guidance"; "I have a design concept and want to talk about buildability (time and costs)"; "I have detailed plans and specifications and want to talk about buildability"; Other), Postcode*, Message, Cloudflare "verify you are human" widget. No budget question. This enquiry-stage dropdown is a smart filter.
- Page copy names a person ("Call Director Chris Curtain") and shows +61 483 946 377 (tel link), address and email. On the home page the tel link sits in the footer, not the header; on phone it is only reachable at the foot of the page or on the contact page (first screen has no call button).
- Footer on every page: phone, email, newsletter sign-up (first name, last name, email).

**Motion and interaction**
- DOM: GSAP + ScrollTrigger, Swiper, WordPress. Hero video loop. Sections fade in on scroll. In several screenshots (home scroll, contact, testimonials) the page ground renders a flat mid-grey; this may be a page-reveal overlay or the real design, uncertain. Fade/slide reveals are gentle and support the reading order; no cursor effects seen; no Lenis found. Helps more than it decorates.

**Weaknesses**
- Mid-grey ground with grey body text and small type reads low-contrast (testimonials and contact screenshots).
- Project pages have no scope, duration, budget or before/after, despite being renovation specialists.
- No phone in the header or on the phone first screen; no sticky call button.
- Cloudflare human-check widget adds friction to the form.
- Awards page leans on nominees/finalists as well as winners (honestly labelled, but cluttered).

---

## 2. Builders of Architecture (BOA) (BEST) - https://buildersofarchitecture.com.au/ - Melbourne (factory address in footer, suburb not captured)

**First screen**
- Desktop: navy left rail with vertical text "BOUTIQUE BUILDERS OF ARCHITECTURALLY DESIGNED HOMES IN MELBOURNE"; hero photo of a bush-coastal house with deck; thin vertical grid lines over it. H1 "Architecture, Brought to Life" (the H1 in the DOM is the small kicker, the large words are an H2, uncertain which is semantically the H1). Body: "For over 15 years, we have been translating leading architects vision into reality." Buttons: "For Home Owners", "For Architects"; header CTA "Get Started".
- Phone: same headline and copy, both audience buttons stacked, a round black paper-plane enquiry button in the header next to the hamburger. No phone number on the first screen.

**Projects**
- Portfolio index: 16 tiles with filters: Project Type (All, Renovation 13, New Build 6) and Location (Victoria 20, Hawthorn, Brighton, Brunswick, Carlton North, Kew, Kyneton, Lorne, Preston ...). Each tile: name plus a one-line poetic caption. A home-page carousel (Slick) of 6 projects (Gunmetal, Pohlman Home, Spindrift, Elm St ...).
- Project page (Elm St, Hawthorn): about 34 large images; header facts: Project Type: Renovation, Location: Hawthorn, Victoria; credit line "Architect: Quinn Architecture | Photographer: Kirsten Bresciani"; Previous/Next and "other success stories". Text depth is one sentence ("A personal vision carried through with clarity and care ..."); no scope, duration, plans, video or before/after. Heavy photography, light on facts.

**Trust**
- Awards listed on About: "Winner 2020: Master Builders Excellence Awards Best Renovation", MBAV finalist entries. "Over 15 years". No licence number found in text (uncertain; not exhaustive). No testimonials found on the pages checked.
- Process page: numbered steps ("Step 1 We engage at the earliest stage to assess feasibility, budget alignment and site conditions ...") plus a dedicated "Early Contractor Involvement (ECI)" page. Separate "Home Owners" and "Architects" pages speak to the two audiences. The architect-referral angle is the best-articulated of the sites.
- Team: not examined in depth (uncertain).

**Enquiry path**
- CTAs everywhere: header "Get Started", "Book A Consultation" mid-home, a form embedded at the foot of the home, process and project pages, and a dedicated contact page.
- Contact form fields: Name*, Phone*, Email*, Enquiry Type* (New Build, Renovation, Heritage Renovation, Sustainable Home, Media, Partnership), Budget Range* ($1.5M-$2M up to $3.5M+, minimum $1.5M, which self-qualifies), "Have you engaged an Architect?" (Yes - Plans ready / Yes - In progress / No - I need help), Preferred Start Date, Message. Not multi-step. A "Heritage Renovation" option is explicit.
- Phone: (03) 9847 7867 as a tel link, but only at the very foot of the page (about 10,300 px down a 10,500 px home page); not in the header.

**Motion and interaction**
- DOM: Slick carousel, Barba (page transitions), WordPress. Carousel with arrows on the home page; fine-line grid overlay. No video hero, no hijacked scroll seen. Carousel is genuinely useful for browsing; the grid lines are decoration.

**Weaknesses**
- Phone number is buried at the page foot; no sticky call/enquiry bar on phone (only the paper-plane icon).
- Project pages are photo galleries with one line of text; no facts for credibility beyond architect and suburb.
- Mandatory $1.5M budget floor is blunt (works for their market, would read as a barrier for a mixed-scope builder).
- Vertical sideways text in the rail is hard to read and eats width on desktop.
- Caption poetry ("where drawings become lived spaces") says little concrete.

---

## 3. Destination Living (BEST) - https://destinationliving.com.au/ - Collingwood, Melbourne

Design-and-build practice (architects, interior designers and builders as one team); closer to the "design-build" than a pure builder, but its content structure is the most informative.

**First screen**
- Desktop: white header with logo, nav Your Block / Our Work / About / Articles / Building Cost Calculator, outlined "Get in touch" button. A 3-slide slider of dark-overlaid project photos (concrete-walled house on the first slide). Directly under it, headline "Capture unique possibilities and spaces that excite" (the H1-level text; the slide headline is "Architecturally led. Thoughtfully designed. Built with intent."). No button inside the hero.
- Phone: slider with the white overlay text "Destination Living is a team of architects, interior designers and builders, working as one." plus an "About us" button; text over a busy photo has poor contrast. Hamburger menu, no phone on first screen.

**Projects**
- Index (/our-work/, /projects/): 59 images; filter chips: Complete, Difficult Section, Downsizer, Dual Occupancy & Developments, Knock Down Rebuild, Narrow, Other, Renovation, Sloping; with "Completed" and "In Progress" lists. Titles are descriptive and suburb-led ("Mitcham Heritage House Renovation", "Richmond Narrow-Site Downsizer").
- Project page (Mitcham Heritage House): full-width hero with a keyword-style H1 "Mitcham Heritage Renovation: Replanning a Victorian Weatherboard", status "completed project", type "renovation", icon row (3 bedrooms, 2 baths, 2 garage), about 50 images on the page, an embedded YouTube video, a long narrative explaining the Heritage Overlay constraint (facade and roof retained), completion month (August 2026) and approach. Strongest text depth of any site here. No architect credit or price seen; no before/after pair seen (uncertain).

**Trust**
- Client Stories page: question-led headings ("Will the design actually be better than I expect?", "Will this be stressful, or controlled?"), each quote attributed by first names only ("Jenny", "Lisa and Greg") and linked to a project. About, Our Team, How We Work and Our Process pages; team shows Mike Costa as "Co-Founder, CEO & Licensed Builder". No licence number found. Awards not checked on the pages visited (uncertain).
- Building Cost Calculator (instant estimate) and a "What will my project cost to build?" article address the price question that most builders avoid.

**Enquiry path**
- Header "Get in touch" plus footer and a "Let's start the conversation" block on the home page. Contact is at /get-in-touch/ (the /contact/ guess returned 404). Copy says the team "is unable to discuss your project ... before this is completed", i.e. form first. Form fields: First Name*, Last Name*, Email*, Mobile*, "Where are you looking to build?"*, "Do you own a block?" (I own the site / I am looking to buy), Your Message. No budget field; a cost calculator replaces it. Phone +61 3 9497 1227 and address shown on the contact page and footer.
- Phone: no tel link in the header; the number is in the footer only.

**Motion and interaction**
- DOM: WordPress with a Divi-style slider; 3-slide hero crossfade with dots; no GSAP/Lenis found. Back-to-top button. Little motion; restrained.

**Weaknesses**
- Hero slider text on phone is hard to read; the desktop hero carries no CTA.
- The "no conversation until you fill the form" rule adds friction (and, at the time seen, no phone number in the header).
- Long, SEO-style page titles ("Mitcham Heritage Renovation: Replanning a Victorian Weatherboard"); long text blocks in light-weight grey type.
- Design-build positioning is not a pure Master Builder story.

---

## 4. Armadillo (WORST) - https://www.armadillohomes.com.au/ - Melbourne (phone 03 9885 0505)

Reported as "Multi Award Winning Master Builder of the Year" on the home page, but the site undersells it.

**First screen**
- Desktop (after a 9 s wait): looping video fills the screen showing a swimming-pool step, stone wall and black balustrade (a landscape/pool detail, not a house). Logo and nav Home / About / Design Studio / Projects / Contact in white small text over the video. No headline, no button. Before the wait the first capture was blank white (Wix load).
- Phone: the same video fills the screen with only the "armadillo" logo; no visible menu icon and no CTA on the first screen (menu icon not seen in the screenshot; uncertain whether it appears after scroll).
- Lower on the home page: "at armadillo we unite purposeful design with considered craftsmanship to create homes defined by detail", "Multi Award Winning Master Builder of the Year", "GET IN TOUCH", then a 3-field form. The whole home page is only about 2,470 px high.

**Projects**
- Wix pages with URLs such as /copy-of-projects, /copy-2-of-gallery (template leftovers). The "Projects" page is a "design & build / our approach" text page with a hero and about 11 images; no project index with suburbs, scope, architect or duration was found. One page showed a wide shot of a steel-framed house under construction against a white page (Wix gallery). Gallery pages ("gallery", "gallery-ourbuilds") not examined in detail (uncertain).

**Trust**
- Only a "Master Builder of the Year" line (no year, no body named) and "multi-award-winning". No licence number, no testimonials, no team page content beyond the founder paragraph on About ("industrial designer and accomplished builder"). Footer reads "(c) 2010-2025", stale by the research date (Nov 2026).

**Enquiry path**
- Contact page: email, tel and mobile (+61 411 134 141) as text, "By appointment only", form fields Name, Email*, Write a message. No project type, budget, suburb or phone field. The home page repeats the same short form. Phone number on mobile sits near the foot of the page (about 1,800 px down a 2,470 px page), not in the header.

**Motion and interaction**
- DOM: Wix (Thunderbolt), Swiper. Autoplaying loop video hero. The motion is decorative: the footage is not of a finished house.

**Weaknesses**
- No message on the first screen at all; the brand promise is below the fold.
- White nav text over bright video and photos is hard to read (seen on the contact and projects heroes); body text is small (computed base font 10px on mobile).
- Thin project evidence: no clear project index, template URLs ("copy-of-projects"), no suburbs or scope.
- Short, undifferentiated form; no way to say what you want built or your budget.
- Stale copyright and an unnamed top award.

---

## Other sites opened (not kept)

- **Leone** (leone.com.au, South Melbourne): black-and-white sculptural video/photo hero, blue marquee banner "BUILT IN THE PRESENT, ARTEFACTS OF THE FUTURE. WE ARE ARTISANS, CRAFTSMEN. MASTER BUILDERS."; GSAP + ScrollTrigger; projects called "Artefacts" with architect, interiors, photographer credits. Strong art direction but: the Bayside House project page still contains template text ("INTERESTING QUOTE BY LEONE OR THE CLIENT REGARDING SOME CHALLENGING ASPECT OF THE BUILD."); no client enquiry form (contact page forms are only for project manager and subcontractor job applications plus a general details form; office "by appointment only"); the logo overlaps the headline on scroll; no tel link found in the DOM on the home page (number shown on the contact page: 03 9626 4800). Runner-up for design, rejected for the placeholder text and weak enquiry path.
- **Hedger Constructions** (hedgerconstructions.com.au, Richmond/Alexandra): WordPress/Avada, 20+ projects, 30+ MBA awards claimed by the search result (not verified on the site), long contact form (first/last name, email, phone, "I'm interested in..." with 11 options including Renovations & extensions, location, timing, budget from $500k, message, reCAPTCHA), "Book a consult" side tab, tel link in footer, 1300 291 101. On desktop the hero rendered blank white in the headless capture (the loop video was paused), so the first screen is unverified; on phone the hero is a small photo with thin "Building with Distinction" text and a pale-blue panel. Conventional template look; solid project volume.
- **Marque** (marque.com.au): volume-style "Custom Luxury Homes for your Unique Lifestyle" video hero, chatbot ("Marque Virtual Assistant") opens over the hero on both desktop and phone and covers the headline, tel 1300 062 778 visible in the page header area. Pre-designed collections, show homes; not a good model for a heritage builder.
- Not loaded: Construct Melbourne (expired Squarespace), Saltwater Builders (502), Carter Grange (connection failure).

## Patterns the best share

1. A specific promise tied to the work, not a generic tagline: Fortem "period renovations and architecturally designed new homes" with an award line under the headline; BOA "translating leading architects' vision into reality".
2. Large, professionally shot project photography dominating the first screen and project pages (17 to 50 images per project), with the project name set over a full-bleed hero.
3. Project pages credit suburb and type (all three); the best also credit the architect (Fortem and BOA name the architect firm) and explain the heritage constraints in plain terms (Destination Living's Heritage Overlay explanation).
4. Awards presented as dated, categorised, linked-to-project lists (HIA/MBV winner, nominee, finalist labelled honestly), not as a row of logos.
5. A visible, two-audience or stage-based route: BOA separates Home Owners and Architects; Fortem's enquiry dropdown asks how far the client is (no plans, concept, detailed plans).
6. Enquiry forms that qualify with one or two good questions (enquiry stage, architect engaged, owning a block, enquiry type including "Heritage Renovation") rather than only name/email/message.
7. A persistent header CTA ("Contact", "Get Started", "Get in touch") on every page, plus a short narrative of process or "how we work".
8. Restrained motion: fades and carousels that help browsing, no cursor effects or scroll hijacking (no Lenis found on any of the sites checked).

## What none of them do well

1. Phone numbers on mobile: none of the four kept sites has a tap-to-call button in the header or a sticky bar; the number is in the footer or on the contact page only.
2. Project facts: none shows duration, scope list, build value range or before-and-after pairs on a project page, even for renovations; plans and drawings were not seen.
3. Licence number: no site showed a builder licence number or insurance/warranty cover in view (Fortem states "Registered Building Practitioner (Domestic Builder - Unlimited)" without a number); no clear "how we handle variations and cost control" section.
4. Testimonials: attributed by first name only (Destination Living) or in a long block with unclear attribution (Fortem); none uses name, suburb, project and photo together or links reviews to a verifiable source (Google, hipages).
5. Mobile first screens: Armadillo shows no message; Destination Living's hero text is hard to read over photos; Fortem and BOA do not show a call or enquiry action beyond the hamburger/icon.

## Table of all sites opened

| Site | City | Verdict |
|---|---|---|
| Fortem Projects (fortemprojects.com) | Oakleigh South, Melbourne | Best fit: heritage-renovation specialist, strong awards page and project pages, tidy qualifying form; grey low-contrast ground, no phone in header. |
| Builders of Architecture (buildersofarchitecture.com.au) | Melbourne | Best structure: two-audience paths, portfolio filters, process and ECI pages, budget and architect questions in the form; photo-heavy thin project text, phone buried. |
| Destination Living (destinationliving.com.au) | Collingwood, Melbourne | Best content depth: filters by block type, long project narratives with heritage constraints, cost calculator; form-first gate and weak mobile hero text. |
| Armadillo (armadillohomes.com.au) | Melbourne | Worst: Wix, video-only hero with no message, thin home and project pages, template URLs, 3-field form, small low-contrast text. |
| Leone (leone.com.au) | South Melbourne | Striking art direction (GSAP), but placeholder quote left on a project page and no client enquiry form. |
| Hedger Constructions (hedgerconstructions.com.au) | Richmond / Alexandra | Large portfolio and detailed form with budget; template look, hero unverified on desktop (blank in headless), phone in footer. |
| Marque (marque.com.au) | Melbourne | Volume-style custom builder; chatbot covers the hero, collections-led, not a model for heritage work. |
| Construct Melbourne / Saltwater Builders / Carter Grange | Melbourne | Did not load (expired Squarespace / 502 / connection failed); not assessed. |
