from falaai_api import ApiClient, Configuration, SpeechApi, AnalysisApi
from falaai_api.models.diagnostic_request import DiagnosticRequest
from falaai_api.models.risk_audit_request import RiskAuditRequest
from falaai_api.models.participant import Participant
from tests.e2e import conftest as cfg
from tests.e2e.e2e_logger import log_test


def test_ai_chain():
    auth = cfg.make_client(cfg.PROD, cfg.KEY)

    with open(cfg.AUDIO, "rb") as fh:
        tr = SpeechApi(auth).create_transcription_v1_audio_transcriptions_post(
            file=fh,
            model="falaai-transcribe-1",
            language="pt",
            client_reference_id="e2e-call-2026-09-22-001",
        )
    log_test("transcriptions", "POST", "/v1/audio/transcriptions", {"file": "analise_25s.mp3", "model": "falaai-transcribe-1", "language": "pt", "client_reference_id": "e2e-call-2026-09-22-001"}, tr, "HTTP 200", 200)
    assert isinstance(tr.id, str) and tr.id
    assert tr.object
    assert isinstance(tr.model, str) and tr.model
    assert isinstance(tr.filename, str) and tr.filename
    assert isinstance(tr.processed_at, str) and tr.processed_at
    assert isinstance(tr.usage.audio_seconds, float) and tr.usage.audio_seconds > 0
    assert isinstance(tr.usage.credits_consumed, int)
    assert isinstance(tr.usage.processing_ms, int)
    assert isinstance(tr.language, str) and tr.language
    assert isinstance(tr.duration_seconds, float) and tr.duration_seconds > 0
    assert isinstance(tr.text, str) and tr.text
    assert isinstance(tr.dialog, str) and tr.dialog
    assert isinstance(tr.audio_events, list)
    for e in tr.audio_events:
        assert isinstance(e.event, str) and e.event
        assert isinstance(e.start_s, float)
        assert isinstance(e.end_s, float)
        assert isinstance(e.duration_s, float)
        assert isinstance(e.formatted_timestamp, str) and e.formatted_timestamp
    assert isinstance(tr.event_types, list)
    assert isinstance(tr.word_count, int) and tr.word_count > 0
    assert isinstance(tr.input.duration_s, float)
    assert isinstance(tr.input.original_format, str) and tr.input.original_format
    assert isinstance(tr.input.codec, str) and tr.input.codec
    assert isinstance(tr.input.sample_rate, int)
    assert isinstance(tr.input.channels, int)

    db = DiagnosticRequest(
        model="falaai-diagnostic-1",
        dialog=tr.dialog,
        language="pt-BR",
        duration_seconds=tr.duration_seconds,
        text=tr.text,
        audio_events=tr.audio_events,
        client_reference_id="e2e-diag-2026-09-22-001",
    )
    dp = AnalysisApi(auth).create_diagnostic_v1_analyze_diagnostic_post(diagnostic_request=db)
    log_test("diagnostic", "POST", "/v1/analyze/diagnostic", db, dp, "HTTP 200", 200)
    assert isinstance(dp.id, str) and dp.id
    assert isinstance(dp.response_language, str) and dp.response_language
    assert dp.object == "analysis"
    assert dp.analysis.dialogue_summary is not None
    assert dp.analysis.contact_reason is not None
    assert dp.analysis.identified_action is not None
    assert dp.analysis.identified_label is not None
    assert dp.analysis.sentiment is not None
    assert isinstance(dp.usage.characters, int)
    assert isinstance(dp.usage.credits_consumed, int)
    assert isinstance(dp.usage.processing_ms, int)

    ab = RiskAuditRequest(
        dialog=tr.dialog,
        language="pt-BR",
        response_language="pt-BR",
        duration_seconds=tr.duration_seconds,
        text=tr.text,
        audio_events=tr.audio_events,
        call_direction="inbound",
        participants=[
            Participant(interlocutor="Speaker 1", name="Mateus", role="agent"),
            Participant(interlocutor="Speaker 2", name="Cliente", role="client"),
        ],
        response_format="v2",
        client_reference_id="e2e-aud-2026-09-22-001",
    )
    a = AnalysisApi(auth).create_risk_audit_v1_analyze_risk_audit_post(risk_audit_request=ab)
    log_test("riskAudit", "POST", "/v1/analyze/riskAudit", ab, a, "HTTP 200", 200)
    pub = a.response
    assert isinstance(pub.meta.id, str) and pub.meta.id
    assert isinstance(pub.meta.usage.characters, int)
    assert isinstance(pub.meta.usage.credits_consumed, int)
    assert isinstance(pub.meta.usage.processing_ms, int)
    for bloco in ("participants", "verdict", "scores", "detections", "analysis", "timeline",
                  "audio_event_model", "categories_summary", "indexer", "summary",
                  "actions_i18n", "audit_decisions", "scoring_explanation"):
        assert getattr(pub, bloco) is not None, f"bloco ausente: {bloco}"
    assert isinstance(pub.html_report, str)