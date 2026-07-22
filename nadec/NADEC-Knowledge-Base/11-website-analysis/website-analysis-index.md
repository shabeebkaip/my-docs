# NADEC — Website/UX/SEO Analysis Index

Per project instructions, this section does NOT re-derive UX/SEO/performance findings from scratch. It indexes and cross-references the existing dedicated audit deliverables, and adds only what this content crawl newly discovered that's relevant to UX/IA.

## Primary sources (read these directly for full findings)
- `/Users/shabeeb/Documents/Shab.co/my-docs/nadec/website-audit-findings.md` — UX/navigation/accessibility/technical audit (8 sections, 30+ numbered findings)
- `/Users/shabeeb/Documents/Shab.co/my-docs/nadec/seo-audit-findings.md` — Technical/on-page/off-page/local SEO audit with scorecard
- `/Users/shabeeb/Documents/Shab.co/my-docs/nadec/pagespeed-data.md` — Raw Core Web Vitals data (PSI, 22 Jul 2026)
- `/Users/shabeeb/Documents/Shab.co/my-docs/nadec/competitor-benchmark.md` — Peer comparison (Almarai, SADAFCO, Baladna, Al Safi Danone)
- `/Users/shabeeb/Documents/Shab.co/my-docs/nadec/design-direction.md` — Recommended visual/IA direction

## New IA findings from this content crawl (not in the prior audits)

**Finding N.1 — Three sitemap-listed pages exist but render empty.** `/en/recipes`, `/en/departments`, and `/en/initiatives` all return "No results found" despite having full page templates (including working filter UI on `/en/initiatives` with "Local"/"Regional" category options). This is hard evidence of exactly the kind of "CMS content failed to publish or template has unfilled placeholder zones" pattern competitor-benchmark.md described qualitatively for the homepage — now confirmed as a sitewide pattern across at least 3 additional page templates, not a homepage-only issue. This meaningfully raises the estimated content-population effort for any CMS-retention redesign path.

**Finding N.2 — A fully-written Chairman's Speech page exists but is orphaned from navigation.** `/en/Chairman_speech` has complete, substantive content (Vision 2030 alignment, sustainability commitments, R&D focus) but is reachable only via sitemap.xml — it is not linked from the main nav, footer, or the About section (which does link to CEO's Speech). This is a discoverability bug: real content that visitors and search engines have no on-site path to find.

**Finding N.3 — The Branches/Head Quarter page is JS-rendered and did not yield branch-level data to static crawling.** Given NADEC's stated distribution scale (38,000+ outlets, 6 farms, 2 plants), the interactive map widget almost certainly contains more location data than a static HTML fetch can extract. This is the one clearly JS-dependent section encountered in this crawl — flagged transparently per crawl-methodology requirements. A rendered/headless-browser pass is needed to fully catalog branches (see `08-contact/contact-and-branches.md` for detail).

**Finding N.4 — URL pattern duplication is pervasive at the individual-link level, not just template level.** Within a single page's link set, the exact same destination is sometimes referenced as `/en/products/54` and elsewhere as `/index.php/en/products/54` — confirmed across product listings, investor links, and privacy policy links. This reinforces seo-audit-findings.md Finding 6.4 with much broader evidence (dozens of instances across the full crawl, not the 2 examples originally cited).

**Finding N.5 — Product detail pages carry zero nutrition/ingredient/SKU content**, confirmed at full-catalog scale (141 products sampled), not just the single product page (`/ar/products/284`) the original SEO audit checked. This raises the priority and estimated content-authoring scope of "expand product page content" from seo-audit-findings.md's Recommended SEO Strategy Section 2.

## How to use this folder in the RFP response
Cite `website-audit-findings.md` and `seo-audit-findings.md` directly for Master Report Sections 21-22 (UX Review, SEO Review) — those documents are the authoritative, detailed source. Use Findings N.1-N.5 above as supplementary evidence gathered during the deeper content crawl that reinforces and extends (never contradicts) the existing audits.
