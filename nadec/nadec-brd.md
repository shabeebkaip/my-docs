# NADEC Website Redesign — Business Requirements Document (Developer-Facing)

**Prepared by:** Code-OX Technologies
**Client:** National Agricultural Development Company (NADEC)
**Source documents:** `NADEC_Website_RFP.docx` (issued 22 Jul 2026 — authoritative scope source), `website-audit-findings.md`, `seo-audit-findings.md`, `aetheris-audit-findings.md`, `pagespeed-data.md`, `competitor-benchmark.md`, `design-direction.md`, `NADEC-Knowledge-Base/NADEC_MASTER_REPORT.md`, `nadec-technical-proposal.html`
**Status:** Draft — pending client confirmation on open decisions (§13) and internal confirmation of Umbraco/.NET delivery capability (§13.2)

---

## 1. Project Overview

The RFP defines **one mandatory deliverable and one optional deliverable** — this is a structural requirement, not a phasing preference, and drives everything below:

1. **Deliverable 1 — Website Design (Mandatory, firm fixed price).** Discovery, IA/UX, bilingual AR/EN high-fidelity design, design system, interactive prototypes, and production-ready **static** front-end templates (HTML5/CSS3/JS + Bootstrap or Tailwind). **No CMS, backend application, or database is in scope for Deliverable 1.**
2. **Deliverable 2 — Umbraco CMS Implementation (Optional, separately priced, proceeds only on NADEC's formal written activation).** Full Umbraco CMS on Microsoft .NET/SQL Server, built on the approved Deliverable 1 templates: content modeling, bilingual culture variants, editorial workflow, legacy migration, SEO, testing, deployment, training, and hypercare.

Not a greenfield build: the current site (nadec.com) is live on Drupal and carries real content volume (investor documents, governance filings, multilingual news, product catalog). Drupal is the **legacy system being migrated from** — it is not, and must not be assumed to be, the target platform. If Deliverable 2 is activated, the target CMS is **Umbraco**, per the RFP's explicit technology mandate (§8.2).

> **Correction note:** an earlier draft of this BRD assumed CMS + migration + 2-year support were core, undifferentiated scope, and separately assumed a Drupal-foundation rebuild (then a MERN/Next.js migration) as the target platform. Neither matches the RFP as issued. This revision aligns strictly to the RFP's own Deliverable 1 / Deliverable 2 split and its Umbraco/.NET/SQL Server mandate.

## 2. Stakeholders

| Role | Responsibility |
|---|---|
| NADEC — Marketing (Project Owner) | Owns Deliverable 1 requirement approval, brand/content sign-off, and the decision to activate Deliverable 2. |
| NADEC — D&T (Digital & Technology) | Technical approval authority: Bootstrap-vs-Tailwind choice, Umbraco/.NET/SQL Server version approval, environment/hosting decisions. |
| NADEC — Quality/Regulatory Team | Owns nutrition, ingredient, and SKU-level product data and sign-off on regulated claims (relevant once content is populated, D2). |
| NADEC — Compliance/Governance Team | Sign-off gate for investor-disclosure and governance-document content before publish (D2). |
| NADEC — IT/Hosting Owner | Grants environment access for Deliverable 2 (DEV/TEST/STAGING/PROD) and hosting/infra access for performance remediation. |
| Delivery Team — Project Lead | Owns delivery against this BRD; single point of accountability for scope, timeline, and quality gates across D1 and (if activated) D2. |
| Delivery Team — QA Lead | Independently verifies each milestone against acceptance criteria (§14) before sign-off. |

## 3. Scope of Work

### 3.1 Deliverable 1 — Website Design (Mandatory)

| # | Deliverable | Description |
|---|---|---|
| 01 | Discovery & Assessment | Kickoff and stakeholder workshops; review of existing site, analytics/SEO findings supplied by NADEC, audiences, content, navigation, brand guidelines, dependencies. |
| 02 | Information Architecture & UX | Audience-first IA (`Consumers / Our Farms & Sustainability / Investors / Media & Corporate / Careers`), replacing the current flat department-first menu; sitemap, navigation model, user journeys, content hierarchy, wireframes for English LTR and Arabic RTL. |
| 03 | Interactive Prototypes | Clickable, reviewable prototypes of key journeys, validated with NADEC stakeholders before final visual design. |
| 04 | UI Design & Design System | "Grounded Premium" visual direction (§5) with governed design tokens and full component library — buttons, cards, navigation, forms, tables, banners, tabs, accordions, states, accessibility guidance. |
| 05 | Bilingual Arabic/English Design | Native RTL design for every template (not a mirrored afterthought), equal-quality typography and component mirroring, paired Arabic/Latin type in the same visual register. |
| 06 | Additional Pages | Any additional corporate page, template, component, or layout requested by Marketing/D&T during requirements, design, UAT, or rollout — scope is not limited to the initially listed page types. |
| 07 | Production-Ready Static Front-End | Responsive, semantic HTML5/CSS3/JS templates and reusable components using the D&T-approved Bootstrap **or** Tailwind CSS version (open decision, §13.1) — homepage, internal pages, corporate info, products/categories, news/media, investor relations, sustainability/CSR, careers, contact/locations, search, forms, 404/error, global components. **Static only — no CMS, backend, or database.** |
| 08 | Handover | Design specifications, asset exports, editable design source files, complete HTML/CSS/JS source code, build instructions, dependency details, implementation guidance. |

**Acceptance:** all agreed screens/states complete; requested pages covered; AR/EN and responsive behavior approved; accessibility and brand comments closed; static templates accurately implement approved designs and run correctly on agreed browsers/devices; source code and editable design files transferred; NADEC Marketing and D&T issue formal written acceptance.

### 3.2 Deliverable 2 — Umbraco CMS Implementation (Optional — activates only on NADEC's written request)

| # | Deliverable | Description |
|---|---|---|
| 01 | CMS Architecture | Latest stable Umbraco release (LTS preferred) approved by D&T, on Microsoft .NET runtime + SQL Server; documented DEV/TEST-UAT/STAGING/PROD environments; secure config, source control, repeatable deployment. |
| 02 | Content Model & Page Building | Structured document types, compositions, data types, block-based components for all approved page types; editors assemble approved components without code changes. |
| 03 | Bilingual Content (CMS) | AR/EN culture variants, linked language versions, localized URLs, independent language-specific content and SEO fields, correct RTL/LTR rendering. |
| 04 | Editorial Governance | Roles (admin/editor/reviewer/approver/publisher); draft/review/approve/reject/rework/publish workflow; notifications; preview; scheduled publish/unpublish; version history/compare/rollback; recycle-bin recovery; audit logs. |
| 05 | Media & Global Content | Governed media library (folders, metadata, alt text, crops/renditions, documents, duplicate controls); CMS-managed navigation, footer, social links, contacts, alerts, banners, legal content, global settings. |
| 06 | Search, Forms, Integrations | Bilingual site search; secure configurable forms (validation, consent, anti-spam, notifications, export); NADEC-approved API/service integrations; no secrets exposed client-side. |
| 07 | Front-End Integration | Pixel-accurate integration of Deliverable 1 templates into Umbraco; any material visual/framework change requires prior Marketing + D&T approval. |
| 08 | Legacy Migration | Inventory of current AR/EN pages, documents, images, video, metadata, taxonomies, URLs, forms, structured data; source-to-target mapping to Umbraco content types; trial migration; final delta migration; reconciliation report; URL preservation or tested 301 redirects. |
| 09 | SEO, Performance, Accessibility, Security | Site audit; keyword/page mapping; SEO-friendly URLs/headings; canonical/hreflang; XML sitemap/robots.txt; structured data; Core Web Vitals optimization; WCAG 2.1 AA; secure coding, least-privilege access, HTTPS/TLS, secrets management, logging, backup/restore. |
| 10 | Testing, Deployment, Training | Full functional/workflow/bilingual/responsive/browser/accessibility/SEO/performance/security/integration/migration/regression/UAT testing; defect log with critical/high closed before go-live; deployment/cutover/rollback plans; hands-on admin/editor/reviewer/publisher training; user guides. |
| 11 | Handover & Hypercare | Architecture, configuration, content model, code, API, deployment, backup/recovery, admin/support documentation; minimum 60–90 calendar day warranty/hypercare post go-live. |

**Acceptance:** all agreed page types, components, workflows, roles, bilingual content, search, forms, integrations operate correctly; migration reconciled; critical redirects/SEO controls validated; quality/security tests pass; critical/high defects closed; production deployment and hypercare complete; NADEC issues formal written acceptance.

**Note on ongoing services:** the RFP explicitly scopes hypercare to 60–90 days only. Ongoing maintenance and ongoing SEO beyond hypercare are **not** part of Deliverable 2 — they must be priced as separate optional line items (Appendix B), not folded into the D2 firm price.

## 4. Current State (verified via live crawl/curl, not assumption)

- **Stack (legacy, being migrated from):** Drupal 9/10, custom theme (`nadec_theme`), Cloudflare CDN/WAF in front. TLS and security headers already correctly configured — preserve, don't regress, if/when D2 goes live.
- **Performance:** Mobile Lighthouse Performance 44/100, mobile LCP 4.8s (fail), desktop CLS 0.62 (fail), TTFB fails on both platforms. Homepage payload ~7.4MB, 3 animated GIF stat-counters = ~2.9MB of that alone. No WebP/AVIF anywhere.
- **i18n:** Root domain always serves Arabic regardless of `Accept-Language`. Arabic pages link `hreflang` to English; English pages do NOT link back (one-directional gap). No `x-default`.
- **SEO baseline:** Zero structured data sitewide. Sitemap lists only ~37 URLs against a real catalog of ~130+ dairy/meat/news items combined. 4 confirmed duplicate-URL pairs (legacy `/index.php/en/X` vs clean `/en/X`). 1 insecure HTTP video embed. Missing SPF record.
- **Content gaps:** 0/141 sampled products have nutrition/ingredient/SKU data. Recipes/Departments/Initiatives pages render fully empty despite existing UI scaffolding.
- **Accessibility:** Real strengths to preserve — font-size toggle, dark mode, voice toolbar, labeled contact form. Real gaps — multiple `<h1>`s per page, missing ARIA landmarks.
- **CSS:** Brand blue/green tokens genuinely coded, but default Bootstrap colors leak through unmapped in places.
- **Local/branches:** NAP data + branches page with embedded map exist, but map is a JS-rendered widget exposing only the HQ record to crawlers/static fetch — full branch network needs a headless (Playwright) enumeration pass before schema work (D2).
- **Security note (careers page):** internal employee email currently leaks via a raw Outlook Safelinks URL — flag as quick-win fix (D2, since it requires a live/CMS-editable page).
- **Known 404:** sitemap.xml contains a literal dead URL.

These findings are **inputs to Deliverable 1 design decisions** (e.g., image-heavy hero patterns to avoid, IA restructure) and become **live remediation targets under Deliverable 2** (performance, redirects, structured data) if and when it is activated.

## 5. Design Requirements (Deliverable 1)

**Direction: "Grounded Premium"** — chosen for NADEC's brand equity as a trusted, 45-year-old publicly listed institution serving both mainstream households and investors, not a generic "modern and clean" brief.

- **Real over synthetic:** actual farm and plant photography/video — drone footage of dairy farms, real processing-line footage — as the primary visual language, not stock imagery or default synthetic 3D.
- **One 3D moment, not a 3D site:** a single, purpose-built "farm to carton" 3D/scroll hero on the homepage only, built as a static/interactive front-end asset. Every other page uses photography, CSS parallax, and scroll-reveal.
- **Brand palette carried forward:** NADEC's existing blue (`#2B338C` / `#001971`) and green (`#7FBC42`) formalized as governed design tokens, not replaced.
- **Typography carries "premium":** a confident type system — warm/humanist serif for headlines, clean grotesque for UI/body — paired equivalently for Arabic and Latin scripts.

**Performance-safe by design.** The 3D hero is capability-gated at the static template level: mobile and low-bandwidth devices receive a static art-directed image or a short sub-2MB video loop instead of the WebGL scene. The hero must never be the LCP-blocking element in the delivered templates.

**Explicitly avoided:** a WebGL-playground site (3D scoped to exactly one hero); a novelty/challenger tone (NADEC is the incumbent, not the disruptor); any palette change (existing brand colors are formalized, not discarded).

Per RFP §2.1: WCAG 2.1 AA design considerations (contrast, focus, labels, keyboard interaction, non-text alternatives) apply at the design/template level regardless of whether Deliverable 2 is activated. All visual assets and fonts must be licensed, disclosed, and transferable to NADEC without vendor lock-in.

Full curated reference gallery and technical guardrails (draw-call budget, off-main-thread shader compilation, compressed assets) are maintained in `design-direction.md`.

## 6. Functional Requirements

### 6.1 Information Architecture (Deliverable 1)
Restructure from the current flat department-first menu to an audience-first IA: `Consumers / Our Farms & Sustainability / Investors / Media & Corporate / Careers`.

### 6.2 Content Types / Templates
For **Deliverable 1**, these are page **templates to design**, not structured content models — Deliverable 1 has no database. For **Deliverable 2** (if activated), each becomes a structured Umbraco content type:

| Type | Deliverable 1 (template) | Deliverable 2 (content type, if activated) |
|---|---|---|
| Product | Category (Dairy/Juice/Meat/Produce) layout, nutrition table layout, ingredients/usage layout | Structured fields: category, nutrition table, ingredients, usage occasions, SKU |
| News/Press | Article template, AR/EN paired layout | Bilingual culture variant pair, publish date, category taxonomy |
| Investor document | Document library layout (Financial/Share Information/Governance/Annual Reports) | Structured document entity; all existing PDF URLs preserved 1:1 during migration |
| Recipe | Currently empty in production — new template needed (ingredients, steps, linked products, imagery) | Full content model with linked-product relationships |
| Branch/Distribution point | Location template | Structured location entity backing `LocalBusiness` schema and sitemap entries |
| Career/Job | Listing template, safe outbound contact method (no raw internal email in markup) | Structured job entity, workflow-gated publish |

### 6.3 Bilingual (AR/EN)
Equal-quality AR/EN design is a **Deliverable 1** requirement (RFP §2.1). Genuinely reciprocal `hreflang` and culture-variant content relationships are a **Deliverable 2** requirement, generated from the CMS translation relationship rather than hand-maintained per page.

### 6.4 Search / Sitemap
CMS-generated sitemap reflecting the full catalog and both language versions as first-class entries — **Deliverable 2 only** (requires a live CMS to generate).

### 6.5 E-commerce / Store
**Not listed in the RFP's expected website sections (§4.1) or anywhere in the deliverable scope.** No D2C e-commerce exists at any of the 5 benchmarked competitors either — category norm, not a NADEC-specific gap. Treat as **out of current RFP scope**; do not design or estimate for it unless NADEC explicitly requests it as an additional item (in which case it requires its own scoping and pricing, per RFP §5.2 change-control terms).

## 7. Non-Functional Requirements

| Area | Current (measured, legacy site) | Target |
|---|---|---|
| Mobile LCP | 4.8s (fail) | Pass Core Web Vitals threshold (<2.5s) — validated once D2 is live |
| Desktop CLS | 0.62 (fail) | <0.1 |
| TTFB | Fails both platforms | Backend/hosting-layer fix — profile Umbraco/.NET render path + origin cache (D2) |
| Homepage payload | ~7.4MB | Materially reduced in D1 templates — no animated-GIF stat counters, WebP/AVIF imagery with responsive `srcset` |
| Static asset cache | `max-age` 4h despite content-hashed filenames | Long-lived immutable caching (D2 hosting config) |
| Mobile/reduced-motion | N/A | Never request the 3D/WebGL hero bundle at all (D1 template requirement) |

Deliverable 1 is responsible for building performance-conscious static templates (optimized images, no render-blocking patterns, capability-gated hero). Full Core Web Vitals validation against live traffic is only possible once Deliverable 2 deploys the site.

**Security** (Deliverable 2): CMS/framework patches proactive, including emergency out-of-cycle patching for critical vulnerabilities — an ongoing-support SLA item once a maintenance term is separately agreed, not just a launch-day task.

**Accessibility:** preserve existing toolbar features; fix multiple-`<h1>` and missing ARIA landmarks; don't regress the working labeled contact form.

## 8. Technical Architecture

### 8.1 Deliverable 1 Front-End Stack — Open Decision
RFP mandates HTML5/CSS3/JavaScript with **either the latest stable Bootstrap or Tailwind CSS version, approved by D&T**. This is not our call to make unilaterally — recommend Tailwind for the governed-design-token/component approach in §5, but D&T approval is required before build starts (§13.1).

### 8.2 Deliverable 2 CMS Platform — RFP-Mandated, Capability Open Risk
RFP mandates **Umbraco (latest stable, LTS preferred) on Microsoft .NET runtime + SQL Server** for Deliverable 2 — this is fixed by the client, not a recommendation we can substitute (Drupal and any other CMS/stack do not satisfy Appendix A compliance). **Open risk, unconfirmed:** whether the delivery team has direct Umbraco/.NET/SQL Server production experience to stand behind the RFP §6.1 vendor-qualification claim and Appendix A compliance line. Must be resolved — confirmed in-house, confirmed via a named subcontractor (disclosed per RFP §7.1), or the compliance matrix marks Deliverable 2 "N" and the bid proceeds on Deliverable 1 only — before this BRD or the proposal are finalized for submission.

### 8.3 Internationalization
Deliverable 1: equal-quality AR RTL / EN LTR templates, component mirroring. Deliverable 2: reciprocal `hreflang="ar"`/`hreflang="en"` + `x-default` generated automatically from the Umbraco content-translation relationship.

### 8.4 CDN & Edge (Deliverable 2)
Cloudflare config retained. Fix static asset cache headers (4h → long-lived immutable for content-hashed bundles).

### 8.5 Hosting & Backend Response Time (Deliverable 2)
TTFB is a server/backend issue. Profile backend rendering path, implement page-level cache warming for high-traffic templates, correct static-asset cache headers. Requires hosting/infra access during remediation phase (§13).

### 8.6 Domain Consolidation (Deliverable 2)
Legacy `/index.php/en/X` duplicate URLs (meat/about/feed/juice confirmed) must resolve via canonical/redirect, not remain as duplicate-content pairs.

## 9. SEO / Technical Requirements (Deliverable 2)

Per RFP §3.2, SEO is scoped under Deliverable 2, not Deliverable 1:

- Structured data: `LocalBusiness`/`Organization` schema referencing fully-enumerated branch data (post-Playwright-enumeration, see §4).
- Sitemap regeneration: CMS-driven, both language versions per page, first-class cross-annotated entries.
- Fix 4 broken 404 assets, 1 insecure HTTP video embed (About page, Azure microsite), missing SPF record.
- Local SEO: confirm current Google Business Profile status directly with NADEC first, then build/optimize multi-location GBP (HQ, processing plants, branch network). Enforce NAP consistency across GBP, site, social, directories.
- Off-page: current backlink profile (3,426 backlinks / 852 referring domains) has 257x spam anchor text + authority concentrated on an Azure microsite, not nadec.com — flag as risk needing full Ahrefs/SEMrush review before final scoping (data gap, not yet actioned).
- **Do not overstate** ISO 42001 AI-governance angle in GEO/AI-search copy — homepage ISO mentions may be food-safety certs, not AI-governance; confirm with NADEC before using that narrative.

**Note:** if NADEC activates Deliverable 1 only, none of the above SEO work is in scope or priced — it depends entirely on a live CMS.

## 10. Content Migration Requirements (Deliverable 2 only)

- All investor-document PDF URLs preserved 1:1 (governance/compliance sensitivity — broken investor links are not acceptable).
- Product/nutrition/SKU data entry requires NADEC quality/regulatory team input — vendor delivers CMS structure + content-entry support, not regulatory sign-off on claims.
- Content touching investor disclosures, governance documents, or regulated product/nutrition claims routes through NADEC's own compliance sign-off workflow before publish — build the CMS workflow to support that gate, don't bypass it.
- At least one trial migration required before final cutover, with migration reports, counts, exceptions, and reconciliation (RFP §3.1).

## 11. Support & Maintenance

**RFP-mandated (part of Deliverable 2 firm price):** minimum 60–90 calendar day warranty/hypercare after go-live, covering vendor-developed code, CMS configuration, migration, responsive behavior, SEO, performance, and approved integrations.

**Separately priced options (not RFP-mandated, propose as add-ons per RFP §3.3 — "price ongoing maintenance and SEO separately as options"):**

| Tier | Definition | Response |
|---|---|---|
| P1 | Site down / CMS admin broken | Fastest tier |
| P2 | Key template/form/CMS admin badly degraded, site still reachable | 2 business days |
| P3 | Routine issue | Standard cycle |

Covers (as an optional term, e.g. annual or 2-year): proactive + emergency out-of-cycle security updates, named-channel technical support, browser/device compatibility fixes from new browser/OS/Umbraco-core updates, minor operational content mods. **Out of scope even as an add-on** (change-request territory): large-scale content migration, bulk rewrites, new catalog categories, full-catalog-scale nutrition/ingredient data entry.

> **Correction note:** do not present this as "RFP Item 2 / 2-year support contract" in client-facing material — the RFP does not mandate a 2-year term. Present it as a Code-OX-recommended optional service, priced and labeled separately from the Deliverable 2 firm price, per RFP §3.3 and §6.2 ("Optional services... shall be separately priced").

## 12. Assumptions & Constraints

- Nutrition, ingredient, and SKU-level product content is authored with input from NADEC's quality/regulatory team (D2).
- Bootstrap-vs-Tailwind (D1) and Umbraco/.NET delivery-capability (D2) are both open and must be resolved before final commercial commitment (§13).
- E-commerce is treated as out of RFP scope unless NADEC explicitly requests it.
- Hosting/infrastructure access sufficient to profile and remediate TTFB is made available during the D2 performance-remediation phase, if activated.
- Content touching investor disclosures, governance documents, or regulated claims routes through NADEC's own compliance/regulatory sign-off before publication.
- A design-and-build timeline for Deliverable 1 is proposed separately from Deliverable 2's timeline, per RFP §6.2 ("a separate optional timeline and milestones for Deliverable 2").
- Off-page backlink remediation (D2) requires licensed tool access (Ahrefs/SEMrush) not yet confirmed as available.
- NADEC may award Deliverable 1 only, and activate Deliverable 2 later through written request, at its sole discretion (RFP §7.2).

## 13. Open Decisions Required Before Submission

1. **Bootstrap vs. Tailwind CSS** for Deliverable 1 — recommend Tailwind, requires D&T approval.
2. **Umbraco/.NET/SQL Server delivery capability** — confirm in-house capability, or name a disclosed subcontractor, or bid Deliverable 1 only. Currently unresolved (flagged, not yet decided).
3. **E-commerce scope** — confirm with NADEC whether it is wanted at all; if so, it is additional scope outside this RFP's deliverables and needs its own pricing.
4. **Hosting/infra access** — sufficient access granted during D2 performance-remediation phase to profile and fix TTFB.
5. **GBP/licensed SEO-tool access** (Ahrefs/SEMrush) for off-page review, if D2/SEO is activated.
6. **Submission logistics** — the RFP document itself leaves Submission Contact, Email, and Deadline blank; obtain the actual values from NADEC Procurement before finalizing the proposal package.
7. **Three client references** and subcontractor disclosures required for RFP §6.1/6.2 — confirm which reference projects to use.

These materially change scope, technology commitments, and pricing — do not finalize the proposal against assumptions on any of them.

## 14. Acceptance Criteria

| Requirement Area | Verified When |
|---|---|
| Deliverable 1 sign-off | All agreed screens/states complete, AR/EN + responsive approved, accessibility/brand comments closed, static templates verified on agreed browsers/devices, source code + design files transferred, NADEC Marketing/D&T issue written acceptance. |
| Information Architecture | All 5 audience-first top-level sections live; no orphaned pages from the old department-first menu. |
| Bilingual reciprocity (D2) | Every AR page links `hreflang="en"` to its EN pair and vice versa, plus `x-default`, validated sitewide. |
| Core Web Vitals (D2) | Mobile LCP < 2.5s and desktop CLS < 0.1 confirmed via field data (CrUX/PageSpeed), not lab data alone. |
| Structured data (D2) | `LocalBusiness`/`Organization` schema validates with zero errors in Google's Rich Results Test for every enumerated branch location. |
| Sitemap (D2) | Regenerated sitemap count matches full live catalog (both languages), zero dead/404 URLs. |
| Investor documents (D2) | 100% of existing investor PDF URLs resolve post-migration (zero broken links). |
| Accessibility | Single `<h1>` per page sitewide, ARIA landmarks present, existing toolbar features (dark mode/font-size/read-aloud) still functional. |
| RTL parity | Dedicated RTL visual-parity pass signed off across chevrons, carousels, form direction, and the homepage hero sequence. |
| Security leak fix (D2) | Careers page no longer exposes internal employee email in page source. |
| Deliverable 2 sign-off (if activated) | All RFP §3.4 acceptance conditions met; migration reconciled; critical/high defects closed; hypercare and training complete; NADEC issues written acceptance. |

## 15. Out of Scope

- Deliverable 2 entirely, unless and until NADEC issues formal written activation (RFP §1, §7.2).
- E-commerce / online store (not in RFP's expected sections).
- Regulatory/nutrition claim sign-off (client-owned).
- Full backlink remediation execution (data gap, needs licensed tool access first).
- Large-scale content authoring beyond CMS scaffolding (client data-entry responsibility, with support).
- Ongoing maintenance/SEO beyond the 60–90 day hypercare, unless separately activated as a priced add-on.

## 16. Glossary

| Term | Meaning |
|---|---|
| CWV — Core Web Vitals | Google's user-experience performance metrics (LCP, CLS, and related), used as an SEO ranking signal. |
| LCP — Largest Contentful Paint | Time until the largest visible element on a page finishes rendering. |
| CLS — Cumulative Layout Shift | Measure of unexpected visual layout movement during page load. |
| TTFB — Time to First Byte | Server response time between request and first byte of response. |
| `hreflang` | HTML attribute telling search engines which language/region version of a page to serve. |
| RTL | Right-to-left text direction, required for Arabic layout. |
| WCAG | Web Content Accessibility Guidelines (targeting 2.1 AA per RFP). |
| GBP | Google Business Profile. |
| NAP | Name, Address, Phone — consistency across the web is a local-SEO ranking factor. |
| Umbraco | Open-source .NET CMS mandated by the RFP for Deliverable 2. |
| Culture variant | Umbraco's mechanism for per-language content on a shared content structure. |
| SKU | Stock Keeping Unit. |

## 17. Sign-Off

By signing below, each party confirms the requirements in this document — including the Deliverable 1 / Deliverable 2 split and open decisions in §13 — are understood and approved as the baseline for delivery.

| Role | Name | Signature | Date |
|---|---|---|---|
| NADEC — Marketing (Project Owner) | | | |
| NADEC — D&T Representative | | | |
| Delivery Team — Project Lead | | | |

---
*This BRD translates the RFP (`NADEC_Website_RFP.docx`) and verified audit findings into developer-actionable requirements. It does not replace `nadec-technical-proposal.html` (client-facing) or `design-direction.md` (visual/UX direction) — read alongside both.*
