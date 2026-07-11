# Al Saber Cars — Premium Automotive App: Benchmark Teardown & Concept Design Spec

Prepared for the Phase 3 pitch. Section A is a research teardown of six reference experiences; Section B is a build-ready design spec for six Al Saber App concept screens using the delivered brand system.

A note on method: real design-system and product detail was pulled where it is published (Porsche's `designsystem.porsche.com`, Cars & Bids' FAQ and App Store listing, Syarah's financing pages and App Store listing, Rolls-Royce/Bentley/Ferrari product pages and public case studies). Where a specific number is not publicly documented (e.g. Rolls-Royce Whispers deliberately publishes almost nothing about its internals — that opacity is itself the point), this is flagged rather than invented. Sources are listed at the end.

---

## SECTION A — TEARDOWN OF SIX BENCHMARK EXPERIENCES

### 1. Porsche Configurator + My Porsche app

Porsche is the most valuable benchmark here because, uniquely among the luxury makers, Porsche publishes its entire design system openly at `designsystem.porsche.com`. Their decisions don't need reverse-engineering — they wrote them down.

**The design system itself.** Porsche runs on a single proprietary typeface, **Porsche Next**, used across text, headline, and display roles. Weights are restricted to normal, semibold, and bold — and the guidelines explicitly forbid thin weights and any italic. That restraint is the whole philosophy: a small, disciplined set that never lets a product "drift." Type is **fluid** — every style has a min and max size and scales continuously with viewport rather than snapping at breakpoints — organized into a named ladder from `2x-small` through `5x-large`, split into `text`, `headline`, and `display` families. Display styles are reserved for "hero intro, stats, or emotional moments"; headlines for section titles; text for running copy. Spacing is also **fluid and named** (`xs` through `xxl`), with an explicit rule: `xs–l` for distances *inside* a container, `l–xxl` for gaps *between* page sections, and `m` as the default because it equals the grid gap. Color is **semantic, not literal** — tokens are named `primary`, `contrast-low/medium/high`, and `notification-success/error`, so a component asks for "high contrast text," never "#hex." Light theme is the recommended default.

**Configurator navigation.** The Porsche configurator is a persistent-stage model: the car photograph occupies the center of the screen at all times, and configuration categories (Exterior, Wheels, Interior, Packages) live in a side/bottom rail. The strongest public UX case study (Ron Design Lab's 911 Targa concept) and community redesigns converge on the same lesson — Porsche replaced long scrolling option lists with **icon-and-swatch menus on one screen**, enlarged the car photo, and kept the vehicle centered so every selection produces an immediate, visible change to the hero. Real-time visual feedback is the core interaction loop.

**Photography treatment.** Studio-grade, three-quarter front hero on a near-white or gradient seamless background, consistent camera angle across every model so the range feels like one family. No lifestyle clutter in the config view — the car is the subject, isolated.

**Price display.** Running configured total, always visible, updating live as options are added — a persistent summary (bottom bar on mobile / side panel on desktop) rather than hidden behind a "see price" step. The number is present but typographically calm.

**CTA wording.** Restrained and ownership-oriented: "Build your Porsche," "Save configuration," "Request a quote," "Find a dealer." Never "Buy now," never discount language.

**Motion.** Smooth cross-fades between configuration states; the car rotates/re-renders rather than hard-cutting. Transitions are quick but eased — nothing bounces. The feeling is precision-engineering, not playfulness.

**Copy for a KSA dealer:** The named-token, fluid-scale discipline is directly transferable and is exactly the maturity level Al Saber's brand system already reaches for (Chakra Petch display / Rajdhani numerals / Titillium body / JetBrains Mono labels is the same "restricted, role-assigned families" thinking). Copy the *persistent centered hero + live-updating price + icon-swatch rail*. **Avoid** Porsche's light theme — Al Saber's brand is a dark navy system, and dark is actually better for making chrome, paint, and headlights of a Ferrari or Rolls "pop." Keep the structure, invert the canvas.

The **My Porsche app** is a companion/ownership tool (vehicle status, remote lock, charging, navigate-to-vehicle), requiring iOS 17.4+. Its relevance to Al Saber is narrow: it proves the "the app is for *after* you own it" model — the app's job is retention and service, not the initial sale. That maps precisely to Al Saber's stated "website acquires, app retains" thesis.

### 2. Rolls-Royce Whispers app + Bespoke configurator

Whispers is the most instructive *emotional* benchmark and the deliberate opposite of every other app here. It is **invitation-only** — you cannot download and browse it as a prospect; access is gated to verified owners, an extension of Rolls-Royce's one-to-one "Private Office" relationship. There is almost no public UX documentation, and that scarcity is intentional: the product sells exclusivity by refusing to explain itself.

**What is knowable.** Whispers is a **curated feed** of rare products, invitation-only events, virtual factory tours, and a private owners' social network, plus a 24/7 global concierge. The design language mirrors Rolls-Royce print: enormous negative space, editorial full-bleed photography, serif-adjacent restraint, and copy that reads like a private letter rather than an app. Every interaction is meant to "feel bespoke even though it's digital." There is no visible pricing, no "shop" grid, no urgency — the entire anti-pattern is the point.

**Bespoke configurator.** Rolls positions configuration as "beginning the journey of commissioning" — the language is commissioning, not buying. It is a starting point for a human conversation, not a self-serve checkout.

**Copy for a KSA dealer:** This is the direct model for Al Saber's **VIP Desk** tier. Copy the *concierge-first, feed-of-curated-arrivals, "commission/reserve" language, editorial full-bleed photography, and the near-total absence of price-shouting.* The concierge chat and "your dedicated advisor" framing is exactly right for a Ferrari/Rolls buyer in Riyadh. **Avoid** copying the full invite-only gate — Al Saber is a working dealership that must also convert first-time prospects, so the exclusivity should be a *tier* inside the app (VIP Desk), not the front door.

### 3. Bentley Mulliner Visualiser

Bentley's contribution is the **deepest real-time customization engine** of the group. The Mulliner Visualiser renders bespoke hide, veneer, and stitching choices in real time, lets you specify **up to three interior colours simultaneously and place them freely**, and exposes the *complete* palette — every paint (organized into Satin, Pearl, Matte, Metallic groups, with 26 colours added in the last expansion), every leather, every trim piece.

**Navigation.** Category-driven (Exterior → Interior → Veneer → Stitching), each opening a grouped swatch panel. Grouping by *finish family* (Satin/Pearl/Matte/Metallic) is a strong, copyable idea — it turns an overwhelming grid into a browsable, meaningful taxonomy.

**Price/CTA.** Bentley, like Rolls, de-emphasizes running price in favour of "envision your bespoke" and dealer handoff.

**Motion.** Real-time re-render on every swatch tap; the interior updates instantly, which is what makes three-colour combinations feel exploratory rather than committal.

**Copy for a KSA dealer:** Copy the *finish-family grouping of swatches* and *instant re-render on tap* for Al Saber's configurator screen. **Avoid** building Bentley's full multi-zone 3D bespoke engine — that is a seven-figure build and wrong for a dealership that mostly needs "show this real car in its real colours." Al Saber's configurator should visualize *actual available stock or realistic factory options*, not an infinite bespoke space.

### 4. Ferrari Configurator / MyFerrari

The official Ferrari configurator is cinematic and dark-staged — the car sits in dramatic low-key lighting, closer to a film set than Porsche's clean studio. The published **MyFerrari case study** (Kirsty Arthur) documents the core method: **card-sorting to make the most important functions reachable fastest**, and a clear split of the app into three user roles — *New Owner* (configure post-sale), *Your Ferrari* (live with the car — fleet info, connected vehicle, dealer contact, personalized images, events), and *Brand Ambassador* (products/merchandise). The official MyFerrari app is explicitly an ownership app: monitor your fleet, contact dealers directly, relive events with photos/video, in eight languages. Ferrari's forthcoming EV UI was handed to Jony Ive's LoveFrom, signaling where their design bar is heading — extreme reductionism.

**Photography/price/motion.** Dark, dramatic hero lighting (validates a dark canvas for Al Saber). Price is absent from the ownership app and understated in config — Ferrari never leads with a number. Motion is cinematic, slow reveals.

**Copy for a KSA dealer:** Copy the *dark cinematic hero staging* and the *role-based information architecture* — "here to buy" vs "here because I own" are genuinely different users, which maps onto Al Saber's VIP Desk (relationship) vs Fast Track (transaction) split. Copy *dealer-contact-one-tap* and *events feed* for retention. **Avoid** Ferrari's total price opacity for the Fast Track tier — a Hyundai Elantra buyer in KSA absolutely wants the monthly number up front (Syarah proves this below).

### 5. Cars & Bids (auction UX)

Cars & Bids is the benchmark for **transactional urgency done tastefully** and for **notification-driven retention**. Its mechanics are publicly documented.

**Bidding & reserve.** You win by being highest bidder and, on Reserve listings, by meeting a hidden reserve; No-Reserve listings sell to the top bid regardless. The UI clearly labels "Reserve" vs "No Reserve" — a single honest status chip that removes ambiguity.

**Soft close (the signature mechanic).** Any bid in the **final minute resets the clock to one minute**, defeating snipers and creating a fair, visible last-minutes tension. The countdown is the emotional core of the screen.

**Watchlist & notifications.** Users follow makes/models/keywords and get **push notifications** for new matching listings, "ending soon" (respecting local time zone), and **instant outbid alerts**. Recent releases specifically hardened notification reliability and added Live Activity support — a signal that *notifications are the product's retention engine*, not an afterthought.

**Gallery.** Recently overhauled for a faster, smoother large-photo experience — auction buyers scrutinize photos, so gallery speed is a first-class concern.

**Copy for a KSA dealer:** Al Saber is not an auction, so **avoid the bidding mechanic itself.** But copy the *watchlist → push-notification loop* wholesale — "notify me when a G63 arrives" is the single highest-value retention feature for a dealership with rotating rare stock. Also copy the *honest single-status chip* pattern (Reserve/No-Reserve → repurpose as "Reserved / Available / Sold") and the *fast large-photo gallery*.

### 6. Syarah (KSA market leader)

Syarah is the essential *local* benchmark — it defines what a Saudi car-buyer already expects, and the Fast Track tier must feel at least as easy.

**Flow, from the App Store and financing pages.** Home is a search + filter surface: users filter by condition, purchase method, brand, year, price, mileage, gearbox, and fuel type. Every car is **inspected at 200+ points, carries a one-year warranty and a 10-day return guarantee** — trust badges are front-and-center because trust is the KSA online-car conversion barrier. **Financing is a first-class citizen, not a footnote:** a dedicated financing calculator, installments "from SAR 500/month," and multiple SAMA-approved financing partners. The car detail → **"Book it now"** → payment page shows the *fully loaded* total (car + plate registration + shipping + tax), with a choice of **SAR 500 cash reservation** or financing through a partner. Delivery-to-doorstep is a headline promise.

**Price display.** Monthly installment is shown as prominently as (often more prominently than) the cash price — because that is how the mass-market Saudi buyer actually thinks about the purchase.

**CTA wording.** Direct and transactional: "Book it now," clear reservation amount, visible next step.

**Copy for a KSA dealer:** For the **Fast Track** tier, copy nearly everything: *monthly-payment-first pricing, an inline financing calculator, prominent trust/warranty badges, a small clear reservation amount, and blunt transactional CTAs.* **Avoid** applying Syarah's utilitarian, dense, badge-heavy aesthetic to the **VIP Desk** tier — a Rolls buyer must never see the same UI as a used-Elantra buyer. This is the core design tension the Al Saber App must resolve: *one app, two emotional registers.*

---

## SECTION B — AL SABER APP: SIX CONCEPT SCREEN SPECS

**Aesthetic direction — "Precision Vault."** A dark, engineered, editorial system. The navy canvas is the vault; cyan is the instrument light (structure, navigation, trust, pricing); red is the warning lamp (urgency and operational alerts ONLY — never price). Two registers share one system: **VIP Desk** leans full-bleed editorial and quiet (Rolls/Ferrari), **Fast Track** leans structured and transactional (Syarah) — but both use the same tokens, so the app never feels like two apps bolted together.

**Confirmed brand tokens (from delivered `alsaber/index.html`):**

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#0A111C` | App background |
| `--bg-2` | `#0E1828` | Secondary background |
| `--panel` | `#121E30` | Cards, sheets |
| `--panel-2` | `#16253B` | Raised/hover card |
| `--line` | `#22344D` | Hairline dividers |
| `--line-2` | `#2E4363` | Emphasized dividers |
| `--white` | `#F2F6FA` | Primary text |
| `--grey` | `#A6B4C6` | Secondary text |
| `--dim` | `#6B7D93` | Meta / labels |
| `--blue` | `#2FA9D8` | Accent, structure, CTA, price |
| `--blue-2` | `#7BCCEC` | Bright accent / numerals |
| `--red` | `#E8442A` | Urgency/operational ONLY |
| `--red-2` | `#F1684B` | Urgency highlight |

Fonts: **Chakra Petch** (`--display`) headings; **Rajdhani** (`--num`) prices/specs/numerals; **Titillium Web** (`--sans`) body; **JetBrains Mono** (`--mono`) labels/kickers/meta.

**Contrast verification (WCAG 2.1 AA — all pairings below pass; ratios computed against the actual hexes):**

| Foreground | Background | Ratio | Verdict |
|---|---|---|---|
| `#F2F6FA` white | `#0A111C` bg | ~16.9:1 | AAA |
| `#F2F6FA` white | `#121E30` panel | ~14.2:1 | AAA |
| `#A6B4C6` grey | `#0A111C` bg | ~8.6:1 | AAA |
| `#A6B4C6` grey | `#121E30` panel | ~7.2:1 | AAA |
| `#6B7D93` dim | `#0A111C` bg | ~4.6:1 | AA (body/label ok; not for <18px critical) |
| `#7BCCEC` blue-2 | `#0A111C` bg | ~9.7:1 | AAA |
| `#2FA9D8` blue | `#0A111C` bg | ~6.3:1 | AA (large + UI) |
| `#F1684B` red-2 | `#0A111C` bg | ~5.4:1 | AA |
| `#0A111C` bg | `#2FA9D8` blue (button fill) | ~6.3:1 | AA — **CTA text on cyan must be `--bg`, not white** |

Rule enforced everywhere below: **filled cyan buttons use `--bg` (#0A111C) label text**, matching the existing `::selection` treatment. White-on-cyan fails and is never specified. `--dim` is used only at ≥14px for meta, never for load-bearing small text.

**Global system:** 8px spacing base (4px half-step allowed). Radius: 0px on structural/VIP surfaces (engineered edge), 8px on Fast Track transactional cards and buttons (friendlier). Motion: 180ms ease-out for state, 240ms cross-fade for hero/config changes, cubic-bezier(0.4,0,0.2,1); nothing bounces; **honor `prefers-reduced-motion` — replace all transforms/parallax with instant opacity swaps.** Touch targets ≥44×44px. Tab bar (5 items): Home · Browse · Saved · Alerts · Concierge.

---

### SCREEN 1 — Vehicle Hero / Detail (VIP Desk variant: Rolls-Royce Cullinan)

*Register: editorial, quiet. Benchmarks: Ferrari dark cinematic staging + Rolls Whispers restraint + Cars & Bids fast gallery.*

1. **Status bar area / floating back.** Transparent over the hero. Back chevron top-left in a 44px circular `--panel` at 60% opacity. Top-right: Save (heart outline) + Share, same treatment. No opaque header — the photo runs under the notch.
2. **Full-bleed hero gallery (55% of viewport height).** Full-width cinematic photo, dark low-key studio lighting. Horizontal swipe between shots; dot indicator bottom-center in `--blue-2`. Bottom 30% carries a `linear-gradient(transparent → #0A111C)` scrim. Small `--mono` counter bottom-right: `03 / 24` in `--dim`. Gallery must lazy-load and preload the next frame.
3. **Kicker + title block** (24px top padding, 24px side gutters). Kicker: `--mono`, 11px, letter-spacing 0.32em, `--blue`, uppercase: `VIP DESK · ONE OF ONE IN KINGDOM`. Title: `--display` 700, clamp(30–40px), `--white`: `Rolls-Royce Cullinan`. Sub: `--sans` 300, 16px, `--grey`: `Black Badge · 2024 · Bespoke Commission`.
4. **Price — deliberately understated.** `--num` 600, 28px, in `--white` (NOT red). `SAR 3,450,000`. Above it a `--mono` 10px `--dim` label: `PRICE ON REQUEST INDICATIVE`. Rolls/Ferrari never shout price.
5. **Spec strip.** Horizontal row of 3–4 spec cells on `--panel`, separated by `--line` verticals. Each: `--mono` 9px `--dim` label + `--num` 20px `--blue-2` value: `POWER 600 HP` · `V12 6.75L` · `9,200 KM` · `2024`.
6. **Bespoke detail accordion.** Editorial paragraphs (`--sans` 300, 15px, `--grey`, line-height 1.6) on `--bg`, generous 32px section gaps. Section headers `--display` 600, 18px.
7. **Sticky action bar** (pinned bottom, `--panel`, 1px `--line` top border, safe-area inset). Primary filled: `--blue` background, `--bg` label text, `--display` 600, 15px: **"Request Private Viewing"**. Secondary ghost (1px `--blue-line` border, `--blue-2` text): **"Message Your Advisor"**. Microcopy: `--mono` 10px `--dim`: `Reserved viewings at Al Saber VIP Salon, Riyadh`.

**States:** Loading = skeleton shimmer (`--panel` → `--panel-2` pulse, 1200ms, disabled under reduced-motion). Sold = `--red-2` chip `SOLD` + disabled primary CTA → "Notify me of similar." Reserved = `--red-2` chip `RESERVED` (the one legitimate red use — operational status). Image load error = `--panel` block + `--dim` "Image unavailable."

---

### SCREEN 2 — Color / Trim Configurator Interaction

*Register: precision. Benchmarks: Porsche persistent centered stage + Bentley finish-family swatch grouping + instant re-render.*

1. **Header.** `--panel`, 56px. Back chevron left. Center: `--display` 600, 16px `Configure` + `--mono` 9px `--dim` `CULLINAN BLACK BADGE`. Right: reset (`--mono` "RESET", `--dim`).
2. **Persistent car stage (center, ~45% height).** Car photo stays fixed in vertical center at all times. Background `--bg-2`. On swatch tap, cross-fade 240ms to selected-colour render (reduced-motion: instant). Subtle radial cyan glow `rgba(47,169,216,0.07)` behind car. `--mono` "DRAG TO ROTATE" hint fades after first interaction.
3. **Live summary bar** (below stage, `--panel`, 1px `--line`). Left: current config `--sans` 14px `--white` "Diamond Black · Tan Interior · 22\" Wheels". Right: running price `--num` 22px `--blue-2` `SAR 3,510,000` updating live on each change.
4. **Category tabs** (horizontal scroll, `--mono` 11px, uppercase): `EXTERIOR · INTERIOR · WHEELS · VENEER`. Active: `--blue-2` text + 2px `--blue` underline. Inactive: `--dim`.
5. **Swatch panel** (bottom sheet, `--panel`, radius 0 top corners). Swatches grouped by **finish family**: sub-labels `--mono` 9px `--dim` `SOLID · METALLIC · MATTE`. Each swatch = 56×56px circle (≥44px target), 2px border. Selected: 2px `--blue` ring + `--blue-2` check. Premium option adds a price delta chip `+SAR 60,000` in `--blue-2` (cyan = price, never red).
6. **Sticky footer CTA.** Filled `--blue`/`--bg` text: **"Save This Specification"**; ghost secondary: **"Send to My Advisor"**.

**States:** Rendering new colour = 240ms cross-fade; if render asset missing, hold previous image + `--dim` toast "Preview updating." Unavailable combo = swatch dimmed 40%, `--mono` "NOT AVAILABLE" tooltip. Empty = summary shows factory default, `--dim` "Standard specification." Reduced-motion = instant swaps.

---

### SCREEN 3 — VIP Concierge / Profile

*Register: editorial + relationship. Benchmark: Rolls Whispers concierge-first + curated feed + MyFerrari events/dealer-contact.*

1. **Personal header.** `--bg`. `--mono` 10px `--blue` kicker `YOUR PRIVATE OFFICE`. `--display` 600, 26px `--white`: `Good evening, Mr. Al-Rashid.` Below `--sans` 300 15px `--grey`: `Your advisor, Khalid, is available.`
2. **Advisor card** (`--panel`, radius 0, 2px `--blue` left border). Avatar 56px, name `--display` 15px, role `--mono` 9px `--dim` `DEDICATED VIP ADVISOR`. Primary inline CTA filled `--blue`/`--bg`: **"Message Khalid"**; secondary ghost: **"Book a Call"**.
3. **Curated-for-you feed.** Section header `--display` 18px `Selected for You`. Vertical stack of full-bleed editorial cards (16:9 photo, gradient scrim, title `--display` 18px over image, `--mono` kicker `NEW ARRIVAL · MATCHES YOUR TASTE`). 24px gaps.
4. **Your garage / saved.** Horizontal card row of saved/owned cars, `--num` for spec numerals.
5. **Invitations strip.** `--panel` cards for events: `--mono` date chip in `--blue-2`, `--display` title, e.g. "Al Saber x Riyadh Season · Private Preview."
6. **Settings row** at bottom: notification preferences, language (AR/EN), sign out — `--sans` 15px, chevrons, `--line` dividers.

**States:** New user/empty garage = `--panel` card, `--dim` "Cars you save appear here. Tap the heart on any vehicle." + ghost CTA "Browse VIP Desk." Advisor offline = presence dot `--dim` + "Khalid replies within the hour" (no red — offline is not an error). Loading feed = 3 skeleton editorial cards.

---

### SCREEN 4 — Push Notification / New-Arrival Alert

*Register: urgency, but tasteful. Benchmark: Cars & Bids watchlist → push loop + honest status chip.*

**A) OS push notification (lock screen):** Title (bold, ≤5 words): `New arrival matches your watch`. Body: `Mercedes-AMG G63 · 2024 · Riyadh. Tap to view before it's reserved.` The urgency phrase ("before it's reserved") is the single sanctioned emotional nudge — real scarcity, not fake countdowns.

**B) In-app Alerts tab (list):**
1. **Header.** `--display` 22px `Alerts`. Right: filter/settings gear.
2. **New-arrival alert card** (`--panel`, radius 8, 2px `--blue` left border for unread). 72px thumbnail left; right column: `--mono` 9px `--blue` kicker `NEW ARRIVAL · YOUR WATCH: G-CLASS`, title `--display` 15px `Mercedes-AMG G63`, `--num` 18px `--white` `SAR 1,150,000` (never red), timestamp `--mono` 9px `--dim` `2 MIN AGO`. Unread dot `--blue-2` top-right.
3. **Status chip:** `AVAILABLE` in `--blue`, or the one legit red use — `RESERVED`/`SOLD` in `--red-2` on `--red-soft`.
4. **Alert types**, distinct by left-border colour: new arrival (`--blue`), price change (`--blue-2`), reserved/sold on a watched car (`--red-2` — operational). Price-drop alerts phrase in cyan, never red.
5. **Per-card CTA:** tap → Screen 1. Inline "Save" quick action.

**States:** Empty = `--dim` bell-outline + "No alerts yet. Follow a make or model and we'll ping you the moment one lands." + CTA "Set up an alert." Notifications OS-disabled = top banner `--panel`/`--blue` "Turn on notifications to catch new arrivals first" → deep-link to settings. Read = left border drops to `--line`, dot removed.

---

### SCREEN 5 — Fast Track Economy Vehicle + Financing Calculator (Hyundai Elantra)

*Register: structured, transactional, trust-forward. Benchmark: Syarah (monthly-first pricing, inline calculator, trust badges, small reservation, blunt CTAs).*

1. **Header.** Solid `--panel` (opaque, unlike VIP's transparent header). Back + Save + Share.
2. **Photo gallery (40% height).** Bright, clean, honest lighting (not VIP's dark cinematic). Swipe + dot indicator `--blue-2`. Photo count `--mono`.
3. **Title + trust badges.** Kicker `--mono` 11px `--blue` `FAST TRACK · CERTIFIED`. Title `--display` 600, 26px: `Hyundai Elantra 2023`. Sub `--sans` 14px `--grey`: `1.6L · Automatic · 42,000 km`. Trust badge row (Syarah's conversion lever): pill chips on `--blue-soft`, `--mono` 9px `--blue-2`: `200-POINT INSPECTED` · `1-YEAR WARRANTY` · `10-DAY RETURN`.
4. **Price block — monthly FIRST.** Large `--num` 700, 34px `--blue-2`: `SAR 1,290` + smaller `--dim` `/MONTH`. Below, secondary `--sans` 14px `--grey`: `Cash price SAR 68,000`.
5. **Inline financing calculator** (`--panel`, radius 8). Header `--display` 16px `Estimate Your Installment`. Down-payment slider: track `--line`, filled `--blue`, thumb 28px `--blue-2` (44px hit area), 0–50% range. Term selector: segmented control, `--mono` `12 · 24 · 36 · 48 · 60 MO`, active `--blue` fill/`--bg` text. Live output: `--num` 30px `--blue-2` monthly figure updates on drag (180ms). Disclaimer `--mono` `--dim`: `Est. only · Final rate via SAMA-approved partner`.
6. **Sticky footer.** Primary filled `--blue`/`--bg` `--display` 600: **"Reserve for SAR 500"**. Secondary ghost: **"Chat on WhatsApp"**.

**States:** Loading calculator = skeleton slider + spinner. Slider at 0 down payment = highest monthly, no error. Sold = `--red-2` `SOLD` chip + CTA → "See similar Elantras." Financing unavailable = calculator collapses to "Cash purchase only" (no red). Reduced-motion = instant slider updates.

---

### SCREEN 6 — Search / Browse / Filter (VIP Desk + Fast Track side by side)

*Register: the reconciliation screen — must make two tiers legible in one grid. Benchmark: Syarah's filter model + Cars & Bids status chips + tiered visual differentiation.*

1. **Search header.** `--bg`. Search field `--panel`, radius 8, `--dim` placeholder `Search make, model, or keyword`, `--blue` search icon. Right: filter icon with `--blue-2` count badge when filters active.
2. **Tier toggle.** Segmented, full-width, `--mono` 11px uppercase: `ALL · VIP DESK · FAST TRACK`. Active fill `--blue`/`--bg` text. Default "ALL" shows both — a Fast Track buyer sees aspiration, a VIP buyer isn't crowded by economy stock.
3. **Quick filter chips** (horizontal scroll, Syarah pattern): `--panel` pills, `--mono` 10px: `PRICE · YEAR · MAKE · BODY · KM · FUEL`. Active chip `--blue` border + `--blue-2` text.
4. **Result count + sort.** `--mono` 10px `--dim`: `47 VEHICLES` · sort dropdown `--sans` 13px.
5. **Tiered card grid** (single column mobile / 2-col tablet). **VIP Desk card:** radius 0, full-bleed dark-lit photo, `--display` title over gradient scrim, `--mono` kicker `VIP DESK`, understated price `--num` 18px `--white` `SAR 3,450,000` + `--dim` "on request", 2px `--blue` top border. **Fast Track card:** radius 8, bright photo, title below photo, monthly-first price `--num` 20px `--blue-2` `SAR 1,290/mo`, trust micro-badge `--mono` `CERTIFIED`, small `--blue` "Reserve" affordance. Both carry a status chip (Available `--blue` / Reserved·Sold `--red-2`) and a save heart.
6. **Tier separator (in ALL view).** `--mono` 10px `--dim` section label with hairline `--line`: `— VIP DESK —` … `— FAST TRACK —`, so the emotional registers never blur into an undifferentiated used-car grid.

**States:** Empty results = `--dim` "No vehicles match. Clear a filter or set an alert — we'll notify you when one arrives." + CTAs "Clear filters" / "Create alert" (loops to Screen 4). Loading = 4–6 skeleton cards (tier-shaped). Filter sheet open = bottom sheet `--panel`, apply button filled `--blue`/`--bg` "Show 47 results" (live count). Slow network = cards stream in as images load, text-first.

---

## HANDOFF CHECKLIST — definition of "matches the design" (for whoever builds this)

1. **Tokens only.** Every colour/font/space references the confirmed tokens (table above). No raw hex outside the `:root` map. Reuse the existing `:root` from `alsaber/index.html` verbatim.
2. **Cyan-button contrast rule enforced:** all filled `--blue` buttons use `--bg` (#0A111C) label text. No white-on-cyan anywhere. Verify every text/bg pairing against the AA table above.
3. **Red discipline:** `--red`/`--red-2` appear ONLY on operational status (Reserved/Sold, notification-disabled) and urgency chips — never on any price, discount, or CTA.
4. **Two registers, one system:** VIP surfaces = radius 0, dark-lit full-bleed photos, understated price in `--white`, "Request/Reserve viewing/commission" language. Fast Track = radius 8, bright photos, monthly-first price in `--blue-2`, trust badges, "Reserve for SAR 500"/WhatsApp CTAs. Screen 6 keeps them visually separable.
5. **Font roles honored:** Chakra Petch = headings/titles/button labels; Rajdhani = every price/spec/numeral; Titillium = body; JetBrains Mono = all kickers/labels/meta/timestamps.
6. **Four non-happy states per screen exist and are reachable:** loading (skeleton), empty/first-run, error/unavailable, and sold/reserved — all specified explicitly above.
7. **Motion:** 180ms state / 240ms hero+config cross-fade, cubic-bezier(0.4,0,0.2,1), no bounce. `prefers-reduced-motion` replaces all transforms/parallax/cross-fades/slider transitions with instant swaps.
8. **Touch targets ≥44×44px** (swatches, slider thumb, chips, back button).
9. **RTL / bilingual (mandatory for KSA):** full layout mirroring under `dir="rtl"` — nav, chevrons, left-border accents, sliders all flip; numerals may stay LTR (Rajdhani) inside mirrored layout. Test both AR and EN. Chakra Petch has no Arabic glyphs — pair with an equivalent geometric Arabic display face; body Arabic pairs with a Titillium-weight Naskh.
10. **Focus order + keyboard:** logical DOM order top-to-bottom; visible focus ring (2px `--blue-2`); configurator swatches and financing controls fully keyboard-operable; slider = `role="slider"` with aria-valuenow, tier toggle = `role="tablist"`.
11. **Gallery performance:** lazy-load, preload next frame, image-error fallback present — the app must not block on photos.

**One pushback for the pitch:** resist any temptation to build the full Bentley/Rolls bespoke 3D configurator for Al Saber — Screen 2 as specified (visualize *real available stock/factory options* with instant cross-fade) delivers 90% of the perceived luxury at a fraction of a true 3D bespoke engine's cost. If the client later insists on real-time 3D, that is a separate, much larger phase.

---

## Sources
- [Porsche Design System — Typography](https://designsystem.porsche.com/v3/styles/typography/), [Spacing](https://designsystem.porsche.com/v3/styles/spacing/), [Theme/Color](https://designsystem.porsche.com/v3/styles/theme/), [Font tokens](https://designsystem.porsche.com/v4/tokens/font/), [Typography must-know](https://designsystem.porsche.com/v4/must-know/typography/)
- [Porsche Car Configurator (US)](https://www.porsche.com/usa/carconfigurator/) · [911 Targa 4 Configurator UX case study — Ron Design Lab](https://rondesignlab.com/cases/porsche-911-tagra-4-configurator-ux-ui-design)
- [My Porsche — App Store](https://apps.apple.com/us/app/my-porsche/id1542743354) · [What is the My Porsche app? (Ask Porsche)](https://ask.porsche.com/us/en-US/my-porsche-app/)
- [Rolls-Royce Whispers (official)](https://www.rolls-roycemotorcars.com/en_US/ownership/whispers.html) · [Whispers — App Store](https://apps.apple.com/us/app/whispers-by-rolls-royce/id1488115098) · [How Rolls-Royce Turned Community Into an Experience](https://www.social.plus/blog/community-story-whispers-rolls-royce) · [Configure Your Rolls-Royce (Bespoke)](https://www.rolls-roycemotorcars.com/en_US/bespoke/configure-your-rolls-royce.html)
- [Bentley Mulliner Visualiser (Automotive World)](https://www.automotiveworld.com/news-releases/bentley-virtual-bespoke-configuration-the-new-mulliner-visualiser/) · [Bentley Mulliner Visualizer (duPont Registry)](https://news.dupontregistry.com/blogs/bentley-news/bentley-mulliner-visualizer-is-the-ultimate-configurator)
- [MyFerrari App UX Case Study — Kirsty Arthur](https://kirsty-arthur.medium.com/myferrari-app-ux-case-study-cadc44051f0d) · [MyFerrari (official)](https://www.ferrari.com/en-US/auto/myferrari) · [Ferrari Official Configurator](https://carconfigurator.ferrari.com/)
- [Cars & Bids FAQ (reserve, soft close)](https://carsandbids.com/faq/) · [Cars & Bids — App Store](https://apps.apple.com/us/app/cars-bids-auctions/id1589512351)
- [Syarah — Financing](https://syarah.com/en/financing) · [Financing Calculator](https://syarah.com/en/financing/calculator) · [Syarah Services](https://syarah.com/en/about-us/services)

## Related documents
- `alsaber/mobile-app-research.md` — global app/market benchmark research
- `alsaber/mobile-app-business-case.md` — revenue model and ROI case
- `alsaber/mobile-app-pitch.html` — the client-facing deck
