from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.auditoria_risco_v2 import AuditoriaRiscoV2


T = TypeVar("T", bound="AuditoriaRiscoV2Response")


@_attrs_define
class AuditoriaRiscoV2Response:
    """
    Attributes:
        response (AuditoriaRiscoV2): Response V2 (build_public_response_v2) — blocos logicos EN-US. Fonte:
            response_builder.py.
    """

    response: AuditoriaRiscoV2
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        response = self.response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response": response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_v2 import AuditoriaRiscoV2  # noqa: PLC0415

        d = dict(src_dict)
        response = AuditoriaRiscoV2.from_dict(d.pop("response"))

        auditoria_risco_v2_response = cls(
            response=response,
        )

        auditoria_risco_v2_response.additional_properties = d
        return auditoria_risco_v2_response

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
