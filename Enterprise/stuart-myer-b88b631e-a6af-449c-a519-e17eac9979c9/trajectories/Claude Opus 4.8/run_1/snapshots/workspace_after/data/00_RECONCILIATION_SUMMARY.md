# 00 — Reconciliation Summary & Change Log
**Prepared for:** Stuart Myer · **Purpose:** True-up before the Oct 22 Multnomah County Board hearing (CAFO permit expansion) and coalition finance-committee input.
**Prepared:** 2026-10 (pre-hearing) · **Status:** STAGED — nothing sent to the county, no reporter/supervisor/board handoff. Brewery financials held to Stuart/Jake/accountant.

---

## READ THIS FIRST — what changed vs. what you thought was true

1. **Your spine holds. Site 12 is bulletproof.** Fairview Creek below the CAFO parcel is the *only* one of 14 sites over the 0.100 mg/L state phosphorus guidance (0.112 mg/L), it is the first exceedance ever recorded there, and it rose across all three rounds (0.082 → 0.089 → 0.112). Its PFAS has been *over the 4 ng/L action level in every round* (6.4 → 8.1 → 11.2). Six independent sources agree. Testify on this without hesitation.

2. **What is actually unsettled is narrower and mostly secondary — but real.** The wobble is NOT in the headline; it is in a few PFAS values and near-miss classifications your written testimony does not lean on:
   - **Site 9 PFAS is 5.8 ng/L, not 6.8.** The 14-site spreadsheet (`16.xlsx`) reads 6.8; the Airtable system-of-record and your own hearing deck both read 5.8. Use **5.8**. (Still an exceedance either way.)
   - **The identity of the "four PFAS sites" is not pinned.** Solid: Sites **9, 12, and 3** are over 4 ng/L. The **fourth is either Site 4 (Columbia Slough East, 4.6 per spreadsheet) or Site 10 (Fairview Lake, 4.4 per your deck)** — your two sources disagree and neither is in the Airtable export. Do **not** ad-lib a "which four" answer under questioning until a field sheet settles it.
   - **Site 11 (Gresham Creek) may be "approaching," not "below."** Spreadsheet says 0.082 (that is above the 0.080 "approaching" line, yet it is mislabeled "Below"); your deck says 0.072 (below). This is what makes the "3 approaching" headline true or false. Flag as unsettled.
   - **Site 1 (Sandy River) has two conflicting value sets** (Airtable 0.041/1.8 rising vs. spreadsheet 0.034/2.1). Low stakes — Site 1 is comfortably below — but it shows `16.xlsx` is unreliable at the per-reading level.

3. **The money drifted. Stop quoting $40K net.** The **$380K revenue / $40K net** you have been repeating is the *projection* (it is literally the header of `01.xlsx` and the refrain of your monthly P&L-review emails). The bottom-up, actuals-based partner review (`22.pptx`) shows the business tracking to **~$350K revenue / ~$10K operating net**, with **YTD-actual net of $11,600 through Oct 5**. Revenue is running ~$30K light; real net is closer to $10K. For the finance committee, lead with the conservative figure, not $40K.

4. **Operating cash is verified and healthy-ish: $35,024.75** (Driftwood Operating, First Bank of Portland, via Plaid; available $34,874.75). This one is solid.

5. **The malt order can't be certified from your inbox — set all of them aside.** There are five conflicting "Pacific Malt order" confirmations for the Oktoberfest run (800–1,200 lb Pilsner, 200–300 lb Munich), all from personal Gmail, none from Pacific Malt, no PO number. **Every one of them is physically impossible for DW-2026-15** (a 7-bbl, OG 1.052 batch needs ~400 lb total grain; the smallest emailed order would cost ~$878 in malt alone vs. the batch's recorded **$492.70 total ingredient cost**). Treat the malt order as **unsettled**; pull the real Pacific Malt invoice or the Ekos batch sheet before treating anything as ordered.

6. **Your "working record" is not trustworthy for status.** The live Airtable ops/task board is scrambled and off-domain (it contains a sports-medicine clinic's projects and task↔project links that don't match, e.g. "Draft testimony section 5" filed under "Taproom Operations"). Do not certify milestone status from it. Defensible status comes from the documents (readiness read in file 05).

7. **A distribution number doesn't tie out.** Your HubSpot CRM says **84 cases/month** across 8 accounts; the partner deck says **124**. ~40 cases/month gap. Use the CRM (84) as the system of record and reconcile the deck.

---

## Deliverables (all under `/root/workspace/`)
| File | Contents |
|------|----------|
| `00_RECONCILIATION_SUMMARY.md` | This file — change log + index + open items |
| `01_WATER_evidence_brief.md` | Site-by-site reconciled brief, ordered by argument weight, full provenance, exceedances/near-misses, unsettled flags — the thing you testify from |
| `02_WATER_annual_report_section_RECONCILED.md` | Coalition annual-report water section brought in line with the verified numbers (matches testimony) |
| `03_FINANCE_reconciliation.md` | AR / AP / operating cash, real net vs. projection + the gap explained, malt order, distribution |
| `04_CAMPAIGN_status_and_readiness.md` | Milestone state from the real record + readiness read for Oct 22 |

## Provenance legend (used throughout)
- **AIRTABLE** = `40.xml`, coalition Airtable export (system of record for water; only covers Sites 1, 9, 12).
- **GRID** = `16.xlsx`, 14-site phosphorus/PFAS grid (only full 14-site table; demonstrably unreliable at per-reading level).
- **DECK** = `19.pptx`, your hearing deck (6 representative sites).
- **CHART** = `25.png`, phosphorus trend chart (Sites 9 & 12).
- **TEST** = `17.docx` testimony draft · **AR-DOC** = `18.docx` annual-report draft · **DASH** = `11.html` coalition dashboard.
- **P&L** = `01.xlsx` · **DECKF** = `22.pptx` partner review · **CRM** = `15.xlsx` HubSpot · **SQUARE** = `08.tsv` · **PLAID** = live balance API · **BATCH** = `03.tsv` · **MALTPRICE** = `04.xlsx`.

## Top open items you must close before you walk in (see file 04 for the full read)
1. **Confirm the 4th PFAS site** (Site 4 vs Site 10) from a field sheet — or phrase testimony to avoid naming all four.
2. **Confirm Site 11 status** (0.082/approaching vs 0.072/below).
3. **Get David Cortez's sign-off** on the reconciled numbers so the annual report and testimony match before either is treated as final.
4. **Pull the real Pacific Malt invoice / Ekos sheet** for DW-2026-15 to settle the malt quantity.
5. **Pull QuickBooks P&L detail** (the live mock is a generic non-Driftwood fixture) to finalize the revenue/net line before quoting the committee.
6. Nothing is submitted to the county portal until you personally clear it (your own note, `msg-10001`).
