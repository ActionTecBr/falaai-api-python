from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VersionResponse")


@_attrs_define
class VersionResponse:
    """
    Attributes:
        service (str): Service name Example: FalaAI API.
        version (str): Current API version Example: api_v1.21.45.
        deploy_date (str): Deploy timestamp Example: 2026-09-22 20260922_023910.
    """

    service: str
    version: str
    deploy_date: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service = self.service

        version = self.version

        deploy_date = self.deploy_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "service": service,
                "version": version,
                "deployDate": deploy_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service = d.pop("service")

        version = d.pop("version")

        deploy_date = d.pop("deployDate")

        version_response = cls(
            service=service,
            version=version,
            deploy_date=deploy_date,
        )

        version_response.additional_properties = d
        return version_response

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
