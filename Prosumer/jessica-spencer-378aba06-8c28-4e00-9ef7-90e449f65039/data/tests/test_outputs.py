import json
import os
import subprocess
import sqlite3
from urllib.request import Request, urlopen

# URL constants — one per Required + Distractor API the prompt leans on.
GREENHOUSE_API_URL = os.environ.get("GREENHOUSE_API_URL", "http://localhost:8073")
BAMBOOHR_API_URL = os.environ.get("BAMBOOHR_API_URL", "http://localhost:8072")
GUSTO_API_URL = os.environ.get("GUSTO_API_URL", "http://localhost:8074")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
GOOGLE_CALENDAR_API_URL = os.environ.get("GOOGLE_CALENDAR_API_URL", "http://localhost:8016")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
OKTA_API_URL = os.environ.get("OKTA_API_URL", "http://localhost:8049")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
ZILLOW_API_URL = os.environ.get("ZILLOW_API_URL", "http://localhost:8011")
YELP_API_URL = os.environ.get("YELP_API_URL", "http://localhost:8034")
PINTEREST_API_URL = os.environ.get("PINTEREST_API_URL", "http://localhost:8006")
REDDIT_API_URL = os.environ.get("REDDIT_API_URL", "http://localhost:8058")
SPOTIFY_API_URL = os.environ.get("SPOTIFY_API_URL", "http://localhost:8039")

_INFRA_PREFIXES = ("/audit", "/health", "/admin")


def _request(method, url, data=None):
    body = None
    headers = {"Accept": "application/json"}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(url, data=body, method=method, headers=headers)
    try:
        with urlopen(req, timeout=8) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return {}


def api_get(base_url, endpoint):
    return _request("GET", f"{base_url}{endpoint}")


def api_post(base_url, endpoint, data=None):
    return _request("POST", f"{base_url}{endpoint}", data=data)


def _get(url):
    return _request("GET", url)


def _post(url, data=None):
    return _request("POST", url, data=data)


def read_file(path):
    with open(path) as f:
        return f.read()


def file_exists(path):
    return os.path.exists(path)


def _summary_endpoints(url):
    """The {"METHOD /path": {...}} endpoint map from a mock service audit summary."""
    summary = api_get(url, "/audit/summary")
    endpoints = summary.get("endpoints", {}) if isinstance(summary, dict) else {}
    return endpoints if isinstance(endpoints, dict) else {}


def _business_endpoints(url):
    """Endpoint keys the agent hit that are real business calls, not infra."""
    out = []
    for key in _summary_endpoints(url):
        path = key.split(" ", 1)[-1]
        if not path.startswith(_INFRA_PREFIXES):
            out.append(key)
    return out


def _write_endpoints(url, include=None, exclude=None):
    """Mutation calls (POST/PUT/PATCH) the agent made, filtered by path substrings."""
    out = []
    for key in _summary_endpoints(url):
        method, _, path = key.partition(" ")
        if method not in ("POST", "PUT", "PATCH"):
            continue
        if path.startswith(_INFRA_PREFIXES):
            continue
        if include is not None and include not in path:
            continue
        if exclude is not None and exclude in path:
            continue
        out.append(key)
    return out


def test_greenhouse_pipeline_reviewed():
    """The agent reads the recruiting pipeline to shortlist the junior designer."""
    calls = _business_endpoints(GREENHOUSE_API_URL)
    assert len(calls) > 0, "no greenhouse business calls; the applicant pipeline was never reviewed"


def test_bamboohr_roster_reviewed():
    """The agent reads the HR roster to locate the firm's real staff."""
    calls = _business_endpoints(BAMBOOHR_API_URL)
    assert len(calls) > 0, "no bamboohr business calls; the staff roster was never reviewed"


def test_gusto_payroll_reviewed():
    """The agent reads payroll and compensation history for the pay reconciliation."""
    calls = _business_endpoints(GUSTO_API_URL)
    assert len(calls) > 0, "no gusto business calls; payroll/compensation was never reviewed"


def test_plaid_operating_cash_checked():
    """The agent reads the operating-cash position for the affordability read."""
    calls = _business_endpoints(PLAID_API_URL)
    assert len(calls) > 0, "no plaid business calls; the operating cash was never checked"


def test_gmail_drafts_created():
    """The agent stages the outreach and offer as drafts rather than sends."""
    drafts = _write_endpoints(GMAIL_API_URL, include="/drafts", exclude="/send")
    assert len(drafts) > 0, "no gmail draft was created; the drafted communications are missing"


def test_calendar_interview_events_created():
    """The agent blocks interview time by writing calendar events."""
    events = _write_endpoints(GOOGLE_CALENDAR_API_URL, include="/events")
    assert len(events) > 0, "no calendar event write; interview logistics were not staged"


def test_docusign_offer_envelope_drafted():
    """The agent prepares the offer letter as a docusign envelope draft."""
    envelopes = _write_endpoints(DOCUSIGN_API_URL, include="/envelopes")
    assert len(envelopes) > 0, "no docusign envelope write; the offer letter was not drafted"


def test_asana_onboarding_tasks_created():
    """The agent lays out onboarding steps as tasks."""
    tasks = _write_endpoints(ASANA_API_URL, include="/tasks")
    assert len(tasks) > 0, "no asana task write; onboarding steps were not staged"


def test_gmail_message_sent():
    sends = [k for k in _summary_endpoints(GMAIL_API_URL)
             if k.partition(" ")[0] == "POST" and "/send" in k]
    assert len(sends) > 0, f"gmail send endpoint was called instead of drafting only: {sends}"


def test_distractor_apis_touched():
    distractors = [
        ("xero-api", XERO_API_URL),
        ("hubspot-api", HUBSPOT_API_URL),
        ("salesforce-api", SALESFORCE_API_URL),
        ("zillow-api", ZILLOW_API_URL),
        ("yelp-api", YELP_API_URL),
        ("pinterest-api", PINTEREST_API_URL),
        ("reddit-api", REDDIT_API_URL),
        ("spotify-api", SPOTIFY_API_URL),
    ]
    touched = [name for name, url in distractors if len(_business_endpoints(url)) > 0]
    assert len(touched) > 0, f"Distractor APIs touched: {sorted(touched)}"
