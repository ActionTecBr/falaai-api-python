"""Teste de CONTRATO/COBERTURA — garante que o SDK cobre 100% das operacoes do /openapi.json
e que os exemplos de uso (fonte unica) existem para os endpoints de IA (sincronia)."""
import json
from pathlib import Path

from falaai_api.api import speech, analysis, usage, webhooks, email_alerts, health, version

_API_ROOT = Path(__file__).resolve().parents[4]  # sdks/python/tests/e2e -> FalaAI_api
_SPEC = _API_ROOT / "openapi.json"
_EXAMPLES = _API_ROOT / "app" / "static" / "examples"

# (metodo, rota) -> funcao do SDK gerado
OP_TO_SDK = {
    ("POST", "/v1/audio/transcriptions"): (speech, "create_transcription_v1_audio_transcriptions_post"),
    ("POST", "/v1/analyze/diagnostic"): (analysis, "create_diagnostic_v1_analyze_diagnostic_post"),
    ("POST", "/v1/analyze/auditoriaRisco"): (analysis, "create_auditoria_risco_v_1_analyze_auditoria_risco_post"),
    ("GET", "/v1/usage/log"): (usage, "get_usage_log_v1_usage_log_get"),
    ("GET", "/v1/usage/by-key"): (usage, "get_usage_by_key_v1_usage_by_key_get"),
    ("GET", "/v1/webhooks"): (webhooks, "list_webhooks_v1_webhooks_get"),
    ("POST", "/v1/webhooks"): (webhooks, "create_webhook_v1_webhooks_post"),
    ("PUT", "/v1/webhooks/{webhook_id}"): (webhooks, "update_webhook_v1_webhooks_webhook_id_put"),
    ("DELETE", "/v1/webhooks/{webhook_id}"): (webhooks, "delete_webhook_v1_webhooks_webhook_id_delete"),
    ("GET", "/v1/email-alerts"): (email_alerts, "list_email_alerts_v1_email_alerts_get"),
    ("POST", "/v1/email-alerts"): (email_alerts, "create_email_alert_v1_email_alerts_post"),
    ("PUT", "/v1/email-alerts/{alert_id}"): (email_alerts, "update_email_alert_v1_email_alerts_alert_id_put"),
    ("DELETE", "/v1/email-alerts/{alert_id}"): (email_alerts, "delete_email_alert_v1_email_alerts_alert_id_delete"),
    ("GET", "/api/version"): (version, "get_version_api_version_get"),
    ("GET", "/v1/health"): (health, "health_check"),
    ("HEAD", "/v1/health"): (health, "health_check_head"),
}

_EXAMPLES_AI = {
    "transcribe": ["curl/transcribe.sh", "python/transcribe.py", "nodejs/transcribe.js"],
    "diagnostic": ["curl/diagnostic.sh", "python/diagnostic.py", "nodejs/diagnostic.js"],
    "auditoria_risco": ["curl/auditoria_risco.sh", "python/auditoria_risco.py", "nodejs/auditoria_risco.js"],
}


def test_openapi_tem_exatamente_as_operacoes_esperadas():
    assert _SPEC.exists(), f"openapi.json ausente: {_SPEC}"
    spec = json.loads(_SPEC.read_text(encoding="utf-8"))
    ops = set()
    for path, methods in spec["paths"].items():
        for m in methods:
            if m in ("get", "post", "put", "delete", "patch", "head"):
                ops.add((m.upper(), path))
    assert ops == set(OP_TO_SDK.keys()), f"divergencia: {ops ^ set(OP_TO_SDK.keys())}"


def test_sdk_cobre_100pc_das_operacoes():
    faltando = []
    for (method, path), (mod, fn) in OP_TO_SDK.items():
        if not hasattr(mod, fn):
            faltando.append(f"{method} {path} -> {mod.__name__}.{fn}")
    assert not faltando, "SDK nao cobre: " + "; ".join(faltando)


def test_exemplos_de_uso_existem():
    faltando = []
    for name, files in _EXAMPLES_AI.items():
        for rel in files:
            if not (_EXAMPLES / rel).exists():
                faltando.append(rel)
    assert not faltando, "exemplos ausentes: " + "; ".join(faltando)