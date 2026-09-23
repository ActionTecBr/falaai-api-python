"""Testes de ERRO — cobre 401 (auth), 422 (validacao) e 400 (valor invalido) dos endpoints.
Usa httpx cru (para enviar payloads invalidos que os models tipados nao permitem).
Loga payload -> resposta -> resultado (mesmo padrao do resto da suite)."""
from falaai_api import AuthenticatedClient
from tests.e2e import conftest as cfg
from tests.e2e.e2e_logger import log_test


def _body(r):
    try:
        return r.json()
    except Exception:
        return r.text


def test_401_invalid_key(auth):
    bad = AuthenticatedClient(base_url=cfg.BASE, token="fai_chave_invalida_000")
    r = bad.get_httpx_client().get("/v1/usage/log", params={"page": 1, "limit": 1})
    log_test("errors_401", "GET", "/v1/usage/log", None, _body(r), f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 401, r.text[:200]


def test_422_diagnostic_missing_required(auth):
    body = {"language": "pt-BR", "dialog": "Speaker 1: ola"}
    r = auth.get_httpx_client().post("/v1/analyze/diagnostic", json=body)
    log_test("errors_422_diag", "POST", "/v1/analyze/diagnostic", body, _body(r), f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 422, r.text[:200]


def test_422_auditoria_missing_required(auth):
    body = {"language": "pt-BR", "dialog": "Speaker 1: ola"}
    r = auth.get_httpx_client().post("/v1/analyze/auditoriaRisco", json=body)
    log_test("errors_422_aud", "POST", "/v1/analyze/auditoriaRisco", body, _body(r), f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 422, r.text[:200]


def test_422_auditoria_extra_forbidden(auth):
    body = {"dialog": "Speaker 1: ola", "language": "pt-BR", "response_language": "pt-BR",
            "duration_seconds": 10.0, "threshold_multiplier": 1.0}
    r = auth.get_httpx_client().post("/v1/analyze/auditoriaRisco", json=body)
    log_test("errors_422_extra", "POST", "/v1/analyze/auditoriaRisco", body, _body(r), f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 422, r.text[:200]


def test_400_auditoria_invalid_language(auth):
    body = {"dialog": "Speaker 1: ola", "language": "xx", "response_language": "pt-BR", "duration_seconds": 10.0}
    r = auth.get_httpx_client().post("/v1/analyze/auditoriaRisco", json=body)
    log_test("errors_400_aud", "POST", "/v1/analyze/auditoriaRisco", body, _body(r), f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 400, r.text[:200]


def test_400_diagnostic_invalid_language(auth):
    body = {"dialog": "Speaker 1: ola", "language": "xx", "duration_seconds": 10.0}
    r = auth.get_httpx_client().post("/v1/analyze/diagnostic", json=body)
    log_test("errors_400_diag", "POST", "/v1/analyze/diagnostic", body, _body(r), f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 400, r.text[:200]