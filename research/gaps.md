# Gaps: things to ask Peter

Everything on the demo comes from his current site. These are the things the new site needs that
his site does not give us, or gives us in a doubtful state. Nothing below has been invented to
fill the hole.

## Must have before anything goes live

1. **Original photographs.** Every project photo on his server is 740 x 450 px. They hold up at
   card size but not at full screen on a modern phone or laptop. Only six homepage slides exist at
   1920 px. The hero uses the Torrens Park slide (1920 x 799), which is soft on large retina
   screens. Ask for the originals from Karen Roberts Photography, and for permission to use them.
2. **A vector logo.** The only logo file is a 390 x 83 px PNG with white lettering. It is used
   as it is; it will not print or scale.
3. **Licence details.** The site says "Builder's Licence GL185386 GL/SGL56932". Confirm both
   numbers are current and what each covers. (Not checked against the CBS register.)
4. **The award, stated one way.** The footer says "Best Renovation ... up to $600,000 ... 2011";
   the Parkside page says "Excellence in Renovation and Addition ($400k to $600k category)". Which
   wording is on the certificate, and was Parkside the 2011 winner? Any awards since?
5. **Master Builders SA membership**: member number and permission to use the logo.

## Facts that may be out of date (the site was last changed in 2022)

6. "Over 25 years of experience", "full time team consists of 14", "second generation": still
   right? The demo's record strip repeats all three.
7. Peter's title. The site never says owner, director or founder. The demo says "Call Peter".
8. Phone 0411 510 558 and 08 8152 0948, the Marleston address and the email: all current?
9. The Epic "Silver", "Gold" and "Platinum" ranges are named in project text but never explained.
   Still offered? What do they mean?

## Needed for the pages still to build

10. **Testimonials.** There are two, not one: the unnamed "Owner - Payneham New Build" and Andrew
    Zoitakis (Westbourne Park extension, which has no project page). May we use both? Can the
    Payneham owner be named? The site also loads a reviews widget (Elfsight) that showed nothing
    when we looked: is there a Google review profile to link?
11. **The team.** No names, roles or portraits other than Peter. A page about the people needs
    them, with a photo of Peter at least.
12. **The process.** The site says "regular on site meetings" but not how often, who attends, or
    what the stages are. The process page needs his real sequence: consultation, design, approvals,
    build, handover, and how variations and costs are handled. Fixed price or cost plus?
13. **Project facts.** Many pages have no year, size or duration (Newton is one sentence;
    Goodwood, Tranmere, Mile End, Torrensville, Payneham, Ashford and Parkside have no dates).
    Which photographs are "before"? Only Unley is called a before and after job, and its before
    photos are not on the site.
14. **Errors on his pages to settle**: Rostrevor is dated "April 2015 - December 2014"; "Goodwood
    - In Progress" (2015) looks like the same house as the finished Goodwood new build; Hyde Park
    and Cross Rd Highgate are still written as in progress.
15. **Clients named on the site**: Stuart O'Grady and Nathan Eagleton (Velo, Victoria Park), Lang
    & Oxford Design (Glenelg), Goostrey Smith Design (Ashford), Jag Kitchens. OK to keep naming?
16. **What he wants more of.** The planner gives six kinds of work equal weight. If he wants
    mostly renovations, or no small jobs, the order and the form should say so.
17. **Service area and minimum job size**, if any.

## Found while building the full site (phase 3)

18. **Projects with no photographs of the finished work** on his site, only before or during:
    torrensville, st-peters-renovation, hyde-park, banksia-park, bridgewater, cross-road-highgate. Each of those pages says so in a marked note. Finished photographs
    would complete them.
19. **Photographs left out on purpose**: six that show a recognisable face (workers or the owner
    on site), two computer renders on the Newton page (one looks like a stock image of a couple),
    and near-duplicates. If Peter wants the people shots in, the people should agree first.
20. **Real "before" photographs exist** for Hyde Park and Golfview Heights (they carry a BEFORE
    stamp). Other projects only have "during" shots, so their pairs are labelled "During", not
    "Before". Any true before photos would be worth having.
21. **Alt text and stage labels were written by looking at each photograph**, not supplied by
    Epic. Peter or the site supervisor should skim the build sequences for anything out of order.
22. **Process page**: three marked gaps (who lodges approvals and how long they take; how often
    site meetings are held and who attends; what happens after handover).
23. **About page**: team names, roles and portraits.

## Placeholders in the demo right now

- The enquiry form validates and shows its success state but sends nowhere. The hook is
  `sendEnquiry()` in `assets/js/epic.js`.
- Rostrevor's dates are shown as "to confirm" because the published ones are impossible.
- Projects with no published year show "To confirm: year".
- The six "first thing we will ask" questions in the planner and the form are ours, written as
  sensible opening questions. They are not claims about Epic; Peter should replace them with his own.
