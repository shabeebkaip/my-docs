# NADEC PageSpeed Insights — Raw Data

URL tested: https://www.nadec.com/en
Report timestamp: 22 Jul 2026, 13:24:12
Source: PageSpeed Insights (real user Chrome UX Report data, latest 28-day period)

## Mobile
- Core Web Vitals assessment: **Failed**
- LCP (Largest Contentful Paint): 4.8s — FAIL (red)
- INP (Interaction to Next Paint): 142ms — PASS (green)
- CLS (Cumulative Layout Shift): 0.02 — PASS (green)
- FCP (First Contentful Paint): 3s — needs improvement (orange)
- TTFB (Time to First Byte): 1.7s — FAIL (red)
- Lighthouse scores: Performance 44, Accessibility 77, Best Practices 96, SEO 92

## Desktop
- Core Web Vitals assessment: **Failed**
- LCP: 3.6s — needs improvement (orange)
- INP: 47ms — PASS (green)
- CLS: 0.62 — FAIL (red) — significant layout shift issue
- FCP: 2.2s — needs improvement (orange)
- TTFB: 1.2s — FAIL (red)
- Lighthouse scores: Performance 67, Accessibility 85, Best Practices 96, SEO 92

## Notes for proposal
- TTFB failing on both mobile+desktop points to server/hosting/backend response time issue — relevant to "front-end and back-end development" RFP item, not just SEO.
- Mobile LCP 4.8s is the single worst metric — mobile performance is the weak point (mobile Perf score 44 vs desktop 67).
- Desktop CLS 0.62 is a real red flag — likely late-loading images/ads/fonts shifting layout — worth a design/dev fix commitment in technical proposal.
- SEO Lighthouse score already 92 (decent baseline) — differentiator should be Core Web Vitals/performance remediation + technical/off-page/local SEO, not basic on-page fixes.
