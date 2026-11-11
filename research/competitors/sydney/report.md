# Sydney and NSW luxury / architectural / high-end renovation builders: website research

Date: 11 Nov 2026. Method: Playwright (Chromium) at 1440x900 and 390x844 (mobile), screenshots read by eye, plus DOM inspection. Nothing submitted, nobody contacted. Award and licence claims below are what the sites say; I did not verify them against MBA/HIA lists.

## Sites opened (7 loaded and reviewed; 2 more failed)

| Site | Verdict |
|---|---|
| chateau.com.au (Chateau Architects + Builders, Castle Hill) | BEST. Full-bleed video hero, calm cream/green palette, strongest trust and enquiry structure (licence, six-step process, staged form with budget). |
| mileham.com.au (MILEHAM Architects + Builders, Freshwater) | BEST. Most editorial, best project pages (full fact sheet incl. heritage listing), real attributed testimonials; weak on phone visibility. |
| tass.com.au (TASS architects + builders, Surry Hills) | BEST. Cinematic video hero, big rounded-corner photography, long project pages, clear service split (build only / design only / design and build). |
| mardiniconstructions.com.au (Mardini Constructions, Leichhardt) | WORST. Dated, no H1, broken reCAPTCHA on the contact form, project index with no detail, lots of copy-heavy remedial nav. Good licence/awards facts, though. |
| gremmohomes.com.au (Gremmo Homes, Baulkham Hills) | Mixed. Slider hero with the same headline repeated 12 times in the DOM, old logo, blue contact page, large blank grey area seen mid-scroll (may be an unrevealed animation: uncertain). Thin enquiry form, no budget/stage. |
| profilepropertygroup.com.au (Profile Property Group, Paddington) | Squarespace; award-winning heritage/high-end, but cover-image-and-name-only homepage, tiny project pages (6 images, ~140 words), no form at all (email/phone listed). |
| australbuild.com.au (Austral Build, Kingsgrove) | Hero "Experience the luxury of custom build", ~56 words on the home page, video-led, fairly empty; project pages short (~113 words); no on-page form found (phone and email only). Decent heritage Paddington project. |
| stratti.com.au | Failed: resolves to an unrelated "Stratti Worldwide" Wix site, not the builder. Dropped. |
| stellergroup.com.au | Failed: loaded blank (no title, links or content). Dropped. |

Screenshots kept (5 each) for chateau, mileham, tass, mardini in this folder.

---

## 1. Chateau Architects + Builders: https://www.chateau.com.au (Castle Hill, Sydney)

**First screen.** Desktop: full-bleed video of a modern zinc-clad home under gum trees, with a darkening overlay. Headline on screen: "Architectural homes built for legacy". The H1 in the DOM is "LUXURY CUSTOM HOME BUILDERS SYDNEY" (an SEO line shown as a green eyebrow below the fold). Nav: About, Our process, Projects, News, Open home. One button: "Get in touch" (outlined, top right). Scroll chevron at the bottom. Phone: the video shrinks to a short strip (about 220px high) with the same headline overlaid, "Get in touch" button and a hamburger; the page below is cream with an eyebrow, a large statement "As one of Sydney's few true architect + builder companies..." and then an image. The hero on phone is weak (headline cramped over a tiny video strip), but the content below is clean.

**Projects.** Index (/project-listing/): cards with style tags (Modern, Contemporary, Classical, Provincial) and a green "Delivered" badge; 12 project links on the page; project intro text. Project page (Vaucluse Ultra Modern): fact table (Built 2022, Style, Location, Design = Sofair Design, Construction), a short summary, a "Request a site review" panel, award badge (HIA NSW Custom Built Home $1.5-2.0M, winner 2023), then 38 images, ~700 words, page height ~9,600px. No before/after, no plans, no video observed on the project page. No duration or contract value.

**Trust.** Licence numbers printed in the footer ("Licence Number: 73523C" and a second "6323" number; I did not work out what each covers). "Since 1969", family-owned, "award-winning master builder". About page has an awards section (#awards) and "Our people" section. A dedicated "Our process" page: six-step architect-led process (01 "The genesis of your dream", Lot review, On-site insight, Vision sharing, ... through "Construction commencement"). Testimonials: not checked on the pages I opened (uncertain).

**Enquiry path.** "Get in touch" in the header on every page; "Request a site review" on each project page; a timed or scroll-triggered pop-up lead magnet "Before the first line is drawn" (free guide, name, email, phone optional, suburb/postcode) which appeared over the second desktop scroll shot (trigger uncertain); "Book a free call" prompts on process and about pages; an "Open home" nav item. Contact form fields: Name*, Phone*, Email*, Confirm email, Current project stage (radio: Just getting started / Have land, ready to design and build / Have drawings and council approval), Suburb*, Postcode, Approximate build budget* (select: 1.5-2.0 / 2.0-2.5 / 2.5-3.0 / 3.0+ Million), How did you find us?, Tell us about your project*. Not multi-step, but qualifying. Two phone numbers (1300 347 128 and an Architectural Consultant mobile 0450 805 881) as tel: links; on phone, both are in the DOM and visible, though not in the first screen.

**Motion.** Background video hero (Elementor), Lenis smooth scroll, Swiper, jQuery. Images appear grey-blocked until lazy/reveal fires (project cards showed grey placeholders mid-scroll). Helps: the video establishes quality fast. Smooth scroll is mild. The pop-up interrupts reading.

**Weaknesses.** Pop-up covers content on desktop; hero is cramped on phone; budget bands start at $1.5M (right for them, would filter out most of an Adelaide mid-market); two licence numbers unexplained; only one CTA in the header; grey placeholders during scroll; no before/after.

## 2. MILEHAM Architects + Builders: https://www.mileham.com.au (Freshwater, Northern Beaches)

**First screen.** Desktop: warm off-white page, centred spaced-caps logo, serif headline "Considered Architecture. Refined Interiors. Responsible Construction.", then a full-width photo of a stone-benched kitchen opening to a garden with a mossy sandstone wall (the photo starts below the headline, so the first screen is half type, half image). Nav left: Architecture, Construction, Portfolio, About Us; right: pill button "Let's Get Started →". Phone: logo, a round menu button, the same serif headline, then the kitchen photo; below the photo there is a blank gap on first load (a reveal not yet fired; it resolved on scroll). Phone has no visible CTA in the first screen (only inside the menu).

**Projects.** Portfolio index: filter tabs (All, CDC, DA, Extensions & Additions, Internal Renovations, Knockdown Rebuilds & New Builds), cards named by story and suburb ("Contemporary Heritage Restoration, Darling Point"; "Refined Randwick Bungalow"; "Lane Cove Federation Charm"). Project page (Darling Point): a full fact sheet: Location, Project Type, Architectural Style, Site (939m2, NSW Heritage Listed, sloping, restricted access), Home Details (6 bed, 4.5 bath, pool), Scope, Engagement (Architecture, Interiors, Project Management), Approval (DA, Woollahra Council, Class 1), Status (Completed 2023). Narrative about the 1903 Arts and Crafts cottage, "Read more" expanders, 41 images, ~1,270 words, ~12,400px tall, 5 video/iframe elements. No before/after pair observed; no plans seen.

**Trust.** Licence #272736C in the footer; AIA and Master Builders Association NSW logos shown on the homepage; "award winning" claims; "Over twenty years". A "Client Stories" page with testimonials attributed by first name and suburb (e.g. "Hiam, Wheeler Heights, Northern Beaches"); I read at least two, count not taken. An about-us #process section, FAQs, a Resource Library (e.g. "DA vs CDC", "architect who is also a builder") and "In the Media".

**Enquiry path.** Pill "Let's Get Started" in the header, repeated through the page; the /enquire/ page opens with "Bring Your Vision to Life". Fields: First Name*, Last Name*, Email*, Phone*, Project Address*, Suburb*, "I require*" (select; info icon), "Investment Estimate*" (select; info icon), "Tell us about your project and what you want to achieve*". A newsletter email field in the footer. Phone: I found no visible phone number on the contact/enquire page or header; the tel: links in the DOM have empty hrefs (uncertain whether a number is hidden elsewhere). It is a form-first business.

**Motion.** GSAP 3.11.4 + ScrollTrigger, Lenis, Swiper, jQuery; a video element on the homepage. Text and image reveals; sections with pinned/slider behaviour (cards partly cut off at the viewport edge suggest a horizontal carousel). Reveals helps pace; the blank gap on phone before reveal is a flaw.

**Weaknesses.** No phone number found; first-load blank areas on phone before reveals fire; thin text-light header on a pale ground; heavy page (~12,000px for one project).

## 3. TASS architects + builders: https://tass.com.au (Surry Hills)

**First screen.** Desktop: full-bleed video of two girls in school uniform running across a lawn in front of a renovated home (people, not just architecture), soft logo "tass" top left, nav top right (About, Portfolio, Services, Contact), lower-left caption "architects + builders", a round sound toggle bottom right ("Click for sound"; "Tap for sound" on phone). No button in the hero. Phone: video fills the screen vertically (a dark blue front door), logo, hamburger, caption, sound button. Cinematic, but nothing to tap except the menu.

**Projects.** /projects/: staggered masonry of large rounded-corner photos with suburb captions only (Crows Nest, Marrickville, Petersham, Randwick, Scarborough, Balmain, Mosman, Gymea Bay). Project page (Crows Nest): large hero photo, a short subtitle "A quiet evolution, designed around light and family living", ~400 words of story (what was reshaped, tree protection, strengthening existing structure), 103 images in the DOM (including the "Other Projects" grid), 1 video, page ~10,500px. No fact table (no duration, scope list, architect credit seen).

**Trust.** "Multi-award winning boutique", "licensed builders and registered architects" (no licence number found in the pages I read), "close to 100 homes built". About page: a long "Recent awards" list (e.g. 2026 Winner MBA NSW Excellence in Housing, Gymea Bay and Balmain; 2025 Winner HIA NSW Emerging Builder of the Year; many finalists) with project names; "only a select number of projects each year"; a Team page; testimonials on the About page (#testimonials; count not taken). Process explanation is thin versus Chateau.

**Enquiry path.** Header "Contact" only; no CTA buttons in the hero. Services page splits into Build only / Architectural Design only / Architectural Design & Build. Form on /contact/: Your Name*, Contact Number*, Email*, Site Address*, Suburb*, Residential Address (if different), How Can We Help?* (Only Build / Architectural Design & Build / Architectural Design / Non-Project Enquiry) which then reveals more fields (a form with conditional follow-up questions; the DOM includes selects, several textareas and a file upload); button "Send Message". Phone 02 9937 2999 on the contact page only (tel: link there); none on the home page or in the mobile header. No budget question visible in the default state.

**Motion.** Video heroes (2 video elements on the home page), jQuery, a custom theme ("PW v.1.0"), no GSAP/Lenis detected. Staggered image placement and fade-in on scroll. The video is the whole first impression and carries real emotional content; the sound toggle is a small friction but optional.

**Weaknesses.** No CTA on the first screen; phone number buried on contact page; project pages have no facts (no scope, duration or credits); heavy page weight (100+ images per project page); the nav links overlap photos on scroll (seen in the scroll shot: the nav text sat on top of a picture, reducing legibility).

## 4. Mardini Constructions (worst): https://mardiniconstructions.com.au (Leichhardt)

**First screen.** Desktop: a full-width photo of a curved sandstone wall with a glass lift tower, under a white header holding a large black "MARDINI CONSTRUCTIONS" block logo centred, and a 9-item nav (Home, Portfolio, Services, Remedial Works, Media & Video, Awards, News, Testimonials, Contact). No headline in the hero, no button, and no H1 in the DOM (title tag: "Multi Award Winning Luxury Home Builder, Sydney"). A chevron at the bottom. The second desktop scroll shows another full-bleed photo with the nav bar tinted blue-grey over it. Phone: very large logo filling a third of the screen, a down-chevron, a small photo, then a block of justified body text ("Multi Award Winning Master Builder, Elvis Mardini ... has won 19 Awards from the MBA and HIA ... over 22 years' experience"). No call button; no phone number visible in the first screen; no tel: links on the homepage DOM.

**Projects.** /portfolios/: a plain 3-column grid of about 20 thumbnails with ALL-CAPS captions (e.g. "MANDOLONG ROAD MOSMAN", "BRONTE", "WELLNESS CENTRE IN DULWICH HILL", year-labelled older ones back to 2011). Photo quality is inconsistent (some drone, some phone-quality or detail crops, a shop interior). I did not open an individual project page; the index itself has only captions (~130 words total). Services emphasise remedial works (underpinning, brickwork, waterproofing), which muddies a premium-builder message.

**Trust.** Strong facts, poorly presented: "Builders Licence No 168676C" and ABN on the contact page, MBA and HIA logos, an Awards page, a Testimonials page (count not taken), "19 awards", "Elvis Mardini" as a named principal and a photo of an awards night. Process explanation: none seen.

**Enquiry path.** Contact page only (no CTA buttons on the home page). Form: Your Name*, Your Phone*, Your Email*, Subject, Your Request or Query, Captcha*. In my run the captcha widget showed "ERROR for site owner: Invalid site key", so the form may not be submittable (verified on the screenshot; I did not submit). Phone numbers (office 02 9568 3201, mobile 0419 714 719) and a fax number listed; fax is a dated signal.

**Motion.** Essentially none: jQuery only, a full-page photo slider/scroller with the fixed header. No scroll reveals observed.

**Weaknesses.** Broken captcha; no H1; no hero message or CTA; oversized phone logo that wastes the first screen; justified body text on a 390px screen produces rivers of white space; an 8-item nav with remedial sub-menus; inconsistent photography; no project depth; fax number; a form that asks nothing useful (no suburb, stage or budget).

---

## Patterns the best share

- A person-led or place-led first impression using real finished work: video (Chateau, TASS) or a single large interior (MILEHAM), with a short plain headline rather than a slogan list.
- The "architect + builder" or integrated-process story is stated near the top, and a dedicated process page or section explains the steps (Chateau six steps; MILEHAM "no handover").
- Project pages carry facts, not just photos: location, style, year, who designed and who built (Chateau), and at the top end scope, site size, heritage listing, approval pathway, status (MILEHAM). Photo counts are 38-100+ per project.
- Awards are tied to specific projects and bands (e.g. "HIA NSW Custom Built Home $1.5-2.0M, winner 2023" on the project page; TASS lists awards by project suburb).
- Licence number and association logos (MBA NSW, AIA) sit in the footer or homepage, not on a hidden page.
- Enquiry forms qualify: project stage, suburb/site address, budget range or investment estimate, and "what do you need" options (Chateau, MILEHAM, TASS).
- Restrained visual identity: a quiet neutral palette, one serif or fine sans, and generous space; no stock photography.
- Testimonials are attributed by name and suburb (MILEHAM) and sit on their own page.

## What none of them do well

- Phone on mobile: nobody has a persistent tap-to-call button or sticky bar; TASS buries the number on the contact page and MILEHAM shows none that I found.
- First-screen calls to action on phone: TASS shows none, Chateau shows "Get in touch" but the hero is cramped, MILEHAM's is only in the menu.
- Project pages stop short of the story buyers ask about: no duration, no contract band, no before/after or plan pairs, no "what it cost / how long" figures (MILEHAM comes closest with its fact sheet).
- Heritage renovation is not a first-class offering: only MILEHAM has a heritage project with listing details; Chateau and TASS are new-build-led. Kitchens and bathrooms, small developments and commercial fit-outs as service lines are absent or lost in nav (Profile has fit-outs and multi-residential, but on a thin site).
- Reveal animations leave blank or grey blocks on first load (Chateau cards, MILEHAM phone gap, Gremmo blank section), and heavy image/video weight with no sign of performance care.

## Caveats

- Counts such as testimonials were not taken for every site; licence meanings, award claims and the exact trigger of Chateau's pop-up are unverified.
- Gremmo's blank grey section and the Austral/Profile "no form" findings come from one run each.
- Files kept: 20 screenshots (chateau, mileham, tass, mardini; desktop-first, phone-first, desktop-scroll-2, project, contact) plus this report. For Mardini, the "project" shot is the portfolio index and for MILEHAM it is the Darling Point project page.
