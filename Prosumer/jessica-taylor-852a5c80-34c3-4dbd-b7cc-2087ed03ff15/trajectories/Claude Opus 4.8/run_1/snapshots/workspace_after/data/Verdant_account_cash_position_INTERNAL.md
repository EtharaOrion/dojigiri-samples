# Verdant Provisions — Account cash position (INTERNAL — not for client)

Prepared for Jessica. This is the honest, books-vs-reality reconciliation for the Verdant
account only. Keep it off anything client-facing.

## Headline

**Nothing on the Verdant account is actually outstanding. Do not chase Aria.**

The one you were worried about — the final deliverables invoice, **INV-2026101, $6,500** —
shows in QuickBooks as **Status: Open, balance $6,500**, and it sits on the AR aging report
as "Current / outstanding." But QuickBooks *also* holds a matching **payment of $6,500
(pmt-200, dated 2027-01-07) applied to that exact invoice**, and Aria sent a thank-you note
after handoff. The money landed. The "Open" status and the AR line are a stale bookkeeping
artifact.

**Which reading I trusted:** the payment ledger (money received). **Which I set aside:** the
invoice `Status` field and the AR aging report — both show a false balance.

**Action:** mark INV-2026101 paid in QuickBooks so it clears off AR. Do not send a collection
note.

## The pattern (why the books can't be trusted here)

Across the whole Verdant ledger in QuickBooks, the invoice `Status` flags alternate
Open/Paid almost at random — but **every single Verdant invoice has a matching full payment
in the payments ledger.** Examples: inv-201, inv-203, inv-205, inv-207, inv-209, inv-211,
inv-213, inv-215 all read "Open," yet each has a payment for its full amount. So the status
flags are noise; the payments are the truth, and the payments say **fully collected.**

The AR aging report is therefore wrong (it shows Verdant ~$6,500 open, inside a ~$156k
company-wide "Current" total that is itself inflated by the same stale statuses).

## In-scope brand-refresh billing (the coherent account)

The signed SOW was a **fixed $6,500 brand refresh** (logo, color system, packaging for 3
SKUs, brand sheet; two revision rounds; extra hours at $75/hr). Against that:

| Invoice | Desc | Amount | Books status | Payment on record | True status |
|---|---|---|---|---|---|
| INV-2026101 | Brand refresh — final deliverables | $6,500 | Open | $6,500 (pmt-200, 2027-01-07) | **PAID** |
| INV-2026106 | Discovery sprint retainer | $2,200 | Paid | $2,200 (2026-04-09) | PAID |

**Defensible bottom line for the refresh: billed and collected in full. $0 truly outstanding.**

## Flags / genuine ambiguities (do not paper over)

1. **Deposit vs. single final invoice.** The early working records (disk file `TVS-2026-014`,
   Feb 2026) describe the $6,500 project billed **50/50 with a $3,250 deposit paid Feb 3**.
   QuickBooks instead shows a **single $6,500 "final deliverables" invoice** (INV-2026101)
   plus a separate **$2,200 "discovery sprint."** These are two different ledger stories
   that don't cleanly add up. I did **not** invent a reconciled total. Confirm which ledger
   is canonical before you state a lifetime-collected figure for the account.
2. **Out-of-scope / decoy staged invoices.** QuickBooks carries ~16 additional Verdant line
   items (inv-200…inv-215: web landing page, Shopify/DTC theme, signage, trade-show booth,
   icon set, quarterly retainer, etc., totaling ~$51k). These (a) fall **outside** the
   brand-refresh SOW, (b) are **duplicated 2–3×**, and (c) are the **identical templated
   block that also appears cloned across other clients** (Pinnacle, Bloom, and names not in
   your book — Aurora, Kiln + Loom, Coastwise). I treated them as noise, **not** Verdant
   brand-refresh billing. If any of that web/retainer work is real, it's a separate
   engagement to track on its own — but it should never go in the refresh recap.
3. **Two micro-payments** ($95 and $60) are cross-wired to invoice ids that aren't in the
   Verdant set — ledger noise; ignore.

## Bottom line for you

- Final deliverables invoice: **paid.** Don't chase it.
- Refresh account: **settled in full.**
- Cleanup to do in QuickBooks: mark INV-2026101 paid; the AR aging is stale.
- Before quoting any total-collected number for Verdant's full history, resolve the
  deposit-vs-single-invoice discrepancy (flag #1).
