# NADEC Website Redesign — Competitive & Peer Benchmark

Prepared for: NADEC (National Agricultural Development Company) RFP — Website Redesign, Bilingual AR/EN, Design System
Scope: Direct competitor benchmark (Almarai) + regional/global dairy-FMCG peers, evaluated for design, IA, bilingual quality, content strategy, and investor-relations integration.
Method: Live inspection of each site (desktop rendering, navigation structure, content architecture) in July 2026. Findings below are evidence-based observations from the live sites, not vendor marketing claims.

---

## 1. Sites Benchmarked

| Site | Why it's in scope |
|---|---|
| **NADEC** (nadec.com/en) — baseline | The client's current site — establishes the starting point every peer is compared against |
| **Almarai** (almarai.com/en) | The dominant KSA dairy competitor and NADEC's #1 direct rival; also Tadawul-listed (TASI: 2280) |
| **SADAFCO / Saudia** (sadafco.com) | Second Saudi dairy/FMCG public company (TASI: 2270) — closest apples-to-apples comparator for a *listed* Saudi F&B site handling IR + consumer content together |
| **Baladna** (baladna.com/en) | Qatar's largest dairy producer, listed on Qatar Exchange — best-in-class regional example of IR fully woven into a modern consumer site, included as the aspirational benchmark |
| **Al Safi Danone** (alsafidanone.com) | Saudi dairy/juice JV with Danone — private company, included to show what a lean, design-led (not IR-encumbered) dairy brand site looks like |

NADEC is itself a **Tadawul-listed public company (ticker 6010, NADEC:AB)**, so the IR-integration comparison across Almarai, SADAFCO and Baladna is the single most decision-relevant thread in this benchmark — all three are public and all three solved "investors + consumers on one site" differently.

---

## 2. NADEC — Current Site Baseline

Before benchmarking peers, the current state is worth recording precisely, since it's the delta the new site has to close.

- **Domain confusion:** `nadec.com.sa` serves an HTTPS certificate for `*.azurewebsites.net` — a broken/misconfigured domain-to-hosting mapping. The real, working site is `nadec.com`. This is a technical/trust issue worth flagging to IT early (mismatched certs trigger browser security warnings and erode trust for a listed company) — separate from the redesign scope but should be fixed in parallel.
- **Content gaps on the live homepage:** large sections of the homepage render as empty white/grey space — an "Our Values" block with no copy, a product grid with white boxes instead of product images, and a "Key Awards" section with no cards populated. This isn't a design opinion, it's the page as currently served — CMS content either failed to publish or the template has unfilled placeholder zones.
- **IA is comprehensive but master-brand only:** About, Social Responsibility, Products (Dairy, Juices, Red Meat, Food/Vegetables, Solutions, Innovation), Investors, Sustainability, Media Center, Contact — seven top-level sections plus a working AR/EN switcher. This is actually a *simpler* brand architecture than Almarai (single master brand vs. Almarai's 12-brand portfolio), which is an advantage NADEC should keep, not add complexity to.
- **Investor Relations is already integrated** into the main nav (not a separate portal) with presentations, annual reports and governance docs — structurally sound, but styled with the same dated visual system as the rest of the site.
- **Performance (PageSpeed Insights, July 2026):** Mobile Core Web Vitals **fail** — LCP 4.8s, TTFB 1.7s, mobile Lighthouse Performance score 44/100. Desktop also fails CWV, with a CLS of 0.62 (significant layout shift, likely late-loading images). SEO Lighthouse score is already a healthy 92, so the redesign's performance win is about Core Web Vitals remediation, not basic on-page SEO. *(Full data: `nadec/pagespeed-data.md`.)*
- **No recipe hub, no dedicated nutrition content surfaced on-page**, despite NADEC's product range spanning dairy, juice, meat and vegetables — a real content-strategy gap relative to every dairy peer benchmarked below.

---

## 3. Comparison Table

| Dimension | NADEC (current) | Almarai | SADAFCO | Baladna | Al Safi Danone |
|---|---|---|---|---|---|
| **Public/Private** | Public (Tadawul 6010) | Public (Tadawul 2280) | Public (Tadawul 2270) | Public (Qatar Exchange) | Private (Savola/Danone JV) |
| **Visual identity** | Dated — icon/SVG-led, generic stock imagery, large unstyled gaps | Dated — cartoon mascots, heavy flat color blocks, 2014-era feel despite market leadership | Clean/corporate but visibly unfinished — placeholder SVGs in production | Modern — editorial photography, warm maroon brand palette, confident typography | Most modern of the set — full-bleed lifestyle photography, generous whitespace, minimal chrome |
| **Homepage IA** | 7 top-level items, single master brand | 9 items across a 12-brand portfolio (heavier IA load) | 7 items, ESG folded under one umbrella menu | 6 items, tight and current | 6 items, tightest of all — About, Brands, Kitchen, Careers, News, Contact |
| **Product catalog pattern** | Category grid, cards mostly broken/empty on live site | Deep, brand-first catalog (must navigate brand → category) reflecting portfolio complexity | Category cards with PDF catalog fallback — thin on-page depth | Accordion-style category list (Fresh Milk, Yoghurt, Cheese, Chilled Juice) — light, fast to scan | Small curated "innovations" carousel, not a full catalog — brand-page depth lives elsewhere |
| **E-commerce** | None | None | None | None | None |
| **D2C pattern across category** | — | None of the five sites sell direct — all route to retail/points-of-sale. This is category-normal, not a NADEC gap. | | | |
| **Bilingual AR/EN** | Working toggle, but Arabic parity of the broken/empty sections is unverified | Working toggle, RTL Arabic homepage as default entry | Working toggle, straightforward | Working toggle | Working toggle, `/ar` sub-path |
| **IR integration model** | **Integrated** — nav-level "Investors" tab, same template as rest of site | **Integrated but heavy** — dedicated IR sub-nav (Financial Info, Share Info, Governance, Investor App) under "Corporate," styled distinctly from consumer pages | **Siloed** — IR redirects to a separate subdomain (`sadafcoir.sadafco.com`), breaking brand continuity | **Best-in-class integrated** — Financial Information and Share Information are just footer categories next to Recipes and Blog; a live "Rights Issue" capital-raise banner surfaces directly on the consumer homepage | N/A — private company, no IR |
| **Content: recipes** | Absent | Strong — dedicated "Recipes" nav item, cook-time-tagged cards on homepage | Absent from homepage | Strong — "Products in the Kitchen" homepage module + dedicated recipes nav item | Strong — branded "AlSafi Kitchen" hub as a top-level nav item |
| **Content: sustainability/CSR** | Present under "Social Responsibility" but compliance-toned | "Almarai Cares" homepage module, community/training framing | Strong — carbon-neutral 2060 / fleet-electrification 2045 targets stated with dates, ESG menu | "We Care" nav item + environmental commitments (tree-planting pledges) tied to national moments (Qatar National Day) | Folded into "About Us" narrative only |
| **Content: blog/editorial** | News-only ("Media Center") | None distinct from news | News only | **Dedicated dated blog** with dairy/nutrition educational articles (e.g. "Does Dairy Cause Inflammation?") — real SEO/content-marketing asset | None |
| **Nutrition info** | Not surfaced on-page | Not prominent on homepage | Referenced but not homepage-prominent | Educational blog covers nutrition topics | Not prominent |
| **Trust/scale signals** | Stats present (21,000 quality tests, 1.5M liters/day, 38,000 outlets) but sit in a mostly-empty section | Strong stat bar (4M liters/day, 220,000 points of sale, 12,000-vehicle fleet) tied to a "Corporate Profile" CTA | Heritage framing ("Since 1976") | Stat bar (3,760 points of sale, 250 products, 22,860 cows) — cow count as an authenticity signal | Heritage framing ("Since 1979," Danone JV since 2001) |
| **Known technical/UX bugs observed** | Empty content blocks, broken product images, empty awards section, mismatched-cert domain, failing Core Web Vitals | "Our Brands" logo grid renders as a large blank gap (asset-loading failure) | Placeholder SVGs live in production | None observed beyond standard lazy-load gaps | Product carousel duplicates items (broken loop logic) |
| **Mobile cues** | Confirmed failing on real Core Web Vitals data (mobile LCP 4.8s, Perf score 44/100) | Structurally responsive but same asset-loading issues likely compound on mobile | Nested 3-level dropdown menus flagged as a mobile-friction risk | Modern component structure (accordion nav, mobile hamburger) suggests better mobile handling | Simple single-page structure, low complexity to break on mobile |

---

## 4. What NADEC's New Site Should Learn From — and Differentiate On

**Learn from Baladna: make Investor Relations a citizen of the homepage, not a walled-off portal.** Baladna is the only public company in this set that treats "Financial Information" and "Share Information" as ordinary footer categories sitting next to Recipes and Blog — and it goes further, surfacing a live capital-markets event (a rights issue) as a homepage banner. SADAFCO shows the failure mode: kicking investors off to a separate subdomain (`sadafcoir.sadafco.com`) breaks brand continuity and makes the IR experience feel bolted-on. NADEC's current site already has the right instinct (IR is in the main nav, not a subdomain) — the redesign should keep that integration and lift the visual execution to Baladna's level, rather than regress toward SADAFCO's siloed model.

**Learn from Almarai and Baladna: build a recipe hub and lean into it as a retention/SEO engine.** Every dairy peer except NADEC has a dedicated recipes destination (Almarai: cook-time-tagged cards; Baladna: "Products in the Kitchen"; Al Safi Danone: branded "AlSafi Kitchen"). This is category-standard, not optional — recipes are how dairy/FMCG brands turn a transactional product page into a reason to come back, and they're a natural long-tail SEO surface ("chicken tawouk recipe," "how to make labneh") that NADEC is currently ceding entirely to competitors. Given NADEC's broader range (dairy *and* produce *and* meat), a recipe hub is arguably a bigger opportunity for NADEC than for single-category peers.

**Learn from Baladna's blog: own the nutrition-education conversation.** Baladna's dated, categorized blog ("6 Signs Your Yoghurt Has Gone Bad," "Does Dairy Cause Inflammation?") is the only real content-marketing asset found across all five sites. None of the Saudi players (NADEC, Almarai, SADAFCO) have anything comparable. This is white space in the *Saudi* market specifically — a bilingual, well-tagged nutrition/education blog would differentiate NADEC from Almarai and SADAFCO immediately, not just catch up to a competitor.

**Differentiate on brand-architecture simplicity.** Almarai's site has to serve 12 sub-brands (Almarai, Lusine, 7DAYS, Alyoum, Nura, Evolac, SureGrow, surenutri, Farm's Select, Ice Leaf, Almira, Seama, Bashayer), which forces a heavier, brand-first navigation model and visibly strains their IA. NADEC operates as a single master brand across dairy, juice, meat and produce. The redesign should treat this as a genuine advantage — a flatter, faster, more scannable category structure than Almarai can offer — rather than importing Almarai's brand-portfolio complexity NADEC doesn't have.

**Differentiate on execution quality Almarai and SADAFCO are both currently failing at.** Almarai is the market leader but its site reads as 2014-era: cartoon milk-carton mascots, flat primary-color blocking, and a broken "Our Brands" logo grid that renders as a large blank gap. SADAFCO's site has placeholder SVGs live in production. Neither looks like a company confident in its digital presence. NADEC does not need to out-spend Almarai's marketing budget to out-design Almarai's website — the bar set by the market leader is genuinely low. Al Safi Danone (the smallest, private player in this set) has the strongest visual execution of any site benchmarked: full-bleed lifestyle photography, restrained color use, generous whitespace, curved section transitions. That's the design quality bar for the redesign, not Almarai's.

**Fix the physical trust and performance problems before anything else ships.** No amount of new visual design fixes a mismatched SSL certificate on `nadec.com.sa` or a mobile Core Web Vitals score of 44/100. These are foundational — a listed company's investor-facing site throwing a browser security warning, or taking 4.8 seconds to become usable on mobile, undermines credibility in a way no homepage redesign can offset. This should be sequenced as a parallel technical workstream, not folded silently into "redesign" scope.

**Do not chase e-commerce.** None of the five sites — including the market leader — sell direct-to-consumer. This is a structural, category-wide pattern (retail/distribution-led go-to-market, not D2C) rather than a gap any of them are leaving open. Unless NADEC has an explicit D2C strategy decision already made internally, the redesign should route "where to buy" to retail/points-of-sale rather than build cart/checkout infrastructure nobody in the category has validated demand for.

---

## 5. Summary Positioning for the Proposal

NADEC's new site should be pitched as: **the first Saudi dairy/FMCG site to combine Baladna-grade investor-relations integration, Al Safi Danone-grade visual design, and a nutrition/recipe content engine none of its direct Saudi competitors (Almarai, SADAFCO) currently have.** That combination doesn't exist anywhere in the peer set today — it's a genuine "first in market" claim, not a catch-up pitch, and it should headline the design strategy section of the proposal.

---

*Sources: live inspection of nadec.com/en, almarai.com/en, sadafco.com, baladna.com/en, and alsafidanone.com, July 2026. NADEC performance data from `nadec/pagespeed-data.md` (PageSpeed Insights, 22 Jul 2026). Screenshots captured during this research are saved in `nadec/` (`almarai-home.png`, `nadec-home.png`, `alsafidanone-home.png`, `baladna-home.png`) for internal reference.*
