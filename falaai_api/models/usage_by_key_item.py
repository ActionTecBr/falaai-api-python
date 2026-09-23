from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsageByKeyItem")


@_attrs_define
class UsageByKeyItem:
    """
    Attributes:
        key_id (str): API key id
        key_name (str): API key name
        total_credits (int): Total credits consumed by the key
        request_count (int): Number of requests
        last_used (None | str | Unset): ISO 8601 of last use (null if never)
    """

    key_id: str
    key_name: str
    total_credits: int
    request_count: int
    last_used: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key_id = self.key_id

        key_name = self.key_name

        total_credits = self.total_credits

        request_count = self.request_count

        last_used: None | str | Unset
        if isinstance(self.last_used, Unset):
            last_used = UNSET
        else:
            last_used = self.last_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_id": key_id,
                "key_name": key_name,
                "total_credits": total_credits,
                "request_count": request_count,
            }
        )
        if last_used is not UNSET:
            field_dict["last_used"] = last_used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key_id = d.pop("key_id")

        key_name = d.pop("key_name")

        total_credits = d.pop("total_credits")

        request_count = d.pop("request_count")

        def _parse_last_used(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_used = _parse_last_used(d.pop("last_used", UNSET))

        usage_by_key_item = cls(
            key_id=key_id,
            key_name=key_name,
            total_credits=total_credits,
            request_count=request_count,
            last_used=last_used,
        )

        usage_by_key_item.additional_properties = d
        return usage_by_key_item

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
