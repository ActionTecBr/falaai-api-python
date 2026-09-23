from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AudioInputMeta")


@_attrs_define
class AudioInputMeta:
    """
    Attributes:
        duration_s (float): Exact audio duration sent in seconds Example: 151.04.
        original_format (str): Original file format (wav, mp3, ogg, etc) Example: wav.
        codec (str): Audio codec sent Example: pcm_s16le.
        sample_rate (int): Audio sample rate in Hz Example: 44100.
        channels (int): Number of channels (1=mono, 2=stereo) Example: 2.
    """

    duration_s: float
    original_format: str
    codec: str
    sample_rate: int
    channels: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duration_s = self.duration_s

        original_format = self.original_format

        codec = self.codec

        sample_rate = self.sample_rate

        channels = self.channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duration_s": duration_s,
                "original_format": original_format,
                "codec": codec,
                "sample_rate": sample_rate,
                "channels": channels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        duration_s = d.pop("duration_s")

        original_format = d.pop("original_format")

        codec = d.pop("codec")

        sample_rate = d.pop("sample_rate")

        channels = d.pop("channels")

        audio_input_meta = cls(
            duration_s=duration_s,
            original_format=original_format,
            codec=codec,
            sample_rate=sample_rate,
            channels=channels,
        )

        audio_input_meta.additional_properties = d
        return audio_input_meta

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
