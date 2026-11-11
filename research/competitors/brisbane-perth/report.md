# Brisbane and Perth builder websites: research for an Adelaide Master Builder site

Captured 11 Nov 2026 with Playwright (Chromium), desktop 1440x900 and phone 390x844. Claims below come from screenshots or the page DOM. Anything unchecked is marked "uncertain". No forms were submitted.

Candidates opened: 10 (Brisbane 5, Perth 5). Brisbane Unique Homes was a parked domain and was dropped. Giorgi and O'Shea & Sons could not be reached through the proxy; MCD Construction likewise. Zorzi Builders sat behind a Cloudflare challenge ("Just a moment...") and could not be opened.

Chosen: three best (Build Prestige Homes, McCarthy Homes, Azure Luxury Homes) and one worst (Blue Chip Builders). Screenshots kept in this folder.

## 1. Build Prestige Homes (best): https://buildprestigehomes.com.au, Brisbane (Hamilton Central PO Box; projects in Wavell Heights etc.)

**First screen**
- Desktop: full-bleed looping video (`bph-intro-video.mp4`) of a large white house on acreage, dark overlay. Wordmark line "BUILD PRESTIGE HOMES" in spaced capitals, then "Where craftsmanship meets experience". Buttons: "REQUEST CONSULTATION" (top left, outlined) and "VIEW PROJECTS". Logo centred, "MENU" top right.
- Phone: same video, cropped. The video has a logo baked into it that is cut off at the edge ("BUILD PRESTIGE HO..."). The strapline sits low-left. The Request Consultation button and any phone number are not in the first phone screen, only the menu.

**Projects**
- Index lists 12+ named projects (Kiama, The Estate, Bonita, Mountjoy, Brookhaven, Newman, Hilltop and others); I did not review the index screenshot closely.
- Kiama page: full-height hero photo with the name, then facts in three labelled fields (project type "Classic American Farmhouse", location "Wavell Heights", size "580m2 | 6 Bedrooms"), then a long overview paragraph (about 200 words) covering kitchen, ensuite, wine cellar, pool, and a stormwater problem solved during construction. 34 images on the page. No before/after, plans, duration, architect, or video seen.
- Homepage "Featured project" card overlays facts (suburb, area, bedrooms) on a crossfading photo.

**Trust**
- Awards block on the homepage as four cards with HIA diamonds: Winner 2021 HIA Brisbane Custom Built Home over $5m; Finalist 2017; Winner 2017; Winner 2015 (People's Choice). Years are shown, which is honest: the newest is 2021.
- QBCC licence 1192228 and ABN in the contact page footer. Process page and #reviews anchor exist; I did not read the review content (uncertain how many testimonials). Houzz, Pinterest links.

**Enquiry path**
- "Request Consultation" is in the header on every page (desktop). Contact page leads to a questionnaire page ("Complete Your Project Questionnaire").
- Questionnaire fields: your name, partner's name, email, mobile, current address (full international address with country list). The contact-page form also carries a budget range slider (`project_budget`) and five dropdowns plus a message. Contact page says "Response within 48 hours" and hours Mon to Fri 8 to 5.
- Phone 0418 745 837 is a `tel:` link, but only in the footer (about 3900 px down the phone homepage). Not in the phone header.

**Motion and interaction**
- DOM contains GSAP, ScrollTrigger, Lenis (smooth scroll) and Swiper. Seen: video hero, crossfading photo sections that overlay each other as you scroll, sticky header that turns from transparent to light. The crossfades help (they show interiors under project facts) but during scroll two photos overlap semi-transparently, which looked muddy in one capture. Lenis changes scroll feel; no hijack observed that blocks scrolling.

**Weaknesses**
- Phone first screen has no CTA or phone number; hero video logo is clipped.
- Questionnaire asks for a full international address and partner's name up front: heavy for a first contact.
- Contact page text is generic ("Let's Build Your Dream Home Together"), email is "click to submit enquiry", office is a PO Box with "by appointment online".
- Awards are mostly 2015 to 2021.

## 2. McCarthy Homes (best on structure and mobile): https://mccarthyhomes.com.au, Brisbane

Note: a project/display-home builder as well as custom, so its project pages are floorplan-led. Still the cleanest "calm and plain" site of the set.

**First screen**
- Desktop: autoplay video of an aerial over Brisbane streets with a giant "McCarthy Homes" wordmark across the top. A frosted bar at the bottom holds "Menu", the round M logo and a black "Contact" button. Below, "CRAFTED TO INSPIRE, BUILT TO ENDURE." and "Solution-driven at our core, we tailor every home to your unique site, design and lifestyle."
- Phone: video of timber roof trusses, wordmark at top, bottom bar with menu button, logo, and a black phone-icon button. The DOM shows a `tel:+61735240606` link that is visible. This is the best phone-first-screen CTA of the set.

**Projects**
- Home designs index plus "homes/<name>" pages. Macedon page: full-bleed photo with name, intro, features list (custom design, alfresco, pool, 2.7 m ceilings, travertine benchtops), spec figures (5 bed, 4.5 bath, 2 car, 451 m2), "Download floorplan" and "Book a consultation". 42 images on the page. No suburb, duration or before/after (these are design types, not delivered jobs).

**Trust**
- QBCC 727 579 and ABN in the footer and on the contact page. A "Built on trust" testimonial (large pull quote, attributed by first names only: "Adrien & Simone") with a portrait video beside it; dedicated Testimonials page linked (not counted). Contact page FAQ answers "Do you offer fixed-price contracts?" and similar. I did not find named awards on the homepage (uncertain).

**Enquiry path**
- Contact button fixed in the bottom bar on every page. Contact form fields (all required): first name, last name, phone, email, build postcode, enquiry type (general, sales, maintenance), build budget (dropdown from $800,000 to $1,500,000+), message, privacy acknowledgement. Phone 07 3524 0606 and email at the top of the contact page. Per-page shorter form on home pages (name, phone, email, checkbox).
- Budget question is a dropdown with bands; it is a project-home range, and would need different bands for Adelaide heritage work.

**Motion and interaction**
- Videos autoplay (banner mp4 and a property reel), Swiper and AOS (scroll reveal) in the DOM. Hero wordmark is large type over video. Motion is restrained and the video is the content (aerial, framing), so it helps. Page was 7100 px tall on desktop.

**Weaknesses**
- Hero wordmark is very large and the headline text sits below the fold on desktop.
- Project-home focus means no suburb, scope or duration facts.
- Budget band starts at $800,000: excludes smaller work.

## 3. Azure Luxury Homes (best for a plain, credible custom builder): https://azureluxuryhomes.com.au, Perth (Mount Hawthorn)

**First screen**
- Desktop: full-screen slideshow of project photos (Circi, Rookwood, Ardross, Burke...) on dark ground, logo top left, "MENU" with a line top right, Facebook and Instagram icons. The title "Excellence In Custom Designed Homes" is in the page title and slide DOM; on the desktop capture it was not visible (text fades in per slide; uncertain whether it showed later). No buttons on the hero.
- Phone: same slideshow, with the headline barely legible on the photo (faded text at roughly 15% contrast in the capture), then a long intro paragraph. No visible button or phone number.

**Projects**
- Luxury Homes index of about 25 named residences, each linking to a page. Project page (Ardross Applecross): dark page, name, very large stacked photographs (72 images, 14,500 px tall), and nothing else: no suburb, scope, architect, duration or text. A "View next residence" list follows. A few links use `?post_type=projects&p=425`, which return a 404 page ("Oops! That page can't be found"): broken links verified.

**Trust**
- Strongest awards page of the set: 2026 HIA Perth Housing Awards winner Home of the Year, Renovation/Addition Project of the Year, Renovation/Addition over $1.5m, Spec Home of the Year, finalists; plus Master Builders winners 2024, 2019, 2015 and finalists back to 2013. Each links to its residence with the suburb named.
- Our Process page: six numbered steps (design brief, concept and costing, plans and contract documents, contract signing, commencement, tendering). Clear and plain. No licence number seen in the pages I read (uncertain). No testimonials seen. No team page content checked.

**Enquiry path**
- Contact page: "We love to listen. Talk to us about building your dream home." Form fields: name, phone, email, message, CAPTCHA. Three phone numbers as `tel:` links (office, Steve, Rob), email, address with Google map. The same form sits in the footer of every page.
- No multi-step form or budget question.

**Motion and interaction**
- Slideshow hero, AOS scroll reveals, WordPress (wp-content). No GSAP or Lenis in the DOM. Motion is mostly fades; hero slideshow decorates.

**Weaknesses**
- Project pages carry no facts at all, only photos; 14,500 px of scroll.
- Phone hero text hard to read; no phone number or CTA on the first phone screen.
- Broken project links; "Excellence In Custom Designed Homes" repeated in the slider markup eight times (uncertain whether that matters to accessibility).
- Fixed side menu overlaps photos on scroll (seen in the scroll-2 capture).

## 4. Blue Chip Builders (worst): https://bluechipbuilders.com.au, Brisbane (Oxley)

**First screen**
- Desktop and phone: a stock-looking photo of a worker with a drill at a timber frame, dark overlay. H1 "Professional & Affordable Building Services in Brisbane", subtext "From home extensions to full renovations, Blue Chip Builders delivers quality results that fit your budget and timeline". Buttons: "Get a Free Quote" (yellow) and "Our Services" (black), same on phone.

**Projects**
- No project pages. The homepage "Recent Building Projects" shows two projects as a title with suburb and one sentence ("Modern Residential Extension - Paddington, 4064"). A "View All Projects" button exists, but the site's only links are Home, About, Services, Contact (verified in the DOM), so it leads nowhere that I found.

**Trust**
- "4.9/5 average rating" with no source; testimonials section present (not counted); no licence number, memberships or awards seen in the homepage text.

**Enquiry path**
- "Get a Free Quote" header button. Contact page shows no form fields in the DOM (uncertain whether an embedded form loads later). Phone shown as text "+61 484 883 888", but the `tel:` link on the page is `(555)214-9031`, which is a template placeholder. The footer email link is `info@peakshieldroofing.com`, which belongs to another business: a leftover from a copied template. Both verified in the DOM.

**Motion and interaction**
- None found (no libraries or video).

**Weaknesses**
- Placeholder phone and another company's email left in links; "Affordable" positioning, not premium; no real project content or credentials; the blue/yellow/American-flag-style logo clashes with the claimed premium; generic copy that could be any builder.

## Patterns the best share

- Hero is a real project (video or photo) with one short line, and a visible route to enquire: a header "Request consultation" or "Contact" button on every page.
- Large photography does the selling; text is calm and short. McCarthy and Build Prestige use a dark-to-light switch (transparent header over hero, solid after).
- Awards are shown with year, body and category (Azure, Build Prestige), not just logos.
- Project pages open with a full-bleed hero and a few labelled facts (type, location, size) then a story; Build Prestige's includes a problem solved on site.
- Contact page puts phone, email, address and licence/ABN together, with a form beside them.
- A numbered process (Azure) tells a client what happens before the contract.
- Testimonials work best as one large quote attributed by name (McCarthy), not a grid of stars.
- A visible `tel:` link: McCarthy puts it in the phone header; most others hide it in the footer.

## What none of them do well

- Phone first screens: only McCarthy shows a call button; Build Prestige and Azure show neither a phone number nor a CTA before scrolling.
- Project pages with the facts a client wants: suburb, scope, duration, architect, budget band, and a before/after. Azure and Weststyle show almost none; none show plans or a timeline of the build.
- Heritage or renovation work: all four are new-build led; no site explains approvals, heritage overlays or living in the home during works.
- Testimonials with full attribution (name, suburb, project): McCarthy uses first names; the others have none that I saw.
- A short first-contact form: the budget and address questions in Build Prestige's questionnaire are heavy; Azure's four-field form is fine but offers no way to say what the project is.

## All sites opened

| Site | City | Verdict |
|---|---|---|
| Build Prestige Homes (buildprestigehomes.com.au) | Brisbane | Best on depth: video hero, dated awards, GSAP/Lenis motion, long project stories; phone CTA hidden on mobile. |
| McCarthy Homes (mccarthyhomes.com.au) | Brisbane | Best on structure and mobile: visible phone button, calm type, quote with attribution; project-home focus. |
| Azure Luxury Homes (azureluxuryhomes.com.au) | Perth | Best awards and process pages; project pages bare, broken links, weak phone hero. |
| Blue Chip Builders (bluechipbuilders.com.au) | Brisbane | Worst: template with placeholder phone, another company's email, no projects. |
| Graya (graya.com.au) | Brisbane | Strong design (black/white, full-width photography, mailing-list and "Exclusive access" form with budgets $1m to $20m+), but a developer; my first-screen capture showed only a logo loader (hero content uncertain); phone is plain text, not `tel:`. |
| Weststyle (weststyle.com.au) | Perth | Elegant slider and big photos; Elementor; project page shows only title and address text; clear approach and awards; simple name/email/phone/message form. Near miss for top three. |
| Domination Homes (dominationhomes.com.au) | Perth | Volume-style site: "PERTH'S BEST LUXURY HOME BUILDER" claim, phone in header, display homes and blog; long page (11,600 px). Not a fit. |
| Tallwood Custom Built Homes (tallwood.com.au) | Perth/South West | Squarespace, a lovely hero photo, "Get in touch" button, awards and testimonials pages; no `tel:` link found on the home page. |
| Contour Projects Group (contourprojects.com.au) | Perth | Capture showed only a heading and nav (page content may not have loaded; uncertain). |
| Brisbane Unique Homes (brisbaneuniquehomes.com.au) | Brisbane | Parked domain; dropped. |
| Zorzi Builders, Giorgi, O'Shea & Sons, MCD Construction | Perth/Brisbane | Not opened (Cloudflare challenge or proxy failure). |
