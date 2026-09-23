from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagnosticAudioEvent")


@_attrs_define
class DiagnosticAudioEvent:
    """
    Attributes:
        event (str): Audio event type. E.g.: [laughter], [sigh] Example: [laughter].
        start_s (float | None | Unset): Start time in seconds Example: 72.98.
        end_s (float | None | Unset): End time in seconds Example: 74.34.
        duration_s (float | None | Unset): Duration in seconds Example: 1.36.
        formatted_timestamp (None | str | Unset): Formatted timestamp (HH:MM:SS.ms) Example: 00:01:12.980.
    """

    event: str
    start_s: float | None | Unset = UNSET
    end_s: float | None | Unset = UNSET
    duration_s: float | None | Unset = UNSET
    formatted_timestamp: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        start_s: float | None | Unset
        if isinstance(self.start_s, Unset):
            start_s = UNSET
        else:
            start_s = self.start_s

        end_s: float | None | Unset
        if isinstance(self.end_s, Unset):
            end_s = UNSET
        else:
            end_s = self.end_s

        duration_s: float | None | Unset
        if isinstance(self.duration_s, Unset):
            duration_s = UNSET
        else:
            duration_s = self.duration_s

        formatted_timestamp: None | str | Unset
        if isinstance(self.formatted_timestamp, Unset):
            formatted_timestamp = UNSET
        else:
            formatted_timestamp = self.formatted_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
            }
        )
        if start_s is not UNSET:
            field_dict["start_s"] = start_s
        if end_s is not UNSET:
            field_dict["end_s"] = end_s
        if duration_s is not UNSET:
            field_dict["duration_s"] = duration_s
        if formatted_timestamp is not UNSET:
            field_dict["formatted_timestamp"] = formatted_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event")

        def _parse_start_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        start_s = _parse_start_s(d.pop("start_s", UNSET))

        def _parse_end_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        end_s = _parse_end_s(d.pop("end_s", UNSET))

        def _parse_duration_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        duration_s = _parse_duration_s(d.pop("duration_s", UNSET))

        def _parse_formatted_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        formatted_timestamp = _parse_formatted_timestamp(d.pop("formatted_timestamp", UNSET))

        diagnostic_audio_event = cls(
            event=event,
            start_s=start_s,
            end_s=end_s,
            duration_s=duration_s,
            formatted_timestamp=formatted_timestamp,
        )

        diagnostic_audio_event.additional_properties = d
        return diagnostic_audio_event

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
