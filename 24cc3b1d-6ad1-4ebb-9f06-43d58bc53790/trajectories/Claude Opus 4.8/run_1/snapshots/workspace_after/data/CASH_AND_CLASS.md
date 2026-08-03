# Jake's Table — Cash & Class Picture (trued up)
_Honest numbers only. Where sources fight, I name which I trusted and which I set aside, and I leave open what won't foot._

---

## 1) Q4 2026 class revenue — the real quarter, end to end

| Figure | Value | Source | Verdict |
|---|---|---|---|
| **Your preliminary jot** | **$4,200** | Estimated-tax log (Q4 2026), marked unpaid / due 2027-01-15 | ⬅️ what you wrote down |
| QuickBooks interim preliminary | $3,200 | QB note on first Q4 invoice (10/01), "pending final reconciliation" | superseded |
| **QuickBooks corrected/reconciled** | **$3,470** | QB note on last Q4 invoice (12/31), **"after final reconciliation of all class seats"** | ✅ **TRUE TOTAL** |

- **True Q4 2026 class revenue = $3,470.**
- **Gap vs your jot: −$730** (your preliminary $4,200 was ~$730 high). It also landed $270 above the interim $3,200.
- **Why I trust $3,470:** it's the post-reconciliation figure in the system of record (QuickBooks), stamped after all late-settling seats came in — exactly the "invoices kept landing after I wrote the number down" effect you flagged. It also fits your own history: prior quarters ran $2,800–$4,300 (Q4'24 $3,200 · Q1'25 $2,800 · Q2'25 $3,600 · Q3'25 $3,100 · Q4'25 $4,300). $3,470 is right in the band.
- **What I set aside, and why:** the raw QuickBooks **invoice line detail does NOT foot to $3,470** — summing the `INV-JT` line items gives ~$9,860 paid / ~$13,085 invoiced for the quarter. That's impossible for a ~$14k/year business (~31 invoices/quarter, every 3 days). The customer/invoice tables are **contaminated with a martial-arts-dojo mock** (customers tagged "Kendo M/W/F," "Judo T/Th," "Household Co," tournament & bar-tab line items, a "system-generated duplicate — needs void"). So the line-level detail is unreliable; only the **reconciled summary tally** is trustworthy.
- ⚠️ **Still open (not forcing a tidy total):** the $3,470 is defensible as the reconciled headline, but the underlying line detail can't be cleanly reconciled to it because of the contaminated rows. **Before you file the 1/15/2027 quarterly, confirm $3,470 is the final class-revenue figure** and get the line detail cleaned.
- **Downstream flag (not tax advice):** your tax log computed self-employment tax ($594) and the estimated payment ($600) off the stale **$4,200**. At **$3,470** those come down (~$490 SE tax at the log's own ~14.1% rate). Update the log before filing; the exact payment is your / the CPA's call.

## 2) Per-seat contribution — home vs venue (which format pulls its weight)

Modeled from your pricing and the deck's cost basis (~$200/mo supplies ÷ ~16 seats/mo ≈ **~$12.50 food/seat**; processor fee ~$2.20–2.50/seat). Contribution = price − food − fees (before fixed cards/photo).

| Format | Price/seat | Est. variable/seat | **Contribution/seat** | Cap | Full-class contribution |
|---|---|---|---|---|---|
| **Home** | $75 | ~$15 | **~$60** | 8 | 8 × $60 = **$480** |
| **Venue** | $65 | ~$15 (+ any venue/Square premium) | **~$50** | 12 | 12 × $50 = **$600** |

- **Per seat, HOME wins by ~$10** — the venue's $10-lower price drops straight off the bottom line while food cost is basically the same.
- **Per session at a full room, VENUE can out-earn** because it seats 12 vs 8.
- **Takeaway:** keep premium/small-batch content at **home** ($/seat), use **venue** when you can fill the bigger room. ⚠️ This is modeled, not itemized per class — food cost per seat isn't broken out per menu, so treat as a planning estimate.

## 3) Holiday Brunch (Dec 6) — what it actually nets on the corrected roster

- **Roster: 3 paid** (Leslie Huang, Nina Osei, Jerome Banks), not 8. Revenue **3 × $75 = $225** (claimed was 8 × $75 = $600).
- **Menu** (from the site): herb-marinated turkey breast · sweet potato casserole (pecan crust) · collard greens w/ smoked turkey · peach cobbler · cornbread (brunch-spread foundation).
- **Food cost per head** (recipe cost sheet): sweet potato casserole $3.40 + collards $3.90 + peach cobbler $2.60 + cornbread $1.80 = **$11.70/head** for the four costed dishes. **Turkey breast is not on the cost sheet → open line** (est. ~$4–6/head; confirm).
- **Net at 3 heads:** $225 − (~3 × ~$16.70 food ≈ **~$50**) − (~$7.50 fees) ≈ **~$165–170 net** (before recipe cards/photo).
  - For contrast, at the phantom 8 it would have "netted" ~$450 — a number you'd have shopped and staffed against.
- **Scale the market list DOWN to 3 (+1–2 buffer), not 8.** Rough saving vs buying for 8 ≈ **~$80–130** in protein/produce you'd otherwise over-buy.

**Corrected brunch shopping guide (for 3–4, from the cost sheet + class list):**
| Item | For ~4 servings | Source |
|---|---|---|
| Turkey breast (herb-marinated) | 1 small breast (~3–4 lb) | DeKalb Farmers Market |
| Sweet potatoes | ~2.5 lb | Costco |
| Pecans | ~1 cup | Costco |
| Collard greens | 1 bunch | DeKalb Farmers Market |
| Smoked turkey neck | 1 | DeKalb Farmers Market |
| Fresh peaches (or garden-freezer stash) | ~2 lb | DeKalb / freezer |
| Stone-ground cornmeal, buttermilk, butter, brown sugar | pantry check | Costco |

⚠️ **OPEN:** seats are still being marketed (Dec 1 IG story "seats open for Dec 6"), so recheck the enrollment list the day before the market run — if it climbs toward 8, scale back up.

## 4) Business profile in the books — what I found

You asked me to fix the "wrong owner and wrong address." Here's the live read of the QuickBooks company profile (checked directly, last updated 2026-10-30):
- **Owner: "Jake Thornton"** — ✅ correct.
- **Address: 2214 Alston Dr SE, Atlanta, GA 30317** (East Lake) — reads consistent with your records. _If the street is wrong, tell me the correct one — it's redacted in my stored copy so I can't independently verify the exact line._
- **Real anomalies I did find:**
  1. **LegalName is doubled: "Jake's Table LLC LLC."**
  2. **A stray co-owner: `CoOwnerName = Marcus Johnson`** sits alongside `OwnershipSplit = "Jake 100%"` — contradictory (Marcus is your husband, not a Jake's Table co-owner).
- **Why I did not auto-fix it:** the QuickBooks connector exposes company info as **read-only** — my correction POST came back **405 Method Not Allowed**. I did not fabricate a change.
- **Do this:** correct **LegalName → "Jake's Table LLC"** and **remove the `CoOwnerName` entry** directly in QuickBooks (or hand to the CPA). Confirm the address street if it's off and I'll flag anything else writable. The owner field itself is already right, so the books aren't lying about *whose* company it is — they're just carrying a duplicated legal name and a phantom co-owner.

---

### Discrepancy ledger (what I trusted vs set aside)
| Question | Sources in conflict | Trusted | Set aside | Why |
|---|---|---|---|---|
| Tasha EDD | tracker/tracker/dashboard/rotation all Nov 14; GA labels rounded | **Nov 14** | rounded weekly GA labels | 4 systems agree + 38+4 math on 11/04 = Nov 14 exactly |
| Q4 revenue | jot $4,200 · QB interim $3,200 · QB reconciled $3,470 · line sum ~$9.8k | **$3,470** | $4,200, $3,200, line detail | reconciled system-of-record figure; fits history; line detail contaminated |
| Brunch roster | enrolled "8" (file + deck) vs 3 paid | **3 paid** | "8 enrolled" | settled per-student payments beat aggregate claim; IG still marketing open seats |
| Class start time | syllabus PDF "2:00 PM" vs site/calendar "1:00 PM" | **1:00 PM** | 2:00 PM syllabus | live site + calendar over static syllabus; syllabus is stale — fix it |
| Out-month on-call windows | dashboard vs rotation file disagree | **rotation file** | dashboard out-months | client-specific rotation is purpose-built; flagged for Keisha |
