# Al Qalam Learning — Scope Document
## Apps to be Built & Features Required

**Date:** 2026-06-28
**Prepared by:** Shabeeb K — CodeOx
**Client:** Al Qalam Learning

---

## Part 1 — Apps to be Built

We recommend **3 applications** sharing a single backend. This is the cleanest split — fewer apps means lower cost, simpler updates, and one source of truth for data.

### App 1 — Al Qalam Mobile App (iOS + Android)
**Tech:** React Native (Expo) — one codebase, both platforms
**Users:** Students, Parents, Teachers (role-based login)
**Purpose:** Day-to-day usage — checking homework, attendance, fees, joining live classes, Quran/Salah tracking, notifications.

Why one app for three roles: 90% of mobile users are parents and students. Teachers also need on-the-go access for marking attendance, uploading homework, sending announcements. Splitting into 3 apps triples maintenance with no real benefit — role-based UI handles it inside one app.

### App 2 — Al Qalam Web Portal (Admin + Teacher)
**Tech:** Next.js (App Router) on Vercel
**Users:** School Admin, Principal, Teachers (for heavy data entry)
**Purpose:** School management dashboard — admissions, fee structures, exam setup, report generation, bulk uploads, broadcast announcements, financial reports. Anything that's painful on a phone.

### App 3 — Al Qalam Parent/Student Web (Optional)
**Tech:** Same Next.js codebase as App 2 (different routes)
**Users:** Parents and students who prefer browser over app
**Purpose:** Mirror of the mobile app for desktop/laptop use — fee payment, viewing report cards, downloading certificates, watching recorded classes.

**Recommendation:** Build App 1 + App 2 in Phase 1. Add App 3 in Phase 2 only if client confirms demand.

---

## Part 2 — Backend (Shared by All Apps)

**Tech:** Supabase (Postgres database + Auth + File Storage + Realtime)
**Purpose:** Single source of truth for all user data, content, files, and real-time events. Push notification service layered on top (Expo Notifications).

Not a separate "app" in the client's view, but a real piece of infrastructure that needs to exist and be quoted.

---

## Part 3 — Features Required (Grouped by Module)

Phase tags: **P1** = MVP launch · **P2** = Engagement + Islamic core · **P3** = Nice-to-have · **P4** = Future

### A. Identity & Access
| # | Feature | Phase | Where |
|---|---|---|---|
| A1 | Email / phone login + OTP | P1 | Mobile + Web |
| A2 | Role-based access (Student / Parent / Teacher / Admin) | P1 | All |
| A3 | Multi-child support for parents | P1 | Mobile |
| A4 | Profile management + photo | P1 | Mobile + Web |
| A5 | Password reset, account recovery | P1 | All |

### B. Student Dashboard
| # | Feature | Phase | Where |
|---|---|---|---|
| B1 | Student profile (name, class, section, ID) | P1 | Mobile |
| B2 | Attendance % at a glance | P1 | Mobile |
| B3 | Today's schedule / upcoming classes | P1 | Mobile |
| B4 | Performance summary card | P2 | Mobile |
| B5 | Quick links (homework, fees, notes) | P1 | Mobile |

### C. Attendance
| # | Feature | Phase | Where |
|---|---|---|---|
| C1 | Teacher marks attendance (class-wise, bulk) | P1 | Mobile + Web |
| C2 | Daily attendance view (student/parent) | P1 | Mobile |
| C3 | Monthly attendance report | P1 | Mobile + Web |
| C4 | Leave application + approval flow | P2 | Mobile + Web |
| C5 | Auto-alert to parent on absence | P2 | Mobile |

### D. Homework & Assignments
| # | Feature | Phase | Where |
|---|---|---|---|
| D1 | Teacher creates homework (text + attachments) | P1 | Mobile + Web |
| D2 | Daily homework list (student/parent) | P1 | Mobile |
| D3 | Student submits — photo or PDF upload | P1 | Mobile |
| D4 | Teacher reviews & gives feedback | P1 | Mobile + Web |
| D5 | Due-date reminders (push) | P1 | Mobile |

### E. Learning Materials
| # | Feature | Phase | Where |
|---|---|---|---|
| E1 | Notes upload (PDF, docs) | P1 | Web |
| E2 | Worksheet library | P1 | Mobile + Web |
| E3 | PDF download + offline view | P1 | Mobile |
| E4 | Practice activities / interactive content | P3 | Mobile |
| E5 | Islamic study resources (categorised) | P2 | Mobile + Web |

### F. Live Classes
| # | Feature | Phase | Where |
|---|---|---|---|
| F1 | Weekly timetable view | P1 | Mobile + Web |
| F2 | Join class button (Zoom/Meet deep link) | P2 | Mobile |
| F3 | Class reminders (push 10 min before) | P2 | Mobile |
| F4 | Recorded class library (video links) | P2 | Mobile + Web |

> **Note:** Live video is NOT custom-built. We integrate Zoom or Google Meet via deep link. Client provides their own Zoom/Meet account.

### G. Exams & Assessments
| # | Feature | Phase | Where |
|---|---|---|---|
| G1 | Exam timetable | P1 | Mobile + Web |
| G2 | Online quiz (MCQ, short answer) | P2 | Mobile + Web |
| G3 | Online exam with timer | P2 | Mobile + Web |
| G4 | Marks entry by teacher | P2 | Web |
| G5 | Grade / report card view | P2 | Mobile + Web |
| G6 | Downloadable PDF report card | P2 | Mobile + Web |

### H. Fees Management
| # | Feature | Phase | Where |
|---|---|---|---|
| H1 | Fee structure setup (admin) | P1 | Web |
| H2 | Fee details + due amounts (parent) | P1 | Mobile |
| H3 | Payment history | P1 | Mobile + Web |
| H4 | Online payment (gateway integration) | P2 | Mobile + Web |
| H5 | Fee reminder notifications | P1 | Mobile |
| H6 | Download receipts (PDF) | P2 | Mobile + Web |

### I. Parent Portal
| # | Feature | Phase | Where |
|---|---|---|---|
| I1 | Child's progress overview | P1 | Mobile |
| I2 | Attendance view | P1 | Mobile |
| I3 | Homework status | P1 | Mobile |
| I4 | Teacher remarks | P1 | Mobile |
| I5 | All notifications for the child | P1 | Mobile |
| I6 | Switch between multiple children | P1 | Mobile |

### J. Teacher Portal
| # | Feature | Phase | Where |
|---|---|---|---|
| J1 | Mark attendance | P1 | Mobile + Web |
| J2 | Create + assign homework | P1 | Mobile + Web |
| J3 | Upload study materials | P1 | Mobile + Web |
| J4 | Enter exam marks | P2 | Web |
| J5 | Send class announcements | P1 | Mobile + Web |
| J6 | View class roster | P1 | Mobile + Web |

### K. Notifications
| # | Feature | Phase | Where |
|---|---|---|---|
| K1 | Push notifications (FCM/APNs) | P1 | Mobile |
| K2 | In-app notification centre | P1 | Mobile + Web |
| K3 | School-wide announcements | P1 | Web (admin sends) |
| K4 | Exam alerts | P1 | Mobile |
| K5 | Holiday & event reminders | P1 | Mobile |

### L. Islamic Features — Quran
| # | Feature | Phase | Where |
|---|---|---|---|
| L1 | Hifdh progress tracker (Surah/Juz logged by ustadh) | P2 | Mobile + Web |
| L2 | Surah memorization checklist | P2 | Mobile |
| L3 | Tilawah recording upload (student → ustadh review) | P3 | Mobile |
| L4 | Quran revision schedule | P2 | Mobile |

### M. Islamic Features — Daily Practice
| # | Feature | Phase | Where |
|---|---|---|---|
| M1 | Daily Adhkar (morning / evening) | P2 | Mobile |
| M2 | Hadith of the week | P2 | Mobile |
| M3 | Dua collection (categorised) | P2 | Mobile |
| M4 | Seerah lessons | P2 | Mobile |
| M5 | Islamic quizzes | P2 | Mobile |

### N. Islamic Features — Salah Tracker
| # | Feature | Phase | Where |
|---|---|---|---|
| N1 | Daily 5-prayer log (student self-marks) | P2 | Mobile |
| N2 | Prayer time reminders (location-based) | P2 | Mobile |
| N3 | Weekly / monthly Salah report | P2 | Mobile |
| N4 | Parent view of child's tracker | P2 | Mobile |

### O. Islamic Events & Competitions
| # | Feature | Phase | Where |
|---|---|---|---|
| O1 | Event calendar (Ramadan, Dhul Hijjah, etc.) | P2 | Mobile + Web |
| O2 | Workshop registration | P3 | Mobile + Web |
| O3 | Musabaqa (competition) registration | P3 | Mobile + Web |
| O4 | Competition results display | P3 | Mobile + Web |

### P. Certificates & Achievements
| # | Feature | Phase | Where |
|---|---|---|---|
| P1 | Achievement badges (gamification) | P2 | Mobile |
| P2 | Downloadable certificates (PDF) | P2 | Mobile + Web |
| P3 | Student awards display | P2 | Mobile |
| P4 | Competition results & ranks | P3 | Mobile + Web |

### Q. School Management (Admin)
| # | Feature | Phase | Where |
|---|---|---|---|
| Q1 | Academic calendar (holidays, exams, events) | P1 | Web |
| Q2 | Class & section setup | P1 | Web |
| Q3 | Student / teacher / parent CRUD | P1 | Web |
| Q4 | Bulk import (CSV) | P1 | Web |
| Q5 | Broadcast announcements (all / by class) | P1 | Web |

### R. Admissions
| # | Feature | Phase | Where |
|---|---|---|---|
| R1 | Online admission form (public) | P3 | Web |
| R2 | Document upload (birth cert, photo, etc.) | P3 | Web |
| R3 | Application status tracking | P3 | Web |
| R4 | Admin review + approve / reject | P3 | Web |

### S. Communication
| # | Feature | Phase | Where |
|---|---|---|---|
| S1 | Support ticket (parent → admin) | P3 | Mobile + Web |
| S2 | WhatsApp support button (deep link) | P1 | Mobile |
| S3 | Parent ↔ Teacher chat (1:1) | P3 | Mobile |
| S4 | Parent ↔ Admin chat | P3 | Mobile |

### T. Cross-cutting / Platform
| # | Feature | Phase | Where |
|---|---|---|---|
| T1 | Multi-language: English + Malayalam | P1 | All |
| T2 | Dark mode | P1 | Mobile + Web |
| T3 | Tablet-responsive layouts | P1 | Mobile |
| T4 | Offline PDF viewing | P1 | Mobile |
| T5 | App update force-prompt (security patches) | P1 | Mobile |
| T6 | Analytics + crash reporting (internal) | P1 | All |

### U. Future (Phase 4)
| # | Feature | Phase | Where |
|---|---|---|---|
| U1 | AI homework assistant | P4 | Mobile |
| U2 | AI-powered exam paper generator (teacher) | P4 | Web |
| U3 | Predictive performance analytics | P4 | Web |

---

## Part 4 — Summary

### Apps
1. **Mobile App** (iOS + Android, React Native) — student/parent/teacher
2. **Web Portal** (Next.js) — admin + teacher heavy-lift
3. **Parent/Student Web** (optional, same Next.js codebase) — P2

### Backend
- **Supabase** (Postgres + Auth + Storage + Realtime)
- **Expo Push** for notifications
- **Zoom / Meet** for live classes (integration, not custom)
- **Payment Gateway** — Razorpay / HyperPay / Tap (region-dependent)

### Feature count by phase
| Phase | Feature count | Goal |
|---|---|---|
| **P1 — MVP** | ~50 features | Launch a working school in 3–4 months |
| **P2 — Engagement + Islamic** | ~30 features | Differentiator: Islamic + payments + live classes |
| **P3 — Nice-to-have** | ~15 features | Polish: chat, musabaqa, admissions |
| **P4 — Future** | 3+ features | AI layer, defer until P1–P3 are live |

---

## Part 5 — What Happens Next

1. Client reviews this scope document
2. Client answers the discovery questionnaire (separate file: `03-discovery-questions.md`)
3. CodeOx prepares fixed-price quote for **P1 only** + indicative pricing for P2–P4
4. Sign off → kickoff

> **Important:** We do not recommend a single fixed-price quote for all 18 modules at once. Phase-wise commitment protects both sides — client sees value early, scope changes are isolated to upcoming phases.
