from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TranscriptionUsage")


@_attrs_define
class TranscriptionUsage:
    """
    Attributes:
        audio_seconds (float): Actual audio duration processed in seconds Example: 151.04.
        credits_consumed (int): Number of credits consumed in this request Example: 65.
        processing_ms (int): Total processing time in milliseconds Example: 15156.
    """

    audio_seconds: float
    credits_consumed: int
    processing_ms: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio_seconds = self.audio_seconds

        credits_consumed = self.credits_consumed

        processing_ms = self.processing_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "audio_seconds": audio_seconds,
                "credits_consumed": credits_consumed,
                "processing_ms": processing_ms,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        audio_seconds = d.pop("audio_seconds")

        credits_consumed = d.pop("credits_consumed")

        processing_ms = d.pop("processing_ms")

        transcription_usage = cls(
            audio_seconds=audio_seconds,
            credits_consumed=credits_consumed,
            processing_ms=processing_ms,
        )

        transcription_usage.additional_properties = d
        return transcription_usage

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
