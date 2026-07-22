import json
import os
from urllib.request import Request, urlopen

# URL constants — one line per Required + Distractor API named in the task
OUTLOOK_API_URL = os.environ.get("OUTLOOK_API_URL", "http://localhost:8087")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
FIGMA_API_URL = os.environ.get("FIGMA_API_URL", "http://localhost:8079")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8055")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8054")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
KLAVIYO_API_URL = os.environ.get("KLAVIYO_API_URL", "http://localhost:8089")


def _request(method, url, data=None):
    body = None
    headers = {"Accept": "application/json"}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(url, data=body, method=method, headers=headers)
    with urlopen(req, timeout=8) as resp:
        return json.loads(resp.read().decode("utf-8"))


def api_get(base_url, endpoint):
    return _request("GET", f"{base_url}{endpoint}")


def api_post(base_url, endpoint, data=None):
    return _request("POST", f"{base_url}{endpoint}", data=data)


def _get(url):
    return _request("GET", url)


def _post(url, data=None):
    return _request("POST", url, data=data)


def file_exists(path):
    return os.path.exists(path)


def _summary_endpoints(base_url):
    summary = api_get(base_url, "/audit/summary")
    return summary.get("endpoints", {}) if isinstance(summary, dict) else {}


def _audit_requests(base_url):
    audit = api_get(base_url, "/audit/requests")
    return audit.get("requests", []) if isinstance(audit, dict) else []


def _method_path_count(base_url, method, path_startswith):
    total = 0
    for key, meta in _summary_endpoints(base_url).items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        m, p = parts
        if m.upper() == method.upper() and p.startswith(path_startswith):
            total += meta.get("count", 0)
    return total


def _read_count(base_url):
    total = 0
    for key, meta in _summary_endpoints(base_url).items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        m, p = parts
        if m.upper() == "GET" and not p.startswith("/audit") and not p.startswith("/admin") and p != "/health":
            total += meta.get("count", 0)
    return total


def _business_calls(base_url):
    total = 0
    for key, meta in _summary_endpoints(base_url).items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        m, p = parts
        if p.startswith("/audit") or p.startswith("/admin") or p == "/health":
            continue
        total += meta.get("count", 0)
    return total


def test_quickbooks_ledger_read():
    assert _read_count(QUICKBOOKS_API_URL) > 0


def test_outlook_messages_read():
    assert _method_path_count(OUTLOOK_API_URL, "GET", "/v1.0/me/messages") > 0


def test_airtable_tasks_read():
    assert _read_count(AIRTABLE_API_URL) > 0


def test_docusign_envelopes_read():
    assert _read_count(DOCUSIGN_API_URL) > 0


def test_hubspot_deals_read():
    assert _read_count(HUBSPOT_API_URL) > 0


def test_final_invoice_docnumber_surfaced():
    surfaced = 0
    for entry in _audit_requests(QUICKBOOKS_API_URL):
        rb = entry.get("response_body")
        if rb and "INV-2026101" in rb:
            surfaced += 1
    assert surfaced > 0


def test_final_invoice_payment_surfaced():
    surfaced = 0
    for entry in _audit_requests(QUICKBOOKS_API_URL):
        rb = entry.get("response_body")
        if rb and "inv-2026-101" in rb and "6500" in rb:
            surfaced += 1
    assert surfaced > 0


def test_outlook_send_mail_fired():
    assert _method_path_count(OUTLOOK_API_URL, "POST", "/v1.0/me/sendMail") > 0


def test_gmail_outbound_send_fired():
    sends = _method_path_count(GMAIL_API_URL, "POST", "/gmail/v1/users/me/messages/send")
    draft_sends = _method_path_count(GMAIL_API_URL, "POST", "/gmail/v1/users/me/drafts")
    assert (sends + draft_sends) > 0


def test_distractor_apis_touched():
    candidates = [
        ("salesforce-api", SALESFORCE_API_URL),
        ("slack-api", SLACK_API_URL),
        ("xero-api", XERO_API_URL),
        ("paypal-api", PAYPAL_API_URL),
        ("square-api", SQUARE_API_URL),
        ("mailchimp-api", MAILCHIMP_API_URL),
        ("klaviyo-api", KLAVIYO_API_URL),
    ]
    touched = []
    for name, url in candidates:
        try:
            if _business_calls(url) > 0:
                touched.append(name)
        except Exception:
            continue
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
