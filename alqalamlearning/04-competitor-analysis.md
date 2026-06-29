# Al Qalam — Competitor Analysis

**Date:** 2026-06-28
**Source:** Client shared screenshots from a meeting with another vendor (PDF: "Al_Qalam_Learning_App_Proposal.pdf")
**Competitor presenter:** Muhammed (shown as "presenting" in the Meet screenshot)

---

## 1. Competitor's Technical Stack (from Section 5 of their proposal)

| Layer | Their choice | Our choice | Honest comparison |
|---|---|---|---|
| Mobile | **Flutter** (Dart) | **React Native** (Expo) | Both fine. Flutter has stronger Google backing; RN is faster to iterate. Tie. |
| Backend | **Node.js + Express** (custom REST/microservices) | **Supabase** (auto-generated APIs on Postgres) | Theirs = more code to write & maintain. Ours = less to build, less to break. **We win on speed.** |
| Database | **MongoDB** | **Postgres** (via Supabase) | MongoDB for relational school data (students/classes/marks) = wrong fit. Postgres + relations is correct. **We win on data integrity.** |
| Cloud | **Firebase + AWS + dedicated VPS** (3 separate platforms) | **Vercel + Supabase** (2 platforms, fully managed) | Theirs = 3 bills, 3 dashboards, 3 things to monitor. Ours = serverless, no VPS to patch. **We win on TCO + ops simplicity.** |
| Live media | Google Meet API deep link | Google Meet / Zoom deep link | Same approach. Tie. |
| Production | "Hardened dedicated VPS with HA firewalls" | Vercel + Supabase (managed, auto-scaling, HA built-in) | Theirs = devops overhead. Ours = zero ops. **We win on operational cost.** |

### Tech read
- "Node.js API **Microservices**" for a single-school app is **over-engineering**. Microservices add complexity that pays off at scale (100+ schools). For one school it just adds 6 months of build time. This is a tell.
- "Hardened dedicated VPS" is 2015 architecture. Modern apps don't need a VPS for this scale.
- MongoDB for a relational school management system is a square-peg-round-hole choice.

**Bottom line:** Their stack is heavier, more expensive to run, and slower to build. But it *sounds* impressive to a non-technical buyer. We must out-position, not out-jargon.

---

## 2. Competitor's Timeline

**Theirs:** 6-month strategic plan
**Ours:** 2 months (as currently quoted)

### The honest problem
Our 2-month quote is **aggressive** for the locked Phase 1 scope (~52 features + chat + multi-platform). Realistic delivery for that scope is **3–4 months**. There are 3 ways to handle this:

**Option A — Match their 6 months at lower price**
- Pro: Looks equally thorough, can include more polish
- Con: Removes our speed advantage; client may pick the bigger-name vendor at same timeline

**Option B — Keep 2 months but cut scope further to a true lean MVP**
- Pro: Genuine speed advantage; "we ship in 2 months while they're still in design"
- Con: P1 becomes smaller (~25 features, not 52); need to renegotiate the ✅ list with client
- **Lean MVP would drop:** Admission section, certificates, achievement badges, leave application, Islamic study resources screen, workshop registration, multi-language. Add these in a fast-follow Phase 1.5 (month 3).

**Option C — Quote 3 months (recommended)**
- Pro: Honest, deliverable, still **half the competitor's timeline** → strong story
- Pro: Keeps the full ✅ list intact (no client conversation to reduce scope)
- Pro: "We deliver in 3 months what they deliver in 6, same features, half the hosting cost" = clean pitch
- Con: Slips our verbal "2 months" by a month — needs careful framing

**Recommendation: Option C.** Reframe to client as: *"On closer review of the full ✅ list including the new chat feature, we are committing 3 months for production-ready delivery — still 50% faster than the alternative quote you received."*

---

## 3. Where Competitor Wins (be honest)

- **Buzzword density** — their proposal sounds "enterprise". Some clients buy this.
- **Perceived thoroughness** — 6 months reads as "careful" to non-technical buyers.
- **Flutter brand recognition** — common in MENA/India dev shops; client may have heard of it.
- **Length of proposal** — if their PDF is 6+ pages, ours needs to look equally substantive (not the same words — same weight).

## 4. Where We Win (lean into these)

1. **Speed:** 3 months vs 6. Client gets a working app in half the time. Real ROI.
2. **Cost of ownership:** 1 managed platform vs VPS + Firebase + AWS. Lower monthly bill, no devops hire needed.
3. **Phase-based payments:** They quote a 6-month lump. We can offer 4 milestone payments (auth+core / homework+attendance / chat+materials / launch) — less risk for the client, easier cashflow.
4. **Islamic-school domain understanding:** We already mapped Hifdh, Salah, Adhkar, Musabaqa, EN+ML i18n in our scope doc. Their proposal screenshot doesn't show any of this (visible section was generic infrastructure). Probe this in the next client call.
5. **Future-proof stack:** Supabase + Vercel = the same stack Y Combinator startups ship with. Modern, well-supported, hire-able.
6. **Local + Malayalam communication** — direct, no agency layers.
7. **No vendor lock-in:** All our code is portable. Supabase = standard Postgres they can export. Vercel = standard Next.js. Their VPS + custom microservices = stuck with the vendor that built it.

---

## 5. Recommended Counter-Pitch (1-pager to send/say)

> **Why CodeOx vs. the other proposal**
>
> 1. **3 months vs 6 months** — same Phase 1 features, delivered in half the time. You start seeing value in week 6 (auth + attendance + homework live), not month 6.
> 2. **One hosting bill vs three** — we use Vercel + Supabase. The other proposal needs Firebase + AWS + a dedicated VPS with someone to maintain it. You save on monthly hosting AND on hiring a devops engineer.
> 3. **Right tools for school data** — student records, classes, marks, attendance are *relational* data. We use Postgres (the right fit). MongoDB (their choice) is built for unstructured documents — wrong tool for a school's structured data.
> 4. **Phased payments** — pay across 4 milestones tied to working features, not 1 big upfront commitment.
> 5. **Islamic-domain-ready** — our scope already accounts for Hifdh tracker, Salah tracker, Adhkar/Hadith, Musabaqa, EN+ML (Phase 2). We didn't need to be told.
> 6. **You own the code** — standard stack, portable, hire any Next.js / React Native dev in the future. No lock-in to one vendor's custom microservices.

---

## 6. Actions for Shabeeb

1. **Decide on Option A / B / C** (recommend C — quote 3 months)
2. Tell client the chat addition pushes honest delivery to 3 months, still half the competitor's quote
3. Build the proposal PDF with similar visual weight to theirs — sections, tables, a tech blueprint of our own (not buzzword-stuffed, but professionally formatted)
4. Include the 6-point counter-pitch (Part 5) as a "Why CodeOx" section in the proposal
5. Probe in next call: *"Did the other vendor's proposal cover the Islamic features — Hifdh, Salah, Adhkar — in Phase 1 or Phase 2?"* — if they didn't, we have a strong differentiator
6. Ask price: *"If you're comfortable sharing, what range did the other proposal land in?"* — informs our pricing strategy

---

## 7. Pricing intel needed

The screenshots don't show their price. If we can find out:
- **If they quoted ≥ ₹15L / SAR 25k:** We come in 30–40% under, same features, 50% faster timeline. Easy win.
- **If they quoted < ₹8L / SAR 15k:** They're underpricing too — race to bottom. Compete on quality + delivery speed, not price.
- **If they quoted in between:** Match or undercut by 10–15%, win on speed + ops cost.

Worth asking the client directly in the next exchange.
