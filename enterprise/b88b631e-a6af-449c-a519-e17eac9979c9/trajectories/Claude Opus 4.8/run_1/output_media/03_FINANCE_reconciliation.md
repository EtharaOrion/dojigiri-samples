# 03 — Brewery Finance Reconciliation
**For:** Stuart Myer (share only with Jake Callahan and the accountant — per data-sharing policy this stays inside that circle).
**As of:** 2026-10 (source snapshots dated Oct 5–8, 2026). **Status:** reconciled from the records available; three lines flagged as not fully verifiable and how to close them.

> Bottom line up front: **Operating cash is real and fine ($35,024.75). The $380K/$40K you quote is the projection, not reality — the books point to ~$350K revenue and ~$10K operating net. Distribution owes you $1,344. No open supplier bills are on record. The Oktoberfest malt order cannot be certified from your inbox — do not treat any of those confirmations as the order.**

---

## 1. Operating cash — where it truly sits  ✅ VERIFIED
- **Driftwood Brewing Operating (First Bank of Portland, …2374): current $35,024.75, available $34,874.75.** Source: PLAID live balance.
- Cross-check of confidence: the same Plaid pull returns your **personal savings at exactly $8,500.00**, which matches your records to the dollar — so this feed is trustworthy.
- This is in line with the "~$35K operating, seasonal" baseline. **Confidence: HIGH.**

## 2. Accounts receivable — what you're actually owed  ✅ (distribution)
From the HubSpot CRM distribution ledger (`15.xlsx`, snapshot 2026-10-05), balances due:
| Account | Balance due |
|---|---:|
| The Knotty Pine Pub | $392 |
| Rivergate Bottle Shop | $280 |
| Sellwood Public House | $308 |
| Cardinal Bar & Grill | $364 |
| Greenfield's, Eastside, Hollow Oak, Vivian | $0 |
| **Total distribution AR** | **$1,344** |
- **Confidence: HIGH** (itemized, account-level, current). None is aged/alarming.
- ⚠ The live QuickBooks mock returns a **generic, non-Driftwood fixture** (revenue booked as "Landscaping Services Revenue," AR $19,780 with generic customer IDs). **It does not reconcile to the distribution ledger and should not be quoted** — treat the CRM's $1,344 as the real distribution AR and pull a proper QuickBooks A/R aging to confirm nothing outside distribution is outstanding.

## 3. Accounts payable — what you actually owe  ⚠ THIN
- **No open supplier bills are documented** in the records provided. Pacific Malt's `04.xlsx` is a Q4 price list (net-30 terms), not an invoice; QuickBooks AP aging returns $0 (but from the generic fixture, so low weight).
- **The one real payable exposure is the unresolved Oktoberfest malt order (see §5).** Until that is pinned, AP is effectively **$0 documented, with one unquantified item outstanding.**
- **Confidence: LOW.** Close by pulling supplier statements / QuickBooks AP aging.

## 4. Revenue & net — projection vs. reality (THE DRIFT)  ⚠ UNSETTLED
Two internal views disagree, and the gap is the whole point of your question:

| Line | `01.xlsx` "P&L 2026" (projection) | `22.pptx` partner review (actuals + Q4) |
|---|---:|---:|
| Taproom | 268,000 | 214,000 |
| Distribution | 86,000 | 88,000 |
| Merch / releases / festivals | 26,000 | 48,000 |
| **Total revenue** | **380,000** | **350,000** |
| Total expenses | 340,000 | 340,000 |
| **Net operating income** | **40,000** | **10,000** |
| *of which YTD actual through Oct 5* | *(projection only)* | *rev 271,800 · exp 260,200 · **net 11,600*** |

- **The $380K / $40K is the projection you've been quoting** (it is the literal header of `01.xlsx` and the refrain of your monthly P&L-review emails, "revenue tracking to the ~$380K projection"). The partner review is built **bottom-up from YTD actuals** and lands at **~$350K revenue / ~$10K operating net**.
- **The drift is real and concentrated in the taproom line** (−$54K: $268K projected vs $214K) partially offset by higher merch/releases. **Net effect: revenue ~$30K light (−7.9%), operating net ~$10K not $40K.**
- **What to tell the finance committee:** lead with **~$350K revenue and ~$10K operating net, YTD-actual net $11,600 through Oct 5, operating cash $35,025.** Do **not** quote $40K net.
- ⚠ Caveats: (a) the partner deck is not internally clean — its cover slides still headline "$40K net" while its detail slide shows $10K, and its distribution case volume (§6) contradicts the CRM; (b) the live QuickBooks feed is the generic fixture and cannot arbitrate. **Confidence: MEDIUM.** Close by exporting the real QuickBooks P&L detail (YTD actual) before the committee meeting and reconciling the taproom line to Square.

## 5. The Oktoberfest malt order — which one stands?  ⛔ NONE OF THEM (as-is)
You have **five conflicting "Pacific Malt order" confirmations** in the inbox for the Oktoberfest run:
| Date | Quantity (Pilsner / Munich) |
|---|---|
| 2026-04-06 | 800 lb / 200 lb |
| 2026-04-18 | 900 lb / 250 lb |
| 2026-04-30 | 1,000 lb / 300 lb |
| 2026-05-12 | 1,100 lb / 225 lb |
| 2026-05-24 | 1,200 lb / 275 lb |
| 2026-06-05 | 800 lb / 200 lb |
| 2026-06-17 | 900 lb / 250 lb |

**Why I set all of them aside (not just picked the newest):**
1. **They don't come from Pacific Malt.** Every one is from a personal Gmail account (Jake/Lauren), none from the supplier, none carries a PO number or "supersedes" language. They are chatter, not confirmations.
2. **They're physically impossible for this batch.** DW-2026-15 is a **7-bbl, OG 1.052, 5.25% amber lager** (`03.tsv`). That needs **~400 lb of total grain**. The *smallest* emailed order (800 lb Pilsner + 200 lb Munich = 1,000 lb) is ~2.5× the whole grain bill.
3. **They blow the recorded cost.** The batch's **total ingredient cost is $492.70** (`03.tsv`, includes malt + hops + yeast). At Pacific Malt's own pre-Q4 prices (Pilsner $0.87, Munich $0.91/lb, `04.xlsx`), 800 lb Pilsner + 200 lb Munich = **$878 in malt alone** — nearly double the entire batch's ingredient cost. None of the emailed quantities can be the order that was actually placed and paid.

**What actually stands:** unknown from the inbox. The defensible figure is a **~400 lb total grain bill (~$360 in malt at pre-Q4 prices), consistent with the recorded $492.70 total ingredient cost.** **Do not enter any inbox quantity as "ordered."**
**To settle it:** pull the **actual Pacific Malt invoice / PO for DW-2026-15** or the **Ekos batch sheet grain bill**. That is the only source I would stand behind. (If two field voice memos `02.mp3`/`05.mp3` include a Pacific Malt voicemail, they may hold it — they could not be transcribed here.)
*Note:* the Q4 price list (`04.xlsx`, effective Oct 1, +$0.05/lb across the board) applies to your **upcoming** orders — Winter Ale DW-2026-16, the Dunkel Q4 trial DW-2026-18 — **not** to Oktoberfest, which was brewed Feb 19 on the prior prices.

## 6. Distribution volume doesn't tie out  ⚠ UNSETTLED
- **HubSpot CRM (`15.xlsx`): 84 cases/month** across 8 accounts. **Partner deck (`22.pptx` slide 7): 124 cases/month.** ~40-case/month gap; last-order dates also differ.
- Use the **CRM (84)** as the system of record; the deck's 124 looks stale or aspirational. Reconcile before it feeds any revenue assumption. Distribution *revenue* lines are close ($86K vs $88K), so the case-count error hasn't (yet) distorted the top line — but fix it.

---
## Confidence summary
| Line | Figure | Confidence |
|---|---|---|
| Operating cash | $35,024.75 | HIGH ✅ |
| Distribution AR | $1,344 | HIGH ✅ |
| Supplier AP | $0 documented + 1 open (malt) | LOW ⚠ |
| Revenue | ~$350K (not $380K) | MEDIUM ⚠ |
| Operating net | ~$10K (not $40K); YTD actual $11,600 | MEDIUM ⚠ |
| Malt order qty | Not certifiable from inbox | BLOCKED ⛔ |
| Distribution volume | 84 cases/mo (CRM) | MEDIUM ⚠ |
