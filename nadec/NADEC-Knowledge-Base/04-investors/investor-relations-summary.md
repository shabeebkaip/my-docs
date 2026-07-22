# NADEC — Investor Relations Summary

Source pages: `/en/investors`, `/en/documents-library` (all filtered views), `/en/faqs`
Full document catalog: `12-json-data/documents.json` (34 documents cataloged with title/category/date/URL)

## Structural note
Per `website-audit-findings.md` Finding 5.3 and `competitor-benchmark.md` Section 3, NADEC's IR content is **integrated into the main site navigation** (an "Investors" top-level menu item), not siloed to a separate subdomain — this matches the Baladna best-practice pattern and is explicitly better than SADAFCO's siloed-subdomain approach. The content itself is current and well-maintained; the visual/template execution is dated (same theme as the rest of the site).

## Key governance/ownership fact (net-new, found via `/en/faqs`)
- **SALIC (Saudi Agricultural and Livestock Investment Company) owns 38.648% of NADEC's shares.** This is the single most important shareholding-structure fact found in this crawl and was not present in the prior UX/SEO audit passes.
- Financial statements are issued annually as of 31 December.
- NADEC is confirmed as "the first agricultural joint-stock company" in the Saudi capital market (founded via the 1981 Royal Decree converting Haradh Agricultural and Animal Production Company).

## Annual Reports (3 years available)
| Year | Uploaded | 
|---|---|
| 2025 | 2026-03 |
| 2024 | 2025-03 |
| 2023 | 2024-07 |

## Quarterly/Annual Earnings Presentations (10 documents, 2021-2026)
FY2025, Q3 2025, Q2 2025, Q1 2025, FY2024, Q3 2024, Q1 2024, FY2023, FY2022, Q2 2021 — a genuinely continuous quarterly disclosure cadence from 2021 through the most recent quarter, current as of this crawl (FY2025 earnings dated 2026-02).

## ESG / Sustainability Reporting (5 documents)
- Sustainability & ESG Report 2024 (2025-09) and 2023 (2024-12)
- Three ESG Position Statements (2026-04): Product Quality and Safety, Environmental, Animal Welfare — all very recently published, suggesting an active ESG-formalization push in 2026.

## Corporate Governance Documents (16 documents)
Board Charter, Corporate Governance Charter, Audit Committee Charter, Nomination & Remuneration Committee Charter, Executive Committee Charter, Remuneration Policy, Whistleblowing Policy, Disclosure and Transparency Policy, Conflicts of Interest Policy, Code of Conduct Policy, Business Competition Standards Policy, Board Nomination and Selection Policy, Articles of Association/Bylaws, Dividend Distribution Policy, Social Responsibility Policy. Most dated 2026-02 through 2026-05 — indicates a comprehensive governance-documentation refresh happened in early-to-mid 2026, likely tied to a Tadawul/CMA compliance cycle or annual governance review.

## Partnerships/Supplier Relations
`/en/partnerships` describes a general framework (contractors, consultants, suppliers, manufacturers) rather than naming specific investor-facing partners, and links to an Ariba-based supplier self-registration portal (`nadec.sourcing.ksaprv.cloud.ariba.com`) — a genuine B2B procurement system, not a marketing page.

## External/Off-Domain Annual Reports Property
The "Annual Reports" nav item under Investors links externally to `https://nadec-landing.cfapps.eu10-004.hana.ondemand.com/en` — an SAP HANA Cloud-hosted property outside the primary `nadec.com` domain. This duplicates/complements the on-domain documents library and was flagged previously in seo-audit-findings.md Section 1 ("brand footprint split across multiple domains") — confirmed again in this crawl as a live, in-use nav link, not a legacy artifact.

## Financial KPIs directly stated on-site
- 200+ dairy, beverage, and agricultural products in portfolio (per `/en/investors`)
- 40+ years operational experience
- No revenue, profit, EPS, or dividend-per-share figures were found in on-page text (these live inside the PDF annual reports/earnings presentations, catalogued as metadata only per crawl scope — not parsed in this pass)

## Not Publicly Available
- Exact revenue/profit/EPS figures (inside PDFs, not extracted)
- Full shareholder register beyond the SALIC 38.648% figure
- Dividend history/amounts (Dividend Distribution Policy exists as a document but figures not extracted)
