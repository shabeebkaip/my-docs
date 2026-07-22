# NADEC Website Redesign — Design Direction

**Prepared for:** RFP response — website revamp, design strategy section
**Prepared by:** Code-OX (in partnership with WeCare Tech design/build)
**Date:** 22 July 2026
**Reads with:** `nadec/website-audit-findings.md` (current-state technical/UX audit), `nadec/competitor-benchmark.md` (regional peer benchmark), `nadec/seo-audit-findings.md` (Core Web Vitals baseline)

---

## 0. The brief in one paragraph

NADEC's regional competitors (Almarai, SADAFCO, Baladna, Al Safi Danone) set a low design bar — none run 3D, WebGL, or award-tier craft, and the market leader's site looks dated by 2014 standards (full findings: `competitor-benchmark.md`, Section 4). Out-designing them is achievable with clean, modern, editorial-quality execution alone. This document goes further, at the client's request: it looks past the regional category entirely, to Awwwards/FWA/CSS Design Awards-recognized work in food, dairy, agriculture, and premium FMCG from Europe and North America, and asks two questions — what elevated craft is actually available to a brand like NADEC, and how much of it is *appropriate* given (a) NADEC's conservative, publicly-listed, heritage-agricultural identity, and (b) the site's current Core Web Vitals are already failing (mobile LCP 4.8s, Lighthouse Performance 44/100 — `seo-audit-findings.md`, Section 3). Every recommendation below is written against those two constraints, not around them.

**Position for the proposal:** a restrained, premium visual layer — real dairy-farm photography and light 3D product work, not a WebGL playground — married to a genuinely fast, accessible, bilingual build. The differentiator is craft *plus* discipline, not craft alone.

---

## 1. Curated reference gallery

Eight real, named, independently verifiable sites. Each entry: what it is, the specific technique worth studying, why it has aged well (or the durability signal available), and the performance trade-off if any.

### 1.1 Simply Chocolate (simplychocolatecph.com) — Copenhagen, Denmark
**Recognition:** Awwwards Site of the Year 2017 (E-Commerce), Site of the Day, plus UI/UX/Innovation awards; CSS Design Awards Website of the Year 2017 finalist.
**Technique:** An "unwrapping" scroll narrative — each chocolate bar is presented as a 3D-rendered product that visually "unwraps" as the user scrolls, using saturated, consistent color-blocking per product line rather than photography.
**Why it's the single best durability reference in this list:** it is now nine years old (2017–2026) and is still cited by design press and still operating as the brand's live commercial site with the same conceptual bones, updated only with new products. The studio's own retrospective note is exactly the claim NADEC should want made about its own new site: it "still looks fresh to this day." The reason it aged well is structural, not decorative — the concept (product-as-hero, scroll-as-unwrapping) is tied to the product itself, not to a visual trend (no glassmorphism, no gradient mesh, no trend-of-the-year typography), so it hasn't dated the way trend-led sites do.
**Performance note:** 2017-era WebGL tooling; a 2026 rebuild of the same concept would use lighter, GPU-instanced rendering and would need explicit mobile budgeting (see Section 4) — the original predates today's Core Web Vitals discipline.
**What to steal for NADEC:** not the chocolate-specific unwrap mechanic, but the principle — build the 3D/animation concept around an actual product truth (milk pouring, cream separating, a carton opening) rather than an abstract "cool scene," so the craft still makes sense to a viewer in 2034.

### 1.2 Oatly — global site, "Infinite Canvas" campaign work (okto.co/work/oatly)
**Recognition:** Red Dot "Best of the Best" in Web Design, Webby Award (Best Homepage), Lovie Awards (Best Homepage, Best UX).
**Technique:** Not 3D/WebGL-led — instead, an "infinite canvas" horizontal-scroll layout built entirely from Oatly's illustrated, editorial brand voice (hand-drawn typography, packaging-style copywriting, playful pacing) rather than photorealism or heavy rendering.
**Why it's relevant to NADEC specifically:** Oatly proves that a food/beverage brand can win top-tier global design awards, repeatedly, across nearly a decade of site iterations, *without* leaning on WebGL or 3D at all — the craft lives in typography, layout rhythm, motion timing, and brand voice. This is the direct counter-example to "3D is what makes a site award-worthy." It also demonstrates the format's biggest weakness: Oatly's own team has been candid that translating a bold campaign concept into a *global, always-on* commerce site is harder to sustain consistently across markets than a single campaign microsite — a caution for NADEC, whose primary domain must serve investors, media, and 38,000+ retail touchpoints, not just a marketing moment.
**Performance note:** illustration/typography-led sites are inherently lighter than 3D/WebGL sites — this is the lowest-risk category on this list from a Core Web Vitals standpoint.
**What to steal for NADEC:** the proof point that restraint plus strong brand voice competes with (and sometimes beats) heavy 3D — directly supports the recommendation in Section 2 to keep 3D minimal and let editorial photography/typography carry most of the site.

### 1.3 Farm Minerals (via Adelt agency, adelt.io/cases/farm-minerals) — agricultural technology, 2026
**Recognition:** Awwwards Site of the Day, 19 February 2026 (very recent — this is a current, not historical, example of what's winning right now).
**Technique:** A 360° 3D-rotating product render and a "product dissolving in water" sequence, built with WebGL/GSAP on Webflow, communicating a complex agri-science product (soil nutrient technology) through scroll-triggered data visualization and interactive product storytelling rather than dense paragraphs of technical copy.
**Why it's the most directly relevant reference for NADEC:** it is an agriculture-adjacent B2B/B2C hybrid brand (not consumer food, but soil/farming technology) proving that 3D product storytelling works for a serious, technical, non-toy agricultural subject — the same tone NADEC needs (a public company talking about food security, quality testing, and Vision 2030 dairy scale, not a novelty D2C brand). It is recent enough that its durability can't be judged yet, which is itself a useful data point: it represents current craft, to be filtered through the aging lessons of 1.1 and 1.2, not copied wholesale.
**Performance note:** 15-page Webflow build with WebGL is a meaningfully heavier stack than a hand-built site; this is the reference to study for *technique* (dissolve/rotate sequences), not for *infrastructure* — NADEC's actual implementation should follow the lighter pattern in Section 4.
**What to steal for NADEC:** the 360° rotating product concept is directly transferable to a NADEC dairy product (a milk carton or cheese wheel rotating, with the label/nutrition panel legible) and the "dissolve" transition concept maps naturally to a "from farm to carton" or "raw milk to finished product" story beat.

### 1.4 GOOD Meat (Resn, resn.co.nz — Awwwards SOTD) — lab-grown meat / future-of-food brand
**Recognition:** Awwwards Site of the Day; built by Resn, one of the studios named in the brief as a 3D/WebGL specialist.
**Technique:** Full WebGL/Three.js/GLSL scroll-navigation experience with sound design, positioning "the future of meat" through cinematic, tactile 3D scenes rather than product photography — this is the closest thing on Awwwards to an agri-food brand running the full high-craft playbook (3D + WebGL + custom shaders + sound).
**Why this is a useful *caution*, not just an inspiration:** GOOD Meat is a venture-funded, culture-forward challenger brand selling a novel, unfamiliar product (lab-grown meat) to an early-adopter audience — the site's job is to make something unfamiliar feel exciting and legitimate through spectacle. NADEC's job is close to the opposite: it sells a familiar, trusted, 45-year-old product to mainstream Saudi households and to institutional investors simultaneously. Importing GOOD Meat's full spectacle level onto NADEC would read as tonally wrong — over-produced for a brand whose actual equity is trust, heritage, and everyday nourishment, not novelty.
**Performance note:** full Three.js/GLSL/sound builds are the heaviest tier of this reference set; appropriate only as a bounded, single-hero-scene technique, never as the site-wide pattern.
**What to steal for NADEC:** camera-following scroll choreography (the sense of "traveling through" a scene as you scroll) is a strong technique for a single homepage hero moment — e.g., traveling from farmland to processing plant to shelf — but should be the *only* place this level of craft appears on the site, not a pattern repeated across product or investor pages.

### 1.5 À l'heure du lait — "The Milking Parlour" 360 experience (ferme-laitiere-france.com) — French national dairy industry body
**Recognition:** Awwwards Site of the Day; ongoing public education site for the French dairy farming sector (CNIEL, the French national interprofessional dairy organization).
**Technique:** An actual 360° dairy-farm documentary experience — visitors navigate real farm locations (milking parlour, dairy processing unit) with 360° photography/video, layered data ("the milk files": best practices, environmental impact, milk production statistics), not synthetic 3D renders.
**Why this is the single most on-category reference found:** this is, literally, a dairy-industry storytelling site, still live, built to explain milk production, farm practices, and dairy's environmental footprint to a general public audience — the exact narrative territory NADEC's "farm-to-table," "nourishing your life," and sustainability content needs to cover. It proves the underlying content (cows, milking, processing, quality testing) can be turned into an immersive property-level attraction without inventing anything artificial — NADEC has six real dairy farms (~60,000 cows) and two real processing plants (`seo-audit-findings.md`) that can be the actual subject of this kind of experience, not a stand-in.
**Performance note:** 360°/documentary media (photography, video, layered text) is generally far lighter than full WebGL/Three.js 3D rendering — this is a strong *lower-risk* alternative to synthetic 3D for the "farm story" section of the site specifically.
**What to steal for NADEC:** build the "Our Farms" / sustainability section as a real 360°-photography or video-led walkthrough of an actual NADEC farm and plant, not a rendered 3D scene — more authentic to the brand, cheaper to build, and lighter to load than the GOOD Meat-style synthetic approach.

### 1.6 Swiss Organic Farm (Awwwards Honorable Mention)
**Recognition:** Awwwards Honorable Mention, organic farming category.
**Technique:** Parallax-driven "walk through the fields" concept — layered 2D/2.5D imagery with scroll-linked parallax depth, not full 3D rendering, communicating an organic farm's fields and products.
**Why it's relevant as a "lighter-weight" alternative:** parallax depth (foreground/midground/background layers moving at different scroll speeds) delivers a meaningful sense of dimensionality and place at a fraction of the engineering and performance cost of true WebGL 3D. This is the honest middle-tier option between "flat static site" and "full 3D/WebGL."
**Performance note:** parallax built with CSS transforms/`will-change` and IntersectionObserver-triggered reveals is achievable within a normal performance budget, unlike WebGL — no GPU shader compilation, no 3D asset loading.
**What to steal for NADEC:** a parallax field/farm hero for secondary pages (About, Sustainability, Quality) where a full 3D scene isn't warranted but a flat photo also undersells the story — this is very likely the correct technique for most of the site, reserving true 3D (Section 2) for a single homepage moment only.

### 1.7 Corphes — Organic Products (Awwwards Honorable Mention)
**Recognition:** Awwwards Honorable Mention.
**Technique:** A reverse-scrolling narrative that emulates physically climbing toward a mountaintop herb source as the user scrolls — the scroll direction itself is mapped to the product's origin story (sourced from altitude).
**Why it's relevant:** another example of scroll mechanics tied to an actual product truth (where the ingredient comes from) rather than an arbitrary animation flourish — reinforces the durability principle from Simply Chocolate (1.1): concept-led motion ages better than decoration-led motion.
**Performance note:** scroll-triggered reveals (GSAP ScrollTrigger or equivalent) with standard image/video assets — no WebGL required for this technique, making it broadly performance-safe.
**What to steal for NADEC:** map a "source to shelf" scroll narrative to NADEC's actual supply chain (farm → quality testing → processing → 38,000 distribution points) using this reveal technique, which is buildable without 3D/WebGL at all.

### 1.8 Baladna (baladna.com/en) — Qatar Exchange-listed dairy producer
**Recognition:** Not an Awwwards-tier award winner — included here deliberately as the *regional ceiling reference*, already documented in `competitor-benchmark.md`, because it sits closest to NADEC's actual constraints (public company, Gulf/GCC market, Arabic/English, IR + consumer content on one site) and is genuinely well-executed within that category: editorial photography, a warm confident palette, IR content integrated at footer level next to Recipes and Blog, and a live capital-markets banner surfaced on the consumer homepage.
**Why it belongs next to the Awwwards examples, not instead of them:** it is the proof that a GCC-listed dairy company *can* look modern and credible without 3D/WebGL at all — it establishes the floor NADEC must clear regionally, while references 1.1–1.7 establish the ceiling of craft NADEC can selectively borrow from to clear that floor by a wide margin rather than a narrow one.
**Performance note:** standard modern component-based build (accordion nav, responsive images) — no unusual performance risk.
**What to steal for NADEC:** the exact pattern for solving "investors + consumers on one site" (see `competitor-benchmark.md` Section 4) — footer-level IR integration, no separate subdomain, no visual downgrade for the investor content.

---

## 2. Recommended visual direction for NADEC

### 2.1 The core judgment call, stated plainly
Of the eight references above, the ones that should influence NADEC most are **1.2 (Oatly), 1.5 (À l'heure du lait), 1.6 (parallax), 1.7 (scroll-reveal), and 1.8 (Baladna)** — restraint, real photography/video, and concept-led scroll motion. **1.1 (Simply Chocolate) and 1.3 (Farm Minerals)** contribute one specific technique each (product rotation, dissolve transition) in a single bounded location. **1.4 (GOOD Meat)** is included as a boundary marker — the ceiling of spectacle NADEC should *not* reach for, named explicitly so the proposal shows the client this was a deliberate exclusion, not an oversight.

This is not "add less 3D because it's a Saudi client" as a vague cultural hedge — it's a direct read of NADEC's actual brand equity. NADEC is a 45-year-old (founded 1981) vertically-integrated food-security company, Tadawul-listed, with a genuinely conservative dual audience (mainstream grocery households and institutional/government-adjacent investors reading the same domain). The RFP's own tagline reference — "Nourishing your life everyday" — is a trust-and-care claim, not a novelty claim. Spectacle-first 3D (GOOD Meat's register) sells novelty; NADEC needs to sell dependability at a premium level of craft. That is a materially different, and if anything harder, design problem than "add impressive 3D" — it's closer to what Baladna and Al Safi Danone are reaching for (both flagged as the design-quality bar in `competitor-benchmark.md`) executed with meaningfully higher craft.

### 2.2 Aesthetic direction, named: "Grounded Premium"
A deliberate, single direction to keep every later decision coherent — not "modern" or "clean" (too vague to build against):

- **Real over synthetic wherever possible.** Actual farm/plant photography and video (drone footage of the six dairy farms, real processing-line footage, real product photography) is the primary visual language — not stock imagery (the current site's known gap, `website-audit-findings.md` Finding 7.3) and not synthetic 3D as a default. This is both a brand-authenticity argument (NADEC's ~60,000 cows and two plants are a genuine, differentiated asset competitors can't easily match — see `seo-audit-findings.md`) and a performance argument (photography/video is cheaper to serve well than 3D, see Section 4).
- **One 3D moment, not a 3D site.** A single, purpose-built 3D/scroll sequence lives on the homepage hero only — most likely a "farm to carton" journey (borrowing the camera-travel technique from 1.4 and the dissolve/rotate technique from 1.3, at a fraction of their visual intensity) or a rotating hero product render (borrowing 1.1's product-as-hero principle). Every other page uses photography, parallax (1.6), and scroll-reveal (1.7) — no WebGL required.
- **Brand palette carried forward, not replaced.** The audit confirms NADEC's blue (`#2B338C`/`#001971`) and green (`#7FBC42`) are already genuinely encoded in the current build (`website-audit-findings.md` Finding 7.1) — this is real brand equity, not a legacy accident, and the RFP should not pitch a palette change. The design direction is to formalize these as design tokens (Finding 7.1's own suggested direction) and pair them with a warm, natural photography palette (cream, wheat, pasture green, milk-white) so the corporate blue/green reads as trust-and-institutional accents against a warm, nourishing photographic base — rather than the flat, primary-color-block application seen at Almarai (`competitor-benchmark.md` Section 3, flagged as the dated 2014-era pattern to avoid repeating).
- **Typography carries more of the "award-tier" feeling than motion does.** Following the Oatly lesson (1.2): a confident, well-set type system (a warm serif or humanist serif for headlines evoking heritage/1981 provenance, paired with a clean grotesque for UI/body, full Arabic-optimized companion faces — see Section 6) does more sustained work than animation, and it doesn't carry the mobile-performance cost 3D does.

### 2.3 What this direction explicitly is not
- Not a WebGL playground with 3D on every page (rejects GOOD Meat's register as a sitewide pattern).
- Not a novelty/challenger-brand tone (NADEC is the incumbent, not the disruptor — Almarai is older and bigger, but NADEC's actual brand job is "trusted, established, nourishing," which the visual direction should lean into rather than fight).
- Not a redesign that discards the existing blue/green identity in pursuit of trend — that would forfeit real, already-built brand equity for no strategic reason.

---

## 3. Information architecture — proposal-stage approach

This builds directly on `website-audit-findings.md` Finding 5.1 and `competitor-benchmark.md`'s Baladna-model recommendation, translated into a page-map suitable for the RFP (not a full sitemap spec — that's a build-phase deliverable).

### 3.1 Recommended top-level model: audience-first, not department-first
Replace the current flat single-menu structure (About, Awards, Feed, Juice, Meat, Milk, News, Statistics — `website-audit-findings.md` Finding 5.1) with a persistent audience split, echoing Baladna's proven pattern but adapted to NADEC's broader category range (dairy + juice + meat + produce vs. Baladna's dairy-only):

1. **Consumers** — Products (Dairy / Juice / Meat / Produce, each with real photography and nutrition content — closing the "thin product content" gap flagged in `seo-audit-findings.md` Section 2), Recipes/Kitchen hub (net-new — closes the gap named as NADEC's single biggest content-strategy deficit versus every dairy peer, `competitor-benchmark.md` Section 4), Quality & Food Safety (surfacing the ISO 22000/9001 certifications currently buried, `website-audit-findings.md` Finding 5.6), Where to Find Us (store/retail-locator style, not e-commerce — per the category-wide no-D2C pattern confirmed across all five benchmarked competitors).
2. **Our Farms & Sustainability** — given a top-level slot of its own (not folded under "About"), because this is where the single 3D/immersive homepage moment (Section 2.2) and the 360°/documentary-style farm storytelling (reference 1.5) live — turning NADEC's real physical scale (six farms, ~60,000 cows, two plants) into the site's signature content, not a footnote.
3. **Investors** — Financial Information, Share Information, Governance, Annual Reports/Disclosures — same template family and visual system as the consumer pages (Baladna model), not a visually distinct or siloed sub-site (the SADAFCO failure mode named in `competitor-benchmark.md` as the pattern to avoid). Preserve all existing direct-linked PDF URLs during migration (`website-audit-findings.md` Finding 5.3).
4. **Media & Corporate** — News (preserve existing cadence, `website-audit-findings.md` Finding 5.4), a net-new nutrition/education blog (the Baladna-inspired white-space opportunity named in `competitor-benchmark.md` — no Saudi dairy competitor currently owns this), Awards/Recognition (surfacing existing content as the trust module suggested in Finding 5.7), press contacts.
5. **Careers** — direct, clean branded link (fixing the exposed-email Safelinks issue, Finding 5.5), not folded into Corporate.

Language switcher (AR default at root domain, preserving the deliberate current behavior per Finding 3.1) and search persist in a slim utility bar above this primary nav on every template.

### 3.2 Homepage module order (the page that carries the design direction)
1. **Hero — the one 3D/immersive moment.** Farm-to-carton scroll sequence or rotating product render (Section 2.2), with a hard static-image fallback (Section 4) for mobile/reduced-motion/low-end devices. Real tagline text ("Nourishing your life everyday" in both languages, as actual HTML text — closing Finding 3.5) overlaid, not baked into an image.
2. **Trust strip.** ISO/quality certification badges + key scale stats (litres/day, distribution points, cow count) rebuilt as lightweight CSS/JS count-up animation, replacing the current 2.9MB of animated GIFs (`website-audit-findings.md` Finding 2.2) — same visual effect, near-zero weight.
3. **Product category grid.** Real photography per category (Dairy/Juice/Meat/Produce), each card linking into the Consumers section.
4. **Recipes/Kitchen teaser.** 3–4 featured recipes pulling from the new hub — the category-standard module every dairy peer except NADEC already has.
5. **Our Farms teaser.** A single striking farm/plant photo or short video with a "go behind the scenes" CTA into the immersive Farms section — this is where curiosity is created, not resolved, on the homepage itself (keeps the homepage light; the heavier storytelling lives one click deep).
6. **News/Media strip.** Latest 3 items, both News and the new education blog.
7. **Investor snapshot.** A quiet, well-designed module (following Baladna's precedent of surfacing IR on the consumer homepage, not hiding it) — latest disclosure or financial headline, linking into the full Investors section. Not styled as an afterthought.
8. **Footer.** Full sitemap, NAP/contact data (`seo-audit-findings.md` Section 5), social, certifications repeated, careers link.

### 3.3 Product/category and article templates
Standard content templates (no 3D) built on the same token system: single `<h1>` per page (closing Finding 4.2), proper landmark regions (closing Finding 4.3), breadcrumbs (already structurally present per `seo-audit-findings.md` Section 2, needs H1 pairing), and structured data per template type (Product, Article, BreadcrumbList, Organization — closing Finding 6.3/`seo-audit-findings.md` Section 1).

---

## 4. Performance-safe implementation strategy for 3D elements

This section exists specifically because the client's current site is already failing Core Web Vitals (mobile LCP 4.8s, Lighthouse Performance 44/100, TTFB 1.7s mobile — `seo-audit-findings.md` Section 3), and any 3D recommendation that doesn't directly address that is not credible in this proposal. The strategy below is deliberately conservative.

### 4.1 Scope discipline (the biggest lever)
- **Exactly one 3D/WebGL scene, on the homepage hero only.** No 3D on product pages, category pages, investor pages, or article templates — those use photography, CSS parallax (reference 1.6), and scroll-reveal (reference 1.7), none of which require a WebGL context.
- **The hero 3D scene must not be, or overlap with, the LCP element.** The current research is explicit on this point: the LCP element should be a real image or text block that paints immediately, with `fetchpriority="high"` and no lazy-loading — the 3D canvas is layered in *after* first paint, treated as a progressive enhancement, not the thing the page waits on.

### 4.2 The mobile decision, stated as policy, not left ambiguous
- **Mobile and low-end/low-bandwidth devices receive a static, art-directed image or a short (sub-2MB) H.264/WebM video loop of the same hero concept — not the WebGL scene at all.** This is not a compromise version of the experience; it is the correct default given that mobile is already the confirmed weak platform (Performance 44 vs. desktop 67, `seo-audit-findings.md` Section 3) and is the primary channel for KSA FMCG shoppers per that same audit. The decision point: `matchMedia` viewport width plus a `prefers-reduced-motion` check plus a basic WebGL-capability check, evaluated before any 3D asset request is made — if any check fails, the static/video fallback loads and no 3D bundle is ever fetched (not deferred — never requested).
- **Desktop/tablet on adequate bandwidth get the full 3D hero**, lazy-instantiated: the 3D bundle (Three.js + assets) loads only after the initial page paint completes, using a dynamic `import()` so it's excluded from the critical-path JavaScript entirely.

### 4.3 Technical guardrails for the desktop 3D build
- Draw-call budget capped (target under 100 draw calls per frame, consistent with current WebGL performance guidance) — enforced as a build acceptance criterion, not a suggestion.
- Shader compilation and geometry/texture decoding moved off the main thread where the target browser support allows (Web Worker/OffscreenCanvas pattern), so the 3D scene initializing doesn't block input responsiveness — directly protects the INP metric, which is currently passing (142ms mobile, `seo-audit-findings.md`) and must not regress.
- Compressed, pre-optimized 3D assets only (Draco/KTX2-style compression for geometry/textures) — no raw, unoptimized exports shipped to production.
- The static fallback image is also the loading placeholder — i.e., visitors never see a blank hero while the 3D scene initializes; they see the finished-looking static frame first, and the 3D scene enhances on top of it if/when it's ready.

### 4.4 What this buys the proposal
This lets NADEC honestly claim an award-tier visual moment on the homepage while still committing to the Core Web Vitals remediation already scoped as the SEO workstream's top priority (`seo-audit-findings.md` Section 3: "prioritize mobile... LCP 4.8s, Performance 44"). The two workstreams (design ambition, performance remediation) are not in tension in this plan — they're sequenced against each other by design: the 3D investment is spent in exactly one place, gated behind capability checks, and never blocks the metrics NADEC most needs to fix.

---

## 5. Why this direction will last

The brief specifically asks for durability, not trend-chasing — the pattern across every reference in Section 1 supports a clear rule:

**What makes past Awwwards/FWA winners age well:** the craft is *tied to the product or brand truth* (Simply Chocolate's unwrap = the physical act of opening chocolate; Corphes' reverse-scroll = the physical act of climbing to source ingredients at altitude; À l'heure du lait's 360° farm tour = an actual farm you could visit) rather than to a decorative trend of the moment (a particular gradient style, a particular font pairing, a particular cursor effect). Concept-led work doesn't "expire" the way a stylistic trend does, because the concept doesn't depend on staying fashionable — the "farm to carton" 3D hero recommended in Section 2.2 is chosen specifically because it's NADEC's actual supply chain, not a borrowed motif.

**What makes past winners age badly:** heavy reliance on a specific trend-of-the-year visual language — the kind of site that reads as "very 2021" or "very 2023" the moment that year's dominant aesthetic (a particular 3D-blob style, a particular scroll-jacking pattern, a particular color-grading trend) cycles out. GOOD Meat (1.4) is included in this document as the example of *maximum current craft*, deliberately not recommended as the template to copy in full, precisely because spectacle-led sites are the ones most exposed to this risk — they read as exciting when new and can read as try-hard once the specific technique becomes common.

**Oatly (1.2) is the strongest evidence available that restraint compounds.** It has won awards across nearly a decade of iterations without ever depending on 3D/WebGL spectacle — the equity is in typography, voice, and layout discipline, which don't have a expiry date the way a rendering technique does.

**Applied to NADEC:** by keeping 3D to a single, product-truth-anchored hero moment, and building the other 95% of the site from real photography, disciplined typography, brand-token color, and lightweight scroll techniques (parallax, reveal-on-scroll) that have no dependency on any particular rendering trend, this direction is built to still look considered in 2032, not just at launch. The proposal should make this explicit to the client: the recommendation is deliberately *not* "the most 3D we could fit," it's "the most durable interpretation of award-tier craft available for a company whose brand equity is trust built over 45 years."

---

## 6. RTL / localization note

NADEC's site is Arabic-first at the root domain (`website-audit-findings.md` Finding 3.1) — this design direction must work in Arabic first, not as an afterthought:

- Any 3D/scroll-camera sequence (Section 2.2, 4.1) must be authored direction-agnostic or explicitly mirrored — a "farm to carton" camera path that reads left-to-right in English needs a validated right-to-left equivalent in Arabic, not a flipped CSS transform applied blindly to a 3D scene (3D camera paths do not auto-mirror the way 2D layout does under `dir="rtl"` — this needs to be a build-phase task, not assumed).
- Typography system (Section 2.2) requires a genuinely paired Arabic display/text face selection alongside the Latin serif/grotesque pairing — chosen and tested for the same "heritage warmth + institutional trust" register in Arabic, not a default system Arabic font applied to a bespoke Latin type system (a common and visible quality gap in bilingual Gulf sites).
- Parallax and scroll-reveal techniques (references 1.6, 1.7) mirror cleanly under RTL with standard CSS logical properties — flagged here as low-risk relative to the 3D hero.
- Carries forward the existing RTL QA recommendation already scoped in `website-audit-findings.md` (Finding 3.4) as a formal budget line, extended to explicitly include the new hero sequence and any new interactive modules, not just legacy templates.

---

*This document is a design-direction brief for proposal inclusion, not a pixel-level specification — component-level design tokens, full page templates, and interaction-state specs are a build-phase deliverable following contract award. All competitive and technical claims above are cross-referenced to `nadec/website-audit-findings.md`, `nadec/competitor-benchmark.md`, and `nadec/seo-audit-findings.md`; all external reference-site claims (Section 1) are drawn from Awwwards, CSS Design Awards, and named agency case studies as cited inline, current as of July 2026.*
