# Nabda AI MVP — UX Audit & Claude Code Fix Prompts
Tested live on localhost:3000 (signed-in session), 26 Sep 2026.

## What's actually wrong (confirmed by clicking through, not guessing)

### 🔴 Critical — will look broken on stage
1. **Sidebar items "AI Solutions" and "Consultation" kick the logged-in user out of the app** onto the public marketing site (dark theme, "Sign in" / "Start Free Trial" in the nav, sidebar gone). Very likely "Training", "Integrations", "Billing" do the same — they're marketing routes (`/ai-solutions`, `/consultation`, etc.), not app routes. A judge clicking any of these mid-demo lands on a landing page.
2. **No real "detail page" per upload.** Clicking "View results" on a data source in My Data just re-renders the same generic Dashboard shell. To see insights, recommendations, action plan, and reports for that one upload, you have to jump across 4+ separate sidebar destinations — exactly the complaint: users shouldn't have to move between modules to read one analysis.
3. **The "active data source" is a hidden, inconsistent global pointer.**
   - The top-level **Dashboard** nav item always shows the original demo aggregate (Health 73/100) and never changes.
   - **Insights / Recommendations / Reports / AI Analyst** all silently follow whatever data source you last opened via My Data (e.g. Health 55/100 for `03_sales_spike_and_drop.xlsx`) — with **zero visible indicator anywhere** telling you which dataset you're looking at, and no switcher to change it.
   - Net effect: two different "current" truths on screen depending which nav item you clicked, and no way to tell which one you're in.
4. **Mislabeled attribution.** The AI Analyst answer footer says "Based on: Nabda Retail Demo dataset" and a freshly generated report is titled "Nabda Retail Demo — Business Report" — even when the actual numbers are clearly from `03_sales_spike_and_drop.xlsx`. Generate reports from two different uploads and they're indistinguishable in the Reports list.

### 🟠 High
5. **13 sidebar items** for what is functionally one workflow (upload → analyze → decide). My Data, AI Analyst, Insights, Recommendations, Reports, Presentations are six separate destinations for output that belongs to a single analysis run.
6. **Duplicate, indistinguishable demo entries** in My Data — two cards both named "Nabda Retail Demo", same date, same health score (78) — no way to tell them apart.
7. **"Generate Report" has no progress feedback.** The button shows a bare "Loading…" for 8–10 seconds with no explanation elsewhere on the page (no skeleton, no "Analyzing…" copy). Reads as frozen in a live demo.
8. **Presentation generation exists in two disconnected places** — a "Generate Presentation" button inside a Report, and a separate top-level "Presentations" page — with no link between them.

### 🟡 Polish
9. Credit usage history shows raw code values (`comprehensiveReport`, `standardAnalysis`, `presentationPerSlide`) instead of human labels.
10. No breadcrumb / "back to [dataset]" link from Insights, Recommendations, Reports or AI Analyst back to the source in My Data.

## The fix: make "Data Source" the one object the app orbits around

Right now the sidebar is organized by **output type** (Insights, Recommendations, Reports, Presentations are all top-level). It should be organized by **the thing the user uploaded** — one detail page per data source, everything about that source inside it as tabs.

**New navigation (5 items instead of 13):**
`Dashboard (all sources)` · `Data Sources` · `Ask AI (global)` · `Credits` · `Settings`
— move Consultation / Training / Integrations / Billing / AI Solutions into Settings or a single "Grow" menu, or cut them from the app sidebar entirely for now since they're marketing pages, not product.

**One Data Source Detail page** (`/app/data/[id]`), tabbed, not separate nav items:
`Overview` (health score + KPIs + trend) → `Insights` → `Recommendations` → `Action Plan` → `Reports` → `Presentations` → `Ask AI` (chat pre-scoped to this source)

**Persistent source switcher** in the top bar so the active context is always visible and changeable from anywhere, and the main "Dashboard" becomes an explicit "all sources" rollup — never silently swapped for one source's numbers.

Result: **Upload → land straight on that source's page → everything about it in one place, tabbed.** No hunting through the sidebar.

---

## Ready-to-paste prompts for Claude Code

Paste these one at a time, in order. Each is self-contained — Claude Code should locate the relevant files itself.

### 1. Fix broken navigation (do this first — it's demo-breaking)
```
In our Next.js app, the sidebar items "AI Solutions" and "Consultation" (and check
"Training", "Integrations", "Billing" too) currently link to public marketing routes
(/ai-solutions, /consultation, etc.) that render OUTSIDE the authenticated app shell —
clicking them from inside /app logs the user out of the app UI onto the public landing
page (dark theme, "Sign in"/"Start Free Trial" nav, no sidebar).

Fix: every sidebar link in the authenticated app must stay inside the /app layout.
Either (a) build proper in-app pages for these at /app/consultation, /app/training,
/app/integrations, /app/billing, /app/ai-solutions that reuse the app shell/sidebar,
using the existing marketing page content as a starting point, or (b) if they're not
ready for this build, remove them from the sidebar for now rather than linking to a
broken destination. Do not leave any authenticated sidebar item pointing at a public
marketing route.
```

### 2. Build one Data Source Detail page with tabs
```
Right now, clicking "View results" on a data source in /app/data navigates to
/app/data/[id] but that route just re-renders the same generic "Executive Dashboard"
component. Insights, Recommendations, and Reports for that specific upload only exist
on separate global pages (/app/insights, /app/recommendations, /app/reports) with no
visible connection back to the source you opened.

Redesign /app/data/[id] into a single detail page for that one data source, with an
in-page tab bar (not separate sidebar items):
  Overview | Insights | Recommendations | Action Plan | Reports | Presentations | Ask AI

- Overview: the Business Health Score, KPI tiles, and trend charts, scoped to this
  source only (this is what currently renders as the generic Dashboard).
- Insights: only the risks/opportunities/trends generated from THIS source's analysis.
- Recommendations: only this source's AI Recommendations feed.
- Action Plan: a distinct, ordered/prioritized checklist view built from the
  recommendations (High/Medium/Low), separate from the raw recommendations list.
- Reports: list + "Generate Report" scoped to this source, reusing the existing
  report-generation logic but passing this source's id explicitly.
- Presentations: the existing Presentation Generator form, pre-scoped to this source.
- Ask AI: the existing AI Analyst chat UI, pre-scoped to this source's data (pass its
  id into whatever context the analyst query uses), keep the suggested-question chips.

The header of this page should show the source's filename/name and upload date at
all times so the user always knows what they're looking at. Keep this page reachable
only via /app/data/[id] — do not also keep separate top-level sidebar entries for
Insights/Recommendations/Reports/Presentations once this exists (see next prompt).
```

### 3. Add a persistent data-source context switcher; separate it from the all-sources Dashboard
```
Today there are two different notions of "current data source" that disagree with
each other: the top-level Dashboard nav item always shows the original seeded demo
totals, while Insights/Recommendations/Reports/AI Analyst silently follow whatever
data source was last opened from My Data — with no indicator anywhere showing which
one is active, and no way to switch it except going back to My Data.

Fix:
1. Add a persistent dropdown/switcher in the top bar (next to the logo or credits
   badge) labeled with the currently active data source's name, e.g.
   "Viewing: 03_sales_spike_and_drop.xlsx ▾". Clicking it lists all analyzed data
   sources and switches the active one from anywhere in the app.
2. Make the top-level "Dashboard" sidebar item an explicit "All Sources" / portfolio
   rollup view (aggregate across every uploaded source), clearly labeled as such, so
   it's never confused with — or silently swapped for — a single source's numbers.
3. Remove the top-level "Insights", "Recommendations", "Reports", "Presentations",
   and "AI Analyst" sidebar items (their content now lives inside the per-source
   detail page's tabs from the previous prompt). Keep only: Dashboard (all sources),
   Data Sources, Ask AI (a global/source-picker version), Credits, Settings.
```

### 4. Fix mislabeled report/analysis attribution
```
The AI Analyst's answer footer ("Based on: Nabda Retail Demo dataset") and generated
report titles ("Nabda Retail Demo — Business Report") are hardcoded/stale — they show
this even when the analysis clearly ran against a different uploaded file (verified:
asked "Analyze my sales" while viewing 03_sales_spike_and_drop.xlsx, got that file's
numbers back, but the footer still said "Nabda Retail Demo dataset").

Fix: both the AI Analyst answer footer and the report title/header must read the
actual active data source's real name (filename or user-given label), not a hardcoded
string. Two reports generated from two different uploads must be visibly
distinguishable in the Reports list by source name, not just by generation timestamp.
```

### 5. Remove duplicate/indistinguishable demo entries
```
My Data (/app/data) currently shows two separate cards both labeled "Nabda Retail
Demo", same "Analyzed Sep 26, 2026" date, same Health 78/100 — there's no way to tell
them apart or know why there are two. Find where "Use Demo Data" creates/duplicates
this seed record and either de-duplicate so only one demo entry can exist per
account, or, if duplicates are intentional (e.g. re-runs), give each a distinguishing
label/timestamp so they're distinguishable in the UI.
```

### 6. Add real progress feedback to report generation
```
Clicking "Generate Report" shows only a small "Loading…" state on the button for
8-10 seconds with no other feedback on the page — in a live demo this reads as
frozen. Add a proper in-progress state: a skeleton/progress view on the page itself
(e.g. "Analyzing your data…" → "Drafting executive summary…" → "Finalizing report…"
style staged messaging, even if simulated), so the wait is visibly explained rather
than looking hung.
```

### 7. Merge the two presentation-generation entry points
```
Presentation generation currently exists in two disconnected places: a "Generate
Presentation" button inside an open Report, and a separate top-level "Presentations"
page with its own form (Topic/Slides/Style/Audience). Consolidate so there is one
presentation-generation flow, reachable from the Presentations tab inside a data
source's detail page (see prompt 2), pre-filled with context from the report/source
it was launched from when applicable.
```

### 8. Humanize credit usage history labels
```
On /app/credits, the Usage History table shows raw internal reason codes verbatim:
"comprehensiveReport", "standardAnalysis", "presentationPerSlide". Map these to
human-readable labels ("Comprehensive Report", "Standard Analysis", "Presentation
Slide") before rendering in the UI. Keep the raw enum only in code/logs, never in
user-facing text.
```

### 9. Add breadcrumb navigation back to the source
```
Add a breadcrumb or "back to [source name]" link at the top of any page reached from
inside a data source's detail page (report view, presentation view, AI Analyst
answer), so users can always navigate back to the source they came from instead of
using browser back or hunting through the sidebar.
```
