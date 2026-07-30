#!/usr/bin/env python3
import os, json, urllib.request

QB = os.environ['QUICKBOOKS_API_URL'] + '/v3/company/4620816365272861350'
A  = os.environ['AIRTABLE_API_URL'] + '/v0/appNW1studio0001'

def post(url, body):
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())

# ---- The 13-line ledger with verdicts ----
LEDGER = [
 # id, date, item, vendor, amount, verdict, acct_id, acct_name, reason
 ("10165","2026-01-06","Athenahealth EHR & practice-mgmt subscription","Athenahealth",549.00,"HOLD","20","Software & Subscriptions","Legitimate clinic software, but at/above the $250 sign-off threshold — needs your approval before it is committed. Also confirm no overlap with the $1,200/mo Athenahealth AP bills."),
 ("9668","2026-01-08","Cedarbrook Artisan — watercolor pans & sable brushes","Cedarbrook Artisan Supply",236.48,"REJECT",None,None,"Botanical-illustration supplies, not clinic business; the identical $236.48 charge posts to your PERSONAL checking in Plaid (01-07). Studio spend miscategorized as a clinic expense."),
 ("19260","2026-01-13","Ridgemont Fine Papers — cotton-rag sheets (commission)","Ridgemont Fine Papers",142.00,"REJECT",None,None,"Cotton-rag for commission work — personal studio spend; matches your personal Plaid charge 01-09 ($142.00). Not a clinic expense."),
 ("17205","2026-01-19","Cascade Medical Waste — sharps/biohazard pickup","Cascade Medical Waste Services",165.00,"APPROVE","14","Medical Supplies","Monthly clinical waste pickup — clearly clinic, foots to receipt, under $250. Clean approval."),
 ("18438","2026-01-24","Northwest Framing — exhibition frames (Wild Botanica)","Northwest Framing & Matting",312.00,"REJECT",None,None,"Framing for your gallery exhibition, not clinic; at/above $250. DOUBLE-REPRESENTED: an identical $312 'exhibition frames' charge also appears on your personal Plaid feed (03-14). This is the line that reads as 'entered more than once.'"),
 ("15555","2026-02-03","Adobe Creative Cloud — design software","Adobe",89.99,"HOLD","20","Software & Subscriptions","Ambiguous: could be clinic marketing/portal OR studio/portfolio design. Cannot confirm business use from the ledger — needs your eye before it clears."),
 ("12630","2026-02-09","Cedarbrook Artisan — gouache set & archival ink","Cedarbrook Artisan Supply",198.75,"REJECT",None,None,"Studio supplies, not clinic; matches your personal Plaid charge 02-11 ($198.75)."),
 ("10601","2026-02-14","Columbia Uniform & Linen — scrubs & exam gowns","Columbia Uniform & Linen",128.40,"APPROVE","14","Medical Supplies","Clinical scrubs/exam gowns — clearly clinic, foots to receipt, under $250. Clean approval."),
 ("16687","2026-02-20","Staff meeting lunch — Jamison Kitchen, Beaverton","Jamison Kitchen",74.60,"APPROVE","22","Meals & Entertainment","Staff-meeting meal — reimbursable under the meals policy, foots to receipt, under $250. (Plaid shows a SEPARATE personal Jamison Kitchen dinner of $68.45 on 01-24 — a different visit, not this charge.)"),
 ("11320","2026-03-04","CME registration — Pacific NW Dermatology Update","PNW Dermatology Update",425.00,"HOLD","19","Continuing Medical Education","Legitimate continuing education, but at/above the $250 threshold — needs your sign-off before it is committed."),
 ("16935","2026-03-11","Evergreen Office — front-desk paper & printer supplies","Evergreen Office Solutions",210.00,"APPROVE","14","Medical Supplies","Front-desk office supplies — clinic operations, under $250. (Booked to Medical Supplies as the nearest supplies account; there is no dedicated office-supplies account.)"),
 ("17492","2026-03-18","Northwest Framing — custom frames (commissioned panels)","Northwest Framing & Matting",340.00,"REJECT",None,None,"Framing for your commissioned art panels, not clinic; at/above $250. Studio/commission cost miscategorized as a clinic expense."),
 ("14898","2026-03-25","Beaverton Chamber of Commerce — membership & listing","Beaverton Chamber of Commerce",450.00,"HOLD","16","Marketing & Advertising","Legitimate business membership, but at/above the $250 threshold — needs your sign-off before it is committed."),
]

# ---- 1. QuickBooks: book APPROVED lines to the right account ----
# staff lunch (16687) already booked as new expense 19261 in an earlier test call.
already = {"16687"}
qb_results = []
for row in LEDGER:
    lid,date,item,vendor,amt,verdict,acct_id,acct_name,reason = row
    if verdict != "APPROVE" or lid in already:
        continue
    body = {
      "AccountRef":{"value":"1","name":"Operating Checking"},
      "PaymentType":"CreditCard",
      "TxnDate":date,
      "Line":[{"Amount":amt,"DetailType":"AccountBasedExpenseLineDetail",
               "Description":f"{item} [AUDIT: APPROVED, reclassified to {acct_name}]",
               "AccountBasedExpenseLineDetail":{"AccountRef":{"value":acct_id,"name":acct_name}}}],
      "PrivateNote":f"Winter reimbursement audit: APPROVED. Reclassification of original expense line {lid} to {acct_name} (#{acct_id}). Original uncategorized line to be voided by Diane to avoid double-count."
    }
    res = post(QB + "/purchase", body)
    newid = res.get("Purchase",{}).get("Id")
    qb_results.append((lid, item, amt, acct_name, newid))
    print(f"QB booked APPROVED line {lid} ({item[:30]}) -> {acct_name} as new Purchase {newid}")

# ---- 2. Airtable ops base: mirror every verdict as a Task under the audit project ----
proj = "Winter Staff Expense Reimbursement Audit (2026 batch)"
recs = []
order = {"HOLD":0,"REJECT":1,"APPROVE":2}
for row in sorted(LEDGER, key=lambda r: (order[r[5]], r[1])):
    lid,date,item,vendor,amt,verdict,acct_id,acct_name,reason = row
    tag = "NEEDS HUMAN" if verdict=="HOLD" else verdict
    dest = f" -> {acct_name}" if acct_name else ""
    name = f"[{tag}] {item} ${amt:.2f}{dest} | {reason}"
    recs.append({"fields":{"Name":name[:900],"Status":("In progress" if verdict=="HOLD" else "Done"),
                            "Project":proj}})
# create in batches of 10
for i in range(0,len(recs),10):
    res = post(A + "/tblTasks00000001", {"records":recs[i:i+10]})
    print("Airtable created", len(res.get("records",[])), "decision records")

print("\nDONE writes.")
