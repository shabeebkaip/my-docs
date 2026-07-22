# NADEC — Aetheris AI Audit Findings (Deep Crawl, 50 Pages)

### Source: Aetheris AI — AI Marketing Platform (Code-OX's internal audit tool, marketing-agent.code-ox.com/audit)
### Audited URL: https://www.nadec.com/en
### Report generated: 22 July 2026, 17:30 (PDF timestamp on file: "7/22/26, 5:30 PM")
### Crawl depth: 50 pages (tool's stated maximum — "Crawled 50 page(s) from this domain (max 50)")
### Source PDF: `/Users/shabeeb/Downloads/Aetheris AI — AI Marketing Platform.pdf` (105 pages)

**Relationship to `nadec/seo-audit-findings.md` (the earlier, 22 July 2026 spot-check audit):**
- **Corroborates:** no structured data sitewide, no hreflang, weak/missing H1s, duplicate meta descriptions, thin product content, Core Web Vitals field data (LCP 4.8s mobile / 3.6s desktop — exact match), Drupal + Cloudflare stack, strong security headers, HTTPS/HSTS.
- **Extends with page-level specificity:** exact duplicate title-tag pairs and URLs, exact thin-content page URLs, exact broken-image file paths, exact oversized-image file paths and sizes, exact sitemap URL count (37, vs. the earlier audit's "~40" estimate), exact backlink/domain-authority numbers (previously flagged as a data gap — now partially closed).
- **Adds a new category not in the earlier audit:** **GEO (Generative Engine Optimization)** — AI-search discoverability (llms.txt, entity/identity schema, LLM-readability of rendered content). See Section 6 below; this connects directly to NADEC's own ISO/IEC 42001 AI-governance narrative already used in the technical proposal (see the flag at the end of Section 6).
- **Explains an apparent discrepancy** between this report's Lab PageSpeed scores (Mobile 30/100, LCP 23.5s; Desktop 33/100, LCP 5.6s) and the Field/CrUX data in both this report and `pagespeed-data.md` (Mobile LCP 4.8s, Desktop LCP 3.6s) — see Section 2 for the full explanation. These are not contradictory; they are different measurement methodologies captured in the same report.
- **New finding not present in the earlier audit at all:** a spam/black-hat anchor-text signal in the backlink profile ("TELEGRAM@SEO_ANOMALY..." with 257 occurrences) and heavy backlink concentration on a third-party Azure microsite rather than nadec.com itself — see Section 5.

---

## 0. Overall Audit Scorecard (as reported by the tool)

| Metric | Value |
|---|---|
| Overall grade | **C- (64/100)** |
| Pages crawled | 50 |
| Checks passed / warnings / failed | 46 passed / 18 warnings / 15 failed |
| Issues by priority | 4 High / 20 Medium / 9 Low |
| Avg load time (across 50 pages) | 560ms |
| Avg words/page | 531 |
| Images sitewide | 1,018 (96% with alt text) |
| Broken links | 0 |
| Internal links | 2,777 |
| Score trend | "±0 vs Jul 22" (no prior-audit delta shown — this is the tool's first recorded run for this URL) |

**Category letter grades:**

| Category | Grade | Failed / Warnings / Passed |
|---|---|---|
| Performance | C | 4 failed / 5 warnings / 12 passed |
| On-Page | D | 4 failed / 9 warnings / 5 passed |
| Technical | B | 2 failed / 3 warnings / 18 passed |
| Links | A | 1 failed / 5 passed |
| Social | C | 2 failed / 1 warning / 5 passed |
| GEO | F | 2 failed / 1 passed |

**GEO = Generative Engine Optimization** (AI-search discoverability — how well the site can be found, parsed, and cited by AI answer engines/LLMs, as distinct from traditional Google/Bing SEO). This is a category the earlier `seo-audit-findings.md` did not evaluate at all. **Flag for the proposal:** NADEC's technical proposal already leans on an ISO/IEC 42001 AI-governance narrative (confirmed elsewhere in this engagement) — an **F grade in GEO is a direct, quantified gap in the same "AI-readiness" story NADEC is telling about itself**. Recommending GEO remediation (identity schema, llms.txt) is a natural, on-brand extension of that narrative rather than a generic SEO upsell, and is worth surfacing prominently in the proposal rather than buried as a low-priority checklist item.

**Top 5 Priority Fixes (as ranked by the tool):**
1. **Critical — Mobile performance poor.** Reduce JavaScript, compress images (WebP), improve server response time. *Major impact / Performance.*
2. **Critical — Real users experience slow loading (LCP over 4s).** Compress and preload the hero image, reduce server response time, eliminate render-blocking resources. *Major impact / Performance.*
3. **Serve all scripts, styles, images, and media over https://** — browsers block or warn on mixed content, breaking pages and eroding trust. *Major impact / Technical SEO.*
4. **Fix or remove references to missing files** — broken images/scripts degrade layout and functionality for real visitors. *Major impact / Links.*
5. Use caching, a CDN, or optimize server-side processing to achieve sub-500ms response. *Moderate impact / Performance.*

---

## 1. Full 33-Item Recommendations List (priority + category, as reported)

| # | Recommendation | Category | Priority |
|---|---|---|---|
| 1 | Critical: mobile performance poor — reduce JS, compress images (WebP), improve server response time | Performance | High |
| 2 | Critical: real users experience slow loading (LCP over 4s) — compress/preload hero image, reduce server response, eliminate render-blocking resources | Performance | High |
| 3 | Serve all scripts, styles, images, and media over https:// | Technical SEO | High |
| 4 | Fix or remove references to missing files (broken images/scripts) | Links | High |
| 5 | Use caching, a CDN, or optimize server-side processing to achieve sub-500ms response | Performance | Medium |
| 6 | Critical: desktop performance poor — reduce JS, compress images (WebP), improve server response time | Performance | Medium |
| 7 | Review color contrast, ARIA attributes, form labels, and alt text using Lighthouse's accessibility audit (mobile) | Performance | Medium |
| 8 | Review color contrast, ARIA attributes, form labels, and alt text using Lighthouse's accessibility audit (desktop) | Performance | Medium |
| 9 | Compress images and serve modern formats (WebP/AVIF) — large images consistently biggest contributor to slow loads | Performance | Medium |
| 10 | Each page should have a unique title | On-Page SEO | Medium |
| 11 | Every page needs a unique, compelling meta description | On-Page SEO | Medium |
| 12 | Write a unique meta description for each page (duplicates reduce CTR) | On-Page SEO | Medium |
| 13 | Use only one H1 per page; convert extras to H2 | On-Page SEO | Medium |
| 14 | Add a descriptive H1 to every page | On-Page SEO | Medium |
| 15 | Each page should have exactly one H1 | On-Page SEO | Medium |
| 16 | Add more quality content to thin pages or consolidate them | On-Page SEO | Medium |
| 17 | Use headings in strict order (H1→H2→H3) without skipping levels | On-Page SEO | Medium |
| 18 | Page is mostly markup with little visible text — add substantial content, reduce inline scripts/styles | On-Page SEO | Medium |
| 19 | Add og:title, og:description, og:image | On-Page SEO | Medium |
| 20 | Consolidate or clearly differentiate near-duplicate pages | On-Page SEO | Medium |
| 21 | Add missing pages to the sitemap so search engines can discover/prioritize them | Technical SEO | Medium |
| 22 | Remove dead URLs from the sitemap | Technical SEO | Medium |
| 23 | Add an SPF TXT record | Technical SEO | Medium |
| 24 | Add Organization or Person JSON-LD schema to help AI engines identify your entity | GEO | Medium |
| 25 | Move inline styles to an external stylesheet | Performance | Low |
| 26 | Convert JPEG/PNG images to WebP or AVIF | Performance | Low |
| 27 | Remove the meta keywords tag (deprecated, exposes keyword strategy to competitors) | On-Page SEO | Low |
| 28 | Add Schema.org JSON-LD to unlock rich snippets | On-Page SEO | Low |
| 29 | Use short, lowercase, hyphen-separated URLs with few query parameters | Technical SEO | Low |
| 30 | Add og:title, og:description, og:image for rich social previews (Facebook/LinkedIn) | Social | Low |
| 31 | Install Facebook Pixel to track conversions, build custom audiences, enable remarketing | Social | Low |
| 32 | Add twitter:card meta tag for rich X/Twitter link previews | Social | Low |
| 33 | Create a /llms.txt file to help LLMs understand site content and structure | GEO | Low |

---

## 2. Performance — Reconciling Lab vs. Field Data (important for the proposal)

The report contains **two different, non-contradictory performance datasets**. Both need to appear in the proposal, framed correctly, or the numbers will look like they conflict.

### Field data (real-user, Chrome UX Report, 28-day p75) — matches `pagespeed-data.md` exactly
| Metric | Mobile | Desktop |
|---|---|---|
| LCP | **4.8s** (Slow) | **3.6s** (Average) |
| INP | 142ms (Fast) | 47ms (Fast) |
| CLS | 0.02 (Fast) | **0.62** (Slow) |
| Overall CWV assessment | **SLOW** | — |

### Lab data (synthetic Lighthouse run, throttled connection/device simulation, captured within this report)
| Metric | Mobile | Desktop |
|---|---|---|
| PageSpeed score | **30/100** | **33/100** |
| First Contentful Paint | 11.4s | 2.0s |
| Speed Index | 11.9s | 3.3s |
| **Largest Contentful Paint** | **23.5s** | **5.6s** |
| Time to Interactive | 31.5s | 6.7s |
| Total Blocking Time | 1,400ms | 1,010ms |
| Cumulative Layout Shift | 0.019 | 0.009 |
| Accessibility | 77/100 | 85/100 |
| Best Practices | 96/100 | 96/100 |
| SEO (Lighthouse) | 92/100 | 92/100 |

**Why these are not contradictory:** Field data is what actual visitors experienced over the last 28 days on their real devices/networks (p75 — 75th percentile). Lab data is a single synthetic test run under Lighthouse's standardized throttling profile (simulated slow mobile CPU/network), which is intentionally much harsher than real-world conditions — that's why lab LCP (23.5s mobile) reads dramatically worse than field LCP (4.8s mobile). Both numbers are legitimate and both matter: **field data is what's actually hurting real users and rankings today; lab data is a stress-test that reveals exactly which resources (hero image, render-blocking JS) are the ceiling on performance once traffic or network conditions are less favorable.** The same pattern holds on desktop (lab LCP 5.6s vs. field LCP 3.6s).

**Why this report's numbers differ slightly from `pagespeed-data.md`'s Lighthouse Performance scores (44 mobile / 67 desktop):** `pagespeed-data.md` was captured at **13:24** on 22 July 2026; this report's lab run was captured at **17:30** the same day — roughly a **4-hour gap**. Lighthouse lab scores are known to vary run-to-run (server load, CDN cache state, and even Google's PSI test-runner capacity at the moment of the request all affect the throttled simulation). A ~4-hour gap producing a lower lab score in the later run (30/33 vs. 44/67) is consistent with normal Lighthouse run-to-run variance, not a real regression in the site — the **field/CrUX data, which is the trustworthy real-user signal, is identical in both reports** (Mobile LCP 4.8s / Desktop LCP 3.6s), which is the strongest evidence these are measurement-methodology differences, not conflicting facts about the site. **Recommendation for the proposal: lead with field/CrUX data as the primary evidence (it's stable and matches across both audits); cite lab data only to illustrate root causes (hero image weight, render-blocking JS, TBT), not as a second contradictory score.**

### Additional Performance detail not in the earlier audit
- **Homepage response time: 1,096ms** (fails the tool's <500ms target) vs. **average across 50 pages: 560ms** (passes) — the homepage itself is the slowest-responding template on the site, not typical.
- **Resources breakdown (homepage):** 60 total objects — 1 HTML, 4 JS, 2 CSS, 51 images, 0 iframes, 2 other.
- **Inline styles: 14 found** on the homepage (Low priority — move to external stylesheet for caching).
- **Gzip/Brotli compression: enabled** (pass).
- **Oversized images (8 found, over 200KB each):**
  - `/sites/default/files/2024-05/%2B%201.5.gif` — **1,252 KB**
  - `/sites/default/files/2024-05/truk.gif` — **969 KB**
  - `/sites/default/files/hadec/food_safety/inner2.png` — **862 KB**
  - (+5 more not individually named in the report)
- **Modern image formats: 20 legacy-format images** (JPEG/PNG/GIF instead of WebP/AVIF) sitewide — Low priority, 25-50% file-size savings available at equal visual quality.

---

## 3. On-Page SEO — Page-Level Specifics

### Duplicate title tags (report states "5 duplicate title(s)" — 3 title strings explicitly named, a 4th confirmed independently below)
The aggregate summary explicitly lists three duplicated title strings:
1. **"Red meat(Protein) | Nadec"** — confirmed at both `/index.php/en/meat` (page-by-page row 30) and `/en/meat` (row 44)
2. **"About | Nadec"** — confirmed at both `/index.php/en/about` (row 9) and `/en/about` (row 20)
3. **"Food and Vegetables | Nadec"** — confirmed at both `/en/feed` (row 32) and `/index.php/en/feed` (row 46)

**Independently confirmed via the page-by-page report (not named in the aggregate summary's truncated text):**
4. **"Juices | Nadec"** — also duplicated, at both `/index.php/en/juice` (row 39) and `/en/juice` (row 40)

**Pattern:** every duplicate-title pair found is the **same content served at two URL forms — the legacy `/index.php/en/X` path and the clean `/en/X` path** — not unrelated pages accidentally sharing a title. This is a clean-URL migration that was never completed with redirects/canonicalization, which is also the direct mechanical cause of the Near-Duplicate Content findings in the next subsection. **Note for the proposal:** the report's own summary count ("5 duplicate title(s)") does not cleanly reconcile with the 3 pairs (6 pages) it explicitly names, and we found a 4th pair independently in the row-level data — treat "5" as a probable undercount/display-truncation artifact of the tool rather than an exact figure, and cite the 4 confirmed pairs (8 pages) as the verified minimum.

### Missing meta description
- **`/en/news/642`** — the only page (1/50) missing a meta description entirely. High priority per the tool (this specific check, uniquely among meta-description issues, is flagged High priority rather than Medium).

### Duplicate meta descriptions (3 duplicate description groups)
- **"At Nadec we are consumer-focused as we..." — duplicated across 23 pages.** This is the corporate boilerplate description the earlier audit flagged as reused on `/ar/milk`; this report quantifies it precisely — 23 of the 50 crawled pages (46%) share this identical description, including the homepage, About, and multiple category pages confirmed in the page-by-page rows (`/en`, `/en/about`, `/index.php/en/about`, `/en/branches`, `/en/social-media`, etc.).
- "Organic Olive Oil..." — duplicated across 3 pages (matches the olive oil product line: `/en/products/313`, `/en/products/343`, `/en/products/312` all returned "Organic Olive Oil" as their SERP snippet description).
- "Strawberry Mojito Juice Made From Concentrates..." — duplicated across 2 pages (`/en/products/483` and `/en/products/484`, the 1.3L and 180ml SKUs of the same product).

### H1 findings (quantified precisely — the earlier audit only spot-checked 2 pages)
- **48/50 pages (96%) are missing an H1 entirely.** Named examples: `/index.php/en/meat`, `/index.php/en/about`, `/index.php/en/food-safety`, `/index.php/en/quality` (+44 more).
- **2/50 pages have 5 H1s each** (the opposite extreme): the **EN homepage (`/en`)** and **AR homepage (`/ar`)** each render 5 separate H1 elements instead of one.
- **Heading hierarchy is broken on 50/50 pages (100%).** Every single crawled page's heading structure **starts at H6 with no H1–H5 present before it** — e.g., `/en` starts with H6 (no H1 first); `/index.php/en/meat` starts with H6 (no H1 first); `/index.php/en/about` starts with H6 (no H1 first) (+47 more). This is a sitewide templating/CMS-theme issue, not a per-page content gap — it points at the Drupal theme's heading markup, not editorial oversight.

### Thin content pages (<300 words) — 8/50 pages
Named in the aggregate summary: `/en/products/483`, `/en/awards/554`, `/en/products/54`, `/en/products/484` (+4 more). Cross-referenced against the page-by-page report, the following additional thin-content pages were independently confirmed with exact word counts:
- `/en/products/483` — Strawberry Mojito Juice 1.3L — **277 words**
- `/en/awards/554` — NADEC Awarded the Social Responsibility Badge 2025 — **292 words**
- `/en/products/54` — Tenderloin Steak — **296 words**
- `/en/products/484` — Strawberry Mojito Juice 180ml — **277 words**
- `/en/products/271` — Cooking Cream 1L — **273 words**
- `/index.php/en/social-media` — **260 words**
- `/index.php/en/branches` — **254 words**
- `/en/products/284` — Pineapple with Mix Fruit Nectar 1.3L — **289 words**

### Near-duplicate content — 10 pairs, ≥ the ones the summary explicitly names
Report states: *"Pages with highly similar body content: `/index.php/en/meat` = `/en/meat` (100%); `/index.php/en/about` = `/en/about` (100%); `/index.php/en/feed` = `/index.php/en/feed` (100%) (+7 more)."* The third pair as displayed in the PDF appears to be a rendering/extraction artifact (both sides show the same URL) — based on the page-by-page confirmation above, the actual third pair is almost certainly **`/en/feed` = `/index.php/en/feed`**, consistent with the same legacy-vs-clean-URL pattern as the other two named pairs and with the duplicate-title finding for the same two URLs. The remaining 7 pairs are not enumerated in the report; given the pattern, they are very likely the same `/index.php/en/X` vs `/en/X` duplication for other page types (e.g., `/juice`), but this could not be independently confirmed for all 10 from the crawl data available (only one clean-URL/legacy-URL twin was captured for `/juice`; the 50-page crawl cap means not every legacy page's clean-URL twin was necessarily crawled).

### Other on-page findings
- **Text-to-HTML ratio: 7%** (fails the tool's threshold) — "the page is mostly markup with little visible text."
- **Meta keywords tag present** (deprecated): `"Nadec Dates, Nadec Annual Report, Annual Report, L..."` — exposes internal keyword targeting to competitors for no ranking benefit.
- **Open Graph tags: none found anywhere** — confirmed absent on every individual page checked in the page-by-page report (homepage, news, products, awards, about, etc.), not just the homepage.
- **Structured Data (JSON-LD): not found on any of the 50 crawled pages** — corroborates the earlier audit's sitewide finding with full-crawl confirmation rather than a spot-check.
- **Canonical URL: present and self-referencing on every page checked** — consistent pass across all 50 rows in the page-by-page report.
- **Site-wide image alt: 975/1018 (96%)** have alt attributes — strong baseline, though the tool couldn't verify alt-text *quality/descriptiveness*, only presence.

---

## 4. Technical SEO — Additional Specifics

- **XML Sitemap: exactly 37 URLs declared** (the earlier audit estimated "~40" from a manual look — this crawl-based figure of 37 is the precise number to use going forward).
- **Sitemap coverage gap: 49 of the 50 crawled pages are NOT in the sitemap.** Only the homepage itself is represented — meaning virtually the entire crawlable site (products, news, awards, corporate pages) relies solely on internal linking for discovery, not the sitemap.
- **Sitemap dead URLs: 1 of 20 sampled sitemap entries is a 404** — `/achievements` returns 404 despite being listed in `sitemap.xml`.
- **SSL certificate: valid, but expires in 39 days** (from report date) — issued by Google Trust Services, valid until **31 Aug 2026, 06:47:14 GMT**. Not urgent, but worth flagging as a renewal-monitoring item for the support/maintenance scope of the RFP.
- **SPF record: not found** for nadec.com (Medium priority — email spoofing/deliverability risk). **DMARC record: found, policy=reject** (pass) — so DMARC is configured correctly but SPF, one of its two supporting mechanisms, is missing, which weakens the DMARC protection in practice.
- **Mixed content: 1 insecure `http://` resource on 1 page (High priority).** Exact resource: `http://neew-public-website.azurewebsites.net/sites/default/files/about_bg_videos/_%D9%8B1%D9%8A%D8%A7%D9%8A%D9%88_0.mp4`, loaded on the `/en/about` page over plain HTTP despite the page itself being served over HTTPS. **This directly corroborates and sharpens the earlier audit's "split brand footprint" finding** — the Azure microsite (`neew-public-website.azurewebsites.net`) isn't just a separate, dormant property; it's actively embedded as a live video resource on the About page, and it's insecure, which is actively breaking (or triggering browser warnings on) a page real visitors see.
- **Broken images/scripts/stylesheets — 4 broken assets (High priority):**
  - `/index.php/sites/default/files/2026-04/meat.png` (404) — referenced on `/index.php/en/meat`
  - `/index.php/sites/default/files/nadec/about/vision2.png` (404) — referenced on `/index.php/en/about`
  - `/index.php/sites/default/files/nadec/about/message.jpg` (404) — referenced on `/index.php/en/about`
  - (+1 more, not individually named)
- **URL structure issues — 5/50 URLs flagged (Low priority):** `/index.php/en/ceo_speech` (underscores), `/index.php/en/Solution` (uppercase), `/index.php/en/food_culture` (underscores), plus 3 links with 4+ query parameters. Independently spotted in the page-by-page crawl but not individually named in this list: `/index.php/en/Social_responsibility` (uppercase + underscore) and `/index.php/en/community_comm` (underscore) — likely among the report's unnamed remainder of the 5, or additional instances of the same pattern.
- **Hreflang: not found** — flagged only as informational (not scored as a fail) by this tool, "relevant only for multi-language sites," but confirmed absent, consistent with the earlier audit's higher-priority framing of this as the single biggest technical gap for a bilingual brand.
- **Analytics tool detected: Google Analytics 4** — confirms GA4 is live on the site (useful cross-reference; the earlier audit did not check analytics implementation).
- **Technology stack confirmed by automated fingerprinting:** Cloudflare (web server/CDN), Drupal (CMS), Google Analytics — matches the earlier audit's manual finding exactly.
- Passing items worth noting for completeness: robots.txt accessible (200), mobile viewport present, favicon present, custom 404 page returns 404 correctly, 5/5 security headers present, HTTP→HTTPS redirect works, `nadec.com` → canonical `www.nadec.com` resolves correctly, HTML5 doctype present, no deprecated HTML tags, no plaintext emails exposed, no iframes, no Flash, 0 redirect chains.

---

## 5. Links / Backlink Profile — New Data (previously flagged as a gap in `seo-audit-findings.md`)

The earlier audit explicitly flagged off-page/backlink data as unavailable (no licensed Ahrefs/SEMrush/Moz access) and marked Section 4 "provisional." This report includes an automated backlink pull that **partially closes that gap** — treat these as directional figures from the tool's own index, not a substitute for a full Ahrefs/SEMrush comparison against Almarai, which is still recommended before final submission.

| Metric | Value |
|---|---|
| Domain Strength | 55/100 |
| Page Strength (homepage) | 55/100 |
| Total backlinks | 3,426 |
| Referring domains | 852 |
| Dofollow / Nofollow | 1,262 / 2,164 |
| EDU backlinks | 2 |
| GOV backlinks | 0 |
| Nofollow ratio (outbound, on-site) | 0% |

**Important quality caveat the raw numbers don't show on their own:**
- **Top referring-domain TLDs:** `.com` (226), `.app` (189), `.online` (84), `.xyz` (80), `.space` (60), `.website` (53), `.site` (50), `.net` (38), `.org` (24), **`.sa` (only 7)**. The heavy weighting toward `.app`/`.online`/`.xyz`/`.space`/`.website`/`.site` — TLDs commonly associated with low-quality directories and link farms rather than editorial content — combined with only 7 Saudi-domain referring links, suggests the raw 852-referring-domain count overstates the profile's real quality and local relevance.
- **Top referring-domain countries:** US (557), .co (132), Germany (28), France (25), Finland (23), UK (18), Ukraine (8), Japan (8), Italy (7), Netherlands (7) — again, a profile weighted toward generic/international sources rather than KSA/GCC-relevant domains.
- **Anchor text finding — flag this prominently:** the #2 most common anchor text pointing at nadec.com, with **257 occurrences**, is literally **"TELEGRAM@SEO_ANOMALY - SEO BACKLINKS, BLACK-LINKS, TRAFFIC BOOST, LINK IN..."** — this is a spam/black-hat SEO service's promotional anchor text, not a legitimate reference to NADEC. This is a strong signal of either negative-SEO targeting or NADEC's domain having been swept up in a low-quality link-farm network. **This was not visible in the earlier audit (no backlink tool was available then) and should be raised as a reputational/technical-SEO risk item**, worth a real Ahrefs/SEMrush disavow-file review as part of the off-page workstream.
- **Backlink concentration on a third-party microsite, not nadec.com:** among the "Top Backlinks" table, the majority of individually-listed high-strength links point to `neew-public-website.azurewebsites.net` — the same off-domain Azure microsite flagged in the earlier audit's brand-fragmentation finding and in the Mixed Content finding above — rather than to `nadec.com` itself. Example referring pages: "Product of the Year 2025" Award for Nadec Fresh Laban, Food Safety, various Arabic ESG/product pages. **This quantifies, for the first time, exactly how much off-page authority is currently accruing to the wrong domain** — a concrete, evidence-based number to cite when recommending domain consolidation.
- **Top pages by backlinks:** `https://nadec.com/` (1,582), `http://www.nadec.com/` (275), `https://www.nadec.com/ar/products/323` (238), `https://www.nadec.com/ar/documents-library?...` (185), `http://nadec.com/` (120) — note that link equity is currently split across 4+ different URL variants of essentially the same homepage (with/without www, with/without trailing content), which normally should be consolidated via canonicalization/redirects to concentrate ranking signal.
- **On-page link structure:** 2,777 internal links (56 avg/page), 519 external links, 0% nofollow, 0 broken internal links detected across the 50 crawled pages (broken *external* assets are covered separately under Section 4's "Broken images/scripts/stylesheets").

---

## 6. Social Results — New Data

| Check | Result |
|---|---|
| Facebook Open Graph tags | None found (fail) |
| Facebook Page linked | Found (pass) |
| Facebook Pixel | Not detected (fail) — "cannot track conversions or run retargeting ads" |
| X Card meta tag | Missing (warning) |
| X (Twitter) account linked | Found (pass) |
| Instagram linked | Found (pass) |
| LinkedIn Page linked | Found (pass) |
| YouTube channel linked | Found (pass) |

**Reading:** NADEC already maintains a full baseline social presence (Facebook, X, Instagram, LinkedIn, YouTube all linked from the site) — the gaps here are purely technical/implementation (no Open Graph tags for rich link previews, no Facebook Pixel for paid remarketing, no Twitter Card), not an absence of social channels. This is a low-cost, high-clarity win to bundle into the rebuild.

---

## 7. GEO Results — New Category (Generative Engine Optimization)

| Check | Result | Priority |
|---|---|---|
| Identity Schema (Organization/Person JSON-LD) | Not found | Medium |
| Detected Schema.org @type values | None | — |
| Rendered Content (LLM Readability) | **Good — 55% rendering** (pass) | — |
| /llms.txt file | Not found | Low |

**What this means:** GEO measures how discoverable and citable a site is for AI answer engines (ChatGPT, Perplexity, Google AI Overviews, etc.), which is functionally distinct from traditional search-engine SEO. NADEC scores an **F (2 failed / 1 passed)** here — the only pass is that the page's rendered content is sufficiently readable for LLMs to parse (55% rendering), but there is no machine-readable identity/entity schema and no `/llms.txt` file to guide AI crawlers on site structure and content priorities.

**Flag for the proposal (explicit connection to NADEC's own narrative):** NADEC's technical proposal already references ISO/IEC 42001 (the AI-management-system standard) as part of its own governance story. An **F-grade GEO score is a directly quantified, evidence-based gap in NADEC's AI-readiness that sits alongside that governance narrative** — recommending Organization/Person JSON-LD schema and an `/llms.txt` file isn't a generic SEO checkbox item here; it's the site-level implementation of the same "AI-ready enterprise" positioning NADEC is already using elsewhere in the RFP response, and should be framed that way rather than tucked into the low-priority tail of the SEO section. (Note: elsewhere on the site, the Arabic homepage's on-page keyword table shows the terms "iso," "iec," and "nspc" appearing in heading tags — this appears to relate to food-safety/quality ISO certifications already referenced on the site, not the AI-governance ISO/IEC 42001 standard specifically; worth confirming with NADEC which ISO standards are referenced where before overstating the connection in copy.)

---

## 8. Structural Notes on the Report Itself

- The document consists of: an executive summary/scorecard (pages 1–3), a Recommendations list (33 items, pages 2–3), six category result sections — Performance, On-Page, Technical, Links, Social, GEO (pages 4–17), a Technology fingerprint block (page 17), and then a **full page-by-page report for all 50 crawled pages** (pages 17/18–105), each following an identical per-page template: SERP snippet preview, header tag usage, keyword-consistency table, and individual checks (title, meta description, H1, content length, image alt, canonical, Open Graph, structured data, Twitter Card).
- **There is no separate keyword-ranking appendix, no separate backlink-geography appendix beyond what's summarized in the Links section, and no additional GEO deep-dive beyond the 4 checks in Section 7 above.** The document ends at page 105 with page 50 of the page-by-page report (`/index.php/en/faqs`) — there is no content after the 50th page entry.
- All 50 crawled page URLs (for reference/cross-checking against the sitemap gap finding in Section 4): `/en/news/642`, `/en/news/641`, `/en/awards/554`, `/index.php/en/ceo_speech`, `/en/products/54`, `/en/news/640`, `/en/products/271`, `/en`, `/index.php/en/about`, `/ar`, `/index.php/en/quality`, `/en/products/483`, `/en/awards/507`, `/en/products/55`, `/en/products/313`, `/en/awards/524`, `/index.php/en/Solution`, `/en/products/484`, `/index.php/en/Social_responsibility`, `/en/about`, `/en/products/284`, `/en/products/343`, `/index.php/en/documents-library`, `/en/products/312`, `/index.php/en/privacy-policy`, `/index.php/en/social-media`, `/index.php/en/branches`, `/en/documents-library`, `/index.php/en/research`, `/index.php/en/meat`, `/index.php/en/food-safety`, `/en/feed`, `/index.php/en/investors`, `/en/awards`, `/index.php/en/partnerships`, `/en/products/68`, `/en/products/310`, `/index.php/en/innovation`, `/index.php/en/juice`, `/en/juice`, `/index.php/en/board-of-directors`, `/index.php/en/milk`, `/index.php/en/food_culture`, `/en/meat`, `/en/news`, `/index.php/en/feed`, `/index.php/en/form/nadec-coop-training-request`, `/index.php/en/community_comm`, `/en/products/628`, `/index.php/en/faqs`.

---

## Recommended Next Steps to Fold Into the RFP Response

1. **Use this report's field/CrUX data (matches `pagespeed-data.md` exactly) as the headline Core Web Vitals evidence** — it's independently corroborated across two separate audit runs on the same day, which is strong evidence for the proposal. Cite lab data only to explain *why* (hero image weight, render-blocking JS, TBT) not as a second score.
2. **Add GEO as a named sixth pillar** in the SEO section of the technical proposal, explicitly tied to NADEC's ISO/IEC 42001 AI-governance narrative — this is a differentiator most competing agency bids are unlikely to include.
3. **Flag the spam anchor-text finding ("TELEGRAM@SEO_ANOMALY...", 257 occurrences) and the Azure-microsite backlink concentration as a distinct off-page risk/opportunity item** — recommend a full Ahrefs/SEMrush link-audit and disavow review as part of the off-page workstream, closing the data gap the earlier audit flagged as provisional.
4. **Use the exact 37-URL sitemap figure and the "49/50 crawled pages not in sitemap" statistic** in place of the earlier audit's "~40 URLs, materially incomplete" estimate — it's now a precise, evidence-based number.
5. **Cite the 4 confirmed duplicate-title/near-duplicate-content pairs (meat, about, feed, juice) as concrete proof of the unfinished clean-URL migration** — this is a sharper, more specific version of the earlier audit's general "non-descriptive product URLs" finding and gives the dev team an exact punch list (implement 301 redirects from `/index.php/en/X` to `/en/X` sitewide, not just for these 4 examples).
6. **Note the SSL certificate expiry (31 Aug 2026)** as a maintenance/support-scope monitoring item, not a current failure.
7. Before finalizing: confirm with NADEC which ISO standard(s) the "iso/iec/nspc" homepage content refers to, so the GEO/ISO-42001 narrative connection in Section 7 isn't overstated in client-facing copy.
