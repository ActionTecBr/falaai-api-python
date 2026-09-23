from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditoriaRiscoConversationScoresV2")


@_attrs_define
class AuditoriaRiscoConversationScoresV2:
    """
    Attributes:
        consolidated_score (float | None | Unset): Consolidated score
        violation_density_per_min (float | None | Unset): Violation density/min
        sentiment_trend (Any | None | Unset): Sentiment trend
        pct_turns_with_violation (float | None | Unset): % turns with violation
        most_critical_turn (Any | None | Unset): Most critical turn
        positive_negative_ratio (Any | None | Unset): Positive:negative ratio
        global_risk_severity (None | str | Unset): Global risk severity code
        global_risk_severity_label (None | str | Unset): Global risk severity label
        global_risk_severity_color (None | str | Unset): Global risk severity color
        risk_likelihood_avg (float | None | Unset): Risk likelihood avg
        risk_impact_avg (float | None | Unset): Risk impact avg
    """

    consolidated_score: float | None | Unset = UNSET
    violation_density_per_min: float | None | Unset = UNSET
    sentiment_trend: Any | None | Unset = UNSET
    pct_turns_with_violation: float | None | Unset = UNSET
    most_critical_turn: Any | None | Unset = UNSET
    positive_negative_ratio: Any | None | Unset = UNSET
    global_risk_severity: None | str | Unset = UNSET
    global_risk_severity_label: None | str | Unset = UNSET
    global_risk_severity_color: None | str | Unset = UNSET
    risk_likelihood_avg: float | None | Unset = UNSET
    risk_impact_avg: float | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        consolidated_score: float | None | Unset
        if isinstance(self.consolidated_score, Unset):
            consolidated_score = UNSET
        else:
            consolidated_score = self.consolidated_score

        violation_density_per_min: float | None | Unset
        if isinstance(self.violation_density_per_min, Unset):
            violation_density_per_min = UNSET
        else:
            violation_density_per_min = self.violation_density_per_min

        sentiment_trend: Any | None | Unset
        if isinstance(self.sentiment_trend, Unset):
            sentiment_trend = UNSET
        else:
            sentiment_trend = self.sentiment_trend

        pct_turns_with_violation: float | None | Unset
        if isinstance(self.pct_turns_with_violation, Unset):
            pct_turns_with_violation = UNSET
        else:
            pct_turns_with_violation = self.pct_turns_with_violation

        most_critical_turn: Any | None | Unset
        if isinstance(self.most_critical_turn, Unset):
            most_critical_turn = UNSET
        else:
            most_critical_turn = self.most_critical_turn

        positive_negative_ratio: Any | None | Unset
        if isinstance(self.positive_negative_ratio, Unset):
            positive_negative_ratio = UNSET
        else:
            positive_negative_ratio = self.positive_negative_ratio

        global_risk_severity: None | str | Unset
        if isinstance(self.global_risk_severity, Unset):
            global_risk_severity = UNSET
        else:
            global_risk_severity = self.global_risk_severity

        global_risk_severity_label: None | str | Unset
        if isinstance(self.global_risk_severity_label, Unset):
            global_risk_severity_label = UNSET
        else:
            global_risk_severity_label = self.global_risk_severity_label

        global_risk_severity_color: None | str | Unset
        if isinstance(self.global_risk_severity_color, Unset):
            global_risk_severity_color = UNSET
        else:
            global_risk_severity_color = self.global_risk_severity_color

        risk_likelihood_avg: float | None | Unset
        if isinstance(self.risk_likelihood_avg, Unset):
            risk_likelihood_avg = UNSET
        else:
            risk_likelihood_avg = self.risk_likelihood_avg

        risk_impact_avg: float | None | Unset
        if isinstance(self.risk_impact_avg, Unset):
            risk_impact_avg = UNSET
        else:
            risk_impact_avg = self.risk_impact_avg

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if consolidated_score is not UNSET:
            field_dict["consolidated_score"] = consolidated_score
        if violation_density_per_min is not UNSET:
            field_dict["violation_density_per_min"] = violation_density_per_min
        if sentiment_trend is not UNSET:
            field_dict["sentiment_trend"] = sentiment_trend
        if pct_turns_with_violation is not UNSET:
            field_dict["pct_turns_with_violation"] = pct_turns_with_violation
        if most_critical_turn is not UNSET:
            field_dict["most_critical_turn"] = most_critical_turn
        if positive_negative_ratio is not UNSET:
            field_dict["positive_negative_ratio"] = positive_negative_ratio
        if global_risk_severity is not UNSET:
            field_dict["global_risk_severity"] = global_risk_severity
        if global_risk_severity_label is not UNSET:
            field_dict["global_risk_severity_label"] = global_risk_severity_label
        if global_risk_severity_color is not UNSET:
            field_dict["global_risk_severity_color"] = global_risk_severity_color
        if risk_likelihood_avg is not UNSET:
            field_dict["risk_likelihood_avg"] = risk_likelihood_avg
        if risk_impact_avg is not UNSET:
            field_dict["risk_impact_avg"] = risk_impact_avg

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_consolidated_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        consolidated_score = _parse_consolidated_score(d.pop("consolidated_score", UNSET))

        def _parse_violation_density_per_min(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        violation_density_per_min = _parse_violation_density_per_min(d.pop("violation_density_per_min", UNSET))

        def _parse_sentiment_trend(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        sentiment_trend = _parse_sentiment_trend(d.pop("sentiment_trend", UNSET))

        def _parse_pct_turns_with_violation(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        pct_turns_with_violation = _parse_pct_turns_with_violation(d.pop("pct_turns_with_violation", UNSET))

        def _parse_most_critical_turn(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        most_critical_turn = _parse_most_critical_turn(d.pop("most_critical_turn", UNSET))

        def _parse_positive_negative_ratio(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        positive_negative_ratio = _parse_positive_negative_ratio(d.pop("positive_negative_ratio", UNSET))

        def _parse_global_risk_severity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        global_risk_severity = _parse_global_risk_severity(d.pop("global_risk_severity", UNSET))

        def _parse_global_risk_severity_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        global_risk_severity_label = _parse_global_risk_severity_label(d.pop("global_risk_severity_label", UNSET))

        def _parse_global_risk_severity_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        global_risk_severity_color = _parse_global_risk_severity_color(d.pop("global_risk_severity_color", UNSET))

        def _parse_risk_likelihood_avg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        risk_likelihood_avg = _parse_risk_likelihood_avg(d.pop("risk_likelihood_avg", UNSET))

        def _parse_risk_impact_avg(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        risk_impact_avg = _parse_risk_impact_avg(d.pop("risk_impact_avg", UNSET))

        auditoria_risco_conversation_scores_v2 = cls(
            consolidated_score=consolidated_score,
            violation_density_per_min=violation_density_per_min,
            sentiment_trend=sentiment_trend,
            pct_turns_with_violation=pct_turns_with_violation,
            most_critical_turn=most_critical_turn,
            positive_negative_ratio=positive_negative_ratio,
            global_risk_severity=global_risk_severity,
            global_risk_severity_label=global_risk_severity_label,
            global_risk_severity_color=global_risk_severity_color,
            risk_likelihood_avg=risk_likelihood_avg,
            risk_impact_avg=risk_impact_avg,
        )

        return auditoria_risco_conversation_scores_v2
