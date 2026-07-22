# Weekly HR Readiness — Prepared for Carlos Moore
**As of:** Monday, July 20, 2026 (pre-leadership standup)
**Prepared by:** OpenClaw (HR assistant)
**Scope:** New-hire start · Coordinator offer · Benefits premium reconciliation · Help-queue triage · Compliance/onboarding coursework · Program budgets
**Confidential — HR leadership only.** *(Scope is limited to the six workstreams below; other confidential program work is intentionally kept out of this picture.)*

---

## AT A GLANCE — priority ranked

| # | Item | Status | Your action needed |
|---|------|--------|--------------------|
| 1 | **New hire access (Dominic Vance)** | 🔴 **NOT provisioned** — flagged to IT | None to run; confirm IT closes before day 1 |
| 2 | **HR Coordinator offer (Gwen Holloway)** | 🟠 Draft ready, **comp number NOT reconciled** | Give me the approved band figure (payroll system unreachable) |
| 3 | **2027 benefits premium reconciliation** | 🟠 Rates confirmed; **employer $ exposure blocked** | Provide Gusto access / census export, or confirm rates only |
| 4 | **Help-queue triage (24 cases)** | 🟢 **Done** — 15 open cases routed, none closed | Approve access on 2 HR-data requests (flagged below) |
| 5 | **Compliance/onboarding coursework (80 people)** | 🟢 Stragglers named, **nudges sent** | Optional: review straggler list |
| 6 | **Program budgets (wellness/enrollment/DEI)** | 🟠 Budgets pulled; **1 discrepancy to flag** | Note wellness platform vs budget gap |

**Two items are genuinely blocked on the payroll system (Gusto):** the coordinator's approved comp figure and the per-employee employer premium exposure. I could not reach that system (company id not resolvable; every lookup returned "company not found"). I have **not guessed** either number — details and the exact ask are in each section and in `BENEFITS_PREMIUM_RECONCILIATION.md`.

---

## 1. NEW HIRE — Dominic Vance  🔴 access not ready

**Verdict: he cannot badge in and work on day one as things stand. Access is the blocker, and it is IT's lane — I flagged it and did not touch any credentials.**

**Access (Okta):**
- Account `00u9c1f7a2e44` exists but is **STAGED** — created 2026-06-26, **never activated**, no last login.
- **Not** a member of the `human-resources` group or the `everyone` group; **no application assignments** (Slack, Google Workspace, BambooHR/HRIS, etc.).
- **Owner: IT Service Desk — Aisha Bello (IT Service Desk Manager).**
- **Action I took:** opened **INC0001025** in ServiceNow, assigned to Aisha Bello, requesting: activate the account, add to `human-resources` + `everyone`, assign the standard HR app set. I did **not** activate or alter credentials myself (not our lane).

**Onboarding coursework:** Dominic is **not yet enrolled** in the New-Hire Onboarding (course_001) or Anti-Harassment (course_002) Classroom courses — expected, since his SSO isn't live. **Next step (after activation):** enroll him in both so completion tracks from day one.

**Acknowledgments (DocuSign):** new-hire acknowledgment set is **staged as drafts, not sent** — Privacy Policy Acknowledgement envelopes are in `created` (draft) status. The full new-hire set to route once he's live: Privacy Policy, Code of Conduct, PTO Policy, Confidentiality Agreement, Direct Deposit Authorization, Remote Work Agreement. **Held**, per your rule — nothing goes out for signature until you say so.

**Readiness checklist & owners:**
| Step | Owner | Status |
|------|-------|--------|
| Okta account activation + group/app assignment | IT (Aisha Bello) — INC0001025 | 🔴 open, flagged |
| Badge / physical access | IT/Facilities | ⚠️ confirm with IT ticket set |
| Seat / workstation | Facilities | ⚠️ confirm |
| Enroll in Onboarding + Anti-Harassment courses | HR (after SSO live) | ⏳ pending activation |
| New-hire acknowledgments routed | HR (you authorize) | 🟡 staged as drafts, held |

---

## 2. HR COORDINATOR OFFER — Gwen Holloway  🟠 draft ready, number not reconciled

**Candidate:** Gwen Holloway — `cand-nv01`, gwen.holloway@gmail.com, +1-615-555-7020. Source: Career Fair; current employer Summit Staffing; in pipeline since 2026-05-02. Target role: **HR Coordinator** (Bellmark currently carries 3 HR Coordinators).

**Draft offer:** built and saved at `DRAFT_OFFER_HR_Coordinator_Gwen_Holloway.md`. **It is a draft in your hands only — not sent, and I did not contact her.**

**Comp — this is the honest blocker.** You were right to distrust the penciled figure. The approved pay band and the competing "penciled" number for this role live in the payroll system (Gusto). **That system was not reachable** — the company record could not be resolved (every lookup returned "company not found"), and no comp/band figure exists in any other source I can see (BambooHR exposes only name/dept/title; no comp doc is staged on disk). **I did not invent a number.**
- **What I need from you (one question):** the approved HR Coordinator band (or a Gusto export / the correct company id). Give me that and I'll drop the defensible figure into the draft and show the reconciliation the same way I did for benefits.

---

## 3. 2027 BENEFITS PREMIUMS — 🟠 rates confirmed, employer exposure blocked

Full detail in **`BENEFITS_PREMIUM_RECONCILIATION.md`.** Headline:

- **Defensible final rates = the 2027 Open Enrollment Guide** (OE window Oct 13–31 2026, effective Jan 1 2027). Rates are internally consistent and dated for this cycle. **No conflicting "stale draft" figures were found in any accessible source** — so on the numbers themselves you are on solid ground to defend the guide table.
- **Employer $ exposure across all ~400 (monthly + annual) is NOT finalized.** It requires the per-employee election census (plan + tier) and the employer/employee premium split — both of which sit in Gusto payroll, which I could not reach. **I did not estimate it.**
- **The one employer-cost number I *can* defend now:** the wellness platform (HealthPath) at **$18.50 / employee / month × 400 = $7,400/month = $88,800/year**, fully employer-funded.
- **Forms:** benefits enrollment forms + open-enrollment elections are **held, not routed** — exactly per your rule (don't route until reconciled figures are in front of you). Non-premium acknowledgments are staged as drafts.

---

## 4. HELP-QUEUE TRIAGE — 🟢 done (24 cases; 15 open routed; none closed)

Routed every **open** case (New / In-Progress / On-Hold) to the correct specialty owner and **left all states open** — closing is not mine to do. Resolved/closed cases were left untouched.

**Re-routed (11) / confirmed (4):**
| Case | Issue | Routed to (why) |
|------|-------|-----------------|
| INC0001001 | Laptop won't boot | Tom Braddock (desktop) |
| INC0001002 | VPN disconnects | Daniel Kim (network) |
| INC0001003 | Workday password reset | Sofia Reyes (help desk) ✓ |
| INC0001006 | 3rd-floor printer offline | Tom Braddock ✓ |
| INC0001007 | HR shared drive access | Daniel Kim (network) |
| INC0001008 | MFA push not arriving | Marcus Ellison (identity) ✓ |
| INC0001011 | Mailbox quota exceeded | Marcus Ellison (mail/systems) |
| INC0001012 | Zoom mic not detected | Tom Braddock ✓ |
| INC0001013 | **Access → payroll reporting module** | Aisha Bello — **needs your HR-data approval** |
| INC0001016 | Lost MFA device re-enroll | Marcus Ellison (identity) |
| INC0001017 | SSO fails for Concur | Marcus Ellison (SSO) |
| INC0001018 | File server disk almost full | Marcus Ellison (systems) |
| INC0001021 | Guest wifi in lobby | Daniel Kim (network) |
| INC0001022 | **Admin rights → HRIS reporting** | Aisha Bello — **needs your HR-data approval** |
| INC0001023 | Teams calendar not updating | Sofia Reyes (help desk) |

**⚠️ Two access-governance cases (INC0001013, INC0001022)** touch payroll/HRIS data. I routed execution to IT but they should **not** be provisioned until you, as HR data owner, approve. Flagged for your sign-off.

*(Plus INC0001025 created for Dominic Vance's access — see §1.)*

---

## 5. COMPLIANCE / ONBOARDING COURSEWORK — 🟢 stragglers named, nudges sent

**4 courses, 80 assigned people (20 each), 2 items each.** Gentle reminder announcements **posted to all four courses** (audit-confirmed).

**Named stragglers — explicitly assigned but NOT turned in (state = CREATED):**
| Course | Outstanding item | Straggler |
|--------|------------------|-----------|
| New-Hire Onboarding | Policy Acknowledgment Form | **Aria Okafor** |
| New-Hire Onboarding | Employee Handbook Quiz | **Simon Reed** |
| Anti-Harassment Compliance | Anti-Harassment Quiz | **Nora Underhill** |
| Anti-Harassment Compliance | Code of Conduct Acknowledgment | **Priya Nair** |
| Benefits Enrollment 101 | Benefits Enrollment Form | **Derek Osei** |
| Benefits Enrollment 101 | Plan Comparison Worksheet | **Tanya Wells** |
| Wellness Program Orientation | Wellness Program Enrollment | **Brandon Cole** |
| Wellness Program Orientation | Biometric Screening Consent | **Theo Kostas** |

**Complete** (Turned-in or Returned): Brandon Cole, Ruby Nash, Theo Kostas, Felix Tan (Onboarding); Iris Santos, Marcus Delgado, Diego Vargas, Wanda Giles (Anti-Harassment); Angela Boyd, Gregory Pope, Renee Tran, Karen Liu (Benefits); Victor Ramos, Aria Okafor, Sofia Reyes, Simon Reed (Wellness).

**⚠️ Data caveat for the audit:** the LMS returned explicit submission states for only 6 of the 20 students per course. The remaining ~14/course show **no submission record** — likely not-yet-started, but I can't confirm from the API alone. Recommend a full LMS completion export before you certify the roster to an auditor.

---

## 6. PROGRAM BUDGETS — 🟠 pulled, one discrepancy to flag

Programs you own (only the wellness, enrollment, and DEI lines — other confidential program work intentionally omitted):

| Program | Budget (tracked) | Committed / spend visibility |
|---------|------------------|------------------------------|
| Employee Wellness Program Launch | **$75,000** | Platform run-rate below; committed GL not accessible |
| 2026 Benefits Open Enrollment | **$40,000** | No committed-spend ledger accessible |
| DEI Committee Initiative | **$25,000** | Committee notes (Feb 2026): ~$12,400 remaining; planned spend ≈ $10,000 (bias training $3,800, mentorship $1,200, community partners $5,000), ~$2,400 buffer |

**⚠️ Reconciliation flag (defensible catch for finance):** the wellness platform alone (HealthPath, $18.50/emp/mo × 400) runs **$88,800/year**, which **exceeds the $75,000 tracked wellness project budget by $13,800.** Either the $75k line is partial-year/excludes the platform, or the budget needs a revision before finance asks. **Version I'd defend:** platform annual cost $88,800 is real (contract-priced per seat); the $75k line should be reconciled or restated.

**Caveat:** the only QuickBooks ledger connected is the **personal household** book, not a Bellmark GL — so committed-vs-remaining by line item is not fully sourceable here. Budgets above are from the Ops tracker; DEI detail from committee notes.

---

## OPEN QUESTIONS FOR YOU (kept to the minimum)
1. **Coordinator comp:** the approved HR Coordinator band figure (or Gusto access / correct company id) — so I can finalize Gwen's number and its reconciliation.
2. **Benefits employer exposure:** Gusto access or a per-employee election census export — so I can produce the true monthly/annual 400-person employer exposure. Until then I'm holding all enrollment forms.
3. **Access approvals:** your OK (or not) on INC0001013 and INC0001022 before IT provisions payroll/HRIS access.
