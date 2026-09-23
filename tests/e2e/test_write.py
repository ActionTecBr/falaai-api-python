from falaai_api.api.webhooks import (
    list_webhooks_v1_webhooks_get, create_webhook_v1_webhooks_post,
    update_webhook_v1_webhooks_webhook_id_put, delete_webhook_v1_webhooks_webhook_id_delete,
)
from falaai_api.api.email_alerts import (
    list_email_alerts_v1_email_alerts_get, create_email_alert_v1_email_alerts_post,
    update_email_alert_v1_email_alerts_alert_id_put, delete_email_alert_v1_email_alerts_alert_id_delete,
)
from falaai_api.models.create_webhook_request import CreateWebhookRequest
from falaai_api.models.update_webhook_request import UpdateWebhookRequest
from falaai_api.models.create_email_alert_request import CreateEmailAlertRequest
from falaai_api.models.update_email_alert_request import UpdateEmailAlertRequest
from falaai_api.models.webhook_event import WebhookEvent
from falaai_api.models.email_event import EmailEvent
from tests.e2e.e2e_logger import log_test

WURL = "https://e2e-falaai.invalid/hook"
WNAME = "E2E Test Webhook"
ANAME = "E2E Test Alert"
AEMAIL = "e2e-test@falaai.invalid"
EVENTS_W = [WebhookEvent.CREDITS_LOW, WebhookEvent.PAYMENT_FAILED]
EVENTS_A = [EmailEvent.CREDITS_LOW, EmailEvent.PAYMENT_FAILED]


def _assert_webhook_full(w, wid, name, active):
    assert w.id == wid
    assert isinstance(w.user_id, str) and w.user_id
    assert w.name == name
    assert w.url == WURL
    assert isinstance(w.secret, str) and w.secret
    assert isinstance(w.events, list) and len(w.events) == 2
    assert w.active is active
    assert isinstance(w.retry_enabled, bool)
    assert isinstance(w.failure_count, int)
    assert isinstance(w.created_at, str) and w.created_at
    assert isinstance(w.updated_at, str) and w.updated_at


def _assert_alert_full(a, aid, name, active):
    assert a.id == aid
    assert isinstance(a.user_id, str) and a.user_id
    assert a.name == name
    assert a.email == AEMAIL
    assert isinstance(a.events, list) and len(a.events) == 2
    assert a.active is active
    assert isinstance(a.created_at, str) and a.created_at
    assert isinstance(a.updated_at, str) and a.updated_at


def _cleanup_webhooks(auth):
    r = list_webhooks_v1_webhooks_get.sync(client=auth, page=1, limit=100)
    for w in (r.data if r else []):
        if w.url == WURL:
            delete_webhook_v1_webhooks_webhook_id_delete.sync_detailed(client=auth, webhook_id=w.id)


def _cleanup_alerts(auth):
    r = list_email_alerts_v1_email_alerts_get.sync(client=auth, page=1, limit=100)
    for a in (r.data if r else []):
        if a.email == AEMAIL:
            delete_email_alert_v1_email_alerts_alert_id_delete.sync_detailed(client=auth, alert_id=a.id)


def test_webhooks_crud(auth):
    _cleanup_webhooks(auth)

    body = CreateWebhookRequest(name=WNAME, url=WURL, events=EVENTS_W)
    c = create_webhook_v1_webhooks_post.sync_detailed(client=auth, body=body)
    log_test("webhooks_create", "POST", "/v1/webhooks", body, c.parsed, f"HTTP {c.status_code}", c.status_code)
    assert c.status_code == 200, c.content[:300]
    wid = c.parsed.id
    _assert_webhook_full(c.parsed, wid, WNAME, True)

    ub = UpdateWebhookRequest(name=WNAME + " (updated)", active=False)
    u = update_webhook_v1_webhooks_webhook_id_put.sync_detailed(client=auth, webhook_id=wid, body=ub)
    log_test("webhooks_update", "PUT", f"/v1/webhooks/{wid}", ub, u.parsed, f"HTTP {u.status_code}", u.status_code)
    assert u.status_code == 200, u.content[:300]
    assert u.parsed.message == "updated"

    r = list_webhooks_v1_webhooks_get.sync(client=auth, page=1, limit=100)
    row = next((w for w in r.data if w.id == wid), None)
    assert row is not None
    _assert_webhook_full(row, wid, WNAME + " (updated)", False)

    d = delete_webhook_v1_webhooks_webhook_id_delete.sync_detailed(client=auth, webhook_id=wid)
    log_test("webhooks_delete", "DELETE", f"/v1/webhooks/{wid}", None, d.parsed, f"HTTP {d.status_code}", d.status_code)
    assert d.status_code == 200, d.content[:300]
    assert d.parsed.message == "deleted"

    r2 = list_webhooks_v1_webhooks_get.sync(client=auth, page=1, limit=100)
    assert next((w for w in r2.data if w.id == wid), None) is None


def test_email_alerts_crud(auth):
    _cleanup_alerts(auth)

    body = CreateEmailAlertRequest(name=ANAME, email=AEMAIL, events=EVENTS_A)
    c = create_email_alert_v1_email_alerts_post.sync_detailed(client=auth, body=body)
    log_test("email_alerts_create", "POST", "/v1/email-alerts", body, c.parsed, f"HTTP {c.status_code}", c.status_code)
    assert c.status_code == 200, c.content[:300]
    aid = c.parsed.id
    _assert_alert_full(c.parsed, aid, ANAME, True)

    ub = UpdateEmailAlertRequest(name=ANAME + " (updated)", active=False)
    u = update_email_alert_v1_email_alerts_alert_id_put.sync_detailed(client=auth, alert_id=aid, body=ub)
    log_test("email_alerts_update", "PUT", f"/v1/email-alerts/{aid}", ub, u.parsed, f"HTTP {u.status_code}", u.status_code)
    assert u.status_code == 200, u.content[:300]
    assert u.parsed.message == "updated"

    r = list_email_alerts_v1_email_alerts_get.sync(client=auth, page=1, limit=100)
    row = next((a for a in r.data if a.id == aid), None)
    assert row is not None
    _assert_alert_full(row, aid, ANAME + " (updated)", False)

    d = delete_email_alert_v1_email_alerts_alert_id_delete.sync_detailed(client=auth, alert_id=aid)
    log_test("email_alerts_delete", "DELETE", f"/v1/email-alerts/{aid}", None, d.parsed, f"HTTP {d.status_code}", d.status_code)
    assert d.status_code == 200, d.content[:300]
    assert d.parsed.message == "deleted"

    r2 = list_email_alerts_v1_email_alerts_get.sync(client=auth, page=1, limit=100)
    assert next((a for a in r2.data if a.id == aid), None) is None