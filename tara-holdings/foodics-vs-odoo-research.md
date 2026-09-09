# Foodics vs Odoo 19/20 Enterprise POS — KSA
## Full comparison + CodeOx gap-closure plan

Prepared for: CodeOx Technologies (internal / pre-sales)
Date: 9 September 2026
Scope: Restaurant / F&B and retail POS in Saudi Arabia. Odoo Enterprise 19 (current stable) and Odoo 20 (unveiled 24–26 Sept 2026, Odoo Experience Brussels; GA expected Oct–Nov 2026). Community mentioned only for accuracy.

> Source: research shared by CodeOx developer (9 Sep 2026). For the Tara Holdings / Urban Eats lead. NOTE: this paste was truncated mid-section 6.3 (delivery plan) — request the remainder from the developer before relying on the full rollout steps.

---

## 1. Bottom line

| Question | Answer |
|---|---|
| Better restaurant POS out of the box in KSA | **Foodics** |
| Better single-stack (POS + inventory + accounting + HR + eCommerce + B2B) | **Odoo Enterprise** |
| Better for retail / mixed retail+F&B | **Odoo Enterprise** |
| One system or both for a scaled F&B group | **Both**: Foodics front-of-house + Odoo back office, connected by third-party connector |
| Can Odoo be customised to match Foodics | **Yes for all functional gaps**; no for SAMA-licensed embedded payments, aggregator API access itself, and Foodics' KSA channel/brand |
| Time to match | **~3 months MVP / 5–7 months full parity**, 1 senior dev + 1 QA, after which 15–20 %/yr upkeep |
| Worth it | Not for one client. Yes as a productised CodeOx F&B vertical amortised over 5+ clients |

---

## 2. Foodics — complete profile

### 2.1 Company (2026)
- Riyadh, founded 2014. ~US$200M raised (Prosus, Sanabil, STV, Peak XV; Kamco Invest stake 2025). Record US$170M Series C (largest MENA SaaS round).
- FY2025 GMV US$13B; 36,000–40,000+ branches (source-dependent); >30 % share of KSA restaurant-management-system market; 35+ countries; >6B orders processed lifetime.
- H1 2025: ARR +29 %, international revenue +56 %, payment volume +38 %.
- **SAMA-licensed** payment institution (Foodics Pay: acquiring, lending, 24h settlement).
- 2026: launched **Foodics Black** (full-service dine-in platform) at LEAP; acquired Greek AI firm **Norma** (now its BI/Analytics Agent); ~US$100M M&A/AI budget.

### 2.2 Product / features
| Area | Foodics |
|---|---|
| Cashier | **iPad-only** app; offline mode with sync |
| Dine-in | Floor plans, tables, waiter app, pay-at-table, QR digital menu, course/seat handling, split bill (item/amount), tips, void reasons |
| Kitchen | KDS (station routing, bump, timers), kitchen/bar printing, expo screen |
| Menu | Modifiers (min/max, forced), combos, timed events/menus, branch-level menus, allergens |
| Inventory | Recipe-level depletion, food-cost %, theoretical vs actual, waste tracking, low-stock alerts, auto-PO, inter-branch transfers with approvals, central kitchen/warehouse |
| Multi-site | Multi-branch, unified reporting, branch P&L, franchise controls |
| HR | Shifts, clock-in, GOSI-aware payroll (Advanced tier) |
| CRM/Loyalty | Loyalty, coupons, promotions, customer profiles, online ordering, self-order kiosk |
| Analytics | Dashboards; Norma AI agent |
| Payments | Foodics Pay (Mada, STC Pay, cards, Apple Pay) native; SAMA-regulated |
| Compliance | ZATCA Phase 2 built in — **B2C simplified invoices only**; B2B standard invoices need add-on (e.g. InvoiceQ). Arabic/RTL, SAR, Hijri, VAT 15 % |
| Aggregators | Jahez native; HungerStation, Keeta, Marsool, ToYou, Careem, Noon Food via Marketplace/middleware (FeedUs, Deliverect, Urbanpiper, Grabtech, Blend) with auto stock depletion |
| Integrations | App Marketplace 100+ (accounting/ERP incl. Odoo via PlusTech, SAP; HR; marketing) |
| Hosting | Foodics cloud, in-Kingdom (PDPL-aligned) |

### 2.3 API
- REST, OAuth 2.0 authorisation-code (scopes e.g. `general.read`), `/whoami` for business mapping.
- Per-action rate limiting: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`, HTTP 429.
- Webhooks; sandbox; customers paginated 50/page.
- API access gated to **Advanced tier or purchased API licence** (verify at scoping). Token validity ~14 days per community sources (unverified officially).

### 2.4 Pricing (SAR, published Sept 2026, monthly billing; annual in brackets)
| Bundle | Tier | SAR/mo |
|---|---|---|
| QSR & Cafés | Starter | 423 (392) |
| | Basic | 801 (742) |
| | Advanced | 1,224 (1,133) |
| Cloud Kitchen | Basic | 612 (567) |
| | Advanced | 936 (867) |
| Dine-In | Basic | 1,183 (1,096) |
- API only in Advanced/Dine-In. Delivery integrations ~SAR 200–400/mo per platform. HR/payroll only on Advanced. 3-terminal Advanced setups quoted ~SAR 3,399/mo. Enterprise deals ~15–20 % below list. Hardware separate: iPad from SAR 1,499; full station SAR 3,500+.
- Older/promo per-outlet figures (199/375/417 + 1,500 implementation) still circulate — use official page.

### 2.5 Pros
- Purpose-built restaurant OS; KSA market leader; deep F&B UX.
- ZATCA B2C native, no plugins.
- Native aggregator ecosystem with stock depletion.
- SAMA-licensed embedded payments + lending.
- Recipe/food-cost/waste, central kitchen, franchise, GOSI payroll.
- Huge KSA hardware/support/reseller channel; Arabic-first.
- In-Kingdom hosting.

### 2.6 Cons
- iPad-only (Apple hardware lock-in).
- Not an ERP: no GL depth, weak procurement outside F&B, no manufacturing beyond recipes; groups still need an ERP for consolidation.
- B2B standard e-invoice needs add-on.
- Cost scales fast with branches, aggregator connectors, payroll.
- API behind top tier / paid licence.
- Online ordering/delivery analytics bolted-on vs dine-in core.
- SaaS lock-in; migration = re-platform.

---

## 3. Odoo Enterprise 19 / 20 — complete profile

### 3.1 Version status
- **Odoo 19**: released Sept/Oct 2025. Rolling point releases 19.1 (Jan 26), 19.2 (Mar), 19.3 (May), 19.4 (Jul 26). PostgreSQL 16+. Current stable.
- **Odoo 20**: unveiled 24 Sept 2026 keynote, Odoo Experience Brussels. GA typically 2–4 weeks later; first solid patch Oct–Nov 2026. Even-numbered = LTS (target for 3–5 yr migrations).
  - **Roadmap (unconfirmed until release notes)**: embedded/agentic AI across accounting, website, helpdesk, POS; **browser-based POS hardware discovery with auto-combos**; AI accounting audit; new payroll dashboard; read-replica DB architecture; purpose-built mobile UI. Odoo itself labels the roadmap "things we will maybe do". No KSA-specific changes announced.
- Odoo revenue ~€619M in 2025.

### 3.2 KSA localisation (Community and Enterprise both ship it)
- `l10n_sa` (CoA, VAT 15 %), `l10n_sa_edi` (ZATCA Phase 2: UBL 2.1 XML, ECDSA cryptographic stamp, CSID onboarding via OTP from Fatoora portal, UUID/ICV/PIH hash chain, TLV QR, B2B clearance + B2C reporting), `l10n_sa_edi_pos` (POS simplified invoices), `l10n_sa_pos` (GCC receipt), Arabic invoice templates. In community codebase since v16.
- Enterprise adds: official Odoo SA support for the localisation, GOSI/WPS payroll, Studio, one-click upgrades, Odoo.sh.
- Current ZATCA wave: **Wave 24** (revenue > SAR 375k), deadline 30 Jun 2026 — integration is now near-universal for VAT-registered SMEs. ZATCA's provider directory is indicative, not certification; liability stays with the taxpayer.

### 3.3 POS features (Odoo 19 Enterprise)
| Area | Odoo 19 |
|---|---|
| Hardware | Browser-based: iPad/Safari, Android/Chrome, Windows, Mac. IoT Box for printers, scales, scanners, cash drawers, customer display. No vendor lock-in |
| Dine-in | Visual floor plans, table transfer/merge, course firing, split bill by item/amount, tips, presets (eat-in/takeaway/delivery with fiscal position, pricelist, prep capacity), table-booking waiting list (Kanban) |
| Kitchen | `pos_preparation_display` KDS, kitchen/bar printing, self-order notes to KDS, snooze/unavailable items |
| Menu | Product combos, modifiers via attributes/variants, free QR digital menu (allergens, combos, online pay), self-order kiosk, unified UoM/packaging, expired-product warning |
| Inventory | Multi-warehouse, MRP BOM per menu item, consume-on-sale, central kitchen via inter-warehouse routes, expiry tracking |
| Multi-site | Multi-company, multi-branch, franchise (central catalogue, analytic accounts per branch, consolidated reporting) |
| HR | Attendance/clock-in, planning/shifts, Payroll with GOSI/WPS (Enterprise) |
| Loyalty | Loyalty programs, gift cards, eWallet, promotions, coupons — shared with eCommerce |
| Offline | Offline mode with auto-sync (hardening still needed; see gaps) |
| UI | Dark mode, redesigned shop floor, quick payment buttons, minimal-rights profiles for temp staff, Arabic/RTL |
| Compliance | ZATCA Phase 2 B2B **and** B2C; SAR; Hijri via config |
| Payments | Native providers exclude Mada acquiring — KSA gateways via Apps Store (Moyasar, Tap, HyperPay, PayTabs, Geidea terminals via connector) |
| Aggregators | None native. Third-party: `mn_food_aggregator_pos` (§5), middleware (FeedUs/Deliverect/Grabtech) |
| eCommerce | Same DB as Website/eCommerce; Odoo 19 added abandoned-cart emails, click & collect with per-location stock, AI recommendations, comparison/wishlist, Google Merchant, social commerce |

### 3.4 Pricing (Middle East pricelist, incl. KSA — cheapest global list)
- **Standard US$8.95/user/mo**, **Custom US$13.60/user/mo**, billed yearly. Custom = Studio, multi-company, external API, Odoo.sh/on-prem.
- One-App-Free: $0, one app, unlimited users.
- Odoo.sh: ~$57.60/worker + $0.20/GB + $14.40/staging on top.
- Community: $0 licence, self-hosted.
- No per-branch/terminal fee → cost favours Odoo as branch count rises, disfavours as user count rises.
- No Odoo 20 pricing change confirmed.
- **Deployment constraint**: Odoo Online (SaaS) blocks third-party modules → any KSA gateway/aggregator/Foodics connector requires **Odoo.sh or on-premise**. PDPL/SDAIA cross-border rules also push regulated clients to in-Kingdom hosting.

### 3.5 Pros
- POS inside the ERP: one data model for POS, eCommerce, inventory, accounting, purchase, MRP, HR, B2B.
- Hardware-agnostic; no iPad lock-in.
- ZATCA B2B + B2C; Arabic/RTL; GOSI/WPS payroll.
- Real BOM/MRP → true food cost; deep multi-warehouse; multi-company consolidation native.
- Loyalty/gift cards/promotions shared across channels.
- Data ownership, full exportability, in-Kingdom hosting possible.
- Very low licence cost in KSA; Studio for low-code changes.

### 3.6 Cons (vs Foodics)
- No native KSA aggregator connectors; aggregator API access must be obtained per platform.
- No native Mada acquiring / SAMA-licensed embedded payments.
- Restaurant UX and KDS depth behind Foodics; documented 18.x offline order-loss and KDS double-order bugs.
- Food-cost/waste analytics need configuration + custom reports.
- Thin KSA F&B hardware/support channel; restaurant owners don't know the brand.
- Implementation-heavy; needs partner; Odoo.sh/on-prem required for connectors.
- Odoo 20 will break OWL-based POS customisations → re-port cost.

---

## 4. Side-by-side

| Criterion | Foodics | Odoo 19 Ent. |
|---|---|---|
| Hardware | iPad only | Any browser device + IoT Box |
| KDS | Mature, station routing | Basic, needs extension |
| Modifiers/combos | Deep | Native, less polished |
| Recipe / food cost / waste | Native, turnkey | Native via MRP, needs setup + reports |
| Aggregators | Native / marketplace | Third-party module / middleware |
| Mada payments | Native (Foodics Pay, SAMA) | Third-party terminal connector |
| ZATCA | B2C native; B2B add-on | B2B + B2C native |
| Multi-branch | Yes | Yes |
| Central kitchen | Yes | Yes (MRP + routes) |
| Franchise | Yes | Yes (multi-company) |
| HR / GOSI | Advanced tier | Enterprise payroll |
| Accounting / GL | No (export to ERP) | Full |
| Procurement / MRP | Recipes only | Full |
| eCommerce / B2B | Online ordering only | Full |
| Offline | Solid | Works; hardening advised |
| Data ownership | Foodics cloud | Own it (Odoo.sh/on-prem) |
| Hosting/PDPL | In-Kingdom | Choose in-Kingdom |
| Licence (10 users, 3 branches) | ~SAR 1,100–3,400/mo | ~SAR 500/mo + hosting |
| Implementation | Days–weeks, turnkey | Weeks–months, partner |
| Local F&B support | Excellent | Thin |

---

## 5. Connectors

### 5.1 Foodics ↔ Odoo (no first-party connector exists)
| Connector | Odoo versions | Price | Notes |
|---|---|---|---|
| Warlock `wt_foodic` | 12.0–19.0 | ~$297–330 one-time, perpetual | Branches, products/variants, customers, POS orders, invoices, sessions, categories, vendors, POs, payment methods. No ratings |
| Div Systems `div_foodics_with_webhook` | 16.0–18.0 only | ~$318 one-time | Adds order webhook, ingredients-as-BOM, combos, analytic account per branch, inventory transfers, visual reports |
| PlusTech (Foodics Marketplace) | not published | Quote-based, managed | Imports branches, devices, users, payment methods, categories, products, modifiers, combos, taxes; item mapping before order sync |
| `qs_foodics_odoo_integration` | 16.0 | unconfirmed | |
- **None supports 20.0 yet.** Expect 1–3 month lag after GA.

### 5.2 Aggregators → Odoo POS: `mn_food_aggregator_pos` (Moaz Nabil)
- v17/18/19, $1,000 one-time, OPL-1, 2,111 LOC, zero reviews, solo KSA developer.
- Delivers: per-platform webhook endpoint (`/aggregator/<platform>/webhook`), HMAC-SHA256 verification, webhook log, idempotency on (platform + order ref), store_id → POS mapping, SKU mapping (AR/EN), auto-accept rules, state machine received→accepted→preparing→ready→picked-up→delivered→settled with outbound status push, reject with reason, driver info, rush-hour pause, cashier floating panel (6 s polling, sound alert), CSV settlement reconciliation with balanced commission journal entries, GMV/commission/net dashboard, ZATCA e-invoice on close, two security groups, sandbox flag, 60-day log purge.
- Auth schemes: API key + secret (Jahez), OAuth 2.0 (HungerStation/Delivery Hero), partner creds (Keeta), signed webhook.
- **Limits**: payload field names are mapped at install against each platform's live spec (i.e. generic framework, not validated adapters); status-push target URLs unspecified; no outbound menu publishing; Marsool unconfirmed; "Odoo Online" availability is author-declared — reality is Odoo.sh/on-prem; OPL-1 means one licence per client, cannot be bundled into a CodeOx product.
- Where to get API access (from the listing): Jahez — integration@jahez.net + integration-portal.jahez.net; HungerStation — Partner/POS API via account manager, developer.hungerstation.com / developers.deliveryhero.com/documentation/pos.html; Keeta — merchant.mykeeta.com, developers.mykeeta.com, api-docs.mykeeta.com; Marsool — merchant support, no public portal.
- Verdict: buy one licence for pilot; saves 4–6 weeks of framework work; decide within 2 weeks whether to keep or re-implement as `cdx_pos_aggregator` under CodeOx licence.

### 5.3 KSA payment / terminal modules for Odoo
- Gateways: Moyasar (SAR/Mada/Apple Pay), Tap, HyperPay, PayTabs — Apps Store, ~SAR 50–1,500/app/yr; verify 19.0 builds.
- Terminals: Geidea / NearPay / Verifone ECR via IoT Box or TCP/HTTP — custom or third-party.
- Mada = >90 % of KSA cards, >95 % of card transactions; Stripe unusable for KSA-resident merchants.

---

## 6. How much of Foodics we can match in Odoo — and how

### 6.1 Gap-by-gap
| # | Foodics capability | Odoo 19 status | Achievable | How (module / approach) | Effort |
|---|---|---|---|---|---|
| 1 | Aggregator order intake (Jahez, HungerStation, Keeta, Marsool, ToYou) | Absent | Yes, gated by API access | Buy `mn_food_aggregator_pos` or middleware (FeedUs/Deliverect/Grabtech); build per-platform adapters + status push URLs + outbound menu publish; sandbox certify each | Framework: 0 (buy) / 4 wks build. Adapters: 1–2 wks each with module, 2–3 wks without. Middleware route: 3–4 wks total |
| 2 | Recipe-level food cost, theoretical vs actual, waste | Native MRP, no F&B reports | Yes | `cdx_pos_fnb_foodcost`: BOM per menu item, consume-on-session-close, waste reason codes on `stock.scrap`, variance report, food-cost % per branch/day | 3–4 wks |
| 3 | Restaurant UX (forced modifiers min/max, seat-level ordering, void reasons, tips, hold/fire) | Partial | Yes | `cdx_pos_fnb_ui`: OWL POS screens, modifier groups model, seat numbers on orderlines, void reason wizard, tip screen | 4–6 wks |
| 4 | KDS maturity (station routing, prep timers, colour ageing, recall, expo view, bump bar) | Basic | Yes | Extend `pos_preparation_display`: routing rules by category/branch, timer thresholds, expo aggregate view, keyboard bump | 3–4 wks |
| 5 | Offline robustness | Works, known bugs | Partially | Local order queue hardening, idempotent order keys, reconciliation cron, session close guards; track upstream 19.x fixes | 2 wks + ongoing |
| 6 | Mada terminal pairing | Absent | Yes | Geidea/NearPay ECR integration via IoT Box or direct; payment method type per terminal | 2–3 wks per vendor |
| 7 | Multi-branch dashboards, branch P&L | Native | Yes | Analytic accounts per branch, dashboard/spreadsheet templates | 1–2 wks |
| 8 | Central kitchen, inter-branch transfers with approval | Native + light | Yes | Multi-warehouse routes, MRP, approval on `stock.picking` | 1–2 wks |
| 9 | Franchise / central menu control / royalties | Yes | Yes | Multi-company, product-template governance, royalty computation, restricted menu editing | 2–3 wks |
| 10 | Self-order kiosk, QR menu, waiter app | Native 19 | Yes | Config + branding | 1 wk |
| 11 | Clock-in, shifts, GOSI payroll | Native Ent. | Yes | Config | 1 wk |
| 12 | Loyalty, gift cards, promos, timed menus | Native | Yes | Config; timed promos small extension | 1 wk |
| 13 | Embedded SAMA-licensed payments / lending | — | **No** | Regulatory; partner with Geidea/Moyasar/Tap instead | — |
| 14 | Aggregator API access | — | **No (not ours to build)** | Onboard CodeOx as approved POS partner with each aggregator; run in parallel from day 1 | Weeks–months, external |
| 15 | KSA F&B hardware/support channel, brand trust | — | **No (commercial)** | Partner with a KSA hardware reseller; reference clients | — |

### 6.2 Timeline
| Package | Includes | Duration | Team | Indicative cost |
|---|---|---|---|---|
| **MVP "Foodics-equivalent"** | #1 via purchased module or middleware (3 platforms), #2, #3, #4, #6 (one terminal), #7–#12 config | **~3 months** | 1 senior Odoo dev + 1 QA | SAR 150–250k |
| **Full parity** | + direct adapters for 3 aggregators, 2+ terminal vendors, #5 hardening, #9 franchise | **5–7 months** | same | SAR 300–450k |
| **Upkeep** | Aggregator API changes, ZATCA updates, Odoo 20 re-port | 15–20 % of build/yr | | |

Critical path is #14 (aggregator onboarding), not development. Start requests before purchase.

### 6.3 Delivery plan
1. **Week 0**: file aggregator POS-partner requests (Jahez, HungerStation/DH, Keeta); buy one `mn_...`

> ⚠️ TRUNCATED HERE — the shared paste ended mid-sentence at section 6.3 step 1. Get the rest of the delivery plan from the developer.
