from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_detection_item_v2 import AuditoriaRiscoDetectionItemV2
    from ..models.auditoria_risco_detections_v2_client_behavior_alerts_item import (
        AuditoriaRiscoDetectionsV2ClientBehaviorAlertsItem,
    )
    from ..models.auditoria_risco_detections_v2_client_risk_alerts_item import (
        AuditoriaRiscoDetectionsV2ClientRiskAlertsItem,
    )


T = TypeVar("T", bound="AuditoriaRiscoDetectionsV2")


@_attrs_define
class AuditoriaRiscoDetectionsV2:
    """
    Attributes:
        violations (list[AuditoriaRiscoDetectionItemV2] | Unset): Active violations
        positives (list[AuditoriaRiscoDetectionItemV2] | Unset): Active positives
        client_risk_alerts (list[AuditoriaRiscoDetectionsV2ClientRiskAlertsItem] | Unset): Client risk alerts
        client_behavior_alerts (list[AuditoriaRiscoDetectionsV2ClientBehaviorAlertsItem] | Unset): Client behavior
            alerts
        client_negatives (list[AuditoriaRiscoDetectionItemV2] | Unset): Client negatives
    """

    violations: list[AuditoriaRiscoDetectionItemV2] | Unset = UNSET
    positives: list[AuditoriaRiscoDetectionItemV2] | Unset = UNSET
    client_risk_alerts: list[AuditoriaRiscoDetectionsV2ClientRiskAlertsItem] | Unset = UNSET
    client_behavior_alerts: list[AuditoriaRiscoDetectionsV2ClientBehaviorAlertsItem] | Unset = UNSET
    client_negatives: list[AuditoriaRiscoDetectionItemV2] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        violations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.violations, Unset):
            violations = []
            for violations_item_data in self.violations:
                violations_item = violations_item_data.to_dict()
                violations.append(violations_item)

        positives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.positives, Unset):
            positives = []
            for positives_item_data in self.positives:
                positives_item = positives_item_data.to_dict()
                positives.append(positives_item)

        client_risk_alerts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_risk_alerts, Unset):
            client_risk_alerts = []
            for client_risk_alerts_item_data in self.client_risk_alerts:
                client_risk_alerts_item = client_risk_alerts_item_data.to_dict()
                client_risk_alerts.append(client_risk_alerts_item)

        client_behavior_alerts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_behavior_alerts, Unset):
            client_behavior_alerts = []
            for client_behavior_alerts_item_data in self.client_behavior_alerts:
                client_behavior_alerts_item = client_behavior_alerts_item_data.to_dict()
                client_behavior_alerts.append(client_behavior_alerts_item)

        client_negatives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_negatives, Unset):
            client_negatives = []
            for client_negatives_item_data in self.client_negatives:
                client_negatives_item = client_negatives_item_data.to_dict()
                client_negatives.append(client_negatives_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if violations is not UNSET:
            field_dict["violations"] = violations
        if positives is not UNSET:
            field_dict["positives"] = positives
        if client_risk_alerts is not UNSET:
            field_dict["client_risk_alerts"] = client_risk_alerts
        if client_behavior_alerts is not UNSET:
            field_dict["client_behavior_alerts"] = client_behavior_alerts
        if client_negatives is not UNSET:
            field_dict["client_negatives"] = client_negatives

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_detection_item_v2 import AuditoriaRiscoDetectionItemV2  # noqa: PLC0415
        from ..models.auditoria_risco_detections_v2_client_behavior_alerts_item import (
            AuditoriaRiscoDetectionsV2ClientBehaviorAlertsItem,  # noqa: PLC0415
        )
        from ..models.auditoria_risco_detections_v2_client_risk_alerts_item import (
            AuditoriaRiscoDetectionsV2ClientRiskAlertsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _violations = d.pop("violations", UNSET)
        violations: list[AuditoriaRiscoDetectionItemV2] | Unset = UNSET
        if _violations is not UNSET:
            violations = []
            for violations_item_data in _violations:
                violations_item = AuditoriaRiscoDetectionItemV2.from_dict(violations_item_data)

                violations.append(violations_item)

        _positives = d.pop("positives", UNSET)
        positives: list[AuditoriaRiscoDetectionItemV2] | Unset = UNSET
        if _positives is not UNSET:
            positives = []
            for positives_item_data in _positives:
                positives_item = AuditoriaRiscoDetectionItemV2.from_dict(positives_item_data)

                positives.append(positives_item)

        _client_risk_alerts = d.pop("client_risk_alerts", UNSET)
        client_risk_alerts: list[AuditoriaRiscoDetectionsV2ClientRiskAlertsItem] | Unset = UNSET
        if _client_risk_alerts is not UNSET:
            client_risk_alerts = []
            for client_risk_alerts_item_data in _client_risk_alerts:
                client_risk_alerts_item = AuditoriaRiscoDetectionsV2ClientRiskAlertsItem.from_dict(
                    client_risk_alerts_item_data
                )

                client_risk_alerts.append(client_risk_alerts_item)

        _client_behavior_alerts = d.pop("client_behavior_alerts", UNSET)
        client_behavior_alerts: list[AuditoriaRiscoDetectionsV2ClientBehaviorAlertsItem] | Unset = UNSET
        if _client_behavior_alerts is not UNSET:
            client_behavior_alerts = []
            for client_behavior_alerts_item_data in _client_behavior_alerts:
                client_behavior_alerts_item = AuditoriaRiscoDetectionsV2ClientBehaviorAlertsItem.from_dict(
                    client_behavior_alerts_item_data
                )

                client_behavior_alerts.append(client_behavior_alerts_item)

        _client_negatives = d.pop("client_negatives", UNSET)
        client_negatives: list[AuditoriaRiscoDetectionItemV2] | Unset = UNSET
        if _client_negatives is not UNSET:
            client_negatives = []
            for client_negatives_item_data in _client_negatives:
                client_negatives_item = AuditoriaRiscoDetectionItemV2.from_dict(client_negatives_item_data)

                client_negatives.append(client_negatives_item)

        auditoria_risco_detections_v2 = cls(
            violations=violations,
            positives=positives,
            client_risk_alerts=client_risk_alerts,
            client_behavior_alerts=client_behavior_alerts,
            client_negatives=client_negatives,
        )

        return auditoria_risco_detections_v2
