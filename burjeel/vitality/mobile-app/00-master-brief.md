# Vitality Mobile App — Master Content Brief

Consolidated from all 10 source docs (01–08.md, 10-screens.html, 11-experience.html). This is the single reference for anything downstream — pitch decks, image-generation prompts, further design work.

## Company facts

- Vitality Home Health Services — part of **Burjeel Arabia Healthcare Network**. Domain **vitality.sa**. HQ Riyadh, An Nakheel District, KSA.
- Trust stats used site-wide: **25,000+ members** ("members," never "patients"), **200+ medical staff**, **15+ years**, **98% patient satisfaction**, **2-hour response time**, **MOH Accredited**.
- 9 core services (Doctor Home Visit, Home Nursing Care, Home Physiotherapy, Home Laboratory, Caregivers, IV Therapy, HydraCool Therapy, Beauty at Your Fingertips, Venus Legacy) + 14+ care programs/packages. Flagship/"Most Popular": **Premium Post-Surgery Recovery Care**.
- Contact: WhatsApp +966 50 444 7658 · Hotline 920022827 · Info@vitality.com. Hours Sat–Thu 10AM–10PM, Friday closed.
- Mission: *"To guide our members to discover wellbeing through an integrative medical approach."*
- Company vision: *"To become the leading international health and wellness provider."*
- Philosophy quote: *"We believe that true healthcare begins with trust and compassion at every step."* — Dr. Amr Alrabiee, Medical Director.
- Existing site taglines: *"Advanced Medical Care… Comfortably at Home"* / *"A Pain-Free Path To Wellness"* / *"We don't just provide a service — we deliver an exceptional care experience."*

## The digital gap (why the app matters)

- Every "Book Now" today exits to a plain WhatsApp chat or the external Nixpend patient portal (`patients.nixpend.com`) — an "ID Number / Date of Birth" hospital-intake-style login, not a Vitality moment.
- A full bilingual 4-step booking wizard already exists in the website's codebase but was **never shipped** as real UI.
- No live availability, no booking confirmation artifact, no payment flow, no accounts/history, zero API integration with Nixpend anywhere on the website.

## Product vision & brand tagline

- Product vision: *"The caring companion in every Saudi home Vitality serves — where members see their care, know their caregiver, and watch themselves recover."*
- **Brand tagline (recurring everywhere): "رفيقك في التعافي" — "Your companion in recovery."**
- Positioning line: *"the warmth of Calm, the journey of Headspace, the relationship of a personal therapist, and the clinical excellence of Riyadh's best home-care team, in Arabic first."*

## Competitive positioning

- 2×2 map: Clinical↔Wellness (x-axis) vs Transactional↔Companion (y-axis).
- Sehhaty (31M+ users, breadth/gov-portal), Sanar (1M+ users, e-commerce marketplace), Cura, Thaat, DarDoc, Justlife, Teladoc — all sit in the **transactional** half.
- **The "companion" quadrant is empty in the entire GCC.** Nearest global analogue is Luna (US in-home PT, same-therapist guarantee) — validates the thesis but isn't a local competitor.
- Vitality's target: clinically credible + emotionally wellness-grade + high on the companion axis.

## Five strategic pillars

1. **Companion-First, never portal** — center of gravity is a person and a journey, never a service grid.
2. **One-Tap Care Access** — fastest path from need to "help is arranged": 2-tap rebooking, saved preferences, native payment.
3. **Visible Recovery** — session-dot journeys, narrated wellness scores, outcome-evidence charts, celebration moments — the engine of renewal.
4. **Family Care Circle** — one account manages mother/father/child, with patient-controlled, per-datatype privacy.
5. **Arabic-First Premium** — RTL-first design, gender-guaranteed matching, prayer-time-aware scheduling, Ramadan mode.

## The five personas (verbatim, use these — not invented substitutes)

| | Name | Age | Role/context | Need | Quote |
|---|---|---|---|---|---|
| A | **Abdulrahman Al-Qahtani** | 58 | Retired ministry director, Al Nakheel — post-surgical (knee replacement) recovery | Session-dot journey, narrated score, care thread, celebrations | *"في المستشفى كان عندي جيش يهتم فيني. رجعت البيت وصرت لحالي."* — "In the hospital I had an army looking after me. I came home and I was on my own." |
| B | **Noura Al-Otaibi** | 36 | Marketing director, Al Yasmin — coordinating daughter for her 68-year-old hypertensive mother | Family Care Circle, proxy booking, female-caregiver guarantee, en-route status | *"I don't need another app. I need to stop being the app — the one who calls, checks, reminds, and worries."* |
| C | **Saleh Al-Dossari** | 61 | Building-materials business owner, Al Murabbah — Type 2 diabetic, insulin-dependent | 30-sec daily check-in, narrated (not raw-number) scores, streak-with-mercy | *"أنا مو مريض أعيش على التطبيق... أبي أحد يطمّني وأمشي."* — "I'm not a patient living inside an app... I want someone to reassure me and get on with my day." |
| D | **Lama Al-Rashid** | 31 | Big-4 consultant, KAFD/Hittin — wellness user (IV therapy, HydraCool, physio for desk-neck) | Zeel-grammar 2-tap booking, transparent pricing | *"If booking self-care takes more effort than the work that made me need it, I'll skip it — and so will everyone I'd have referred."* |
| E | **Reem Al-Harbi** | 28 | New mother, Al Sahafa — post-natal physio/nursing/lymphatic recovery | Absolute female-caregiver guarantee, interruptible 5–10 min exercise chunks | *"كل يومي لولدي. عشر دقايق للعلاج الطبيعي هي الشي الوحيد اللي لي أنا."* — "My whole day belongs to my son. Ten minutes of physio is the one thing that's mine." |

Recurring caregiver character used across all docs: **Amal Al-Rashidi**, physiotherapist, MOH-verified.

## Onboarding & the Match Reveal (the app's first emotional peak)

- Flow: Feel → Match → Book → Identity. Progress shown as an ambient gold line, never a step counter.
- Gender preference (Screen 3) is asked **once**, on a blush-toned screen, and is a **hard guarantee forever after** — micro-copy: *"هذا التفضيل مضمون في كل زيارة — لن نسألك مجدداً"* ("guaranteed every visit, never asked again").
- Matching wait screen (min. 2400ms, theatrical even if instant): *"نستمع إلى ما شاركته معنا…"* → *"نبحث في فريق متخصصينا المعتمدين…"* → *"وجدنا."* ("Found.")
- **Match Reveal screen** — the emotional peak: circular caregiver photo, Arabic name + transliteration, specialty tag, years of experience, MOH license badge, 20-second intro video button. Headline: *"وجدنا متخصصتك"* ("We found your specialist"). CTA: *"احجز أول زيارة مع [Name]"*.
- No name/ID/account required until booking — identity is deferred.

## Home screen (never opens on a list)

Adaptive modules M1–M10, 5 home states (new member / visit day / mid-recovery / program complete / family coordinator):
- **M1 Companion Header** — time-aware Arabic greeting + caregiver photo/presence
- **M2 Recovery Progress** — session-dot journey + daily ring
- **M3 Daily Wellness Score** — one number + one warm narrated sentence, never a grade
- **M6 Therapist/En-Route Card** — becomes a live en-route status card on visit day
- **M7 Milestones & Celebrations** — full-screen gold celebration, shareable to Family Circle
- **M9 Family Support Glimpse** — dependent's week at a glance

Sample verbatim copy: *"مساء الخير، أبو خالد 🌙"* / *"Your visit is confirmed for tomorrow"* / *"جسمك يتعافى بشكل ممتاز — استمر"* (wellness score narration) / *"جسمك يحتاج راحة اليوم — خذها"* (rest-day narration).

## Booking flow

4-step wizard: **Select Service → Date & Time → Your Details → Payment → Confirmation**.
- Payment: Mada, Apple Pay, Tabby/Tamara (orders ≥ SAR 1,000), cash on visit (opt-in).
- **Prayer-time-aware slots** shown in sage green with a crescent icon 🌙 — never greyed out or blocked, always selectable. Tooltip: *"This slot overlaps with prayer time — we can coordinate around this."*
- **2-Tap Rebooking ("My Usual")** — skips straight to pre-filled payment for repeat members.
- **Proxy booking** — a family coordinator (e.g. Noura) books on behalf of a dependent; confirmation shows "Booked by: Noura."
- Confirmation Artifact: navy card, gold corner ornaments, success checkmark, booking ref (e.g. **#VHC-2026-4831**), caregiver mini-card with gender-guarantee badge, "Add to Calendar" / "Share with Family."

## Recovery, wellness & celebration

- **Session-dot journey**: dots fill per session, current dot glows gold, finish line named in life terms ("Walking unaided," never "Mobility target 2").
- **Narrated wellness score**: one number (e.g. 74) + one warm Arabic sentence, never a raw grade or alarm color.
- **Outcome evidence**: "Pain down 40% since session 1," reviewed with the caregiver each visit.
- **Streak with mercy**: built-in rest days, one-tap streak repair, no shame copy, Ramadan-aware.
- **Celebration Moment**: full-screen navy + gold-shimmer takeover on milestones, Arabic calligraphy greeting ("مبروك يا أبو خالد"), gold particle animation, tappable caregiver voice note, "share with family circle."

## Family Care Circle

- One account manages multiple family members (e.g. Noura managing her mother and father).
- **Patient-controlled, per-datatype privacy** — e.g. mobility progress shareable, mood check-ins private. Never framed as surveillance.
- Family Dashboard: avatar row with status rings, dependent's week at a glance, proactive rebooking prompt: *"احجز لوالدتك — نفس الوقت؟"* ("Book for your mother — same time?").
- WhatsApp-native invite flow; roles = coordinator / viewer.

## Visual design system (exact tokens — use these, not approximations)

**Colors**
- Navy: `#001229` (darkest/bg), `#001C3D` (primary/trust surfaces), `#002B5B` (pressed/elevated)
- Gold: `#C5A059` (primary — rings, CTAs, milestones — progress/achievement ONLY, never decorative), `#D4B67C` (secondary/hover), `#F9F3E8` (achievement wash), `#9E7D41` (AA-compliant gold text)
- Ivory/neutral (~80% of UI): `#FDFCFA` (page bg), `#F7F5F0` (cards), `#F0EBE0` (input fills), `#E5DED0` (borders), ink text `#16233A`
- Therapeutic accents (desaturated dawn-desert tones): Sage `#8FAE8B` (calm/recovery), Sky `#7FA8C4` (info), Blush `#D9A08F`/`#9A5B48` (gentle encouragement), Apricot `#E0A85E` (attention, non-alarming)
- Rule: **navy = trust, gold = earned achievement — never used decoratively.** No red anywhere except a rare critical-emergency escalation color.

**Typography**
- **Termina** (weight 300) — display/headlines only: splash, onboarding, celebration headlines, score numerals. Never in body/forms.
- **Montserrat** — all working UI: body, labels, buttons, cards.
- **Noto Sans Arabic** — all Arabic text (sized one step larger to optically match Termina).
- **Aref Ruqaa** — ceremonial calligraphy only (celebrations, "مبروك"), used sparingly.

**Mood & imagery**
- Overall concept: "Premium Care, Softened for Daily Life" — a private suite, not a hospital or a gov-portal. Warm ivory daylight surfaces, navy as structure (not wallpaper), gold as rare reward (not decoration).
- Generous soft radii (20–28px), pill/circle shapes, warm navy/gold-tinted shadows (never grey).
- Photography: real Saudi homes (majlis, warm lamps, tea trays), natural golden-hour light, warm color grade with soft film grain, modest dress (thobe/abaya/hijab), elderly figures shown upright/dignified/active — never diminished.
- Illustration alternative ("Warm Najdi Modern"): flat-with-soft-depth, grain-free, soft long shadows, used for concept/diagram slides.
- L-shaped gold corner ornaments appear only on Celebration and Confirmation cards. Najdi geometric motifs (muqarnas/arabesque) survive only as ≤4% opacity ambient texture.

## Wearable & health-platform integration (confirmed v1 scope, 2026-07-12 — see `09-wearable-integration.md` and `04-experience-features.md` B9)

- **Verdict: confirmed for v1** — read-only connection to Apple Health, Samsung Health (via Google Health Connect), WHOOP, or Mi Health, feeding the app's own analysis, and having the app suggest actions or send motivation based on it. No write-back to any platform, no fall-detection/clinical-alerting pipeline, no Family Circle escalation in this scope — those stay a v2+ possibility, not part of what's confirmed. This supersedes the old blanket "WON'T (this horizon)" line in `03-product-strategy.md`/`04-experience-features.md` for this specific narrower scope only.
- **Platforms:** Apple HealthKit + Google Health Connect are on-device SDKs, no cloud OAuth/partner gate. Samsung Health syncs into Health Connect since Oct 2022 (no separate Samsung SDK needed). WHOOP has a clean open-registration OAuth API, no aggregator needed, data lives in WHOOP's cloud rather than on-device. **Mi Health (Xiaomi) is unverified** — no confirmed public API found; verify with Xiaomi's developer docs before promising it to the client.
- **Design rule:** wearable data only ever adjusts *tone* of the existing narrated score and recovery journey, or feeds a suggestion/motivation message — never a second number, never a raw clinical figure, never alarm-red.
- **Compliance flag:** health data is Sensitive/Tier-4 under Saudi PDPL; cloud-based wearable APIs (WHOOP/Mi Health) need real legal review for cross-border data transfer before committing.
- **Competitive reality check (verified):** Sehhaty already syncs Apple HealthKit/CareKit — but narrowly, steps/walking only, no heart rate/sleep, no native Watch app, confirmed verbatim on its App Store listing. A WHOOP↔Sehhaty/Seha/NPHIES partnership via Lean Business Services is confirmed via press release. Sanar and every other actual home-healthcare/booking competitor (Cura, DarDoc, Thaat, Justlife, Okadoc, Vezeeta, Altibbi, SEHA) show no evidence of any wearable integration. Fakeeh Care and Cleveland Clinic Abu Dhabi (hospital-system apps, not direct competitors) go deeper — vitals dashboards, not suggestions. **Correct pitch claim: "deeper than Sehhaty's steps-only sync, and the only one turning wearable data into an actual suggestion/motivation message — not just display" — not "first in the GCC to sync wearables."**

## CodeOx / closing credentials (use on any closing/cover slide)

- **CodeOx** — prepared by Shabeeb Kaip, Head of Operations
- shabeeb.k@code-ox.com · +966 53 571 6437 · code-ox.com
- Classification line used in the original deck: "Confidential — Client Use Only"
