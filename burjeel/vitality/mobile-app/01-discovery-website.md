
# Vitality Home Healthcare — Phase 1 Discovery: Website & Digital Experience Audit

**Client:** Vitality Home Healthcare (vitality.sa) — Premium home healthcare, Riyadh, KSA
**Prepared by:** CodeOx — Mobile App Engagement, Phase 1 Discovery
**Date:** 9 July 2026
**Sources:** Full codebase analysis (`/Users/shabeeb/Documents/code-ox/vitality`, Next.js 16.2.4 + next-intl + MongoDB CMS) and live rendered pages at https://vitality.sa (home, services, programs, about)
**Feeds:** 8 downstream workstreams — treat this as the single source of truth for what exists today.

---

## 1. Website Structure — Sitemap, IA, Navigation

### 1.1 Tech stack (context for app team)
- **Framework:** Next.js 16.2.4 (App Router), React 19.2.4, Tailwind CSS v4 (`@theme` tokens in `globals.css`; `tailwind.config.ts` is content-paths only)
- **i18n:** next-intl, locales `en` + `ar` with full RTL support (`src/i18n/routing.ts`, `src/messages/{en,ar}.json`)
- **CMS:** Custom admin panel at `(admin)/admin/*` backed by MongoDB/Mongoose (models: Home, Service, ServiceCMS, Program, ProgramCMS, Blog, Career, Job, Application, MedicalTeam, About, Contact, Enquiry, PromoCode, SEO, SEOGlobal, Footer, PrivacyPolicy, LegalTerms, User). Nearly every public section is CMS-editable with bilingual fields.
- **Media:** Cloudinary + `/api/upload` + `/api/files/uploads/*`; animation stack GSAP + ScrollTrigger + Framer Motion + Embla carousel; forms react-hook-form + zod; email nodemailer; tests Playwright e2e (home, contact, careers, i18n switch, RTL, admin login).
- **Server:** `next start -p 3008`.

### 1.2 Public sitemap (from `src/app/(locale)/[locale]/` + `src/app/sitemap.ts`)

| Route | Page | Priority (sitemap) | Notes |
|---|---|---|---|
| `/{locale}` | Home | 1.0 | 10 CMS-driven sections (see 1.4) |
| `/{locale}/about` | About Us | 0.8 | Hero, intro, mission/vision, philosophy, milestones, leadership, stats, quote, CTA |
| `/{locale}/services` | Services list | 0.8 | Grid of service cards |
| `/{locale}/services/[slug]` | Service detail | 0.7 | Includes / skilled / personalised / preparation sections + booking CTA |
| `/{locale}/programs` | Programs & Packages | 0.8 | Grid of 14 programs/services |
| `/{locale}/programs/[id]` | Program detail | 0.6 | Full-viewport hero, inclusions, "How it works" steps, CTA |
| `/{locale}/medical-team` | Medical Team | 0.8 | Grid + hero + CTA |
| `/{locale}/medical-team/[slug]` | Team member profile | — | Bio, credentials, languages |
| `/{locale}/news` | Blog | 0.9 | Featured + grid |
| `/{locale}/news/[slug]` | Article | 0.6 | |
| `/{locale}/careers` | Careers | 0.7 | Job listings + application modal (CV upload) |
| `/{locale}/careers/[slug]` | Job detail | 0.5 | |
| `/{locale}/contact` | Contact | 0.7 | Contact methods + enquiry form |
| `/{locale}/testimonials` | Testimonials | 0.6 | |
| `/{locale}/privacy`, `/{locale}/terms` | Legal | 0.3 | CMS-driven |

Plus: `not-found.tsx`, `robots.ts`, dynamic `sitemap.ts` (DB-driven, excludable per-page via SEO model).

**There is NO on-site booking page.** `messages/en.json` contains a complete 4-step booking wizard vocabulary (`booking.step1..step4`, payment, insurance, booking reference) that is **not implemented anywhere** — a fully-specified but dormant booking flow.

### 1.3 Navigation model
- **Top nav** (`Navbar.tsx`, fixed, 72px, transparent→navy on scroll): About Us · Services · Programs · News · Careers · Contact. Home reached via logo. "Home" link commented out.
- **Right cluster:** gold "Book Now" pill (→ `BOOKING_URL`, external, `target="_blank"`), language switcher (EN ⇄ عربي), mobile hamburger → `MobileMenu` overlay.
- **PromoStrip** (36px, above nav): active promo code + phone fetched client-side from `/api/promo-codes?active=true` and `/api/footer`.
- **Persistent floaters:** WhatsApp FAB bottom-right (green #25D366, pre-filled Arabic message "مرحباً، أريد الاستفسار عن خدمات فيتاليتي"), `LiveChatWidget` bottom-left — a **mock chat** (static "Online" header, one Arabic greeting, an input that goes nowhere). Prime AIWA insertion point.
- **Message keys exist but pages don't** for: Promotions, Why Vitality, Coverage Area, FAQs, Testimonials nav — vocabulary ready, IA not yet exposed.

### 1.4 Home page section order (`page.tsx`, all CMS-driven from `Home` collection)
1. `DiscoveryHero` — full-screen hero, stats, dual CTA
2. `DoctorsGallery` — "How It Works"
3. `ServicesTeaser` — "Our Premier Services" (DB services, beauty sorted last)
4. `BeautySection` — "Beauty & Wellness"
5. `NearbyHospitals` — "Vitality.. Your Partner in Wellness"
6. `RecoveryPath` — "Clinical Path to Wellness" (6-step journey)
7. `NewsTeaser` — "Latest News"
8. `TestimonialsSection` — "Patient Testimonials"
9. `MedicalTeamPreview` — "Medical Elite"
10. `BookingCTAStrip` — "Our Promise — Uninterrupted Care" (dual CTA + stats + hotline)

---

## 2. Service Offerings (complete inventory)

### 2.1 Core services — `src/data/services.ts` (seed) / `Service` model (live, CMS-managed)

| # | Service (EN) | Service (AR) | Duration | Category tag | Description (EN, exact) |
|---|---|---|---|---|---|
| 1 | Doctor Home Visit | زيارة طبيب | Annual | membership | "Professional medical consultations and health assessments at the comfort of your home by qualified doctors." |
| 2 | Home Nursing Care | التمريض المنزلي | 2–3 hours | checkup | "Comprehensive nursing care services at home, ensuring comfort, safety, and continuous medical support." |
| 3 | Home Laboratory Services | المختبر المنزلي | 45–60 mins | aesthetics | "Convenient home sample collection and laboratory testing with accurate and timely results." |
| 4 | Caregivers | مرافق صحي | 60–90 mins | aesthetics | "Dedicated healthcare support and assistance for patients to ensure comfort and proper daily care." |
| 5 | Home Physiotherapy | العلاج الطبيعي المنزلي | 45–60 mins | aesthetics | "Personalized physiotherapy sessions at home to support recovery, mobility, and rehabilitation." |
| 6 | Beauty at Your Fingertips | جمالك على بُعد ضغطة زر | 1–2 hours | iv-therapy | "Enjoy advanced aesthetic and wellness treatments in the comfort of your home, delivered with professionalism and care." |
| 7 | HydraCool Therapy | الهيدرا كول | 45–60 mins | physiotherapy | "A refreshing skin treatment designed to deeply cleanse, hydrate, and rejuvenate your skin for a healthy glow." |
| 8 | Venus Legacy for Body Contouring & Slimming | فينوس ليجاسي للنحت والرشاقة | 60–90 mins | wellness | "Advanced non-invasive body contouring technology to tighten skin, reduce cellulite, and enhance body shape." |
| 9 | IV Vitamin Therapy | العلاج بالفيتامينات الوريدية | On Request | nursing | "Personalized IV vitamin infusions designed to boost energy, improve hydration, strengthen immunity, and enhance overall wellness." |

**Note:** the `category` values are visibly shuffled relative to service identity (e.g. Home Lab = "aesthetics", HydraCool = "physiotherapy") — the taxonomy is decorative today, not a functional filter. The app will need a real clinical taxonomy. No prices on any service. No on-page filtering/search on the services list.

Each service carries four bilingual content blocks (rendered on the detail page):
- **includes** (e.g. Physiotherapy: Physical Assessment, Therapeutic Exercises, Pain Management Therapy, Mobility Improvement)
- **skilledIncludes** ("Board-Certified" section — e.g. Post-Surgery Rehabilitation, Sports Injury Recovery, Orthopedic Therapy, Neurological Physiotherapy)
- **personalIncludes** ("Personalised Care" — e.g. Customized Exercise Plans, Posture Correction, Home Recovery Guidance, Progress Monitoring)
- **preparation** (patient prep guide — e.g. Wear Comfortable Clothing, Prepare Open Exercise Space, Provide Medical Reports, Stay Hydrated)

### 2.2 Service-line copy — `src/data/content.ts` (`SERVICES_CONTENT`)
- **Home Healthcare Services:** "Our medical team works in full coordination with treating physicians to ensure continuity of care and optimal clinical outcomes." Items: Home Nursing · Chronic Disease Management · Elderly Care · Medication Administration & Treatment Plans · Home Physician Visits · In-Home Laboratory Testing.
- **Physical Therapy & Rehabilitation:** "specialized physiotherapy and rehabilitation programs designed to restore mobility, improve flexibility, and enhance functional independence."
- **Medical IV Therapy:** "medically supervised IV therapy programs support overall wellness, boost energy levels, and enhance vital body functions safely at home."
- **Medical Aesthetics:** Mesotherapy ("Stimulates collagen and improves skin elasticity."), **Glow Program** ("Enhances radiance and skin vitality."), **Shape It Program** / AR 'برنامج "كن كما تتمنى"' ("Personalized treatments for aesthetic enhancement.").

### 2.3 Item-level glossary — `src/data/serviceMap.ts`
~45 named care items each with a one-line bilingual clinical description (e.g. "24/7 nurse hotline: Direct line to a qualified nurse available around the clock for advice and emergencies."; "Qualified nursing staff: MOH-certified nurses trained in advanced home-care procedures."). This is a ready-made **care-item dictionary** the app can reuse for tooltips/cards.

---

## 3. Packages & Programs (complete inventory)

Source: `src/data/packages.ts` (seed) → live `Program` collection (CMS-managed; live page shows the same 13 + "14+ Care Programs" stat). Tiers enum: `essential | advanced | elite | service | program` (essential/advanced/elite currently unused — tier ladder reserved for future). All priced items are per **session**, currency **SAR**. `price: 0` renders as no price shown.

| Package (EN) | AR | Tier | Price | Includes | Positioning |
|---|---|---|---|---|---|
| Health Check at Home | الفحص الصحي الشامل في المنزل | service | — | Lab tests, Medical consultation, Personalized health report | Entry-level wellness snapshot |
| **Premium Post-Surgery Recovery Care** | برنامج التعافي الطبي بعد العمليات | program | — | Physician visits, Nursing care, Physiotherapy sessions, Wound monitoring | **Featured, badge "Most Popular" / "الأكثر طلباً"** — hero program |
| Home Care Plus Program | خدمات الرعاية المنزلية الشاملة | program | — | Elderly care, Chronic condition management, Daily health monitoring, 24/7 nurse hotline | Long-term/elderly flagship |
| Diabetes Care Program at Home | برنامج العناية بمرضى السكري في المنزل | program | — | Blood sugar monitoring, Insulin administration, Nutrition counseling, Diabetic foot care | Chronic-condition vertical |
| Lymphatic Recovery Therapy | علاج التصريف اللمفاوي للتعافي | service | — | Lymphatic drainage massage, Swelling reduction, Post-procedure recovery | Post-cosmetic/recovery wellness |
| IV Antibiotic Therapy at Home | المضادات الحيوية الوريدية في المنزل | service | — | IV antibiotic administration, Medical supervision, Qualified nursing staff | Clinical at-home treatment |
| IM Injection | إبرة عضلية | service | **250 SAR** | IM injection, Certified nurse, Post-injection monitoring | Priced micro-service |
| IV Therapy | علاج وريدي | service | **300 SAR** | IV line insertion, Fluid/medication infusion, Vital signs monitoring | Priced micro-service |
| Urinary Catheter Insertion/Removal | قسطرة بولية | service | **350 SAR** | Catheter insertion/removal, Hygiene care, Certified nursing procedure | Priced micro-service |
| NGT Tube Insertion | أنبوب تغذية (تركيب) | service | **350 SAR** | NGT insertion, Placement verification, Feeding guidance | Priced micro-service |
| NGT Tube Removal | أنبوب تغذية (إزالة) | service | **250 SAR** | Safe removal, Post-removal care, Certified nurse | Priced micro-service |
| Tracheotomy Care | العناية بثقب القصبة الهوائية | service | **350 SAR** | Cleaning, Tube maintenance, Respiratory assessment | Priced micro-service |
| Nebulization | جلسة علاج بالبخار | service | **250 SAR** | Nebulizer delivery, Symptom relief, Certified nurse | Priced micro-service |
| Wound Care Grade 1 | العناية بالجرح (درجة 1) | service | **389 SAR** | Cleaning & dressing, Infection prevention, Healing assessment | Priced micro-service |

**Pricing observations:** only 8 nursing micro-services carry prices (250–389 SAR/session); flagship programs are quote-on-request. **Live site currently displays no prices at all** (price 0 suppressed and priced items not rendering price on the public grid per WebFetch of /en/programs). Multi-session bundles, memberships and subscriptions exist in vocabulary (`packages.perMonth "/ month"`, `visits`, tier ladder) but are unused — clear runway for app subscription packaging.

### 3.1 Specialized Medical Programs (`PROGRAMS_CONTENT`, content.ts)
1. **Chronic Disease Stability Program** — "Ongoing monitoring and management for patients with chronic conditions."
2. **Elderly Care Program** — "Comprehensive care designed for the unique needs of elderly patients at home."
3. **Post-Surgery & Recovery Program** — "Structured recovery plans to support patients following surgery or illness."
4. **Home Rehabilitation Program** — "Physiotherapy and rehabilitation delivered entirely at home for maximum comfort."

### 3.2 Promotions (`src/data/promotions.ts` — dated 2025, likely stale seeds)
- **Ramadan Wellness Special** — 30% off, at-home wellness checkups for fasting patients (vitals, mobile lab, clinical dietetics). CTA "Secure Offer".
- **Elite Family Care Bundle** — 25% off, dedicated physician access for up to 6 family members + quarterly preventative health audits. CTA "Explore Bundle".
- **Distinguished Senior Care** — 20% off, premium monthly senior programs: daily clinical monitoring, complex medication management, specialized companionship. CTA "Learn More".
Plus a live **PromoCode** system (admin-managed codes surfaced in the PromoStrip).

---

## 4. User Booking Journey — how booking actually works today

### 4.1 The single most important line in the codebase
`src/lib/constants.ts`:
```ts
export const WHATSAPP_NUMBER = "966504447658";
// ponytail: swap back to "https://patients.nixpend.com/vitality/" when portal is ready
export const BOOKING_URL = `https://wa.me/${WHATSAPP_NUMBER}`;
```
**Every "Book Now" in code is an external handoff — there is no native booking flow on the website.** The Nixpend patient portal (`patients.nixpend.com/vitality/`) was live as the booking target, then rolled back to plain WhatsApp; the live home page currently mixes both: CMS-configured hero/CTA buttons "Begin Healing Journey", "BOOK A DOCTOR VISITS", "START YOUR HEALING" → `patients.nixpend.com/vitality/`, while "Book Now"/"Book Your Session" and all services-page CTAs → `wa.me/966504447658`.

### 4.2 Every booking entry point (all → WhatsApp or Nixpend portal, all `target="_blank"`)
| Surface | CTA | Destination |
|---|---|---|
| Navbar (desktop) | "Book Now" gold pill | `BOOKING_URL` (wa.me) |
| DiscoveryHero | primary CTA | `BOOKING_URL`; live CMS override → Nixpend portal |
| Services list card | "Book Now" (full-width gold) | `BOOKING_URL` |
| Service detail (hero + bottom CTA) | "Book Now" + "WhatsApp" pair | CMS link or `BOOKING_URL` / `wa.me` |
| Program detail | Book / WhatsApp / Call buttons | CMS links / `wa.me` / `tel:920022827` |
| BookingCTAStrip (home) | primary + WhatsApp + "Or Via Emergency Line" 920022827 | CMS / wa.me / tel |
| WhatsApp FAB (every page) | pre-filled AR message | `wa.me/966504447658` |
| Medical team CTA, About CTA, Careers CTA | various | same pattern |

Trust microcopy under service-detail CTA: **"Secure & Encrypted Booking" / "نظام حجز آمن ومشفر"** — displayed even though booking is a WhatsApp jump; the brand is already promising a secure booking system.

### 4.3 The only native form: contact enquiry
`ContactInterface.tsx` → `POST /api/enquiry`. Fields: **name, email, phone, message** (all required; email regex; length caps; HTML-stripped). On submit: stored in MongoDB `Enquiry` (status workflow for admin), fire-and-forget email via nodemailer (`sendNewEnquiryNotification`), UI flips to a submitted state. No auto-reply to patient, no SLA, no booking semantics. (Careers has a second form: job application with CV upload.)

### 4.4 Dormant booking vocabulary (messages/*.json `booking.*`)
Complete 4-step wizard copy exists in both languages: Step 1 Select Service → Step 2 Date & Time → Step 3 Your Details (patient name, phone, WhatsApp, area/district, full address, notes, health insurance) → Step 4 Payment → "Booking Confirmed Successfully!" + "Booking Reference". Supporting constants also dormant: `RIYADH_AREAS` (12 districts: Al Olaya, Al Malaz, Al Nakheel, Al Sulimaniyah, Al Rawdah, Al Murabbah, Al Yasmin, Al Sahafa, Al Woroud, Hittin, Al Aqiq, Al Hamra), `TIME_SLOTS` (08:00–20:00 hourly, skipping 13:00), `INSURANCE_PROVIDERS` (Bupa Arabia, Tawuniya, MedGulf, Al-Rajhi Takaful, AXA Cooperative, No Insurance). **The full booking domain model was designed and translated — it just never shipped as UI.** This is the app's blueprint, pre-approved by the client's own content.

### 4.5 No Nixpend API integration in the web codebase
Zero API calls to Nixpend anywhere in `src/` — the only Nixpend touchpoint is the (currently commented-out) portal URL. Therapist roster, availability, scheduling live entirely inside Nixpend; the website has no visibility into them. Real-time availability, booking write-back, and patient records are greenfield for the app (via Nixpend integration, aligned with the AIWA/AIKA deployments).

### 4.6 Friction points in today's journey (framed as opportunities)
1. **Channel switch at the moment of intent** — every Book Now exits the branded experience into WhatsApp/portal; context (which service, which page) is not carried over except the FAB's generic pre-filled text.
2. **No availability signal** — users can't see if/when a therapist can come; "We reach you within 2 hours of booking confirmation" is stated but not demonstrable.
3. **No confirmation artifact** — no booking reference, no calendar entry, no reminder (the vocabulary for these already exists).
4. **No payment path** — prices exist for 8 services but there's no way to pay; insurance list exists but is never collected.
5. **No account/history** — returning patients restart from zero every time; no recovery progress, no session count, no care-plan continuity.
6. **Two competing booking destinations live simultaneously** (wa.me vs Nixpend portal) — a natural consolidation point for the app + AIWA.

---

## 5. Existing UX Patterns & Component Inventory

- **Layout primitives:** `Navbar` (transparent→solid scroll morph, gold top hairline), `MobileMenu` overlay, `PromoStrip`, `Footer`, `WhatsAppButton` FAB, `LiveChatWidget` (mock), `Logo` (size/light variants).
- **Section grammar (repeated on every page):** eyebrow chip (`section-eyebrow`: 0.625rem, letter-spacing 0.45em, uppercase, gold) → large light-weight headline with one **gold-shimmer italic highlight word** (CMS `highlightWord` pattern, `dangerouslySetInnerHTML` rich text) → hairline gold divider (`GoldDivider`, `luxury-divider`) → body copy at white/40–55 opacity.
- **Cards:** `luxury-card` / `glass-card` / `deep-glass` (navy glassmorphism, 1px gold borders at 10–15% opacity, hover lift −4px + gold border glow), `pkg-card-3d` (hover rotateX), image cards with bottom-fade navy gradient, corner ornaments (`corner-ornament-tl/br`, L-shaped gold brackets).
- **Buttons:** `luxury-button-gold` (gold with woven-fabric SVG texture blended `soft-light` — echoes the linen weave in the logo — plus sweep-shine on hover), pill-shaped, tiny uppercase tracking-[0.3em] labels; secondary = ghost white/15 border pill; WhatsApp buttons always carry the WA glyph.
- **Decorative identity layer (unique):** `caligraphy/ArabicDecor.tsx` + `NajdiPalaces.tsx` — FloatingIslamicStars, MuqarnasRow, ArabesqueCorners, RoyalPalaceGate, DiriyahPalace, MasmakFort, NajdiTower, OldRiyadhRow — Najdi-heritage silhouettes at 8–18% opacity behind sections; `arabic-calligraphy-watermark` (giant outlined Arabic word, 22vw, gold stroke at 4.5%).
- **Motion:** GSAP entrance timelines (staggered fade-up, `back.out` pops), ScrollTrigger reveals (`ScrollReveal` wrapper), marquee (react-fast-marquee), CountUp stats, `animate-float`, `pulseGold`, `subtleZoom` on hero imagery, `goldScan` sheen sweeps, `ambientBreath`/`luxuryOrb` background orbs. WhatsApp FAB pops in after 2s.
- **Numbered-list pattern:** service detail renders "Board-Certified" items as a ledger table with giant gold index numerals; preparation steps as cards with ghost numerals (5.5rem at 5% gold) and a gold left rule.
- **Forms:** shadcn-style `ui/` primitives (button, card, input, label, textarea) — minimal; admin side uses MUI + notistack + react-quill. Public forms are rare (contact, careers only).
- **RTL discipline:** `dir` set per component; logical properties; critical rule `[dir="rtl"] * { letter-spacing: 0 !important }` (WebKit Arabic-joining fix); `html[lang="ar"] * { font-family: Noto Sans Arabic !important }`.
- **Accessibility notes for the app team:** heavy reliance on 6.5–10px uppercase micro-labels, low-contrast white/30–50 body text on navy, and `dangerouslySetInnerHTML` CMS rich text — premium look, but the app should raise the accessibility floor (type sizes, contrast) while keeping the aesthetic.

---

## 6. Brand Analysis — exact tokens

### 6.1 Color system (`globals.css @theme`)
| Token | Hex | Role |
|---|---|---|
| `--color-navy` | **#001C3D** | Primary surface (brand navy) |
| `--color-navy-dark` | **#001229** | Deep sections, page bg |
| `--color-navy-light` | **#002B5B** | Elevated navy |
| `--color-navy-50` | #E8EDF5 | Light tint |
| `--color-gold` | **#C5A059** | Brand gold — CTAs, accents, eyebrows |
| `--color-gold-light` | #D4B67C | Hover gold |
| `--color-gold-pale` | #F9F3E8 | Pale gold wash |
| `--color-gold-muted` | #9E7D41 | Muted gold |
| `--color-ivory` | #F7F5F0 / `--color-ivory-warm` #F0EBE0 | Light surfaces |
| `--color-charcoal` | #1A1A2E | Dark neutral |
| WhatsApp green | #25D366 | FAB only |

Gradients: gold `135deg #C5A059 → #D4B67C → #C5A059`; hero `135deg #001229 → #001C3D 60% → #002B5B`; shimmer text `#C5A059 → #F0D98A → #C5A059 → #A88A3D` (a secondary gold family #C9A84C/#F0D98A/#A88A3D appears in shimmer/scrollbar). Shadows: `--shadow-gold: 0 8px 40px rgba(201,168,76,0.15)`, card `0 10px 40px rgba(7,21,38,0.3)`. Scrollbar: navy track, gold thumb. Selection: gold at 30%.

### 6.2 Typography
| Font | Loading | Role |
|---|---|---|
| **Termina** (with Syne fallback) | CDN import (fonts.cdnfonts.com) | All headings h1–h6, weight 300, letter-spacing −0.01em, line-height 1.15 |
| **Montserrat** 300–900 | next/font Google | Body (default weight 300, ls 0.01em), buttons/labels |
| **Noto Sans Arabic** 300–900 | next/font Google | Forced on every element when `lang="ar"` |
| **Aref Ruqaa** 400/700 | next/font Google | Arabic calligraphy accents |

Scale in practice: hero `clamp(2.4rem, 5.5vw, 4.2rem)` up to 7xl display; section h2 ~1.75rem font-black −0.02em; body 0.82–0.93rem; micro-labels 6.5–10px uppercase, tracking 0.2–0.45em. Signature contrast: ultra-light display headings + tiny ultra-tracked uppercase labels + gold-shimmer italic highlight words.

### 6.3 Imagery, iconography, texture
- Photography: real in-home clinical shoot (DSC*.jpg — nurse visits, physio sessions, at-home care), warm and human; some CMS uploads are AI-generated (Gemini_Generated_Image_*.png for nursing micro-services) — inconsistency to resolve in app art direction.
- Icons: **lucide-react** throughout (Calendar, Clock, ShieldCheck, MessageCircle, Star, Sparkles, Crown, Activity, Heart…); tier icons: Shield=essential, Sparkles=advanced, Crown=elite, Activity=service, Star=program.
- Texture: woven-linen SVG turbulence texture (from the logo mark) blended into every gold button; global film-grain overlay (`grain-overlay`, 3.5% noise); dot-matrix radial gold grids (40–44px spacing) behind sections.
- Trust badges: five-star rows, "MOH Accredited", "Certified Care", ShieldCheck chips everywhere.

### 6.4 Brand facts (constants.ts)
- Company: **Vitality Home Healthcare / فيتاليتي للرعاية الصحية المنزلية**; part of **Burjeel Arabia Healthcare Network** (about copy).
- WhatsApp **+966 50 444 7658**; hotline **920022827**; email Info@vitality.com; HQ **Riyadh, An Nakheel District**; hours **Sat–Thu 10 AM–10 PM, Friday closed** (in tension with "Available 24/7" trust badges — the app should reconcile service hours vs hotline hours).
- Socials: instagram/facebook/x/linkedin/tiktok @myvitality.sa (live footer also shows YouTube, Snapchat).

---

## 7. Tone of Voice & Content Strategy (messages/ EN + AR)

**Register:** premium-clinical-warm. Physician-led authority + concierge hospitality + family warmth. Never casual, never salesy; superlatives are about care quality, not discounts.

**Key phrases & taglines (exact):**
- Hero: **"Advanced Medical Care… Comfortably at Home" / "رعاية طبية متقدمة… براحة في منزلك"** (the ellipsis-pause is a signature device)
- Badge: "Premium Home Healthcare · Riyadh" / "رعاية صحية منزلية متميزة · الرياض"
- "Experience a new standard of home healthcare with Vitality—where expert medical care meets comfort, convenience, and compassion."
- Why: **"We don't just provide a service — we deliver an exceptional care experience" / "نحن لا نقدم خدمة — نحن نقدم تجربة رعاية استثنائية"**
- Trust triplet: "Physician-Led Care" · "Available 24/7" · "MOH Accredited"
- Feature proofs: "We reach you within 2 hours of booking confirmation", "Complete health monitoring via detailed digital reports", "Medical support hotline open 24 hours, 7 days a week"
- Testimonials header: "Thousands of families trust us" / "آلاف العائلات وثقت بنا"
- Footer tagline: "Premium home healthcare in Riyadh"
- Live-site taglines (About/CMS): **"A Pain-Free Path To Wellness"**, "Care Delivered at Your Convenience", "The Service You Deserve Beyond Imagination", "We believe true healthcare begins at home, where medical expertise meets family warmth, ensuring you are always safe.", philosophy quote "We believe that true healthcare begins with trust and compassion at every step." — Dr. Amr Alrabiee, Medical Director
- Vision/Mission (content.ts): "To become the leading international health and wellness provider." / **"To guide our members to discover wellbeing through an integrative medical approach."** — note **"members"**, not patients: the membership/wellness-companion framing already exists in the client's own mission.
- Home section titles (live): "How It Works", "Our Premier Services", "Beauty & Wellness", "Vitality.. Your Partner in Wellness", **"Clinical Path to Wellness"**, "Medical Elite", **"Our Promise — Uninterrupted Care"**.

**Arabic voice:** formal MSA, warm and dignified — "براحة في منزلك" (in the comfort of your home), "رعاية يومية حانية" (tender daily care), "لضمان تعافٍ آمن وسريع". Family-oriented (رعاية كبار السن، إرشادات للعائلة). Testimonials use authentic Saudi names (أم محمد، عبدالله الشمري، هدى العنزي).

**Content strategy today:** trust-building (credentials, stats: 98% satisfaction, 25K+ patients, 2h response, 15+ years, 200+ staff) + service education (includes/preparation lists) + editorial blog ("News & Health Tips"). Everything funnels to one CTA: Book Now → WhatsApp.

---

## 8. Physiotherapy & Home Healthcare Workflows — as presented today

- **Physiotherapy** is one card among nine, yet the team page leads with it: 2 of 3 featured staff are physio (Talal Almufi, "Head of Physiotherapy", 12 yrs, orthopedic; Areeba Sheraz, "Senior Rehabilitation Specialist", 10 yrs, post-surgical + geriatric, EN/AR/Urdu). Detail page promises: Post-Surgery Rehabilitation, Sports Injury Recovery, Orthopedic Therapy, Neurological Physiotherapy, Customized Exercise Plans, Posture Correction, Progress Monitoring — **plans and progress are promised but nothing tracks them**; sessions are 45–60 min.
- **The care journey is already storyboarded** — `RecoveryPath` "Clinical Path to Wellness" 6 steps: **Book Your Visit → Expert Consultation → Full Assessment → Tailored Care Plan → Professional Treatment → Vitality Recovery** (احجز موعدك → استشارة الخبراء → تقييم شامل → خطة رعاية مخصصة → علاج احترافي → استعادة النشاط). This is a narrative graphic only; the app can make it the literal patient state machine.
- **Nursing/home healthcare** is presented as coordination-first: "full coordination with treating physicians to ensure continuity of care" — continuity is the core promise, delivered operationally via Nixpend, invisible to the patient digitally.
- **Chronic/elderly**: Home Care Plus + Diabetes Care programs describe recurring workflows (daily monitoring, insulin, 24/7 hotline, foot care) — inherently longitudinal, sold as single "sessions".

---

## 9. Wellness Programs — what's wellness-positioned today

- **Explicit wellness inventory:** IV Vitamin Therapy ("boost energy… enhance overall wellness"), HydraCool Therapy, Beauty at Your Fingertips, Venus Legacy body contouring, Lymphatic Recovery Therapy, Mesotherapy, **Glow Program**, **Shape It Program**, Health Check at Home ("Personalized health insights"), Ramadan Wellness Special.
- **Wellness language saturates the brand even for clinical services:** about overview calls Vitality "a leading **wellness** provider"; mission "guide our **members** to discover **wellbeing** through an **integrative medical approach**"; home sections "Beauty & Wellness", "Your Partner in Wellness", "Clinical Path to Wellness"; programs SEO "curated health and wellness programs tailored for your home".
- **Gap:** wellness is a *category of treatments*, not yet a *continuous companion experience* — no assessments, streaks, plans, content programs, or progress. The brand promise ("partner in wellness", "members") is ahead of the product; the app closes that distance. This is the strongest possible foundation for the "wellness companion, not a patient portal" positioning — it's literally the client's existing mission statement.

---

## 10. Emotional Positioning — current feeling vs. target feeling

**What the site makes users feel now:** *impressed and reassured before booking.* Dark navy + gold + Najdi heritage silhouettes + grain = a five-star-hotel lobby; credentials, stats and shield icons manufacture trust; the woven texture and Arabic calligraphy signal cultural belonging. The register is **prestige + safety**.

**Emotional curve today:** high at discovery (luxury, trust) → drops at booking (ejected to a WhatsApp chat with no context) → blind spot between booking and door-knock (no confirmation object, no therapist identity, no ETA) → warm during the visit (per testimonials: "on time, professional and caring", "made my recovery smooth") → silence after (no follow-up surface; recovery progress invisible).

**Target feeling for the app:** relief ("help is arranged and I can see it"), comfort ("I know who is coming and when"), hope ("I can see my recovery moving"), continuity ("Vitality remembers me"). The brand already *speaks* these ("Uninterrupted Care", "Continuous Support", "Vitality Recovery", "Tailored Care Plan") — the app's job is to make each phrase a screen: booking → confirmation card; 2h response → live ETA; digital reports → results timeline; care plan → visible plan with progress; recovery → milestones celebrated in gold.

---

## 11. Gap Analysis — opportunities & natural next maturing steps

*(All items are the normal maturing steps of a digital healthcare brand at this stage — the website has done its job as a premium trust-builder; the app is the logical next chapter.)*

| # | Opportunity | Today | App vision |
|---|---|---|---|
| 1 | **Native booking** | All CTAs hand off to WhatsApp/portal; complete 4-step booking vocabulary already written & translated but unshipped | In-app service→slot→details→confirm flow, powered by Nixpend availability + write-back; AIWA/AIKA as sibling channels on the same backbone |
| 2 | **Live availability & ETA** | "2h response" stated, not shown; TIME_SLOTS constant dormant | Real slots from Nixpend roster (~30 therapists), therapist profile + live ETA on visit day |
| 3 | **Patient identity & continuity** | No accounts, no history; mission already says "members" | Member profile, family members (elderly-care proxy booking), visit history, care team memory |
| 4 | **Care-plan & recovery tracking** | "Tailored Care Plan", "Progress Monitoring", "Digital Reports" promised in copy; RecoveryPath is a 6-step graphic only | Make RecoveryPath the literal in-app journey: plan, session countdown (e.g. "session 4 of 12"), exercise adherence, milestone celebrations |
| 5 | **Payments & insurance** | 8 services priced 250–389 SAR but no checkout; insurance list (Bupa, Tawuniya, MedGulf, Al-Rajhi Takaful, AXA) never collected | In-app payment (Mada/Apple Pay), transparent pricing, insurance capture, package/subscription purchase (perMonth vocabulary + tier ladder essential/advanced/elite already reserved) |
| 6 | **Wellness companion layer** | Wellness is a treatment category; blog is the only content surface | Assessments, personalized programs (Glow, Shape It as journeys), reminders, health content in AR/EN, IV/physio maintenance nudges |
| 7 | **Post-visit loop** | No follow-up surface; testimonials collected off-channel | Ratings, digital visit reports, re-booking prompts, hotline/AIKA escalation button |
| 8 | **Unified messaging** | Mock LiveChatWidget UI; WhatsApp FAB; two booking destinations | AIWA-powered in-app chat + WhatsApp continuity; one booking brain across app/web/voice |
| 9 | **Real service taxonomy & discovery** | Category tags shuffled/decorative; no search or filters; district list static | Clean clinical taxonomy, symptom/need-based finder, coverage-aware district selection (~15 districts) |
| 10 | **Notifications & confirmation artifacts** | "Booking Confirmed Successfully!" + "Booking Reference" strings exist with no flow | Push/WhatsApp confirmations, calendar add, reminder cadence, arrival alerts |

---

## 12. Current User Journey Map (end-to-end, with emotional curve)

| Phase | Touchpoints today | What happens | Emotion |
|---|---|---|---|
| **Discover** | Instagram/TikTok @myvitality.sa, Google, word of mouth → vitality.sa | Luxury navy/gold hero "Advanced Medical Care… Comfortably at Home", 98%/25K+/2h/24-7 stats, MOH badges | ↑ High: impressed, reassured — "these people are serious" |
| **Browse** | Services grid → service detail; Programs grid → program detail; team, testimonials, blog | Rich bilingual education: includes, board-certified lists, personalised care, preparation guide; "Most Popular" badge steers to Post-Surgery Recovery | ↑ Confident, informed; ↓ small dip: almost no prices, no availability — "but when can they come, and what does it cost?" |
| **Decide → Book** | Any of ~8 Book Now surfaces | Ejected to WhatsApp (966504447658) with generic pre-filled text, or to patients.nixpend.com; conversation restarts from zero; back-and-forth on service, address, time, price | ↓ Low: channel switch, uncertainty, effort. Everything from here is human-operated and invisible to the site |
| **Wait** | WhatsApp thread, phone 920022827 | Confirmation, scheduling and any payment arranged manually; no booking reference, reminder, or therapist preview | ↓ Anxious blind spot — "is it actually confirmed? who is coming?" |
| **Visit** | Therapist/nurse at home (Nixpend-scheduled) | Per testimonials: punctual, professional, caring ("The nurse arrived on time… My mother recovered much faster than expected") | ↑ Peak: relief, gratitude, trust earned in person |
| **Recover / repeat** | Nothing digital; maybe a WhatsApp follow-up | No report, plan visibility, exercise support, or progress view between sessions; re-booking = restart the WhatsApp dance | ↓ Fade-out: goodwill exists but has no home; loyalty is person-dependent, not product-supported |
| **Advocate** | Testimonials page, social | 5-star reviews exist, gathered manually | flat — untapped referral energy |

**Journey verdict:** the brand wins the *pre-booking* emotional game decisively and the *in-home* moment is its proudest asset; the entire digital middle (book → wait → recover) is a manually-bridged gap. The mobile app should own exactly that middle, wrapped in the already-proven navy/gold "quiet luxury meets Najdi heritage" identity, and speak the six words the site already promises: **Book, Consult, Assess, Plan, Treat, Recover.**

---

## Appendix A — Key file map (for downstream workstreams)
- Brand tokens: `src/app/globals.css` (@theme + luxury utilities), `src/lib/fonts.ts`
- Content: `src/data/content.ts` (canonical client copy), `src/messages/{en,ar}.json` (UI strings incl. dormant booking wizard), `src/data/{services,packages,promotions,team,testimonials,serviceMap}.ts`
- Booking constants: `src/lib/constants.ts` (WhatsApp, phone, districts, time slots, insurers, hours)
- Journey narrative: `src/components/home/RecoveryPath.tsx`; conversion: `src/components/home/BookingCTAStrip.tsx`, `src/components/services/ServiceDetailContent.tsx`
- Native form + API: `src/components/contact/ContactInterface.tsx`, `src/app/api/enquiry/route.ts`
- CMS models: `src/lib/models/*` (Program.ts defines tier/pricing/includes schema the app can mirror)

