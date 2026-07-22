# NADEC — SEO Audit Findings & Strategy
### Prepared for: RFP Technical Proposal — SEO Scope
### Domain audited: https://www.nadec.com/ (AR/EN)
### Audit date: 22 July 2026

**Scope alignment:** This audit is structured against the five SEO sub-items defined in NADEC's RFP — (1) Technical SEO, (2) On-Page SEO, (3) Performance/Core Web Vitals, (4) Off-Page Authority, (5) Local SEO — so it can be inserted directly into the corresponding section of the technical proposal.

**Methodology note:** Findings below are based on direct inspection of live site responses (HTML source, HTTP headers, robots.txt, XML sitemap) captured on 22 July 2026, plus Google PageSpeed Insights / Chrome UX Report field data for the same date. Off-page authority metrics (Domain Rating, backlink counts) require a licensed tool (Ahrefs/SEMrush/Moz) that was not available in this session — those figures are flagged as **provisional/directional** and should be pulled live before the proposal is finalized. All other findings below were directly verified against the live site and are not estimates.

**Company context (verified):** NADEC (National Agricultural Development Company) is a Tadawul-listed public company (ticker 6010, NADEC:AB), founded 1981, headquartered in Riyadh. Vertically integrated dairy/agri/FMCG operation — six dairy farms (~60,000 cows), two dairy plants (1.5M+ litres/day), 38,000+ distribution points nationally. Primary KSA dairy/FMCG competitor: Almarai (founded 1977, also Tadawul-listed, larger scale). This scale and public-company profile is directly relevant to the off-page and local SEO opportunity sections below.

---

## SEO Scorecard (provisional)

| Area | Score | Basis |
|---|---|---|
| Technical SEO | 58/100 | Verified: strong security/infra foundation, but no hreflang, no structured data, incomplete sitemap |
| On-Page SEO | 55/100 | Verified: good title/meta baseline, but missing H1s, duplicate meta descriptions, thin product content |
| Core Web Vitals / Performance | 40/100 | Verified via PSI/CrUX: CWV fails on both mobile and desktop |
| Off-Page Authority | N/A (provisional) | No licensed backlink tool in this session — qualitative signals only, see Section 4 |
| Local SEO | 45/100 | Verified: NAP + branch data present but not machine-readable; GBP status not verified |

Scores reflect **current-state opportunity sizing** for the proposal, not a pass/fail grade — NADEC has already committed to a revamp, and every item below is framed as scope for that engagement rather than a criticism of the existing build.

---

## 1. Technical SEO

**What's already working well** (verified):
- HTTPS is correctly enforced — `http://nadec.com` returns a clean 301 redirect to `https://www.nadec.com/`, and the site sends `Strict-Transport-Security: max-age=31536000; includeSubDomains`.
- Strong security header baseline: Content-Security-Policy, `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `X-XSS-Protection`. HTTP/2 confirmed, HTTP/3 advertised via `alt-svc`.
- Cloudflare sits in front of the origin (CDN + edge caching + DDoS mitigation).
- CSS/JS are server-side aggregated (Drupal asset aggregation: homepage loads only 2 CSS files and 3 JS files) — request count is not a bottleneck.
- Canonical tags are present and correctly self-referencing on every template tested (AR homepage → `/ar`, EN homepage → `/en`, product page → its own URL). No canonical conflicts found.
- `viewport` meta tag is correctly configured for mobile rendering, and native `loading="lazy"` is applied to 34 of 51 images on the homepage.
- `lang`/`dir` attributes are correctly set per locale (`lang="ar" dir="rtl"` vs. `lang="en" dir="ltr"`).

**Opportunities identified** (verified):
- **No hreflang annotations.** The AR/EN language switcher exists in the UI and the site correctly serves two full language versions, but there is no `<link rel="alternate" hreflang="ar|en" href="...">` markup in either page's `<head>`. Without this, Google has no explicit signal that the AR and EN pages are translations of one another — the single most consequential technical gap for a bilingual FMCG brand competing in both Arabic and English search in KSA.
- **Sitemap is materially incomplete.** `/sitemap.xml` lists only ~40 URLs — corporate/investor pages, top-level product categories, and news items — while the live site has dozens of individual product SKUs alone (product detail URLs observed: `/ar/products/284`, `/304`, `/306`, `/310`–`/313` and more), plus a growing news archive. Individual product pages do not appear to be comprehensively represented in the sitemap that Google is being pointed to.
- **`robots.txt` doesn't reference the sitemap.** The file present is Drupal's unmodified default template — it correctly blocks system paths (`/admin/`, `/core/`, `/user/login`, etc.) but contains no `Sitemap:` directive, so sitemap discovery relies entirely on manual Search Console submission rather than being self-documenting for all crawlers.
- **Non-descriptive product URLs.** Product detail pages use numeric IDs (`/ar/products/284`) rather than keyword-bearing slugs (e.g., `/ar/products/full-fat-milk-1l`), losing a relevance signal that search engines read directly from the URL.
- **Zero structured data sitewide.** No JSON-LD and no microdata/RDFa schema was found on any template tested — homepage (AR/EN), product category, product detail, branches, contact, or FAQ pages. This is despite the site having ideal source content for `Organization`, `Product`, `BreadcrumbList`, `LocalBusiness`, and `FAQPage` schema already present in unstructured form (a public-company profile, a full product catalog, physical branch listings with embedded Google Maps, and a dedicated FAQ page).
- **Brand footprint is split across multiple domains.** Careers run on a third-party ATS subdomain (`jobs2web.com`), and at least one additional NADEC property is hosted on Azure (`neew-public-website.azurewebsites.net`) and one on SAP HANA Cloud (`nadec-landing.cfapps.eu10-004.hana.ondemand.com`) rather than under `nadec.com`. Consolidating these under the primary domain (or a properly canonicalized subdomain) would concentrate crawl equity and backlink authority instead of splitting it across unrelated hostnames.
- **Mobile-first indexing readiness** is structurally fine (viewport, lazy-loading, responsive lang/dir handling) but the *experience* Google's mobile-first index will actually evaluate is weak — see Section 3.

---

## 2. On-Page SEO

**What's already working well** (verified):
- Titles and meta descriptions exist on every page tested — a baseline many corporate sites skip. Titles follow a consistent, brand-appropriate `Page Name | نادك` / `Page Name | Nadec` pattern.
- Breadcrumb navigation is implemented in the markup on product pages, giving users and crawlers a clear category → product path.
- AR and EN templates carry parallel title/meta fields — no missing-translation pages were found on the templates tested, indicating the bilingual content pipeline itself is sound at the template level.

**Opportunities identified** (verified):
- **No H1 on commercial pages.** Neither the dairy category page (`/ar/milk`) nor the tested product detail page (`/ar/products/284`) contains an `<h1>` element. The H1 is the strongest on-page relevance signal after the title tag — its absence on exactly the pages that should rank for product-category search terms is the single highest-priority on-page fix.
- **Duplicate meta descriptions at the template level.** The `/ar/milk` dairy category page — arguably the most commercially important page on the entire site — reuses NADEC's corporate boilerplate description verbatim ("تعد نادك، من أوائل الشركات الصناعية الغذائية والزراعية..."), identical to the homepage, instead of a unique description targeting dairy-category search intent. This pattern likely repeats across the juice, meat, and feed category pages.
- **Titles and headers skew corporate rather than commercial.** Copy is well-written and brand-appropriate (Vision 2030, quality, sustainability), but it's written for an investor/CSR audience rather than structured around the commercial search intent of KSA grocery shoppers, distributors, and foodservice buyers (specific product names, nutritional attributes, usage occasions).
- **Thin product content.** The tested SKU (نكتار أناناس مع فواكه مشكلة, 1.3L) has a single-line description with no nutritional information, ingredients, or usage content visible in the page markup — limiting ranking potential for long-tail product queries and reducing the page's usefulness to shoppers.
- **Generic/duplicated image alt text.** Primary content images (e.g., the logo) carry correct descriptive alt text, but a large share of navigation icons share the identical, non-descriptive alt value `"Menu Icon"` across many different icons — a missed accessibility and relevance opportunity that's cheap to fix during the rebuild.
- **Internal linking is structurally present but not strategically built.** Nav + breadcrumbs exist, but there's no evidence of contextual cross-linking (e.g., category pages linking to related recipes/usage content, or products linking to related items in the same range) that would reinforce topical authority.

---

## 3. Core Web Vitals / Performance

Measured via Google PageSpeed Insights / Chrome UX Report (real-user field data, 28-day window, captured 22 July 2026, tested on `https://www.nadec.com/en`):

| Metric | Mobile | Desktop | Verdict |
|---|---|---|---|
| **LCP** (Largest Contentful Paint) | 4.8s | 3.6s | Mobile fails, desktop needs improvement |
| **INP** (Interaction to Next Paint) | 142ms | 47ms | Both pass |
| **CLS** (Cumulative Layout Shift) | 0.02 | 0.62 | Mobile passes; **desktop fails significantly** |
| **FCP** (First Contentful Paint) | 3.0s | 2.2s | Both need improvement |
| **TTFB** (Time to First Byte) | 1.7s | 1.2s | **Both fail** |
| **Lighthouse Performance** | 44 | 67 | Mobile is the weak platform |
| **Lighthouse Accessibility** | 77 | 85 | — |
| **Lighthouse Best Practices** | 96 | 96 | Strong |
| **Lighthouse SEO** | 92 | 92 | Already a good technical baseline |

**Reading the data:**
- **Core Web Vitals fail the assessment on both mobile and desktop** — this directly affects Google's page-experience ranking signal, on top of the direct UX/conversion cost of slow pages.
- **TTFB fails on both platforms (1.7s mobile / 1.2s desktop).** This is a server/backend response-time issue, not a front-end asset problem — it points at hosting, backend rendering (Drupal page generation), or origin cache configuration, and should be scoped jointly with the RFP's front-end/back-end development workstream, not treated as an SEO-only fix.
- **Mobile is the clear weak point** (Performance 44 vs. 67 desktop; LCP 4.8s is the single worst metric measured). Given majority-mobile traffic patterns typical of KSA FMCG audiences, this is where remediation should be prioritized first.
- **Desktop CLS of 0.62 is a red flag** — a "fail" this severe is almost always caused by late-loading images, ads/embeds, or web fonts shifting content after initial paint, and is a concrete, fixable design/dev commitment for the proposal (reserve layout space for images/embeds, preload key fonts).
- Supporting technical observations from direct source inspection: the site serves images exclusively in legacy formats (PNG/JPG/GIF/SVG — no WebP/AVIF found anywhere in the homepage markup) and does not use `srcset`/responsive image variants despite images carrying explicit width/height attributes. Combined with the measured LCP numbers, this is a plausible contributor to slow mobile paint times and is a straightforward fix during a rebuild.
- Third-party scripts are present (Google Tag Manager/GA4, social embeds, and a live-chat widget visible in the CSP allow-list) — normal for a corporate site, but worth auditing for load-order/defer strategy given the CLS finding.
- **SEO Lighthouse score is already a strong 92** — the differentiator NADEC should be buying in this engagement is Core Web Vitals remediation plus the technical/off-page/local depth below, not basic on-page hygiene (which the current build already gets partially right).

---

## 4. Off-Page Authority

**Data limitation (stated explicitly):** Licensed backlink/Domain Rating tooling (Ahrefs, SEMrush, or Moz) was not available in this audit session. The findings below are qualitative, drawn from verifiable public signals rather than a live backlink index pull. **Before this section is finalized in the client proposal, run a live Ahrefs or SEMrush comparison of nadec.com vs. almarai.com to replace directional signals with exact Domain Rating and referring-domain counts.**

**Verified qualitative signals:**
- NADEC is a Tadawul-listed public company (ticker 6010 / NADEC:AB), which generates naturally authoritative inbound coverage from financial and business-news domains — confirmed presence on Bloomberg, Yahoo Finance, Zawya, and AGBI, plus an active Wikipedia entry and LinkedIn company page. This is a real, currently underexploited off-page asset: investor-relations and press activity is already earning links from high-authority domains, but doesn't appear to be systematically leveraged for consumer-facing dairy/FMCG search terms.
- Recent earned-media moments exist to build on (Ministry of Human Resources CSR "Social Responsibility Badge," Al-Jouf Award for Excellence and Innovation for the organic olive oil project, "Product of the Year 2025 – KSA" for Nadec Fresh Milk) — these are the kind of stories that convert into consumer-press and food-media backlinks if actively pitched, rather than only published to the corporate news page.
- As noted in Section 1, brand-authority signals are currently split across `nadec.com`, a third-party careers ATS subdomain, and at least two off-domain microsites (Azure, SAP HANA Cloud) — links and citations pointing at those properties build authority for someone else's domain rather than NADEC's own.

**Competitive context:** Almarai is the dominant KSA dairy/FMCG brand — larger scale, longer-established (1977 vs. NADEC's 1981), also Tadawul-listed, and the natural authority benchmark for this category. Exact comparative Domain Rating/backlink-count figures should be pulled live (see data limitation above) rather than assumed for the final proposal.

---

## 5. Local SEO

**Verified on-site signals:**
- NAP data exists in the footer of every page: `+966 11 202 7777` and toll-free `800 124 1199`, with a dedicated `/contact-us` page.
- A dedicated `/branches` page exists with an embedded Google Map — confirming NADEC already maintains a structured, centrally-managed branch/location listing that a local SEO program can build directly on top of.

**Opportunities identified:**
- **No `LocalBusiness`/`Organization` schema markup anywhere on the site** (consistent with the sitewide absence of structured data noted in Section 1). Branch and HQ address data exists in the page content but is not machine-readable, so Google has no structured basis to associate it with a Knowledge Panel or local pack listing.
- **Google Business Profile status was not verified in this session** — GBP account access is required and wasn't available via the tools used for this audit. This should be confirmed directly with NADEC (does an active, verified GBP already exist for HQ and/or individual branches?) before the proposal quantifies this as a gap.
- **Given NADEC's physical footprint** — HQ, dairy farms, processing plants, and a nationwide branch network feeding 38,000+ distribution points — local pack visibility is a meaningfully underused channel relative to the brand's actual scale, and a strong candidate for a structured multi-location local SEO program once GBP status is confirmed.

---

## Recommended SEO Strategy (mapped to RFP scope)

### 1. Technical SEO
- Implement `hreflang` alternate annotations across every AR/EN page pair.
- Add a `Sitemap:` directive to `robots.txt`; rebuild the XML sitemap to comprehensively include all product, news, and content URLs with accurate `lastmod` values, split into sub-sitemaps by content type if volume warrants.
- Roll out sitewide JSON-LD: `Organization` (homepage), `Product` (product detail pages), `BreadcrumbList` (all templates), `FAQPage` (`/faqs`), `LocalBusiness` (branches/contact).
- Migrate keyword-relevant URL slugs for product pages away from numeric IDs.
- Consolidate off-domain career/campaign microsites under `nadec.com` (or a properly canonicalized subdomain) to stop splitting crawl and link equity.

### 2. On-Page SEO
- KSA-specific keyword research across dairy/agri/FMCG terms in both Arabic and English, mapped to category and product pages.
- Add unique H1s to every template; rewrite category/product meta titles and descriptions to be unique and commercially targeted (stop reusing the corporate boilerplate description on category pages).
- Expand product page content: nutritional information, ingredients, and usage occasions, tied into a content/recipe hub for cross-linking.
- Fix generic/duplicated alt text sitewide as part of the rebuild.
- Build contextual internal linking between category, product, and content pages (not just nav/breadcrumb).

### 3. Performance / Core Web Vitals
- Prioritize mobile: it is the clearly weaker platform (LCP 4.8s, Performance 44) and the primary channel for KSA FMCG shoppers.
- Investigate and remediate TTFB (1.2–1.7s) at the hosting/backend layer — scope jointly with the RFP's front-end/back-end development workstream, since this is a server response-time issue, not a client-side fix.
- Diagnose and fix the desktop CLS failure (0.62) — audit late-loading images, embeds, and web fonts for layout-shift causes; reserve layout space and preload critical assets.
- Convert imagery to WebP/AVIF with responsive `srcset` variants to cut LCP weight, building on the aggregation and lazy-loading practices already in place.

### 4. Off-Page Authority Building
- Systematize digital PR: pitch existing earned-media moments (CSR awards, product-of-the-year recognitions, Vision 2030 food-security narrative) to consumer/food press, not just the corporate news page.
- Build a recipe/content hub designed to earn links from food bloggers and lifestyle media.
- Pursue links from KSA retail, grocery, and foodservice industry directories and trade bodies.
- Consolidate domain authority per the Technical section (stop splitting equity across off-domain microsites).
- Benchmark Domain Rating and referring-domain growth against Almarai on a recurring (quarterly) basis via Ahrefs/SEMrush once live data is pulled.

### 5. Local SEO
- Confirm current Google Business Profile status (existing/verified or not) directly with NADEC as the first step.
- Build/optimize a multi-location GBP program covering HQ, plants, and branch locations.
- Implement `LocalBusiness`/`Organization` schema referencing the branch data already structured in the CMS.
- Enforce NAP consistency across GBP, website, social profiles, and third-party directories (Zawya, LinkedIn, etc.).
- Add local/geo schema to branch pages and stand up a review-management process where applicable.

---

## Immediate Next Steps to Strengthen This Section Before Submission
1. Pull live Ahrefs/SEMrush Domain Rating and backlink comparison: nadec.com vs. almarai.com (closes the Section 4 data gap with hard numbers).
2. Confirm Google Business Profile status directly with the NADEC team (closes the Section 5 data gap).
3. If Search Console access can be shared, pull actual indexed-page counts and coverage-error data to replace the sitemap-completeness estimate in Section 1 with exact figures.
