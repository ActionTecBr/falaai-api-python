from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagnosticCategoricalAnalysis")


@_attrs_define
class DiagnosticCategoricalAnalysis:
    """
    Attributes:
        list_choice (None | str | Unset): Selected value from classification list (used in action, label, sentiment)
            Example: Informative.
        justification (None | str | Unset): Justification for the choice Example: Information about required
            documentation was provided.
        evidence_phrases (list[str] | Unset): Verbatim transcript excerpts supporting the analysis Example:
            ['[00:01:36.640 - 00:02:02.659] No, same thing: proof of address...'].
    """

    list_choice: None | str | Unset = UNSET
    justification: None | str | Unset = UNSET
    evidence_phrases: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_choice: None | str | Unset
        if isinstance(self.list_choice, Unset):
            list_choice = UNSET
        else:
            list_choice = self.list_choice

        justification: None | str | Unset
        if isinstance(self.justification, Unset):
            justification = UNSET
        else:
            justification = self.justification

        evidence_phrases: list[str] | Unset = UNSET
        if not isinstance(self.evidence_phrases, Unset):
            evidence_phrases = self.evidence_phrases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if list_choice is not UNSET:
            field_dict["list_choice"] = list_choice
        if justification is not UNSET:
            field_dict["justification"] = justification
        if evidence_phrases is not UNSET:
            field_dict["evidence_phrases"] = evidence_phrases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_list_choice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        list_choice = _parse_list_choice(d.pop("list_choice", UNSET))

        def _parse_justification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        justification = _parse_justification(d.pop("justification", UNSET))

        evidence_phrases = cast(list[str], d.pop("evidence_phrases", UNSET))

        diagnostic_categorical_analysis = cls(
            list_choice=list_choice,
            justification=justification,
            evidence_phrases=evidence_phrases,
        )

        diagnostic_categorical_analysis.additional_properties = d
        return diagnostic_categorical_analysis

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
