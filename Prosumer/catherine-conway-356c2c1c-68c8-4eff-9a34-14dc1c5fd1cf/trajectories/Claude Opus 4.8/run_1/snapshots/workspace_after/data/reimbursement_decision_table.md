# Winter Staff-Expense Reimbursement Audit — Decision Table

Source: QuickBooks staff expense ledger (13 winter lines, categorized by Diane Kowalski), cross-checked against the Plaid bank feed. Realm 4620816365272861350.
Sorted: lines **needing a human** first, then rejections, then clean approvals.

| QB ID | Date | Person / Owner | Meal / Item | Amount | Verdict | Account | Reason |
|---|---|---|---|---|---|---|---|
| 10165 | 2026-01-06 | Diane Kowalski (categorized) | Athenahealth EHR & practice-mgmt subscription | $549.00 | HOLD (needs human) | Software & Subscriptions (#20) | Legitimate clinic software but at/above the $250 sign-off threshold; needs Catherine's approval. Confirm no overlap with the $1,200/mo Athenahealth AP bills. |
| 15555 | 2026-02-03 | Diane Kowalski (categorized) | Adobe Creative Cloud — design software | $89.99 | HOLD (needs human) | Software & Subscriptions (#20) | Ambiguous clinic-marketing vs studio/portfolio use; cannot confirm business purpose from the ledger. |
| 11320 | 2026-03-04 | Diane Kowalski (categorized) | CME registration — Pacific NW Dermatology Update | $425.00 | HOLD (needs human) | Continuing Medical Education (#19) | Legitimate continuing education but at/above the $250 threshold; needs sign-off before committing. |
| 14898 | 2026-03-25 | Diane Kowalski (categorized) | Beaverton Chamber of Commerce — membership & listing | $450.00 | HOLD (needs human) | Marketing & Advertising (#16) | Legitimate business membership but at/above the $250 threshold; needs sign-off. |
| 9668 | 2026-01-08 | Studio / Catherine (personal) | Cedarbrook Artisan — watercolor pans & sable brushes | $236.48 | REJECT | — (not clinic) | Botanical-illustration supplies, not clinic business; identical $236.48 charge on personal Plaid 01-07. Studio spend miscategorized. |
| 19260 | 2026-01-13 | Studio / Catherine (personal) | Ridgemont Fine Papers — cotton-rag sheets (commission) | $142.00 | REJECT | — (not clinic) | Commission paper; personal studio spend; matches personal Plaid 01-09 ($142.00). |
| 18438 | 2026-01-24 | Studio / Catherine (personal) | Northwest Framing — exhibition frames (Wild Botanica) | $312.00 | REJECT | — (not clinic) | Exhibition framing, not clinic; at/above $250. DOUBLE-REPRESENTED: identical $312 charge also on personal Plaid 03-14 (the 'entered more than once' line). |
| 12630 | 2026-02-09 | Studio / Catherine (personal) | Cedarbrook Artisan — gouache set & archival ink | $198.75 | REJECT | — (not clinic) | Studio supplies, not clinic; matches personal Plaid 02-11 ($198.75). |
| 17492 | 2026-03-18 | Studio / Catherine (personal) | Northwest Framing — custom frames (commissioned panels) | $340.00 | REJECT | — (not clinic) | Framing for commissioned art panels, not clinic; at/above $250. |
| 17205 | 2026-01-19 | Diane Kowalski (categorized) | Cascade Medical Waste — sharps/biohazard pickup | $165.00 | APPROVE | Medical Supplies (#14) | Monthly clinical waste pickup; clearly clinic; foots to receipt; under $250. Booked QB Purchase 19262. |
| 10601 | 2026-02-14 | Diane Kowalski (categorized) | Columbia Uniform & Linen — scrubs & exam gowns | $128.40 | APPROVE | Medical Supplies (#14) | Clinical scrubs/gowns; clearly clinic; under $250. Booked QB Purchase 19263. |
| 16687 | 2026-02-20 | Clinic staff (Diane categorized) | Staff meeting lunch — Jamison Kitchen, Beaverton | $74.60 | APPROVE | Meals & Entertainment (#22) | Staff-meeting meal; reimbursable under meals policy; under $250. Booked QB Purchase 19261. (Personal Jamison dinner $68.45 on 01-24 is a separate visit.) |
| 16935 | 2026-03-11 | Diane Kowalski (categorized) | Evergreen Office — front-desk paper & printer supplies | $210.00 | APPROVE | Medical Supplies (#14) | Front-desk office supplies; clinic ops; under $250. Booked QB Purchase 19264 (nearest supplies account). |

## Reimbursable total — working

- Ledger grand total (all 13 lines): **$3,321.22**
- Less REJECT (personal studio/art spend, not clinic): **-$1,229.23**
- Less HOLD (legit clinic but >= $250 threshold or ambiguous — pending your sign-off): **-$1,513.99**
- **Clean reimbursable now (clinic is on the hook for): $578.00**

Approved lines booked: Cascade $165.00 + Columbia $128.40 + Staff lunch $74.60 + Evergreen $210.00 = **$578.00** (each under $250; booked to correct accounts as QB Purchases 19261-19264).
If all four HOLD lines clear your review, up to **+$1,513.99** more (max $2,091.99).

## Your three worries — what I'm standing behind
- **A meal entered more than once:** No — the only meal (staff lunch $74.60) appears once. What *is* double-represented is the **Northwest Framing exhibition-frames $312**, which sits in the clinic books (QB 18438) AND on your personal Plaid feed (03-14) at the identical amount. That is the line that reads as duplicated; it's already rejected as personal.
- **A total you can't rely on:** Within this ledger, every total foots exactly to its receipt line — none is unreliable. Separately, the one genuinely shaky total in the QB books this period is the **Henry Schein AP bill INV-HS-8821, $1,298.50** ("invoice says 55 boxes, Sofia counted 50, multiple discrepancies," still open) — flagged for you/Diane, though it's a vendor bill, not a staff meal.
- **Lines not matching the bank feed:** Confirmed — **five lines ($1,229.23)** are personal botanical-art/exhibition spend that appears on your personal checking in Plaid, miscategorized as clinic expenses. Those are the lines that don't hold together.

## Verdict on the batch
**Not clean enough to hand to the accountant as-is.** You and Diane have a short conversation coming: art/studio spend run through the clinic books (5 lines), four legitimate items over the $250 threshold awaiting your sign-off, and the Henry Schein delivery discrepancy to reconcile.