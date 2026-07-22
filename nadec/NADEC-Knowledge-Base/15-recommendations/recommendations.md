# NADEC — Content & Knowledge-Base-Derived Recommendations

These are recommendations arising specifically from the content crawl (org, products, news, investors, documents, social, contact). For UX/SEO/performance/design recommendations, see the existing dedicated deliverables (website-audit-findings.md, seo-audit-findings.md, design-direction.md) — not duplicated here.

## Content-population priorities (new evidence this crawl surfaced)
1. **Populate or remove the three empty page templates** (`/en/recipes`, `/en/departments`, `/en/initiatives`) — either commit to building out this content (Recipes especially, per competitor-benchmark.md's identified white-space opportunity) or remove the orphaned/empty templates so they stop returning "No results found" to visitors and crawlers.
2. **Link the Chairman's Speech into primary navigation**, alongside the CEO's Speech — real, substantive content is currently undiscoverable by normal site navigation.
3. **Author real product content at scale**: nutrition facts, ingredients, allergen info, and SKU/barcode data are absent across all 141 products sampled (100% of the catalog checked). This is the single largest content-authoring line item for the redesign and should be budgeted as a distinct workstream (likely requiring input from NADEC's quality/regulatory team, not just marketing).
4. **Reconcile the two conflicting "daily quality tests" figures** (21,000+ on homepage vs. 13,000+ on Quality page) before either number is carried into new site copy or the RFP proposal itself.
5. **Fix the exposed internal email in the careers Safelinks URL** and replace with a clean branded careers link (carried forward from website-audit-findings.md Finding 5.5, re-confirmed present).
6. **Surface the KAUST research partnership and other named partnership news** (Georgia, Japan, Social Development Bank) as actual content on `/en/research` and `/en/partnerships`, which currently describe partnerships only in generic terms despite specific, citable examples existing in the news archive.
7. **Publish a press/media kit page** with downloadable logo assets and brand guidelines — none was found on the current site.
8. **Resolve the "feed" URL slug vs. "Food and Vegetables" page title mismatch** — likely a legacy holdover from an earlier IA (possibly an animal-feed section) and worth cleaning up during URL restructuring (ties to seo-audit-findings.md's product-URL-slug recommendation).

## Governance/IR content strategy
9. **Reflect the SALIC 38.648% shareholding and full ownership structure prominently** in the new Investors section — this is exactly the kind of "quiet, well-designed" investor snapshot module design-direction.md Section 3.2 recommends for the homepage.
10. **Time the new site's Investors section launch to complement, not compete with, the 2026 governance-documentation refresh** already underway (12 of 16 governance docs updated Feb-May 2026) — the content is already being modernized; the visual/template layer should catch up in the same cycle.

## Social/digital
11. **Standardize the social handle naming** across platforms (`nadecfoods` vs `nadec.com.sa` vs `NadecKSA` vs `nadecfood`) as part of any broader digital-brand-consistency workstream.
12. **Commission a live social-media audit** (follower counts, engagement, posting cadence per platform) as an explicit discovery-phase task if the RFP scope includes social strategy — none of that data is published on-site and none should be assumed/estimated.

## Branches/locations
13. **Budget a headless-browser data-extraction pass** (or request direct data-export access from NADEC) to fully enumerate branch/distribution-point locations — the current map widget is JS-rendered and not crawlable via standard HTTP fetch, and this is likely a genuinely large dataset given the stated 38,000+ distribution points.
