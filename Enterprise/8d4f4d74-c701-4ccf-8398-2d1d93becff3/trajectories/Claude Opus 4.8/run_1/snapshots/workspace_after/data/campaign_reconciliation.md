# Building Our Future — Trued-Up Roster Reconciliation
**Prepared for:** Rev. Colette Mullins (private working document — not for distribution)
**Date of review:** 2026-07-20
**Scope:** Independent, family-by-family review of the 16 top-tier campaign pledges, checked pledge line against giving landed, and cross-checked across every source found in the review packet.

---

## 1. What sources actually exist in this packet (and what does not)

Before any figure, the honest picture of the evidence, because a number is only as good as where it lives:

| Source found | What it is | Role |
|---|---|---|
| `file_15.xml` — *PledgeTracker* (`goal=2,500,000 secured=1,100,000 asof=2026-10-01`) | Structured pledge ledger, 16 families: Amount / Paid / Balance / NextContact | **Pledge line of record (present)** |
| `file_38.tsv` — *Family pledge / cultivation tracker* | 16 families: Pledge / Paid-to-date / Balance / Last-contact / Next-steps | **Cultivation notes + paid line (present)** |
| `file_26.pdf` (board minutes 10/15/26), `file_30.pdf` (campaign overview), `file_56.html` (dashboard), `file_51.pptx` (deck) | Narrative summaries | Corroborating summaries — all headline **$1.1M / 16 families** |

**Sources the review expected but did NOT find in this packet — flagged so no figure leans on a source that is not here:**

- **No Salesforce (donor system of record) export.** The two trackers above are internal working tools, not the database of record.
- **No independent money-trail export** — no Stripe, PayPal, Square, or QuickBooks/bank deposit report. The "received" figures below rest on the two internal trackers, **not** on independent processor/bank confirmation.
- **No crypto-gift data of any kind** — no coin type, quantity, wallet, or Coinbase/Binance/Kraken quote anywhere in the materials. (See §5.)
- The image, video, and audio files in the packet are personal-life material (stained-glass window, chess set, bread, Brandywine Falls footage, a Wood Thrush field recording, and a music track) — **none are financial records.**

**Bottom line on evidence:** the two financial sources that *do* exist **agree with each other on every family, to the dollar.** There is no per-family contradiction to arbitrate in the available records. That is a genuine finding, not an absence of work — but the confidence ceiling is set by the fact that neither the donor system of record nor the bank/processor trail was in the packet to confirm them against.

---

## 2. Family-by-family reconciliation (all figures traceable)

Pledge / Paid / Balance shown for each family. **`file_15.xml` and `file_38.tsv` match exactly for all 16** (verified programmatically; internal check `pledge = paid + balance` holds in every row).

| # | Family | Pledged | Received | Outstanding | % In | Cross-source | Verdict |
|--:|---|--:|--:|--:|--:|---|---|
| 1 | Hendricks | 200,000 | 100,000 | 100,000 | 50% | ✔ agree | On record; large balance to schedule |
| 2 | Morrison | 175,000 | 87,500 | 87,500 | 50% | ✔ agree | On record; Q4 statement due |
| 3 | Goldstein | 125,000 | 62,500 | 62,500 | 50% | ✔ agree | On record; **payment schedule unconfirmed** |
| 4 | Patel | 100,000 | 100,000 | 0 | 100% | ✔ agree | **Paid in full** |
| 5 | Bergman | 80,000 | 40,000 | 40,000 | 50% | ✔ agree | On record |
| 6 | Novotny | 75,000 | 75,000 | 0 | 100% | ✔ agree | **Paid in full** |
| 7 | Callahan | 60,000 | 30,000 | 30,000 | 50% | ✔ agree | On record |
| 8 | Okonkwo | 50,000 | 25,000 | 25,000 | 50% | ✔ agree | On record; Q1-2027 payment to confirm |
| 9 | **Fitzgerald** | 45,000 | **0** | 45,000 | **0%** | ✔ agree | **⚠ FLAG — pledged, nothing received** |
| 10 | Yamamoto | 40,000 | 20,000 | 20,000 | 50% | ✔ agree | On record; review pledge terms |
| 11 | Kowalski | 35,000 | 35,000 | 0 | 100% | ✔ agree | **Paid in full** |
| 12 | Delacroix | 30,000 | 15,000 | 15,000 | 50% | ✔ agree | On record |
| 13 | Walcott | 25,000 | 12,500 | 12,500 | 50% | ✔ agree | On record |
| 14 | Thornton | 25,000 | 25,000 | 0 | 100% | ✔ agree | **Paid in full** |
| 15 | Nguyen | 20,000 | 10,000 | 10,000 | 50% | ✔ agree | On record |
| 16 | Stern | 15,000 | 7,500 | 7,500 | 50% | ✔ agree | On record |
| | **TOTAL** | **1,100,000** | **645,000** | **455,000** | 58.6% | | |

---

## 3. Totals you can defend in front of Howard

- **Total pledged (commitment value):** **$1,100,000** — matches the headline every summary carries.
- **Total actually received to date:** **$645,000** — this figure is computed from the paid-to-date column; **no summary document in the packet states it.** Every deck and dashboard reports only the $1.1M pledged.
- **Outstanding on existing pledges:** **$455,000.**
- Against the **$2,500,000** goal: **pledge gap = $1,400,000** (matches the "$1.4M remaining" in the overview and dashboard). **Cash-in-hand gap = $1,855,000.**

The arithmetic that will match whatever Howard computes: `645,000 + 455,000 = 1,100,000`; `2,500,000 − 1,100,000 = 1,400,000`.

---

## 4. Findings surfaced directly (not smoothed into a total)

1. **The summaries hide the cash story.** Board minutes, overview, dashboard, and deck all lead with "$1.1M pledged." None report that **only $645K has actually landed.** This is the single most likely place Howard's questions go, and the packet in §BoardPacket presents received-vs-promised plainly so we are not caught telling a pledged number as if it were cash.

2. **Fitzgerald — $45,000 pledged, $0 received.** The one pledge where nothing at all has arrived. Both trackers agree, and `file_38` already carries the note "First payment pending — follow up Nov." Worth a direct, gentle conversation before it becomes a board line.

3. **Uniform 50% pattern is worth an eye.** Eleven of sixteen families sit at *exactly* half paid. For genuine multi-year pledges that can be perfectly normal (first installment in). But the uniformity is the kind of thing that reads as an estimate rather than a reconciled deposit figure — and with **no bank/processor trail in the packet to confirm it, I cannot certify these as landed cash.** Recommend confirming a handful against actual deposits before sign-off.

4. **No family shows a *reduced* pledge or a receipt exceeding its pledge.** No evidence in the available records of a commitment quietly cut or a mismatched receipt. If such a change lives in Salesforce or the deposit log, it is not in this packet.

---

## 5. OPEN VERDICTS (left open on purpose — evidence too thin to force a clean answer)

- **The crypto gift — UNRESOLVED, no valuation possible.** There is **no crypto data anywhere in the materials**: no coin, no quantity, no acquisition or gift date, no Coinbase/Binance/Kraken quote. I will **not** invent a figure to tidy the page. To value it honestly I need the coin and units and a gift-date price cross-checked across at least two exchanges. **Per your instruction and mine: nothing about that gift is to be moved, sold, or converted — that is your decision with the committee, and nothing here actions it.**
- **"Received" total ($645K) — provisional.** Confidence-capped until confirmed against the donor system of record and the actual deposit/processor trail, neither of which was in this packet.
- **Goldstein / Okonkwo payment schedules** — trackers note follow-ups pending; the schedules themselves are not in the records.

---

*Every figure above traces to `file_15.xml` (pledge line) and `file_38.tsv` (paid line + cultivation notes), which agree to the dollar, corroborated by `file_26.pdf`, `file_30.pdf`, `file_56.html`, and `file_51.pptx`. Where a figure could not be traced to a source in this packet, it is marked open rather than asserted.*
