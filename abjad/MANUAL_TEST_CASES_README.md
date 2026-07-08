# Abjad — Manual Test Cases: How to Use

Companion to **`docs/MANUAL_TEST_CASES.html`** (the interactive test-case book).

## What this is

A browser-based, offline test-case book for manually testing the entire Abjad platform
(teacher app, school app, admin panel, backend). ~245 test cases across 25 modules.

- **Open** `docs/MANUAL_TEST_CASES.html` in any browser (double-click it — no server needed).
- The index page links to one page per module under `docs/tests/`.
- On every module page: set each case's **Status** (Pass / Fail / Blocked / Not Run) and type in **Notes**.
- Everything **auto-saves to your browser** (localStorage) and is shared across all module pages,
  so your name, date, and every result persist as you move around and reopen the file.
- **Export results (JSON)** and **Reset all** live on the index page. Per-page **Print → Save as PDF**
  gives you a signed section report.

> Because it uses `localStorage`, keep testing in the **same browser + same profile**. Results do not
> sync between machines — use Export JSON to hand off or archive.

## File layout

```
docs/
  MANUAL_TEST_CASES.html        <- open this (index)
  MANUAL_TEST_CASES_README.md   <- this file
  tests/
    tc.css   tc.js              <- shared styles + persistence (do not delete)
    auth.html tprof.html dash.html job.html save.html app.html int.html off.html
    notif.html tick.html sch.html sjob.html cand.html sapp.html soff.html short.html
    team.html sdash.html adm.html abill.html bill.html match.html loc.html sec.html edge.html
```

## Environment / prerequisites

| Component | URL | Start command (from its folder) |
|---|---|---|
| Frontend (teacher + school) | http://localhost:3000 | `pnpm dev` |
| Admin panel | http://localhost:3001 | `pnpm dev -- -p 3001` (dev script has no port set) |
| Backend API | http://localhost:5001 | `pnpm dev` |
| MongoDB / Redis | :27017 / :6379 | must be running for the backend |

- **OTP is emailed, not SMS** (intentional). For `@abjad.test` accounts the code is printed to the
  **backend terminal** (`📧 [DEV] OTP Email … Code: 123456`). Keep that terminal visible.
- **Moyasar runs in test mode.** Sandbox cards are listed on the Billing page (`tests/bill.html`).
  Apple Pay / STC Pay cannot be tested in a desktop browser — mark N/A.
- Some billing states (past-due, expired, legacy) require a **manual DB edit** — noted per case and in
  `docs/billing-test-plan.md`.

## Required test accounts (create before the session)

| # | Role | Purpose |
|---|---|---|
| 1 | **Teacher** (approved) | full teacher flow: profile, search, apply, interviews, offers |
| 1 | **Teacher** (fresh/unverified) | signup, OTP, approval-state, empty-state, paywall cases |
| 1 | **School** (verified) | job posting, candidate search, applications, offers, hiring |
| 3 | **School team members** | one each of Recruiter, Interviewer, Viewer (added to the verified school) — role-permission cases |
| 1 | **Admin** | admin panel: queue, approvals, suspension, tickets, billing, audit |

For end-to-end billing states, also create the `@abjad.test` accounts (U1–U15) described in
`docs/billing-test-plan.md` (teacher/school × free / trial / monthly / annual / cancelled / expired /
legacy / bank-pending / past-due).

## Suggested test order

1. **Smoke pass** — run every **Critical (C)** case first, across all modules. If a Critical fails, the
   build likely isn't ready for a full pass; report immediately.
2. **Module passes** — work module by module in the index order (Teacher → School → Admin). Many cases
   chain (e.g. a school schedules an interview → verify on the teacher side), so run related teacher/school
   modules close together.
3. **Cross-cutting** — finish with **Security & Roles (SEC)**, **Localization (LOC)**, and
   **Edge & Responsive (EDGE)**, which touch behaviour set up in earlier modules.
4. **Billing E2E** — run once the app is otherwise stable; it needs the Moyasar sandbox and specific accounts.

## How to report a bug

For any case you mark **Fail**, file a bug with: the **case ID** (e.g. `SAPP-05`), the role/account used,
exact steps, expected vs actual, screenshot/console error, and severity below. Put a one-line summary +
bug-tracker link in the case's **Notes** cell.

### Severity definitions

| Severity | Definition | Examples |
|---|---|---|
| **Critical** | Blocks a core flow, data loss, security hole, or money handled wrong. No workaround. | Can't log in; payment charged but no subscription; teacher sees another school's data; apply button dead. |
| **Major** | Important feature broken or wrong, but a workaround exists or it's not the primary path. | Reschedule reason not saved; match badge missing; a filter returns wrong results. |
| **Minor** | Limited-impact functional issue. | Wrong empty-state copy; count off by one after refresh; a toggle doesn't persist. |
| **Cosmetic** | Visual/copy only, no functional impact. | Misaligned RTL padding; truncated label; inconsistent spacing. |

Per the team quality pipeline: **Critical or Major** bugs return the task to the owning developer and must
be **re-verified by QA** after the fix. Minor/Cosmetic can be batched.

## Known intentional behaviours (do NOT log as bugs)

- OTP by **email, not SMS**; OTP resend = 60s client cooldown only (no backend throttle).
- "Remember this device": ~30 days when checked; session-cookie + ~1 day when unchecked.
- Job descriptions are **plain textareas** with structured sections (Responsibilities / Requirements /
  School culture / Benefits × Ar/En) + a 2000-word counter — **not** a rich text editor, by design.
- School verification requires **2 documents** (Commercial Registration + License). Tax cert &
  authorization letter are intentionally omitted.
- Job posts intentionally have **no** gender / nationality / age / special-requirements fields
  (pending client legal confirmation).
- Admin pricing: **edit-only** on 6 seeded plans (no create/delete), by decision.
- Refunds are **full-only**, processed Moyasar-first; bank-transfer refunds are handled off-platform.
- Nationality filter on candidate search is intentionally deferred.

## Notes for the tester

- If a case depends on a state you can't reach (e.g. a DB-only billing state, or an admin action you lack
  access to), mark it **Blocked** and note why — don't guess Pass/Fail.
- Test **both** the UI and, for security cases (SEC), the direct URL/API — hiding a button is not the same
  as enforcing a permission.
- When a case says "reflects on the other side," actually switch accounts and confirm — cross-role
  consistency is where real bugs hide.
