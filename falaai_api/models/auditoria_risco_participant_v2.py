from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditoriaRiscoParticipantV2")


@_attrs_define
class AuditoriaRiscoParticipantV2:
    """
    Attributes:
        interlocutor (None | str | Unset): Speaker label
        name (None | str | Unset): Participant name
        role (None | str | Unset): Role (agent/client/bot/unknown)
    """

    interlocutor: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interlocutor: None | str | Unset
        if isinstance(self.interlocutor, Unset):
            interlocutor = UNSET
        else:
            interlocutor = self.interlocutor

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interlocutor is not UNSET:
            field_dict["interlocutor"] = interlocutor
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_interlocutor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interlocutor = _parse_interlocutor(d.pop("interlocutor", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        auditoria_risco_participant_v2 = cls(
            interlocutor=interlocutor,
            name=name,
            role=role,
        )

        auditoria_risco_participant_v2.additional_properties = d
        return auditoria_risco_participant_v2

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
