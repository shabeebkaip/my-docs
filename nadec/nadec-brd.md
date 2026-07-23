# NADEC Website Redesign — Business Requirements Document (Developer-Facing)

**Prepared by:** Code-OX Technologies
**Client:** National Agricultural Development Company (NADEC)
**Source documents:** RFP scope (3 items), `website-audit-findings.md`, `seo-audit-findings.md`, `aetheris-audit-findings.md`, `pagespeed-data.md`, `competitor-benchmark.md`, `design-direction.md`, `NADEC-Knowledge-Base/NADEC_MASTER_REPORT.md`, `nadec-technical-proposal.html`
**Status:** Draft — pending client confirmation on 3 open decisions (§9)

---

## 1. Project Overview

Rebuild nadec.com (public-company KSA agri/FMCG dairy brand) covering three RFP scope items:

1. **Website Design & Development** — UX/UI, design system, front-end + back-end, CMS, bilingual AR/EN
2. **Annual Website Support & Maintenance** — 2 years, security patching, SLA-tiered support
3. **SEO** — technical, on-page, Core Web Vitals, off-page, content strategy, Local SEO

Not a greenfield build: current site is live, Drupal-based, has real content volume (investor documents, governance filings, multilingual news, product catalog) that must migrate cleanly.

## 2. Current State (verified via live crawl/curl, not assumption)

- **Stack:** Drupal 9/10, custom theme (`nadec_theme`), Cloudflare CDN/WAF in front. TLS and security headers already correctly configured — preserve, don't regress.
- **Performance:** Mobile Lighthouse Performance 44/100, mobile LCP 4.8s (fail), desktop CLS 0.62 (fail), TTFB fails on both platforms. Homepage payload ~7.4MB, 3 animated GIF stat-counters = ~2.9MB of that alone. No WebP/AVIF anywhere.
- **i18n:** Root domain always serves Arabic regardless of `Accept-Language`. Arabic pages link `hreflang` to English; English pages do NOT link back (one-directional gap). No `x-default`.
- **SEO baseline:** Zero structured data sitewide. Sitemap lists only ~37 URLs against a real catalog of ~130+ dairy/meat/news items combined. 4 confirmed duplicate-URL pairs (legacy `/index.php/en/X` vs clean `/en/X`). 1 insecure HTTP video embed. Missing SPF record.
- **Content gaps:** 0/141 sampled products have nutrition/ingredient/SKU data. Recipes/Departments/Initiatives pages render fully empty despite existing UI scaffolding.
- **Accessibility:** Real strengths to preserve — font-size toggle, dark mode, voice toolbar, labeled contact form. Real gaps — multiple `<h1>`s per page, missing ARIA landmarks.
- **CSS:** Brand blue/green tokens genuinely coded, but default Bootstrap colors leak through unmapped in places.
- **Local/branches:** NAP data + branches page with embedded map exist, but map is a JS-rendered widget exposing only the HQ record to crawlers/static fetch — full branch network needs a headless (Playwright) enumeration pass before schema work.
- **Security note (careers page):** internal employee email currently leaks via a raw Outlook Safelinks URL — flag as quick-win fix.
- **Known 404:** sitemap.xml contains a literal dead URL.

## 3. Functional Requirements

### 3.1 Information Architecture
Restructure from current flat department-first menu to audience-first IA:
`Consumers / Our Farms & Sustainability / Investors / Media & Corporate / Careers`

### 3.2 CMS Content Types (structured, not freeform HTML blobs)
- **Product** — category (Dairy / Juice / Meat / Produce), nutrition table, ingredients list, usage occasions, SKU. Fields must exist even if NADEC populates data post-launch (quality/regulatory team owns data entry, dev owns schema).
- **News/Press article** — bilingual pair relationship (AR node ↔ EN node), publish date, category.
- **Investor document** — Financial Information / Share Information / Governance / Annual Reports & Disclosures. All existing direct-linked PDF URLs must be preserved 1:1 during migration (no broken investor links).
- **Recipe** — currently empty in production; needs full content model (ingredients, steps, linked products, imagery).
- **Branch/Distribution point** — structured location entity (not just a map pin) so it can back `LocalBusiness` schema and a real sitemap entry.
- **Career/Job** — safe outbound contact method, no raw internal email leakage in markup.

### 3.3 Bilingual (AR/EN)
- Every content type is a translation-paired node set (not a bolted-on translation plugin over English-only fields).
- Language switch must be genuinely reciprocal — this is a template requirement, not a content requirement (see §5.3).

### 3.4 Search / Navigation
- Sitemap must be CMS-generated (not hand-maintained), reflecting full catalog + both language versions of every page as first-class entries.

### 3.5 E-commerce / Store
- **Open decision required from client** — no D2C e-commerce currently exists at any of the 5 competitor benchmarks either (category-wide norm, not a NADEC-specific gap). Confirm scope: full store vs. store-locator vs. B2B portal vs. none. Materially changes timeline/effort — do not assume.

## 4. Non-Functional Requirements (with target numbers, not vague "make it fast")

| Area | Current (measured) | Target |
|---|---|---|
| Mobile LCP | 4.8s (fail) | Pass Core Web Vitals threshold (<2.5s) |
| Desktop CLS | 0.62 (fail) | <0.1 |
| TTFB | Fails both platforms | Backend/hosting-layer fix — profile Drupal render path + origin cache |
| Homepage payload | ~7.4MB | Materially reduced — kill animated-GIF stat counters, convert imagery to WebP/AVIF w/ responsive `srcset` |
| Static asset cache | `max-age` 4h despite content-hashed filenames | Long-lived immutable caching |
| Mobile/reduced-motion | N/A | Never request the 3D/WebGL hero bundle at all (see design-direction.md) |

Security: CMS core/module/framework patches proactive, including emergency out-of-cycle patching for critical vulns (this is also a 2-year support-contract SLA item, not just launch-day).

Accessibility: preserve existing toolbar features; fix multiple-`<h1>` and missing ARIA landmarks; don't regress the working labeled contact form.

## 5. Technical Architecture Decisions

### 5.1 CMS Platform
**Recommended: rebuild on existing Drupal foundation**, not a full platform migration. Rationale: Drupal's content-modeling already supports the investor-document library, multilingual workflow, webform infrastructure NADEC depends on. Migrating the governance-document library + bilingual pipeline to a new platform is materially higher risk.
**Open decision required from client** — confirm Drupal-rebuild path vs. full migration before final commercial/timeline commitment (full migration is a larger undertaking, must be scoped separately if chosen).

### 5.2 Front-End Delivery
Component-based theme layer against a governed design-token system (color/type-scale/spacing) — replacing default Bootstrap utility classes currently left unmapped to brand colors. Image pipeline upgraded via Drupal's existing image-styles system to add WebP/AVIF + responsive `srcset` (currently used only for cropping, not format conversion).

### 5.3 Internationalization Fix
Reciprocal `hreflang="ar"`/`hreflang="en"` + `x-default` across every paired AR/EN template, generated automatically from the CMS content-translation relationship — not hand-maintained per page.

### 5.4 CDN & Edge
Cloudflare config retained. Fix static asset cache headers (4h → long-lived immutable for content-hashed bundles).

### 5.5 Hosting & Backend Response Time
TTFB is a server/backend issue, not front-end. Profile backend rendering path, implement page-level cache warming for high-traffic templates, correct static-asset cache headers. **Requires hosting/infra access during remediation phase** (see §9).

### 5.6 Domain Consolidation
Legacy `/index.php/en/X` duplicate URLs (meat/about/feed/juice confirmed) must resolve via canonical/redirect, not remain as duplicate-content pairs.

## 6. SEO/Technical Requirements

- Structured data: `LocalBusiness`/`Organization` schema referencing fully-enumerated branch data (post-Playwright-enumeration, see §2).
- Sitemap regeneration: CMS-driven, both language versions per page, first-class cross-annotated entries.
- Fix 4 broken 404 assets, 1 insecure HTTP video embed (About page, Azure microsite), missing SPF record.
- Local SEO: confirm current Google Business Profile status directly with NADEC first, then build/optimize multi-location GBP (HQ, processing plants, branch network). Enforce NAP consistency across GBP, site, social, directories.
- Off-page: current backlink profile (3,426 backlinks / 852 referring domains) has 257x spam anchor text + authority concentrated on an Azure microsite, not nadec.com — flag as risk needing full Ahrefs/SEMrush review before final scoping (not yet actioned, data gap).
- **Do not overstate** ISO 42001 AI-governance angle in GEO/AI-search copy — homepage ISO mentions may be food-safety certs, not AI-governance; confirm with NADEC before using that narrative.

## 7. Content Migration Requirements

- All investor-document PDF URLs preserved 1:1 (governance/compliance sensitivity — broken investor links are not acceptable).
- Product/nutrition/SKU data entry requires NADEC quality/regulatory team input — dev delivers CMS structure + content-entry support, not regulatory sign-off on claims.
- Content touching investor disclosures, governance documents, or regulated product/nutrition claims routes through NADEC's own compliance sign-off workflow before publish — build the CMS workflow to support that gate, don't bypass it.

## 8. Support & Maintenance (2-year contract scope)

SLA tiers (from technical proposal):
- **P1** (site down / CMS admin broken) — fastest tier
- **P2** (key template/form/CMS admin badly degraded, site still reachable) — 2 business days
- **P3** — routine

Covers: security updates (proactive + emergency out-of-cycle), technical support (named channel), browser/device compatibility fixes from new browser/OS/Drupal-core updates, minor operational content mods.
**Out of scope** (change-request territory): large-scale content migration, bulk rewrites, new catalog categories, full-catalog-scale nutrition/ingredient data entry.

## 9. Open Decisions — Required From Client Before Dev Starts

1. **CMS-foundation path**: Drupal rebuild (recommended) vs. full platform migration.
2. **E-commerce scope**: full store / store-locator / B2B portal / none.
3. **Hosting/infra access**: sufficient access granted during performance-remediation phase to profile and fix TTFB.
4. GBP/licensed SEO-tool access (Ahrefs/SEMrush) for off-page review.

These four materially change timeline and effort — do not start build against assumptions.

## 10. Out of Scope (this phase)

- Regulatory/nutrition claim sign-off (client-owned).
- Full backlink remediation execution (flagged as data gap, needs licensed tool access first).
- Large-scale content authoring beyond CMS scaffolding (client data-entry responsibility, with support).

---
*This BRD translates the client-facing technical proposal + verified audit findings into developer-actionable requirements. It does not replace `nadec-technical-proposal.html` (client-facing) or `design-direction.md` (visual/UX direction) — read alongside both.*
