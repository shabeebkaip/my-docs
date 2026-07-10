# Vitality Home Care — Mobile App Information Architecture & Navigation

**Document 05 — Information Architecture & Navigation**
**Client:** Vitality Home Care (vitality.sa) — premium home healthcare, Riyadh, KSA
**Prepared by:** CodeOx — Shabeeb Kaip, Head of Operations · shabeeb.k@code-ox.com · +966 53 571 6437
**Date:** 9 July 2026
**Inputs:** Document 01 (Discovery), Document 02 (Benchmarking), Document 03 (Product Strategy), Document 04 (Experience Model & Feature Architecture)
**Feeds:** All design and engineering workstreams — this is the navigation contract.

---

## 1. IA Philosophy

The app's information architecture is a single, shallow companion canvas — not a nested medical record system. The governing rule is **depth only where intimacy requires it**: the home screen surfaces the one thing that matters right now; everything else lives exactly one tap away, never more than two. There are no more than four levels of depth anywhere in the hierarchy. The IA deliberately hides Nixpend's data model (appointments, records, invoices) behind human language layers — a booking is "Amal, Tuesday 4 pm," not a confirmation number; a visit history is "your care story," not a record cabinet. This is the structural expression of Pillar 1 (companion-first) and the primary architectural distinction from Sehhaty, Sanar, and DarDoc (whose IA is a direct reflection of their clinical backends). Navigation is optimized for State (c) — the mid-recovery program, the app's center-of-gravity state — because that is where members spend the most cumulative time and where a navigation failure most damages the companion feeling. All other states are accommodated by the adaptive home screen without changing the nav shell.

---

## 2. Tab Bar Model

The app uses a **4-tab bottom bar**. Five tabs would crowd the bar; three would overload each tab. No fifth tab ("More" / "Menu") is permitted — that pattern hides critical navigation and punishes Saleh and Abdulrahman.

The tab bar is persistent across all states except: full-screen celebration takeovers (C2), the exercise player in landscape mode (B2), and the match-reveal screen (A3) — those three contexts hide the bar and restore it on dismiss or exit.

RTL layout: tab order reverses in Arabic locale (see Section 8). Described left-to-right in LTR order below.

| Tab | Arabic label | English label | Icon | Owns |
|---|---|---|---|---|
| **T1 · Home** | الرئيسية | Home | Soft house — filled when active | The adaptive companion canvas (all 5 states). All home-screen modules M1–M10. The daily emotional loop entry points. Deep-link landing for most AIWA and notification targets. |
| **T2 · My Care** | رعايتي | My Care | Heart with a subtle medical cross — filled when active | Active and past care plans, booking history, exercise player (B2), wellness score history, check-in history, outcome evidence charts (B4), caregiver notes archive (C5), health check results (B6), wellness programs (B7). The sustained care relationship in one place. |
| **T3 · Connect** | تواصل | Connect | Chat bubble — filled when active | The care thread (D1), the AIKA voice-call button (D2), appointment assistance (D4 — reschedule/cancel flows), post-visit note reading surface, notification center. All person-to-person and member-to-care-team surfaces live here. |
| **T4 · Me** | حسابي | Me | Person silhouette — filled when active | Member profile (A7), Family Care Circle (E1–E6), payment methods (A6), notification preferences (D3, D5), privacy and sharing controls (E4), content shelf (B8), app settings, biometric/auth settings, terms. |

**Badge rules.** Unread messages in the care thread badge T3. An uncompleted check-in badges T1 with a soft amber dot (never red), cleared on completion or by end of day. Family-circle updates from dependents badge T4. No other automatic badges — anti-pattern #4 from Doc 02 (Sehhaty's notification overload).

---

## 3. Navigation Type Rules

Every transition in the app follows one of five navigation types. The type is determined by the relationship between the origin and destination, not by designer preference. This table is normative.

| Type | When to use | Motion | Back gesture | Tab bar |
|---|---|---|---|---|
| **Push (stack)** | Moving deeper into a hierarchy within a tab — e.g., Home → exercise player, My Care → single session detail, Me → privacy settings | Slide in from leading edge (right in LTR, left in RTL) | Swipe from leading edge or back button in nav bar | Stays visible |
| **Modal (full-height sheet)** | Interruptive actions that require a decision before returning: booking wizard steps 1–4 (A1), therapist match reveal (A3), payment confirmation (A6), AIKA call screen (D2), privacy setting changes (E4) | Slide up from bottom, dim background | Swipe down from drag handle; tapping background does NOT dismiss (user must make a decision) | Hidden |
| **Bottom sheet (peek)** | Supplementary detail that doesn't require leaving the current screen: appointment detail peek, quick check-in (B3) from home, en-route ETA detail, milestone detail (C3), care-thread attachment preview | Slide up; background dimmed at 40% opacity, tappable to dismiss | Swipe down or tap outside | Stays visible |
| **Full-screen takeover** | Emotional peak moments that require the full canvas: celebration (C2), exercise player in landscape (B2), match reveal animated sequence (A3), onboarding | Cross-dissolve in, no chrome | Explicit close button (top trailing corner) or automatic dismiss after celebration animation | Hidden |
| **Inline expand** | Contextual detail within the home canvas that doesn't warrant a new screen: module M3 score expansion (tap to reveal evidence chart), M5 encouragement full text, M9 family glimpse quick-read | Expand in place, no transition | Collapse tap on the same element | Stays visible |

**Rule: No modal presenting another modal.** If a flow begun in a modal requires a secondary action (e.g., adding a new address from inside booking), it pushes within the modal's navigation stack, it does not open a second modal sheet over the first.

**Rule: Push depth limit.** No push stack exceeds 4 levels within a single tab. If a flow would require a 5th level, it is redesigned as a modal flow.

---

## 4. Screen Hierarchy

Every named screen, its parent, its navigation type on entry, and its owning feature code from Doc 04.

### T1 — Home Tab

| Level | Screen | Parent | Entry type | Feature |
|---|---|---|---|---|
| L1 | **Home Canvas** | Tab root | — | C4, A2.1 (all states) |
| L2 | **Check-in Sheet** | Home Canvas | Bottom sheet | B3 |
| L2 | **Wellness Score Detail** | Home Canvas | Inline expand → Push | B5 |
| L2 | **Encouragement Full View** | Home Canvas | Inline expand | C1 |
| L2 | **En-route Status Detail** | Home Canvas | Bottom sheet | A4, D3 |
| L2 | **Milestone Celebration** | Home Canvas | Full-screen takeover | C2, C3 |
| L2 | **Quick Rebook Card** | Home Canvas | Bottom sheet → modal | A5 |
| L3 | **Score History Chart** | Wellness Score Detail | Push | B5, B4 |

### T2 — My Care Tab

| Level | Screen | Parent | Entry type | Feature |
|---|---|---|---|---|
| L1 | **My Care Root** | Tab root | — | — |
| L2 | **Active Care Plan** | My Care Root | Push | B1 |
| L3 | **Exercise Player** | Active Care Plan | Full-screen takeover | B2 |
| L3 | **Session Detail** | Active Care Plan | Push | B1, B4 |
| L2 | **Recovery Progress Overview** | My Care Root | Push | B4 |
| L3 | **Outcome Evidence Chart** | Recovery Progress Overview | Push | B4 |
| L2 | **Wellness Score History** | My Care Root | Push | B5 |
| L3 | **Single Day Score Detail** | Wellness Score History | Push | B5 |
| L2 | **Caregiver Notes Archive** | My Care Root | Push | C5 |
| L3 | **Single Caregiver Note** | Caregiver Notes Archive | Push | C5 |
| L4 | **Voice / Video Note Player** | Single Caregiver Note | Full-screen takeover | C5 |
| L2 | **Booking History** | My Care Root | Push | A7 |
| L3 | **Single Booking Detail** | Booking History | Push | A1, A7 |
| L2 | **Health Check Results** | My Care Root | Push | B6 |
| L3 | **Single Result Warm Summary** | Health Check Results | Push | B6 |
| L2 | **Wellness Programs** | My Care Root | Push | B7 |
| L3 | **Program Journey Detail** | Wellness Programs | Push | B7 |
| L2 | **Content Shelf** | My Care Root | Push | B8 |
| L3 | **Content Item Player** | Content Shelf | Push | B8 |
| L2 | **Milestones Timeline** | My Care Root | Push | C3 |
| L3 | **Milestone Detail & Share** | Milestones Timeline | Bottom sheet | C3, E6 |

### Booking Wizard (modal, launched from any tab via CTA or deep link)

| Step | Screen | Parent | Entry type | Feature |
|---|---|---|---|---|
| — | **Booking Entry Modal** | Any surface (CTA / deep link) | Modal | A1 |
| Step 1 | **Service Selection** | Booking Entry Modal | Push (within modal) | A1, A2 |
| Step 2 | **Therapist Match Reveal** | Service Selection | Full-screen takeover (within modal stack) | A3 |
| Step 3 | **Date & Time Selection** | Therapist Match Reveal | Push | A1, A4 |
| Step 4 | **Your Details** | Date & Time | Push | A1, A4, A7 |
| Step 5 | **Payment** | Your Details | Push | A6 |
| Step 6 | **Confirmation Artifact** | Payment | Push (replaces stack) | A1 |
| — | **Add / Edit Address Sheet** | Your Details | Bottom sheet (within modal) | A4 |

### T3 — Connect Tab

| Level | Screen | Parent | Entry type | Feature |
|---|---|---|---|---|
| L1 | **Connect Root** | Tab root | — | — |
| L2 | **Care Thread** | Connect Root | Push | D1 |
| L3 | **Attachment Full View** | Care Thread | Full-screen takeover | D1 |
| L2 | **AIKA Voice Call** | Connect Root | Modal | D2 |
| L2 | **Appointment Assistance** | Connect Root | Push | D4 |
| L3 | **Reschedule Flow** | Appointment Assistance | Modal | D4 |
| L3 | **Cancel Flow** | Appointment Assistance | Modal | D4 |
| L2 | **Notification Center** | Connect Root | Push | D3, D5 |

### T4 — Me Tab

| Level | Screen | Parent | Entry type | Feature |
|---|---|---|---|---|
| L1 | **Me Root** | Tab root | — | — |
| L2 | **Member Profile** | Me Root | Push | A7 |
| L3 | **Edit Profile** | Member Profile | Push | A7 |
| L2 | **Family Care Circle** | Me Root | Push | E1, E2 |
| L3 | **Invite a Member** | Family Care Circle | Bottom sheet | E1 |
| L3 | **Circle Member Detail** | Family Care Circle | Push | E2, E3 |
| L4 | **Sharing Controls** | Circle Member Detail | Push | E4 |
| L3 | **Booking on Behalf** | Family Care Circle | Modal (booking wizard variant) | E5 |
| L2 | **Privacy & Sharing** | Me Root | Push | E4 |
| L3 | **Per-datatype Sharing Settings** | Privacy & Sharing | Push | E4 |
| L2 | **Payment Methods** | Me Root | Push | A6 |
| L2 | **Notification Preferences** | Me Root | Push | D3, D5 |
| L2 | **Content Shelf** | Me Root | Push (same destination as T2 L2) | B8 |
| L2 | **App Settings** | Me Root | Push | — |

---

## 5. Adaptive Home Screen State Machine

The full module ordering per state is defined in Doc 04, Section A2.1. This section records the state-detection logic and the transition rules that IA and engineering must implement.

### 5.1 State Detection Logic

State is evaluated on every app open and on receipt of a Nixpend push event. The first matching condition wins, evaluated top to bottom.

| Priority | State | Condition |
|---|---|---|
| 1 | **(e) Family coordinator** | Active session belongs to a Circle member with coordinator role viewing a dependent's record |
| 2 | **(b) Visit day** | A confirmed booking exists for today (Nixpend booking date = today) OR en-route status event received |
| 3 | **(c) Mid-recovery** | An active care plan exists in Nixpend with at least one session completed and at least one session remaining |
| 4 | **(d) Program complete** | A care plan exists and is marked complete OR all sessions consumed; no new active plan |
| 5 | **(a) New member** | No booking history and no active plan (first-time member, or returning member fully discharged with no pending booking) |

State (b) takes priority over State (c) because the visit-day experience must dominate even when a long-running plan is active — the most urgent fact wins the home screen.

### 5.2 Module Ordering Reference (normative, from Doc 04 A2.1)

| State | Module order (top to bottom) |
|---|---|
| (a) New member | M1 · Match invitation card · M3 (lightweight check-in offer) · M8 · M9 (circle invitation) |
| (b) Visit day | M1 · M6 (en-route / confirmation) · M4 · M2 (if plan exists) · M3 · M9 (shared status) |
| (c) Mid-recovery | M1 · M2 · M3 · M4 · M6 · M7 · M5 · M8 (one pick) |
| (d) Program complete | M1 · M7 (graduation recap) · M3 · M8 · M2 (maintenance ring) · 2-tap rebook card |
| (e) Family coordinator | M1 (family variant) · M9 (as family dashboard) · M6 (proxy variant) · Booking-on-behalf card · M7 (shared celebrations) · Circle management |

### 5.3 Module Transitions

Transitions between states are not animated from the old module order to the new one — the home screen re-renders on the new state's layout at next open. Mid-session state changes (e.g., en-route event arrives while app is open) trigger a gentle cross-dissolve refresh of the home canvas, not a jarring layout jump. A loading skeleton is shown for up to 1.5 seconds while Nixpend facts are fetched; if fetch fails, the last cached state is shown with a quiet "you're offline" indicator — the home screen never presents an empty or broken state.

---

## 6. Deep Link Taxonomy

Deep links arrive from three sources: AIWA (WhatsApp), AIKA (voice agent), and the notification system (D3, D5). Every deep link must land in the correct app context without requiring the member to navigate manually. Links that arrive when the app is closed cold-launch to the appropriate screen; links that arrive when the app is backgrounded push to the foreground and animate to the target.

All deep links require the member to be authenticated. Unauthenticated deep links land on the biometric unlock screen; after unlock, the app navigates to the intended destination (not to Home).

| Source | Trigger / intent | Deep link target | Nav type on landing |
|---|---|---|---|
| **AIWA** | "Your visit is confirmed" message CTA | Home Canvas — State (b) active | Tab switch to T1, re-evaluate state |
| **AIWA** | "Your caregiver is on the way" | Home Canvas — en-route card (M6) | Tab switch to T1, en-route bottom sheet auto-opens |
| **AIWA** | "View your visit summary" | Single Caregiver Note (most recent) | Push from T2 root |
| **AIWA** | "Reschedule your appointment" | Reschedule Flow modal | Modal from T3 |
| **AIWA** | "Your check-in is ready" | Check-in Bottom Sheet | Tab switch to T1, sheet opens |
| **AIWA** | "View your health check results" | Single Result Warm Summary | Push from T2 |
| **AIWA** | "Book again with Amal" | Quick Rebook Card sheet | Tab switch to T1, rebook sheet opens |
| **AIWA** | "Invite your family" | Invite a Member sheet | Tab switch to T4 → Family Care Circle → sheet opens |
| **AIKA** | Post-call: "I've sent you your booking summary" | Booking Confirmation Artifact | Push from T2 Booking History |
| **AIKA** | Post-call: "View available slots" | Date & Time Selection (booking wizard step 3) | Booking wizard modal opens at step 3 |
| **AIKA** | Post-call: "Your question has been sent to Areeba" | Care Thread | Push from T3 |
| **Notification** | T-24h visit reminder (D3) | Home Canvas — State (b) pre-visit | Tab switch to T1 |
| **Notification** | Exercise nudge | Active Care Plan screen | Push from T2 |
| **Notification** | Daily check-in invitation | Check-in Bottom Sheet | Tab switch to T1, sheet opens |
| **Notification** | Milestone earned (C3) | Milestone Celebration full-screen | Full-screen takeover from any state |
| **Notification** | Caregiver note posted (C5) | Single Caregiver Note | Push from T2 |
| **Notification** | Family: care update (E3) | Circle Member Detail (for coordinator) | Push from T4 |
| **Notification** | Family: milestone shared (E6) | Milestone Detail & Share sheet | Bottom sheet from T4 |
| **Notification** | Wellness results ready (B6) | Single Result Warm Summary | Push from T2 |
| **Notification** | Care thread message (D1) | Care Thread | Push from T3, scrolled to new message |

**Fallback rule.** Any deep link whose target screen cannot be resolved (e.g., the booking it references has been cancelled) lands on Home Canvas and shows a contextual inline message ("that visit has been updated — here's what's current") rather than an error screen.

---

## 7. Overlay System

Three overlay types are used. The rules below are normative and exhaustive — no overlay type may be used outside its defined purpose.

### 7.1 Bottom Sheet (Peek)

**Max height:** 60% of screen height. If content requires more, it becomes a modal.
**Drag handle:** always present, 36dp wide, 4dp tall, centered at top.
**Dismiss:** swipe-down or tap outside the sheet. Exception: check-in sheet requires the check-in to be submitted or explicitly skipped before dismissal (a gentle confirmation appears: "skip today's check-in?").
**Stacking:** bottom sheets do not stack. If a second bottom sheet is triggered from within a bottom sheet (e.g., address picker within the rebook sheet), it replaces the first, not layers over it. The exception is the full-screen exercise player launched from the care plan — that is a takeover, not a sheet.

| Sheet | Max height | Sticky footer | Used by |
|---|---|---|---|
| Check-in (B3) | 52% | "Done — see your score" CTA | Daily ritual entry from M4, notification |
| En-route detail | 44% | None — auto-updates | M6 visit-day state, AIWA notification |
| Quick rebook (A5) | 48% | "Book Amal again" primary CTA + "change something" secondary | M2 rebook card, State (d) home |
| Appointment detail peek | 40% | "Manage" → Appointment Assistance push | Booking history, confirmation artifact |
| Milestone detail (C3) | 50% | "Share with family" CTA (if E6 opted in) | M7, Milestones Timeline |
| Invite a Circle member (E1) | 44% | "Send invite via WhatsApp" CTA | Family Care Circle |
| Add / edit address | 56% | "Save address" CTA | Booking wizard step 4 |

### 7.2 Modal (Full-height Sheet)

**Presented over a dimmed background (60% black overlay).** Tapping outside does NOT dismiss a modal — the user must navigate within it or explicitly close via the leading "X" (close) button in the modal navigation bar. The close button is always in the leading position (right in Arabic RTL, left in English LTR).

**Modals have their own navigation stack.** The booking wizard (A1, A2, A3, A5, E5) is the primary example: each step pushes onto the modal's stack; the member can navigate back within the wizard without collapsing it.

**Payment confirmation** (A6) is the only modal that triggers step-up biometric auth mid-flow. The auth prompt appears as an OS-native sheet (Face ID / Touch ID prompt) over the modal; on auth failure, the payment step is not advanced.

| Modal | Steps / content | Dismissible | Feature |
|---|---|---|---|
| Booking wizard | 5 steps + confirmation | Only via explicit "X" with cancel confirmation | A1, A2, A3, A4, A6 |
| Booking on behalf (proxy) | Same 5 steps, patient context injected | Only via explicit "X" | E5 |
| AIKA voice call | Single screen — call status, mute, end | Explicit end-call only | D2 |
| Reschedule flow | 2 steps: new slot → confirm | Only via explicit "X" | D4 |
| Cancel flow | 1 step: reason → confirm with grace copy | Only via explicit "X" | D4 |

### 7.3 Full-screen Takeover

**Hides tab bar, navigation bar, and status bar.** Used for emotionally total moments where any chrome would break the feeling. All takeovers have an explicit, always-visible exit mechanism.

| Takeover | Exit mechanism | Duration logic | Feature |
|---|---|---|---|
| Milestone celebration (C2) | Tap anywhere after 2.5s animation completes; or "X" top-trailing corner | Auto-dismisses to Home after 8s if untouched | C2, C3 |
| Exercise player (B2) | "End session" button, always visible at top-trailing | User-controlled; landscape auto-rotate supported | B2 |
| Match reveal (A3) | Continues automatically to date selection after 4s; "Meet [name]" CTA available from 1.5s | Auto-advances — user is carried forward, not dropped | A3 |
| Voice / video note player (C5) | Tap-to-dismiss after note completes; "X" always available | Audio/video controlled by playback bar | C5 |
| Onboarding (pre-auth) | Cannot be dismissed mid-flow; "skip for now" available from screen 3 | User-controlled | — |

### 7.4 Toast / Inline Feedback

Toasts are used only for transient, non-critical confirmations: "Streak intact — rest day saved," "Reminder set," "Address saved." They appear at the **bottom** of the screen, above the tab bar, auto-dismiss after 3 seconds, do not stack, and are never used for errors (errors are inline within the relevant surface). Maximum one toast per user action.

---

## 8. RTL Navigation Specification

The app is **Arabic-first**. The Arabic layout is the design-of-record; English is the mirror. Every layout, transition, and icon direction rule is defined here.

### 8.1 Layout Mirroring

| Element | LTR (English) | RTL (Arabic) |
|---|---|---|
| Tab bar order | T1 Home → T2 My Care → T3 Connect → T4 Me (left to right) | T4 Me → T3 Connect → T2 My Care → T1 Home (right to left); T1 is the rightmost tab |
| Push transition direction | New screen slides in from right; back slides in from left | New screen slides in from left; back slides in from right |
| Navigation bar back button | Left edge | Right edge |
| Modal close "X" button | Leading = left | Leading = right |
| Progress ring fill direction | Clockwise | Clockwise (rings do not mirror — circular elements are direction-neutral) |
| Session dots | Left to right, start filled | Right to left, start filled |
| Care thread message bubbles | Member messages right-aligned; caregiver messages left-aligned | Member messages left-aligned; caregiver messages right-aligned |
| Swipe-to-reply in care thread | Swipe right on message | Swipe left on message |
| Home screen module content alignment | Leading = left | Leading = right |
| Bottom sheet drag handle | Centered (no change) | Centered (no change) |
| Icon directionality | Chevrons, arrows, back indicators all mirror | All directional icons flipped; non-directional icons (heart, home, check) do not flip |

### 8.2 Typography in Dual-Language Surfaces

Some screens carry mixed Arabic and English content (e.g., caregiver credentials, medication names, numerical values). The rules:

- **Paragraph-level language:** Set the `textDirection` / `writingMode` attribute at the paragraph level, not the screen level. An Arabic screen can contain an English sentence if the sentence is English (e.g., a caregiver's English-language bio segment).
- **Numerals:** Eastern Arabic-Indic numerals (٠١٢٣٤٥٦٧٨٩) used throughout Arabic interface except: dates displayed in a calendar picker (Western Arabic numerals for grid legibility) and payment amounts (Western Arabic numerals, per KSA banking convention).
- **Mixed inline text:** Arabic text wraps to Arabic line-height rules (1.8× body size); do not apply Latin line-height to Arabic strings.
- **Font stack:** Arabic typeface loads first; Latin fallback is activated only when the system detects a Latin-script string. Both faces must be loaded at app launch — no late-loading flash of unstyled text.

### 8.3 Prayer-Time Navigation Constraints

The notification governor (D5) suppresses pushes during the five prayer windows. The equivalent rule applies to **modal interruptions**: no modal may auto-trigger during a prayer window. Auto-triggered modals (e.g., post-visit survey) are queued and delivered on prayer-window exit. User-initiated modals (e.g., the member tapping "book now" during prayer time) are permitted — the constraint applies to system-initiated interruptions only.

### 8.4 Elderly-First Touch Targets

All primary daily-action interactive elements — check-in sliders (B3), exercise player controls (B2), care thread send button (D1), AIKA call button (D2), rebook CTA (A5) — have a minimum touch target of **56dp × 56dp**, exceeding the WCAG 44px minimum. Secondary actions (edit, settings, secondary CTAs) observe 44dp minimum. The 56dp requirement is a production constraint, not a guideline.

---

## 9. Navigation Contract Summary

This table cross-references every feature code from Doc 04 to its primary screen home and its tab.

| Feature code | Feature name | Primary screen | Tab | Can also be reached from |
|---|---|---|---|---|
| A1 | Booking Wizard | Booking Entry Modal | Any (modal) | T1 CTA, T4 family, deep link |
| A2 | Package Booking | Service Selection (step 1 of A1) | Modal | — |
| A3 | Therapist Match Reveal | Match Reveal (takeover, step 2 of A1) | Modal | State (a) match invitation card |
| A4 | District Scheduling | Date & Time (step 3 of A1) | Modal | — |
| A5 | 2-Tap Rebook | Quick Rebook Sheet | T1 State (d) | T2 Booking History, notification |
| A6 | Payments | Payment (step 5 of A1); Payment Methods | Modal / T4 | T4 Me |
| A7 | Member Profile | Member Profile | T4 | — |
| B1 | Daily Recovery Plans | Active Care Plan | T2 | T1 M4 → push |
| B2 | Exercise Player | Exercise Player (takeover) | T2 | T1 M4 exercise card, notification |
| B3 | Daily Check-ins | Check-in Bottom Sheet | T1 (sheet) | T1 M4, notification deep link |
| B4 | Progress Visualization | Recovery Progress Overview | T2 | T1 M2 inline expand → push |
| B5 | Narrated Wellness Score | Wellness Score Detail | T1 → T2 | T1 M3 inline expand |
| B6 | Health Check Results | Health Check Results | T2 | AIWA deep link, notification |
| B7 | Wellness Programs | Wellness Programs | T2 | T1 M8 recommendation |
| B8 | Content Shelf | Content Shelf | T2 / T4 | T1 M8 |
| C1 | Encouragement Engine | T1 M5 (inline); all loop messaging | T1 | — |
| C2 | Celebrations | Milestone Celebration (takeover) | Any (interrupts) | — |
| C3 | Achievement Milestones | Milestones Timeline | T2 | T1 M7, notification deep link |
| C4 | Care Companion Presence | Home Canvas (all states) | T1 | — |
| C5 | Post-Visit Caregiver Notes | Single Caregiver Note | T2 | T1 M6, T3, AIWA deep link |
| D1 | Care Thread | Care Thread | T3 | T1 M6 one-tap, notification |
| D2 | AIKA Voice | AIKA Voice Call (modal) | T3 | T1 contextual surface (anxious moments) |
| D3 | Reminders | Notification Preferences | T4 | — |
| D4 | Appointment Assistance | Appointment Assistance | T3 | T1 M6, AIWA deep link |
| D5 | Prayer-Time Notifications | Notification Preferences | T4 | — |
| E1 | Circle Invite | Invite a Member (sheet) | T4 | T1 State (a) M9 invite card |
| E2 | Family Dashboard | Circle Member Detail / State (e) home | T4 / T1 | — |
| E3 | Care Updates | Notification Center | T3 | T4 Circle Member Detail |
| E4 | Privacy Controls | Per-datatype Sharing Settings | T4 | T4 Circle Member Detail |
| E5 | Booking on Behalf | Booking on Behalf (modal) | T4 | T1 State (e) booking card |
| E6 | Shareable Celebrations | Milestone Detail & Share (sheet) | T2 | T1 M7, C2 celebration action |

---

*End of Document 05 — Information Architecture & Navigation.*
