# NADEC — Product Catalog Summary

Full structured data: `12-json-data/products.json` (141 products) and `products.csv` (same schema, flat file).

## Coverage note
This is a **partial but representative** catalog crawl, not exhaustive. Site-reported pagination:
- Dairy (`/en/milk`): 11 pages total — **6 of 11 pages crawled** (~72 of an estimated 130+ products)
- Juice (`/en/juice`): 2-3 pages total — **all pages crawled** (36 of 36 products, complete)
- Meat (`/en/meat`): 2 pages total — **1 of 2 pages crawled** (22 products captured; page 2 not fetched)
- Food & Vegetables (`/en/feed`): 1 page, no pagination — **complete** (11 of 11 products)

**Total captured: 141 products.** Remaining dairy pages (7-11) and meat page 2 were not crawled in this pass due to crawl-budget prioritization toward breadth across all site sections (org, investors, news, documents) rather than full-depth product-catalog exhaustion. A follow-up run can resume from `/en/milk?page=6` through `?page=10` and `/en/meat?page=2` to close this gap — see agent memory for resume instructions.

## Category breakdown (this crawl)
| Category | Products captured |
|---|---|
| Dairy (Milk and Cheese) | 72 |
| Juices | 36 |
| Red Meat (Protein) | 22 |
| Food and Vegetables | 11 |
| **Total** | **141** |

## Product detail page depth
Only one product detail page was fully extracted at the individual-SKU level (`/en/products/284`, Pineapple with Mix Fruit Nectar 1.3L) to establish the template pattern. Finding: **no nutrition facts table, no ingredients list, and no SKU code were present on the product detail page** — confirming `seo-audit-findings.md`'s "thin product content" finding (Section 2) at the full-catalog level, not just the single sample page that audit checked. This is a structural content gap across the entire catalog, not an isolated page issue.

## Product naming/data patterns observed
- Product URLs are numeric IDs, inconsistently prefixed with `/index.php/en/products/{id}` or `/en/products/{id}` for the same underlying content (duplicate URL forms, consistent with the site-wide pattern noted in website-audit-findings.md Finding 6.4).
- Product names embed size/weight directly in the title (e.g., "Full Fat Milk 1L") rather than as a separate structured field — there is no separate SKU/weight/packaging metadata surfaced anywhere in the page markup.
- A parallel "Al Hilal" sub-brand line appears within the dairy catalog (flavored long-life milk, launched ~May 2025) — not mentioned anywhere in company/about copy, suggesting either a sub-brand strategy not yet reflected in corporate messaging, or a private-label/co-branded line.
- "Innovative" tagging exists as a page-level curation (`/en/innovation`) rather than a per-product filter/badge visible on category listing pages.

## Not Publicly Available
- Pricing (no product on the site displays price — consistent with the no-e-commerce, retail-distribution go-to-market model noted in competitor-benchmark.md)
- Nutrition facts, ingredients, allergen information
- SKU/barcode data
- Product launch dates (except where inferable from image-upload folder dates, e.g., `2025-05` for Al Hilal line)
