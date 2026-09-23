from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantDiagnostic")


@_attrs_define
class ParticipantDiagnostic:
    """
    Attributes:
        interlocutor (str): Exact speaker label from the dialog (e.g. 'Speaker 1') Example: Speaker 1.
        role (str): Role: agent | client | bot | agent_requester | agent_custodian Example: client.
        name (None | str | Unset): Participant name if mentioned in the dialogue Example: AntÃ´nio.
        confidence (None | str | Unset): high | medium | low Example: high.
        evidence (None | str | Unset): Exact verbatim quote supporting the role (no timestamps) Example: TÃ¡ quarenta
            reais e setenta e um, AntÃ´nio..
    """

    interlocutor: str
    role: str
    name: None | str | Unset = UNSET
    confidence: None | str | Unset = UNSET
    evidence: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interlocutor = self.interlocutor

        role = self.role

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        confidence: None | str | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        evidence: None | str | Unset
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        else:
            evidence = self.evidence

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
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if evidence is not UNSET:
            field_dict["evidence"] = evidence

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        interlocutor = d.pop("interlocutor")

        role = d.pop("role")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_confidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_evidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evidence = _parse_evidence(d.pop("evidence", UNSET))

        participant_diagnostic = cls(
            interlocutor=interlocutor,
            role=role,
            name=name,
            confidence=confidence,
            evidence=evidence,
        )

        participant_diagnostic.additional_properties = d
        return participant_diagnostic

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
