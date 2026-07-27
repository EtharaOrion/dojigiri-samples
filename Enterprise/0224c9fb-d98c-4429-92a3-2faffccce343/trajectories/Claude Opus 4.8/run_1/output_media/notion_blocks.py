import json, os, urllib.request

PAGE="page-4ad217834455"
BASE=os.environ["NOTION_API_URL"]

B=[]
def h1(t): B.append(("heading_1",t))
def h2(t): B.append(("heading_2",t))
def h3(t): B.append(("heading_3",t))
def p(t): B.append(("paragraph",t))
def li(t): B.append(("bulleted_list_item",t))

h1("Q3 Board Reconciliation — Grant & Sponsorship Provenance Log")
p("Owner: Andrew Santos (ED). Prepared 2026-07-20 ahead of the Q3 board meeting. Purpose: for every figure trued up this round, record (a) the value(s) seen and where each came from, (b) the number Andrew now stands behind, and (c) why. Rule applied throughout: the pipeline is a claim to be checked; where a line and the cash disagree, the cash wins and it is said plainly.")
p("Sources of record: Xero restricted-fund books (Livernois), HubSpot deals (pipeline of record), Stripe/Square (cash actually collected), plus internal workbooks, the fundraising dashboard, board deck, sponsor one-sheet, and the anonymized prospect pipeline. 'Cash' = a receipt visible in a connected financial system.")

h1("A. Showcase Sponsorship")

h2("A1. Great Lakes Power Foundation — headline sponsor")
li("Values seen: $25,000 (sponsor one-sheet file_29; showcase workbook file_24; fundraising dashboard file_42; board deck file_44/45; HubSpot deal 411 stage sponsor_signed; contact note for Lisa Monroe). $62,500 (HubSpot deal 427 'GLPF sponsorship — 2026', grants pipeline, full_proposal_submitted). $162,500 (HubSpot deal 435 'GLPF headline renewal — 2026', grants pipeline, awarded).")
li("STANDING BEHIND: $25,000 signed commitment; $0 cash received to date.")
li("Why: $25,000 is the only figure carrying a signed sponsor deal (411), a completed board-confirmation task, and the relationship-owner note (Lisa Monroe). The $62,500 and $162,500 sit in the wrong pipeline (grants, not sponsors), carry no signed status, and disagree with each other by $100,000 — optimistic placeholders / data-entry drift. No $25,000 receipt appears in Stripe, Square, or Xero, so it is a pledge, not money in the door. Confirm the check with Lisa Monroe / development before stating as 'raised'.")

h2("A2. Second signed showcase sponsor — Rivertown Partners LLC (tier 3)")
li("Values seen: $5,000 (HubSpot deal 415, sponsor_signed). Related but different: dashboard file_42 'Local Business Circle $10,000 (Open)'; prospect pipeline P-303 at 'Friend' level (= $5,000 on the one-sheet, but = $1,000 on the public form).")
li("STANDING BEHIND: $5,000 signed; $0 cash received to date.")
li("Why: Rivertown is the actual signed tier-3 sponsor in the CRM at $5,000. The dashboard's '$10,000' local-business line overstates by $5,000 and the 'Friend' label is unreliable (means $5k in one document, $1k in another). Believe the signed $5,000.")

h2("A3. Soft showcase sponsor — DTE Energy Foundation (tier 2)")
li("Values seen: $10,000 (HubSpot deal 412, sponsor_proposal_sent).")
li("STANDING BEHIND: $0 defensible; $10,000 soft (proposal out, unsigned).")
li("Why: proposal sent, not signed. Counts as pipeline only.")

h2("A4. Do NOT count as showcase — Livernois-opening sponsors")
li("Ford Motor Company Fund $15,000 (HubSpot 413, verbal_commit) and General Motors Foundation $15,000 (HubSpot 414, intro_meeting) are tagged 'Livernois opening sponsor', a different event. If rolled into the showcase pipeline they inflate it by up to $30,000 of wrong-event soft money. Keep in the Livernois-opening bucket.")

h2("A5. In-kind partners (no cash)")
li("Motor City Chronicle — media partner (HubSpot 416, signed, $0). Midtown Arts Collective — co-programming (HubSpot 417, intro, $0). In-kind; do not count toward the $120,000 cash goal.")

h2("A6. Sponsor-tier naming collision (fix before the pack goes out)")
li("$10,000 tier is called 'Champion' (one-sheet/prospect pipeline) and 'Spotlight' (deck/public form). $5,000 tier is 'Friend' (one-sheet) and 'Stage Light' (deck). $1,000 tier is 'Friend of the Arts' (deck/public form only). 'Friend' therefore means $5,000 in one place and $1,000 in another. Standardize on one tier sheet.")

h2("A7. Showcase cash actually collected (Stripe)")
li("Showcase tickets collected: $3,840 (55 tickets: one-time $1,920 + sponsor-tier $1,920). General donations (not showcase raise): $2,272. Square terminal: $236 unattributed small sales, no auction/showcase cash (event is 2026-11-14, future). Auction $0 to date.")

h2("A8. Showcase gap — the net the board should see")
li("Goal $120,000. Signed-or-received to date: $33,840 ($25,000 GLPF pledge + $5,000 Rivertown pledge + $3,840 ticket cash). Soft/ahead: DTE $10,000, remaining tickets ~$26,160, live auction $35,000. Event cost $45,000 (venue $12k + production $10k committed = $22k firm; catering $8k quoted, marketing $5k in progress, awards $10k planned = $23k not yet firm). Net at today's signed position: $33,840 − $45,000 = −$11,160 (underwater until more closes). Net at full goal: $120,000 − $45,000 = $75,000.")

h1("B. Livernois Restricted Renovation Fund")

h2("B1. Restricted award received")
li("Greenfield Year-1 restricted tranche: $75,000 received (Xero INV-2047 PAID, ref GREENFIELD-Y1-LIVERNOIS-RESTRICTED). This is the hard cash the renovation draws against.")

h2("B2. Renovation envelope vs actual contractor ledger (Xero, restricted expense code 500)")
li("Planned envelope: $28,000 (deck file_46: Buildout 11k / Studio equipment 7k / Safety & code 4k / Furnishing 4k / Contingency 2k).")
li("Actual to date — PAID $17,250: Electrical rough-in 4,200; HVAC commissioning 3,850; Flooring 3,200; ADA build-out 2,650; Drywall & paint 1,250; Baseboard & trim 650; Plumbing fixtures 900; Permit & inspection 550.")
li("AUTHORISED (approved PO, unpaid) $5,400: Signage exterior/wayfinding 1,900; Program-room millwork 3,500.")
li("SUBMITTED (awaiting approval) $3,200: Furniture delivery/install 2,400; Interior donor-recognition signage 800.")
li("DRAFT (not yet authorized) $1,950: Final punch-list / C-of-O fixes 1,500; Program storage shelving 450.")
li("Totals: Paid $17,250 | Paid+Authorised $22,650 | +Submitted $25,850 | +Draft (fully projected) $27,800.")

h2("B3. Verdict")
li("STANDING BEHIND: on budget, NOT over. Fully projected commitment $27,800 vs the $28,000 envelope = $200 headroom. Cash actually out the door: $17,250.")
li("The 'few-thousand drift' Andrew felt is TIMING/POSTING, not an overrun: depending on whether a prior snapshot counted paid-only ($17,250) or committed ($22,650–$25,850), you get a $5,400–$8,600 difference. Same project, different cut of the same ledger.")

h2("B4. Held open — do not force to a clean total")
li("No discrete 'Studio equipment $7,000' line has posted to the restricted renovation account. Either it is still to come, was reclassified, or belongs to program (not renovation) budget. Resolve before the Greenfield report so composition matches the narrative. To close: confirm with development/bookkeeping whether studio equipment is restricted-renovation or program spend.")
li("Cross-contamination guard: Detroit Home Pros / Andre Williams also holds the PERSONAL Palmer Woods kitchen job ($18,000, household funds). That $18,000 must never post to the Livernois restricted account. The Xero restricted lines are correctly tagged LIVN-WO-*; keep it that way.")

h1("C. Four Institutional Funders")

h2("C1. Greenfield Foundation — $150,000 (2-year)")
li("STANDING BEHIND: $75,000 Year-1 restricted cash received (Xero INV-2047). Full award value $150,000 over two years.")
li("Noise/flags: HubSpot 401 labels it '$150,000 Year 2 renewal awarded' while the internal record says we are in Year 1; 423 shows a '$12,500 Year 2 milestone', 421 a '$0 reporting-requirement' placeholder. Reconcile the Year-1/Year-2 label. Obligation due: Year-1 grant report (fall 2026); Year-2 milestone narrative + budget reconciliation March 2027 (condition on the Year-2 tranche).")

h2("C2. Beacon Foundation — renewal (the 'step-up')")
li("Values seen: $75,000 (file_6; HubSpot 402 full_proposal_submitted) vs $25,000 (HubSpot 424 'renewal 2026' full_proposal_submitted); 422 site_visit_scheduled $0.")
li("STANDING BEHIND: $0. Nothing awarded. The step-up is wishful until awarded — and the CRM carries two conflicting submitted amounts ($75k and $25k).")
li("Obligation/condition: renewal narrative due fall; submission due 2026-12-15 (file_51). Resolve the $25k vs $75k ask before submitting so the board is not told a number the proposal doesn't match.")

h2("C3. ACF Art Works — $50,000 (project)")
li("STANDING BEHIND: $50,000 received (HubSpot 403 awarded; calendar file_49 'award received 2026-01-15'; workbook file_6 'Received').")
li("Noise: HubSpot 425 '$37,500 reporting 2026' is a reporting entry, not new money — ignore for totals. Obligation due: interim update this winter (owned by development).")

h2("C4. City of Detroit Cultural Affairs — $35,000 (annual)")
li("STANDING BEHIND: $35,000 current operating grant, active (HubSpot 404 awarded; file_6 active).")
li("Noise: HubSpot 428 '$75,000 renewal 2026' is a future ask at 2x, not secured. Obligation/condition: annual re-application due this winter, via the City grant-admin portal (NOT connected → manual hand-off; report deadline, never mark done).")

h2("C5. Hartwell (scoped for the site visit, not one of the four) — flag")
li("HubSpot shows 405 '$90,000 LOI submitted' AND 426 '$50,000 full application awarded'. 'Awarded' conflicts with the internal status (full application in review, site visit Nov 5/7 pending). Do NOT treat Hartwell as awarded; almost certainly a premature/optimistic entry. Confirm actual status before any board statement.")

h1("D. Manual hand-offs (portals not connected — never auto-close)")
li("Beacon renewal submission — due 2026-12-15 — funder portal, manual. Report deadline; do not mark done.")
li("City Cultural Affairs annual re-application — winter — City grant-admin portal (Box), manual. Report deadline; do not mark done.")
li("Hartwell full application follow-through — site visit Nov 5/7 — Hartwell portal, manual. Report deadline; do not mark done.")

h1("E. Open scheduling discrepancy")
li("Hartwell site visit date: internal calendar file_49 says 2026-11-05 (Thu); workspace HEARTBEAT says 2026-11-07 (Sat, 10am–noon). Confirm which before finalizing the agenda.")

# build children with the mock's flat text schema
children=[{"object":"block","type":t,"text":txt} for (t,txt) in B]
payload=json.dumps({"children":children}).encode()
req=urllib.request.Request(BASE+"/v1/blocks/"+PAGE+"/children",data=payload,
    headers={"Content-Type":"application/json"},method="PATCH")
r=urllib.request.urlopen(req)
res=json.load(r)
print("appended blocks:",len(res.get("results",[])))
