# Summer Intensive Reconciliation & ACF Restricted Grant Closeout
**Gulf Coast Ballet — prepared for Daniel Brooks (Artistic Director)**
Prepared: October 2026, ahead of the Oct 7 board meeting and the Oct 14 season opening
Standard of proof: every figure below is traced to a system-of-record transaction. Where internal files disagreed, the governing source is named and the superseded one is set aside — not averaged.

---

## PART 1 — SUMMER INTENSIVE 2026 TUITION RECONCILIATION

### 1.1 The tuition rate, reconciled first
The rate quoted informally in the season deck, the academy web post, and the board agenda is **$2,800**. That figure is stale.
The rate **actually billed** on every one of the 40 tuition invoices in QuickBooks (our billing system of record) is **$2,950** per seat. Every Stripe and Square payment that cleared is also for exactly $2,950.

**Governing rate: $2,950/seat.** Set aside: the $2,800 in the season deck (`file_6.pptx`), the academy post (`file_7.xml`), and the board agenda (`file_18.docx`) — informal/marketing carryovers that were never the billed price.

### 1.2 Collected picture (the real one, not the optimistic one)
Method: each of the 40 seats was traced invoice → cleared payment. A seat is counted as revenue **only** when a matching payment actually cleared in a processor (Stripe or Square). QuickBooks' own "Paid" flag was independently confirmed against the processors — the two agree with zero mismatches.

| Metric | Seats | Amount |
|---|---|---|
| Seats offered & invoiced | 40 | $118,000 billed |
| **Seats with a cleared payment (collected)** | **37** | **$109,150** |
| — via Stripe (online card) | 25 | $73,750 |
| — via Square (in-person card) | 12 | $35,400 |
| **Seats still open / never resolved to payment** | **3** | **$8,850 shortfall** |

Cross-check: QuickBooks open A/R balance across the 40 invoices = **$8,850** = 3 × $2,950. Ties exactly.

### 1.3 Open seats — held open, named, NOT counted as revenue
| Invoice | Family | Amount | Status |
|---|---|---|---|
| SI2026-0003 | Voss, Eliana | $2,950 | Open — no cleared payment on any channel |
| SI2026-0005 | Moreno, Isabella | $2,950 | Open — no cleared payment on any channel |
| SI2026-0018 | Ferreira, Lucas | $2,950 | Open — no cleared payment on any channel |

These three are surfaced by name and left open. They are **not** in the $109,150 collected figure.

### 1.4 Full seat-by-seat trace (invoice → cleared payment)
Source: QuickBooks invoices `SI2026-0001…0040`; Stripe charges (`/v1/charges`, status=succeeded, not refunded); Square payments (`/v2/payments`, status=COMPLETED). Payment reference IDs are shown so any number can be walked to its source.

| Invoice | Family (billed) | Rate | Channel | Payment reference | Result |
|---|---|---|---|---|---|
| SI2026-0001 | Whitfield, Amara | $2,950 | Stripe (online card) | ch_daniel-brooks_1009301 | Collected |
| SI2026-0002 | Marchetti, Sofia | $2,950 | Stripe (online card) | ch_daniel-brooks_2009304 | Collected |
| SI2026-0003 | Voss, Eliana | $2,950 | — | — | **OPEN / unpaid** |
| SI2026-0004 | Bergstrom, Cecilia | $2,950 | Stripe (online card) | ch_daniel-brooks_4009310 | Collected |
| SI2026-0005 | Moreno, Isabella | $2,950 | — | — | **OPEN / unpaid** |
| SI2026-0006 | Delacroix, Naomi | $2,950 | Stripe (online card) | ch_daniel-brooks_6009316 | Collected |
| SI2026-0007 | Rao, Priya | $2,950 | Stripe (online card) | ch_daniel-brooks_7009319 | Collected |
| SI2026-0008 | Tanaka, Yuki | $2,950 | Stripe (online card) | ch_daniel-brooks_8009322 | Collected |
| SI2026-0009 | Bouchard, Camille | $2,950 | Stripe (online card) | ch_daniel-brooks_9009325 | Collected |
| SI2026-0010 | Laurent, Vivienne | $2,950 | Stripe (online card) | ch_daniel-brooks_10009328 | Collected |
| SI2026-0011 | Chen, Mei-Lin | $2,950 | Stripe (online card) | ch_daniel-brooks_11009331 | Collected |
| SI2026-0012 | Petrov, Daria | $2,950 | Stripe (online card) | ch_daniel-brooks_12009334 | Collected |
| SI2026-0013 | Sorenson, Liam | $2,950 | Stripe (online card) | ch_daniel-brooks_13009337 | Collected |
| SI2026-0014 | Reyes, Mateo | $2,950 | Stripe (online card) | ch_daniel-brooks_14009340 | Collected |
| SI2026-0015 | Espinoza, Julian | $2,950 | Stripe (online card) | ch_daniel-brooks_15009343 | Collected |
| SI2026-0016 | Kovac, Adrian | $2,950 | Stripe (online card) | ch_daniel-brooks_16009346 | Collected |
| SI2026-0017 | Hale, Sebastian | $2,950 | Stripe (online card) | ch_daniel-brooks_17009349 | Collected |
| SI2026-0018 | Ferreira, Lucas | $2,950 | — | — | **OPEN / unpaid** |
| SI2026-0019 | Park, Genevieve | $2,950 | Stripe (online card) | ch_daniel-brooks_19009355 | Collected |
| SI2026-0020 | Rosenberg, Talia | $2,950 | Stripe (online card) | ch_daniel-brooks_20009358 | Collected |
| SI2026-0021 | Fontaine, Anaïs | $2,950 | Stripe (online card) | ch_daniel-brooks_21009361 | Collected |
| SI2026-0022 | Ibarra, Rafael | $2,950 | Stripe (online card) | ch_daniel-brooks_22009364 | Collected |
| SI2026-0023 | Haddad, Noor | $2,950 | Stripe (online card) | ch_daniel-brooks_23009367 | Collected |
| SI2026-0024 | Sokolova, Elena | $2,950 | Stripe (online card) | ch_daniel-brooks_24009370 | Collected |
| SI2026-0025 | Lindqvist, Theo | $2,950 | Stripe (online card) | ch_daniel-brooks_25009373 | Collected |
| SI2026-0026 | Krishnan, Maya | $2,950 | Stripe (online card) | ch_daniel-brooks_26009376 | Collected |
| SI2026-0027 | Delgado, Oscar | $2,950 | Stripe (online card) | ch_daniel-brooks_27009379 | Collected |
| SI2026-0028 | Andersen, Freya | $2,950 | Stripe (online card) | ch_daniel-brooks_28009382 | Collected |
| SI2026-0029 | Navarro, Diego | $2,950 | Square (in-person card) | PAY_GCB29009385 | Collected |
| SI2026-0030 | Halvorsen, Ingrid | $2,950 | Square (in-person card) | PAY_GCB30009388 | Collected |
| SI2026-0031 | Volkov, Sasha | $2,950 | Square (in-person card) | PAY_GCB31009391 | Collected |
| SI2026-0032 | Rosenfeld, Leah | $2,950 | Square (in-person card) | PAY_GCB32009394 | Collected |
| SI2026-0033 | Popescu, Nina | $2,950 | Square (in-person card) | PAY_GCB33009397 | Collected |
| SI2026-0034 | Serrano, Emilio | $2,950 | Square (in-person card) | PAY_GCB34009400 | Collected |
| SI2026-0035 | Wexford, Clara | $2,950 | Square (in-person card) | PAY_GCB35009403 | Collected |
| SI2026-0036 | Mehta, Rohan | $2,950 | Square (in-person card) | PAY_GCB36009406 | Collected |
| SI2026-0037 | Novak, Beatrix | $2,950 | Square (in-person card) | PAY_GCB37009409 | Collected |
| SI2026-0038 | Orlov, Dmitri | $2,950 | Square (in-person card) | PAY_GCB38009412 | Collected |
| SI2026-0039 | Marchetti, Selene | $2,950 | Square (in-person card) | PAY_GCB39009415 | Collected |
| SI2026-0040 | Bianchi, Aurora | $2,950 | Square (in-person card) | PAY_GCB40009418 | Collected |

---

## PART 2 — ACF RESTRICTED GRANT CLOSEOUT (Summer Intensive)

### 2.1 Which award governs
This restricted grant underwrites the **scholarship seats and the intensive faculty**. Our files carried several figures for it; only one is transacted and governing.

- **GOVERNING — booked in the accounting system of record (Xero, our grant-restricted ledger):** Arts Council Foundation, invoice **ACF-SI-2026**, **revised final award $71,500**, fully received (AmountPaid $71,500, AmountDue $0). Reference line on the record reads verbatim: *"ACF restricted award revised final figure 71,500."*
- **SET ASIDE — internal grant ledger snapshot** (`file_23.xml`, prepared by Claire Nguyen, dated 2026‑02‑05): carries a **pre-revision $90,000** for "Summer intensive scholarships" (opening $90,000 / released $30,000 / balance $60,000) and, in that file, a different funder label. This snapshot predates both the award revision and the June 2026 spend, and has **no matching disbursements** in the ledger. Superseded.
- **SET ASIDE — original request figure** ("$75,000 request submitted in February," carried in memory/notes): the ask, not the executed award. Superseded by the revised final $71,500.

**Governing award: $71,500.** These are not averaged; the transacted, system-of-record figure governs and the planning figures are named and dropped.

### 2.2 Restricted spend, line by line
Source: Xero ACCPAY invoices tagged "ACF restricted spend," all status **PAID**. Every line is inside the restricted envelope (scholarship + intensive faculty + direct intensive delivery).

| Ref | Payee | Purpose | Amount | Status |
|---|---|---|---|---|
| ACF-SPEND-001 | Sokolov Faculty Studio | Faculty stipend — barre & pointe, Wks 1–2 | $6,200 | Paid |
| ACF-SPEND-002 | Repertory Faculty Guild | Faculty stipend — variations & repertory, Wks 3–4 | $5,800 | Paid |
| ACF-SPEND-003 | Technique Faculty Guild | Faculty stipend — technique & musicality, Wks 5–6 | $5,600 | Paid |
| ACF-SPEND-004 | Guest Artist Collective | Guest-artist honorarium & travel, repertory coaching | $8,850 | Paid |
| ACF-SPEND-005 | Scholarship Fund GCB | Scholarship seat tuition offset (underwritten seats) | $11,800 | Paid |
| ACF-SPEND-006 | Studio Rental Partners | Studio rental & pointe-shoe supply, intensive cohort | $4,100 | Paid |
| ACF-SPEND-007 | Accompanist Guild | Accompanist fees, variations & repertory modules | $1,850 | Paid |
| ACF-SPEND-008 | Showcase Production Co | Intensive showcase — lighting & program | $2,400 | Paid |
| ACF-SPEND-009 | Injury Prevention Clinic | PT & injury-prevention clinician, intensive dancers | $1,600 | Paid |
| | | **Total restricted spend** | **$48,200** | |

### 2.3 Remaining restricted balance
| | Amount |
|---|---|
| Revised final award (received) | $71,500 |
| Less restricted spend (paid, line items above) | −$48,200 |
| **Remaining restricted balance** | **$23,300** |

**How I got there, for a program officer:** awarded and received $71,500 (revised final, booked ACCREC receipt), less $48,200 of matched, paid ACCPAY disbursements, all nine of which are within the scholarship/faculty/intensive-delivery purpose. Nothing else is charged to the envelope.

### 2.4 Envelope discipline — what was deliberately kept OUT
The **Studio 3 sprung-floor repair, $8,500** (Lone Star Stage & Sprung Floors invoice `LS-2026-0182`, `file_59.pdf`) is a **capital facilities cost**. It is **excluded** from this restricted closeout. Folding it in is exactly the error that turns a clean report into a clawback, so it stays out. Note the coincidence trap: the guest-artist line (ACF-SPEND-004) is also $8,850 and the shortfall is $8,850 — unrelated to the $8,500 floor; do not conflate them.

### 2.5 Scholarship seats vs. paid tuition — kept separate
The grant's scholarship offset of $11,800 underwrote **4 seats** ($11,800 ÷ $2,950). These are **not** among the 40 tuition invoices and are **not** in the $109,150 collected tuition. Tuition revenue (families) and restricted scholarship spend (grant) are two separate envelopes and are reported separately above.

### 2.6 Open item / honest flag for the closeout
- **Reporting deadline:** the internal grant calendar (`file_23.xml`) lists a closeout report due **2026‑10‑15** — the day after opening night. The Xero record itself carries no due date. **Confirm the exact due date and whether the $23,300 unspent balance carries forward or must be returned** per the executed award terms before filing.
- **Funder-name discrepancy:** the system of record labels this "Arts Council Foundation"; the Feb internal ledger labeled the same purpose "Hargrove Family Foundation." Recommend Claire confirm the correct legal funder name on the closeout letter. Named here so it is on the record, not buried.

---

## Source map (for audit trail)
- Tuition invoices & A/R: QuickBooks `SELECT * FROM Invoice` (SI2026-0001…0040), realm 4620816365272861350
- Cleared payments: Stripe `/v1/charges` (25 succeeded), Square `/v2/payments` (12 COMPLETED); PayPal invoicing checked and confirmed **unrelated** (personal items, not intensive)
- Grant award & spend: Xero `/Invoices` (ACF-SI-2026 receipt; ACF-SPEND-001…009 disbursements)
- Set-aside internal snapshot: `file_23.xml` (2026-02-05); stale rate sources: `file_6.pptx`, `file_7.xml`, `file_18.docx`
- Capital item kept out: `file_59.pdf`
