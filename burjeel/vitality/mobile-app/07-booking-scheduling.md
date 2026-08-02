# Vitality Home Care — Mobile App Booking, Scheduling & Transaction Flows

**Document 07 — Booking, Scheduling & Transaction Flows**
**Client:** Vitality Home Care (vitality.sa) — premium home healthcare, Riyadh, KSA
**Prepared by:** CodeOx — Shabeeb Kaip, Head of Operations · shabeeb.k@code-ox.com · +966 53 571 6437
**Date:** 9 July 2026
**Inputs:** Document 01 (Discovery — dormant booking vocabulary), Document 02 (Benchmarking — Patterns 12, 13, 15; Anti-patterns 2, 11), Document 03 (Product Strategy — Pillar 2, §8.3), Document 04 (Feature Architecture — Layer A, C3 boundary map), Document 08 (Visual Design — §5.8 Booking Wizard)
**Feeds:** Design and engineering for the booking, scheduling, payment, and visit-day workstreams.

---

## 1. Booking Philosophy

The target feeling is stated in Document 03 §8.3: **"That was effortless — and it's truly arranged."** Momentum, then certainty. The booking flow earns that second clause through two acts: a wizard that moves without friction, then a confirmation artifact that makes the arrangement visible and permanent.

The flow's content already exists. The dormant 4-step booking vocabulary in `messages/en.json` and `messages/ar.json` — service → slot → details → payment → "Booking Confirmed Successfully!" plus a booking reference — is the canonical model. This document specifies how that model becomes a native app experience: screen by screen, input by input, edge case by edge case.

Two constraints hold across every screen:

1. **The Nixpend boundary (Doc 04 C3).** Members never see Nixpend; Nixpend never renders a screen. The app reads therapist roster, availability slots, booking/visit state, pricing, and care-plan structure from Nixpend. It writes new bookings, reschedules, cancellations, check-in red flags, pre-visit intake, and exercise feedback back. Every Nixpend call is invisible to the member; every piece of data is translated into companion language before display.

2. **The cultural invariants.** Gender guarantee is immutable once set — it cannot be changed accidentally, and it is visible on every screen where care is assigned. Prayer-time windows are soft guidance, never hard blocks. Home is a threshold; address details are collected with discretion and stored with specificity.

---

## 2. The 4-Step Booking Wizard — Full Screen Specification

### Step 1 — Select Service

**Purpose:** Orient the member in what Vitality offers; get them to the right domain quickly. The service card is the emotional entry point — it must feel like choice, not a form.

**Screen content:**

- **Header:** `BOOKING` eyebrow (Montserrat 600, 12px, 0.08em tracking, navy-800) — Arabic: `احجز خدمتك`. A brief warm line below: "What brings you here today?" / "ما الذي تحتاجه اليوم؟"
- **Service cards** — a scrollable vertical list, not a grid. Each card:
  - Warm photography fill (left side, 96×96px, rounded 12px), service name (h3, ink-900), a one-line descriptor ("إلى منزلك — مرنة وآمنة"), pricing badge bottom-right (body-strong, gold-700: "من 250 ريال") where fixed-price applies.
  - Tapping a card immediately highlights it (navy-800 border 2px, gold-500 check badge top-right) and pre-selects it — no separate "confirm selection" step. The CTA button at the bottom activates.
- **Programs section** — clearly labeled with a sage-700 eyebrow "برامج التعافي" / "Recovery Programs" below the individual services. Cards for Post-Surgery Recovery, Home Care Plus, Diabetes Care use a slightly taller format with a "multi-session journey" tag in apricot-200.

**Services displayed (in order):**

Individual: Doctor Home Visit · Home Nursing Care · Home Lab Services · Caregivers · Home Physiotherapy · Beauty at Home · HydraCool · Venus Legacy · IV Vitamin Therapy

Programs: Post-Surgery Recovery Care (flagship — displayed first with a gold accent bar on the left) · Home Care Plus · Diabetes Care · Glow · Shape It · Health Check at Home

**Pricing display rule:** Services with a defined SAR range show it on the card. Programs without a fixed price show "مخصص لك" / "Personalised quote" — never a blank.

**Inputs:** Single selection (tap). Deselect by tapping again.

**Validation:** CTA "Continue" / "متابعة" is disabled until a service is selected. No error state — the button simply waits.

**Nixpend data:** None read at this step. Service menu is a local constant (12 services + programs). The dynamic availability call waits for Step 2.

**Copy direction:** Arabic-first. Service names in Arabic with English subtitle for compound-specialist terms (e.g., "HydraCool" and "Venus Legacy" keep their brand names in both languages).

**Back behavior:** Returns to wherever booking was triggered from (home screen CTA, rebooking card, service detail page). No data is lost; the step is stateless.

**Edge case — program selected by returning member who already has an active plan:** The program card shows a "برنامجك النشط" / "Already active" chip in sage-200. Tapping it navigates to the active plan screen with a message: "يبدو أن لديك برنامجاً نشطاً — هل تريد حجز جلسة ضمنه؟" / "Looks like you have this program active — would you like to book a session within it?"

---

### Step 2 — Date & Time

**Purpose:** Show real availability; handle prayer times with cultural intelligence; get to a confirmed slot without friction.

**Screen content:**

- **Header:** Service name carried over as eyebrow. Title: "متى نزورك؟" / "When shall we visit?"
- **Date picker** — horizontal scroll of date chips (3 weeks forward), Mon-Fri/Sat format in Arabic-Gregorian. Today chip labeled "اليوم". Unavailable dates (full coverage) are hidden, not greyed — the visible list is always bookable. If the next 3 days are fully booked in the member's district, the closest available date auto-scrolls into view and a soft line reads: "أقرب موعد متاح في حيّك — الثلاثاء" / "Earliest available in your district — Tuesday."
- **Time slots** — a scrollable 2-column grid of 90-minute slots from 08:00 to 21:00. Each slot shows start time only (end time visible on tap/expand). Booked slots are removed. Prayer-window slots use the sage treatment (see §10).
- **Duration note:** A light caption below the time grid — "المواعيد 90 دقيقة" / "Visits are 90 minutes" — sets expectation without overwhelming.

**Prayer-time slot model:** Full specification in §10 below.

**Inputs:** Date chip (required) → time slot (required). Both must be selected before Continue activates.

**Validation:** If a district hasn't been set yet (first-time booking), selecting a time slot triggers a soft inline prompt: "في أي حيّ؟" / "Which district?" — a compact district selector that pre-selects the saved address district if one exists in profile.

**Nixpend data:** `GET /availability?serviceId=&districtId=&from=&to=` returns bookable slots. Prayer windows come from a local prayer-time constant (Riyadh, computed monthly) merged with slot data. The API is called when Step 1 completes, pre-loading availability so Step 2 feels instant.

**Copy direction:** Time in 12-hour Arabic format ("مساءً ٤:٣٠") with 24hr available as an accessibility setting. Date in Arabic numeral with Gregorian day name ("الثلاثاء، ٨ يوليو").

**Back behavior:** Returns to Step 1 with service selection intact.

**Edge case — no slots available in district for 14 days:** The step shows the "No availability" treatment (§11). Does not proceed to Step 3.

**Edge case — member tries to book <24h notice:** Slot is available but a soft note appears: "قد لا يتسنى لنا تأكيد هذا الموعد فوراً" / "Same-day confirmation may take a moment." The slot remains selectable; the booking proceeds; care team is flagged for expedited confirmation.

---

### Step 3 — Your Details

**Purpose:** Collect the minimum context to deliver care correctly. Pre-fill everything possible. Ask nothing twice.

**Screen content:**

- **Header:** Eyebrow with service + date/time summary (e.g., "تمريض منزلي · الثلاثاء ٤:٣٠م"). Title: "بعض التفاصيل" / "A few details."
- **Patient section** — "من هذه الزيارة؟" / "Who is this visit for?" — member themselves (default, pre-selected) or a dependent from the Family Circle. On first booking with no dependents, a `+ Add a family member` link appears inline (opens a bottom sheet, not a new screen).
- **Address section** — saved addresses shown as chips. Primary address pre-selected. `+ Add address` opens a lightweight form: district picker (12 districts listed), street name, apartment/villa, building number, and the **home-entry notes field** — "ملاحظات للوصول" / "Access notes" — with a placeholder: "مدخل العائلة، اتصل قبل الوصول..." / "Family entrance, call before arriving..." This note is saved to the address profile for all future bookings.
- **Household protocol toggle** (shown only when a male caregiver is possible for the service): "هل يحتاج وجود محرم؟" / "Is a mahram required for male caregivers?" — a binary toggle, saved to the address profile.
- **Special notes** — "ملاحظات للمعالج" / "Notes for your caregiver" — freetext, 200 char. Medical context, allergies, specific instructions. A light helper: "يطّلع عليها فقط فريق الرعاية" / "Only your care team sees this."
- **Insurance section** — "هل لديك تأمين صحي؟" / "Insurance coverage?" — a toggle. When on: insurer picker (Bupa Arabia, Tawuniya, MedGulf, Al-Rajhi Takaful, AXA, Other) + policy number field. Saved from prior booking and pre-filled. Helper: "ندقق التغطية ونُعلمك قبل الزيارة" / "We'll verify coverage before the visit."
- **Gender guarantee** — not an input here; displayed as an immutable confirmation badge: "كريمة مؤكدة" / "Female caregiver — guaranteed" with a lock icon (if previously set from onboarding/matching). For first-time users of a service that has a gender preference option: a gender selector appears at the top of this step.
- **Pre-visit intake nudge** (if applicable to service — e.g., physiotherapy, post-surgery): A collapsible section "أخبرنا قليلاً" / "Tell us a little more" with 3–5 condition-specific questions (e.g., "متى أجريت العملية؟" / "When was the operation?"). Completing it shows a soft confirmation: "جيد — أمال ستكون مستعدة" / "Good — Amal will be prepared." Incomplete is allowed; a reminder fires at T-24h.

**Inputs:** Patient (required), address/district (required), notes (optional), insurance (optional), household protocol (optional, saved per address).

**Validation:** Continue button activates when patient + address are set. Insurance toggle with empty fields blocks Continue with an inline error: "أضف رقم بوليصتك" / "Add your policy number."

**Nixpend data:** None written at this step. District cross-checked client-side against the 12-district constant.

**Back behavior:** Returns to Step 2 with slot selection intact. All Step 3 fields retained in state.

**Edge case — district not covered:** If the address district falls outside the 12 covered, a soft inline message: "هذا الحيّ ليس ضمن نطاقنا بعد — يمكنك تجربة حيٍّ مجاور أو التواصل معنا" / "This district isn't covered yet — try a nearby area or contact us." See §11.

---

### Step 4 — Payment → Confirmation

**Purpose:** Close the transaction cleanly; produce the Confirmation Artifact immediately. The payment screen should feel brief — it's a formality on the way to relief.

**Screen content (Payment):**

- **Order summary card** — ivory-100 surface, rounded 16px:
  - Service name + date/time + caregiver (if pre-matched) or "سيُحدد المعالج قريباً" / "Caregiver to be confirmed"
  - Patient name + district
  - Gender guarantee badge (if applicable)
  - Line-item pricing: service fee (SAR), insurance deduction (if verified, shown as negative line), total in bold numeral-hero style
- **Payment method selector:**
  - Mada: bank card icon + last-4 if saved, or "أضف بطاقة" / "Add card" (inline tokenisation, no redirect)
  - Apple Pay: Apple Pay button rendered natively per HIG (never a custom recreation)
  - STC Pay: shown as available option from fast-follow v1.1 onward
  - Tabby / Tamara: shown only when order total ≥ SAR 1,000 (package bookings); displayed as "4 دفعات بدون فوائد" / "4 interest-free payments"
  - Cash on visit: not shown in payment step. Available only as a setting in the member profile (toggle). If enabled, it appears as a payment option here with a disclosure: "يُدفع عند الزيارة — لا يُجمَع في التطبيق" / "Paid at visit — not collected in app."
- **Trust footer** — every payment screen shows, above the CTA, a locked-icon line: "حجز آمن ومشفّر · Vitality Home Care" — the site's "Secure & Encrypted Booking" microcopy made literally true (TLS + tokenized card, no raw card data in app).
- **CTA:** "تأكيد الحجز" / "Confirm Booking" — gold-500 fill, ink-900 text, woven-linen texture on press.

**Nixpend data:** `POST /bookings` — writes: serviceId, patientId, slotId, districtId, addressId, notes, insuranceId, caregiverId (if pre-matched), paymentMethod. Returns: bookingReference, confirmedCaregiver, totalCharged.

**Back behavior:** Returns to Step 3 with all details intact. Payment method selection is retained.

**On payment success:** Immediate transition to **Confirmation Artifact** screen (not a toast, not a modal — a full screen).

**On payment failure:** Inline error beneath payment selector — "لم تنجح المعاملة — جرّب طريقة دفع أخرى" / "Payment didn't go through — try another method." CTA resets; no exit from flow.

---

## 3. Service vs Program Booking

**Single-service booking** (Doctor, Nurse, Lab, Caregiver, Beauty, IV Therapy, HydraCool, Venus Legacy): runs the 4-step wizard as specified. Results in one confirmed visit. Rebooking is available immediately from the confirmation artifact.

**Program/package booking** (Post-Surgery Recovery, Home Care Plus, Diabetes Care, Glow, Shape It): Step 1 routes into a pre-wizard program overview screen before the 4 steps begin:

- **Program overview screen:** Full-bleed warm photography, program name in Termina display, a 3-bullet "what's included" section, session count + cadence ("12 sessions over 6 weeks"), total price or quote-request CTA, and testimonials pulled from Nixpend review data. The primary CTA "ابدأ رحلتك" / "Begin your journey" enters Step 1 with the program pre-selected.
- After payment confirmation, the program booking **instantiates a care plan** in Nixpend (`POST /care-plans`) with session milestones, a named finish line authored from a template, and the first session scheduled. The Confirmation Artifact for a program booking shows the full session-dot journey previewed below the booking reference — not just one visit, but the whole arc visible from day zero.
- **Pre-visit intake for programs** is more detailed: 5–8 condition-specific questions that feed the care plan. These are presented within Step 3 and are strongly nudged (not required) — "تُساعد إجاباتك معالجتك في إعداد خطة مخصصة تماماً لك" / "Your answers help your caregiver prepare a plan that's truly yours."

---

## 4. The Confirmation Artifact

**What it is:** A full-screen card that IS the relief moment. Not a summary screen. Not a receipt. An artifact — something the member will look at again.

**Design (Doc 08 §5.8):**

- **Surface:** navy-800 (#001C3D) full-bleed background
- **Corner ornaments:** gold muqarnas arabesque marks, four corners, 40×40px opacity 60% — Najdi heritage, not decoration
- **Booking reference:** Termina numeral-hero, gold-400 (#D4B67C), large, centered — "REF 240819-04" — the member's proof
- **Status line:** "تم تأكيد حجزك" / "Your booking is confirmed" in Montserrat 600 18px, off-white (#F2EFE8)
- **Service + date/time block:** body-strong, off-white
- **Gender guarantee badge:** small locked icon + "كريمة مؤكدة" / "Female — guaranteed" in sage-200, always visible
- **Caregiver mini-card:** If a caregiver is confirmed: circular photo (48px), name in h3 off-white, role caption. If pending: "سيُخصص لك معالج قريباً" / "Your caregiver will be assigned shortly" — never a blank.
- **Actions row (3 icons, bottom):**
  1. Calendar add (adds to iOS/Android native calendar with title, address, caregiver note)
  2. Share (WhatsApp-first share sheet: deep link back to booking + confirmation text)
  3. Reminder settings (opens reminder cadence sheet: T-24h / T-2h toggles, prayer-time-aware)
- **Reminder cadence default:** T-24h on (includes prep checklist) + morning-of visit reminder, T-2h on.

**Persistence:** The confirmation card persists as the top module on the home screen (State b) until the visit is marked complete by the care team in Nixpend. On home it appears as a compressed version (photo, name, date/time, ETA if visit day) with a "تفاصيل الحجز" / "Booking details" tap target.

**For program bookings:** The artifact adds a session-dot preview strip below the caregiver card: 12 grey dots, first one glowing gold — "رحلتك من ١٢ جلسة بدأت" / "Your 12-session journey has begun."

---

## 5. 2-Tap Rebooking — "My Usual" (Feature A5)

**Grammar:** Zeel's — after every completed visit, one card surfaces on the home screen and in the post-visit handoff. Its copy: "احجز مع أمل مجدداً — نفس الوقت الأسبوع القادم؟" / "Book Amal again — same time next week?"

**What "My Usual" saves:**

- Caregiver ID (the person, not just the role)
- Gender guarantee (locked forever — it followed from onboarding)
- Service type
- Last address + home-entry notes
- Preferred time slot (day-of-week + hour)
- Payment method last used

**Trigger points:**

1. Post-visit handoff card (appears ~30 minutes after visit-complete state in Nixpend — see §7)
2. Home screen State (d) — maintenance mode: the 2-tap rebook card as module 6
3. Thursday 9pm (and any saved preferred time window) — a push notification: "مستعدة لأمل يوم ثلاثاء؟" / "Ready for Tuesday with Amal?" Deep-links to the pre-filled confirmation step.

**The 2-tap flow (Lama's 11-second path):**

1. Tap the rebooking card on home → full-screen pre-filled Step 4 (payment + order summary) with all defaults loaded. The wizard's Steps 1–3 are skipped — they're satisfied by saved preferences. A light "تفاصيل الحجز" / "Booking details" link expands to show service/date/address for review without forcing it.
2. Tap "تأكيد الحجز" / "Confirm Booking" → Apple Pay sheet (or saved Mada) → Confirmation Artifact.

**If any saved detail has changed** (caregiver unavailable that slot, address deleted): the flow inserts only the broken step before the payment screen. It says which detail needs updating — never restarts from Step 1.

**Family favorite:** For Noura booking for her mother, "My Usual" for her mother's profile is stored under the dependent record. The rebooking card for coordinator sessions reads: "احجز كريمة لوالدتك — نفس الوقت؟" / "Book a nurse for your mother — same time?"

---

## 6. Booking-on-Behalf — Noura's Proxy Flow (Feature E5)

**Model:** One Vitality account (Noura) contains a Family Care Circle with dependent profiles (mother, etc.). Noura can initiate a booking from her home screen on any dependent's behalf. Payment always comes from Noura's own wallet/card. The visit record is attached to the patient (mother). The confirmation goes to Noura's device.

**Entry points:**

- Home screen M9 (family dashboard) → "احجز لوالدتك" / "Book for your mother"
- Booking-on-behalf card within the dependent profile view
- The 2-tap "My Usual" rebooking shortcut for the dependent (described in §5)

**Step 1 modification:** Patient selector at the top of Step 1, defaulting to the dependent. A header line: "تحجزين لـ: والدتك" / "Booking for: your mother."

**Step 3 modifications:**

- The address section shows the dependent's saved addresses (not Noura's home). Noura can add new addresses to the dependent's profile directly.
- The home-entry notes for the dependent's address are carried: "مدخل العائلة، اتصل قبل الوصول" — these notes are editable by the booking coordinator.
- Gender guarantee: if the dependent's profile has a gender preference set, it appears as immutable. A clear label: "هذا الإعداد يحميها — يُعدَّل فقط من ملفها الشخصي" / "This setting protects her — change it only from her profile."
- The mahram protocol flag from the dependent's address is respected and shown as a reminder if a female-only guarantee has not been set.

**Step 4 modifications:** Payment section clearly labels: "الدفع من حسابك" / "Payment from your account" with Noura's saved payment methods. The order summary shows the dependent's name prominently.

**Confirmation Artifact — proxy variant:** Same design as §4, with an additional line: "تم الحجز بواسطة: نورة" / "Booked by: Noura." The artifact is sent to Noura's device. A notification is sent to the patient (mother) if the patient's Vitality account exists: "نورة حجزت لك زيارة الثلاثاء ٤:٣٠م — هل تريدين مراجعة التفاصيل؟" / "Noura booked a Tuesday 4:30pm visit for you — would you like to review?"

---

## 7. Visit Day Flow

### T-24h Reminder

Trigger: 24 hours before the confirmed visit time, push notification delivered at a prayer-aware window (not during Fajr, Dhuhr, Asr, Maghrib, Isha, ±15min buffer).

**Notification copy (Arabic primary):** "زيارتك غداً في الساعة ٤:٣٠م مع أمل — هل أنتَ جاهز؟" / "Your visit tomorrow at 4:30pm with Amal — ready?"

**Deep-link destination:** An in-app pre-visit card showing:
- Caregiver photo, name, role, brief bio line
- Date/time/district confirmation
- A **preparation checklist** — service-specific, pulled from the website's existing prep guides (post-surgical: "لا تتناول طعاماً ثقيلاً قبل ساعتين"; physiotherapy: "ارتدِ ملابس مريحة"). 3–5 items, tappable with a check animation.
- Pre-visit intake prompt if incomplete: "أكمل التفاصيل الطبية — ثلاث دقائق فقط" / "Complete the medical details — three minutes."
- Address and home-entry notes (visible to the member for self-check: "هل المدخل الصحيح؟" / "Is the access note correct?")

### Visit Day — En-Route Status Card

The home screen's M6 module transforms. The confirmed booking card becomes a live status card, driven by Nixpend visit state transitions:

| Nixpend State | Card display | Copy (Arabic) | Copy (English) |
|---|---|---|---|
| `confirmed` | Caregiver photo + time | "غداً، أمال ستكون لديك في ٤:٣٠م" | "Amal visits you tomorrow at 4:30pm" |
| `preparing` | Caregiver photo + soft pulse | "أمال تستعد لزيارتك" | "Amal is preparing for your visit" |
| `on_the_way` | Caregiver photo + ETA countdown | "أمال في الطريق — ٢٠ دقيقة" | "Amal is on her way — 20 min" |
| `arriving` | Caregiver photo + door icon | "أمال وصلت — ستطرق الباب خلال لحظات" | "Amal has arrived — at your door shortly" |
| `in_progress` | Caregiver photo + timer | "الزيارة جارية — أمال لديك الآن" | "Visit in progress with Amal" |
| `completed` | Post-visit card (see below) | "انتهت الزيارة — كيف كانت؟" | "Visit complete — how did it go?" |

**En-route card detail (during `on_the_way` and `arriving`):**

- Caregiver photo, name, role badge
- License badge number (for verification at compound gate — a real compound-entry need in Riyadh)
- Vehicle description (optional, if Nixpend provides)
- ETA as countdown timer (minutes only, no maps)
- ID note: "يمكن لأمان البوابة التحقق بهذا الرقم" / "Security can verify with this ID"

The en-route card is the home screen's dominant module — modules 2–5 compress to icons below it. Nothing competes with it.

### Post-Visit Handoff

~30 minutes after `completed` state in Nixpend:

- **Post-visit summary card** — warm ivory-100 surface: what was done (one sentence in plain Arabic from the caregiver note in Nixpend), caregiver's personal note, a wellbeing question ("كيف تشعر الآن؟" / "How are you feeling now?" — 3 emoji-free sentiment chips).
- **2-tap rebook card** surfaces immediately below (§5).
- If a care plan is active: the session dot for today's visit fills gold with a small animation; the journey strip shows the next dot upcoming.
- A review prompt (deferred 2h, not immediate): "كيف كانت تجربتك مع أمال؟" / "How was your experience with Amal?" — 5-star with optional text. Feeds Nixpend review data.

---

## 8. Reschedule & Cancellation — Grace-First Design (Feature D4)

**Core principle:** Alternatives before penalty. The member should feel the app is trying to solve their problem, not protect Vitality's schedule.

### Reschedule

**Entry:** Booking detail screen → "تعديل الموعد" / "Reschedule" (Montserrat 600, gold-700 text link, no destructive red).

**Flow:**

1. Current booking summary shown.
2. A soft question: "ما الذي تغيّر؟" / "What changed?" — three quick chips: "تعارض في الموعد" / "Schedule conflict", "أحتاج وقتاً آخر" / "Need a different time", "سأكون خارج المدينة" / "Out of town." Selection is optional (feeds care team context) but never blocks the flow.
3. Step 2 (Date & Time) opens with the same service and patient pre-loaded. The current slot is marked "موعدك الحالي" and the system suggests ±3 adjacent slots first (Doc 02 Pattern 13: alternatives surfaced, not a blank calendar).
4. Confirming a new slot: `PATCH /bookings/{id}` with new slotId. Confirmation Artifact updates with new time. Caregiver is notified by Nixpend.
5. The caregiver is preserved through the reschedule unless they are unavailable at the new slot — in which case (§11 caregiver substitution flow) the member is informed before confirming.

**Cancellation policy display:** Shown as an info chip below the reschedule CTA, not leading with it: "إلغاء مجاني قبل ٢٤ ساعة" / "Free cancellation up to 24 hours before visit." Policy is contextual — the member sees it only when they open the option, not plastered on every booking screen.

### Cancellation

**Entry:** Booking detail screen → "إلغاء الحجز" / "Cancel booking" — caption size, sand-700 color. Not a bright CTA. The member must scroll past the reschedule option to find it.

**Flow:**

1. A bottom sheet (not a full screen) with two offers before the cancellation confirm:
   - "يمكننا تغيير الموعد بدلاً من ذلك" / "We can change the time instead" (links to reschedule)
   - If within 24h cancellation window: "هل تريد التحدث إلى فريقنا؟" / "Would you like to talk to our team?" (opens AIWA care thread)
2. A second tap on "إلغاء الحجز" within the sheet produces the final confirm: "هل أنتَ متأكد؟" / "Are you sure?" — with cancellation policy note.
3. On confirm: `DELETE /bookings/{id}`. Refund (if applicable) is processed per the policy; a clear line appears: "سيصلك المبلغ خلال ٥–٧ أيام عمل" / "Refund within 5–7 business days."
4. Home screen returns to State (a) if no other bookings exist.

**AIWA/AIKA escalation:** Any reschedule or cancellation conversation that touches a complex case (dispute over cancellation fee, medical emergency, package mid-cancel) should route to a human coordinator via AIWA. The care thread opens with context pre-loaded: "أريد تعديل موعدي" is enough — the agent sees the booking ID.

---

## 9. Payment Flow — Detail

### Mada

Tokenised card entry via the payment gateway (Moyasar or HyperPay — to be confirmed with client). The in-app card form uses native iOS/Android text fields with autofill from the wallet. Saved card shows masked PAN + bank logo. OTP via SMS for 3DS. No redirect — entirely in-app.

### Apple Pay

Native Apple Pay sheet, presented exactly per Apple HIG. No custom Apple Pay button artwork — use the system-provided sheet trigger. Biometric (Face ID/Touch ID) authentication is the confirmation step. Receipt delivered to Apple Wallet + Vitality payment history.

### Tabby / Tamara

Shown only when order total ≥ SAR 1,000 (program bookings). The option is labeled "قسّم على ٤ دفعات بدون فوائد" / "Split into 4 interest-free payments" with the provider logo. Tapping opens a bottom sheet with the installment preview before routing to the provider's embedded SDK. Requires the member's Saudi National ID number (captured once, stored encrypted in profile). The Confirmation Artifact shows installment schedule inline.

### Insurance capture

Step 3 collects insurer + policy number. At payment step, an inline status chip shows the verification state: "يتم التحقق من التغطية" (apricot-200, pending) or "التغطية مؤكدة — خصم ٢٠٠ ريال" (sage-200, confirmed). If verification fails before the visit: a push notification: "لم نتمكن من التحقق من تأمينك — تواصل معنا أو ادفع الآن وسنسترد لك الفرق" / "We couldn't verify your insurance — pay now and we'll refund the difference." Full CHI integration is a v2 roadmap item.

### The trust footer

Every payment screen — Step 4, package overview, Tabby sheet — shows below the CTA:

```
🔒  حجز آمن ومشفّر · Vitality Home Care
```

Navy-800 text on ivory-200 background. `caption` size (13px). The padlock icon is the system SF Symbol / Material icon — never a custom SVG. This is the site's "Secure & Encrypted Booking" phrase carried into the native experience.

### Receipts and payment history

Member profile → "المدفوعات" / "Payments" — a chronological list of transactions: service name, caregiver, date, amount, payment method, status (paid/refunded/pending). Each row taps to a full receipt (PDF-exportable). Insurance claims show separately in a sub-section: "مطالبات التأمين" / "Insurance claims."

---

## 10. The Prayer-Time Slot Model

Prayer times in Riyadh are not variable obstacles — they are the structure of the day. The slot picker must treat them as such: known, respected, and informative rather than merely blocking.

**Implementation:**

- Prayer windows are computed from a monthly Riyadh prayer-time constant (Fajr, Dhuhr, Asr, Maghrib, Isha ± 15 minutes). This constant is bundled with the app and refreshed monthly.
- In the Step 2 time-slot grid, prayer-window slots are rendered in **sage-200 background (#E3EBE1)** with a small crescent-and-muezzin icon (14px, sage-500, right-aligned within the chip).
- They are **not greyed**, not strikethrough, not removed — they are present and selectable, with a soft visual distinction.
- Tapping a prayer-window slot triggers a brief bottom-sheet tooltip (200ms open, tap anywhere to dismiss): "هذا الوقت يتداخل مع وقت الصلاة — يمكننا التنسيق حول ذلك" / "This slot overlaps with prayer time — we can coordinate around this." The member can still select and book the slot; the note gives them agency.
- If the member selects a prayer-window slot, a confirmation note is added to the caregiver brief in Nixpend: "الزيارة تتداخل مع وقت الصلاة — يُرجى المرونة" / "Visit overlaps with prayer time — please be flexible."
- Fajr (05:00–06:30 approx.) and Isha (21:00+) boundaries constrain the slot grid naturally — the grid runs 08:00–21:00 and covers no Fajr slots, keeping the implementation minimal.

**What this is not:** Prayer windows are never shown as "unavailable" or "blocked." The visual treatment is a soft cultural signal, not a hard gate. Members who pray at different times or who do not observe are not asked to identify themselves.

---

## 11. Edge Cases & Error States

### No availability in district

Triggered when Nixpend returns zero available slots for the selected district in the next 14 days.

**Treatment (Step 2):** The time-slot area is replaced by a warm card on ivory-100: "لا مواعيد متاحة في حيّك هذا الأسبوع" / "No availability in your district this week." Below: two offers:
1. "جرّب حيٍّ مجاور" / "Try a nearby district" — district picker resets.
2. "أخبرنا وقتك المفضل — سنتواصل معك عند توفّره" / "Tell us your preferred time — we'll reach out when it's available." Opens a lightweight waitlist form (date range + preferred time + notification on). Writes to Nixpend as a demand signal.

### Caregiver substitution

Triggered when: a rebook attempt finds the saved caregiver unavailable at the requested slot; or the care team substitutes a caregiver between booking and visit.

**Pre-booking substitution (rebooking):** The 2-tap flow surfaces a note before the payment screen: "أمال غير متاحة في هذا الوقت — يمكنك اختيار وقت آخر أو طلب كريمة أخرى من نفس التخصص" / "Amal isn't available then — choose another time or request another specialist with the same specialty." Two CTA buttons (not a destructive modal). Gender guarantee is explicitly preserved in either path.

**Post-booking substitution (caregiver change):** Push notification to member: "تم تغيير كريمتك لهذه الزيارة" / "Your caregiver for this visit has changed." Notification deep-links to an updated Confirmation Artifact showing the new caregiver mini-card. A care thread message from the coordinator appears simultaneously: "نأسف لهذا التغيير — سارة ذات خبرة نفس مستوى أمال وستكون جاهزة لزيارتك" / "We're sorry for the change — Sara has the same expertise as Amal and will be ready for your visit." Gender guarantee explicitly confirmed in the message.

### Payment failure

**Inline treatment (Step 4):** Error appears below the payment selector without closing the flow. Copy: "لم تنجح المعاملة — تحقق من بياناتك أو جرّب طريقة أخرى" / "Payment didn't go through — check your details or try another method." CTA resets to active. The booking is not created until payment succeeds. No error code, no bank reference number — just a clear next step.

**Apple Pay failure:** System handles the error dialog. Vitality's UI shows a brief retry nudge: "جرّب مرة أخرى أو اختر Mada" / "Try again or choose Mada."

**Tabby/Tamara rejection:** "لم يتم قبول طلب التقسيط — يمكنك الدفع بالكامل عبر Mada أو Apple Pay" / "Installment request not approved — you can pay in full via Mada or Apple Pay." Never exposes the reason for rejection (credit decision).

### District not covered

Triggered if a member enters an address in a district outside the 12 covered.

**Treatment (Step 3, address entry):** Inline, below the district picker: "هذا الحيّ خارج نطاقنا حالياً — نعمل على التوسع قريباً" / "This district isn't in our coverage yet — we're expanding soon." Two links: "اختر عنواناً آخر" / "Use a different address" + "أخبرنا أين أنتَ — ننبّهك حين نصل" / "Tell us where you are — we'll notify you when we arrive." The second link opens a one-field waitlist: district + phone/notification toggle. Zero friction, zero shame.

**The 12 covered districts** (from Doc 01, the `RIYADH_DISTRICTS` constant): Al Olaya, Al Malaz, Al Murabba, Al Sulaimaniyah, Al Nakheel, Al Rawdah, Al Yarmouk, Al Aziziyah, Al Aqiq, Al Muruj, Al Sahafah, Hittin.

---

*Document references: Doc 01 §3 (dormant booking codebase), Doc 02 §6 (Patterns 12, 13, 15; Anti-patterns 2, 11), Doc 03 §8.3 (booking philosophy), Doc 04 Layer A (features A1–A7), Doc 04 C3 (Nixpend boundary), Doc 08 §5.8 (Booking Wizard visual spec).*

*Feeds: UX design files for booking wizard, payment screens, confirmation artifact, en-route card, and reschedule/cancel flows. Engineering stories for Nixpend booking API integration, prayer-time slot computation, Mada/Apple Pay tokenisation, and Tabby/Tamara conditional display.*

---

**End of Document 07.**
