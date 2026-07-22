# NADEC — Contact & Branches

Source: `/en/contact-us`, `/en/branches`
Full structured data: `12-json-data/contacts.json`, `12-json-data/branches.json`

## Contact Channels
- **Customer service:** +966 11 202 7777
- **Toll-free:** 800 124 1199
- **General email:** info@nadec.com.sa
- **Contact form** (`/en/contact-us`): Your Name, Your Email, Communication Number, Subject, Message, CAPTCHA — per `website-audit-findings.md` Finding 4.5, this form is well-built accessibility-wise (proper label associations, aria-required).
- **Whistleblowing portal:** external EthicsPoint instance (`secure.ethicspoint.eu/domain/media/en/gui/114655/index.html`) — a genuine, properly outsourced whistleblowing channel, a positive governance signal.
- **Supplier registration:** external Ariba portal (`nadec.sourcing.ksaprv.cloud.ariba.com`)
- **Careers:** routes through jobs2web.com ATS via an unbranded Microsoft Safelinks-wrapped URL that exposes an internal staff email (`em.ishaq@nadec.com.sa`) in plain page-source text — flagged previously in website-audit-findings.md Finding 5.5, confirmed still present in this crawl.

## Branches
The `/en/branches` page (labeled "Head Quarter" in nav) is built around an **interactive map/locator widget**, which is JS-rendered and did not return individual branch records via static page-text extraction. Only the general administration/HQ entry was extractable as text:
- **General Administration:** Riyadh, Saudi Arabia. Phone 011 202 7777 / 800 124 1199. Hours 9:00 AM–5:00 PM.

**Crawl limitation:** Given NADEC's stated scale (six dairy farms, two plants, a nationwide distribution network feeding 38,000+ outlets), the live site almost certainly has more branch/location records loaded into the map widget than were extractable via WebFetch's static HTML rendering. This is the one clearly JS-rendered section encountered in this crawl (see workaround note below) — a headless-browser pass (Playwright/Chrome DevTools) would be needed to enumerate the full branch list, which was outside this pass's tool allocation.

## Workaround attempted
WebFetch (HTML→markdown conversion) does not execute client-side JS map/locator widgets. No headless browser session was used for this specific page in this pass. Recommendation for a follow-up run: use the Playwright or Chrome-in-browser tools to load `/en/branches`, wait for the map widget to populate, and extract branch markers/list-view data directly from the rendered DOM.

## Not Publicly Available
- Individual branch addresses, cities, GPS coordinates beyond HQ
- Branch-level services or phone numbers
- Farm/plant physical addresses (only project names and regions — Hail, Wadi Al-Dawasir, Haradh, Al-Jouf — are named, not street addresses)
