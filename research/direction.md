# Direction: Epic Building Group

One page. Proved by one screen: the homepage hero and the section under it (`index.html`).
Screenshots and clips are in `research/direction/`.

The first attempt (cream ground, serif headline, mono labels, the photograph in a ruled card) was
rejected on 11 Nov 2026 as generic. This is the second direction, and it starts from the opposite
end: what a builder's own things look like. A site sign. A black iron fence. A sandstone wall. A
drawing pinned up in a site office.

## The idea

**The first screen is a black sheet, and the house gets built on it.** Epic's Torrens Park home is
drawn in white line from the footings up (footings, walls, portico, roof, front fence), at the full
width of the screen. Then the sheet lifts like a blind and the photograph of the finished home is
standing exactly where the drawing was. The lines are traced from that photograph, so they land on
it. It takes six seconds, plays once, and can be played again.

Nobody among the 50 builders' sites we opened uses motion to show building. They use it to set a
mood. This one explains the job: it goes up in order, and someone is counting the stages.

## Identity

Epic's, not Lumen's. No gradient, no ink art, no pills, no cards.

- **Iron and stone.** The site is black wrought iron and pale lime render, with sandstone for
  numbers. Those are the materials in their own best photograph.
- **Their red, used as a brand colour.** Sampled from the three beams of their mark. It is the
  colour of every action and of the small three-bar "beam" that marks a section or a choice.
- **Their real logo**, untouched, on the iron header.
- **Type like a site sign.** One family, Archivo, in three widths: wide and heavy capitals for
  headlines, normal for reading, condensed capitals for labels. No serif, no monospace.
- **Square.** No rounded corners anywhere. Masonry has none.
- **Photographs at full bleed**, never in a frame. Captions set on the photograph in capitals.
- **Facts at scale.** The licence number, the award year and the team size are set as large as a
  headline, because they are the proof.

## Tokens

Colour
| Token | Value | Use |
|---|---|---|
| `--iron` | `#0e1011` | dark ground, header, hero sheet, footer |
| `--bone` | `#f3eee4` | light ground; text on iron (16.6:1) |
| `--sand` | `#cfb07a` | numerals and marks on iron (8.9:1) |
| `--ink` | `#101213` | text on bone |
| `--ink-2` | `#454b4f` | secondary text on bone (8.4:1) |
| `--mist` | `#b9b6ad` | secondary text on iron (9.3:1) |
| `--red` | `#b01f2c` | actions, the beam; white text on it is 6.9:1 |
| `--red-2` | `#8f1722` | pressed |
| rules | bone at 18% on iron, ink at 16% on bone | 1px dividers; 2px ink rule opens a list |

Type (Archivo variable, self-hosted, 44 KB, `font-display: swap`)
| Style | Width / weight | Size | Leading / tracking |
|---|---|---|---|
| Shout (h1) | 122% / 760, capitals | clamp(39px, 6.9vw, 116px) | 0.92 / -0.035em |
| H2 | 122% / 740, capitals | clamp(34px, 5vw, 80px) | 0.96 / -0.032em |
| H3 | 110% / 680 | clamp(24px, 2.4vw, 36px) | 1.08 / -0.02em |
| Lede | 100% / 400 | clamp(17px, 1.4vw, 20px) | 1.5 |
| Body | 100% / 400 | 17px (never under 16) | 1.55 |
| Label | 82% / 650, capitals | 13px (the smallest text on the site) | 1.3 / 0.14em |

Spacing: a 4px module: 8, 12, 16, 24, 32, 48, 64, 96. Section padding clamp(72px, 10vw, 152px).
Gutter clamp(20px, 4.2vw, 64px). Measure 1440px.

Radius: 0.

Shadow: none at rest. One, `--lift` (`0 10px 20px rgba(0,0,0,.18), 0 30px 60px rgba(0,0,0,.22)`),
under a button while it is hovered.

Motion
- Durations: 150ms (colour), 350ms (press, hover), 700ms (marks), about 1s (a stage of the build).
- Easing: `--ease-out` cubic-bezier(.2,.7,.2,1) for arrivals; `--ease-in-out`
  cubic-bezier(.65,0,.2,1) for the sheet; `--spring` (a `linear()` spring, with a cubic-bezier
  fallback) for anything pressed, lifted or marked.
- Things are built, not faded: lines and photographs rise from their foot with `clip-path`.
  Words step up 26px, 90ms apart.
- Every button, choice and link has hover, press and focus states. The hero leans a few pixels
  toward the pointer.
- Only transform, opacity, clip-path and colour are animated. The finished state is the default
  in the CSS, so with reduced motion or JavaScript off the page is simply complete. No scroll
  hijacking; nothing moves the layout.

## What the proof screen shows

1. **Hero**: the build, the statement "Traditional Master Builders." in their own words, one
   sentence on what they do, and two actions: start a project conversation, or call Peter. Both
   are on the first phone screen, and a call and enquire bar follows down the page on phones.
2. **The record**: licence, 2011 Master Builders SA award, team of 14, 25+ years, second
   generation. Each is a statement on their current site.
3. **What are you planning?** Six choices in large type. Picking one brings up a real Epic job of
   that kind, built from its foot like the hero, and the first question the enquiry form will ask
   for that kind of work. It is radio buttons and CSS, so it works without JavaScript and by
   keyboard, and the button carries the choice to the contact page (`/contact?type=...`).

## Measured (local server, Lighthouse 12 phone emulation, three runs, 11 Nov 2026)

Performance 100, accessibility 100, best practices 100. LCP 1.7 s, total blocking time 0 to 20 ms,
layout shift 0, page weight 169 KB. (SEO reads 63 only because the demo is deliberately noindex.)
Their live homepage on the same test: performance 44, LCP 5.2 s, 5,147 KB.

Checked at 390, 768, 1024 and 1440 wide: no sideways scroll, no tap target under 44px, no text
under 13px. Checked with reduced motion and with JavaScript off: complete and usable.

## How the rest follows from this

- Project pages open the same way: that project's photograph at full bleed with its facts set
  large, then the build told in order using their own site photographs (Ovingham, Highgate, Field
  Street and Torrensville all have footings-to-finish sets), then a gallery that opens full screen.
- Before and after as a still pair: the old in grey, the new in colour, the red beam between.
- Process as five stages down an iron rail, with the weekly site meeting marked along it.
- The enquiry form takes the choice made here as its first answer.
