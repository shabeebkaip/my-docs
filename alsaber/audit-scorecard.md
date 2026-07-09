# Website Audit Scorecard — alsabercars.com

**Auditor:** Senior Website Audit (Code-OX) · **Date:** 9 July 2026
**Pages covered:** Homepage (`/`), car detail (`/car/1045/Mercedes_G63_AMG_2019`), purchase form (`/purchase?car_name=Mercedes_G63_AMG_2019`), `/robots.txt`, `/sitemap.xml`; HTTP-status spot checks on `/about`, `/offers`, `/brands`, `/all-cars`, `/privacy-policy`, `/terms-and-conditions`, `/language/en`; header checks on http/https and www/apex variants.
**Method:** curl with full Chrome headers (server returns 406 to bare clients), Playwright rendered audit at 1366/375/320 px, DOM inspection, console and network capture. Performance figures cited from Google PageSpeed, 8 July 2026 (measured, not estimated).

---

## Executive Summary

**Overall Score: 46 / 100 — Grade F**

The site presents a genuinely attractive dark luxury theme and a working inventory browse-and-enquire flow, but it is structurally invisible to search, measurably slow (Google-measured LCP 57.5 s mobile on a 34 MB payload), and its single conversion path drops the car the buyer selected. The result is a website that functions as a brochure for visitors who already know it exists, and converts almost none of them.

**Top strengths**
- Coherent dark luxury visual theme; consistent Tajawal typography; logo present on every page
- Clean, stable rendering: zero console errors/warnings on all three audited pages; CLS 0.015 (measured — excellent)
- Correct HTTPS with HTTP→HTTPS 301; Laravel CSRF tokens on all forms
- Car detail pages carry real substance: price (465,000 SAR), 67 spec rows, detailed Arabic description, 18-photo gallery

**Critical issues**
1. Search invisibility: empty meta descriptions sitewide, no H1 on any page, `/sitemap.xml` 404, zero structured data, zero Open Graph tags
2. Performance: 34,252 KiB payload, LCP 57.5 s mobile / 9.2 s desktop, FCP 9.4 s (all measured by PageSpeed 8 Jul 2026)
3. Broken conversion hand-off: `?car_name=` parameter ignored — buyer must re-find their car in a 782-option dropdown, then complete a salary/commitments finance form before any human contact
4. Images: 118 of 119 rendered images without alt text; car galleries are CSS `background-image` divs (uncrawlable, un-altable); 0 WebP; 0 lazy loading; no Cache-Control on gallery JPGs

**Immediate priorities (this week):** meta descriptions + H1s + sitemap.xml; pre-fill the purchase form from the URL parameter; compress/convert hero and gallery images and add cache headers; add security headers.

---

## Category Scores

| # | Category | Score | Max | Why |
|---|----------|------:|----:|-----|
| 1 | User Experience | 8 | 15 | Clear nav and working search on desktop; car pages informative. Lost points: purchase hand-off discards car selection, no breadcrumbs/wayfinding, mobile first screen offers no action or search. |
| 2 | UI Design | 6 | 10 | Consistent dark theme, good hierarchy on car page. Lost points: template-generic components, low-contrast body copy on hero, framed hero image clipped on mobile. |
| 3 | Branding | 3 | 5 | Logo visible everywhere, consistent palette. Lost points: no ownable identity beyond the logo; unbranded default Laravel 404 page (English). |
| 4 | Mobile Responsiveness | 6 | 10 | Layout adapts at all breakpoints, hamburger menu works. Lost points: horizontal overflow at 375 px (380 px doc) and 320 px (333 px doc), hero clipping, search hidden on mobile. |
| 5 | Accessibility | 4 | 10 | PageSpeed accessibility 82 (measured). Lost points: 118/119 images no alt, 0 H1, no `<main>`/`<header>` landmarks, no skip link, 22 buttons + 10 links without accessible names, 9/33 form controls with programmatic labels, 10 px minimum font. |
| 6 | SEO | 4 | 15 | robots.txt valid (allow-all), unique titles per page, clean URLs. Lost points: empty meta description/keywords sitewide, no H1, sitemap.xml 404, no canonical, no structured data, no OG/Twitter, no hreflang despite EN version, www + apex both 200 with mixed internal links (duplicate-content risk), galleries invisible to image search. |
| 7 | Performance | 3 | 10 | Measured (PageSpeed 8 Jul 2026): 55 mobile / 54 desktop; FCP 9.4 s; LCP 57.5 s mobile / 9.2 s desktop; SI 19.5 s; payload 34,252 KiB; render-blocking savings 8,980 ms; image savings 17,126 KiB; cache savings 26,670 KiB. TBT 80 ms and CLS 0.015 are good — weight, not scripting. |
| 8 | Security | 2 | 5 | HTTPS valid, HTTP→HTTPS 301, CSRF tokens, session cookies HttpOnly/SameSite. Lost points: zero security headers (no HSTS, CSP, X-Frame-Options, X-Content-Type-Options), jQuery 3.3.0 (pre-3.5, known XSS CVE-2020-11022/23), `Access-Control-Allow-Origin: *` on HTML. |
| 9 | Content Quality | 3 | 5 | G63 page has a genuinely good Arabic description (engine, torque, options). Lost points: inconsistent depth across listings, raw data-label formatting in spec/feature tables, empty descriptions on some cars (per prior walkthrough). |
| 10 | Conversion Optimization | 1 | 5 | A CTA exists on every car. Lost points: selection discarded at the form, finance interrogation before contact, no per-car WhatsApp/call/callback, no monthly-payment context, no lead capture for not-ready buyers, no required/inline validation. |
| 11 | Technical Quality | 3 | 5 | No console errors, no broken links in sample (all spot-checked pages 200). Lost points: invalid `direction="rtl"` attribute (works only via CSS), sitemap 404, 634 KB purchase HTML (852 server-rendered `<option>`s), favicon declared `type="image/gif"` for a PNG. |
| 12 | Trust & Credibility | 3 | 5 | Privacy policy + terms pages live, footer contact incl. WhatsApp 920013757, 5 social profiles, about page (200). Lost points: no testimonials, no certifications/CR number visible, watermarked warehouse photography. |
| | **Total** | **46** | **100** | **Grade F** (F < 50) |

---

## Findings (Critical first)

### CRITICAL

**C1 · Site is structurally invisible to search**
*Evidence:* All three audited pages ship `<meta name="description" content="">` and `<meta name="keywords" content="">`; 0 `<h1>` elements on any page; `/sitemap.xml` returns 404 (default Laravel page); 0 `ld+json` blocks; no Open Graph/Twitter tags; no `<link rel="canonical">`; no hreflang although `/language/en` (302, session-based EN version) exists.
*Impact:* The inventory cannot rank, cannot show rich results, and shared car links arrive on WhatsApp as bare URLs. Consistent with CWV field data "Not applicable" (traffic below Google's measurement floor).
*Recommendation:* Per-page meta descriptions and H1s; generate sitemap.xml from inventory and reference it in robots.txt; add Vehicle/AutoDealer/Offer JSON-LD and OG tags on car pages; canonical tags; pick one host (www) and 301 the other.
*Expected benefit:* Baseline eligibility for organic and image search plus rich WhatsApp previews — the cheapest traffic channel currently at zero.

**C2 · Measured performance far outside acceptable range**
*Evidence (Google PageSpeed, 8 Jul 2026 — measured):* mobile 55 / desktop 54; FCP 9.4 s; LCP 57.5 s mobile, 9.2 s desktop; Speed Index 19.5 s; payload 34,252 KiB; render-blocking savings 8,980 ms; image savings 17,126 KiB; cache savings 26,670 KiB. Browser check confirms: 0 WebP among 109 loaded images, 0 `loading="lazy"`, gallery JPGs served with `Last-Modified` but no `Cache-Control`.
*Impact:* Most mobile visitors never see a car; ad and social spend delivers users to a blank screen.
*Recommendation:* WebP/AVIF conversion + responsive sizes; lazy-load below-fold; defer non-critical JS/CSS with critical CSS inline; long-lived immutable cache headers on static assets.
*Expected benefit:* Estimated LCP under ~3 s and payload under ~3 MB with standard techniques (estimate — verify by re-running PageSpeed after each change).

**C3 · The conversion hand-off drops the buyer's car**
*Evidence:* `/purchase?car_name=Mercedes_G63_AMG_2019` renders the car `<select name="car_id">` with placeholder "اختر سيارة" and 782 options — no field on the page contains "G63". The finance path (default tab) then asks salary, commitments, mortgage status, installments, city, work sector, bank, driving licence — before any contact. 0 `required` attributes; 9/33 inputs have programmatic labels; money fields use `type="number"` spinners.
*Impact:* Maximum friction at the moment of highest intent; very plausibly the largest single conversion leak.
*Recommendation:* Pre-select the car from the URL parameter (one controller/JS change); default to a short lead form (name, phone, car) with finance details as an optional follow-up; add per-car WhatsApp/call buttons.
*Expected benefit:* Direct lift in completed enquiries; measurable within weeks via form analytics.

**C4 · The product photography is invisible to machines**
*Evidence:* Homepage: 126 `<img>` tags, 1 alt attribute (rendered: 118/119 without alt). Car galleries are `div.rtl-slider-slide` CSS `background-image` elements — 18 full-res DSLR JPGs (129–498 KB each) loaded eagerly into 339×270 slots; as backgrounds they can never carry alt text and are excluded from Google Images.
*Impact:* Entire inventory absent from image search (a primary car-shopping channel); accessibility failure; bandwidth waste.
*Recommendation:* Replace background divs with `<img>` + descriptive Arabic/English alt ("مرسيدس G63 AMG 2019 أبيض — خلفية"); serve sized WebP variants; lazy-load.
*Expected benefit:* Image-search discovery for every car plus a large share of the 17 MB measured image savings.

### HIGH

**H1 · Zero security headers; outdated jQuery**
*Evidence:* Response headers contain no Strict-Transport-Security, Content-Security-Policy, X-Frame-Options, or X-Content-Type-Options; `Server: Apache` banner exposed; `Access-Control-Allow-Origin: *` on HTML; jQuery 3.3.0 in page (pre-3.5 — CVE-2020-11022/11023 XSS).
*Impact:* Clickjacking/downgrade/XSS surface larger than necessary on a site collecting salary and bank data.
*Recommendation:* Add the four headers at Apache level (30-minute task); upgrade jQuery to 3.7.x.
*Expected benefit:* Standard hardening; protects the most sensitive form on the site.

**H2 · Duplicate hosts with no canonical**
*Evidence:* `https://www.alsabercars.com/` and `https://alsabercars.com/` both return 200 with identical content; internal links mix both hosts (nav uses www, assets and some car links use apex); no canonical tags.
*Impact:* Split link equity and duplicate-content ambiguity for every URL on the site.
*Recommendation:* 301 apex→www and add canonicals.
*Expected benefit:* Consolidated ranking signals; prerequisite for any SEO work paying off.

**H3 · Horizontal overflow and clipped hero on phones**
*Evidence:* documentElement.scrollWidth 380 px at 375 px viewport; 333 px at 320 px. Hero's framed car image clipped at the right edge (screenshot); search bar and any CTA absent from the mobile first screen; minimum rendered font 10 px.
*Impact:* Side-to-side wobble and cropped visuals on the majority traffic device; first screen offers nothing to do.
*Recommendation:* Fix the overflowing element (likely the hero frame), add a search/CTA to the mobile hero, raise minimum font to 12 px+.
*Expected benefit:* Cleaner mobile first impression; fewer immediate bounces.

**H4 · Accessibility structure missing (PageSpeed 82 — measured)**
*Evidence:* No `<main>`/`<header>` landmarks, no skip link, 22 buttons and 10 links with no accessible name, 9/33 labelled form controls, heading structure starts at h2.
*Impact:* Screen-reader users cannot orient; unnamed controls are also unreadable to crawlers.
*Recommendation:* Landmarks, aria-labels on icon controls, `<label for>` on all inputs, one H1 per page.
*Expected benefit:* Accessibility score into the 90s; overlaps heavily with SEO fixes.

**H5 · Purchase page ships 634 KB of HTML**
*Evidence:* 634,595-byte document containing 852 server-rendered `<option>` elements (782 cars, 43 cities, banks, installments) duplicated across individual/corporate forms.
*Impact:* Slowest possible start for the funnel's most important page, especially on mobile data.
*Recommendation:* Async searchable select (Select2 with AJAX source — Select2 is already loaded) instead of embedding the full inventory twice.
*Expected benefit:* ~90% smaller purchase page (estimate — verify with curl after change).

**H6 · English version exists but is invisible to search**
*Evidence:* `EN` switcher → `/language/en` → 302 back to the same URLs (session-based language); no hreflang anywhere; same URL serves both languages.
*Impact:* English luxury-buyer searches ("G63 for sale Riyadh") cannot land on English content; Google may index either language unpredictably.
*Recommendation:* Language-prefixed URLs (`/en/...`) with hreflang pairs.
*Expected benefit:* Opens the English-speaking premium segment as an indexable audience.

### MEDIUM

**M1 · Invalid `direction="rtl"` attribute** — `<html lang="ar" direction="rtl">` on all pages; the valid attribute is `dir`. Rendering survives only because `bootstrap.rtl.min.css` sets CSS `direction: rtl`. Fix: use `dir="rtl"`. Benefit: correct semantics for assistive tech and parsers.
**M2 · robots.txt lacks a Sitemap directive** — file exists and allows all (200), but points crawlers nowhere. Add `Sitemap:` line once sitemap.xml exists.
**M3 · Form UX gaps** — no `required` attributes or inline validation, no progress indication on the long finance path, number-spinner controls on money fields. Standard form hygiene pass recommended.
**M4 · Listing data formatting** — spec/feature tables show raw label:value output in places (per 8 Jul walkthrough, e.g. "determination: 850" on the EN rendering). Editorial mapping of DB labels to human labels recommended. *(Partially verified: the Arabic G63 table reads acceptably; EN-side labels not re-verified in this session.)*
**M5 · No lead capture for not-ready buyers** — no callback request, stock alerts, or saved-car account behind the heart icon.
**M6 · Split image origin without Timing-Allow-Origin** — pages on www load images from apex; extra connection cost and opaque resource timing.

### LOW

**L1 · Unbranded default Laravel 404 page** in English on an Arabic luxury site (seen at /sitemap.xml).
**L2 · Favicon declared `type="image/gif"` for a PNG, 16×16 only** — no touch icons.
**L3 · `Server: Apache` banner** — cosmetic hardening.

---

## Priority Roadmap

**Immediate (0–7 days)** — C1 (meta descriptions, H1s, sitemap.xml + robots Sitemap line [M2], canonicals), C3 (pre-fill car from URL param; short-form default), H1 (four security headers), H2 (301 apex→www), M1 (dir attribute).
**Short-term (1–4 weeks)** — C2 (WebP + lazy-load + cache headers + defer render-blocking), C4 (galleries to `<img>`+alt), H3 (mobile overflow + mobile hero CTA), H5 (async car select), H4 (landmarks/labels/names), M3 (form validation + steps), C1 remainder (Vehicle JSON-LD + OG tags).
**Long-term (1–3 months)** — H6 (URL-based EN + hreflang), M4 (listing data editorial pass), M5 (lead capture: callbacks, stock alerts, accounts), jQuery/stack modernisation (H1 tail), photography standard, L1–L3 polish.

---

## Competitive Assessment

Against modern automotive-retail standards (syarah.com, motory.sa, manufacturer dealer sites): competitors deliver sub-3 s LCP pages, full-screen 15–30-photo galleries with exterior-first ordering, monthly-payment context beside every price, per-car WhatsApp CTAs, structured data feeding Google rich results, and bilingual indexable content. alsabercars.com currently competes on none of these axes; its genuine advantages (inventory breadth, premium stock, an attractive theme direction) are neutralised by delivery. The gap is execution, not concept — every one of these standards is reachable on the existing Laravel stack.

## Final Verdict

**Grade F (46/100).** In plain terms: the showroom's digital front door is slow enough that most mobile visitors leave before seeing a car, invisible enough that Google cannot send meaningful traffic, and its one "Buy" journey forgets which car the buyer chose. None of this reflects on the business itself — these are normal maturing steps for a site that has outgrown its original template. The fix order is: be findable (SEO basics), be fast (images + caching), don't drop the buyer (form hand-off). Re-measure with PageSpeed and Search Console after each phase.

---

# CROSS-CHECK — vs. Code-OX client report (`alsaber/website-report.html`, 45 findings, 8 Jul 2026)

### (a) Findings my independent audit contradicts or cannot support

1. **Finding 37 — "No sitemap and no robots.txt — both return 404": partially wrong.** `/robots.txt` returns **200** with a valid allow-all policy (`User-agent: *` / `Disallow:`). Only `/sitemap.xml` is 404. The finding (and the fix-first bullet "No sitemap, no robots.txt — Google crawls blind") must be corrected to "no sitemap, and robots.txt names no sitemap." A client-side developer can falsify the current wording in one request.
2. **Finding 33 — "Purchase form is entirely in English": not reproducible in a default session.** In a fresh Arabic session the form renders fully in Arabic (طلب شراء / افراد / شركات / تمويل / كاش / الأسم / رقم الهاتف). The English rendering appears only after the auditor's session was switched via the EN toggle (language is session-based). The real finding is different and still valid: *the site silently keeps you in the last-selected language with no per-URL language*, and some EN translations are poor ("Total salary in ATM"). Reframe before client delivery — as written, a live demo will contradict the report.
3. **Finding 41 — "Arabic only — no English version exists": wrong as stated.** An English version exists behind the header `EN` switcher (`/language/en`). The defensible claim is the hreflang/indexability one (my H6): the EN version is session-based, shares URLs, and is invisible to English search. Same conclusion, different — and correct — mechanism.
4. **Findings 14 / 15 / 18 (G63 gallery: "3 interior tiles, no gallery"): stale as of 9 July.** The G63 photos were re-uploaded 8 Jul 06:57 (Last-Modified headers). Live page now serves an **18-photo slick carousel** (3-up), opening with exterior/detail shots, plus a substantive Arabic description — not "1 photo / 2-word description" for this car. The Porsche-page examples may still hold, but the G63 screenshots (shot-1, shot-2) no longer match the live site. Re-capture evidence or re-scope these findings to the listings that still exhibit the problem. Legitimate residuals on the G63: no lightbox/full-width hero, no photo counter, thumbnails as CSS backgrounds.
5. **Fix-first bullet "No WhatsApp, no call button — only a salary form": overstated.** A site-wide WhatsApp link (`wa.me/920013757`) exists in the footer. The correct, still-strong claim is finding 20's car-page version: no per-car WhatsApp/call/viewing CTA at the point of desire.

### (b) Material issues the report misses

1. **Security is entirely absent from the report** — zero security headers (HSTS, CSP, X-Frame-Options, X-Content-Type-Options) on a site collecting salary, commitments, and bank data; jQuery 3.3.0 with known XSS CVEs; `Access-Control-Allow-Origin: *`. For a revamp pitch this is a strong, verifiable additional pillar.
2. **Duplicate hosts:** www and apex both serve 200 with no canonical and mixed internal linking — a fundamental SEO defect that belongs beside findings 35–42.
3. **Purchase page weight:** 634 KB HTML with 852 server-rendered options — an independent, easily demonstrated performance/CRO fact about the funnel's key page.
4. **Mobile horizontal overflow** (380/375, 333/320) — concrete, reproducible mobile defect; the report's mobile findings are otherwise impressionistic.
5. **Galleries as CSS backgrounds** — explains *why* alt text is absent on car photos and strengthens finding 38.
6. Minor but citable: invalid `direction="rtl"` attribute; robots.txt missing Sitemap line; unbranded English Laravel 404 page.

### (c) Verdict — is the report client-ready as revamp-pitch evidence?

**Nearly, but not as-is.** The performance and SEO core (findings 1–8, 35–40, 42), the conversion analysis (20–32, 34), and the measured PageSpeed evidence are accurate, well-framed, and independently confirmed — that is ~85% of the report and it is strong. However, it should not go in front of the client until four corrections are made, because each is refutable in a live demo: fix the robots.txt claim (37), reframe the English-form finding (33) and the "no English version" finding (41), and re-verify/re-scope the G63 gallery evidence (14/15/18) against the refreshed photos. Optionally add the missed security-headers finding — it adds a pillar the current report lacks. With those changes, the report is client-ready and persuasive.
