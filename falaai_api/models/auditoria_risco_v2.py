from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.auditoria_risco_analysis_v2 import AuditoriaRiscoAnalysisV2
    from ..models.auditoria_risco_audio_event_model_v2 import AuditoriaRiscoAudioEventModelV2
    from ..models.auditoria_risco_audit_decisions_v2 import AuditoriaRiscoAuditDecisionsV2
    from ..models.auditoria_risco_detections_v2 import AuditoriaRiscoDetectionsV2
    from ..models.auditoria_risco_indexer_v2 import AuditoriaRiscoIndexerV2
    from ..models.auditoria_risco_meta_v2 import AuditoriaRiscoMetaV2
    from ..models.auditoria_risco_participants_v2 import AuditoriaRiscoParticipantsV2
    from ..models.auditoria_risco_scores_v2 import AuditoriaRiscoScoresV2
    from ..models.auditoria_risco_scoring_explanation_v2 import AuditoriaRiscoScoringExplanationV2
    from ..models.auditoria_risco_summary_v2 import AuditoriaRiscoSummaryV2
    from ..models.auditoria_risco_timeline_v2 import AuditoriaRiscoTimelineV2
    from ..models.auditoria_risco_v2_acoes_i18n import AuditoriaRiscoV2AcoesI18N
    from ..models.auditoria_risco_v2_categories_summary import AuditoriaRiscoV2CategoriesSummary
    from ..models.auditoria_risco_verdict_v2 import AuditoriaRiscoVerdictV2


T = TypeVar("T", bound="AuditoriaRiscoV2")


@_attrs_define
class AuditoriaRiscoV2:
    """Response V2 (build_public_response_v2) â€” blocos logicos EN-US. Fonte: response_builder.py.

    Attributes:
        meta (AuditoriaRiscoMetaV2):
        participants (AuditoriaRiscoParticipantsV2):
        verdict (AuditoriaRiscoVerdictV2):
        scores (AuditoriaRiscoScoresV2):
        detections (AuditoriaRiscoDetectionsV2):
        analysis (AuditoriaRiscoAnalysisV2):
        timeline (AuditoriaRiscoTimelineV2):
        audio_event_model (AuditoriaRiscoAudioEventModelV2):
        categories_summary (AuditoriaRiscoV2CategoriesSummary): Per-category summary (keyed by category)
        indexer (AuditoriaRiscoIndexerV2):
        summary (AuditoriaRiscoSummaryV2):
        acoes_i18n (AuditoriaRiscoV2AcoesI18N): Used actions i18n catalog (keyed by action)
        audit_decisions (AuditoriaRiscoAuditDecisionsV2):
        scoring_explanation (AuditoriaRiscoScoringExplanationV2):
        html_report (str): HTML report (base64 gzip)
    """

    meta: AuditoriaRiscoMetaV2
    participants: AuditoriaRiscoParticipantsV2
    verdict: AuditoriaRiscoVerdictV2
    scores: AuditoriaRiscoScoresV2
    detections: AuditoriaRiscoDetectionsV2
    analysis: AuditoriaRiscoAnalysisV2
    timeline: AuditoriaRiscoTimelineV2
    audio_event_model: AuditoriaRiscoAudioEventModelV2
    categories_summary: AuditoriaRiscoV2CategoriesSummary
    indexer: AuditoriaRiscoIndexerV2
    summary: AuditoriaRiscoSummaryV2
    acoes_i18n: AuditoriaRiscoV2AcoesI18N
    audit_decisions: AuditoriaRiscoAuditDecisionsV2
    scoring_explanation: AuditoriaRiscoScoringExplanationV2
    html_report: str

    def to_dict(self) -> dict[str, Any]:
        meta = self.meta.to_dict()

        participants = self.participants.to_dict()

        verdict = self.verdict.to_dict()

        scores = self.scores.to_dict()

        detections = self.detections.to_dict()

        analysis = self.analysis.to_dict()

        timeline = self.timeline.to_dict()

        audio_event_model = self.audio_event_model.to_dict()

        categories_summary = self.categories_summary.to_dict()

        indexer = self.indexer.to_dict()

        summary = self.summary.to_dict()

        acoes_i18n = self.acoes_i18n.to_dict()

        audit_decisions = self.audit_decisions.to_dict()

        scoring_explanation = self.scoring_explanation.to_dict()

        html_report = self.html_report

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "meta": meta,
                "participants": participants,
                "verdict": verdict,
                "scores": scores,
                "detections": detections,
                "analysis": analysis,
                "timeline": timeline,
                "audio_event_model": audio_event_model,
                "categories_summary": categories_summary,
                "indexer": indexer,
                "summary": summary,
                "acoes_i18n": acoes_i18n,
                "audit_decisions": audit_decisions,
                "scoring_explanation": scoring_explanation,
                "html_report": html_report,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_analysis_v2 import AuditoriaRiscoAnalysisV2  # noqa: PLC0415
        from ..models.auditoria_risco_audio_event_model_v2 import AuditoriaRiscoAudioEventModelV2  # noqa: PLC0415
        from ..models.auditoria_risco_audit_decisions_v2 import AuditoriaRiscoAuditDecisionsV2  # noqa: PLC0415
        from ..models.auditoria_risco_detections_v2 import AuditoriaRiscoDetectionsV2  # noqa: PLC0415
        from ..models.auditoria_risco_indexer_v2 import AuditoriaRiscoIndexerV2  # noqa: PLC0415
        from ..models.auditoria_risco_meta_v2 import AuditoriaRiscoMetaV2  # noqa: PLC0415
        from ..models.auditoria_risco_participants_v2 import AuditoriaRiscoParticipantsV2  # noqa: PLC0415
        from ..models.auditoria_risco_scores_v2 import AuditoriaRiscoScoresV2  # noqa: PLC0415
        from ..models.auditoria_risco_scoring_explanation_v2 import AuditoriaRiscoScoringExplanationV2  # noqa: PLC0415
        from ..models.auditoria_risco_summary_v2 import AuditoriaRiscoSummaryV2  # noqa: PLC0415
        from ..models.auditoria_risco_timeline_v2 import AuditoriaRiscoTimelineV2  # noqa: PLC0415
        from ..models.auditoria_risco_v2_acoes_i18n import AuditoriaRiscoV2AcoesI18N  # noqa: PLC0415
        from ..models.auditoria_risco_v2_categories_summary import AuditoriaRiscoV2CategoriesSummary  # noqa: PLC0415
        from ..models.auditoria_risco_verdict_v2 import AuditoriaRiscoVerdictV2  # noqa: PLC0415

        d = dict(src_dict)
        meta = AuditoriaRiscoMetaV2.from_dict(d.pop("meta"))

        participants = AuditoriaRiscoParticipantsV2.from_dict(d.pop("participants"))

        verdict = AuditoriaRiscoVerdictV2.from_dict(d.pop("verdict"))

        scores = AuditoriaRiscoScoresV2.from_dict(d.pop("scores"))

        detections = AuditoriaRiscoDetectionsV2.from_dict(d.pop("detections"))

        analysis = AuditoriaRiscoAnalysisV2.from_dict(d.pop("analysis"))

        timeline = AuditoriaRiscoTimelineV2.from_dict(d.pop("timeline"))

        audio_event_model = AuditoriaRiscoAudioEventModelV2.from_dict(d.pop("audio_event_model"))

        categories_summary = AuditoriaRiscoV2CategoriesSummary.from_dict(d.pop("categories_summary"))

        indexer = AuditoriaRiscoIndexerV2.from_dict(d.pop("indexer"))

        summary = AuditoriaRiscoSummaryV2.from_dict(d.pop("summary"))

        acoes_i18n = AuditoriaRiscoV2AcoesI18N.from_dict(d.pop("acoes_i18n"))

        audit_decisions = AuditoriaRiscoAuditDecisionsV2.from_dict(d.pop("audit_decisions"))

        scoring_explanation = AuditoriaRiscoScoringExplanationV2.from_dict(d.pop("scoring_explanation"))

        html_report = d.pop("html_report")

        auditoria_risco_v2 = cls(
            meta=meta,
            participants=participants,
            verdict=verdict,
            scores=scores,
            detections=detections,
            analysis=analysis,
            timeline=timeline,
            audio_event_model=audio_event_model,
            categories_summary=categories_summary,
            indexer=indexer,
            summary=summary,
            acoes_i18n=acoes_i18n,
            audit_decisions=audit_decisions,
            scoring_explanation=scoring_explanation,
            html_report=html_report,
        )

        return auditoria_risco_v2
