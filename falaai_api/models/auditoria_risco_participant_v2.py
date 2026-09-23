from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditoriaRiscoParticipantV2")


@_attrs_define
class AuditoriaRiscoParticipantV2:
    """
    Attributes:
        interlocutor (None | str | Unset): Speaker label
        name (None | str | Unset): Participant name
        role (None | str | Unset): Role (agent/client/bot/unknown)
        confidence (None | str | Unset): Role inference confidence (high/medium/low)
        source (None | str | Unset): Role source (input/inferred)
        evidence (None | str | Unset): Role inference evidence
    """

    interlocutor: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    confidence: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    evidence: None | str | Unset = UNSET

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

        confidence: None | str | Unset
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        evidence: None | str | Unset
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        else:
            evidence = self.evidence

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if interlocutor is not UNSET:
            field_dict["interlocutor"] = interlocutor
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if source is not UNSET:
            field_dict["source"] = source
        if evidence is not UNSET:
            field_dict["evidence"] = evidence

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

        def _parse_confidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_evidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evidence = _parse_evidence(d.pop("evidence", UNSET))

        auditoria_risco_participant_v2 = cls(
            interlocutor=interlocutor,
            name=name,
            role=role,
            confidence=confidence,
            source=source,
            evidence=evidence,
        )

        return auditoria_risco_participant_v2
