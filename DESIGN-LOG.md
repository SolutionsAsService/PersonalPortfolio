# DESIGN-LOG — SolutionsAsService portfolio (DADA)

Carry-forward read first: `UGC-site/CARRY-FORWARD.md` and `tulsa-plumbing-site/CARRY-FORWARD.md` (focus rings and clip-path, broad attribute selectors, fixed bars in captures, hidden inputs widening the page, measuring contrast per text node).

## 1. Traversal Plan

**Brief:** Redo the studio portfolio completely: card tiles of the best front-end sites, each linking straight to the live site.
**Mode: Adaptive** — the audience is prospective clients and collaborators; governing criterion MAYA.

### Step 0. Tooling
Same as the plumbing run: Agent tool (one sub-agent per authority), Playwright + Chrome captures (`fullshot.py`, `siteshots.py` for the 30 live candidate sites), `textcontrast.py`, no graph renderer (Mermaid text / hand-read edges).

### Seed (labels verbatim)
- Stance: `White (Kenya Hara)` (emptiness as invitation — the frame steps back so the work shows)
- Rules: `Grid Systems in Graphic Design (Josef Müller-Brockmann)`, `Designing Programmes (Karl Gerstner)`, `WCAG 2.2 Contrast and Perceivability (W3C)`
- Breaker: `Irma Boom: Biography in Books (Irma Boom)`
- Counterpoint (dotted): `The Form of the Book (Jan Tschichold)` via `boom -.->|book as object answers| tschichold`

### Panel: the same seven seats (Debord, Shklovsky, Holmes, Mace, Krug, Sharp, Bringhurst).

## 3. Panel Reports

### R0 premortem (old portfolio: `port/shots/q0-*`; contact sheet of 30 live sites `port/sheet.jpg`)
| Critic | Observed | Verdict | Requested change |
|---|---|---|---|
| Debord | broken images with alt text only; "Project Five"…; About = "This is the about page." | OBJECT, Andon | live screenshots as links; feature usable sites; drop filler pages; email |
| Shklovsky | fully habitualised template; the work's strangeness hidden | OBJECT, Andon | tiles as the art; one unexpected device; curate; a first line only this studio could write |
| Holmes | nothing works when images fail; form is the only route | OBJECT, Andon | title and purpose in text on every tile; whole-card links; direct email; curate |
| Mace | footer links ≈1.5:1 on purple; broken images; footer overlaps cards | OBJECT, Andon | alt/text per tile; whole-tile 44px links with focus; one nav; 320px check |
| Krug | page never says what the studio does; "Project Five" | OBJECT, Andon | plain who/what sentence; one big click target per tile; consistent chrome |
| Sharp | studio name absent; nothing ownable | OBJECT, Andon | name + one repeated asset; real screenshot + one-line outcome; curate to the strongest |
| Bringhurst | Arial, no hierarchy, centred ragged stacks | OBJECT, Andon | one text + one display face, scale; left-aligned measure; consistent screenshots |

Curation votes (sites named by ≥ 3 critics): UGC, WTF, Taos River, Physics Map, Developer Map, Dice Box, JARVIS, Internet Structure, Autheo, Electricity guide. Cut by ≥ 3: CSS demo, basic-*, cannabis-co, password-gen, fish-site, silly-cat.

## 2. Decision Records

## Move M1: Curate and fold to one page  (KEEP-THE-RULE)
Depends on: none
Anchors: Don't Make Me Think (Steve Krug) | How Brands Grow (Byron Sharp) via crit_brand_sharp | Counterpoint The Form of the Book (Jan Tschichold)
Intent: 17 of 30 live sites, chosen by the R0 votes plus the new Copperline, grouped Business sites (4) / Maps & atlases (6) / Tools & apps (4) / Guides (3). Excluded: unstyled or early sites, a stalled loader (History Timeline). About and Contact become sections on the one page; `/about` and `/contact` redirect there.
Alternatives rejected: (a) 8–12 only (Sharp) — the maps are a distinct strength and would vanish; filters keep 17 scannable; (b) separate project pages — every tile already goes to the live site, so a detail page is a detour.
Mode field: Advanced — an index, not a sales page; Acceptable — one page, one nav, plain headline.

## Move M2: A programme for tiles  (KEEP-THE-RULE)
Depends on: M1
Anchors: Rule Designing Programmes (Karl Gerstner) | Rule Grid Systems in Graphic Design (Josef Müller-Brockmann)
Intent: every tile is generated from `_src/projects.json` by one rule: browser bar with the real domain, a 16:10 screenshot (1200/600w, 1.7 MB for all 34 files), plate number, title, one line, "Visit <domain> ↗", tags. The whole tile is one link opening the live site in a new tab (announced to screen readers). Four business sites are featured at two columns; the rest at three.
Formal argument: the domain in the bar tells a visitor exactly where the link goes (Krug), and the tile works even if the image fails (Holmes).
Mode field: Advanced — a programme, not hand-made cards; Acceptable — the familiar browser window.

## Move M3: The fore-edge contact sheet  (BREAK)
Depends on: M2
Anchors: Breaker Irma Boom: Biography in Books (Irma Boom) | Counterpoint The Form of the Book (Jan Tschichold) | Stance White (Kenya Hara)
Intent: under the headline, every project appears as a thin vertical slice in index order, like the printed fore-edge of a book; a slice widens on hover or focus and jumps to its tile. On phones it becomes a swipeable strip. The first sight of the studio is all of the work at once.
Formal argument: Shklovsky R0 asked for "one unexpected device… a tile that behaves like the site it shows"; Boom treats the book's edge as content; Tschichold's counterpoint (the page must stay readable) is kept by putting the strip below a plain sentence, never instead of it.
Mode field: Advanced — the whole body of work as an edge; Acceptable — it is navigation with names for screen readers.

## Move M4: The frame steps back  (KEEP-THE-RULE)
Depends on: none
Anchors: Stance White (Kenya Hara) | Rule The Elements of Typographic Style (Robert Bringhurst) | Rule Interaction of Color (Josef Albers)
Intent: paper `#F3F1EC`, ink `#121212` (16.6:1), one ultramarine `#2B2FD9` (7.41:1) as the studio's single asset (mark, italic headline, link colour, hover bar); Newsreader for display, IBM Plex Sans for text, Plex Mono for catalogue metadata. The screenshots supply all other colour.
Mode field: Advanced — near-empty frame; Acceptable — measured contrast.

## Move M5: Filters and access  (KEEP-THE-RULE)
Depends on: M2
Anchors: The Principles of Universal Design (Ronald Mace et al.) | Mismatch (Kat Holmes) | 10 Usability Heuristics (Jakob Nielsen)
Intent: filter chips with counts (`aria-pressed`, 44px, live "Showing N projects" status; without JS everything shows); skip link; 3px focus rings; header wraps below 400px.
Residual diff (measured): filters show 6 / 4 / 3 / 17 cards for Maps / Business / Guides / All, with the empty grid hidden; 17 tile links, 17 distinct URLs; `textcontrast.py` 0 failing at 1280 and 390. Overflow found and fixed: the hidden labels in the strip escaped its scroll box (page 2123px wide at 390) → `position: relative` on slices; header 374px at 320 → wraps; grid tracks `1fr` refused to shrink below a no-wrap domain (323px at 320) → `minmax(0, 1fr)`. Final `scrollWidth` = viewport at 320, 360, 390, 768, 1100 and 1280.

### Deferred to the owner
- A direct email address (asked for by Debord, Holmes, Krug, Sharp). Contact currently goes to the GitHub org; add the address in `_src/template.html`.

### R1 (`port/shots/q1-*`)
| Critic | Observed | Verdict | Requested change |
|---|---|---|---|
| Debord | real screens tied to live URLs; "Every tile below opens the real, live site" is verifiable; the strip is pure image but honest | PASS | strip slices as links (already are — see below); mailto when supplied |
| Shklovsky | headline and strip estrange; parts 2–3 a uniform 3-column metronome | OBJECT (narrow) | break the grid rhythm with 2–3 larger tiles; curate |
| Holmes | R0 met; GitHub-only contact excludes non-technical clients unless the deferral reads as intentional; tags faint | PASS | say the email is coming; raise tag contrast |
| Mace | R0 met; card link names = whole card text | PASS | name links by title; label contact link |
| Krug | R0 met; "independent critique" sentence is happy talk; bare GitHub URL | OBJECT (minor) | labelled contact action; cut the sentence |
| Sharp | assets consistent; GitHub-only contact; all 17 kept | OBJECT (minor) | mailto slot; lead with the strongest |
| Bringhurst | — agent stopped by a usage limit before reporting; seat re-run in R2 | — | — |

**Premises measured before acting:**
- "Eyebrow collides with the nav on phones" (Debord, Sharp, Krug, Holmes, Mace): **refused by measurement** for the live page — at 390px the header ends at y=85 and the eyebrow starts at y=133 (`check-390.png`). The collision was in the capture: `fullshot.py` scrolled back to the top with `scrollTo(0,0)` while `html { scroll-behavior: smooth }` was set, so the full-page shot was taken mid-animation with the sticky header painted part-way down. Lever: `scrollTo({top:0, behavior:'instant'})`. This also explains the plumbing critics' "call bar mid-page" reports. OVERRULE for the page; capture tool fixed.
- "Tags faint" (Holmes): `--muted` `#5A5F6B` on paper = 5.67:1 → OVERRULE.
- "Strip frames are not links" (Debord): each `.slice` is an `<a href="#work-…">` with an sr-only title → OVERRULE.

## Move M6: Contact that reads as intentional; less happy talk  (KEEP-THE-RULE)
Depends on: M1
Anchors: Don't Make Me Think (Steve Krug) | Mismatch (Kat Holmes)
Intent: the contact link reads "Message us on GitHub", with a line under it naming the address, what to do there, and that a direct email is on its way. The "independent critique" sentence is cut from About. Card links are named by title + "Visit <domain> (opens in a new tab)" via `aria-labelledby` (Mace). Taos tags no longer claim "Booking" (unverified).
Residual diff: accessible name of tile 1 = "Copperline Plumbing Co. | Visit tulsa-plumbing-site.vercel.app (opens in a new tab)" (was the whole card's text).

## Move M7: Break the metronome  (BREAK)
Depends on: M2
Anchors: Making and Breaking the Grid (Timothy Samara) | Counterpoint Grid Systems in Graphic Design (Josef Müller-Brockmann)
Intent: two tiles (Green 3D Globe, Dungeon Dice Box) span two columns at ≥ 1101px with `grid-auto-flow: dense`, so the grid has a felt rhythm; below that width they fall back into the regular columns.
Measured: wide tiles 780px vs 376px regular at 1280; `scrollWidth` = viewport at 320, 390, 768, 1100, 1280, 1440; `textcontrast.py` 0 failing.
Declined: cutting to 8–12 sites (Sharp, Shklovsky) — the owner asked for all the pretty front-end sites; the four strongest lead at double size and filters make the rest scannable.

### R2 (`port/shots/q2-*`)
| Critic | Verdict | Note |
|---|---|---|
| Debord | PASS | strip is texture answered by the labelled grid; optional slice captions |
| Shklovsky | OBJECT (one item) | rhythm now felt (M7); phone eyebrow "ghosted" behind nav in capture |
| Holmes | OBJECT (one item) | same phone capture; tags faint |
| Mace | PASS | link names and contact met; same phone capture |
| Krug | PASS | happy talk gone; asks for a clean recapture |
| Sharp | PASS | curation decline accepted (reach across entry points); mailto slot |
| Bringhurst | PASS | R0 met; stranded words in "straight from / main" and two tile titles |

**Premise re-measured:** the R1 capture fix was **inert**: `scrollTo({top:0, behavior:'instant'})` still left `scrollY = 39` because the earlier `scrollTo(0, y)` calls in the loop were themselves smooth (inherited from `html { scroll-behavior: smooth }`) and still animating. Lever that worked: inject `html { scroll-behavior: auto !important }` before scrolling; `q2-index-m-top.jpg` re-shot and clean (header and eyebrow separate, matching the live measurement y=85 vs y=133). The page itself needed no change → OVERRULE for the design, capture tool fixed.
"Tags faint" (Holmes): 5.67:1 measured → OVERRULE.

## Move M8: Rag and the email slot  (KEEP-THE-RULE)
Depends on: M6
Anchors: The Elements of Typographic Style (Robert Bringhurst) | How Brands Grow (Byron Sharp)
Intent: `text-wrap: balance` on tile titles and lines, `pretty` on the About rows, a non-breaking space before `main`; a marked comment in `_src/template.html` where the mailto goes, so the email goes live with one edit.
Declined: per-slice crop for the Open Tabletop sliver (Debord, optional) — the strip is an index of textures by design and each slice is labelled for assistive tech.

### R3 (`port/shots/q3-*`, after M8 and the capture fix)
All seven PASS, no Andon, every seat "nothing new". Carry-overs, all non-blocking: Bringhurst (tag boxes are a taste point; `main` alone in the Ship row), Holmes and Debord (the same `main` line), Krug and Sharp (owner email).

**Measured before deciding:** the `&nbsp;` from M8 was **inert**: "from" sat at y=5362 and `main` at y=5398 (1280px). Cause: each `.facts li` is `display: grid`, so the loose text and `<code>` became separate anonymous grid items, and `<code>` went to a new grid row. No spacing character can fix that.

## Move M9: One grid item per fact value  (KEEP-THE-RULE)
Depends on: M8
Anchors: The Elements of Typographic Style (Robert Bringhurst)
Intent: wrap each About value in `<span class="v">`; label styles move to `span:not(.v)`.
Declined: unboxing the tags (Bringhurst, "a taste point, not a failure") — the boxes separate tags at a glance on busy screenshots.

### R4 (after M9) and R5 (confirmation, files byte-identical)
Both rounds: all seven PASS, no Andon, every seat "nothing new". Carry-overs only: Bringhurst's taste point on the boxed tags (declined, M9); the owner's email (Sharp, Krug, Debord, Holmes). Debord's optional `title` on slices is not taken: slices already carry sr-only names, and a hover title would duplicate the tile caption beneath. No ADAPT, SCRAP, REOPEN or new OPEN item in either round.

## 2f. Deletion review
| Inherited | Verdict | Note |
|---|---|---|
| "Welcome to My Portfolio", purple Arial template | SCRAP | — |
| Eight project links with broken images, "Project Five–Eight" | SCRAP | replaced by 17 live, screenshotted tiles |
| `about.html` ("This is the about page.") and `contact.html` (form with no recipient) | SCRAP; folded into sections; `/about` and `/contact` redirect | — |
| Early sites (CSS demo, basic stat/rafting, cannabis-co, Thomas Sowell, password-gen, fish, silly-cat) | Left out of the index; the repos and their live sites are untouched | R0 votes from 5+ critics |

## 2g. Figures the page prints, re-measured at the final state
| Printed | Procedure | Value | Result |
|---|---|---|---|
| "18 live projects" (eyebrow, All chip, meta) | `len(projects)` in `_src/projects.json`; cards in `index.html` | 18 / 18 | reproducible |
| Chip counts 4 / 6 / 4 / 4 | count by `group` | business 4, maps 6, tools 4, guides 4 | reproducible |
| Plates No. 01–18 | `No. (\d\d)` in `index.html` | 01…18 | reproducible |
| Strip slices | count `.slice` | 18 | reproducible |
| "Every tile below opens the real, live site" | HTTP GET on all 18 tile URLs | 18 × HTTP 200 (2026-10-27) | reproducible |
| Contrast | `textcontrast.py` at 1280 and 390 | 0 failing | reproducible |

## 4. Anchor Ledger
| Anchor | Role | Status | Evidence |
|---|---|---|---|
| White (Kenya Hara) | Stance | KEEP | paper frame; the screenshots carry the colour; survived Shklovsky R1 ("metronome") via M7 |
| Grid Systems in Graphic Design (Josef Müller-Brockmann) | Rule / counterpoint | KEEP | 3- and 2-column grids, `minmax(0, 1fr)` |
| Designing Programmes (Karl Gerstner) | Rule | KEEP | every tile generated from one data file by one rule |
| WCAG 2.2 Contrast and Perceivability (W3C) | Rule | KEEP | 0 failing; ultramarine 7.41:1 |
| Irma Boom: Biography in Books (Irma Boom) | Breaker | KEEP | fore-edge contact strip; survived Debord ("texture") |
| The Form of the Book (Jan Tschichold) | Counterpoint (dotted) | KEEP | the strip sits below a plain sentence, never instead of it |
| Making and Breaking the Grid (Timothy Samara) | Breaker | KEEP | wide tiles (M7) |
| The Elements of Typographic Style (Robert Bringhurst) | Rule | KEEP | scale, rag, the Ship-row fix (M9) |
| Don't Make Me Think (Steve Krug) | Rule | KEEP | plain headline, labelled contact, no happy talk |
| How Brands Grow (Byron Sharp) | Lens | KEEP | one mark, one colour, one tile shape |
| Mismatch / The Principles of Universal Design | Welcome | KEEP | whole-tile links named by title, 44px targets, honest contact |

## Stop test
- **S1** No OPEN Frontier items. Owner deferral: a direct email (slot marked in `_src/template.html`). **Met.**
- **S2** All-PASS WHOLE rounds without Andon: R3, R4, R5. **Met.**
- **S3** Two consecutive rounds with no ADAPT/SCRAP/REOPEN/new OPEN item: R4 and R5. **Met.**
- **S4** Ambition push: the boldest move (M3, the fore-edge strip) was escalated by M7, carrying its "unequal slices" logic into the grid as two double-width tiles. Measured: wide tiles 780px against 376px regular at 1280; Shklovsky R2: "rhythm, not metronome". **Met.**
- **S5** Dotted edge `boom -.-> tschichold` applied (strip under a plain sentence); critic pairs Sharp ↔ Shklovsky (curation) resolved by keeping all 17 sites with the strongest four leading. **Met.**

## Double loop
The panel's main failure in this run came from the instrument, not the doctrine. Five critics reported a phone-header collision that existed only in the capture, because the capture tool scrolled with smooth scrolling still on. My first fix was inert (`scrollY` still 39), and it took a measurement to find the real lever. The same artefact had already produced the "call bar mid-page" reports on the plumbing site. **Graph amendment:** add a node "Instrument check" to the Panel Method cluster with the edge `c_genchi -->|verify the capture against the live page before tabling a premise for| CRITICS`, so any finding seen only in a screenshot is measured on the live page before a move is spent on it.

## 5. Compliance Check
- [x] Tooling inventory; mode with reason; seed with a dotted counterpoint; living Frontier (§1, R0 votes)
- [x] BREAK moves (M3, M7); no quota; stopped on S1–S5 after 9 moves and 6 rounds
- [x] Decision Records before moves. **Deviation:** batched (M1–M5, M6–M7, M8, M9), not one at a time
- [x] Panels per WHOLE round, 7 seats, one sub-agent per authority. **Deviation:** one panel per batch, not per move; Bringhurst's R1 seat failed on a usage limit and was re-run in R2
- [x] Every OBJECT resolved; OVERRULEs by measurement recorded (phone collision, tag contrast, strip links)
- [x] S1–S5 shown; 2g at final state; Anchor Ledger; double loop; final reply states mode, tools and skips
