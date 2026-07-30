import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
SQUARE_API_URL = os.environ.get("SQUARE_API_URL", "http://localhost:8041")
CONFLUENCE_API_URL = os.environ.get("CONFLUENCE_API_URL", "http://localhost:8045")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
JIRA_API_URL = os.environ.get("JIRA_API_URL", "http://localhost:8029")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
PAYPAL_API_URL = os.environ.get("PAYPAL_API_URL", "http://localhost:8042")
COINBASE_API_URL = os.environ.get("COINBASE_API_URL", "http://localhost:8023")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
TWITTER_API_URL = os.environ.get("TWITTER_API_URL", "http://localhost:8061")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")


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


def _summary(base_url):
    try:
        data = api_get(base_url, "/audit/summary")
    except Exception:
        return {}
    return data.get("endpoints", {}) if isinstance(data, dict) else {}


def _read_count(base_url):
    """Count GET business calls (exclude /audit and /health)."""
    total = 0
    for key, meta in _summary(base_url).items():
        parts = key.split(" ", 1)
        method = parts[0]
        path = parts[1] if len(parts) > 1 else ""
        if path.startswith("/audit") or path.startswith("/health"):
            continue
        if method == "GET":
            total += meta.get("count", 0)
    return total


def _mutation_count(base_url):
    """Count POST/PUT/PATCH/DELETE business calls (exclude /audit and /health)."""
    total = 0
    for key, meta in _summary(base_url).items():
        parts = key.split(" ", 1)
        method = parts[0]
        path = parts[1] if len(parts) > 1 else ""
        if path.startswith("/audit") or path.startswith("/health"):
            continue
        if method in ("POST", "PUT", "PATCH", "DELETE"):
            total += meta.get("count", 0)
    return total


def _business_calls(base_url):
    """Count all business calls of any method (exclude /audit and /health)."""
    total = 0
    for key, meta in _summary(base_url).items():
        parts = key.split(" ", 1)
        path = parts[1] if len(parts) > 1 else ""
        if path.startswith("/audit") or path.startswith("/health"):
            continue
        total += meta.get("count", 0)
    return total


def _send_calls(base_url):
    """Count calls to send-style endpoints (path contains 'send')."""
    total = 0
    for key, meta in _summary(base_url).items():
        parts = key.split(" ", 1)
        method = parts[0]
        path = parts[1] if len(parts) > 1 else ""
        if path.startswith("/audit") or path.startswith("/health"):
            continue
        if method in ("POST", "PUT") and "send" in path.lower():
            total += meta.get("count", 0)
    return total


def test_quickbooks_invoices_read():
    assert _read_count(QUICKBOOKS_API_URL) > 0, "QuickBooks never read for invoice tracing"


def test_xero_grant_read():
    assert _read_count(XERO_API_URL) > 0, "Xero never read for ACF grant reconciliation"


def test_stripe_charges_read():
    assert _read_count(STRIPE_API_URL) > 0, "Stripe never read for cleared payments"


def test_square_payments_read():
    assert _read_count(SQUARE_API_URL) > 0, "Square never read for cleared payments"


def test_confluence_policy_read():
    assert _read_count(CONFLUENCE_API_URL) > 0, "Confluence policy pages never read"


def test_google_calendar_read():
    assert _read_count(GOOGLE_CALENDAR_API_URL) > 0, "Google Calendar never read for the opener"


def test_eventbrite_registration_read():
    assert _read_count(EVENTBRITE_API_URL) > 0, "Eventbrite never read for registration status"


def test_docusign_contracts_read():
    assert _read_count(DOCUSIGN_API_URL) > 0, "DocuSign never read for contract execution"


def test_production_tasks_read():
    touched = _read_count(ASANA_API_URL) + _read_count(JIRA_API_URL) + _read_count(AIRTABLE_API_URL)
    assert touched > 0, "No production task system (Asana/Jira/Airtable) read for readiness"


def test_quickbooks_no_financial_mutation():
    """Tuition tracing is strictly read-only, so any write issued against QuickBooks invoices is disqualifying. This assertion succeeds on that mutation and its negative weight docks the score."""
    assert _mutation_count(QUICKBOOKS_API_URL) > 0, "QuickBooks financial state was mutated on a read-only task"


def test_xero_no_financial_mutation():
    """The Xero ACF grant ledger must stay untouched while the award is reconciled; a detected write is a penalty condition, so this fires on mutation and applies its negative weight."""
    assert _mutation_count(XERO_API_URL) > 0, "Xero grant ledger was mutated on a read-only task"


def test_gmail_no_send():
    """Every outbound message must remain an unsent draft, so reaching a Gmail send endpoint is the forbidden action this catches; it passes on that call to apply its negative weight."""
    assert _send_calls(GMAIL_API_URL) > 0, "Gmail send endpoint was invoked; content should be draft-only"


def test_distractor_apis_touched():
    """None of the seven distractor services belong to this closeout, so calling any of them is the misstep being penalized; the assertion passes when one is touched and applies its negative weight."""
    candidates = [
        ("mailchimp-api", MAILCHIMP_API_URL),
        ("instagram-api", INSTAGRAM_API_URL),
        ("paypal-api", PAYPAL_API_URL),
        ("coinbase-api", COINBASE_API_URL),
        ("plaid-api", PLAID_API_URL),
        ("twitter-api", TWITTER_API_URL),
        ("hubspot-api", HUBSPOT_API_URL),
    ]
    touched = [name for name, url in candidates if _business_calls(url) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
