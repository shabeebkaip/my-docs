# Al Qalam Learning — Pre-Proposal Analysis

**Date:** 2026-06-28
**Lead:** Al Qalam Learning (Islamic school / madrasa)
**Ask:** Mobile app (iOS + Android) + Web app
**Owner:** Shabeeb K — CodeOx

---

## 1. What they actually asked for

A combined **School ERP + LMS + Islamic-education platform**, delivered as a parent/student mobile app, a teacher/admin portal, and a web counterpart.

18 functional modules across:
- School operations (attendance, fees, exams, admissions, calendar)
- Learning (materials, homework, live classes, assessments)
- Roles (student, parent, teacher, admin)
- Islamic layer (Quran/Hifdh tracker, Salah tracker, Adhkar, Hadith, Musabaqa)
- Comms (notifications, chat, support)
- Extras (multi-language EN/ML, dark mode, offline PDFs, future AI assistant)

**Honest size read:** Comparable in scope to Classera / Teachmint / Edmingle + a custom Islamic module. This is a 6–9 month build for a competent small team if scoped right, 12+ months if everything ships at once.

---

## 2. Build vs. Buy — the question they probably haven't asked themselves

Generic school ERP/LMS already exist (Classera, Teachmint, Edmingle, ClassDojo). What does NOT exist off-the-shelf is the **Islamic layer**: Hifdh tracker, Salah tracker, Tilawah recordings, Musabaqa, Adhkar/Hadith/Seerah content, Malayalam.

**Three real options to present:**

| Option | What it is | Cost shape | Time |
|---|---|---|---|
| **A. Full custom** | Build everything from scratch | Highest | 9–12 mo |
| **B. Hybrid (recommended)** | White-label an existing LMS for the school-ops modules + custom-build the Islamic layer + custom branding | Medium | 4–6 mo |
| **C. Phased custom** | Build only MVP modules now (custom), defer rest | Medium-low | 3–4 mo MVP |

We should present B and C — A is the over-engineered default we should talk them out of unless they have strategic reasons (e.g., they want to resell this to other madrasas later, which would change the answer).

---

## 3. Phasing — do NOT ship 18 modules at once

Recommended phase split:

**Phase 1 — MVP (3–4 months)**
- Auth + role-based access (student / parent / teacher / admin)
- Student profile, class/section
- Attendance (teacher marks, parent/student views, monthly report)
- Homework (assign, submit photo/PDF, feedback)
- Notes / materials (PDF upload, download, offline view)
- Notifications (push + in-app)
- Fees view + payment history (display only; gateway in Phase 2)
- Academic calendar
- Multi-language EN + ML

**Phase 2 — Engagement & Islamic core (2–3 months)**
- Live class integration (Zoom/Meet deep link, not custom WebRTC)
- Recorded classes (just video links — YouTube unlisted or Vimeo)
- Online exams + quizzes
- Marks, grades, report cards
- Online fee payment (gateway integration)
- **Hifdh tracker + Surah memorization**
- **Salah tracker + prayer reminders**
- Daily Adhkar, Hadith of the week, Dua collection
- Certificates + achievement badges

**Phase 3 — Nice-to-have (2 months)**
- Parent ↔ Teacher chat
- Musabaqa / competition module
- Workshop registrations
- Admin contact / support ticketing
- Online admission form + document upload
- Tilawah recording uploads (needs storage strategy)

**Phase 4 — Future**
- AI homework assistant
- Advanced analytics dashboards

---

## 4. Tech stack (lazy, proven)

- **Mobile:** React Native (Expo) — single codebase iOS + Android, fast OTA updates
- **Web admin/teacher portal:** Next.js (App Router) on Vercel
- **Backend:** Supabase (Postgres + Auth + Storage + Realtime) — covers auth, DB, file storage, push token mgmt, realtime notifs in one
- **Payments:** Razorpay (if India) / HyperPay or Tap (if KSA/Gulf) — confirm region first
- **Live class:** Zoom SDK deep link or Meet link — DO NOT build custom video
- **Push:** Expo Notifications + Supabase trigger
- **AI (Phase 4):** OpenAI / Claude API via Vercel AI Gateway

Why this stack: minimum moving parts, max reuse, single dev can own most of it, scales fine for one school or 50.

---

## 5. Risks & scope-creep traps

- **"AI homework assistant (future upgrade)"** → quote it as Phase 4, don't include in initial pricing
- **Chat system** → already marked optional; defer to Phase 3
- **Tilawah recording uploads** → audio storage costs grow fast; cap file size, max minutes, retention policy
- **Multi-language** → EN + ML only; lock the scope, don't let Arabic UI sneak in unscoped
- **Live classes** → integration only, not native video — make this explicit in contract
- **"Premium" features** (dark mode, offline PDF) → fine, but baseline; not "premium"
- **Single school vs. multi-tenant** → huge architectural fork; must ask before quoting

---

## 6. Questions we MUST ask the client before quoting

Send these to them as a discovery questionnaire:

**Business / scale**
1. One school/madrasa, or multiple branches? (multi-tenant?)
2. Roughly how many students, teachers, parents in year 1? Year 3?
3. Are you planning to license this to other madrasas later? (= product vs. project)
4. Region / country? (payment gateway, hosting, compliance)
5. Existing systems they use today (any ERP, WhatsApp groups, Google Classroom)?

**Product**
6. iOS + Android both at launch, or one first?
7. Is the web app for admins/teachers only, or also a full parent/student web experience?
8. Languages confirmed: English + Malayalam — anything else (Arabic UI)?
9. Live classes: Zoom or Meet preference? Do they already have licences?
10. Payments: which gateway? Do they collect fees online today?
11. Quran Tilawah recordings — student-uploaded audio? How long avg? Reviewed by ustadh?
12. Any compliance requirement (data residency, child data protection, KSA PDPL / India DPDP)?

**Commercials & timeline**
13. Target launch date?
14. Budget range expectation?
15. Who owns the IP — them, us, joint?
16. Maintenance / support model after launch (SLA expectations)?

---

## 7. Recommended next step

1. Send the **discovery questionnaire** (Section 6) — do not quote without answers
2. Based on answers, decide: **Option B (hybrid)** or **Option C (phased custom)**
3. Then build the proposal (Phase 1 scope + price + Phase 2 outlook)

Do NOT send a full 18-module fixed-price quote. That's how projects die.

---

*Next file in this folder: `02-discovery-questions.md` (clean version to send to client) once analysis is signed off.*
