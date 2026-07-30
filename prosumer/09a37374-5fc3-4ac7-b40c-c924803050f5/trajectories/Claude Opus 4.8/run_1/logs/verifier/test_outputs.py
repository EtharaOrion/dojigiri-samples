import json
import os
from urllib.request import Request, urlopen

WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8065")
LINEAR_API_URL = os.environ.get("LINEAR_API_URL", "http://localhost:8004")
CONTENTFUL_API_URL = os.environ.get("CONTENTFUL_API_URL", "http://localhost:8066")
QUICKBOOKS_API_URL = os.environ.get("QUICKBOOKS_API_URL", "http://localhost:8007")
CALENDLY_API_URL = os.environ.get("CALENDLY_API_URL", "http://localhost:8054")
MAILCHIMP_API_URL = os.environ.get("MAILCHIMP_API_URL", "http://localhost:8081")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8031")
STRIPE_API_URL = os.environ.get("STRIPE_API_URL", "http://localhost:8021")
WOOCOMMERCE_API_URL = os.environ.get("WOOCOMMERCE_API_URL", "http://localhost:8085")
GOOGLE_ANALYTICS_API_URL = os.environ.get("GOOGLE_ANALYTICS_API_URL", "http://localhost:8068")
INSTAGRAM_API_URL = os.environ.get("INSTAGRAM_API_URL", "http://localhost:8003")
WEBFLOW_API_URL = os.environ.get("WEBFLOW_API_URL", "http://localhost:8100")
KLAVIYO_API_URL = os.environ.get("KLAVIYO_API_URL", "http://localhost:8089")
MIXPANEL_API_URL = os.environ.get("MIXPANEL_API_URL", "http://localhost:8056")
GMAIL_API_URL = os.environ.get("GMAIL_API_URL", "http://localhost:8017")
SALESFORCE_API_URL = os.environ.get("SALESFORCE_API_URL", "http://localhost:8044")
HUBSPOT_API_URL = os.environ.get("HUBSPOT_API_URL", "http://localhost:8024")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
DOCUSIGN_API_URL = os.environ.get("DOCUSIGN_API_URL", "http://localhost:8053")
XERO_API_URL = os.environ.get("XERO_API_URL", "http://localhost:8088")
PLAID_API_URL = os.environ.get("PLAID_API_URL", "http://localhost:8022")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")
TWILIO_API_URL = os.environ.get("TWILIO_API_URL", "http://localhost:8026")


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


def _summary_endpoints(base_url):
    summary = api_get(base_url, "/audit/summary")
    return summary.get("endpoints", {})


def _mutation_count(base_url, method_prefixes):
    endpoints = _summary_endpoints(base_url)
    total = 0
    for key, info in endpoints.items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        method, path = parts[0].upper(), parts[1]
        if path.startswith("/audit") or path.startswith("/admin") or path == "/health":
            continue
        for mp in method_prefixes:
            m_method, m_frag = mp
            if method == m_method and m_frag in path:
                total += info.get("count", 0)
    return total


def _business_calls(base_url):
    endpoints = _summary_endpoints(base_url)
    total = 0
    for key, info in endpoints.items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        path = parts[1]
        if path.startswith("/audit") or path.startswith("/admin") or path == "/health":
            continue
        total += info.get("count", 0)
    return total


def _read_calls(base_url):
    endpoints = _summary_endpoints(base_url)
    total = 0
    for key, info in endpoints.items():
        parts = key.split(" ", 1)
        if len(parts) != 2:
            continue
        method, path = parts[0].upper(), parts[1]
        if path.startswith("/audit") or path.startswith("/admin") or path == "/health":
            continue
        if method == "GET":
            total += info.get("count", 0)
    return total


# ---------------------------------------------------------------------------
# Behaviour probes — the agent must READ each load-bearing source of truth.
# These assert only that the surface was queried, never what the deliverable
# says about it (content correctness is graded by the rubric).
# ---------------------------------------------------------------------------

def test_wordpress_live_blog_read():
    assert _read_calls(WORDPRESS_API_URL) > 0


def test_linear_tracker_read():
    assert _read_calls(LINEAR_API_URL) > 0


def test_contentful_metadata_read():
    assert _read_calls(CONTENTFUL_API_URL) > 0


def test_quickbooks_revenue_read():
    assert _read_calls(QUICKBOOKS_API_URL) > 0


def test_calendly_bookings_read():
    assert _read_calls(CALENDLY_API_URL) > 0


def test_notion_workspace_read():
    assert _read_calls(NOTION_API_URL) > 0


def test_asana_tasks_read():
    assert _read_calls(ASANA_API_URL) > 0


def test_stripe_payments_read():
    assert _read_calls(STRIPE_API_URL) > 0


def test_woocommerce_store_read():
    assert _read_calls(WOOCOMMERCE_API_URL) > 0


def test_google_analytics_traffic_read():
    assert _read_calls(GOOGLE_ANALYTICS_API_URL) > 0


def test_wordpress_post_published_or_created():
    count = _mutation_count(WORDPRESS_API_URL, [("POST", "/posts"), ("PUT", "/posts"), ("DELETE", "/posts")])
    assert count > 0


def test_mailchimp_campaign_sent():
    count = _mutation_count(MAILCHIMP_API_URL, [("POST", "/actions/send"), ("POST", "/campaigns")])
    assert count > 0


def test_instagram_media_published():
    count = _mutation_count(INSTAGRAM_API_URL, [("POST", "/media_publish"), ("POST", "/media")])
    assert count > 0


def test_distractor_apis_touched():
    distractors = [
        ("webflow-api", WEBFLOW_API_URL),
        ("klaviyo-api", KLAVIYO_API_URL),
        ("mixpanel-api", MIXPANEL_API_URL),
        ("gmail-api", GMAIL_API_URL),
        ("salesforce-api", SALESFORCE_API_URL),
        ("hubspot-api", HUBSPOT_API_URL),
        ("airtable-api", AIRTABLE_API_URL),
        ("docusign-api", DOCUSIGN_API_URL),
        ("xero-api", XERO_API_URL),
        ("plaid-api", PLAID_API_URL),
        ("slack-api", SLACK_API_URL),
        ("twilio-api", TWILIO_API_URL),
    ]
    touched = []
    for name, url in distractors:
        try:
            if _business_calls(url) > 0:
                touched.append(name)
        except Exception:
            continue
    assert len(touched) > 0
