from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AudioEvent")


@_attrs_define
class AudioEvent:
    """
    Attributes:
        event (str): Type of identified audio event. Ex: [riso], [suspiro], [pausa], [tosse] Example: [suspiro].
        start_s (float): Start time of audio event in seconds Example: 75.42.
        end_s (float): End time of audio event in seconds Example: 75.43.
        duration_s (float): Event duration in seconds Example: 0.01.
        formatted_timestamp (str): Formatted timestamp HH:MM:SS.mmm of event start Example: 00:01:15.420.
    """

    event: str
    start_s: float
    end_s: float
    duration_s: float
    formatted_timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        start_s = self.start_s

        end_s = self.end_s

        duration_s = self.duration_s

        formatted_timestamp = self.formatted_timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event": event,
                "start_s": start_s,
                "end_s": end_s,
                "duration_s": duration_s,
                "formatted_timestamp": formatted_timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event")

        start_s = d.pop("start_s")

        end_s = d.pop("end_s")

        duration_s = d.pop("duration_s")

        formatted_timestamp = d.pop("formatted_timestamp")

        audio_event = cls(
            event=event,
            start_s=start_s,
            end_s=end_s,
            duration_s=duration_s,
            formatted_timestamp=formatted_timestamp,
        )

        audio_event.additional_properties = d
        return audio_event

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
