"""Testes de ERRO — cobre 401 (auth), 422 (validacao) e 400 (valor invalido) dos endpoints.
Usa httpx cru (para enviar payloads invalidos que os models tipados nao permitem).
Loga payload -> resposta -> resultado (mesmo padrao do resto da suite)."""
from tests.e2e import conftest as cfg
from tests.e2e.e2e_logger import log_test


def _body(r):
    try:
        return r.json()
    except Exception:
        return r.text


def _httpx(client):
    return client.rest_client


def test_401_invalid_key(auth):
    bad = cfg.make_client(cfg.BASE, "fai_chave_invalida_000")
    r = _httpx(bad).request("GET", "/v1/usage/log", query_params={"page": 1, "limit": 1})
    log_test("errors_401", "GET", "/v1/usage/log", None, _body(r), f"HTTP {r.status}", r.status)
    assert r.status == 401, r.text[:200]


def test_422_diagnostic_missing_required(auth):
    body = {"language": "pt-BR", "dialog": "Speaker 1: ola"}
    r = _httpx(auth).request("POST", "/v1/analyze/diagnostic", body=body)
    log_test("errors_422_diag", "POST", "/v1/analyze/diagnostic", body, _body(r), f"HTTP {r.status}", r.status)
    assert r.status == 422, r.text[:200]


def test_422_risk_audit_missing_required(auth):
    body = {"language": "pt-BR", "dialog": "Speaker 1: ola"}
    r = _httpx(auth).request("POST", "/v1/analyze/riskAudit", body=body)
    log_test("errors_422_aud", "POST", "/v1/analyze/riskAudit", body, _body(r), f"HTTP {r.status}", r.status)
    assert r.status == 422, r.text[:200]


def test_422_risk_audit_extra_forbidden(auth):
    body = {"dialog": "Speaker 1: ola", "language": "pt-BR", "response_language": "pt-BR",
            "duration_seconds": 10.0, "threshold_multiplier": 1.0}
    r = _httpx(auth).request("POST", "/v1/analyze/riskAudit", body=body)
    log_test("errors_422_extra", "POST", "/v1/analyze/riskAudit", body, _body(r), f"HTTP {r.status}", r.status)
    assert r.status == 422, r.text[:200]


def test_400_risk_audit_invalid_language(auth):
    body = {"dialog": "Speaker 1: ola", "language": "xx", "response_language": "pt-BR", "duration_seconds": 10.0}
    r = _httpx(auth).request("POST", "/v1/analyze/riskAudit", body=body)
    log_test("errors_400_aud", "POST", "/v1/analyze/riskAudit", body, _body(r), f"HTTP {r.status}", r.status)
    assert r.status == 400, r.text[:200]


def test_400_diagnostic_invalid_language(auth):
    body = {"dialog": "Speaker 1: ola", "language": "xx", "duration_seconds": 10.0}
    r = _httpx(auth).request("POST", "/v1/analyze/diagnostic", body=body)
    log_test("errors_400_diag", "POST", "/v1/analyze/diagnostic", body, _body(r), f"HTTP {r.status}", r.status)
    assert r.status == 400, r.text[:200]