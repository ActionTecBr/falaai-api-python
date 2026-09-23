from falaai_api import AuthenticatedClient
from falaai_api.types import File
from falaai_api.api.speech import create_transcription_v1_audio_transcriptions_post
from falaai_api.api.analysis import create_diagnostic_v1_analyze_diagnostic_post, create_auditoria_risco_v_1_analyze_auditoria_risco_post
from falaai_api.models.body_create_transcription_v1_audio_transcriptions_post import BodyCreateTranscriptionV1AudioTranscriptionsPost
from falaai_api.models.diagnostic_request import DiagnosticRequest
from falaai_api.models.auditoria_risco_request import AuditoriaRiscoRequest
from falaai_api.models.participant import Participant
from falaai_api.models.participant_role import ParticipantRole
from falaai_api.models.auditoria_risco_request_call_direction_type_0 import AuditoriaRiscoRequestCallDirectionType0
from tests.e2e import conftest as cfg
from tests.e2e.e2e_logger import log_test


def test_ai_chain():
    auth = AuthenticatedClient(base_url=cfg.PROD, token=cfg.KEY)

    f = File(payload=open(cfg.AUDIO, "rb"), file_name="analise_25s.mp3", mime_type="audio/mpeg")
    tb = BodyCreateTranscriptionV1AudioTranscriptionsPost(
        file=f,
        model="falaai-transcribe-1",
        language="pt",
        client_reference_id="e2e-call-2026-09-22-001",
    )
    r = create_transcription_v1_audio_transcriptions_post.sync_detailed(client=auth, body=tb)
    log_test("transcriptions", "POST", "/v1/audio/transcriptions", {"file": "analise_25s.mp3", "model": "falaai-transcribe-1", "language": "pt", "client_reference_id": "e2e-call-2026-09-22-001"}, r.parsed, f"HTTP {r.status_code}", r.status_code)
    assert r.status_code == 200, r.content[:300]
    tr = r.parsed
    assert isinstance(tr.id, str) and tr.id
    assert tr.object_
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
    assert isinstance(tr.input_.duration_s, float)
    assert isinstance(tr.input_.original_format, str) and tr.input_.original_format
    assert isinstance(tr.input_.codec, str) and tr.input_.codec
    assert isinstance(tr.input_.sample_rate, int)
    assert isinstance(tr.input_.channels, int)

    db = DiagnosticRequest(
        model="falaai-diagnostic-1",
        dialog=tr.dialog,
        language="pt-BR",
        duration_seconds=tr.duration_seconds,
        text=tr.text,
        audio_events=tr.audio_events,
        client_reference_id="e2e-diag-2026-09-22-001",
    )
    d = create_diagnostic_v1_analyze_diagnostic_post.sync_detailed(client=auth, body=db)
    log_test("diagnostic", "POST", "/v1/analyze/diagnostic", db, d.parsed, f"HTTP {d.status_code}", d.status_code)
    assert d.status_code == 200, d.content[:300]
    dp = d.parsed
    assert isinstance(dp.id, str) and dp.id
    assert isinstance(dp.response_language, str) and dp.response_language
    assert dp.object_ == "analysis"
    assert dp.analysis.dialogue_summary is not None
    assert dp.analysis.contact_reason is not None
    assert dp.analysis.identified_action is not None
    assert dp.analysis.identified_label is not None
    assert dp.analysis.sentiment is not None
    assert isinstance(dp.usage.characters, int)
    assert isinstance(dp.usage.credits_consumed, int)
    assert isinstance(dp.usage.processing_ms, int)

    ab = AuditoriaRiscoRequest(
        dialog=tr.dialog,
        language="pt-BR",
        response_language="pt-BR",
        duration_seconds=tr.duration_seconds,
        text=tr.text,
        audio_events=tr.audio_events,
        call_direction=AuditoriaRiscoRequestCallDirectionType0.INBOUND,
        participants=[
            Participant(interlocutor="Speaker 1", name="Mateus", role=ParticipantRole.AGENT),
            Participant(interlocutor="Speaker 2", name="Cliente", role=ParticipantRole.CLIENT),
        ],
        response_format="v2",
        client_reference_id="e2e-aud-2026-09-22-001",
    )
    a = create_auditoria_risco_v_1_analyze_auditoria_risco_post.sync_detailed(client=auth, body=ab)
    log_test("auditoriaRisco", "POST", "/v1/analyze/auditoriaRisco", ab, a.parsed, f"HTTP {a.status_code}", a.status_code)
    assert a.status_code == 200, a.content[:300]
    pub = a.parsed.response
    assert isinstance(pub.meta.id, str) and pub.meta.id
    assert isinstance(pub.meta.usage.characters, int)
    assert isinstance(pub.meta.usage.credits_consumed, int)
    assert isinstance(pub.meta.usage.processing_ms, int)
    for bloco in ("participants", "verdict", "scores", "detections", "analysis", "timeline",
                  "audio_event_model", "categories_summary", "indexer", "summary",
                  "acoes_i18n", "audit_decisions", "scoring_explanation"):
        assert getattr(pub, bloco) is not None, f"bloco ausente: {bloco}"
    assert isinstance(pub.html_report, str)