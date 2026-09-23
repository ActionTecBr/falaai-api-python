from falaai_api.api.health import health_check, health_check_head
from falaai_api.api.version import get_version_api_version_get
from falaai_api.api.usage import get_usage_log_v1_usage_log_get, get_usage_by_key_v1_usage_by_key_get
from falaai_api.api.webhooks import list_webhooks_v1_webhooks_get
from falaai_api.api.email_alerts import list_email_alerts_v1_email_alerts_get
from tests.e2e.e2e_logger import log_test


def test_health_get(client):
    r = health_check.sync_detailed(client=client)
    log_test("health_get", "GET", "/v1/health", None, r.parsed, f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 200
    p = r.parsed
    assert p.status == "ok"
    assert isinstance(p.version, str) and p.version
    assert isinstance(p.uptime_seconds, int) and p.uptime_seconds >= 0
    assert isinstance(p.database, bool)
    assert isinstance(p.phase, str) and p.phase
    assert isinstance(p.launch_date, str) and p.launch_date


def test_health_head(base_url):
    import httpx
    r = httpx.head(f"{base_url}/v1/health", timeout=15)
    log_test("health_head", "HEAD", "/v1/health", None, {"status_code": r.status_code}, f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 200


def test_version(client):
    r = get_version_api_version_get.sync_detailed(client=client)
    log_test("version", "GET", "/api/version", None, r.parsed, f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 200
    p = r.parsed
    assert p.service == "FalaAI API"
    assert isinstance(p.version, str) and p.version
    assert isinstance(p.deploy_date, str) and p.deploy_date


def test_usage_log(auth):
    r = get_usage_log_v1_usage_log_get.sync_detailed(client=auth, page=1, limit=5)
    log_test("usage_log", "GET", "/v1/usage/log", {"page": 1, "limit": 5}, r.parsed, f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 200
    p = r.parsed
    assert p.page == 1 and p.limit == 5
    assert isinstance(p.data, list)
    for it in p.data:
        assert isinstance(it.id, str) and it.id
        assert isinstance(it.endpoint, str) and it.endpoint
        assert isinstance(it.credits_cost, int)
        assert isinstance(it.status, str) and it.status
        assert isinstance(it.errors_count, int)
        assert isinstance(it.created_at, str) and it.created_at


def test_usage_by_key(auth):
    r = get_usage_by_key_v1_usage_by_key_get.sync_detailed(client=auth)
    log_test("usage_by_key", "GET", "/v1/usage/by-key", None, r.parsed, f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 200
    for it in r.parsed:
        assert isinstance(it.key_id, str) and it.key_id
        assert isinstance(it.key_name, str)
        assert isinstance(it.total_credits, int)
        assert isinstance(it.request_count, int)


def test_webhooks_list(auth):
    r = list_webhooks_v1_webhooks_get.sync_detailed(client=auth, page=1, limit=5)
    log_test("webhooks_list", "GET", "/v1/webhooks", {"page": 1, "limit": 5}, r.parsed, f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 200
    p = r.parsed
    assert p.page == 1 and p.limit == 5
    for w in p.data:
        assert isinstance(w.id, str) and w.id
        assert isinstance(w.user_id, str) and w.user_id
        assert isinstance(w.name, str)
        assert isinstance(w.url, str) and w.url
        assert isinstance(w.secret, str)
        assert isinstance(w.events, list)
        assert isinstance(w.active, bool)
        assert isinstance(w.retry_enabled, bool)
        assert isinstance(w.failure_count, int)
        assert isinstance(w.created_at, str) and w.created_at
        assert isinstance(w.updated_at, str) and w.updated_at


def test_email_alerts_list(auth):
    r = list_email_alerts_v1_email_alerts_get.sync_detailed(client=auth, page=1, limit=5)
    log_test("email_alerts_list", "GET", "/v1/email-alerts", {"page": 1, "limit": 5}, r.parsed, f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 200
    p = r.parsed
    assert p.page == 1 and p.limit == 5
    for a in p.data:
        assert isinstance(a.id, str) and a.id
        assert isinstance(a.user_id, str) and a.user_id
        assert isinstance(a.name, str)
        assert isinstance(a.email, str) and a.email
        assert isinstance(a.events, list)
        assert isinstance(a.active, bool)
        assert isinstance(a.created_at, str) and a.created_at
        assert isinstance(a.updated_at, str) and a.updated_at