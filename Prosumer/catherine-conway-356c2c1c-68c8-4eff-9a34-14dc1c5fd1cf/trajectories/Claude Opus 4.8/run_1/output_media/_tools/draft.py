#!/usr/bin/env python3
import os, json, urllib.request
G = os.environ['GMAIL_API_URL'] + '/gmail/v1/users/me/drafts'

body = """Hi Diane,

I've run the winter expense batch line by line before our monthly review. Most of it is fine, but there are nine lines I need you to chase before this goes to the accountant. Splitting them into two groups.

REJECTED — these should not sit in the clinic books at all (they're my studio/art spend, not practice expenses; several also show up on my personal account):
1. Cedarbrook Artisan, watercolor pans & brushes — $236.48 (Jan 8). Studio supplies; also on my personal card Jan 7.
2. Ridgemont Fine Papers, cotton-rag sheets — $142.00 (Jan 13). Commission paper; on my personal card Jan 9.
3. Northwest Framing, Wild Botanica exhibition frames — $312.00 (Jan 24). Exhibition framing, not clinic — and the same $312 charge also appears on my personal feed dated Mar 14, so it's effectively been captured twice. Please pull it from the clinic books.
4. Cedarbrook Artisan, gouache set & ink — $198.75 (Feb 9). Studio supplies; on my personal card Feb 11.
5. Northwest Framing, custom frames for commissioned panels — $340.00 (Mar 18). My commission framing, not clinic.
These five ($1,229.23) come straight out of the clinic total. Where I paid them personally, no clinic action is needed beyond removing them; where the clinic card was used, I'll reimburse the practice.

HOLD — legitimate clinic items, but I need to sign off before they're committed (each is at or above our $250 line, or I can't tell the use):
6. Athenahealth EHR subscription — $549.00 (Jan 6). Fine in principle, but please confirm it isn't doubling the $1,200/mo Athenahealth bills already in AP.
7. Adobe Creative Cloud — $89.99 (Feb 3). Tell me whether this is the clinic/marketing seat or my portfolio one before it clears.
8. CME registration, Pacific NW Dermatology Update — $425.00 (Mar 4). Legitimate CME; just needs my sign-off over the threshold.
9. Beaverton Chamber of Commerce membership — $450.00 (Mar 25). Fine, over threshold — hold for my approval.

The four clean lines (Cascade medical waste $165, Columbia scrubs $128.40, the staff-meeting lunch $74.60, and Evergreen office supplies $210 — $578.00 total) I've approved and categorized to their proper accounts. Note: I booked the corrected, categorized versions in QuickBooks, so please void the original uncategorized entries for those four so we aren't double-counting.

One more, separate from this batch: the Henry Schein bill INV-HS-8821 ($1,298.50, still open) has the delivery discrepancy Sofia flagged — invoice says 55 boxes, she counted 50. Don't pay it until that's reconciled.

Nothing here is sent anywhere yet. Let's walk the nine at the review.

Thanks,
Catherine
"""

payload = {"to":"diane.kowalski@Greenridertech.co",
           "subject":"Winter staff-expense batch — exceptions to sort before quarter close",
           "body":body}
data = json.dumps(payload).encode()
req = urllib.request.Request(G, data=data, headers={'Content-Type':'application/json'})
with urllib.request.urlopen(req) as r:
    print(json.dumps(json.loads(r.read().decode()))[:400])
