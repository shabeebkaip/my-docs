# Al Saber Cars — Premium Mobile App Business Case

**Prepared by:** Code-OX (code-ox.com) · Head of Operations, Shabeeb K
**Contact:** shabeeb.k@code-ox.com · +966 53 571 6437
**Date:** 11 July 2026
**For:** Al Saber Cars Co. — alsabercars.com

> This document builds on Code-OX's delivered website audit of alsabercars.com (46/100, Grade F, 8–9 July 2026). All performance figures cited from the audit are Google-measured, not estimated. All market figures are sourced and linked. Every financial projection is explicitly labelled **[ESTIMATE]** or **[ASSUMPTION]** — Al Saber's own sales figures were not available at the time of writing, so the model is built to be re-run with real numbers the moment the client shares them.

---

## 1. The market Al Saber is competing in

Saudi Arabia's automotive retail market is large, growing, and moving online faster than the average dealer's website can keep up with. The relevant, sourced numbers:

| Metric | Figure | Source |
|---|---|---|
| New vehicle sales, KSA, 2025 | 856,000–914,000 units | Halacarly / Focus2move |
| Total new-car market value, 2025 | **SAR 122.8 billion** (avg SAR 134,300/vehicle) | Halacarly |
| Used-car market value, 2026 | **USD 7.45 bn (~SAR 27.9 bn)**, growing 8.58% CAGR to 2031 | Mordor Intelligence |
| Luxury-car market value, 2024→2033 | USD 4.2 bn → USD 6.8 bn (5.04% CAGR) | IMARC Group |
| Smartphone penetration, KSA | **98%**; internet 99% | Saudi Market Research |
| E-commerce user penetration, 2026 | **57.4%**, rising to 65.1% by 2030 | Statista |
| E-commerce market, 2026 | USD 31.29 bn, 11.92% CAGR | Mordor Intelligence |

Al Saber sits across two of these markets at once: it carries **luxury stock** (Ferrari, Rolls-Royce, Porsche, Mercedes G63 — the audit confirmed a live G63 listed at SAR 465,000) and **volume/economy stock** (MG, Hyundai Elantra). That breadth is the business's genuine strength — but it is also why a generic template site hurts it: the same page has to make a Rolls-Royce buyer feel premium *and* convert a first-car Elantra buyer on a finance plan. One brochure site cannot do both jobs well; a well-structured app can.

**Where Al Saber plausibly sits [ASSUMPTION — to be confirmed with client]:** a multi-brand independent dealer with an 782-car live inventory (the exact count the audit found in the purchase-form dropdown). If Al Saber moves on the order of **50–150 cars per month** at a blended average price of ~SAR 130,000 (in line with the national SAR 134,300 average, skewed up by the luxury tail), that implies annual revenue in the range of **SAR 78M–234M**. We are *not* claiming this as fact — it is the assumption the model below is built on, and every output scales linearly if the real number is higher or lower.

---

## 2. The conversion leak, turned into money

### 2.1 What the audit actually measured (facts)

- Mobile **LCP of 57.5 seconds** on a **34 MB** page (Google PageSpeed, 8 Jul 2026). Most mobile visitors never see a car.
- The **"Purchase" CTA discards the selected car** — the `?car_name=` parameter is ignored, dumping the buyer into a **782-option dropdown**, then a salary/bank/mortgage finance interrogation before any human contact. The audit flagged this as **the single largest measured conversion leak.**
- **No per-car WhatsApp or call CTA** — only a generic footer link.

Independently, retail benchmarks quantify the app-vs-web gap this creates: mobile-web conversion runs ~2.5–4%, while shopping **apps convert at 6–18%** — a 2–5x uplift — and app cart-abandonment is ~20% vs. **85.65% on mobile web** (Arvisus, Criteo, Skailama). Al Saber's mobile web is not even at the low end of that range because the page barely loads.

### 2.2 The recovered-sales model [ESTIMATE]

The logic: an app removes the two killers the audit found — the load time and the dropped-car hand-off. It opens the car the buyer tapped, shows the price and a monthly-payment figure, and puts a WhatsApp/call button one tap away. We do **not** need to assume app-level conversion rates to make the case — we only need to recover a *fraction* of the visitors currently lost at the broken step.

**Assumptions (all adjustable):**
- Monthly qualified mobile visitors reaching a car page: **4,000** [ASSUMPTION — Al Saber to confirm via analytics; the audit noted traffic is currently below Google's field-data floor, so this is a target-state figure once SEO/perf fixes land]
- Of those, share who *intend* to enquire but are lost at the load time / dropped-car form: **conservatively 3%** = 120 lost high-intent sessions/month
- App recovers **just 15%** of those = **18 additional genuine leads/month**
- Lead-to-sale close rate: **20%** [ASSUMPTION — typical dealer sales-floor close on a warm inbound]

→ **~3.6 incremental sales/month ≈ 43 incremental sales/year.**

Now price it two ways:

| Scenario | Incremental sales/mo | Avg gross vehicle value | Incremental revenue/mo | Annual |
|---|---|---|---|---|
| **Economy-weighted** | 3.6 | SAR 90,000 | **SAR 324,000** | **SAR 3.9M** |
| **Blended** | 3.6 | SAR 130,000 | **SAR 468,000** | **SAR 5.6M** |
| **One luxury sale swings it** | +1 Rolls/Ferrari/mo | SAR 800K–1.5M | **+SAR 0.8–1.5M** | **+SAR 9.6–18M** |

The last row is the point that matters for a dealer with Al Saber's stock: **the app does not need to move volume to pay for itself.** Recovering *one* luxury sale that would otherwise have bounced on a 57-second load screen — a single Rolls-Royce or Ferrari lead that a competitor's faster app would have caught — returns more than the entire build cost (Section 4). Everything else is upside.

**Even the most pessimistic read** — recover only 5% of lost sessions, close only 15%, all economy cars at SAR 70,000 — still yields ~0.9 sales/mo ≈ **SAR 63,000/mo ≈ SAR 756,000/yr** in recovered revenue. The floor is comfortably above any plausible build cost.

### 2.3 Retention value: the asset a website cannot build

A website has no memory of a visitor. An app does. Push notifications are the single highest-ROI mechanic here, and the data is strong:

- Push-enabled apps retain users at **~2x** the rate of non-push (Invesp).
- Re-engagement push campaigns see **13% CTR**; targeted campaigns up to 30% (Invesp).
- 65% of users return within 30 days when push is on (MoEngage).

**Retention model [ESTIMATE]:**
- Assume the app accumulates **2,000 opted-in users** in year one (browsers + past buyers) [ASSUMPTION]
- A monthly "new arrivals / price drop / offer" push to 2,000 users at a conservative **8% CTR** = **160 re-engaged sessions/month**
- At a **2% enquiry rate** on re-engaged sessions = **~3 extra warm leads/month** at **zero incremental ad spend**

That is 3 leads/month that cost nothing after the app is built — the compounding asset. A used-car buyer returns to the market every 3–5 years; the app is how Al Saber stays on their phone until they do. A website cannot do this at all.

---

## 3. Competitive positioning: the cost of being app-absent

**Syarah** is KSA's category leader and it is **app-first**: 6M+ app downloads, 20,000+ cars sold, USD 82M+ raised (Series C USD 60M), now the largest car-refurbishing centre in MENA (Arab News, StartupScene, Entrepreneur). Motory and manufacturer apps occupy the rest of the shelf.

The strategic reality: **54% of mobile-commerce transactions now happen inside apps, not browsers** (Venn Apps). In a 98%-smartphone market, the car-shopping journey increasingly *starts and lives* in an app. A dealer with no app is not on that shelf at all — it is competing only for the shrinking share of buyers who happen to type a URL or arrive from a WhatsApp-forwarded link that (per the audit) renders as a bare URL with no preview.

**What being app-absent costs Al Saber [ESTIMATE / logical argument]:**
- Syarah and Motory are aggregators — Al Saber's inventory appears there *alongside every competitor's*, on their terms, often with a lead-fee or commission attached. Al Saber owns no direct channel to its own past buyers.
- Every luxury buyer who defaults to opening Syarah instead of thinking "Al Saber" is a brand-equity leak. Al Saber's differentiator is *curated premium stock and dealer relationship* — precisely what an aggregator flattens into a price grid.

**What catching up buys them:** a branded, owned channel where the Ferrari-to-Elantra range is presented on Al Saber's terms, push access to past buyers that no aggregator can touch, and a premium feel that matches the logo — directly answering the client's own stated pain that the current site "doesn't match their branding." The app is not a defensive me-too; it is the one place Al Saber can out-premium the aggregators, because the aggregators are optimised for volume, not for making a Rolls-Royce buyer feel curated-for.

---

## 4. Cost framing — realistic industry range, no fake quote

Code-OX has **not** quoted a fixed price yet. For deck purposes, here is the defensible market range for an MVP dealership app with the scope in Section 6 (browse/search, saved cars, push, WhatsApp deep-link, financing calculator), from 2026 benchmarks:

| Source | MVP mobile app range (2026) |
|---|---|
| Netguru / Aalpha / Bolder Apps | USD 15,000–50,000 |
| Marketplace-scope MVP, single platform, core features | USD 25,000–60,000 |
| Cross-platform (Flutter/React Native) saving | 30–45% vs. dual-native |

Converted and reasoned for this scope, a cross-platform MVP realistically lands around **SAR 90,000–200,000** to build, plus ~15–20%/year maintenance (industry standard). Al Saber's inventory backend already exists (Laravel), so the app can consume it via API rather than rebuilding data infrastructure — which pulls this toward the lower end of the range.

**The payback line for the deck:**
> At the model's mid-case (SAR 468,000/month recovered), an SAR 150,000 MVP pays for itself in **under one month** of recovered sales. Even at the pessimistic floor (SAR 63,000/month), payback is **~2.4 months** — and *one recovered luxury sale covers the entire build outright.*

This lets the deck say "this pays for itself within X recovered sales" honestly, without Code-OX having under- or over-committed on price.

---

## 5. Objection handling — data-backed, with proof points

**"We already have a website."**
The audit measured that website at 46/100, with a **57.5-second mobile load** and a purchase flow that **drops the car the buyer selected**. The website isn't a substitute for the app — it is the reason the app is needed. Apps convert 2–5x higher than mobile web and abandon at 20% vs. 85% (Criteo, Arvisus). The website should be fixed *and* the app built; they serve different buyers.
→ **Proof point:** run PageSpeed live in the meeting on their own car page. The 57.5s number is not ours to argue — it's Google's.

**"An app is expensive."**
Against the recovered-revenue model, it is the cheapest sales rep Al Saber will ever hire — mid-case payback under a month, and a single recovered luxury sale covers the build. The real expense is the status quo: every month without it is ~SAR 63,000–468,000 of leads leaking out the broken funnel.
→ **Proof point:** offer **milestone-based phased payment** — Al Saber pays per phase (Section 6), so cash out never runs ahead of value delivered. Nothing is due for Phase 2 until Phase 1 is live and measured.

**"Customers just use WhatsApp."**
Good — the app makes WhatsApp *better*, not redundant. Today there is **no per-car WhatsApp CTA** (audit finding); the buyer can't message about the specific car they're looking at. The app puts a deep-linked WhatsApp button on every car ("I'm interested in this G63, ref #1045") so the sales team receives context, not a cold "hi." WhatsApp is the closing channel; the app is what feeds it qualified, car-specific conversations.
→ **Proof point:** we can wire per-car WhatsApp deep-links as a **standalone pilot even before the full app** — a small, cheap, measurable test of lead quality uplift.

**"We need to think about it."**
Reasonable — so let's de-risk the decision, not delay it. Propose a **paid discovery + clickable prototype** as step one (small, fixed, capped), so the "think about it" happens with a real prototype in hand and a hard number on their own recovered-sales math, instead of a slide deck.
→ **Proof point:** a 2-week prototype of the browse→car→WhatsApp flow they can put in a real buyer's hands before committing to the full build.

---

## 6. Phased roadmap — effort (S/M/L) × impact

Sequenced by value-per-effort, not feature list order. Each phase is a payment milestone.

### Phase 1 — MVP (the money phase)
*Goal: stop the leak. Ship the flow the website breaks.*

| Item | Effort | Impact | Why here |
|---|---|---|---|
| Browse/search inventory (consume existing Laravel API) | M | High | Table stakes; backend already exists |
| Car detail with price + **monthly-payment figure** | S | High | Fixes the audit's "no payment context" gap |
| **Per-car WhatsApp deep-link + call button** | S | **Very High** | High impact, low effort — directly plugs the #1 leak; the single best value-per-effort item |
| **Push notification infra + opt-in** | M | **Very High** | Builds the retention asset from day one; every day delayed is opted-in users not captured |
| Saved / favourite cars | S | Medium | Low effort, feeds re-engagement push |
| Financing calculator (payment estimate, no bank interrogation) | M | High | Replaces the salary/bank form that kills conversion |

**Deliberately NOT in MVP:** in-app payment, live chat build, account/loyalty tiers, AR/360 views. None move the recovered-sales needle in month one — YAGNI until the funnel is proven.

### Phase 2 — Engagement & polish
| Item | Effort | Impact |
|---|---|---|
| Segmented push (by brand/budget/past interest) | M | High — 3–4x targeting uplift (Invesp) |
| Full-screen exterior-first galleries (fixes audit's gallery findings) | M | Medium |
| Bilingual EN/AR in-app (fixes the invisible-EN problem) | M | Medium — opens English luxury segment |
| Stock alerts ("new Ferrari arrived") | S | High — pure retention, low effort |

### Phase 3 — Differentiation
| Item | Effort | Impact |
|---|---|---|
| **AIWA integration** (Code-OX chat agent) for 24/7 car-specific enquiry handling | L | High — natural cross-sell; handles after-hours leads the sales floor misses |
| Trade-in valuation flow | L | Medium |
| Loyalty / VIP tier for repeat luxury buyers | M | Medium — matches the premium-brand positioning |
| Reviews / testimonials (fixes audit trust gap) | S | Medium |

**Cross-sell flag:** Phase 3's AIWA hook is the bundling opportunity — an app generating leads 24/7 needs something answering them 24/7. That is a second Code-OX line item, not a discount give-away.

---

## 7. One-paragraph summary for the deck cover

Al Saber sells across a market worth **SAR 122.8bn/year** (new cars alone) into a country with **98% smartphone penetration**, where **54% of mobile-commerce now happens in apps** and the category leader (Syarah, 6M+ downloads) is app-first — while Al Saber's own website loads in **57.5 seconds** and **forgets which car the buyer chose**. A cross-platform MVP app (est. **SAR 90K–200K**) that recovers even **15% of the leads currently lost** at that broken step returns **SAR 63K–468K/month** — paying for itself in **under a month at mid-case, or with a single recovered luxury sale** — and builds the one asset a website never can: a push channel back to every past buyer's phone.

---

**Code-OX** · code-ox.com · shabeeb.k@code-ox.com · +966 53 571 6437
Logo: code-ox.com/codeoxlogo.svg

### Sources
- Used-car market: [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/saudi-arabia-used-car-market)
- New-car sales & value 2025: [Halacarly](https://blog.halacarly.com/en/saudi-arabia-car-sales-2025-complete-report-with-numbers-brands-and-models/), [Focus2move](https://www.focus2move.com/saudi-arabia-auto-market/)
- Luxury-car market: [IMARC Group](https://www.imarcgroup.com/saudi-arabia-luxury-car-market)
- Smartphone/e-commerce penetration: [Saudi Market Research](https://saudimarketresearchconsulting.com/tapping-into-98-mobile-market-research-in-saudi-arabia/), [Statista](https://www.statista.com/outlook/emo/ecommerce/saudi-arabia/), [Mordor E-commerce](https://www.mordorintelligence.com/industry-reports/saudi-arabia-ecommerce-market)
- Syarah: [Arab News](https://www.arabnews.com/node/1919151/business-economy), [StartupScene](https://thestartupscene.me/INVESTMENTS/Riyadh-Based-Car-Marketplace-Syarah-Raises-60-Million-in-Series-C), [Entrepreneur](https://www.entrepreneur.com/en-ae/growth-strategies/saudi-arabia-based-syarah-opens-the-largest-car/463337)
- App vs. mobile-web conversion: [Arvisus](https://www.arvisus.com/e-commerce-mobile-apps-vs-mobile-websites-what-converts-better-in-2025/), [Criteo](https://www.criteo.com/blog/retail-travel-apps-higher-conversions-mobile/), [Skailama](https://www.skailama.com/blog/good-mobile-ecommerce-conversion-rate-2025), [Venn Apps](https://www.vennapps.com/blog/35-essential-stats-on-mobile-commerce-in-2025)
- Push notifications: [Invesp](https://www.invespcro.com/blog/push-notifications/), [MoEngage](https://www.moengage.com/learn/push-notification-statistics/)
- App development cost: [Netguru](https://www.netguru.com/blog/mobile-app-development-cost), [Aalpha](https://www.aalpha.net/articles/how-much-does-it-cost-to-build-an-mvp-mobile-app/), [Bolder Apps](https://www.bolderapps.com/blog-posts/mobile-app-development-cost-2026)
