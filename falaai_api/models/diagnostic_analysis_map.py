from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnostic_categorical_analysis import DiagnosticCategoricalAnalysis
    from ..models.diagnostic_text_analysis import DiagnosticTextAnalysis
    from ..models.participant_diagnostic import ParticipantDiagnostic


T = TypeVar("T", bound="DiagnosticAnalysisMap")


@_attrs_define
class DiagnosticAnalysisMap:
    """
    Attributes:
        dialogue_summary (DiagnosticTextAnalysis):
        contact_reason (DiagnosticTextAnalysis):
        identified_action (DiagnosticCategoricalAnalysis):
        identified_label (DiagnosticCategoricalAnalysis):
        sentiment (DiagnosticCategoricalAnalysis):
        participants_identified (list[ParticipantDiagnostic] | Unset): Identified participants and roles (same field
            names as auditoria)
    """

    dialogue_summary: DiagnosticTextAnalysis
    contact_reason: DiagnosticTextAnalysis
    identified_action: DiagnosticCategoricalAnalysis
    identified_label: DiagnosticCategoricalAnalysis
    sentiment: DiagnosticCategoricalAnalysis
    participants_identified: list[ParticipantDiagnostic] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dialogue_summary = self.dialogue_summary.to_dict()

        contact_reason = self.contact_reason.to_dict()

        identified_action = self.identified_action.to_dict()

        identified_label = self.identified_label.to_dict()

        sentiment = self.sentiment.to_dict()

        participants_identified: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.participants_identified, Unset):
            participants_identified = []
            for participants_identified_item_data in self.participants_identified:
                participants_identified_item = participants_identified_item_data.to_dict()
                participants_identified.append(participants_identified_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dialogue_summary": dialogue_summary,
                "contact_reason": contact_reason,
                "identified_action": identified_action,
                "identified_label": identified_label,
                "sentiment": sentiment,
            }
        )
        if participants_identified is not UNSET:
            field_dict["participants_identified"] = participants_identified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnostic_categorical_analysis import DiagnosticCategoricalAnalysis  # noqa: PLC0415
        from ..models.diagnostic_text_analysis import DiagnosticTextAnalysis  # noqa: PLC0415
        from ..models.participant_diagnostic import ParticipantDiagnostic  # noqa: PLC0415

        d = dict(src_dict)
        dialogue_summary = DiagnosticTextAnalysis.from_dict(d.pop("dialogue_summary"))

        contact_reason = DiagnosticTextAnalysis.from_dict(d.pop("contact_reason"))

        identified_action = DiagnosticCategoricalAnalysis.from_dict(d.pop("identified_action"))

        identified_label = DiagnosticCategoricalAnalysis.from_dict(d.pop("identified_label"))

        sentiment = DiagnosticCategoricalAnalysis.from_dict(d.pop("sentiment"))

        _participants_identified = d.pop("participants_identified", UNSET)
        participants_identified: list[ParticipantDiagnostic] | Unset = UNSET
        if _participants_identified is not UNSET:
            participants_identified = []
            for participants_identified_item_data in _participants_identified:
                participants_identified_item = ParticipantDiagnostic.from_dict(participants_identified_item_data)

                participants_identified.append(participants_identified_item)

        diagnostic_analysis_map = cls(
            dialogue_summary=dialogue_summary,
            contact_reason=contact_reason,
            identified_action=identified_action,
            identified_label=identified_label,
            sentiment=sentiment,
            participants_identified=participants_identified,
        )

        diagnostic_analysis_map.additional_properties = d
        return diagnostic_analysis_map

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
