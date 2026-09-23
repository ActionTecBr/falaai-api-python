from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UsageLogItem")


@_attrs_define
class UsageLogItem:
    """
    Attributes:
        id (str): Usage log entry id
        endpoint (str): Endpoint called
        credits_cost (int): Credits consumed
        status (str): Result status
        errors_count (int): Errors count
        created_at (str): ISO 8601 timestamp
    """

    id: str
    endpoint: str
    credits_cost: int
    status: str
    errors_count: int
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        endpoint = self.endpoint

        credits_cost = self.credits_cost

        status = self.status

        errors_count = self.errors_count

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "endpoint": endpoint,
                "credits_cost": credits_cost,
                "status": status,
                "errors_count": errors_count,
                "created_at": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        endpoint = d.pop("endpoint")

        credits_cost = d.pop("credits_cost")

        status = d.pop("status")

        errors_count = d.pop("errors_count")

        created_at = d.pop("created_at")

        usage_log_item = cls(
            id=id,
            endpoint=endpoint,
            credits_cost=credits_cost,
            status=status,
            errors_count=errors_count,
            created_at=created_at,
        )

        usage_log_item.additional_properties = d
        return usage_log_item

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
