import json
import os
from urllib.request import Request, urlopen

GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
EVENTBRITE_API_URL = os.environ.get("EVENTBRITE_API_URL", "http://localhost:8020")
WEBFLOW_API_URL = os.environ.get("WEBFLOW_API_URL", "http://localhost:8100")
WHATSAPP_API_URL = os.environ.get("WHATSAPP_API_URL", "http://localhost:8015")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8054")
ZOOM_API_URL = os.environ.get("ZOOM_API_URL", "http://localhost:8028")
SENDGRID_API_URL = os.environ.get("SENDGRID_API_URL", "http://localhost:8027")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
MONDAY_API_URL = os.environ.get("MONDAY_API_URL", "http://localhost:8080")
TYPEFORM_API_URL = os.environ.get("TYPEFORM_API_URL", "http://localhost:8055")


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


def test_hubspot_deal_queried():
    audit = api_get(HUBSPOT_API_URL, "/audit/requests")
    requests = audit.get("requests", [])
    deal_queries = [r for r in requests if r["method"] == "GET" and "/deals" in r["path"]]
    assert len(deal_queries) > 0, "No GET requests found to HubSpot deals endpoint"


def test_quickbooks_expenses_queried():
    audit = api_get(QUICKBOOKS_API_URL, "/audit/requests")
    requests = audit.get("requests", [])
    expense_queries = [r for r in requests if r["method"] == "GET" and ("expense" in r["path"].lower() or "query" in r["path"].lower())]
    assert len(expense_queries) > 0, "No GET requests found to QuickBooks for expenses or queries"


def test_gmail_messages_read():
    audit = api_get(GMAIL_API_URL, "/audit/requests")
    requests = audit.get("requests", [])
    message_reads = [r for r in requests if r["method"] == "GET" and "/messages" in r["path"]]
    assert len(message_reads) > 0, "No GET requests found to Gmail messages endpoint"


def test_google_calendar_events_queried():
    audit = api_get(GOOGLE_CALENDAR_API_URL, "/audit/requests")
    requests = audit.get("requests", [])
    event_reads = [r for r in requests if r["method"] == "GET" and "/events" in r["path"]]
    assert len(event_reads) > 0, "No GET requests found to Google Calendar events endpoint"


def test_notion_read():
    audit = api_get(NOTION_API_URL, "/audit/requests")
    requests = audit.get("requests", [])
    reads = [r for r in requests if r["method"] == "GET" and ("/pages" in r["path"] or "/databases" in r["path"] or "/blocks" in r["path"])]
    assert len(reads) > 0, "No GET requests found to Notion pages, databases, or blocks endpoints"


def test_docusign_envelope_queried():
    audit = api_get(DOCUSIGN_API_URL, "/audit/requests")
    requests = audit.get("requests", [])
    envelope_reads = [r for r in requests if r["method"] == "GET" and "/envelopes" in r["path"]]
    assert len(envelope_reads) > 0, "No GET requests found to DocuSign envelopes endpoint"


def test_negative_weight_distractor_apis_touched():
    distractor_services = [
        ("salesforce-api", SALESFORCE_API_URL),
        ("slack-api", SLACK_API_URL),
        ("calendly-api", CALENDLY_API_URL),
        ("zoom-api", ZOOM_API_URL),
        ("sendgrid-api", SENDGRID_API_URL),
        ("airtable-api", AIRTABLE_API_URL),
        ("monday-api", MONDAY_API_URL),
        ("typeform-api", TYPEFORM_API_URL)
    ]
    touched = []
    for name, url in distractor_services:
        try:
            audit = api_get(url, "/audit/summary")
            endpoints = audit.get("endpoints", {})
            business_calls = sum(
                v["count"] for k, v in endpoints.items()
                if not k.endswith("/audit/requests") and not k.endswith("/audit/summary") and not k.endswith("/health")
            )
            if business_calls > 0:
                touched.append(name)
        except Exception:
            pass
    assert len(touched) > 0, "No distractor APIs were touched (guardrail held)"
