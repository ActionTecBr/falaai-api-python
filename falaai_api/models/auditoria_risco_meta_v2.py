from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_usage_v2 import AuditoriaRiscoUsageV2


T = TypeVar("T", bound="AuditoriaRiscoMetaV2")


@_attrs_define
class AuditoriaRiscoMetaV2:
    """
    Attributes:
        id (str): Analysis id
        usage (AuditoriaRiscoUsageV2):
        object_ (str | Unset): Object type Default: 'auditoria_risco'.
        call_duration_s (float | None | Unset): Call duration (s)
        analyzed_at (None | str | Unset): ISO 8601 analyzed timestamp
        client_reference_id (None | str | Unset): Echoed client reference id
    """

    id: str
    usage: AuditoriaRiscoUsageV2
    object_: str | Unset = "auditoria_risco"
    call_duration_s: float | None | Unset = UNSET
    analyzed_at: None | str | Unset = UNSET
    client_reference_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        usage = self.usage.to_dict()

        object_ = self.object_

        call_duration_s: float | None | Unset
        if isinstance(self.call_duration_s, Unset):
            call_duration_s = UNSET
        else:
            call_duration_s = self.call_duration_s

        analyzed_at: None | str | Unset
        if isinstance(self.analyzed_at, Unset):
            analyzed_at = UNSET
        else:
            analyzed_at = self.analyzed_at

        client_reference_id: None | str | Unset
        if isinstance(self.client_reference_id, Unset):
            client_reference_id = UNSET
        else:
            client_reference_id = self.client_reference_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "usage": usage,
            }
        )
        if object_ is not UNSET:
            field_dict["object"] = object_
        if call_duration_s is not UNSET:
            field_dict["call_duration_s"] = call_duration_s
        if analyzed_at is not UNSET:
            field_dict["analyzed_at"] = analyzed_at
        if client_reference_id is not UNSET:
            field_dict["client_reference_id"] = client_reference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_usage_v2 import AuditoriaRiscoUsageV2  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        usage = AuditoriaRiscoUsageV2.from_dict(d.pop("usage"))

        object_ = d.pop("object", UNSET)

        def _parse_call_duration_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        call_duration_s = _parse_call_duration_s(d.pop("call_duration_s", UNSET))

        def _parse_analyzed_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        analyzed_at = _parse_analyzed_at(d.pop("analyzed_at", UNSET))

        def _parse_client_reference_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_reference_id = _parse_client_reference_id(d.pop("client_reference_id", UNSET))

        auditoria_risco_meta_v2 = cls(
            id=id,
            usage=usage,
            object_=object_,
            call_duration_s=call_duration_s,
            analyzed_at=analyzed_at,
            client_reference_id=client_reference_id,
        )

        return auditoria_risco_meta_v2
