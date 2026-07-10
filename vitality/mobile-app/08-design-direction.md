# Vitality Home Care — Mobile App Visual Design Direction

**Document 08 — Visual Design Direction**
**Client:** Vitality Home Care (vitality.sa) — premium home healthcare, Riyadh, KSA
**Prepared by:** CodeOx — Shabeeb Kaip, Head of Operations · shabeeb.k@code-ox.com · +966 53 571 6437
**Date:** 9 July 2026
**Inputs:** Document 01 (Discovery — brand tokens §6, component grammar §5), Document 02 (Benchmarking — visual tone lessons, anti-patterns §5), Document 03 (Product Strategy — 5 pillars, 7 target feelings §7, personas §5)
**Feeds:** All screen-level design and frontend implementation. This document is the binding visual contract.

---

## 1. Design Philosophy — "Premium Care, Softened for Daily Life"

The website is a five-star hotel lobby: dark navy, gold shimmer, Najdi silhouettes, film grain. It was built to impress a family once, at the moment of decision — and it works. But the app is opened at 7am by Abdulrahman checking whether today's knee pain is normal, and at 11pm by Noura checking that her mother's nurse came. A lobby is somewhere you pass through; the app is somewhere you *live*. Nobody convalesces in a lobby.

**The evolution: from hotel lobby to private suite.** Same hotel, same standards, same gold — but the lighting is warmer, the surfaces are softer, and the room knows your name. We invert the website's figure-ground: the site is dark navy with ivory accents; the app is warm ivory with navy depth. Navy stops being wallpaper and becomes *structure* — the trusted, weighty moments. Gold stops being decoration and becomes *reward* — earned, celebratory, rarer and therefore more precious.

| Carries over unchanged | Adapts for daily companion use |
|---|---|
| Navy #001C3D + gold #C5A059 as the non-negotiable identity anchors | Default surface flips from navy-dark to warm ivory — daylight, not dusk |
| Termina light-weight display voice for brand moments | Montserrat takes over all UI; Termina becomes rare and ceremonial |
| Gold-shimmer highlight device (`#C5A059→#F0D98A→#C5A059`) | Reserved exclusively for celebration/milestone moments — never on buttons |
| Najdi heritage motifs (Diriyah, muqarnas, arabesque corners) | Reduced to ≤4% opacity ambient patterns; never competing with content |
| Woven-linen texture (the logo's DNA) | Survives only on the primary CTA button and celebration surfaces |
| Eyebrow-label + light headline section grammar | Eyebrows raised from 6.5–10px to a legible 11–12px; tracking relaxed |
| Trust-badge discipline (MOH, credentials) woven hotel-style | Moves from marketing chips into caregiver profile cards |
| Arabic-first voice, Aref Ruqaa calligraphy accents | Calligraphy reserved for graduation/celebration; never body UI |
| Film grain | Dropped in UI (accessibility + rendering cost); kept in photography treatment |

**Three governing tests for every screen:**
1. **The 7am test** — would a stiff 58-year-old with morning pain feel *soothed* opening this? (Calm's lesson: the app open is itself a moment of care.)
2. **The lobby test** — if it looks like the website homepage, it's too formal; if it looks like Sehhaty, it's too bureaucratic. The target is between: *quiet luxury, domesticated*.
3. **The gold test** — is this gold *earned*? Gold marks progress, celebration, and the primary action. Gold as wallpaper is forbidden.

---

## 2. Color System

### 2.1 Identity anchors (from the website, roles redefined for app)

| Token | Hex | Website role | App role |
|---|---|---|---|
| `navy-900` | #001229 | Page background | Dark-mode base; splash; celebration backdrops |
| `navy-800` | #001C3D | Primary surface | **Depth & trust surfaces**: caregiver cards, confirmation artifacts, headers of "official" moments (booking confirmed, MOH credentials), primary text on light |
| `navy-700` | #002B5B | Elevated navy | Pressed/hover states of navy surfaces; dark-mode elevated |
| `navy-100` | #E8EDF5 | Light tint | Cool wash for informational chips on ivory |
| `gold-500` | #C5A059 | CTAs, accents, eyebrows | **Progress & celebration**: filled ring segments, session dots done, primary CTA, milestone accents |
| `gold-400` | #D4B67C | Hover gold | Gold hover/active; secondary progress |
| `gold-100` | #F9F3E8 | Pale wash | Achievement chip backgrounds; celebration wash |
| `gold-700` | #9E7D41 | Muted gold | Gold text on light surfaces (AA-compliant gold) |
| Shimmer trio | #C9A84C / #F0D98A / #A88A3D | Shimmer text | Celebration Moment shimmer only — nowhere else |

**Rule:** navy = "you can trust this," gold = "you achieved this." Neither is ever a neutral.

### 2.2 Warm neutral base — the ivory family, expanded (default daily surfaces)

The website's two ivories (#F7F5F0, #F0EBE0) expand into a full daylight ramp. This is where the app *lives* — ~80% of any everyday screen.

| Token | Hex | Role |
|---|---|---|
| `ivory-50` | #FDFCFA | Page background (default light mode) |
| `ivory-100` | #F7F5F0 | Card background, grouped-list background *(site ivory)* |
| `ivory-200` | #F0EBE0 | Recessed wells, input fills, inactive ring track *(site ivory-warm)* |
| `ivory-300` | #E5DED0 | Hairline borders, dividers |
| `ivory-400` | #CFC5B2 | Disabled fills, placeholder icons |
| `sand-500` | #A89A82 | Tertiary text, timestamps, captions |
| `sand-700` | #6E6353 | Secondary text on ivory (AA: 5.9:1 on ivory-50) |
| `ink-900` | #16233A | Primary body text — navy-derived warm ink, softer than pure navy (13.9:1 on ivory-50) |

### 2.3 Therapeutic secondary palette — wellness states

Soft, desaturated, dawn-desert temperatures. These carry *state*, never brand. Each has a 500 (accent), 200 (fill), and 700 (text-on-light) step.

| Family | 200 (fill) | 500 (accent) | 700 (text) | Used for |
|---|---|---|---|---|
| **Sage** — calm, recovery, "all is well" | #E3EBE1 | #8FAE8B | #4C6B48 | Recovery score in good range, rest-day states, check-in complete, breathing/exercise player |
| **Sky** — clarity, information, hydration | #E1EBF2 | #7FA8C4 | #3D6480 | Informational banners, care-thread caregiver bubbles, hydration/vitals context |
| **Blush** — warmth, gentleness, encouragement | #F5E6E0 | #D9A08F | #9A5B48 | Gentle nudges ("ready to try again today?"), mood check-in, women's-health & post-natal contexts (Reem) |
| **Apricot** — attention without alarm | #FAEBD9 | #E0A85E | #8A6224 | "Needs your attention" — upcoming payment, reschedule needed, mild flag on a reading |

### 2.4 Semantic tokens

Anti-pattern 4 is binding: **no alarm-red for routine health data, ever.** Red exists in exactly one place — a true emergency escalation.

| Token | Light | Dark | Role & rule |
|---|---|---|---|
| `success` | #4C6B48 (sage-700) | #A8C4A4 | Confirmations, completed items — quiet, not triumphant (gold owns triumph) |
| `progress` | #C5A059 (gold-500) | #D4B67C | Anything moving forward: rings, dots, streaks, journey fill |
| `info` | #3D6480 (sky-700) | #A5C4DA | Neutral guidance, ETAs, tips |
| `attention` | #8A6224 (apricot-700) | #E8BC7A | Needs action soon — warm amber voice, paired with caregiver-toned copy, never a red badge |
| `critical` | #B3453A | #E08A80 | **Emergency escalation only** (call 937/hotline, severe red-flag check-in routing). Never on charts, scores, streaks, or missed sessions. A missed session gets blush + compassion, not red |
| `whatsapp` | #25D366 | #25D366 | WhatsApp continuity affordances only |

### 2.5 Dark mode — "the suite at night"

Dark mode is where the app returns to the website's native register — navy nights. It should feel like the site's hero gradient, calmed.

| Token | Light value | Dark value |
|---|---|---|
| `surface-page` | ivory-50 #FDFCFA | navy-900 #001229 |
| `surface-card` | ivory-100 #F7F5F0 | #06223F (navy-800 lifted) |
| `surface-raised` | #FFFFFF | #0B2C4E |
| `text-primary` | ink-900 #16233A | #F2EFE8 (warm off-white, never pure #FFF) |
| `text-secondary` | sand-700 #6E6353 | #B8AE9C |
| `border-hairline` | ivory-300 #E5DED0 | rgba(197,160,89,0.14) — the site's gold-hairline card border, inherited |
| `gold on dark` | gold-700 #9E7D41 (text) | gold-400 #D4B67C (7.1:1 on navy-900) |
| Therapeutic fills | 200-step | 500-step at 18% opacity over card |

Auto dark mode follows system; sleep-adjacent surfaces (evening wind-down content, post-Isha hours) may soft-suggest it.

### 2.6 WCAG AA contrast notes (higher floor than the website — Doc 01 §5 flagged the site's white/30–50 body text)

- Body text ≥ 4.5:1 always: ink-900/ivory-50 = 13.9:1 ✓; sand-700/ivory-50 = 5.9:1 ✓; sand-500 is **caption-only ≥ 18pt or decorative**.
- Gold #C5A059 on ivory-50 = ~2.4:1 — **gold is never text on light**; use gold-700 #9E7D41 (4.6:1) for gold-toned text, gold-500 for fills/strokes ≥ 3:1 graphical-object requirement ✓.
- White on navy-800 = 15.6:1 ✓; gold-400 on navy-900 = 7.1:1 ✓ (the site's gold-on-navy pairing survives untouched).
- Therapeutic 700-steps all ≥ 4.5:1 on ivory-50 (verified: sage 5.5, sky 5.6, blush 4.6, apricot 5.2).
- Minimum body size 16px (Saleh: "large type essential"); the website's 6.5–10px micro-labels are banned below 11px in-app.

---

## 3. Typography Scale

### 3.1 Font roles

| Font | Role in app | When |
|---|---|---|
| **Termina** (300, Syne fallback) | Display & brand voice | Splash, onboarding headlines, match reveal name, celebration headlines, empty-state headlines, section heroes. **Never** in components, forms, lists, or anything read twice a day — Termina at small sizes reads cold and mechanical |
| **Montserrat** (400/500/600/700) | The entire working UI | All body, labels, buttons, cards, navigation, data. App default weight is 400–500 (the site's 300 body weight is too faint for 58-year-old eyes on mobile) |
| **Noto Sans Arabic** (400–700) | All Arabic text, both roles | Termina has no Arabic — Arabic display uses Noto Sans Arabic 300/400 at +1 size step to match Termina's optical presence. `letter-spacing: 0` always (WebKit joining fix from the site carries over) |
| **Aref Ruqaa** (400/700) | Ceremonial calligraphy | Celebration Moments, graduation, Ramadan/Eid greetings, the "مبروك" moment. Max ~4 appearances per user-month — scarcity is the point |

### 3.2 Type scale — English (Montserrat unless noted)

| Token | Size / Line | Weight | Face | Usage |
|---|---|---|---|---|
| `display` | 34 / 40 | 300, ls −0.01em | Termina | Onboarding & celebration headlines only |
| `h1` | 28 / 34 | 300 | Termina | Screen heroes, match reveal name |
| `h2` | 22 / 28 | 600 | Montserrat | Screen titles, card group headers |
| `h3` | 18 / 24 | 600 | Montserrat | Card titles, thread names |
| `body-lg` | 17 / 26 | 400 | Montserrat | Narrated score sentences, primary reading |
| `body` | 16 / 24 | 400 | Montserrat | Default body |
| `body-strong` | 16 / 24 | 600 | Montserrat | Inline emphasis, values |
| `caption` | 13 / 18 | 400 | Montserrat | Timestamps, helper text (sand-500/700) |
| `label` | 12 / 16 | 600, ls 0.08em, uppercase | Montserrat | Eyebrows, chips — the site's 0.3–0.45em tracking relaxed to 0.08em for legibility |
| `numeral-hero` | 44 / 48 | 300 | Termina | The recovery score digit, session count |

### 3.3 Type scale — Arabic (Noto Sans Arabic, ls 0 throughout)

Arabic script has taller vertical metrics and no uppercase; sizes bump +1–2px, line-heights +2–4px, and `label` uses weight only (no letterspacing, no case).

| Token | Size / Line | Weight | Notes |
|---|---|---|---|
| `display` | 36 / 46 | 300 | Optical match for Termina display |
| `h1` | 30 / 40 | 300 | |
| `h2` | 23 / 32 | 700 | Noto Sans Arabic 600 renders lighter than Montserrat 600 — use 700 |
| `h3` | 19 / 27 | 700 | |
| `body-lg` | 18 / 29 | 400 | Narrated score — the app's most-read Arabic sentence |
| `body` | 17 / 27 | 400 | |
| `caption` | 14 / 20 | 400 | |
| `label` | 13 / 18 | 700 | No tracking, no case transform — weight carries the hierarchy |
| `calligraphy` | 30–56 fluid | 400/700 | Aref Ruqaa, celebration only |

Numerals follow device locale (Arabic-Indic ٠١٢٣ vs Western) via `locale`-aware formatting; the recovery score numeral respects it.

### 3.4 Dynamic type

All tokens map to platform text styles (iOS Dynamic Type / Android sp) and must survive +2 accessibility steps without truncating the home screen's top card. Saleh and Abdulrahman will run large text; test at 120% by default.

---

## 4. Design Tokens — Space, Shape, Elevation, Motion, Haptics

### 4.1 Spacing (4pt base, generous by default — whitespace is the cheapest luxury)

| Token | Value | Usage |
|---|---|---|
| `space-1` | 4 | Icon–label gaps |
| `space-2` | 8 | Intra-component |
| `space-3` | 12 | Chip padding, list-item internal |
| `space-4` | 16 | Screen gutter (default), card padding |
| `space-5` | 20 | Card padding (feature cards) |
| `space-6` | 24 | Between cards |
| `space-8` | 32 | Between sections |
| `space-12` | 48 | Above/below hero moments |
| `space-16` | 64 | Celebration breathing room |

### 4.2 Radius (soft and generous — companion, not clinical; no sharp corners anywhere a patient looks)

| Token | Value | Usage |
|---|---|---|
| `radius-sm` | 10 | Chips, small controls |
| `radius-md` | 16 | Inputs, buttons |
| `radius-lg` | 20 | Cards (default) |
| `radius-xl` | 28 | Hero cards (Caregiver Card, Narrated Score) |
| `radius-full` | 999 | Pills, avatars, ring elements, FAB |

The website's L-shaped gold corner ornaments survive only on the Celebration Moment and confirmation artifact — as a 24px `corner-ornament` decoration, not a component border.

### 4.3 Elevation — warm shadows, never gray

Shadows tint toward navy (depth) or gold (glow), inheriting the site's shadow DNA (`0 10px 40px rgba(7,21,38,0.3)` / `--shadow-gold`), lightened for ivory surfaces.

| Token | Value | Usage |
|---|---|---|
| `elevation-0` | none, hairline border ivory-300 | List rows, grouped content |
| `elevation-1` | 0 2px 8px rgba(22,35,58,0.06) | Resting cards |
| `elevation-2` | 0 6px 20px rgba(22,35,58,0.08) | Raised cards, bottom sheet |
| `elevation-3` | 0 12px 32px rgba(22,35,58,0.12) | Modals, en-route live card |
| `elevation-gold` | 0 8px 28px rgba(197,160,89,0.22) | Celebration surfaces, closed ring glow — the only glowing shadow |

### 4.4 Motion — calm, unhurried, breath-paced

The site's GSAP energy (back.out pops, scan sweeps, marquees) is *marketing motion*. App motion is slower, softer, and interruptible. Nothing bounces in a health app.

| Token | Duration | Easing | Usage |
|---|---|---|---|
| `motion-instant` | 100ms | ease-out | Taps, toggles, haptic-paired feedback |
| `motion-quick` | 200ms | cubic-bezier(0.25, 0.1, 0.25, 1) | Component state changes |
| `motion-gentle` | 350ms | cubic-bezier(0.33, 0, 0.15, 1) — decelerate, "settling" | Screen transitions, cards entering, sheet presentation. The default |
| `motion-breath` | 900ms | ease-in-out | Ring filling, score number counting up, ambient gradient shifts |
| `motion-ceremony` | 1600–2400ms | choreographed | Celebration Moment, match reveal, graduation. The only place shimmer, particle gold, and Aref Ruqaa animate |

Rules: fades + 12–16px translate, never zoom-pops; stagger 40–60ms; ambient home-screen gradient drifts on a ~8s breathing cycle (the site's `ambientBreath`, slowed); everything honors reduced-motion (§9).

### 4.5 Haptics

| Moment | Haptic |
|---|---|
| Check-in submitted, exercise rep done | Light impact |
| Booking confirmed, ring closed | Success notification (paired with gold fill animation) |
| Milestone / celebration | Success, then one soft light impact as shimmer settles — restrained; never a buzz-storm |
| Attention states | Single light tap. **Never** error/heavy haptics for health data |
| Emergency escalation button | Medium impact on press — deliberate weight |

---

## 5. Component System — the signature nine

Shared grammar for all: ivory surfaces, radius-lg+, one navy anchor element, gold only where progress/celebration lives, every card answerable in one glance ("is this handled?" — Feeling 1).

### 5.1 Caregiver Card — the recurring character (Pattern 4; the home screen's heart)
- **Anatomy:** portrait photo or stylized avatar (radius-full, 64–88px, hairline gold ring at 2px when "your" caregiver), name (h3), role + years (caption), credential chip (MOH/license — navy-100 fill, navy-800 text, ShieldCheck icon), status line (body, sky-700: "confirmed for Tuesday 4pm"), message affordance.
- **States:** *matched/resting* (ivory card, elevation-1) · *upcoming visit* (navy-800 card variant, white text — the trust surface) · *en-route* (promotes to En-route Status card) · *in-thread* (compact row) · *covering specialist* (blush wash header: "Amal is covering for Sara this visit — she has your full plan").
- **Tone:** a person, not a listing. No star ratings, no price, no "select" button. Photography per §7; female caregivers may opt into illustrated avatar (§6, Cultural note 5).

### 5.2 Progress Ring & Session-Dot Journey (Patterns 7 + 3)
- **Ring anatomy:** single ring (not three — one thing today), track ivory-200, fill gold-500 gradient sweep, center shows today's actions as 2–3 micro-icons or the fraction; closes with `motion-breath` fill + `elevation-gold` pulse + success haptic.
- **Journey anatomy:** horizontal dot rail per care plan; done = gold-500 filled, current = gold-400 with soft 1.5s glow pulse, future = ivory-300 outline, rest days = sage-200 dot; finish-line flag labeled in life terms ("Walking unaided" / "المشي بدون مساعدة"), Termina caption.
- **States:** active · rest-day (sage message, ring "closes" with rest credited) · missed (dot stays open, *no red, no X* — blush microcopy: "rest was probably what you needed") · plan complete (all dots lit, hands off to Celebration Moment).
- **Tone:** progress as story, never compliance dashboard. Percentages hidden; dots and the narrated sentence carry meaning.

### 5.3 Narrated Score Card (Pattern 2 — WHOOP score, Oura voice)
- **Anatomy:** greeting eyebrow (label, time-aware: "صباح الخير أبو خالد"), score numeral (`numeral-hero`, Termina 300, ink-900), state tint behind numeral (sage/sky/blush/apricot 200 wash — never a red zone), then the sentence (body-lg, the most important text in the app): "جسمك يحتاج راحة اليوم — خذها", then one suggested action chip.
- **States:** good (sage) · steady (sky) · gentle-day (blush) · check-in pending (numeral replaced by soft prompt) · red-flag (apricot card + "Amal has been notified and will call you" — the system escalates quietly, the member sees care, not alarm).
- **Tone:** a nurse's voice, not a lab report. Arabic written natively first. Never a grade, never "poor."

### 5.4 Celebration Moment (Pattern 8 — the gold budget spent all at once)
- **Anatomy:** full-screen navy-900 backdrop (the brand's night-sky register returns), gold shimmer particles (site shimmer trio), Aref Ruqaa headline ("مبروك يا أبو خالد"), Termina subline in English, milestone artifact (lit journey dots / session number), optional caregiver voice-note bubble with play button, share-to-family-circle action, corner ornaments.
- **States:** minor (inline card version — gold-100 wash, no takeover) · major (full-screen, `motion-ceremony`) · graduation (extended: evidence recap "session 1 → today", then wellness-shelf doorway).
- **Tone:** pride restored, not confetti spam. Full-screen moments are rationed (first session, halfway, streak weeks, graduation). Always dismissible in one tap.

### 5.5 Care Thread Bubbles (Pattern 6)
- **Anatomy:** caregiver bubbles sky-200 fill, ink-900 text, avatar-anchored, left/RTL-right; member bubbles ivory-200; system/care-team notices as centered navy-100 chips; response-expectation banner pinned ("Areeba replies within 3 hours, 9am–9pm"); photo attachments with pre-send blur-until-confirm for sensitive images; voice notes first-class (Saleh prefers them).
- **States:** awaiting reply (subtle breathing dot, not "seen/unseen" pressure) · caregiver replied (gentle notification) · escalation offered (after keywords/red-flags: AIKA call chip appears inline) · thread quiet hours (prayer/night notice in caption).
- **Tone:** a warm private line, not a ticketing system. No "ticket #", no bot-speak; AIWA answers appear in the same caregiver-team voice.

### 5.6 En-route Status Card (Pattern 12 — Zeel/Uber grammar, the home-threshold guardian)
- **Anatomy:** elevation-3 live card; caregiver photo large, name, license badge, gender-guarantee check ("ممرضة — كما طلبت"), live ETA (body-strong, sky-700), map strip (muted ivory cartography, navy route), ID/vehicle details expandable for gate security, call/message actions, prep checklist link.
- **States:** T-24h reminder (photo + prep list) · preparing · on the way (live ETA) · arriving (navy-800 banner: "Amal is at your door") · visit in progress (quiet state) · post-visit (hands off to summary + rebook card).
- **Tone:** certainty. This card kills the #1 anxiety; every element answers "who, exactly, and when, exactly."

### 5.7 Family Circle Avatars (Pattern 14)
- **Anatomy:** overlapping avatar cluster (radius-full, 2px ivory-50 separators); each member avatar wears a thin state ring — gold arc = today's ring progress (share-permitted data only), sage dot = visit completed today, apricot dot = needs attention; patient-controlled privacy icon (subtle lock) on non-shared facets; tap → member's shared-view dashboard.
- **States:** all-well (calm cluster) · milestone shared (gold shimmer flick on that avatar) · attention (apricot, with the *caregiver's* framing, never raw data) · invite pending (dashed outline avatar).
- **Tone:** presence without surveillance. Noura sees "handled"; her mother controls what "handled" reveals.

### 5.8 Booking Wizard Steps (the dormant 4-step vocabulary, finally rendered)
- **Anatomy:** step rail as 4 dots (same dot language as journeys — booking *is* a mini-journey), one decision per screen: service (cards with warm photography, transparent SAR pricing at last) → date/time (slot chips; prayer windows rendered as quiet sage gaps, not "unavailable" errors) → details (saved defaults pre-filled: address, gender guarantee locked, entry notes) → payment (Mada/Apple Pay/Tabby, navy trust footer with the now-true "Secure & Encrypted Booking").
- **Terminal state — the Confirmation Artifact:** navy-800 card, gold corner ornaments, booking reference (numeral style), caregiver mini-card, calendar-add, reminder cadence. This card *is* the relief moment; it persists on home until the visit.
- **States:** returning-member fast path (2-tap "book my usual" bypasses the rail) · slot conflict (apricot, alternatives offered) · payment pending (never blocks confirmation visibility).
- **Tone:** momentum then certainty. Max one question per screen; Lama finishes in 11 seconds, Abdulrahman never feels rushed.

### 5.9 Empty States that Comfort
- **Anatomy:** small warm illustration (§6), Termina headline that *reframes* ("Nothing needs your attention — كل شيء تمام"), one gentle next action, ambient Najdi pattern at 3% opacity.
- **Variants:** no upcoming visits ("Your care team is a tap away") · thread empty ("Ask Areeba anything — even at 2am; she'll answer by morning") · no family members ("Care is better together — invite your family") · post-graduation home ("You did it. We're still here.").
- **Tone:** an empty state is a *good* day in healthcare. Never "No data," never a gray void.

---

## 6. Illustration Direction

**Style: "Warm Najdi Modern"** — flat-with-soft-depth illustration; rounded forms on the app's radius grammar; palette drawn strictly from the token set (ivory grounds, navy line-work at 60–80%, sage/sky/blush scenes, one gold accent per illustration — the gold test applies to art too). Grain-free; soft long shadows suggesting Riyadh's low morning sun.

**Human representation — respectful, Saudi-authentic:**
- Modest dress always: abaya/thobe options across scenes, hijab as default option for female figures with variation, no idealized bodies. Mixed-gender scenes only where contextually correct (Cultural note 8).
- **Elderly dignity is a hard rule:** older figures are drawn upright, active, in their own majlis — receiving care as hosts, never as diminished patients. Abdulrahman must see himself with pride, not pity (his key quote is the acceptance test).
- Faces are simplified/serene (Headspace's lesson: softness without cartoon silliness); a face-free geometric-abstract variant exists for contexts where figures are better avoided.
- Caregiver figures always depicted mid-warmth: sitting *with*, kneeling *beside* — never standing over.

**Najdi heritage motifs, adapted:** the site's Diriyah/Masmak/muqarnas silhouettes become a subtle app pattern library — a single-weight geometric line pattern (triangles, crenellations, muqarnas steps) used at ≤4% navy on ivory (light) / ≤6% gold on navy (dark, celebration): onboarding backdrops, empty states, section headers, the celebration backdrop. Never behind body text, never above 8% opacity.

**Illustration vs photography:** illustration for *concepts and feelings* (onboarding, empty states, exercise diagrams, educational content, streak/rest metaphors, anything about pain or private body contexts — Reem's post-natal content is always illustrated); photography for *real people and real promises* (caregivers, en-route, testimonials, service booking). Rule of thumb: if it's about *them* (the member's feelings), illustrate; if it's about *us* (who is coming to your door), photograph.

---

## 7. Photography Direction

- **Subjects:** Vitality's actual caregivers and clinical team — the site's real DSC in-home shoot proved this works; extend it. The AI-generated fill images in the CMS (Gemini_Generated_*) are **retired from the app**; no synthetic humans in a trust product.
- **Settings:** real Saudi homes — majlis seating, warm lamps, tea trays, family thresholds. Natural light, golden-hour warmth (the palette's ivory/gold in real life). Never: hospital corridors, scrubs-with-clipboard stock, gloved-hands-with-stethoscope clichés, blue-tinted clinical lighting.
- **Treatment:** slightly warm grade (+temperature, lifted shadows toward ivory), soft film-grain allowed *in photography only* (brand texture continuity), navy bottom-fade gradient for text-overlay cards inherited from the site.
- **Caregiver portraits:** consistent kit — ivory backdrop, soft key light, genuine smile, uniform present but not dominating; shot in both hijab and non-hijab per the caregiver's own presentation; each caregiver also records the 20-second intro video against the same backdrop (match-reveal asset).
- **Dignity & modesty review:** every photo passes a cultural review (modest dress, patient consent, no exposed medical situations). Elderly members in imagery are hosts, not subjects.

---

## 8. Iconography

- **Style:** continue **lucide-react** (site continuity, RTL-friendly) — rounded caps/joins, **2px stroke** at 24px grid; sizes 16/20/24/28; outlined at rest, **filled variants for active/selected states** (tab bar, toggles, completed items).
- **Color rule:** icons are ink-900 or sand-700 on light, warm off-white on navy. **The gold-accent rule: gold icons exclusively signal progress or celebration** — the filled ring, a completed session dot's check, a milestone badge. A gold settings icon is a token-system bug.
- Therapeutic-state icons take their family's 700 (sage check, sky info, apricot bell). Critical red icon exists only on the emergency affordance.
- **Custom glyph set (draw in the same 2px grammar):** progress ring, session dot, prayer-time slot marker, family circle, majlis/home-visit, IV drip, gentle-exercise set, caregiver badge. No emoji in system UI; the care-tone guide governs any expressive characters in thread copy.
- Directional icons auto-mirror in RTL (§9); lucide's RTL-safe subset preferred.

---

## 9. Accessibility & Culture

**RTL mirroring rules (Arabic-first: design RTL, mirror to LTR):**
- All layout via logical properties (start/end); navigation chevrons, back arrows, progress direction, journey dot rails, step rails, and carousels mirror. The Progress Ring fills **clockwise in both** directions (physical metaphor, not reading order); numerals and phone numbers stay LTR inside RTL text.
- Non-mirrored: media playback icons, clock faces, brand logo, caregiver photos.
- `letter-spacing: 0` on all Arabic (inherited site rule); never letterspace or fake-italicize Arabic; the site's shimmer-italic device is EN-only — Arabic celebration uses Aref Ruqaa instead.

**Elderly-first ergonomics (Abdulrahman, Saleh — and Noura's mother viewing shared screens):**
- Touch targets ≥ 48×48dp minimum, **56dp for primary daily actions** (check-in slider, call/message caregiver, emergency); generous inter-target spacing (≥ space-2).
- Check-in inputs are big physical controls (fat slider thumbs 32dp, large tappable mood faces), one-handed reachable bottom-half placement (Reem holds a baby).
- Full Dynamic Type support to +2 steps (§3.4); minimum contrast per §2.6; voice-note input wherever text input exists.

**Reduced motion:** every `motion-breath`/`motion-ceremony` animation has a static or cross-fade equivalent; celebration falls back to a still gold card with haptic; ambient gradient drift disables; ring fills jump-cut with a fade. Honor system setting without asking.

**Arabic-first copy principles (binding, from Cultural note 1):**
- Every system string written natively in warm MSA with Saudi softness first ("حياك الله", "تم الحجز — نشوفك الثلاثاء"), then localized *to* English; the care-tone guide reviews both.
- Notifications as invitations, never demands; quiet by default during the five prayer windows and configurable night hours; Ramadan mode shifts rhythm (post-Taraweeh slots, Iftar-aware nudges).
- Kinship address forms honored (أبو خالد / أم فهد) when the member opts in during onboarding.
- No bureaucratic register (the Sehhaty tell); no transliterated English tech-speak where a natural Arabic word exists.

**Cultural non-negotiables surfaced visually:** gender-guarantee check rendered on every caregiver/en-route card; per-datatype privacy locks visible in the family circle; prayer-time slots styled as respected pauses, not unavailability errors; en-route ID details for the home threshold.

---

## 10. Governance

- These tokens are the single source of truth; screen designs may not introduce hex values, radii, or durations outside this document without amending it.
- Standing design-review checklist = the 7 feelings (Doc 03 §7) + the 12 anti-patterns (Doc 02 §5) + the three tests in §1 of this document.
- The gold budget, the red rule (§2.4), and the Arabic-first copy rule are veto-level: any screen violating them returns to design regardless of schedule.

*End of Document 08.*
