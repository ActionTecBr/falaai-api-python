from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditoriaRiscoAuditDecisionsV2")


@_attrs_define
class AuditoriaRiscoAuditDecisionsV2:
    """
    Attributes:
        risk_origin (None | str | Unset): Risk origin
        has_zero_tolerance_violation (bool | None | Unset): Has zero-tolerance violation
        deterministic_validator_changes (list[Any] | Unset): Deterministic validator changes
    """

    risk_origin: None | str | Unset = UNSET
    has_zero_tolerance_violation: bool | None | Unset = UNSET
    deterministic_validator_changes: list[Any] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        risk_origin: None | str | Unset
        if isinstance(self.risk_origin, Unset):
            risk_origin = UNSET
        else:
            risk_origin = self.risk_origin

        has_zero_tolerance_violation: bool | None | Unset
        if isinstance(self.has_zero_tolerance_violation, Unset):
            has_zero_tolerance_violation = UNSET
        else:
            has_zero_tolerance_violation = self.has_zero_tolerance_violation

        deterministic_validator_changes: list[Any] | Unset = UNSET
        if not isinstance(self.deterministic_validator_changes, Unset):
            deterministic_validator_changes = self.deterministic_validator_changes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if risk_origin is not UNSET:
            field_dict["risk_origin"] = risk_origin
        if has_zero_tolerance_violation is not UNSET:
            field_dict["has_zero_tolerance_violation"] = has_zero_tolerance_violation
        if deterministic_validator_changes is not UNSET:
            field_dict["deterministic_validator_changes"] = deterministic_validator_changes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_risk_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        risk_origin = _parse_risk_origin(d.pop("risk_origin", UNSET))

        def _parse_has_zero_tolerance_violation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        has_zero_tolerance_violation = _parse_has_zero_tolerance_violation(d.pop("has_zero_tolerance_violation", UNSET))

        deterministic_validator_changes = cast(list[Any], d.pop("deterministic_validator_changes", UNSET))

        auditoria_risco_audit_decisions_v2 = cls(
            risk_origin=risk_origin,
            has_zero_tolerance_violation=has_zero_tolerance_violation,
            deterministic_validator_changes=deterministic_validator_changes,
        )

        return auditoria_risco_audit_decisions_v2
