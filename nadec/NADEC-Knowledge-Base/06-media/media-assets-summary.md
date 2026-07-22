# NADEC — Media Assets Summary

This folder catalogs media asset URLs and alt-text patterns discovered during the crawl (per mission scope: image/video URLs and alt text captured as metadata, binaries not downloaded/re-hosted).

## Image hosting pattern
All product, leadership, award, and news images are served from Drupal's managed file system under `/sites/default/files/`, with responsive "image styles" subpaths, e.g.:
- Product thumbnails: `/sites/default/files/styles/item_sm/public/{yyyy-mm}/{filename}`
- Product detail hero: `/sites/default/files/styles/product_detail_style/public/{yyyy-mm}/{filename}`
- Leadership photos: `/sites/default/files/styles/members_card/public/{yyyy-mm}/{filename}` (board) and `/sites/default/files/styles/member_lg/public/{yyyy-mm}/{filename}` (CEO)
- Awards/certificates: `/sites/default/files/styles/media_style/public/{yyyy-mm}/{filename}` and `/sites/default/files/styles/medium/public/{yyyy-mm}/{filename}`

This confirms Drupal's image style pipeline is actively used for responsive cropping (per website-audit-findings.md Finding 2.3), though not yet for format conversion (no WebP/AVIF variants found).

## File naming quality observations
- Many product images retain literal Arabic filenames (URL-encoded), e.g. `%D9%84%D8%AD%D9%85%20%D8%A7%D9%84%D8%B8%D9%87%D8%B1_1.png` (meat products) — functional but not SEO-friendly (no descriptive English alt-equivalent filename), and not ideal for CDN caching/readability.
- Some filenames carry internal production artifacts, e.g. "Eyad" (apparent photographer/designer initials) appended to dozens of dairy product filenames — cosmetic but indicates raw production files were uploaded without a file-naming convention pass.
- Leadership photos show inconsistent source quality: some are professionally cropped/background-removed (`-removebg-preview.png` suffix on Board photos), others are plain phone-camera-style crops (e.g., VP photos using original camera filenames like `IMG_4854.JPEG`, `9.jpeg`).

## Video content
No embedded video players or video file URLs were found on any crawled page (homepage, news, about, products). The `/en/news/604` article title references "a film documenting the journey of agriculture and food in the Kingdom" (Founding Day content) but the film itself was not verified as embedded/playable on the article page in this pass.

## Animated GIFs (carried over from website-audit-findings.md, confirmed relevant to Media asset strategy)
Three animated GIFs power the homepage statistics/counter section (`truk.gif`, `+ 1.5.gif`, `+ 20000.gif`), totaling ~2.9MB — the single largest fixable asset-weight issue on the site (Finding 2.2). Relevant to any redesign's media-asset strategy: these should become the model case for "replace legacy heavy media with lightweight code-driven equivalents."

## Not Publicly Available
- A dedicated media/press-kit download page (logos, brand guidelines, high-res photography for press use) was not found anywhere in the crawled navigation or footer.
