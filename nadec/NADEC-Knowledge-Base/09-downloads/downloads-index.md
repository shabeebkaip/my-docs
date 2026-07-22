# NADEC — Document Downloads Index

Full machine-readable catalog: `12-json-data/documents.json` (34 documents)

This folder catalogs metadata only (title, category, date, description, download URL, suggested local filename) per crawl scope — PDF binaries were not downloaded/re-hosted.

## By category
- **Annual Reports:** 3 (2023, 2024, 2025)
- **Financial Reports and Investor Presentations:** 10 (quarterly/annual earnings, 2021-2026)
- **ESG Reports:** 2 (2023, 2024 Sustainability & ESG Reports)
- **ESG Position Statements:** 3 (Product Quality & Safety, Environmental, Animal Welfare — all dated 2026-04)
- **Corporate Governance:** 16 (charters, policies — see `04-investors/investor-relations-summary.md` for full list)

## Access pattern
All documents are hosted on-domain at `nadec.com/sites/default/files/{yyyy-mm}/{filename}.pdf` — this is a good sign for URL stability during a CMS migration (per website-audit-findings.md Finding 5.3, these are exactly the kind of direct-linked PDF URLs financial analysts bookmark, and preserving them with redirects during any rebuild is a stated priority).

## Suggested local filename convention (applied in documents.json)
`nadec-{category-abbreviation}-{descriptive-slug}-{year-or-period}.pdf`, e.g. `nadec-annual-report-2025-en.pdf`, `nadec-gov-board-charter.pdf`, `nadec-earnings-q3-2025.pdf`

## Not cataloged in this pass
- Documents Library pagination beyond page 3 of 4 was substantially covered (governance + ESG + financial categories all represented), but the filter-view URLs (`?field_tags_target_id=131` for ESG Reports, `=134` for ESG Position Statements) were not each independently re-crawled beyond what surfaced in the general listing — no evidence of hidden documents exclusive to those filtered views based on category cross-referencing done.
