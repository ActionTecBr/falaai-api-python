from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

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

        return auditoria_risco_applied_action_v2
