from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

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

        return auditoria_risco_scoring_explanation_v2
