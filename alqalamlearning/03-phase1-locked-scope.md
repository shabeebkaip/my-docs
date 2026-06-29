# Al Qalam Learning — Phase 1 Locked Scope
## Based on client's ✅ / ❌ marks on the feature list

**Date:** 2026-06-28
**Status:** Draft pending 4 clarifications (see Part 4)
**Prepared by:** Shabeeb K — CodeOx

---

## Part 1 — Apps to be Built (Updated)

Client confirmed **"Mobile & Tablet & Desktop support"** → all three platforms are in Phase 1.

| # | App | Tech | Users | Phase 1? |
|---|---|---|---|---|
| 1 | **Mobile App** (iOS + Android) | React Native (Expo) | Student, Teacher | ✅ |
| 2 | **Tablet support** (same app, responsive) | React Native | Same | ✅ |
| 3 | **Web Portal — Admin + Teacher** | Next.js | Admin, Principal, Teacher | ✅ |
| 4 | **Web Portal — Student** (browser version of mobile) | Next.js | Student | ✅ |
| 5 | **Backend** (shared) | Supabase (Postgres + Auth + Storage) | — | ✅ |

> **Note:** Parent Portal was marked ❌ across the board — see clarification Q1 below before confirming this app split.

---

## Part 2 — Phase 1 Features (Client-Confirmed ✅)

### 1. Student Dashboard ✅
- Student profile
- Class & section details
- Student ID
- Attendance percentage
- Performance summary
- Upcoming classes

### 2. Live Classes (partial)
- Weekly timetable ✅
- Class reminders ✅
- *(join button, Zoom/Meet integration, recorded classes → P2)*

### 3. Learning Materials ✅
- Notes
- Worksheets
- PDF downloads
- Practice activities
- Islamic study resources

### 4. Homework & Assignments ✅
- Daily homework
- Assignment submission
- Upload photos / PDFs
- Teacher feedback
- Due-date reminders

### 5. Exams & Assessments (partial)
- Exam timetable ✅
- Marks & grades ✅
- Report cards ✅
- *(online exam + quiz → P2; teachers enter marks manually for offline exams in P1)*

### 6. Attendance Management ✅
- Daily attendance
- Monthly attendance report
- Leave application

### 7. Fees (partial — needs clarification, see Q2)
- Fee reminders ✅
- *(fee details, payment history, online payment, receipts → P2)*

### 8. Teacher Portal ✅
- Mark attendance
- Upload homework
- Upload study materials
- Enter marks
- Send announcements

### 9. Notifications ✅
- School announcements
- Exam alerts
- Holiday notices
- Event reminders
- Parent messages

### 10. Islamic Events (partial)
- Workshop registrations ✅
- *(Musabaqa, Ramadan, Dhul Hijjah activities → P2)*

### 11. Certificates & Achievements (partial)
- Download certificates ✅
- Achievement badges ✅
- Student awards ✅
- *(competition results → P2)*

### 12. Academic Calendar ✅
- School calendar
- Holidays
- Exam dates
- Events

### 13. Admission Section ✅
- Online admission form
- Document upload
- Admission status tracking

### 14. Support
- Admin contact ✅
- WhatsApp support button ✅
- *(parent support ticket — unmarked, see Q4)*

### 15. Platform / Extras
- Multi-language: English + Malayalam ✅
- Mobile, tablet & desktop support ✅
- Push notifications ✅ (implied by Section 10)

---

## Part 3 — Deferred to Phase 2+ (Client-marked ❌)

### Live Classes (P2)
- Join class button
- Google Meet / Zoom integration
- Recorded classes section

### Exams (P2)
- Online exams
- Quiz section

### Fees (P2)
- Fee details
- Payment history
- Online payment
- Download receipts

### Parent Portal — entire module (P2 — but see Q1)
- Child's progress
- Attendance view
- Homework status
- Teacher remarks
- Notifications

### Islamic Features — entire block (P2)
- **Quran Section:** Hifdh tracker, Surah memorization, Tilawah recordings, revision schedule
- **Islamic Studies:** Hadith of the week, Daily Adhkar, Dua collection, Seerah, Islamic quizzes
- **Salah Tracker:** Daily prayer log, prayer reminders, weekly report
- **Islamic Events:** Musabaqa, Ramadan activities, Dhul Hijjah activities

### Certificates
- Competition results

### Future (P4)
- AI homework assistant

### Unmarked (need decision — see Part 4)
- Parent support ticket
- Parent ↔ Teacher chat
- Parent ↔ Admin chat
- Dark mode
- Offline PDF viewing

---

## Part 4 — Clarifications Required Before Locking

There are 4 contradictions / missing marks in the client's response. These need answers before we quote.

### Q1 — Parent access in Phase 1?
**Issue:** Parent Portal was marked ❌ across all 5 items, but:
- Notifications module includes "Parent messages" (✅)
- Fee reminders ✅ — who receives them if parents aren't users?
- Homework "due date reminders" ✅ — students or parents?

**Possible interpretations:**
- (a) No separate parent login in P1 — parents view via student's account (shared credentials)
- (b) Parents are notified via WhatsApp / SMS only, not app login
- (c) Misclick — parents ARE users but the *dedicated portal screens* are deferred

**Recommendation:** Confirm interpretation (a) or (b). If (a), we still need a basic parent-shared-view UI. If (b), we need a WhatsApp/SMS sender integration in P1.

### Q2 — Fee reminders without fee details?
**Issue:** "Fee details" ❌ but "Fee reminders" ✅. A reminder needs *something* to remind about.

**Possible interpretations:**
- (a) Admin enters fee due dates in backend; parents only get reminder push: "Fee due on X" (no amount shown)
- (b) Misclick — fee details should also be ✅
- (c) Reminders go out via WhatsApp (not in-app), admin manages fees offline

**Recommendation:** Most likely (a) — confirm with client. If yes, we still need an admin-side fee entry screen in P1.

### Q3 — Islamic features entirely in P2?
**Issue:** This is an Islamic school, but ALL Islamic features (Quran, Salah, Adhkar, Hadith) are marked ❌ for Phase 1. Only "Islamic study resources" (under Learning Materials) and "Workshop registration" survive.

**Possible interpretations:**
- (a) Intentional — they want core school ops working first, Islamic layer in P2 (sensible MVP)
- (b) Misread — Islamic features are the differentiator and should be P1

**Recommendation:** Confirm — if (a), no objection. But ask: "Are you OK with launching without the Quran/Salah/Adhkar features for the first 3–4 months?"

### Q4 — Unmarked items — include or defer?
The following had no ✅ or ❌ — need explicit decision:

| Feature | Recommend |
|---|---|
| Parent support ticket | P2 (chat covers it later) |
| Parent ↔ Teacher chat | P3 (originally optional) |
| Parent ↔ Admin chat | P3 (originally optional) |
| Dark mode | P1 (trivial — single line of work) |
| Offline PDF viewing | P1 (already needed for Notes/Worksheets) |
| Push notifications | P1 (implied by Notifications module) |

---

## Part 5 — Phase 1 Summary (Pending Clarifications)

| Metric | Count |
|---|---|
| Phase 1 feature groups | 15 of 18 modules (partial or full) |
| Phase 1 individual features | ~52 |
| Deferred to P2 | ~30 (Islamic block + Live class join + Online exam + Online payment + Parent Portal screens) |
| Apps to build in P1 | Mobile (iOS+Android+tablet) + Web (admin/teacher + student) |
| Estimated timeline | **3.5 – 4.5 months** for P1 (subject to Q1 answer) |
| Estimated team | 1 mobile dev + 1 full-stack web dev + 1 designer + PM (Shabeeb) |

---

## Next Step

1. **Send Part 4 (clarifications)** to client — get answers on Q1, Q2, Q3, Q4
2. Lock Phase 1 final feature list
3. Send fixed-price proposal for P1 + indicative pricing for P2
4. Kickoff

---

## Part 6 — Client Update Round 2 (2026-06-28)

Client received the simplified 2-month Phase 1 plan and responded with:

### 6.1 — Confirmed: Mobile AND Desktop access (both)
> *"Mobile and desktop il access option venamtto"*

**Action:** Web Portal — Student is now **definitely in Phase 1** (no longer optional). Same Next.js codebase as the admin/teacher portal, different routes. No change to estimated timeline.

### 6.2 — NEW: Student ↔ Teacher Communication in Phase 1
> *"Students teachers communication option also needed"*

This was previously P3. Client wants it in P1.

**Recommendation — scope it tight to protect the 2-month timeline:**
- ✅ 1:1 chat between student and their teacher (text only)
- ✅ Teacher can reply to multiple students from a single inbox
- ✅ Per-subject / per-class thread
- ❌ No group chats
- ❌ No media (photo/video/voice) in P1 — text only
- ❌ No read receipts, typing indicators (defer)
- ❌ No parent ↔ teacher chat (defer to P2)
- Tech: Supabase Realtime (already in stack — zero extra infra)

**Timeline impact:** +1 week (acceptable within 2-month window if we lock all other scope now)

### 6.3 — Scope Flexibility Caveat
> *"Ath pole cherya enthnklm okke add aakkaan aavashyam undel idayil parayaamallolle"*
> ("Likewise, if there's any small thing that needs to be added in between, we can mention it")

This is friendly but it's a **scope-creep door**. Needs a clear handling rule in the contract / kickoff doc.

**Recommended response to the client:**
> "Sure — small additions during the project are fine. We'll batch them into a fortnightly review. Anything that takes <1 day, we absorb. Anything bigger, we'll quickly estimate and either fit it in (if it doesn't slip the deadline) or queue it into Phase 2. This way we keep the 2-month launch promise."

This gives them goodwill without leaving the door wide open.

### 6.4 — Updated Phase 1 Lock

| Module | Status |
|---|---|
| All previously ✅ items in Part 2 | Confirmed P1 |
| Web Portal — Student (browser) | **Confirmed P1** (was conditional) |
| Student ↔ Teacher 1:1 chat (text only) | **Added to P1** |
| Parent ↔ Teacher chat | Still P2 |
| Group chats / media chat | Still P2 |
| Timeline | 2 months (client's number) — tight but achievable IF scope is now locked |

### 6.5 — What Shabeeb Should Reply Next

1. Confirm desktop access is in Phase 1 ✅
2. Confirm student-teacher chat is in Phase 1 (text only, 1:1) ✅
3. Set the scope-change rule (per 6.3 above) — friendly but explicit
4. Then: send the proposal / contract with the locked Phase 1 list

