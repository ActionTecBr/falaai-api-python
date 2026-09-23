from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_audio_event_model_v2_windows_s import AuditoriaRiscoAudioEventModelV2WindowsS


T = TypeVar("T", bound="AuditoriaRiscoAudioEventModelV2")


@_attrs_define
class AuditoriaRiscoAudioEventModelV2:
    """
    Attributes:
        model (str | Unset): MAC model text (i18n) Default: ''.
        description (str | Unset): MAC description (i18n) Default: ''.
        windows_s (AuditoriaRiscoAudioEventModelV2WindowsS | Unset): Temporal windows (s)
    """

    model: str | Unset = ""
    description: str | Unset = ""
    windows_s: AuditoriaRiscoAudioEventModelV2WindowsS | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        description = self.description

        windows_s: dict[str, Any] | Unset = UNSET
        if not isinstance(self.windows_s, Unset):
            windows_s = self.windows_s.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if description is not UNSET:
            field_dict["description"] = description
        if windows_s is not UNSET:
            field_dict["windows_s"] = windows_s

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_audio_event_model_v2_windows_s import (
            AuditoriaRiscoAudioEventModelV2WindowsS,  # noqa: PLC0415
        )

        d = dict(src_dict)
        model = d.pop("model", UNSET)

        description = d.pop("description", UNSET)

        _windows_s = d.pop("windows_s", UNSET)
        windows_s: AuditoriaRiscoAudioEventModelV2WindowsS | Unset
        if isinstance(_windows_s, Unset):
            windows_s = UNSET
        else:
            windows_s = AuditoriaRiscoAudioEventModelV2WindowsS.from_dict(_windows_s)

        auditoria_risco_audio_event_model_v2 = cls(
            model=model,
            description=description,
            windows_s=windows_s,
        )

        auditoria_risco_audio_event_model_v2.additional_properties = d
        return auditoria_risco_audio_event_model_v2

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
