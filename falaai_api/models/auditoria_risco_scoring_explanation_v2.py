from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditoriaRiscoScoringExplanationV2")


@_attrs_define
class AuditoriaRiscoScoringExplanationV2:
    """
    Attributes:
        summary (None | str | Unset): Explanation summary
        steps (list[Any] | Unset): Explanation steps
    """

    summary: None | str | Unset = UNSET
    steps: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        steps: list[Any] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = self.steps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary is not UNSET:
            field_dict["summary"] = summary
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        steps = cast(list[Any], d.pop("steps", UNSET))

        auditoria_risco_scoring_explanation_v2 = cls(
            summary=summary,
            steps=steps,
        )

        auditoria_risco_scoring_explanation_v2.additional_properties = d
        return auditoria_risco_scoring_explanation_v2

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
