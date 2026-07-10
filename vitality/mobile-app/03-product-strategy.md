# Vitality Home Care — Mobile App Product Strategy

**Document 03 — Product Strategy**
**Client:** Vitality Home Care (vitality.sa) — premium home healthcare, Riyadh, KSA
**Prepared by:** CodeOx — Shabeeb Kaip, Head of Operations · shabeeb.k@code-ox.com · +966 53 571 6437
**Date:** 9 July 2026
**Inputs:** Document 01 (Website & Digital Experience Discovery), Document 02 (Competitive Benchmarking & Pattern Library)
**Feeds:** 6 downstream workstreams — IA & navigation, onboarding, booking, progress & retention, family circle, visual design. This document is the strategic contract they all build against.

---

## 1. Product Vision

Vitality's own mission statement already says it: *"To guide our members to discover wellbeing through an integrative medical approach."* Members — not patients. The website has spent two years earning the right to that word: a five-star digital lobby that makes thousands of Riyadh families feel that exceptional care is one message away. The app is the natural next chapter of that same promise — the moment "Uninterrupted Care" stops being a headline and becomes a living presence in the member's pocket. When someone opens the Vitality app — the night before surgery, the morning after a fall, the week a parent's diabetes gets harder to manage alone — they should feel what Vitality's best nurses already make people feel at the door: *someone capable and kind is handling this, and I can see my way back to strength.* Not a hospital in an app. A companion who happens to command Riyadh's best clinical team. The GCC has a dozen apps that can dispatch a nurse; it has none that can hold a family's hand through a recovery. Vitality will be the first, in Arabic first, wrapped in the navy-and-gold warmth the brand already owns.

**Vision statement:**

> **"The caring companion in every Saudi home Vitality serves — where members see their care, know their caregiver, and watch themselves recover."**

---

## 2. Product Mission

**What the app does, every day, for whom:**

Every day, the Vitality app gives **members and their families** one calm place to:

1. **Reach care in one tap** — book a visit, message their caregiver, or escalate to a human (AIWA in-app, AIKA by voice, the hotline behind both) without ever restarting a conversation from zero.
2. **See who is coming and when** — a named, credentialed, gender-guaranteed caregiver with a face, an ETA, and a message thread — never a faceless "the provider will contact you."
3. **Watch recovery happen** — a care plan rendered as a journey with session dots, a daily check-in that becomes a warmly narrated recovery score, and outcome evidence ("pain down 40% since session 1") reviewed with the caregiver.
4. **Care as a family** — a son in Al Olaya managing his mother's Home Care Plus program in Al Malaz sees her progress ring fill, with the mother controlling exactly what is shared.
5. **Stay well between episodes** — Arabic-first wellness content, gentle rituals, and maintenance nudges that keep Vitality present after the last session, so the next need starts inside the relationship, not on Google.

Operationally, the app is a thin, beautiful layer over **Nixpend HMS** (roster, availability, scheduling, records) and a sibling channel to **AIWA** (WhatsApp) and **AIKA** (voice) — one booking brain, three doors, one feeling.

---

## 3. Core Value Proposition

### 3.1 For members (patients)

Today the member experiences Vitality's warmth in person and its prestige online — but the digital middle (book → wait → recover) is bridged by WhatsApp conversations and phone calls. The app closes that gap with three things no GCC competitor offers: **a caregiver you know, a journey you can see, and a companion that remembers you.**

> **Elevator:** *"Your own Vitality caregiver, your recovery made visible, and help one tap away — in the comfort of your home, in your language."*

### 3.2 For families (the caregivers-of-the-caregiver)

The Saudi family is the true unit of care: adult children book for parents, husbands for wives, mothers for everyone. Today that coordination lives in WhatsApp threads and worried phone calls. The Family Care Circle gives the coordinating family member visibility (visits confirmed, caregiver en route, milestones reached), control (book, pay, manage on behalf), and peace of mind — with the patient's dignity protected by per-datatype privacy controls.

> **Elevator:** *"Care for your parents from anywhere in Riyadh — see the visit confirmed, the nurse arrive, and the recovery progress, without a single chasing phone call."*

### 3.3 For Vitality (the business)

The app converts a person-dependent, WhatsApp-operated service into a product-supported relationship: bookings that don't leak at the channel switch, packages that renew because progress is visible, families that multiply accounts through invites, coordinators freed by AIWA/AIKA deflection, and a defensible position — the empty GCC "companion quadrant" — that Sanar, Thaat, and Justlife cannot copy with a service menu.

> **Elevator:** *"The app turns Vitality's earned goodwill into retained members, recurring packages, and a moat no transactional competitor can cross."*

---

## 4. Strategic Pillars

Five pillars. Every feature decision in every downstream workstream must trace to at least one; anything that traces to none is out of scope by default (Anti-pattern 12: feature-breadth creep is Sehhaty's game, and Sehhaty already won it).

### Pillar 1 — Companion-first, never portal

**What:** The app's center of gravity is a person and a journey — the matched caregiver as recurring character, the ambient emotional home screen, the care thread — never a service grid, a records cabinet, or a workflow state machine. Nixpend stays invisible; the member sees "Sara is confirmed for Tuesday 4pm," never "request #4832 pending."
**Why:** The entire GCC cluster sits in the transactional half of the positioning map. Sehhaty owns breadth; Sanar owns the commodity marketplace. The only unoccupied, defensible position — and the client's explicit mandate — is the companion quadrant. Every portal pattern that leaks in (grids, forms-first, alarm-red badges) surrenders the position.
**Owned patterns:** Caregiver as recurring character, ambient emotional home screen, care thread, match reveal.

### Pillar 2 — One-tap care access

**What:** From moment of need to "help is arranged" in the fewest possible taps: 2-tap rebooking of "my usual," saved preferences (caregiver, gender, address, home-entry notes), pre-visit intake done in advance, real Nixpend availability shown as bookable slots, Mada/Apple Pay/Tabby payment in-flow, and AIWA chat + AIKA voice as always-open sibling doors. The dormant 4-step booking wizard the client already wrote and translated (service → date/time → details → payment → "Booking Confirmed Successfully!" + reference) finally ships — as the app's native flow.
**Why:** Today's journey drops at the exact moment of intent: every Book Now exits the branded experience, context is lost, and confirmation is a human promise rather than an artifact. The booking domain model is already designed and client-approved in `messages/*.json`; the app is where it comes alive, and the "Secure & Encrypted Booking" microcopy already on the site becomes literally true.
**Owned patterns:** 2-tap rebooking & saved rituals, pre-visit intake, en-route status, confirmation artifacts (reference, calendar, reminders).

### Pillar 3 — Visible recovery

**What:** Make the website's "Clinical Path to Wellness" graphic (Book → Consult → Assess → Plan → Treat → Recover) the literal in-app state machine. Every care plan renders as a journey with session dots and a named finish line ("Walking unaided"). A 30-second daily check-in (pain, mood, sleep) produces a narrated recovery score in the Oura voice — "جسمك يحتاج راحة اليوم — خذها" — never a grade. Outcome evidence charts prove the plan is working. Celebration moments — gold, full-screen, occasionally carrying a voice note from the actual caregiver — mark milestones.
**Why:** The website already promises "Tailored Care Plan," "Progress Monitoring," and "detailed digital reports"; nothing tracks them yet. Sword and Hinge proved the evidence loop is the most motivating chart in recovery care; Headspace proved session dots convert appointments into a story. Visible recovery is also the direct engine of package renewal — members renew what they can see working.
**Owned patterns:** Session-dot journey, narrated recovery score, outcome evidence, celebration moments, daily check-in ritual, streak with mercy, progress ring.

### Pillar 4 — Family Care Circle

**What:** One account manages profiles for mother, father, child — the mental model Saudis already learned from Sehhaty and Tawakkalna, so education cost is zero. Family members book, pay, and follow on behalf of elders; they see progress rings, confirmed visits, and shareable celebration moments. The patient controls sharing per data type (mobility progress: shared; mood check-ins: private) with conservative defaults — the Labayh lesson.
**Why:** The family is the care unit in KSA, and the decision-maker for Vitality's two flagship programs (Home Care Plus, Post-Surgery Recovery) is usually not the patient. The family circle is simultaneously the strongest retention structure (many stakeholders per patient), the strongest growth loop (each invite is an activated future member), and the client's existing "Elite Family Care Bundle" promotion made structural.
**Owned patterns:** Family care circle, per-datatype privacy, shareable celebrations, dependent booking with proxy intake.

### Pillar 5 — Arabic-first premium

**What:** Every screen designed RTL-first with English as the faithful mirror; emotional copy written natively in warm MSA with Saudi softness ("حياك الله"), then localized to English. Gender preference as a guaranteed first-class matching field, not a filter. Prayer-time-aware scheduling and notification quiet hours; Ramadan mode from v1's content calendar. The visual language extends the website's proven identity — navy #001C3D, gold #C5A059, Najdi heritage silhouettes, woven-linen texture — softened from "hotel lobby" to "private suite": calmer gradients, warmer light, higher accessibility floor (type size, contrast) without losing the aesthetic.
**Why:** Sehhaty set the national floor for Arabic parity; anything less reads foreign. But no competitor combines Arabic-first with premium emotional design — the GCC apps that are Arabic-native are bureaucratic, and the ones that feel designed are English-first. Cultural fluency (gender guarantee, salah-aware slots, home-threshold respect) is Vitality's fastest trust signal and cannot be retrofitted.
**Owned patterns:** Trust layer (MOH license, credentials, woven elegantly), gender-guaranteed match, prayer-aware scheduling, en-route caregiver ID for the home threshold.

---

## 5. User Personas

Five personas grounded in Vitality's real service lines. Names are composites; behaviors are drawn from the discovery testimonials, the benchmarking cultural research, and the service inventory.

---

### Persona A — Abdulrahman Al-Qahtani · Post-surgical recovery member

*Anchor service: Premium Post-Surgery Recovery Care (the "Most Popular" flagship) — physician visits, nursing, physiotherapy, wound monitoring.*

| | |
|---|---|
| **Age / context** | 58 · Retired ministry director, Al Nakheel. Knee replacement at a private hospital; discharged with a paper of instructions and a follow-up date six weeks away. His wife found Vitality on Instagram. |
| **Goals** | Walk unaided at his majlis before Ramadan. Avoid re-hospitalization. Understand whether each week's pain is "normal." |
| **Anxieties** | "Is this swelling dangerous?" The blind gap between hospital discharge and the first home visit. Being seen as diminished by visitors. Losing track of which exercise, which pill, which day. |
| **Tech comfort** | Moderate — WhatsApp, YouTube, Twitter/X daily; suspicious of apps that demand forms. Prefers Arabic interfaces; reads English fine but *feels* in Arabic. |
| **What relief looks like** | Opening the app the evening after discharge and seeing a 6-week plan with his physiotherapist's face on it and session 1 confirmed for tomorrow, 4pm. |
| **Key quote** | *"في المستشفى كان عندي جيش يهتم فيني. رجعت البيت وصرت لحالي."* — "In the hospital I had an army looking after me. I came home and I was on my own." |
| **Needs from the app** | The session-dot journey with a named finish line; the narrated recovery score answering "is this normal?" every morning; the care thread to send a photo of the swelling and hear back within hours; outcome evidence to show his sons he's improving; celebration moments that restore pride, not pity. |

---

### Persona B — Noura Al-Otaibi · The coordinating daughter (family decision-maker)

*Anchor service: Home Care Plus Program — elderly care, chronic condition management, daily monitoring, 24/7 nurse hotline. **The economic buyer for Vitality's highest-LTV programs.***

| | |
|---|---|
| **Age / context** | 36 · Marketing director in Al Yasmin; mother (68, hypertensive, increasingly frail) lives across the city in Al Malaz with a housekeeper. Noura coordinates everything — appointments, medicines, moods — over three WhatsApp threads and guilt. |
| **Goals** | Know, without calling, that her mother was visited, took her medication, and is trending okay. Choose who enters her mother's home. Pay and manage everything from her own phone. |
| **Anxieties** | The unanswered midday call. Strangers at her mother's door — gender and identity of the caregiver is non-negotiable. Being blamed by siblings if something is missed. Her mother concealing decline to avoid "being a burden." |
| **Tech comfort** | High — runs her team on Slack; expects Careem-grade live status and Apple-Pay checkout. Zero patience for OTP mazes. |
| **What relief looks like** | A Thursday-evening glance at the family circle: mother's week — three visits done, progress ring closed five days of seven, nurse Amal's note: "ضغطها مستقر هذا الأسبوع" — pressure stable this week. |
| **Key quote** | *"I don't need another app. I need to stop being the app — the one who calls, checks, reminds, and worries."* |
| **Needs from the app** | The Family Care Circle as home base; proxy booking with saved entry notes ("family section entrance, call before arriving"); female-caregiver guarantee locked in once; en-route status forwarded on visit days; per-datatype sharing her mother controls, so trust flows both ways; one place to pay, renew the package, and invite her brother. |

---

### Persona C — Saleh Al-Dossari · Chronic condition member (diabetes)

*Anchor service: Diabetes Care Program at Home — glucose monitoring, insulin administration, nutrition counseling, diabetic foot care.*

| | |
|---|---|
| **Age / context** | 61 · Owns a building-materials trading business in Al Murabbah; Type 2 for eleven years, now insulin-dependent, recent foot ulcer scare. His son enrolled him after the site's "Chronic Disease Stability Program" page convinced him. |
| **Goals** | Stability — no more scares, no hospital. Keep working. Keep his condition quiet outside the family. |
| **Anxieties** | The foot. Numbers he doesn't understand delivered without interpretation. Feeling policed by health tech — red marks, missed-day shame. Long-term: "Will this only get worse?" |
| **Tech comfort** | Low-moderate — WhatsApp voice notes over typing; large type essential; his son sets up anything new. Arabic only. |
| **What relief looks like** | A morning message in warm Arabic that reads like a nurse, not a lab: "قراءاتك هذا الأسبوع أهدأ من الأسبوع الماضي — استمر" — steadier than last week, keep going. |
| **Key quote** | *"أنا مو مريض أعيش على التطبيق. أنا رجّال عندي شغل — أبي أحد يطمّني وأمشي."* — "I'm not a patient living inside an app. I'm a man with work to do — I want someone to reassure me and let me get on with my day." |
| **Needs from the app** | The daily check-in as a 30-second ritual, prayer-time aware; the narrated score (Oura voice) instead of raw numbers; streak with mercy — a bad day meets compassion, never a red X; the recurring nurse he knows by name; hotline/AIKA escalation one tap deep; quiet routing of red-flag readings to the care team without alarming him; privacy from everyone except who he chooses. |

---

### Persona D — Lama Al-Rashid · Busy professional, wellness & performance

*Anchor services: IV Vitamin Therapy, Health Check at Home, HydraCool, physiotherapy for a recurring desk-work neck issue — the wellness/aesthetics revenue engine.*

| | |
|---|---|
| **Age / context** | 31 · Consultant at a Big-4 firm in KAFD, lives in Hittin. Optimizes everything; already tracks sleep on her Apple Watch and books everything else in two taps. Discovered Vitality through the "Beauty & Wellness" grid and a friend's IV-drip recommendation. |
| **Goals** | Energy through brutal project cycles. Effortless self-maintenance — booked in the gaps of a calendar that has none. A premium experience that respects her time and standards. |
| **Anxieties** | Wasting an evening on WhatsApp back-and-forth to book a 45-minute drip. Unvetted providers at her door. Being marketed at — one "20% off!" push and she deletes the app. |
| **Tech comfort** | Very high — the app is compared to Careem, Zeel, and her banking app, not to other clinics. |
| **What relief looks like** | Thursday 9pm: "Book my usual?" — same nurse, same drip, Saturday 6pm, Apple Pay, done in eleven seconds. Sunday: her energy panel notes the pattern. |
| **Key quote** | *"If booking self-care takes more effort than the work that made me need it, I'll skip it — and so will everyone I'd have referred."* |
| **Needs from the app** | Zeel-grammar on-demand booking: 2-tap "my usual," saved preferences, live en-route status with caregiver photo and ETA; transparent prices (the 250–389 SAR services finally shown and payable); wellness programs as journeys (Glow, Shape It) rather than one-offs; maintenance nudges timed to her cadence, never promotional pushes; a referral moment elegant enough to share. |

---

### Persona E — Reem Al-Harbi · New mother in physio recovery

*Anchor services: Home Physiotherapy (post-natal back/pelvic rehabilitation), Home Nursing, Lymphatic Recovery Therapy — the empathy-defining persona for tone and motion design.*

| | |
|---|---|
| **Age / context** | 28 · First baby, three months old; C-section recovery plus back pain from carrying and nursing. Lives in Al Sahafa; husband travels for work; her mother visits twice a week. Leaving the house with the baby for clinic physio is a two-hour logistics operation — home visits are the only realistic option. |
| **Goals** | Carry her son without wincing. Reclaim a body that feels like hers. Do her home exercises in the fragments of time a newborn allows. |
| **Anxieties** | A male stranger at the door while she's home alone — female caregiver is absolute. Exercising "wrongly" and hurting herself. Guilt at spending time and money on herself. The 2am spiral: "Is this pain normal after C-section?" |
| **Tech comfort** | High but attention-fragmented — everything she does is interruptible; sessions with the app last 30 seconds, at odd hours, one-handed. |
| **What relief looks like** | Match reveal: "Your physiotherapist: Areeba — 10 years, post-surgical & women's health, speaks Arabic and English" — a woman, credentialed, with a warm intro video. And at 2am, a care thread that answers by morning. |
| **Key quote** | *"كل يومي لولدي. عشر دقايق للعلاج الطبيعي هي الشي الوحيد اللي لي أنا."* — "My whole day belongs to my son. Ten minutes of physio is the one thing that's mine." |
| **Needs from the app** | Gender-guaranteed match as the first question, remembered forever; the exercise player in interruptible 5–10 minute chunks with Arabic voiceover; streak with mercy calibrated for newborn chaos; the care thread for the 2am questions; celebration moments that honor her effort ("first week complete — you did this while raising a newborn"); visit slots aligned to nap windows and her mother's visiting days. |

---

## 6. User Goals — functional, emotional, social

| Persona | Functional goals | Emotional goals | Social goals |
|---|---|---|---|
| **Abdulrahman** (post-surgical) | Follow the 6-week plan; get "is this normal?" answered fast; never miss/confuse a session or medication | Feel the hospital's safety net came home with him; see proof he's improving; keep dignity intact | Show sons and majlis peers he is recovering strongly; be cared for without feeling diminished |
| **Noura** (family coordinator) | Book/pay/manage for her mother remotely; verify visits happened; control who enters the home | Silence the background worry; trade guilt for confidence; trust without surveilling | Be the reliable daughter in the family's eyes; share good news (milestones) with siblings; coordinate without conflict |
| **Saleh** (chronic/diabetes) | Log the daily check-in in 30 seconds; get readings interpreted; reach a nurse instantly when the foot worries him | Feel stable, not sick; be reassured, not policed; keep hope on a condition that "only gets worse" | Keep his condition private outside the family; reassure his wife and son without being managed by them |
| **Lama** (wellness professional) | Book "my usual" in 2 taps; transparent prices and instant payment; reliable arrival windows | Feel the service matches her standards; self-care without friction-guilt; trust the person at her door | Refer with pride — the app as a status-consistent recommendation; wellness as identity, not indulgence |
| **Reem** (new-mother physio) | Female caregiver guaranteed; exercises in interruptible chunks; 2am questions answered by morning | Feel her body is recoverable; permission for self-care; never feel judged for missed days | Reassure her husband and mother she's supported when alone; a shareable milestone that says "I'm coming back" |

---

## 7. Emotional Design Goals — the seven target feelings

The client's mandate, verbatim: *"When users open the app, they should feel relief, comfort, emotional support, confidence, care, hope, and recovery."* Each feeling becomes a design principle with concrete moments — this table is the acceptance criteria for every downstream screen.

| # | Feeling | Design principle | Example moments in the app |
|---|---|---|---|
| 1 | **Relief** | *Resolution before information.* The first thing any screen answers is "is this handled?" — status before data, confirmation before detail. Help is always one tap, never a phone-menu tree. | Booking ends on a confirmation artifact (reference, caregiver, time, calendar add) — not a "we'll contact you." The home screen's top card always resolves today's biggest open question. AIKA call button surfaces contextually at anxious moments (post-op week 1, red-flag check-in). |
| 2 | **Comfort** | *Soft by default.* Calm gradients on the navy/gold system, slow fades, generous whitespace, warm time-aware greetings ("مساء الخير أم فهد"), max three elements above the fold. No alarm-red for anything routine; ambers and the caregiver's voice instead. | App open is a lowered-heart-rate moment (Calm's lesson): ambient gradient, the caregiver's face, today's one thing. Notifications written as invitations, never demands. Prayer-time quiet hours on by default. |
| 3 | **Emotional support** | *A person, present.* Every interaction has a named, pictured human attached; the app speaks in first person as the care team, never as "the system." The thread never closes. | The care thread with response expectation set ("Areeba replies within 3 hours, 9am–9pm"). Missed-exercise message: "يبدو أن جسمك احتاج راحة أمس — نجرب اليوم؟" — rest was probably what you needed; ready today? A voice note from the caregiver at milestone moments. |
| 4 | **Confidence** | *Competence made visible, elegantly.* Credentials, MOH license, background-check badge, and guarantees (gender, same-caregiver) woven into profile cards hotel-style — present everywhere, stamped nowhere. Every promise is demonstrable: "2h response" becomes a live ETA. | Match reveal shows credentials + years + specialty + intro video. En-route card shows license badge and ID for the gate. Pre-visit intake confirms "Areeba knows about your C-section history" — the member never repeats their story. |
| 5 | **Care** | *Remembered, anticipated, never restarted.* The app knows the member: saved preferences, care-team memory, context carried across app/AIWA/AIKA. Being known is the luxury. | "Book Amal again — same time next week?" after each visit. Ramadan mode adjusts reminders unprompted. A returning member after six months is greeted mid-story: "Welcome back, Abu Khalid — how is the knee?" |
| 6 | **Hope** | *Progress made visible and narrated.* Every metric is evidence pointed forward; every chart has a caring sentence attached; finish lines are named in life terms, not clinical ones. | Session-dot journey with the finish line labeled "Walking unaided." Outcome evidence: "Pain down 40% since session 1" reviewed together at the visit. The narrated recovery score frames plateaus as part of the story, not failure. |
| 7 | **Recovery** | *Endings are celebrated and belonging continues.* Recovery is the destination the whole product points at — milestones in gold, graduation as a designed moment, and discharge as a doorway to wellness membership, not an account going dark. | Full-screen gold celebration at plan completion, with the caregiver's congratulation note; shareable to the family circle. Graduation flows into the wellness shelf and maintenance rituals — "recovered" becomes "member," closing the loop to the brand's own word. |

---

## 8. The Feeling Map — emotion by lifecycle stage

For each stage: today's reality (the strong foundation), the target feeling, and the specific design mechanism that produces it. This is the emotional state machine the IA, onboarding, booking, and retention workstreams implement.

### 8.1 Before opening the app — the moment of need

| | |
|---|---|
| **Today** | The website does this brilliantly: a person in pain or a worried daughter lands on vitality.sa and is met with prestige, credentials, and warmth — trust is won. The next step is a WhatsApp conversation, which is human and responsive, though it starts from zero each time. |
| **Target feeling** | **"Help is closer than the pain."** Before a single tap, the app icon itself is a promise: someone is already on my side. |
| **Mechanism** | The app as pre-installed reassurance: home-screen widget showing next visit / today's ring; AIKA's number saved as "Vitality — نتكلم معك" for the moments a call feels better than a screen; deep links from AIWA WhatsApp threads straight into the relevant app context, so the channels feel like one companion with three voices. Push at moments of likely need is care-only, never promotional (Anti-pattern 9). |

### 8.2 During onboarding

| | |
|---|---|
| **Today** | There is no onboarding — the website's education-rich pages (includes, preparation guides, team profiles) do the pre-sale, then a coordinator takes over on WhatsApp. That human warmth is the standard the app must match digitally. |
| **Target feeling** | **"They listened to me before they asked anything of me."** Understood, not processed. |
| **Mechanism** | **Feel → match → book → identity, in that order.** Calm's deferred registration + BetterHelp's intake-as-listening: a short conversational flow (what brings you here; who is the care for — self or a parent, activating the family circle early; gender preference first, guaranteed forever; language; style: "encouraging coach" or "gentle and patient") → the theatrical **match reveal** — "finding your specialist…" then a named human with face, credentials, and intro video — the app's first emotional peak, before any account exists. Nixpend identity plumbing appears only when booking requires it; biometric unlock thereafter (Anti-patterns 2, 6). |

### 8.3 During booking

| | |
|---|---|
| **Today** | Booking works — thousands of families have booked via WhatsApp and the coordinators convert with genuinely personal service. The complete 4-step booking vocabulary (service → slot → details → payment → confirmation + reference) is already written and translated in the codebase — a client-approved blueprint awaiting its UI. |
| **Target feeling** | **"That was effortless — and it's truly arranged."** Momentum, then certainty. |
| **Mechanism** | The dormant wizard shipped natively as a thin, beautiful layer over Nixpend: real availability (prayer-time-aware slots from the live roster), the 12-district coverage picker, insurance capture (Bupa, Tawuniya, MedGulf, Al-Rajhi Takaful, AXA), transparent pricing with Mada/Apple Pay/Tabby, and pre-visit intake folded in comfortably (home-entry notes, condition context). It ends on a **confirmation artifact**: booking reference, caregiver card, calendar add, reminder cadence — the "Booking Confirmed Successfully!" strings finally rendered. Repeat members skip it all: **2-tap rebooking** of "my usual." |

### 8.4 Waiting for the visit — the anxiety gap

| | |
|---|---|
| **Today** | Confirmation and scheduling are handled attentively by coordinators over WhatsApp and phone — high-touch, human, and invisible to any screen. The wait between "confirmed" and the doorbell is where a member's imagination currently works alone. |
| **Target feeling** | **"I know exactly who is coming, and when."** The sacred home threshold, respected in advance. |
| **Mechanism** | The **en-route status** pattern (Zeel/Uber grammar): a live card on visit day — caregiver photo, name, license badge, ETA, "Amal is on her way," plus ID/vehicle details for compound gates. Before that: a T-24h reminder with the caregiver's face and a preparation checklist drawn from the website's existing prep guides ("wear comfortable clothing, prepare open exercise space"). The caregiver arrives as someone the member already knows — killing the #1 home-visit anxiety and turning "We reach you within 2 hours" from a claim into a countdown. |

### 8.5 During recovery — between sessions

| | |
|---|---|
| **Today** | The in-home visit is Vitality's proudest asset — testimonials confirm punctual, professional, genuinely caring service. Between visits, care continues informally through WhatsApp when members reach out; the plan, exercises, and progress live with the clinical team. |
| **Target feeling** | **"I'm getting better, and I'm not doing it alone."** Hope with evidence; effort with company. |
| **Mechanism** | The full **daily loop + journey loop**: 30-second daily check-in → **narrated recovery score** in the Oura voice → **progress ring** for today's actions (exercises ✓ check-in ✓ walk ✓). The **exercise player** (video by her own therapist where possible, Arabic voiceover, interruptible chunks) with **streak-with-mercy**. The **care thread** always open for the swelling photo and the 2am question. At each visit, caregiver and member review the **outcome evidence** chart together — "pain down 40% since session 1" — turning data into hope. **Celebration moments** in gold at every milestone, the big ones carrying the caregiver's own voice note. |

### 8.6 After treatment ends

| | |
|---|---|
| **Today** | Care concludes warmly in person; gratitude is real (the testimonials prove it) and returning members restart via WhatsApp when the next need arises. The goodwill exists — it simply has no digital home yet. |
| **Target feeling** | **"I finished something — and they're still with me."** Pride, then continuity instead of silence. |
| **Mechanism** | **Graduation as a designed moment**: full-screen celebration, the journey's dots all lit, a recap of the evidence (where you started → where you are), the caregiver's congratulation note, shareable to the family circle. Then the **post-visit/post-plan loop**: a warm plain-language final summary (Nixpend data, rewritten for humans), a gentle maintenance plan, the wellness shelf unlocked, and the caregiver relationship kept warm — "Areeba is still your physiotherapist; message anytime." Rebooking any future need is 2 taps inside the relationship, not a cold restart. |

### 8.7 During long-term wellness

| | |
|---|---|
| **Today** | Wellness is Vitality's fastest-growing surface — IV therapy, Glow, Shape It, HydraCool, health checks — and the brand already speaks companion language ("Your Partner in Wellness," "members"). Today these are excellent individual treatments; the connective tissue between them is the app's opportunity. |
| **Target feeling** | **"Vitality is part of how I live well — not where I go when something breaks."** Belonging; quiet pride of membership. |
| **Mechanism** | The **ambient/brand layer at cruising altitude**: wellness programs as journeys with session dots (Glow and Shape It rendered like Headspace courses), maintenance rituals and cadence-aware nudges ("your quarterly health check is due — same nurse?"), the **Arabic wellness content shelf** (original, caregiver-authored, Ramadan-aware) as the between-episode heartbeat, seasonal moments (Ramadan mode, a Thursday-evening weekly recap timed for family day), and the tier ladder the codebase already reserves (essential/advanced/elite) maturing into a true membership — the word the client's mission chose years ago. |

---

## 9. Positioning Statement & Brand Promise

### 9.1 Positioning statement

> **For** Riyadh's premium households — members recovering at home and the families who care for them —
> **who** want more than a booking utility when health enters their home,
> **the Vitality app** is a caring wellness companion
> **that** puts a known, gender-guaranteed caregiver, a visible recovery journey, and one-tap access to real clinical care in their pocket, Arabic first —
> **unlike** the transactional home-care marketplaces (Sanar, Thaat, DarDoc) and government portals (Sehhaty) that book services but hold no one's hand,
> **because** only Vitality combines Riyadh's proven premium in-home clinical team with companion-grade emotional design — the warmth of Calm, the journey of Headspace, the relationship of Luna — on one care brain shared with AIWA and AIKA.

### 9.2 Brand promise for the app

> **"رفيقك في التعافي — Your companion in recovery."**
> Open the app and someone capable and kind is already handling it: you'll know who's coming, see yourself getting stronger, and never carry a health worry alone. We don't just provide a service — we deliver an exceptional care experience, now uninterrupted between visits.

*(Deliberately continuous with the site's own promises: "We don't just provide a service — we deliver an exceptional care experience" and "Our Promise — Uninterrupted Care." The app doesn't need a new promise; it keeps the existing one more of the time.)*

### 9.3 Positioning guardrails (from the benchmarking map)

- **Never drift down** into transactional marketplace territory — that is a price knife-fight with Sanar/Thaat/Justlife that erodes premium pricing power.
- **Never drift full-right** into pure wellness — clinical credibility (MOH license, real outcomes, real caregivers) is the moat.
- **Never compete on breadth** — 49 services is Sehhaty's game. One narrow promise, done beautifully.
- The target cell — **clinically credible, emotionally wellness-grade, high on the companion axis** — is empty in the GCC. First mover owns the vocabulary.

---

## 10. Success Definition — measurable outcomes

Ten outcomes, emotional and commercial, each with a v1 target and its strategic pillar. Baselines to be confirmed with Vitality's coordinators and Nixpend data during Discovery close-out; targets below are consultancy estimates calibrated to the benchmark set (Luna 99.7% satisfaction, Sehhaty adoption curves, Zeel rebooking norms).

| # | Outcome | Metric | v1 target (12 months post-launch) | Pillar |
|---|---|---|---|---|
| 1 | **Members feel the mandate** | In-app emotional pulse ("How did that feel?" micro-survey at 3 journey moments) + app-NPS | NPS ≥ 70 (vs. ~30–40 typical for GCC health apps); ≥ 80% of pulse responses in the relief/comfort/confidence range | All |
| 2 | **Booking conversion without leakage** | App booking-flow completion rate (service selected → confirmed), vs. today's channel-switch drop-off | ≥ 65% flow completion; ≥ 50% of all Vitality bookings originating in-app by month 12 | 2 |
| 3 | **The anxiety gap closes** | % of visits with en-route status viewed; pre-visit inbound "is it confirmed?" WhatsApp/calls per booking | ≥ 75% en-route views; confirmation-chasing contacts down 60% | 2 |
| 4 | **Recovery is visibly working** | Daily check-in completion during active care plans; % of plans with ≥ 80% session-dot completion | ≥ 55% median daily check-in adherence; ≥ 85% of started plans completed | 3 |
| 5 | **Packages renew because progress is visible** | Care-plan → package renewal rate; wellness program (Glow/Shape It/IV) repeat rate | Package renewal ≥ 45%; wellness repeat booking ≥ 60% within 90 days | 3, 5 |
| 6 | **The family multiplies membership** | Family-circle invites sent/accepted per primary account; % of bookings made on behalf of a dependent | ≥ 1.5 accepted invites per active family account; ≥ 30% proxy bookings (validating the Noura persona) | 4 |
| 7 | **Members come back between episodes** | D30/D90 retention for post-discharge members; content-shelf weekly engagement | D90 ≥ 35% (vs. near-zero digital retention possible today); ≥ 25% of graduated members active weekly via ring/content | 3, 5 |
| 8 | **Coordinators are freed, not replaced** | % of routine inquiries (booking status, rescheduling, prep questions) resolved by AIWA/AIKA + self-serve app surfaces without human coordinator touch | ≥ 50% deflection of routine contacts; coordinator time redirected to high-touch cases; CSAT on AI-handled threads ≥ 4.5/5 | 1, 2 |
| 9 | **Revenue becomes recurring** | In-app payment share (Mada/Apple Pay/Tabby); membership-tier attach rate once the essential/advanced/elite ladder ships | ≥ 70% of app bookings prepaid in-app; ≥ 15% of active members on a recurring tier by month 12 | 2, 5 |
| 10 | **The relationship holds** | Same-caregiver continuity rate (Luna guarantee); caregiver-thread response SLA compliance; 2-tap rebooking share | ≥ 80% same-caregiver visits within a plan; ≥ 90% thread replies within stated window; ≥ 40% of repeat bookings via "book again" | 1 |

**Reporting rhythm:** a monthly Companion Scorecard for Vitality leadership pairing one emotional metric with one commercial metric per row — because in this product, the emotional numbers are the leading indicators of the commercial ones. Emotional targets (1, 3, 4) are gate criteria for scaling marketing spend: the strategy explicitly refuses to pour acquisition into an experience that doesn't yet produce the seven feelings.

---

## 11. Strategic Risks & Mitigations (summary)

| Risk | Mitigation |
|---|---|
| **Companion positioning drifts back to portal** under feature pressure | Pillar 1 is the veto: every backlog item must name its pillar; the 12 anti-patterns from Document 02 are a standing design-review checklist. |
| **Nixpend integration depth gates the experience** (availability, write-back, records) | Sequence booking mechanics as thin UI over Nixpend early (Patterns 12/13/15 per Doc 02 dependency note); everything emotional (score, ring, journey, thread) is app-native and ships regardless. |
| **Same-caregiver guarantee vs. real roster constraints** (~30 therapists) | Guarantee within plan, with a designed, guilt-free "meet your covering specialist" handoff when unavoidable — never a silent substitution. |
| **Arabic emotional copy quality** | Cultural note 1 is binding: Arabic written natively first, English localized from it; a care-tone guide governs every system message, including AIWA/AIKA. |
| **Privacy inside the family circle** | Conservative sharing defaults, per-datatype patient control (Labayh lesson) — dignity failures are trust-ending in this market. |

---

*End of Document 03. Downstream workstreams (IA & navigation, onboarding, booking, progress & retention, family circle, visual design) should treat Sections 4, 7, and 8 as binding acceptance criteria and Sections 5–6 as the persona set for all flows and testing.*
