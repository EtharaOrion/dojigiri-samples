# Driftwood Brewing — Q4 2026 Finance Summary (for the annual report brewery page)
**Confidential — partners only (Stuart Myer, Jake Callahan). Working draft for Stuart's review, 2026-10-20.**
Kept entirely on the brewery's side of the wall — no coalition data here.

---

## 1. ABV check — are the alcohol figures computed correctly off the logged gravities?
**Yes, all five recent batches are correct.** Using the standard ABV = (OG − FG) × 131.25:

| Batch | Beer | OG | FG | ABV (calc) | ABV (logged) | OK? |
|---|---|---|---|---|---|---|
| DW-2026-14 | Anniversary Wild Ale | 1.054 | 1.004 | 6.56% | 6.56% | ✔ |
| DW-2026-15 | Oktoberfest Amber Lager | 1.052 | 1.012 | 5.25% | 5.25% | ✔ |
| DW-2026-16 | Winter Ale Base Brew | 1.068 | 1.016 | 6.83% | 6.83% | ✔ |
| DW-2026-17 | Holiday Saison | 1.060 | 1.006 | 7.09% | 7.09% | ✔ |
| DW-2026-18 | Munich Dunkel | 1.052 | 1.014 | 4.99% | 4.99% | ✔ |

No corrections needed. Every logged ABV matches the gravities.

## 2. Ingredient cost per batch vs current malt pricing
**Malt increase (Pacific Malt Q4 2026 list, effective October 1, 2026):** +$0.05/lb on all base malts (Pilsner, Pale Ale, Munich, Munich Dark, Vienna, Wheat) and most crystal/roast; +$0.06/lb on Crystal 60L and Acidulated; +$0.04/lb on Flaked Oats.

**Which batches are on which cost basis (by brew date vs the Oct 1 price change):**

| Batch | Brew date | Logged ingredient cost | Cost basis |
|---|---|---|---|
| DW-2026-14 | 2025-09-10 | $303.60 | **OLD** (pre-increase) |
| DW-2026-15 | 2026-02-19 | $492.70 | **OLD** (pre-increase) |
| DW-2026-16 | 2026-10-06 | $510.60 | **Current** (post Oct 1) |
| DW-2026-17 | 2026-10-08 | $445.30 | **Current** (post Oct 1) |
| DW-2026-18 | 2026-10-13 | $517.86 | **Current** (explicitly the Q4 cost trial batch) |

**So the three Q4 batches (DW-16, -17, -18) already reflect current malt pricing.** DW-14 and DW-15 are on the old basis.

> **⚠️ Missing input — cannot finalize an exact current-basis restatement of DW-14/DW-15.** Recomputing those two at current pricing requires their **grain bills (lb of each malt per batch)**, which are not in the data I was given. The direction is known (+$0.05/lb of base malt), so the impact scales directly with grain weight — but I am not putting an invented pound count into the summary. **What I need from you:** the per-batch grain bills (or a total grain-weight figure) for DW-14 and DW-15, and I'll restate them exactly. If those two older beers aren't part of the Q4 page, this is moot and the Q4 numbers above already stand.

## 3. Batch economics / margins at the prices we actually sell
Basis: a 7-bbl batch = 217 gal = **1,736 × 16-oz pours (gross, before cellar/serving loss of roughly 8–12%)**. Taproom pint prices from the current menu.

| Batch | Beer | Ingredient cost | Ingredient $/pint | Taproom price | Gross taproom value (1,736 pours) | Ingredient cost as % of taproom value |
|---|---|---|---|---|---|---|
| DW-2026-15 | Oktoberfest Amber | $492.70 | $0.284 | $8/pint | ~$13,888 | 3.5% |
| DW-2026-16 | Winter Ale | $510.60 | $0.294 | **TBD** | — | set price to finalize |
| DW-2026-17 | Holiday Saison | $445.30 | $0.256 | $8/pint | ~$13,888 | 3.2% |
| DW-2026-18 | Munich Dunkel | $517.86 | $0.298 | $7/pint | ~$12,152 | 4.3% |
| DW-2026-14 | Anniversary Wild Ale | $303.60 | $0.175 | $10/pour (+ 250×500ml bottles) | — | limited release, priced separately |

**Read on margins:** at taproom prices, ingredient cost is only **~3–4.5% of gross sales value** per batch — healthy, and the malt increase moves that ratio by well under a point. **But that is the taproom-price ceiling, not blended reality.** Roughly a third of each batch self-distributes at wholesale — from the QuickBooks invoices, a 1/6-bbl keg runs ~$165, i.e. **~$4.00 per pint-equivalent** vs the $7–$8 taproom pint. Blended realization (taproom + wholesale) lands well below the taproom figure, so use these as **ingredient-margin ceilings**, not net margins. Net margin also carries packaging, labor, rent, and overhead — the P&L's total COGS (ingredients + packaging) is ~$124–132K for the year, of which these per-batch ingredient lines are only the ingredient slice.

**To finalize:** set the Winter Ale (DW-16) taproom price and confirm the taproom/wholesale volume split you want me to blend on.

## 4. Wholesale accounts receivable — what's owed right now (QuickBooks, source of truth)
Pulled live from QuickBooks (realm = Driftwood Brewing Company). **The QuickBooks customer balances are the money we can actually count on.**

| Account | Balance due |
|---|---|
| **Woodstock Wine & Beer** | **$693.00** |
| **Hawthorne Fermentary** | **$505.50** |
| **Laurelhurst Public House** | **$280.50** |
| All other 17 wholesale accounts | $0.00 |
| **Total outstanding (real AR)** | **$1,479.00** |

**Worth chasing before the quarter closes:** all three, in order of size — **Woodstock ($693), Hawthorne Fermentary ($505.50), Laurelhurst ($280.50)**. Laurelhurst's open item is the oldest (traces to an October 2025 invoice), so start there for aging even though it's the smallest.

> **⚠️ Data-integrity flag — do NOT report the raw invoice ledger as receivables.** The QuickBooks *invoice-level* `Balance` fields are stale: ~105 invoices show open balances summing to roughly **$19,780**, but those flags don't reconcile to customer balances or to applied payments (many "open" invoices were in fact paid, and the fixture never cleared the flag). Counting that $19.8K would be exactly the "money we hoped for" trap. **The reconciled, collectible figure is $1,479.** Recommend a QuickBooks invoice-to-payment cleanup so the ledger ties out.
>
> Separately: the **HubSpot CRM sheet lists different account names and balances** (e.g., "Knotty Pine $392," "Cardinal $364," total $1,344) that do **not** match QuickBooks. HubSpot is out of sync — **treat QuickBooks as the AR source of truth** and reconcile HubSpot later.

## 5. Open items for you
1. Grain bills for DW-14 and DW-15 (only if they belong on the Q4 page) → exact current-basis restatement.
2. Winter Ale (DW-16) taproom price.
3. The taproom-vs-wholesale volume split you want used for blended per-batch margins.
4. Green-light to chase Woodstock, Hawthorne Fermentary, and Laurelhurst on their balances.
