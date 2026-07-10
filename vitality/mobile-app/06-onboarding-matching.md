# Vitality Home Care — Mobile App Onboarding & Matching Flow

**Document 06 — Onboarding & Matching Flow**
**Client:** Vitality Home Care (vitality.sa) — premium home healthcare, Riyadh, KSA
**Prepared by:** CodeOx — Shabeeb Kaip, Head of Operations · shabeeb.k@code-ox.com · +966 53 571 6437
**Date:** 9 July 2026
**Inputs:** Document 01 (Discovery), Document 02 (Benchmarking — Pattern 5, Anti-patterns 2 & 6), Document 03 (Product Strategy §8.2), Document 04 (Feature Architecture — A3, A7, C4, E1), Document 08 (Visual Design Direction)
**Feeds:** Design and engineering for the onboarding, matching, and member-profile workstreams.

---

## 1. Philosophy & Principles

The onboarding sequence has one job before any other: earn the right to ask. Vitality's members are not filling out a patient intake form — they are deciding whether to let a stranger into their home or their parent's home. The sequence must make that decision feel safe, warm, and obvious.

**The guiding sequence:** Feel → Match → Book → Identity. In that order, without exception.

Five principles govern every screen in this flow:

1. **Understood before processed.** Every question is a statement of care, not a data-collection event. "Who are you caring for?" is not a routing flag — it is an acknowledgment that the care is real. Copy written accordingly.

2. **Deferred identity, front-loaded trust.** Name, national ID, and account creation do not appear in onboarding. They appear at the moment of booking, when the member already has a named caregiver and a confirmed slot — and they will hand over identity willingly because they want the booking to be real.

3. **Gender preference is a guarantee, not a filter.** The first matching question is not "do you have a preference?" It is stated as the default truth: female caregivers for home visits is what most families expect and what Vitality delivers. The member confirms their preference once; the system honours it forever. It is never asked again.

4. **One question per screen, no backward steps.** Each screen has a single, answerable question and a clear tap-forward. The progress indicator is ambient — a thin gold line at the top of the screen — never a fraction counter ("3/7"). Fractions create impatience; a thin advancing line creates anticipation.

5. **No anti-pattern 2, no anti-pattern 6.** No paperwork-first, no OTP on open, no account wall, no re-authentication demands inside the flow. The first screen the user sees after the splash is a warm question, not a login form.

---

## 2. Entry Paths

Three entry paths lead into onboarding. All three converge at the match reveal. What changes is the state they arrive with.

### Path A — Cold Start (New user, organic or marketing-link)

The member taps the app icon for the first time. No pre-existing session. No prior data. This is the primary path and the one all screen specs below describe in full.

**Arrives at:** Splash → Brand Moment → Onboarding Screen 1.

**State produced:** Fully guided conversational flow, 6 questions, theatrical wait, match reveal, home screen State (a).

### Path B — AIWA Deep Link (WhatsApp-originated member)

The member has already booked through AIWA (Vitality's WhatsApp agent). AIWA captured their care type and gender preference at booking time, and has passed a session token in the deep link. The app detects the token on first open.

**Arrives at:** Splash → "Welcome to the app, [name from AIWA]" bridge screen → a compressed 2-question flow (only language preference and care style preference, since AIWA already has care type and gender) → direct to the match reveal pre-loaded with the AIWA-captured caregiver if one was assigned, or a new match on those preferences → home screen State (b) if a booking exists, or State (a) if the AIWA conversation was exploratory.

**Edge case:** If the AIWA token is expired or the booking was cancelled, treat as Path A (cold start) with a soft message: "Let's find you the right specialist."

### Path C — Family Coordinator Path (Noura)

The member opens the app and on Screen 2 ("Who is the care for?") selects "A family member." From that point the flow diverges into the Family Coordinator path. See Section 6 for the full spec. This path converges back at the match reveal — the reveal is for the dependent's specialist, not the coordinator's own.

---

## 3. The Full Onboarding Sequence — Screen-by-Screen

### Screen 0 — Splash / Brand Moment

| | |
|---|---|
| **Purpose** | Brand arrival. Creates the first emotional impression: warm, premium, Arabic-first. Not a loading screen. |
| **Duration** | 1800ms. Cannot be tapped away. |
| **Surface** | navy-800 (#001C3D). Najdi geometric pattern at ≤4% opacity fades in at 600ms. Vitality wordmark in Termina 300 centered. Gold shimmer sweep across the wordmark at 1200ms (motion-ceremony timing). |
| **Copy** | Arabic wordmark. Below it, in Montserrat 400, ivory-50: **"رفيقك في التعافي"** (Your companion in recovery). No English subtitle in the splash — this moment is Arabic-first. |
| **Transition** | Fade to ivory-50 at 1800ms. Motion-gentle (350ms). |
| **Produces** | Visual tone contract. User understands: this is premium, this is Arabic, this is care. |
| **Edge cases** | If device is in low-power mode, skip the shimmer sweep but hold the 1800ms. If system language is English, the transition to Screen 1 will surface the English caption immediately — do not show English in the splash itself. |

---

### Screen 1 — Entry Question: "What brings you here?"

| | |
|---|---|
| **Purpose** | The first spoken word of the relationship. Opens the conversation without presupposing clinical context. |
| **Surface** | ivory-50. Najdi pattern ambient at 3% opacity, corners only. Gold progress line: 0% filled. |
| **Layout** | Generous top padding (72px). Question text centered. Three response cards below, stacked vertically with 12px gap, full-width, rounded-16, ivory-100 fill with navy-800 text. |
| **Arabic copy (question)** | **"ما الذي يجلبك إلينا اليوم؟"** |
| **English copy (question)** | *What brings you here today?* |
| **Response options** | 1. **أتعافى من عملية أو إصابة** — I'm recovering from surgery or injury · 2. **أهتم بشخص عزيز** — I'm caring for a loved one · 3. **أريد العيش بصحة أفضل** — I want to live with better health |
| **Interaction** | Single tap selects and advances immediately. No "Next" button. The selected card gets a gold-500 left border for 200ms as tactile confirmation before transition. |
| **What it feeds** | Routes: option 1 → post-surgical track (Abdulrahman, Reem-post-natal equivalent); option 2 → family coordinator divergence check on Screen 2; option 3 → wellness track (Lama, general wellness). Care-type preference stored in local session state. |
| **Accessibility** | All three options visible without scroll on any device ≥ 375px width. Voice-over label reads the full Arabic then the English. Large-type mode (Saleh's setting): increases card padding to 20px vertical, font-size to 20sp. |
| **Edge cases** | "None of these" is not an option — if the member pauses here, a soft prompt appears at 8 seconds: "لا عجلة — اختر ما يناسبك." (No rush — choose what fits.) |

---

### Screen 2 — Who Is the Care For?

| | |
|---|---|
| **Purpose** | Determines whether this is a personal care journey or a coordinating-family journey. Activates the Family Care Circle path early for Noura. |
| **Surface** | ivory-50. Progress line: 17%. |
| **Arabic copy (question)** | **"لمن تبحث عن الرعاية؟"** |
| **English copy** | *Who is this care for?* |
| **Response options** | 1. **لي أنا** — For me · 2. **لأحد أفراد عائلتي** — For a family member |
| **Interaction** | Single tap, immediate advance. |
| **What it feeds** | "For me" → continues to Screen 3. "For a family member" → triggers Family Coordinator flag; continues to Screen 3 but all subsequent copy shifts to proxy voice ("Tell us about the person you're caring for"). See Section 6. |
| **Edge cases** | Member may be both (Noura uses the app herself for wellness). If "For a family member" is selected, a quiet sub-prompt appears: "يمكنك لاحقاً إضافة رعاية لنفسك أيضاً." (You can add care for yourself later.) This prevents the coordinator from feeling locked out of their own health. |

---

### Screen 3 — Gender Preference

| | |
|---|---|
| **Purpose** | The most culturally load-bearing question in the flow. Positioned as the first matching question — a statement of Vitality's commitment, not a filter. For Reem (new mother) this screen is the moment of emotional reassurance that decides whether she trusts the app. |
| **Surface** | Warm blush wash: blush-200 (#F5E6E0) as the full-page background rather than ivory-50. This surface change signals: this question is different; this is about trust, not logistics. Progress line: 33%. |
| **Arabic copy (question)** | **"ما تفضيلك للمختص الصحي الذي يزور منزلك؟"** |
| **English copy** | *What is your preference for the caregiver who visits your home?* |
| **Response options** | 1. **مختصة أنثى** — Female caregiver (default state: visually pre-selected with blush-500 border) · 2. **مختص ذكر** — Male caregiver · 3. **لا تفضيل لديّ** — No preference |
| **Pre-selection rationale** | Female is visually pre-selected (not locked). The default mirrors the majority expectation without forcing a choice. The member may change it freely. |
| **Micro-copy below options** | **"هذا التفضيل مضمون في كل زيارة — لن نسألك مجدداً."** — *This preference is guaranteed for every visit. We won't ask again.* · Rendered in sand-700 italic, 13px. |
| **Interaction** | Single tap changes selection. Blush surface remains regardless of selection — this question's warmth is not conditional. |
| **What it feeds** | Gender preference flag stored as a hard matching constraint in session state. Passed to the matching algorithm as a required filter, not a scored preference. |
| **For Reem's path** | If Screen 1 indicated post-natal or mother care, the question title shifts: "ما تفضيلك للمختصة التي ترعى طفلك؟" (What is your preference for the specialist caring for your child?) — copy adaptation, same question logic. |
| **Edge cases** | If the member selects male or no preference, no confirmation dialog. The blush surface and the guarantee micro-copy remain — the guarantee applies regardless of preference. |

---

### Screen 4 — Language Preference

| | |
|---|---|
| **Purpose** | Sets the communication language for the caregiver relationship and the app's notification voice. A practical question, made warm. |
| **Surface** | ivory-50. Progress line: 50%. |
| **Arabic copy** | **"بأي لغة تفضّل التواصل مع فريق رعايتك؟"** |
| **English copy** | *In which language would you like your care team to communicate with you?* |
| **Response options** | 1. **العربية** — Arabic · 2. **English** · 3. **كلتيهما مناسبتان** — Both work for me |
| **What it feeds** | Caregiver language preference passed to matching algorithm. App notification language set. If Arabic: all system-generated care messages and check-in nudges render in Arabic first. |
| **Accessibility note** | Saleh's large-type mode: this screen also surfaces a sub-option for Arabic-Indic numeral preference (٤:٠٠ vs 4:00 for appointment times). Presented as a small toggle below the language options: "أفضّل الأرقام العربية" with a preview. Default on if system locale is Arabic-SA. |

---

### Screen 5 — Care Style Preference

| | |
|---|---|
| **Purpose** | The final preference question before matching. Humanises the caregiver assignment by capturing how the member wants to be supported — not a clinical variable, a relationship tone. |
| **Surface** | ivory-50. Progress line: 67%. |
| **Arabic copy (question)** | **"كيف تفضّل أن يدعمك متخصص الرعاية؟"** |
| **English copy** | *How would you like your care specialist to support you?* |
| **Response options** | 1. **محفّز وحاضر** — "Encouraging and present" (coaching tone, active motivation) · 2. **لطيف ومتأنٍّ** — "Gentle and patient" (soft-paced, unhurried) · 3. **مهني وموضوعي** — "Professional and focused" (clinical precision, less emotional commentary — Lama's likely pick) |
| **Illustration** | Each card carries a subtle abstract illustration (geometric, modest — consistent with Saudi cultural norms): a forward-moving arc for encouraging, a slow open circle for gentle, a clean line grid for professional. Not human faces. 40×40px, navy-100 tint. |
| **What it feeds** | Care style preference passed as a soft scoring signal (not a hard filter) to the matching algorithm. Populates the caregiver profile tag visible on the match reveal card ("Your specialist's approach: gentle and patient"). |
| **Edge cases** | Member who skips (Lama): allow skip via "تخطَّ" (Skip) link, sand-700 color, bottom-right. Skip feeds a null care-style preference; matching algorithm uses care type and gender as primary signals. |

---

### Screen 6 — Matching Wait State (Theatrical)

| | |
|---|---|
| **Purpose** | The emotional bridge between preference-giving and match reveal. Transforms a data lookup into a felt moment of investment. Lasts 2400ms minimum — even if the match resolves in 200ms, the wait is held. |
| **Surface** | navy-800 full-screen. Najdi geometric pattern at 4% opacity, slow pulse animation. Gold progress line becomes a looping arc — an animated ring building at the top of the screen, like a loading state that feels intentional. |
| **Animation sequence** | 0ms: screen cuts from ivory-50 to navy-800 (no fade — intentional hard cut to navy signals a transition to something significant). · 200ms: the Najdi pattern fades in. · 400ms: the gold arc begins its first loop. · 800ms: the first line of copy fades in. · 1600ms: the second line fades in, the first fades out. · 2400ms: the final line fades in ("Found."), and the reveal animation begins. |
| **Copy sequence (Arabic)** | Line 1: **"نستمع إلى ما شاركته معنا…"** (We're listening to what you shared with us…) · Line 2: **"نبحث في فريق متخصصينا المعتمدين…"** (We're searching our certified specialist team…) · Line 3: **"وجدنا."** (Found.) |
| **Tone** | The copy is active, not passive. "نستمع" (we are listening) is deliberately present-progressive — the system is *attending*, not *processing*. |
| **What it feeds** | During this wait, the matching algorithm receives: care type (Screen 1), coordinator flag (Screen 2), gender preference (Screen 3), language (Screen 4), care style (Screen 5). It returns: caregiver ID, name, photo URL, credentials array, specialty, years of experience, care style tag, intro video URL. |
| **Edge case — no match** | If the algorithm returns no qualified caregiver meeting the hard constraints (gender + availability): never show "no results." Transition to a coordinator-handoff screen: "متخصصتنا متاحة قريباً — سيتواصل معك فريقنا خلال ساعة." (Our specialists are available soon — our team will contact you within an hour.) Coordinator is notified immediately in Nixpend. The member lands on home screen State (a) with the Match Invitation card active. |
| **Accessibility** | `prefers-reduced-motion`: collapse to a simple text sequence at 800ms each, no animation. |

---

### Screen 7 — Match Reveal

This is the app's first emotional peak. The design and motion must honour that.

| | |
|---|---|
| **Purpose** | The named, credentialed caregiver is revealed as a person, not a result. The member forms the first emotional attachment to their specific specialist. |
| **Surface** | Opens on navy-800. Transitions to ivory-50 over 400ms as the card rises — the world lightens as the specialist arrives. |
| **Animation** | From navy-800, the caregiver's photo appears first — a circular avatar, 96×96px, rising from the bottom third of the screen with a spring ease (motion-ceremony: 1600–2400ms). The card surface (ivory-100) rises beneath the photo. Name appears next (400ms after photo settles), then credentials in sequence — each element stepping in with a 120ms stagger. The gold arc from the wait state does a single celebratory sweep and resolves as a thin gold circle around the avatar photo. |
| **Card content** | — **Circular photo** (96px, gold ring border, 2px) · — **Name in Arabic** (Termina 300, 22px, navy-800) and below it the transliteration in Montserrat 400, 15px, sand-700 · — **Specialty tag** (gold-100 pill, gold-700 text, 12px) — e.g., "متخصصة تأهيل بعد الجراحة" (Post-surgical rehabilitation specialist) · — **Years of experience** (sand-700, 13px) — e.g., "٨ سنوات من الخبرة" · — **Care style tag** from Screen 5 (sky-100 pill, sky-700 text) — e.g., "أسلوبها: لطيفة ومتأنية" · — **20-second intro video thumbnail** — a still from the caregiver's recorded video greeting, with a gold play button overlay. Tap opens the video inline (not fullscreen) so the card remains visible. · — **MOH license badge** — a small verified checkmark chip, ivory-200 fill, ink-900 text: "معتمدة من وزارة الصحة" |
| **Copy above the card** | In Termina 300, 18px, navy-800: **"وجدنا متخصصتك"** — *We found your specialist.* Below it, in Montserrat 400, 14px, sand-700: **"بناءً على ما شاركته معنا، هذه هي أفضل خبرة في فريقنا لرعايتك."** — *Based on what you shared, this is the best expertise in our team for your care.* |
| **Primary CTA** | Gold-500 CTA button, full-width: **"احجز أول زيارة مع [Name]"** — *Book my first visit with [Name]* |
| **Secondary action** | Text link below the CTA, sand-700: **"تصفّح المتخصصين الآخرين"** — *See other specialists.* Tapping this reveals a horizontal scroll of 2–3 other matched profiles, each as a compact card (photo, name, specialty). This is never the default focus — the primary match is presented with full confidence. |
| **Post-reveal action** | Tapping the primary CTA navigates to the Booking flow (Document 07). The session state now carries the matched caregiver ID. If the member does not book immediately, the match is preserved: they land on home screen State (a) with the caregiver's card as the Match Invitation card's resolved state. |
| **Accessibility** | Video auto-plays muted with captions if captions are available; does not auto-play at all under `prefers-reduced-motion`. Voice-over reads: "[Name], [specialty], [years] experience, MOH certified." |

---

## 4. Deferred Registration

Identity collection is deliberately separated from onboarding. The sequence is:

**First open → Onboarding (Screens 0–7) → Home screen → [Member explores, or proceeds to book] → Booking flow triggers registration**

At the point of first booking, the app requests:
1. **Phone number** — for booking confirmation and AIWA continuity. OTP sent once, stored. No re-OTP on subsequent opens (Anti-pattern 6 binding rule).
2. **Full name** — pre-filled from AIWA session if Path B.
3. **National ID (Iqama or Saudi ID)** — required only for packages involving insurance billing. For self-pay bookings, it is optional and framed honestly: "رقم الهوية يساعدنا في إعداد تقاريرك الطبية عند الحاجة." (Your ID helps us prepare your medical reports when needed.)

What is stored before registration:
- All preference responses (care type, coordinator flag, gender preference, language, care style) — stored in local device state, not on server.
- Matched caregiver ID — stored locally.
- The anonymous session identifier from AIWA if Path B.

After successful registration, biometric unlock (Face ID / fingerprint) is offered immediately — framed as comfort, not security: **"فعّل الدخول ببصمتك — لتفتح تطبيقك بلحظة واحدة."** (Activate fingerprint access — to open the app in a single moment.) Biometric prompt is offered once; if declined, it is accessible from Profile > Security settings and never asked again in-flow (Anti-pattern 6).

---

## 5. Family Coordinator Onboarding (Noura's Path)

The family coordinator path diverges at Screen 2 when the member selects "لأحد أفراد عائلتي" (For a family member). The conversation shifts register.

### Screen 2F — Who Are You Caring For?

After the flag is set, Screen 3 is preceded by a brief connector screen:

**Arabic:** "من العظيم أن تهتم بمن تحب. أخبرنا عن الشخص الذي تسعى للحصول على الرعاية له."
**English:** *It's meaningful to care for someone you love. Tell us about the person you're looking after.*

Surface: ivory-50. No question mark — a statement of acknowledgment, not a request.

Three relationship options follow on the same screen (secondary tap targets, smaller than Screen 1's primary cards):
- **أمي / أبي** — My mother / My father (elderly care path)
- **زوجي / زوجتي** — My spouse
- **طفلي** — My child
- **شخص آخر** — Someone else

Relationship type is stored and determines which care catalogue is surfaced in Booking (elderly care vs. paediatric vs. general).

### Screens 3F–5F — Proxy Preference Questions

All subsequent screens run in proxy voice:
- Screen 3 gender: **"ما تفضيل والدتك للمختص الصحي الذي يزور منزلها؟"** — *What is your mother's preference for the caregiver who visits her home?* (Female pre-selected. Guarantee micro-copy identical.)
- Screen 4 language: **"بأي لغة تفضّل والدتك التواصل مع فريق الرعاية؟"**
- Screen 5 care style: **"كيف تفضّل والدتك أن يدعمها متخصص الرعاية؟"**

### Dependent Profile Creation

After match reveal, Noura is invited to create a dependent profile for her mother before proceeding to booking:

**"حتى نُعِدّ رعاية شاملة لوالدتك، ما اسمها وعمرها؟"** — *To prepare complete care for your mother, what is her name and age?*

Name (Arabic): required. Age: required. Medical conditions summary: optional free text ("diabetes, hypertension — optional for now"). This is the only extended data entry in the onboarding flow, and it is framed as care preparation, not intake administration.

### Privacy Configuration for the Dependent

Immediately after profile creation, Noura sees the privacy setup screen — the only screen in onboarding that explicitly addresses data sharing:

**"ما الذي ستطّلع عليه والدتك؟"** — *What will your mother be able to see?*

Two toggles, defaulted to respecting the dependent's autonomy:
- "تستطيع والدتك رؤية من يقوم بحجوزاتها" (Your mother can see who is making her bookings) — Default: ON
- "تستطيع والدتك تلقّي رسائل تشجيعية مباشرة من تطبيقها" (Your mother can receive encouragement messages directly in her app) — Default: ON

The coordinator cannot see the dependent's mood check-ins or daily wellness scores by default — this is stated explicitly, not buried: **"ملاحظة: التحقق اليومي والمزاج خاص بوالدتك دائماً — لك أن ترى نتائج الزيارات والأهداف فقط."** (Note: Daily check-ins and mood remain private to your mother — you see visit outcomes and milestones only.)

Noura's match reveal then shows the dependent's matched specialist — the card runs identically to the main reveal, but the CTA reads: **"احجزي لوالدتك أول زيارة مع [Name]"** — *Book your mother's first visit with [Name].*

---

## 6. Returning Member Experience (AIWA Deep Link — Path B)

When the member arrives via a WhatsApp deep link from AIWA, the app has three pieces of prior context: care type, (optionally) gender preference, and the member's first name from the AIWA conversation.

**Bridge screen (replaces Screens 0–2):**

Surface: ivory-50. Vitality wordmark small at top-center. Large centered greeting:

**"أهلاً [Name]، يسعدنا أن تكون معنا في التطبيق."**
*Welcome [Name], we're glad you're here in the app.*

Below the greeting, a soft single line in sand-700: **"واصلنا من حيث توقفنا في المحادثة."** — *We're picking up where we left off in the conversation.*

The bridge screen transitions at 2000ms or on tap. It flows directly to:
- Screen 4 (Language preference) and Screen 5 (Care style preference) — the only two questions AIWA cannot reliably capture.
- Then straight to the matching wait state and reveal.

If the member already has a booked appointment in Nixpend (i.e., the WhatsApp booking completed), the match reveal is replaced by a booking confirmation card:

**"حجزك مؤكّد مع [Caregiver Name]."** — *Your booking is confirmed with [Caregiver Name].*

The card shows the same rich caregiver profile (photo, specialty, credentials, intro video) but adds the booking details (date, time, address confirmation). The primary CTA becomes **"اعرض تفاصيل زيارتك"** — *View your visit details.* Home screen landing state is State (b) — Booking Confirmed.

---

## 7. Accessibility & Cultural Notes

### Large Type (Saleh's mode)

If the device's system accessibility setting is "Larger Text" (Dynamic Type equivalent, iOS), or if Saleh explicitly sets large type in Profile > Display: all onboarding screens increase body text from 16px to 20px, card padding increases from 16px to 20px vertical, and the progress line thickens from 2px to 4px. The Arabic-Indic numeral preference (٤:٠٠ vs 4:00) surfaces on Screen 4 as described. None of these changes affect layout integrity — the question cards remain single-question per screen; no content is collapsed.

### Arabic-First Voice

All screen copy is authored in Arabic first, then adapted to English. "Adapted" — not translated. The English copy is not a literal equivalent; it matches the warmth of the Arabic register rather than its literal wording. All navigation labels (progress line, skip, CTA buttons) follow the same principle. RTL layout is the base layout; LTR is the mirror.

### Voice-Note Intro Option

On the match reveal screen, if language preference is Arabic and care style preference is "gentle and patient," a secondary option appears below the intro video thumbnail: **"استمع لرسالة صوتية من [Name]"** — *Listen to a voice message from [Name].* This is a 15-second recorded Arabic voice greeting from the caregiver. This option exists specifically for Saleh's profile: low-moderate tech comfort, Arabic-only, prefers hearing a voice over reading credentials. The voice greeting is not mandatory for caregivers to record in v1; it is an opt-in enrichment with a "coming soon" fallback state ("رسالة صوتية قادمة قريباً").

### Prayer-Time Awareness in Onboarding

If the member opens the app and begins onboarding during a prayer window (detected from the device's geolocation and a prayer-time API call made on app open), the flow is not interrupted. Prayer-time awareness surfaces in the booking flow (Document 07), not in the onboarding questions. However: if the onboarding sequence is abandoned mid-flow during a prayer window and the member returns within 90 minutes, they are returned to the screen they left — not restarted. Session state is preserved locally for 24 hours.

### Female-Caregiver Guarantee — Visual Reinforcement for Reem

For Reem's path (new mother, post-natal care), the warm blush surface introduced in Screen 3 (Gender Preference) persists subtly — as a blush-100 tint on all subsequent card backgrounds — through to the match reveal. The match reveal for Reem shows a caregiver with the specialty tag "متخصصة رعاية ما بعد الولادة" (Post-natal care specialist). The guarantee micro-copy from Screen 3 is echoed quietly on the match reveal card: a blush-100 pill reading **"مختصة أنثى — مضمون"** (Female specialist — guaranteed), 11px, sand-700. This is the only screen in the app where the gender guarantee is made visually explicit at the card level, because for Reem it is the primary source of trust.

---

*End of Document 06.*
