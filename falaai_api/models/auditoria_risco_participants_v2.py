from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_participant_v2 import AuditoriaRiscoParticipantV2


T = TypeVar("T", bound="AuditoriaRiscoParticipantsV2")


@_attrs_define
class AuditoriaRiscoParticipantsV2:
    """
    Attributes:
        identified (list[AuditoriaRiscoParticipantV2] | Unset): Identified participants
        call_direction (None | str | Unset): inbound/outbound
        role_inference_reliable (bool | Unset): Role inference reliability Default: True.
        identification_status (str | Unset): Identification status Default: 'none'.
        unidentified_items_count (int | Unset): Unidentified items count Default: 0.
    """

    identified: list[AuditoriaRiscoParticipantV2] | Unset = UNSET
    call_direction: None | str | Unset = UNSET
    role_inference_reliable: bool | Unset = True
    identification_status: str | Unset = "none"
    unidentified_items_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identified: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identified, Unset):
            identified = []
            for identified_item_data in self.identified:
                identified_item = identified_item_data.to_dict()
                identified.append(identified_item)

        call_direction: None | str | Unset
        if isinstance(self.call_direction, Unset):
            call_direction = UNSET
        else:
            call_direction = self.call_direction

        role_inference_reliable = self.role_inference_reliable

        identification_status = self.identification_status

        unidentified_items_count = self.unidentified_items_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identified is not UNSET:
            field_dict["identified"] = identified
        if call_direction is not UNSET:
            field_dict["call_direction"] = call_direction
        if role_inference_reliable is not UNSET:
            field_dict["role_inference_reliable"] = role_inference_reliable
        if identification_status is not UNSET:
            field_dict["identification_status"] = identification_status
        if unidentified_items_count is not UNSET:
            field_dict["unidentified_items_count"] = unidentified_items_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_participant_v2 import AuditoriaRiscoParticipantV2  # noqa: PLC0415

        d = dict(src_dict)
        _identified = d.pop("identified", UNSET)
        identified: list[AuditoriaRiscoParticipantV2] | Unset = UNSET
        if _identified is not UNSET:
            identified = []
            for identified_item_data in _identified:
                identified_item = AuditoriaRiscoParticipantV2.from_dict(identified_item_data)

                identified.append(identified_item)

        def _parse_call_direction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        call_direction = _parse_call_direction(d.pop("call_direction", UNSET))

        role_inference_reliable = d.pop("role_inference_reliable", UNSET)

        identification_status = d.pop("identification_status", UNSET)

        unidentified_items_count = d.pop("unidentified_items_count", UNSET)

        auditoria_risco_participants_v2 = cls(
            identified=identified,
            call_direction=call_direction,
            role_inference_reliable=role_inference_reliable,
            identification_status=identification_status,
            unidentified_items_count=unidentified_items_count,
        )

        auditoria_risco_participants_v2.additional_properties = d
        return auditoria_risco_participants_v2

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
