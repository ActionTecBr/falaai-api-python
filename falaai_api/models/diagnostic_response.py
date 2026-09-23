from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnostic_analysis_map import DiagnosticAnalysisMap
    from ..models.diagnostic_usage import DiagnosticUsage


T = TypeVar("T", bound="DiagnosticResponse")


@_attrs_define
class DiagnosticResponse:
    """
    Attributes:
        id (str): Unique analysis identifier. Prefix 'di-' + UUID Example: di-550e8400-e29b-41d4-a716-446655440000.
        response_language (str): Language used in the response. E.g.: 'pt-BR', 'en-US', 'es-ES' Example: pt-BR.
        object_ (str): Object type. Always 'analysis' Example: analysis.
        analysis (DiagnosticAnalysisMap):
        usage (DiagnosticUsage):
        client_reference_id (None | str | Unset): Client-supplied ID echoed verbatim (if provided in request) Example:
            call-2026-08-30-001.
    """

    id: str
    response_language: str
    object_: str
    analysis: DiagnosticAnalysisMap
    usage: DiagnosticUsage
    client_reference_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        response_language = self.response_language

        object_ = self.object_

        analysis = self.analysis.to_dict()

        usage = self.usage.to_dict()

        client_reference_id: None | str | Unset
        if isinstance(self.client_reference_id, Unset):
            client_reference_id = UNSET
        else:
            client_reference_id = self.client_reference_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "response_language": response_language,
                "object": object_,
                "analysis": analysis,
                "usage": usage,
            }
        )
        if client_reference_id is not UNSET:
            field_dict["client_reference_id"] = client_reference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnostic_analysis_map import DiagnosticAnalysisMap  # noqa: PLC0415
        from ..models.diagnostic_usage import DiagnosticUsage  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        response_language = d.pop("response_language")

        object_ = d.pop("object")

        analysis = DiagnosticAnalysisMap.from_dict(d.pop("analysis"))

        usage = DiagnosticUsage.from_dict(d.pop("usage"))

        def _parse_client_reference_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_reference_id = _parse_client_reference_id(d.pop("client_reference_id", UNSET))

        diagnostic_response = cls(
            id=id,
            response_language=response_language,
            object_=object_,
            analysis=analysis,
            usage=usage,
            client_reference_id=client_reference_id,
        )

        diagnostic_response.additional_properties = d
        return diagnostic_response

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
