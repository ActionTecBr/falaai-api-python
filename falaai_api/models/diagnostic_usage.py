from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DiagnosticUsage")


@_attrs_define
class DiagnosticUsage:
    """
    Attributes:
        characters (int): Total characters analyzed Example: 3946.
        credits_consumed (int): Credits consumed: max(ceil(chars/500)*3, 3) * 5 Example: 15.
        processing_ms (int): Total processing time in milliseconds Example: 6800.
    """

    characters: int
    credits_consumed: int
    processing_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        characters = self.characters

        credits_consumed = self.credits_consumed

        processing_ms = self.processing_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "characters": characters,
                "credits_consumed": credits_consumed,
                "processing_ms": processing_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        characters = d.pop("characters")

        credits_consumed = d.pop("credits_consumed")

        processing_ms = d.pop("processing_ms")

        diagnostic_usage = cls(
            characters=characters,
            credits_consumed=credits_consumed,
            processing_ms=processing_ms,
        )

        diagnostic_usage.additional_properties = d
        return diagnostic_usage

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
