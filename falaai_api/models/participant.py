from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.participant_role import ParticipantRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="Participant")


@_attrs_define
class Participant:
    """
    Attributes:
        interlocutor (str): Exact identifier as used in dialog (e.g. 'Interlocutor 1', 'Antonio') Example: Interlocutor
            1.
        role (ParticipantRole): Role: agent (human operator), client (customer), bot (IVR/AI)
        name (None | str | Unset): Participant name (humanizes report, does not affect logic) Example: Maria.
    """

    interlocutor: str
    role: ParticipantRole
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interlocutor = self.interlocutor

        role = self.role.value

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interlocutor": interlocutor,
                "role": role,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interlocutor = d.pop("interlocutor")

        role = ParticipantRole(d.pop("role"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        participant = cls(
            interlocutor=interlocutor,
            role=role,
            name=name,
        )

        participant.additional_properties = d
        return participant

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
