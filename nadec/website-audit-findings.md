# NADEC (www.nadec.com) — Current State Findings

**Prepared for:** RFP response — website revamp scope
**Audit date:** 22 July 2026
**Scope covered:** Homepage (AR + EN), About/Investors, Contact, News, Milk (product), Quality, Careers pathway, robots.txt, sitemap.xml, response headers, SSL configuration, aggregated CSS/JS and image assets referenced from the homepage.
**Method:** Direct HTTP inspection (headers, HTML source, sitemap/robots, asset payloads, redirect chains, SSL certificate) plus static analysis of responsive CSS. No authenticated/CMS-admin access was available, and no headless-browser rendering (Lighthouse, real-device testing) was run in this pass — items that require that kind of tooling are explicitly marked **[Verify with tool]** below with the recommended method.

This document is written as a neutral technical/UX baseline of the current site, consistent with the RFP's framing of this engagement as a revamp. It is organized by review area, then closes with a condensed list suitable for internal cost scoping.

---

## 1. Technology Stack & Infrastructure

**Finding 1.1 — CMS and hosting stack**
What was found: Response headers (`x-drupal-cache`, `x-drupal-dynamic-cache`) and URL patterns (`/index.php/...`, `/sites/default/files/...`, `/themes/custom/nadec_theme/...`) confirm the site runs on **Drupal** (9 or 10, custom theme `nadec_theme`), fronted by **Cloudflare** (CDN, DDoS/WAF, HSTS injection). Static asset URLs use Drupal's content-hashed CSS/JS aggregation.
Why it matters: This is directly relevant to scoping — a revamp can either (a) restyle/rebuild on the existing Drupal instance, preserving the investor-relations document library and webform infrastructure, or (b) migrate to a new stack (headless CMS, Next.js, etc.), which is a materially larger undertaking given the content volume (annual reports, board bios, news archive, multilingual content).
Suggested direction: Confirm with NADEC's IT/marketing team which path the RFP expects before estimating. If Drupal is retained, budget for theme-layer rebuild + content migration; if replaced, budget for full CMS migration including the investor documents library and bilingual workflow.

**Finding 1.2 — SSL/TLS and transport security**
What was found: Valid certificate (Google Trust Services, expires 31 Aug 2026), HTTP→HTTPS redirect (301) and apex→`www` redirect (301) both function correctly. `Strict-Transport-Security: max-age=31536000; includeSubDomains` is set. A Content-Security-Policy, `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, and `X-XSS-Protection` are all present.
Why it matters: The security header baseline is already solid — this is not an area requiring urgent remediation.
Suggested direction: Carry forward the existing header configuration into the new build; no rework needed here. Note for the proposal: this reduces one category of risk/effort versus a typical legacy-site revamp.

**Finding 1.3 — Static asset caching policy**
What was found: Content-hashed CSS/JS bundles and images are served with `Cache-Control: max-age=14400` (4 hours) rather than long-lived/immutable caching, despite filenames already containing content hashes that make them safe to cache indefinitely.
Why it matters: Returning visitors re-download the same CSS/JS/image bytes every few hours instead of once. This is a low-effort, high-value performance fix.
Suggested direction: In the revamp, set `Cache-Control: public, max-age=31536000, immutable` for hashed static assets. Small effort, measurable repeat-visit speed gain.

---

## 2. Performance (Core Web Vitals — estimated)

**Finding 2.1 — Homepage payload weight**
What was found (measured directly, not estimated): the EN homepage's own HTML is ~111 KB. Its two aggregated CSS bundles total **~1.43 MB**, its aggregated JS totals **~560 KB**, and the 49 images referenced directly on the homepage total **~5.36 MB** — a combined homepage payload of roughly **7.4 MB** before fonts/third-party tags (Google Tag Manager) are counted.
Why it matters: 7+ MB on a single landing page is heavy by 2026 standards, especially for mobile users on throttled or metered connections, which make up a large share of KSA retail/consumer traffic. This directly affects LCP and bounce rate on mobile.
Suggested direction: In the revamp, set an explicit homepage weight budget (e.g., <1.5 MB initial load) and treat it as an acceptance criterion.

**Finding 2.2 — Animated GIFs used for what appear to be statistics/counter graphics**
What was found: Three of the homepage's images are animated `.gif` files — `truk.gif` (992 KB), `+ 1.5.gif` (1.28 MB), `+ 20000.gif` (659 KB) — together accounting for **~2.9 MB**, more than half of the homepage's total image weight. These sit inside a "statistics" view block (likely a counters/achievements section).
Why it matters: Animated GIF is one of the least efficient formats available for this kind of content; the same visual effect (an animated counter or truck icon) is achievable with a few KB of CSS/JS animation or a short MP4/WebM, at a fraction of the size.
Suggested direction: Rebuild the statistics/counters section as a CSS or lightweight JS number-count animation instead of pre-rendered GIFs. This alone would remove ~2.9 MB from the homepage.

**Finding 2.3 — No next-generation image formats**
What was found: Homepage images are served as `.png`, `.jpg`/`.gif`, and `.svg`. No `.webp` or `.avif` variants were found, and no `srcset`/responsive image markup was observed on the sampled pages.
Why it matters: WebP/AVIF typically cut image payload 25–50% at equivalent visual quality versus PNG/JPG, and responsive `srcset` avoids shipping desktop-sized images to mobile viewports.
Suggested direction: Standard practice for the revamp: serve WebP/AVIF with fallback, and generate responsive `srcset` variants through the CMS's image styles pipeline (Drupal already has this capability via image styles, currently used for cropping but not format conversion).

**Finding 2.4 — Time to first byte and lazy loading**
What was found: TTFB on the EN homepage measured ~712 ms in this test (single sample, not a statistically robust benchmark). `loading="lazy"` is already applied to 34 of the homepage's images — a good practice already in place, though not applied site-wide/consistently (some menu icons and above-the-fold images lack it, appropriately, but coverage should be audited page-by-page).
Why it matters: TTFB in the 700ms range is on the higher side of "acceptable" and worth profiling further; lazy-loading adoption is a genuine existing strength to preserve.
Suggested direction: **[Verify with tool]** Run PageSpeed Insights / Lighthouse and WebPageTest against both AR and EN homepages to get authoritative LCP/INP/CLS field or lab data before finalizing the performance section of the proposal — the figures above are server-side measurements, not full-page rendering metrics.

---

## 3. Bilingual (Arabic/English) Experience

**Finding 3.1 — Root domain defaults to Arabic regardless of browser language**
What was found: Requesting `https://www.nadec.com/` — with or without an `Accept-Language: en-US` header — always returns the Arabic homepage (`<html lang="ar" dir="rtl">`), served at the bare `/` URL rather than redirecting to `/ar`. The English site lives at the separate path `/en`.
Why it matters: This is a deliberate, defensible choice for a Saudi-headquartered company (Arabic-first is appropriate), but it means English-preferring visitors arriving via the bare domain (e.g., from a business card, search result, or backlink to `nadec.com`) land on Arabic content with no automatic language-preference detection, and must self-navigate to `/en`.
Suggested direction: Decide deliberately in the revamp whether to (a) keep Arabic-default at the bare domain (current behavior, valid choice), or (b) add `Accept-Language`-based redirect with a persistent cookie/user override, or (c) serve a lightweight language-selector splash on first visit. Either way, document it as an intentional decision rather than default behavior.

**Finding 3.2 — Missing `hreflang` alternate tags on English pages**
What was found: The Arabic homepage's `<head>` correctly includes `hreflang="en"` pointing to the English equivalent, but the English homepage (`/en`) does **not** include a reciprocal `hreflang="ar"` alternate tag back to the Arabic version (checked directly in page source).
Why it matters: `hreflang` should be bidirectional. One-directional tagging is a common and easy-to-miss technical SEO gap; search engines may not reliably associate the two language versions as alternates of each other, which can affect which version ranks for a given user's locale/language.
Suggested direction: Add reciprocal `hreflang="ar"`/`hreflang="en"` (plus `x-default`) tags across all paired AR/EN templates in the revamp. This is a template-level fix, not a per-page content fix.

**Finding 3.3 — Content parity between AR and EN sections**
What was found: Spot-checking the URLs listed only under `/ar/...` in the XML sitemap (e.g., `board-of-directors`, `branches`, `departments`, `food-safety`, `faqs`, `news`, `initiatives`, `innovation`, `awards`, `vice-presidents`, `recipes`, `social-media`) against their `/en/...` equivalents shows all of them **do** resolve with HTTP 200 in English — so English content exists for these sections even though the sitemap only formally lists the Arabic URL with an alternate-language link for some, and omits several `/en/` entries entirely as first-class sitemap entries.
Why it matters: The underlying bilingual content appears reasonably complete (a genuine strength worth carrying into the proposal), but the sitemap's incomplete/asymmetric listing of English URLs means Google may be crawling and indexing the English pages less consistently than the Arabic ones.
Suggested direction: Regenerate the XML sitemap in the revamp so both language versions of every page are listed as first-class entries with correct reciprocal `hreflang` annotations (ties to Finding 3.2 and 6.2).

**Finding 3.4 — RTL layout implementation**
What was found: The CSS bundle includes 261 `@media` responsive breakpoint rules and only 4 explicit `[dir=...]`-scoped RTL override rules. The `<html dir="rtl">` attribute is correctly set on Arabic pages, and the framework in use (Bootstrap-derived, based on class naming and default color variables observed in the stylesheet) has built-in RTL-aware utilities, which likely accounts for most of the mirroring without needing many custom overrides.
Why it matters: Low explicit RTL rule count is not automatically a problem if the base framework handles mirroring — but it can't be fully confirmed without visual/rendered inspection across both language versions.
Suggested direction: **[Verify with tool]** During discovery, do a side-by-side rendered screenshot comparison of AR vs EN across key templates (homepage, product page, article, form) at 375px/768px/1440px to confirm icons, carousels, and directional UI elements (chevrons, progress bars, back buttons) mirror correctly. Budget for RTL QA as a distinct line item — it is consistently underestimated in bilingual rebuilds.

**Finding 3.5 — Brand tagline not present in homepage markup**
What was found: The tagline referenced in the brand brief ("Nourishing your life everyday") does not appear as text anywhere in the EN or AR homepage HTML (searched directly). It may exist only inside a logo/hero image (not extractable via HTML inspection) or may not currently be surfaced on the homepage at all.
Why it matters: If the tagline is baked into an image, it's invisible to search engines, screen readers, and translation — and can't be verified without OCR/visual inspection.
Suggested direction: **[Verify visually]** Confirm during discovery whether the tagline appears as an image or is simply not featured on the current homepage. Either way, the revamp should render the tagline (in both languages) as real text in the hero/header, which also benefits SEO and accessibility.

---

## 4. Accessibility (WCAG 2.2 basics)

**Finding 4.1 — Existing accessibility toolbar (strength)**
What was found: The site already ships a visible accessibility toolbar with a dark-mode toggle, three font-size options, and a "voice" control (likely a text-to-speech/read-aloud widget), plus a working "Skip to main content" link.
Why it matters: This is a genuine, above-baseline accessibility investment already present on the site and should be explicitly preserved (and ideally extended) in the revamp rather than treated as a gap to fix.
Suggested direction: Carry these features forward; consider adding a visible focus-outline standard and a contrast-boost mode alongside the existing toggles.

**Finding 4.2 — Multiple `<h1>` elements per page**
What was found: The EN homepage contains **five** `<h1>` elements (plus 4 h2, 31 h3, 9 h4, 1 h5, 6 h6).
Why it matters: WCAG/semantic-HTML best practice calls for a single `<h1>` per page representing its primary topic, both for screen-reader users navigating by heading and for SEO topical clarity. Multiple H1s (common in component-driven/block-based page builders, which this appears to be) flatten that hierarchy.
Suggested direction: In the revamp's component library, restrict `<h1>` to the page title template slot; give repeating content blocks/widgets `<h2>`/`<h3>` starting points instead. This is a template-governance fix, not a per-page content fix.

**Finding 4.3 — Missing ARIA landmark roles**
What was found: A `<nav>` element is present, but no `role="banner"`, `role="main"`, `role="navigation"`, or `role="contentinfo"` landmarks were found on the homepage; the only ARIA roles present relate to a dialog/tab-panel widget (`role="dialog"`, `role="tablist"`, `role="tabpanel"`, etc.).
Why it matters: Landmark roles let screen-reader and switch-device users jump directly to header/nav/main/footer regions instead of tabbing through the whole page linearly.
Suggested direction: Add semantic HTML5 landmarks (`<header>`, `<main>`, `<footer>`) or explicit ARIA roles in the new template layer — a small, low-cost addition once the component library is being rebuilt anyway.

**Finding 4.4 — Image alt text: present but partly non-descriptive**
What was found: All 51 images sampled on the EN homepage do have an `alt` attribute (a genuine strength — no missing-alt violations found), but a number of them use the generic value `alt="Menu Icon"` repeated across visually distinct navigation icons (food safety, social media, dairy, etc.), and 5 images use `alt=""` (acceptable only if those are purely decorative — not independently confirmed here).
Why it matters: Screen-reader users hear "Menu Icon" repeated many times with no way to distinguish one navigation item from another, which defeats the purpose of the alt text.
Suggested direction: Replace generic icon alt text with the actual label of each menu item (e.g., `alt="Food Safety"`, `alt="Social Responsibility"`) as part of the navigation rebuild; confirm the empty-alt images are genuinely decorative and mark them `aria-hidden="true"` if so.

**Finding 4.5 — Contact form accessibility (strength)**
What was found: The `/en/contact-us` Webform is well-built from an accessibility standpoint: every input has a properly associated `<label for="...">`, required fields carry both `required` and `aria-required="true"`, and the search field uses a visually-hidden label rather than a placeholder-only pattern.
Why it matters: This is a solid, standards-compliant form implementation already in place — a pattern worth replicating across any new forms added in the revamp (e.g., product inquiry, distributor contact).
Suggested direction: No fix needed; use this form as the internal accessibility reference pattern for new form components.

---

## 5. Information Architecture, Navigation & Content

**Finding 5.1 — Primary navigation and site structure**
What was found: Main navigation surfaces core sections (About, Awards, Feed, Juice, Meat, Milk, News, Statistics), with deeper content (Board of Directors, Investors, Quality, Food Safety, Research, Careers-adjacent links, Documents Library, FAQs) reachable but not all present in the top-level menu based on homepage markup alone.
Why it matters: For a diversified FMCG + publicly listed company, the site is effectively serving three audiences at once — consumers (products/recipes), B2B/media (news, partnerships), and investors (financial disclosures, governance) — and the current top-level nav appears weighted toward the corporate/consumer side rather than clearly branching by audience.
Suggested direction: Consider an audience-based IA in the revamp (e.g., persistent top-level split between "Consumers," "Investors," "Media/Corporate," "Careers") rather than a flat single menu, which is a common and effective pattern for public-company FMCG sites.

**Finding 5.2 — No e-commerce or "where to buy" functionality**
What was found: No shop/cart/checkout functionality or "where to buy"/store-locator content was found anywhere in the homepage or the sampled Milk product page.
Why it matters: This is consistent with NADEC's actual go-to-market (retail distribution through supermarkets/hypermarkets, not direct online sales), so its absence is not inherently a deficiency — but if the RFP scope includes e-commerce, that would be a net-new capability, not a redesign of an existing one, which has significant cost/scope implications.
Suggested direction: Confirm explicitly with the client whether "e-commerce" in scope means (a) full transactional online store, (b) a lighter "where to buy / store locator" feature, or (c) B2B ordering portal for retail partners. These are very different-sized builds and should be priced separately.

**Finding 5.3 — Investor Relations content is substantive and current**
What was found: The `/en/investors` page links directly to annual reports through fiscal year 2025 (a PDF dated with a 2026-03 upload timestamp) and a Disclosure & Transparency Policy PDF, indicating the investor relations content is being actively maintained.
Why it matters: For a Tadawul-listed company, IR content freshness and completeness is a governance-visible area; this is a strength to preserve, not rebuild from scratch.
Suggested direction: In the revamp, prioritize migrating the investor documents library with correct URLs/redirects intact (financial analysts and index providers often bookmark direct PDF links), and consider adding a structured financial calendar / disclosures RSS feed if not already present.

**Finding 5.4 — News content is current**
What was found: The News listing includes articles dated as recently as 6 July 2026 (audit conducted 22 July 2026), indicating active content operations.
Why it matters: Freshness signals (to users and to search engines) are healthy here — this is not an area needing a "make it look active" fix.
Suggested direction: Preserve the existing editorial cadence; ensure the CMS migration doesn't lose publish dates/authorship metadata for existing articles.

**Finding 5.5 — Careers pathway routes through a raw third-party redirect link**
What was found: The careers link on the homepage points to a long, unbranded Microsoft "Safelinks" redirect URL wrapping a third-party `jobs2web.com` careers portal. The raw URL also exposes an internal NADEC employee email address (`em.ishaq@nadec.com.sa`) in plain text within the public page source, as an artifact of how the link was copied from an Outlook-forwarded email into the CMS.
Why it matters: Functionally the link works, but it is unbranded (breaks the user's sense of staying on a trusted NADEC-operated experience) and incidentally exposes an internal staff email address in public HTML — a minor information-hygiene issue worth cleaning up regardless of revamp scope.
Suggested direction: Replace with a clean, branded URL to the careers/jobs portal (either a direct link or a `careers.nadec.com`-style redirect the client controls), removing the Safelinks wrapper and the embedded internal email.

**Finding 5.6 — Trust/certification signals exist but are not surfaced prominently**
What was found: ISO 22000 and ISO 9001 certification mentions were found on the deeper `/en/quality` page, but no certification badges, ISO/SFDA/HACCP marks, or similar trust indicators appear on the homepage or the sampled product page.
Why it matters: For a food/dairy FMCG brand, quality/safety certifications are a high-value trust signal best placed where most visitors actually land (homepage, product pages) rather than several clicks deep.
Suggested direction: Surface certification badges/logos in the homepage footer or a dedicated "Quality & Food Safety" trust strip, linking through to the existing `/quality` content.

**Finding 5.7 — No customer testimonials or third-party social proof found**
What was found: No testimonial content, review snippets, or similar social-proof modules were found on the homepage or product page sampled.
Why it matters: For a consumer FMCG brand this is a lower-priority gap than for a B2B service business (purchase decisions happen at retail shelf, not on-site), but a "trusted by households since 1981 / award recognitions" module (the site does have an Awards section already) could still strengthen brand credibility on-site.
Suggested direction: Low priority; consider surfacing existing Awards content as a homepage trust module rather than building net-new testimonial infrastructure.

---

## 6. Technical SEO

**Finding 6.1 — XML sitemap contains a dead, malformed URL**
What was found: `sitemap.xml` includes the literal entry `http://www.nadec.com/achievements` — using the non-HTTPS scheme and no language prefix. Requesting this exact URL returns **HTTP 404**.
Why it matters: This is a confirmed, verifiable defect: a URL submitted to search engines via the XML sitemap does not resolve. Sitemap errors like this are flagged directly in Google Search Console's Sitemaps report and can slightly erode crawl-budget efficiency and indexing trust signals.
Suggested direction: Remove or correct this entry in the new sitemap; ensure the sitemap generator only emits canonical, live, HTTPS URLs (ties to Finding 3.3's broader sitemap regeneration recommendation).

**Finding 6.2 — Sitemap coverage is sparse relative to actual site size**
What was found: The full `sitemap.xml` lists only 37 `<url>` entries — essentially the top-level corporate/informational pages. Individual news articles, product sub-pages, recipe detail pages, and document-library filtered views do not appear to be individually listed.
Why it matters: A sparse sitemap means search engines rely more heavily on internal-link discovery for deeper content (news articles, recipes), which is less reliable for timely indexing of new content such as press releases or disclosures.
Suggested direction: In the revamp, generate the sitemap programmatically from actual content types (news, recipes, documents) rather than a curated/manual list, so new content is auto-included.

**Finding 6.3 — No structured data (Schema.org/JSON-LD) detected**
What was found: Zero instances of `application/ld+json` structured data were found on the homepage.
Why it matters: For a company of NADEC's profile, `Organization`/`Corporation` schema (logo, social profiles, contact points) and, ideally, `NewsArticle` schema on news pages and `BreadcrumbList` on deep pages, all support richer search-result presentation (knowledge panel eligibility, sitelinks search box, rich snippets).
Suggested direction: Add structured data as a standard part of the new template layer — this is a well-understood, low-risk addition with clear SEO upside for a brand-name/public-company query profile.

**Finding 6.4 — Inconsistent URL structure (clean URLs vs. `/index.php/` paths)**
What was found: Some internal links point to clean URLs (`/en/about`), while others — including the Investors and Privacy Policy links referenced from the homepage — point to `/index.php/en/investors` and `/index.php/en/privacy-policy` style paths. Both resolve, but the pattern is inconsistent.
Why it matters: This is a low-severity but visible technical inconsistency (Drupal's clean-URL routing is enabled but not consistently used when generating internal links), and can occasionally cause duplicate-URL/canonicalization ambiguity if both forms get linked-to or indexed separately.
Suggested direction: Normalize all internal link generation to clean URL form during the rebuild; add canonical tags as a safety net regardless.

**Finding 6.5 — robots.txt is standard/conservative**
What was found: `robots.txt` follows Drupal's default pattern, disallowing admin/system paths only; nothing indexable appears to be unintentionally blocked.
Why it matters: This is healthy and needs no remediation.
Suggested direction: Carry forward as-is; revisit only if the new platform changes URL structure.

---

## 7. Visual Design & Brand Consistency

**Finding 7.1 — Brand color palette is implemented consistently in code**
What was found: The stylesheet's most-used colors are `#2b338c`/`#2B338C` (dark blue, 63 occurrences) and `#001971` (navy, 32 occurrences), with `#7fbc42` (green, 19 occurrences) — consistent with the stated NADEC blue/green brand identity.
Why it matters: This confirms the brand palette is genuinely encoded in the design system rather than applied ad hoc — a solid foundation to carry into the revamp's design tokens.
Suggested direction: Extract these as formal CSS custom properties/design tokens in the new build (if not already) so brand color governance is centralized rather than repeated as literal hex values throughout the stylesheet.

**Finding 7.2 — Leftover default framework colors alongside brand palette**
What was found: Alongside the brand colors, the stylesheet also contains unmodified Bootstrap default utility colors (`#0d6efd` primary blue, `#198754` success green, `#dc3545` danger red, `#ffc107` warning, `#0dcaf0` info, `#6c757d` secondary gray) at meaningful frequency.
Why it matters: This suggests the theme was built on top of Bootstrap's default color system without fully remapping every utility class to brand tokens, which can cause inconsistent-looking UI elements (buttons, alerts, badges) that don't quite match the primary brand palette.
Suggested direction: In the revamp, remap the framework's theme variables (`$primary`, `$secondary`, etc., or CSS custom properties if using a newer Bootstrap) to the brand palette at the source, rather than overriding per-component.

**Finding 7.3 — Visual/rendered design quality**
What was found: Not independently assessed via rendered screenshots in this pass (text/code-level audit only).
Why it matters: Layout composition, spacing, typography scale, and overall visual polish are best judged from rendered views, not raw HTML/CSS.
Suggested direction: **[Verify visually]** Recommend a rendered screenshot pass (desktop/tablet/mobile, AR + EN) before finalizing the design-direction section of the proposal, to support specific before/after visual comparisons — these tend to land well in competitive RFP presentations.

---

## 8. Mobile Responsiveness (inferred from code; not device-tested)

**Finding 8.1 — Responsive framework is genuinely in place**
What was found: The viewport meta tag is correctly configured (`width=device-width, initial-scale=1.0`), and the CSS bundle contains 261 `@media` rules across a full range of breakpoints (376px, 400px, 450px, 500px, 576px, 767px, 768px, 991px, 992px, 1200px, 1399px, 1600px, 1700px) — consistent with a genuinely responsive, Bootstrap-derived grid system rather than a fixed desktop layout with minimal mobile patching.
Why it matters: This indicates mobile responsiveness is architecturally real, not superficial — a meaningful positive to note in the proposal rather than a gap to sell against.
Suggested direction: **[Verify with tool]** Confirm with real-device or emulated testing (Chrome DevTools device mode, BrowserStack) at 320/375/768/1024px that touch targets, the accessibility toolbar, and the statistics/carousel widgets behave correctly — code-level inference is a strong signal but not a substitute for rendered verification, especially given the two page-weight/GIF issues already flagged (Finding 2.1–2.2), which will disproportionately affect mobile load times.

---

## Condensed List for Internal Scoping (Design + Dev Estimation)

| # | Item | Type | Relative Effort |
|---|------|------|------------------|
| 1.1 | Decide: rebuild on existing Drupal vs. migrate stack | Scoping decision | Determines whole-project sizing |
| 1.3 | Fix static asset cache headers | Infra config | Trivial |
| 2.1–2.3 | Homepage payload optimization (image compression, WebP/AVIF, responsive images, replace 3 GIFs with CSS/video) | Performance | Small–Medium |
| 3.1 | Decide language-default/redirect strategy for bare domain | Scoping decision + Small dev | Small |
| 3.2, 6.2 | Rebuild sitemap generation + reciprocal hreflang across templates | Technical SEO | Small–Medium |
| 3.4 | RTL QA pass across all key templates | QA | Medium (often underestimated) |
| 3.5 | Confirm/implement tagline as real text, both languages | Content/Design | Trivial |
| 4.2–4.4 | Semantic heading structure, ARIA landmarks, descriptive icon alt text | Accessibility | Small–Medium (template-level) |
| 5.1 | Audience-based IA redesign (Consumer / Investor / Media / Careers) | UX/IA | Medium–Large |
| 5.2 | Clarify e-commerce scope (full store vs. store-locator vs. B2B portal) | Scoping decision | Determines a major cost variable |
| 5.3 | Migrate investor documents library with URL/redirect integrity | Content migration | Medium |
| 5.5 | Replace careers link with clean branded URL | Content fix | Trivial |
| 5.6 | Surface ISO/quality certifications on homepage/product pages | Content/Design | Small |
| 6.1, 6.3, 6.4 | Fix sitemap dead URL, add structured data, normalize clean URLs | Technical SEO | Small–Medium |
| 7.1–7.2 | Formalize brand design tokens; remap framework default colors to brand palette | Design system | Medium |
| 8.1 | Device/emulator responsive QA pass | QA | Small–Medium |

**Items requiring tools not available in this pass** (recommend running before finalizing the proposal's performance claims):
- Lighthouse / PageSpeed Insights (LCP, INP, CLS field + lab data) for both AR and EN homepages
- Rendered screenshot comparison across breakpoints and both languages
- Real-device RTL layout QA
- Browser console error check (JS errors not visible via static HTML inspection)

---

*Findings are based on direct inspection of publicly accessible pages, HTTP headers, robots.txt/sitemap.xml, and CSS assets on 22 July 2026. No credentials, admin access, or private analytics data were used. Figures marked [Verify with tool] or [Verify visually] should be confirmed with the appropriate tooling before being quoted as final metrics in the client-facing proposal.*
