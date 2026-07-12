# Vitality Home Care — App Experience Model & Feature Architecture

**Document 04 — Experience Model & Feature Architecture**
**Client:** Vitality Home Care (vitality.sa) — premium home healthcare, Riyadh, KSA
**Prepared by:** CodeOx — Shabeeb Kaip, Head of Operations · shabeeb.k@code-ox.com · +966 53 571 6437
**Date:** 9 July 2026
**Inputs:** Document 01 (Discovery), Document 02 (Benchmarking & Pattern Library), Document 03 (Product Strategy)
**Feeds:** IA & navigation, onboarding, booking, progress & retention, family circle, visual design workstreams. This document turns the strategy into the screen-level experience contract and the complete, prioritized feature inventory.

---

# PART A — APP EXPERIENCE MODEL

## A1. The Experience Principle — how the app opens

**The app never opens on medical reports, appointment lists, or documents. It opens on a person, a journey, and one warm sentence.**

This is the single binding rule from which every home-screen decision derives (Pillar 1: companion-first, never portal). The moment of app-open is the product's most repeated emotional event — for Abdulrahman it may happen five times a day in week one after surgery. Each open must lower the heart rate, not raise it (Calm's lesson). Sehhaty, Sanar, and Thaat all open on grids and tasks; Vitality opens on care.

**The emotional hierarchy of the home screen — in strict priority order:**

1. **A person** — the matched caregiver as recurring character: her face, her name, her presence. Once matched, the app's center of gravity is "your physiotherapist Areeba," never a service catalog.
2. **A resolution** — the top card always answers today's biggest open question before showing any data: *"Amal is confirmed for tomorrow, 4pm."* Status before detail, relief before information (Emotional Design Goal 1).
3. **A journey** — the session-dot journey and progress ring: where you are in the story, visibly moving toward a named finish line ("Walking unaided").
4. **A voice** — the narrated recovery score and encouragement messages: warm Arabic-first sentences, never grades, never raw numbers.
5. **Everything else** — booking, records, content, settings — lives one level down, reachable in one tap but never shouting.

**Corollaries (the standing veto list, from the 12 anti-patterns):** no service-grid above the fold, ever; no alarm-red for routine items; no Nixpend workflow states visible ("request #4832 pending" is forbidden vocabulary); maximum three elements above the fold; greeting is time-aware and name-aware ("مساء الخير أبو خالد"); notifications on this surface are invitations, never demands.

---

## A2. Home Screen Concept — the adaptive companion canvas

The home screen is a single vertical canvas of **named modules** that reorder, appear, and retire based on the member's care state. The layout logic is app-side; the facts feeding it (bookings, plan state, roster) come from Nixpend. Nine modules:

| Module | What it is | Pattern source |
|---|---|---|
| **M1 · Companion Header** | Time-aware greeting + caregiver presence (photo, name, "your physiotherapist"), soft navy-to-dawn gradient, Najdi silhouette at low opacity | Pattern 16 (ambient home), Pattern 4 (recurring character) |
| **M2 · Recovery Progress** | The session-dot journey for the active care plan — dots filled, current session glowing gold, finish line named in life terms — plus the daily progress ring (exercises ✓, check-in ✓, walk ✓) | Patterns 3, 7 |
| **M3 · Daily Wellness Score** | The narrated recovery score: one number rendered small, one warm sentence rendered large — "جسمك يحتاج راحة اليوم — خذها." Never a grade, always guidance | Pattern 2 |
| **M4 · Today's Care Plan** | Today's one-to-three actions as gentle cards: this morning's exercises (opens the exercise player), the check-in if not done, medication or hydration nudge from the plan | Pattern 11 |
| **M5 · Encouragement Messages** | The encouragement engine's slot: context-aware warm copy — after a completed ring, after a hard day, before a visit. Written in the care-tone guide voice, first person as the care team | Emotional Goal 3 |
| **M6 · Therapist Check-in Card** | The relationship surface: last message from the care thread, "Areeba replies within 3 hours, 9am–9pm," one-tap into the thread; on visit day it transforms into the **en-route status card** (photo, ETA, license badge, ID for the gate) | Patterns 6, 12 |
| **M7 · Recovery Milestones & Celebrations** | Upcoming and just-earned milestones; earned ones trigger the full-screen gold celebration (major ones carry the caregiver's voice note); shareable to the Family Care Circle | Pattern 8 |
| **M8 · Personalized Recommendations** | Quiet, cadence-aware: Arabic content shelf picks ("sleeping after knee surgery"), maintenance nudges ("your quarterly health check is due — same nurse?"), wellness program suggestions post-graduation. Never promotional | Pattern 17 |
| **M9 · Family Support Glimpse** | For patients: who's watching with you ("Noura celebrated your milestone"); for family coordinators: the dependent's week at a glance. Respects per-datatype privacy always | Pattern 14 |
| **M10 · Motivation System strip** | Streak-with-mercy indicator woven into M2's ring rather than a separate badge wall — streak weeks shown as soft gold marks, repair always one tap, Ramadan-aware | Pattern 9 |

### A2.1 The Adaptive State Model — the heart of the app

The home screen has five states. State detection is driven by Nixpend facts (does a booking exist? is a care plan active? is today a visit day?) plus app-side facts (is this a family-member session?). Module order per state is normative — downstream IA must implement exactly this.

---

**STATE (a) — New member, no booking yet** · *"They listened before they asked."*

The one state where no caregiver exists yet — so the app leads with warmth and the path to the match, never a form or a grid.

| Order | Module | Behavior in this state |
|---|---|---|
| 1 | M1 Companion Header | Greeting + the brand promise line: "رفيقك في التعافي — your companion in recovery" |
| 2 | **Match invitation card** (pre-state of M6) | "Tell us what brings you here — we'll find your specialist." Opens the conversational intake → gender preference first → **match reveal**. This card IS the home screen's hero |
| 3 | M3 (lightweight) | A gentle first check-in offer: "How are you feeling today?" — value before identity, feeds a first narrated sentence |
| 4 | M8 Recommendations | Three warm entry points by need, not by service name: "Recovering after surgery," "Caring for a parent," "Everyday wellness" — services live behind these, one level down |
| 5 | M9 Family glimpse (invitation) | "Caring for someone else? Set up their circle" — activates the Noura path early |

*Never in this state:* prices, insurance fields, records, account creation walls. Registration is deferred until booking requires it (Anti-pattern 2).

---

**STATE (b) — Booking confirmed / visit day** · *"I know exactly who is coming, and when."*

| Order | Module | Behavior |
|---|---|---|
| 1 | M1 Companion Header | Caregiver-forward: her photo large, "Amal — your nurse" |
| 2 | **M6 as en-route status** | Pre-visit: confirmation artifact card (reference, date/time, calendar add, T-24h preparation checklist from the site's existing prep guides). Visit day: live en-route card — photo, name, license badge, ETA countdown, vehicle/ID for compound gates. The "2 hours" promise becomes a countdown |
| 3 | M4 Today's Care Plan | Pre-visit intake nudge if incomplete ("Amal will know about your C-section history — nothing to repeat") |
| 4 | M2 Recovery Progress | If a plan exists: the dot for today's session glowing "today" |
| 5 | M3 Daily Wellness Score | Present but quiet — visit day belongs to the visit |
| 6 | M9 Family glimpse | "Noura can see the visit is confirmed" (if shared) |

---

**STATE (c) — Mid-recovery program** · *"I'm getting better, and I'm not doing it alone."* **The app's center-of-gravity state.**

| Order | Module | Behavior |
|---|---|---|
| 1 | M1 Companion Header | Warm, familiar, brief |
| 2 | M2 Recovery Progress | Full glory: session dots (e.g., 4 of 12 filled), named finish line, today's ring |
| 3 | M3 Daily Wellness Score | The morning anchor — narrated from today's check-in |
| 4 | M4 Today's Care Plan | Exercises (player), check-in, plan actions |
| 5 | M6 Therapist Check-in | Thread preview + next session date |
| 6 | M7 Milestones | Next milestone visible ("3 sessions to halfway"); celebrations interrupt full-screen when earned |
| 7 | M5 Encouragement | Context slot — fires on ring close, streak weeks, hard days |
| 8 | M8 Recommendations | One relevant content pick, max |

---

**STATE (d) — Program complete / wellness maintenance** · *"I finished something — and they're still with me."*

| Order | Module | Behavior |
|---|---|---|
| 1 | M1 Companion Header | "Areeba is still your physiotherapist — message anytime." The relationship never closes |
| 2 | M7 Milestones (graduation recap) | The completed journey, all dots lit; the evidence recap (where you started → where you are); the caregiver's congratulation note, shareable |
| 3 | M3 Daily Wellness Score | Continues as the daily heartbeat — recovery score matures into a wellness score |
| 4 | M8 Recommendations | The wellness shelf steps forward: Glow/Shape It as journeys, quarterly health-check cadence nudges, Arabic content |
| 5 | M2 (maintenance ring) | Lighter daily ring — movement, check-in — no session dots unless a wellness program journey is active |
| 6 | **2-tap rebook card** | "Book Amal again?" — my usual, saved preferences, eleven seconds (Lama's state) |

---

**STATE (e) — Family-member view (coordinator session)** · *"I stopped being the app."* Noura's home screen, structurally distinct.

| Order | Module | Behavior |
|---|---|---|
| 1 | M1 (family variant) | "مساء الخير نورة" + the circle: mother's profile card front and center |
| 2 | **M9 as Family Dashboard** | The dependent's week at a glance — visits done, ring days closed, caregiver's note ("ضغطها مستقر هذا الأسبوع") — showing ONLY what the patient has shared, with an honest "some items are private" state |
| 3 | M6 (proxy variant) | Next visit for the dependent + en-route forwarding on visit days |
| 4 | **Booking-on-behalf card** | Book/renew for mother: saved entry notes, female-caregiver guarantee locked, package renewal, pay |
| 5 | M7 (shared celebrations) | Milestones the patient chose to share — the good-news channel that replaces the chasing phone call |
| 6 | Circle management | Invite brother, manage payment, sharing summary (read-only view of what mother controls) |

*Never in this state:* private check-in data (mood, pain detail) unless explicitly shared per-datatype; any implication of surveillance — the dashboard shows care happening, not the patient being watched.

---

## A3. The Daily Emotional Loop — three 30-second rituals

The loop gives the app a daily reason to exist between visits. Every interaction is designed for 30 seconds, one hand, interruptible (Reem's constraint). All times prayer-aware and configurable; all steps skippable without shame.

**☀️ Morning — the Check-in Ritual (after Fajr-friendly hours, member-configured)**
Push written as an invitation ("صباح الخير — كيف جسمك اليوم؟"). Open → three soft sliders: pain, mood, sleep → one tap done. The app answers immediately with the **narrated recovery score**: "قراءاتك أهدأ من أمس — يوم لطيف على نفسك" — steadier than yesterday, be gentle with yourself. Red-flag inputs route quietly to the care team (and AIWA follow-up) without alarming the member — Saleh is reassured, the nurses are alerted. Total: 30 seconds, and the member leaves knowing "is this normal?" is answered.

**🌤 Day — Guidance (ambient, pull-based)**
The home screen carries the day: today's exercises in the player (5–10 minute interruptible chunks, Arabic voiceover), the ring filling with each action, the care thread open for the swelling photo. No midday pushes by default — presence, not pestering. On visit days the loop yields to the en-route ritual.

**🌙 Evening — Reflection (before Isha or member-set)**
If the ring closed: a micro-celebration and one warm line ("closed five days this week — your body notices"). If it didn't: mercy, never a red X — "rest was probably what you needed; we try again tomorrow," streak intact via rest-day logic. One optional question on active plans ("how did today's exercises feel?") feeds the adaptive plan and tomorrow's narration. Thursday evenings, the weekly recap lands here — timed for family day, shareable to the circle.

---

## A4. Motivation System — celebration, evidence, and merciful streaks

Four interlocking mechanics, all app-native (zero Nixpend dependency beyond plan facts):

**1. Milestones.** Every care plan compiles into a milestone ladder at plan creation: first session, first week, halfway, personal-goal moments (first unaided walk), final session. Wellness programs (Glow, Shape It) get the same ladder. Milestones are named in life terms, never clinical ones — "Walking to the majlis," not "mobility target 2."

**2. Celebration moments.** Milestone reached → full-screen gold moment on brand (navy, gold shimmer, woven-linen texture — the website's celebration language brought to motion). Major milestones (halfway, graduation) unlock a **caregiver-recorded voice/video note** — "Sara sent you a voice note: congratulations on session 10." Unforgeable premium; no GCC competitor can copy it with a service menu. Celebrations are shareable to the Family Care Circle in one tap (patient's choice), converting private progress into family pride — Abdulrahman shows his sons he's improving.

**3. Outcome evidence.** The longitudinal chart of the member's own pain/mobility/adherence across sessions — "Pain down 40% since session 1" — reviewed together with the caregiver at each visit (Sword's loop). Evidence is always narrated, plateaus framed as part of the story. This is the renewal engine: members renew what they can see working.

**4. Streaks with mercy — culturally tuned.** Adherence streaks reward consistency but are engineered to never shame: built-in rest days, one-tap streak repair ("bad pain day? your streak is safe"), and compassionate miss-copy from the care-tone guide. **Ramadan mode** is first-class: shifted check-in windows (post-Iftar, post-Taraweeh), adjusted exercise/hydration guidance, streak logic that treats fasting days generously, Ramadan-specific encouragement copy written natively in Arabic. Friday is a natural rest day by default. Gamification never uses compliance percentages, red marks, or leaderboards — the only competitor is yesterday's pain.

---

# PART B — FEATURE ARCHITECTURE

Every feature traces to at least one strategic pillar (P1–P5) and serves named personas (A=Abdulrahman, N=Noura, S=Saleh, L=Lama, R=Reem). Dependencies: **NX** = Nixpend HMS, **AIWA** = WhatsApp AI, **AIKA** = voice AI, **App** = app-native. MoSCoW: M/S/C/W.

## Layer A — CORE EXPERIENCE (booking & transactions)

| # | Feature | Description | Personas | Emotional purpose | Dependency | MoSCoW |
|---|---|---|---|---|---|---|
| A1 | **Native 4-Step Booking Wizard** | The dormant, client-approved booking vocabulary in the codebase finally shipped as UI: Select Service → Date & Time (real Nixpend availability, prayer-time-aware slots) → Your Details (patient, address, district, notes, insurance) → Payment → confirmation artifact with booking reference, caregiver card, calendar add, reminder cadence. Pre-visit intake folded in comfortably. The site's "Secure & Encrypted Booking" microcopy becomes literally true. | All | Relief + confidence — "that was effortless, and it's truly arranged" | NX (availability read, booking write) | **M** |
| A2 | **Package & Program Booking** | Flagship programs (Post-Surgery Recovery, Home Care Plus, Diabetes Care) bookable as multi-session journeys, not one-offs: program overview, inclusions, quote-request or transparent pricing, and — on confirmation — the care plan instantiated as a session-dot journey. The tier ladder (essential/advanced/elite) the codebase reserves matures here into memberships in v2. | A, N, S | Hope — buying a journey with a visible ending, not a series of appointments | NX (program setup, plan state) | **M** |
| A3 | **Home Physio Booking with Therapist Matching** | The BetterHelp-grammar intake: gender preference first (guaranteed forever — a hard requirement, not a filter), language, specialty, style ("encouraging coach" / "gentle and patient") → theatrical "finding your specialist…" → the **match reveal**: a named human with photo, credentials, years, specialty, 20-second intro video. Same-caregiver guarantee within a plan; guilt-free "request a different specialist" with an explicit gender-change path. Never a directory of 40 cards. | R, A, L | The app's first emotional peak — being listened to, then met by a person | NX (roster read, assignment write) | **M** |
| A4 | **Home Visit Scheduling with District Coverage** | Riyadh district picker (the 12-district constant already written), coverage-aware slotting, saved addresses with home-entry notes ("family section entrance, call before arriving"), household protocol capture (male-caregiver-requires-mahram flags). Visit-day en-route status lives in Layer D's sibling card. | All | Comfort — the sacred home threshold respected before the doorbell | NX (coverage, scheduling) | **M** |
| A5 | **2-Tap Rebooking & Favorites ("My Usual")** | Zeel's grammar: after every visit, one card — "Book Amal again, same time next week?" Saved rituals: caregiver, gender, service, address, entry notes, payment method. Lama's eleven-second Thursday-night booking. Favorites extend to family dependents ("mother's usual nurse"). | L, N, S | Care — being remembered is the luxury; never restart from zero | NX (booking write) + App (preferences) | **M** |
| A6 | **Payments & Insurance** | Mada + Apple Pay mandatory, Tabby/Tamara installments for large post-surgical packages, STC Pay fast-follow; transparent pricing for the 8 priced services (250–389 SAR) finally shown and payable; insurance capture (Bupa, Tawuniya, MedGulf, Al-Rajhi Takaful, AXA) at booking with CHI-linkage readiness on the roadmap; receipts and payment history; cash-on-visit as an explicit policy toggle. | All (N pays for others) | Confidence — premium means no money awkwardness at the door | NX (pricing, invoicing) + payment gateway | **M** (Tabby **S**) |
| A7 | **Member Profile & Care Memory** | Deferred-until-booking identity (biometric unlock thereafter; step-up auth only for payments/records), profile with conditions context, visit history as a warm timeline (not a records cabinet), returning-member recognition ("Welcome back, Abu Khalid — how is the knee?"). | All | Care — "Vitality remembers me" | NX (patient record link) + App | **M** |

## Layer B — WELLNESS EXPERIENCE (plans, tracking, progress)

| # | Feature | Description | Personas | Emotional purpose | Dependency | MoSCoW |
|---|---|---|---|---|---|---|
| B1 | **Daily Recovery Plans** | The active care plan rendered as the website's "Clinical Path to Wellness" made literal: today's actions (exercises, check-in, medication/hydration nudges) as Today's Care Plan cards, sourced from the physio-authored plan in Nixpend, presented one day at a time — the day has a shape (Headspace's Today model). | A, S, R | Relief — "I know exactly what today asks of me" | NX (plan read) + App (presentation) | **M** |
| B2 | **Guided Exercise Player** | Physio-prescribed home program: video demo (by the member's own therapist where possible), Arabic voiceover, guided timer, landscape floor-exercise mode, 5–10 minute interruptible chunks, then "how did it feel?" (pain/difficulty) adapting the next assignment. Kaia's player UX without the CV; camera-guided form feedback is a v2+ candidate. | R, A | Confidence — "I'm doing it right, even alone" | App (content) + NX (prescription) | **M** (CV feedback **W** for now) |
| B3 | **Wellness Tracking — Daily Check-ins** | The 30-second morning ritual: pain, mood, sleep sliders. Feeds the recovery score, the ring, the outcome evidence, and — on red flags — quiet care-team routing via Nixpend/AIWA without alarming the member. Prayer-time-aware scheduling; Ramadan-shifted windows. | S, A, R | Emotional support — checked on daily, policed never | App (native) + NX (red-flag write) | **M** |
| B4 | **Progress Visualization — Ring, Dots, Evidence** | The three progress instruments: daily progress ring (Apple grammar, closes with micro-celebration), session-dot journey per plan (current dot glowing, finish line named), and outcome evidence charts ("pain down 40% since session 1") reviewed with the caregiver at visits. Widget-ready. | A, S, R, N (view) | Hope — progress made visible and narrated | App + NX (session facts) | **M** |
| B5 | **Narrated Daily Wellness Score** | One readiness number computed from check-in inputs (no wearable required), always subordinate to its sentence: warm Arabic-first interpretation in the Oura voice — "جسمك يطلب راحة اليوم — خذها." Rest days framed as achievements. Never a grade, never alarm-red. | S, A, L | Comfort — data delivered as a caring voice | App (native) | **M** |
| B6 | **Health Check Results, Presented Warmly** | Lab results and health-check reports (Health Check at Home, chronic monitoring) delivered behind a humanized summary layer: "what does this mean and am I okay?" first, the caregiver's one-line note, then the detail for those who want it. Never a raw table as the primary surface. | S, L, N | Relief — interpretation before information | NX (results read) + App (narration layer) | **S** |
| B7 | **Wellness Programs as Journeys** | Glow, Shape It, and IV-therapy courses rendered exactly like care plans: session dots, milestones, celebrations — the wellness revenue engine given the journey treatment. Maintenance cadence nudges ("quarterly health check due — same nurse?"). | L | Belonging — "Vitality is part of how I live well" | NX (program) + App | **S** |
| B8 | **Arabic Wellness Content Shelf** | Small curated library, original Arabic first: recovery sleep audio, gentle mobility videos, caregiver-authored tips, post-surgical FAQs, Ramadan-aware seasonal content. The between-episode heartbeat and the soft re-entry after discharge. | All | Belonging — presence between episodes | App (CMS) | **S** |
| B9 | **Wearable & Health-Platform Sync (read-only)** | Connect Apple Health, Samsung Health (via Google Health Connect), or WHOOP, read-only, no write-back. The app reads whatever activity/sleep/vitals data the platform already has and feeds it into the existing narrated score, recovery plan tone, and exercise suggestions, plus new motivation copy calibrated to real activity levels, not just check-in answers. No new raw-number dashboard; anomalies shift a sentence's tone, never introduce an alarm color. Mi Health (Xiaomi) is unverified, no confirmed public API found; do not commit it until checked. See 09-wearable-integration.md for full feasibility, guardrails, and compliance notes. | S, A, R | Confidence, the app notices more without the member doing more | App (HealthKit/Health Connect SDK, on-device) + WHOOP API (cloud, read-only) | **M** |

## Layer C — EMOTIONAL SUPPORT LAYER (the differentiator)

| # | Feature | Description | Personas | Emotional purpose | Dependency | MoSCoW |
|---|---|---|---|---|---|---|
| C1 | **Encouragement Engine** | The context-aware warm-copy system behind module M5 and all loop messaging: ring closed, streak week, hard day, pre-visit eve, plateau, return-after-absence. Every line written natively in warm MSA by the care-tone guide, localized to English; first person as the care team. Miss-messages meet compassion by contract: "rest was probably what you needed — ready to try again today?" | All | Emotional support — a person, present, in every sentence | App (native) | **M** |
| C2 | **Recovery Celebrations** | The full-screen gold celebration moments: first session, first week, halfway, ring-close micro-moments, graduation with the journey recap. On-brand motion (navy/gold shimmer, linen texture). Shareable to the Family Care Circle at the patient's choice. | All | Recovery — endings celebrated, effort honored ("you did this while raising a newborn") | App (native) | **M** |
| C3 | **Achievement Milestones** | The milestone ladder per plan/program: life-termed names, next-milestone visibility on the home screen, milestone history as the member's story. Feeds celebrations and family sharing. | A, S, R | Hope — a finish line that keeps getting closer | App + NX (plan facts) | **M** |
| C4 | **Care Companion Presence** | The ambient layer that makes the app feel inhabited: time-aware greetings, caregiver-forward header, state-aware top card, prayer-quiet defaults, Ramadan mode, the returning-member welcome. The sum of a hundred small warmths — this is the "companion" in companion-first. | All | Comfort — opening the app lowers the heart rate | App (native) | **M** |
| C5 | **Post-Visit Caregiver Notes** | After each visit: a warm plain-language summary — what we did, how you're doing, what's next — plus the caregiver's personal note ("ضغطها مستقر هذا الأسبوع"), pushed from Nixpend visit data and rewritten for humans. Major milestones upgrade to caregiver voice/video notes. The single highest-leverage premium artifact per visit. | All (N reads them) | Care + confidence — the visit's warmth persists in writing | NX (visit summary) + App (humanization) | **M** (voice notes **S**) |

## Layer D — COMMUNICATION LAYER (one care brain, three doors)

| # | Feature | Description | Personas | Emotional purpose | Dependency | MoSCoW |
|---|---|---|---|---|---|---|
| D1 | **Care Thread** | The always-open persistent chat with the caregiver/care team: swelling photos, "is this normal?" 2am questions, voice notes (Saleh's preference). AIWA powers first-line responses and triage with seamless, honest human escalation; response expectation always set ("Areeba replies within 3 hours, 9am–9pm"). Context carried across app/WhatsApp — deep links from AIWA threads land in the right app screen; one companion, three voices. | A, R, S | Emotional support — the thread never closes | AIWA + NX (care team) | **M** |
| D2 | **Voice Support (AIKA)** | The one-tap call surface for members who feel better talking than typing: AIKA answers as Vitality on the SIP trunk, handles booking status, rescheduling, and prep questions, escalates warmly to the hotline/coordinators. Surfaces contextually at anxious moments (post-op week 1, red-flag check-in day). Saved in contacts as "Vitality — نتكلم معك." | S, A | Relief — a voice when a screen is too much | AIKA | **S** (button + hotline **M**) |
| D3 | **Follow-up Reminders** | The care-only reminder system: T-24h visit reminder with the caregiver's face and prep checklist, exercise nudges at member-set times, medication cadence from the plan, post-visit follow-ups, quarterly wellness cadence. All invitations, never demands; marketing is contractually banned from push (it lives in email/WhatsApp). | All | Care — anticipated, never pestered | App + NX (schedule facts) | **M** |
| D4 | **Appointment Assistance** | Reschedule/cancel with grace (real alternative slots offered, no penalty-first language), running visit status, "is it confirmed?" permanently answered by the confirmation artifact, coordinator escalation for the complex cases — the app + AIWA/AIKA absorbing the routine so coordinators keep the high-touch work. | N, L | Confidence — control without a phone call | NX (write) + AIWA/AIKA | **M** |
| D5 | **Prayer-Time-Aware Notifications** | System-wide notification governor: no pushes across the five prayer windows (Riyadh timings), Friday-family-day awareness (weekly recap lands Thursday evening), Ramadan-shifted schedules, member-tunable quiet hours. Cultural fluency as infrastructure, on by default. | All | Comfort — the app knows how life here flows | App (native) | **M** |

## Layer E — FAMILY LAYER (the Family Care Circle)

| # | Feature | Description | Personas | Emotional purpose | Dependency | MoSCoW |
|---|---|---|---|---|---|---|
| E1 | **Circle Invite Flow** | One account invites family into a dependent's circle: WhatsApp-native invite (the channel Saudis already coordinate care in), role assignment (coordinator, viewer), the Sehhaty/Tawakkalna dependents mental model — zero education cost. Each accepted invite is an activated future member (the growth loop). | N | Belonging — the family becomes the care unit, officially | App + AIWA (invite delivery) | **M** |
| E2 | **Family Dashboard** | Home-screen State (e): the dependent's week at a glance — visits confirmed/done, ring days closed, latest caregiver note, next appointment — everything Noura currently assembles from three WhatsApp threads, in one Thursday-evening glance. Honest "some items are private" affordance. | N | Relief — trade guilt for confidence; stop being the app | App + NX (visit facts) | **M** |
| E3 | **Care Updates & Shared Progress** | The push channel for the circle: visit-completed notes, milestone celebrations shared by the patient, en-route forwarding on visit days, the weekly recap. Good news by default — the dashboard shows care happening, never surveillance. | N, A (sharer) | Hope, shared — milestones as family pride | App + NX | **M** |
| E4 | **Patient-Controlled Privacy (Per Data Type)** | The Labayh lesson as architecture: the patient controls sharing per data type — mobility progress: shared; mood check-ins: private; visit confirmations: circle-wide — with conservative defaults and a plain-language sharing summary. Dignity is the product; a privacy failure here is trust-ending. | S, A (control), N (respects) | Confidence + dignity — trust flows both ways | App (native) | **M** |
| E5 | **Booking-on-Behalf** | Noura's key job: book, pay, renew, and manage for her mother from her own phone — proxy intake, saved entry notes, the female-caregiver guarantee locked in once and remembered forever, package renewal, payment methods held by the coordinator. Validated by the ≥30% proxy-booking success metric. | N | Relief — everything handled from anywhere in Riyadh | NX (booking write) + App | **M** |
| E6 | **Shareable Celebration Moments** | Milestone celebrations exportable as elegant, on-brand cards to the family circle and (patient's choice) beyond — Reem's "I'm coming back" moment, Abdulrahman's proof to his sons. The referral surface that never feels like marketing. | R, A, N | Recovery + pride — a shareable "I did this" | App (native) | **S** |

**Feature count: 32** — Core 7 · Wellness 9 · Emotional 5 · Communication 5 · Family 6.

---

# PART C — PRIORITIZATION & PHASING

## C1. MoSCoW Summary

| Priority | Features | Count |
|---|---|---|
| **MUST** | A1–A7 (Tabby→S), B1–B5, B9 wearable sync (read-only), C1–C5 (voice notes→S), D1, D3, D4, D5 (+ D2's call button), E1–E5 | **25** |
| **SHOULD** | A6-Tabby installments, B6 warm results, B7 wellness journeys, B8 content shelf, C5 caregiver voice notes, D2 AIKA full flows, E6 shareable celebrations | **7** |
| **COULD** | Membership tier ladder (A2 extension), STC Pay, CHI insurance linkage, home-screen widgets, weekly "wrapped" recaps | — |
| **WON'T (this horizon)** | Computer-vision exercise feedback (B2), telehealth video consults, pharmacy/marketplace/symptom-checker breadth (Anti-pattern 12), wearable write-back / fall-detection / Family Circle escalation (v2+ if ever), community features | — |

## C2. Release Phasing

### v1.0 — MVP: "The Companion Arrives" (the feeling is the scope)

**The MVP must deliver the companion feeling, not just booking.** A booking-only v1 would park Vitality in the transactional quadrant beside Sanar and Thaat — the exact position the strategy exists to escape. The emotional features are therefore **non-negotiable in MVP**, named explicitly:

> **Non-negotiable emotional core of v1.0:** the match reveal (A3), the adaptive home screen with Companion Presence (C4) in all five states, the session-dot journey + progress ring + narrated wellness score (B4, B5), the daily check-in ritual (B3), the encouragement engine with streak-with-mercy (C1), celebration moments (C2/C3), post-visit caregiver notes (C5), the care thread (D1), and the Family Care Circle with per-datatype privacy (E1–E5). If any of these slip, the launch slips — a companion that can't celebrate, encourage, or remember is a portal with a gradient.

**Full v1.0 scope:** all 24 MUSTs — the native booking wizard on real Nixpend availability with Mada/Apple Pay, program booking instantiating care plans, matching with gender guarantee, district scheduling with en-route status, 2-tap rebooking, daily plans + exercise player, the complete daily emotional loop, prayer-aware notifications, and the family layer. RTL-first throughout; Ramadan mode in the launch content calendar.

**Rationale:** v1.0 closes the emotional curve's three dips from Document 01 in one release — the booking channel-switch (native wizard + confirmation artifact), the anxiety gap (en-route status), and the post-visit silence (caregiver notes, journey, thread). Success gates: NPS ≥ 70 pulse trajectory, ≥ 65% booking completion, ≥ 75% en-route views.

### v1.5 — "The Companion Speaks" (+2–4 months)

All SHOULDs: AIKA voice flows end-to-end (D2), caregiver voice/video milestone notes (C5+), warm health-check results (B6), wellness programs as journeys — Glow/Shape It (B7), the Arabic content shelf (B8), Tabby/Tamara installments, shareable celebration cards (E6). **Rationale:** deepen retention and the wellness revenue engine once the core loop has real usage data; AIKA ships when AIWA thread-handling quality is proven (CSAT ≥ 4.5 on AI-handled threads).

### v2.0 — "The Membership" (+6–9 months)

The tier ladder the codebase reserves (essential/advanced/elite) matured into true recurring membership; CHI insurance linkage; home-screen widgets and Apple Health import; weekly wrapped-style recaps; camera-guided exercise feedback evaluation (Kaia pattern); coverage expansion beyond the 12 districts as the roster grows. **Rationale:** recurring revenue and ecosystem depth built on a proven companion, honoring metric 9 (≥ 15% recurring-tier attach).

## C3. Nixpend Integration Boundary Map

One clean rule: **Nixpend owns the facts of care; the app owns the feelings about them.** The member never sees Nixpend; Nixpend never renders a screen.

| Direction | Data | Consumed by |
|---|---|---|
| **READ from Nixpend** | Therapist roster + credentials + availability slots | Matching (A3), booking wizard (A1), scheduling (A4) |
| | Booking/visit state (confirmed, en-route, completed) | Confirmation artifacts, en-route card, family updates |
| | Care-plan structure (sessions, prescriptions, program inclusions) | Session-dot journey, daily plans, exercise player, milestone ladder |
| | Visit summaries & results | Post-visit notes (humanized app-side), warm results (B6) |
| | Pricing, invoicing, patient record link | Payments (A6), profile (A7) |
| **WRITE to Nixpend** | New bookings, reschedules, cancellations (incl. proxy bookings) | A1, A4, A5, D4, E5 |
| | Check-in red flags (routed quietly to care team) | B3 |
| | Pre-visit intake, exercise adherence/feedback, session confirmations | A1, B2 |
| **STAYS APP-SIDE (never in Nixpend)** | The entire emotional layer: encouragement engine, celebration moments, milestone framing, narrated score computation and copy, streak logic, Ramadan/prayer governor, care-tone content | Layers B (presentation), C, D5 |
| | Family Care Circle: membership, roles, per-datatype privacy rules, sharing state | Layer E |
| | Preferences & rituals: "my usual," saved addresses/entry notes, gender guarantee record, notification settings | A5, A7 |
| | Content shelf, celebrations media, caregiver intro/milestone videos | B8, C2, C5 |
| **SIBLING CHANNELS** | AIWA (WhatsApp) and AIKA (voice) read/write the same Nixpend booking brain; app deep-links carry context across channels | D1, D2, E1 |

**Boundary consequence for delivery risk (from Doc 03 §11):** booking mechanics are thin UI over Nixpend and are sequenced early to de-risk the integration; everything emotional is app-native and ships regardless of integration depth. If Nixpend availability APIs slip, v1.0's emotional core still stands on manual-confirmed bookings — the companion never waits for the plumbing.

---

*End of Document 04. The IA & navigation workstream implements the A2.1 state model verbatim; the visual design workstream treats A1's emotional hierarchy and C2's non-negotiable emotional core as binding acceptance criteria; the booking workstream builds Layer A strictly inside the C3 boundary map.*
