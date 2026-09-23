from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_applied_action_v2 import AuditoriaRiscoAppliedActionV2
    from ..models.auditoria_risco_verdict_v2_risk_matrix import AuditoriaRiscoVerdictV2RiskMatrix


T = TypeVar("T", bound="AuditoriaRiscoVerdictV2")


@_attrs_define
class AuditoriaRiscoVerdictV2:
    """
    Attributes:
        label (None | str | Unset): Human-readable verdict
        level_code (None | str | Unset): Classification level code
        color (None | str | Unset): Level color
        icon (None | str | Unset): Level icon
        risk_matrix (AuditoriaRiscoVerdictV2RiskMatrix | Unset): Risk matrix
        applied_actions (list[AuditoriaRiscoAppliedActionV2] | Unset): Applied actions
        decision_details (Any | None | Unset): Decision details
    """

    label: None | str | Unset = UNSET
    level_code: None | str | Unset = UNSET
    color: None | str | Unset = UNSET
    icon: None | str | Unset = UNSET
    risk_matrix: AuditoriaRiscoVerdictV2RiskMatrix | Unset = UNSET
    applied_actions: list[AuditoriaRiscoAppliedActionV2] | Unset = UNSET
    decision_details: Any | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        level_code: None | str | Unset
        if isinstance(self.level_code, Unset):
            level_code = UNSET
        else:
            level_code = self.level_code

        color: None | str | Unset
        if isinstance(self.color, Unset):
            color = UNSET
        else:
            color = self.color

        icon: None | str | Unset
        if isinstance(self.icon, Unset):
            icon = UNSET
        else:
            icon = self.icon

        risk_matrix: dict[str, Any] | Unset = UNSET
        if not isinstance(self.risk_matrix, Unset):
            risk_matrix = self.risk_matrix.to_dict()

        applied_actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.applied_actions, Unset):
            applied_actions = []
            for applied_actions_item_data in self.applied_actions:
                applied_actions_item = applied_actions_item_data.to_dict()
                applied_actions.append(applied_actions_item)

        decision_details: Any | None | Unset
        if isinstance(self.decision_details, Unset):
            decision_details = UNSET
        else:
            decision_details = self.decision_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if level_code is not UNSET:
            field_dict["level_code"] = level_code
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if risk_matrix is not UNSET:
            field_dict["risk_matrix"] = risk_matrix
        if applied_actions is not UNSET:
            field_dict["applied_actions"] = applied_actions
        if decision_details is not UNSET:
            field_dict["decision_details"] = decision_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_applied_action_v2 import AuditoriaRiscoAppliedActionV2  # noqa: PLC0415
        from ..models.auditoria_risco_verdict_v2_risk_matrix import AuditoriaRiscoVerdictV2RiskMatrix  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_level_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        level_code = _parse_level_code(d.pop("level_code", UNSET))

        def _parse_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        icon = _parse_icon(d.pop("icon", UNSET))

        _risk_matrix = d.pop("risk_matrix", UNSET)
        risk_matrix: AuditoriaRiscoVerdictV2RiskMatrix | Unset
        if isinstance(_risk_matrix, Unset):
            risk_matrix = UNSET
        else:
            risk_matrix = AuditoriaRiscoVerdictV2RiskMatrix.from_dict(_risk_matrix)

        _applied_actions = d.pop("applied_actions", UNSET)
        applied_actions: list[AuditoriaRiscoAppliedActionV2] | Unset = UNSET
        if _applied_actions is not UNSET:
            applied_actions = []
            for applied_actions_item_data in _applied_actions:
                applied_actions_item = AuditoriaRiscoAppliedActionV2.from_dict(applied_actions_item_data)

                applied_actions.append(applied_actions_item)

        def _parse_decision_details(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        decision_details = _parse_decision_details(d.pop("decision_details", UNSET))

        auditoria_risco_verdict_v2 = cls(
            label=label,
            level_code=level_code,
            color=color,
            icon=icon,
            risk_matrix=risk_matrix,
            applied_actions=applied_actions,
            decision_details=decision_details,
        )

        auditoria_risco_verdict_v2.additional_properties = d
        return auditoria_risco_verdict_v2

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
