from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditoriaRiscoAppliedActionV2")


@_attrs_define
class AuditoriaRiscoAppliedActionV2:
    """
    Attributes:
        action_type (str): Action type code
        label (str): Action label
        description (str): Action description
        priority (str): CRITICO/ALTO/MEDIO/BAIXO
        color (str | Unset): Color Default: ''.
        icon (str | Unset): Icon Default: ''.
        condition (None | str | Unset): Condition
        reason (str | Unset): Reason Default: ''.
    """

    action_type: str
    label: str
    description: str
    priority: str
    color: str | Unset = ""
    icon: str | Unset = ""
    condition: None | str | Unset = UNSET
    reason: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        action_type = self.action_type

        label = self.label

        description = self.description

        priority = self.priority

        color = self.color

        icon = self.icon

        condition: None | str | Unset
        if isinstance(self.condition, Unset):
            condition = UNSET
        else:
            condition = self.condition

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action_type": action_type,
                "label": label,
                "description": description,
                "priority": priority,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if icon is not UNSET:
            field_dict["icon"] = icon
        if condition is not UNSET:
            field_dict["condition"] = condition
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        action_type = d.pop("action_type")

        label = d.pop("label")

        description = d.pop("description")

        priority = d.pop("priority")

        color = d.pop("color", UNSET)

        icon = d.pop("icon", UNSET)

        def _parse_condition(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        condition = _parse_condition(d.pop("condition", UNSET))

        reason = d.pop("reason", UNSET)

        auditoria_risco_applied_action_v2 = cls(
            action_type=action_type,
            label=label,
            description=description,
            priority=priority,
            color=color,
            icon=icon,
            condition=condition,
            reason=reason,
        )

        auditoria_risco_applied_action_v2.additional_properties = d
        return auditoria_risco_applied_action_v2

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
