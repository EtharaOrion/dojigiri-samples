# DRAFT 2 — Wholesale Receivables + Cash Reconciliation
**Confidential — Stuart Myer and Jake Callahan only. Working draft, not final.**
Snapshot basis: HubSpot CRM export dated 2026-10-05 and the Q4 partner deck. No invoice-level ledger, payment/deposit record, or brewery bank statement was present in the provided files — see Blockers. Nothing below is invented.

---

## Bottom line up front
- **Best-available outstanding A/R = $1,344**, across **4 of 8** accounts. But this is the *summary* balance you told me not to trust, and I agree it can't be fully trusted — there are **no individual invoices, dates, invoice numbers, or payment records** in the files, so I cannot match invoices to payments, or catch a double-payment / stale / mis-dated invoice. That work is **blocked**, not done.
- **The two readable sources on wholesale volume disagree badly** (84 vs 124 cases/month; 6 of 8 accounts differ). If wholesale is billed per case, that ~40-case/month gap is material and it undermines confidence in any per-account revenue or balance until reconciled.
- **The books don't even agree with your own partner deck**: QuickBooks P&L shows $380K revenue / $40K net; the deck's P&L table shows $350K / $10K. Root cause identified below (a dropped $30K festival line). Worth fixing before anyone quotes a net number.
- **Bank-vs-books on the operating account cannot be done** — no brewery operating-account statement was provided (only your *personal* savings statement, which is a different account).

---

## 1. Outstanding receivables (best available, CRM snapshot 10/05)

| Account | Balance due | Notes / flag |
|---|---|---|
| The Knotty Pine Pub | **$392** | Last order 10/01 |
| Cardinal Bar and Grill | **$364** | Last order 10/04 |
| Sellwood Public House | **$308** | Last order date conflicts across sources (10/02 vs 9/29) |
| Rivergate Bottle Shop | **$280** | Last order 10/03 |
| Greenfield's Deli | $0 | Family account; paid current |
| Eastside Tavern | $0 | Last-order date conflicts (10/01 vs 9/25) |
| Hollow Oak Kitchen | $0 | Paid current |
| Vivian Wine and Beer | $0 | Last-order date conflicts (10/01 vs 9/28) |
| **TOTAL A/R** | **$1,344** | Summary only — not invoice-verified |

**What I cannot certify without the invoice book:** whether any of these four balances is one invoice or several; whether anything is past terms (net-30); whether a payment was applied to the wrong invoice; whether anything was paid twice. The user's own worry — "the summary balance isn't telling the whole truth once you get down into the individual invoices" — stands, and I can't resolve it with what's here.

## 2. Data-quality flag: volume/date mismatch between the two sources
Same 8 accounts, two documents, two different stories:

| Account | CRM cases/mo (15.xlsx) | Deck cases/mo (22.pptx) | Last-order mismatch |
|---|---|---|---|
| Greenfield's Deli | 8 | 24 | — |
| Knotty Pine Pub | 14 | 18 | — |
| Rivergate Bottle Shop | 10 | 22 | — |
| Hollow Oak Kitchen | 9 | 16 | — |
| Sellwood Public House | 11 | 14 | 10/02 vs 9/29 |
| Eastside Tavern | 12 | 12 | 10/01 vs 9/25 |
| Vivian Wine and Beer | 7 | 8 | 10/01 vs 9/28 |
| Cardinal Bar and Grill | 13 | 10 | 10/04 vs 9/27 |
| **TOTAL** | **84** | **124** | — |

A 40-case/month discrepancy (48%) between the CRM and the partner deck is not a rounding issue. One of these is stale/wrong. **Pin down which is current before either of you quotes a distribution number** — it feeds both the receivables and the distribution-revenue line.

## 3. Books vs partner deck (internal P&L inconsistency)

| Line | QuickBooks P&L (01.xlsx) | Partner deck table (22.pptx s5) | Gap |
|---|---|---|---|
| Taproom | 268,000 | 214,000 | 54,000 |
| Distribution | 86,000 | 88,000 | 2,000 |
| Releases/festivals/merch | 26,000 | 48,000 (36k + 12k) | — |
| **Total revenue** | **380,000** | **350,000** | **30,000** |
| Ingredients / COGS | 132,000 | 124,000 | 8,000 |
| Insurance/licenses | 12,400 | 31,400 | 19,000 |
| Marketing/distribution | 6,000 | 13,000 | 7,000 |
| Total expenses | 340,000 | 340,000 | 0 |
| **Net** | **40,000** | **10,000** | **30,000** |

**Root cause of the headline $40K vs $10K:** the deck's own revenue-mix chart (slide 2) lists a **$30K festivals line** that is **missing from the deck's P&L table** (slide 5). Drop $30K of revenue, net falls exactly $30K (40→10). The deck contradicts itself (slide 2 says $380K/$40K; slide 5 table says $350K/$10K). **QuickBooks ($380K/$40K) is the more complete of the two.** The taproom line still needs reconciling (268 vs 214) and the expense composition differs materially even though totals happen to match — recategorization between COGS, insurance/licenses, and marketing. Clean this up before the accountant sees two different P&Ls.

## 4. Operating account: bank vs books — **cannot reconcile (blocked)**
- Books/working figure: ~$35K operating balance (from memory/P&L context), lean in winter.
- **No brewery operating-account bank statement was in the provided files.** The only bank statement present is Stuart's *personal* First Bank savings (ending 4827), which is not the brewery account and is irrelevant here.
- To do the recon you asked for I need the **brewery operating-account statement** (or the Plaid export for that account) for the period. Until then I can't give you a bank-vs-books gap or a "likeliest reason" — and I won't invent one before you poke the accountant.

---

## What it takes to close Draft 2
1. **A/R aging / invoice register** from QuickBooks (invoice #, account, date, amount, terms, paid date/amount) — the single most important missing item; everything about double-pays / stale / mis-dated depends on it.
2. **Deposit / payment-received ledger** to match against invoices.
3. **Decision on which volume source is current** (CRM 84 vs deck 124), then a per-account price/case to value distribution.
4. **Brewery operating-account statement** for the bank-vs-books reconciliation.
