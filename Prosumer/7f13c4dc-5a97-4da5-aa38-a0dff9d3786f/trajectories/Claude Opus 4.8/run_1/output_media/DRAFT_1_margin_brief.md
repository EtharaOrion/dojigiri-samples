# DRAFT 1 — Per-Batch Margin Brief, Fall Run (DW-2026-14 → 18)
**Confidential — Stuart Myer and Jake Callahan only. Working draft, not final.**
Prepared for the Q3/fall true-up. Data as read off the batch cost log and the Q4 partner deck; nothing here is fabricated. Where a number can't be stood behind yet, it is flagged OPEN, not guessed.

---

## Bottom line up front
- **Only one of the five batches has actually reached customers: DW-2026-15 Oktoberfest (released 10/03).** The other four are either aging-to-release (DW-14, releases 10/31) or still fermenting (DW-16/17/18). You can't honestly cut a margin on those yet.
- **Even Oktoberfest's margin is NOT closeable from the files provided.** The ingredient COST side is solid ($492.70, corroborated in two places). The REVENUE side — pints poured and kegs shipped for *this* batch — is not in any readable file. That's the blocker, not the cost.
- **No cost *disagreement* actually shows up in the readable records.** The batch cost log and the partner deck agree to the cent on all five batches. The "number Jake keeps quoting that I no longer trust" is not in any file I can open — it is presumably in the two voice memos (02.mp3 / 05.mp3, which could not be transcribed here) or in Ekos/QuickBooks, which weren't provided. See Blockers.

---

## Margin ranking (as far as the data honestly allows)

Margin as you defined it = **(batch revenue − ingredient cost) ÷ batch revenue**. Revenue basis = taproom pours + wholesale kegs for that specific batch. Ingredient cost only (packaging/labor excluded, per your framing).

| Rank | Batch | Beer | Ingredient cost (stood behind) | Revenue basis | Gross margin | Status |
|---|---|---|---|---|---|---|
| 1 | DW-2026-15 | Oktoberfest Amber Lager | **$492.70** | **OPEN — no per-beer sales / keg-depletion data** | **OPEN** | Released 10/03; the season's workhorse. Cost is defensible; revenue is the missing input. |
| — | DW-2026-14 | Anniversary Wild Ale | $303.60 | n/a | Not yet answerable | Single-night release **10/31** (250 × 500ml + one night draft). Hadn't sold at data date. Revisit after 10/31. |
| — | DW-2026-16 | Winter Ale Base Brew | $510.60 | n/a | Not yet answerable | Fermenting; holiday release **12/19**. Highest grain bill of the set. |
| — | DW-2026-17 | Holiday Saison | $445.30 | n/a | Not yet answerable | Fermenting; packaged 11/21. Only "preview" pours so far. |
| — | DW-2026-18 | Munich Dunkel | $517.86 | n/a | Not yet answerable | Fermenting; Q4 pricing **trial** batch, packaged 11/14. |

**No beer is "quietly bleeding" on the ingredient line** — grain bills are $304–$518 on 7-bbl batches, which is normal. Whether any beer bleeds depends entirely on the revenue/mix, which is the open item.

---

## Cost cross-check (what I could and couldn't verify)

**Two readable sources, and they agree:**
| Batch | Batch cost log (03.tsv) | Partner deck slide 4 (22.pptx) | Agree? |
|---|---|---|---|
| DW-14 | 303.60 | 303.60 | ✓ |
| DW-15 (Oktoberfest) | 492.70 | 492.70 | ✓ |
| DW-16 | 510.60 | 510.60 | ✓ |
| DW-17 | 445.30 | 445.30 | ✓ |
| DW-18 | 517.86 | 517.86 | ✓ |

So there is **no figure I had to overturn** — because no readable source contradicts these. That is itself worth knowing: if Jake is quoting a different Oktoberfest cost, it isn't coming from either of these documents.

**One real apples-to-oranges flag on the cost *trend*, not the levels:** Pacific Malt's Q4 list (effective **10/01/2026**) raised malt 5–6¢/lb (Munich 0.91→0.96). The batches straddle that increase:
- Brewed **before** the increase (old price round): DW-14 (9/10/2025), **DW-15 Oktoberfest (2/19/2026)**.
- Brewed **after** (Q4 prices): DW-16 (10/6), DW-17 (10/8), DW-18 (10/13, explicitly the "Q4 cost trial").

Putting all five on one "cost per batch" chart compares pre- and post-increase grain bills. That's fine for a trend line but **do not read DW-18 vs DW-15 as a like-for-like recipe delta** — part of the gap is the price round, not the recipe.

**What I could NOT do:** recompute any grain bill from scratch to "run the disagreement to a defensible figure." That requires the per-batch recipe (lbs of each malt/hop/yeast) or the underlying Pacific Malt / Crosby Hops invoices. Neither is in the readable files. **This is why the margin brief cannot be finalized** — per your sequencing rule, no final margin hardens until the cost question is actually resolved, and resolving it needs the recipe or the supplier invoice.

---

## ABV sanity check — commercial standard vs the homebrew shortcut

You asked me to check strength against the commercial standard, not the `(OG−FG)×131.25` shortcut (which is the formula printed on the taproom education deck, 38.pptx, and the one baked into the batch log). Using the standard formula **ABV = 76.08·(OG−FG)/(1.775−OG) · (FG/0.794)**:

| Batch | Beer | OG | FG | Shortcut ×131.25 (on menus now) | **Commercial standard** | Δ |
|---|---|---|---|---|---|---|
| DW-15 | Oktoberfest | 1.052 | 1.012 | 5.25% | **5.36%** | +0.11 |
| DW-14 | Anniversary Wild Ale | 1.054 | 1.004 | 6.56% | **6.67%** | +0.11 |
| DW-16 | Winter Ale | 1.068 | 1.016 | 6.83% | **7.16%** | +0.34 |
| DW-17 | Holiday Saison | 1.060 | 1.006 | 7.09% | **7.28%** | +0.19 |
| DW-18 | Munich Dunkel | 1.052 | 1.014 | 4.99% | **5.11%** | +0.12 |

**Action:** The shortcut under-states every beer, most on the Winter Ale (+0.34%). Oktoberfest and the Wild Ale are going on the festival sheet and a bottle label — use **5.36%** and **6.67%** on anything a regulator or buyer reads. (These are recomputed from the reported OG/FG; if the hydrometer readings themselves are in question, confirm the gravities.)

---

## To close DW-15 Oktoberfest (the one you actually want)
1. **Square item-sales report by beer** for the Oktoberfest run (units + $ of Oktoberfest pints/flights, 10/03 onward) — the 08.tsv export only covers 10/01–10/07 and gives daily *gross* + "top seller," not per-beer dollars.
2. **Keg-out log for DW-15** — how many ½-bbl / sixtel kegs went to the 8 wholesale accounts and at what per-keg price.
3. Then: revenue = taproom $ + wholesale $; margin = (revenue − 492.70) ÷ revenue.

*Scale context only (NOT a margin, do not quote):* a 7-bbl batch ≈ 217 gal ≈ ~1,600 sellable pints after cellar/foam loss; at $8 taproom that's a ~$12–13K gross ceiling if 100% poured in-house. Wholesale realizes less per ounce. Point being the $492.70 grain bill is a small slice of a full batch's value — the number that matters is the taproom/wholesale **mix**, which is the open input.
