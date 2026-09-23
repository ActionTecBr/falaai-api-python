from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_conversation_scores_v2 import AuditoriaRiscoConversationScoresV2
    from ..models.auditoria_risco_scores_v2_per_participant import AuditoriaRiscoScoresV2PerParticipant


T = TypeVar("T", bound="AuditoriaRiscoScoresV2")


@_attrs_define
class AuditoriaRiscoScoresV2:
    """
    Attributes:
        conversation (AuditoriaRiscoConversationScoresV2):
        per_participant (AuditoriaRiscoScoresV2PerParticipant | Unset): Per-participant KPIs
    """

    conversation: AuditoriaRiscoConversationScoresV2
    per_participant: AuditoriaRiscoScoresV2PerParticipant | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conversation = self.conversation.to_dict()

        per_participant: dict[str, Any] | Unset = UNSET
        if not isinstance(self.per_participant, Unset):
            per_participant = self.per_participant.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conversation": conversation,
            }
        )
        if per_participant is not UNSET:
            field_dict["per_participant"] = per_participant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_conversation_scores_v2 import AuditoriaRiscoConversationScoresV2  # noqa: PLC0415
        from ..models.auditoria_risco_scores_v2_per_participant import (
            AuditoriaRiscoScoresV2PerParticipant,  # noqa: PLC0415
        )

        d = dict(src_dict)
        conversation = AuditoriaRiscoConversationScoresV2.from_dict(d.pop("conversation"))

        _per_participant = d.pop("per_participant", UNSET)
        per_participant: AuditoriaRiscoScoresV2PerParticipant | Unset
        if isinstance(_per_participant, Unset):
            per_participant = UNSET
        else:
            per_participant = AuditoriaRiscoScoresV2PerParticipant.from_dict(_per_participant)

        auditoria_risco_scores_v2 = cls(
            conversation=conversation,
            per_participant=per_participant,
        )

        auditoria_risco_scores_v2.additional_properties = d
        return auditoria_risco_scores_v2

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
