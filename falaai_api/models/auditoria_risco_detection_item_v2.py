from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_detection_item_v2_mac_details_item import AuditoriaRiscoDetectionItemV2MacDetailsItem


T = TypeVar("T", bound="AuditoriaRiscoDetectionItemV2")


@_attrs_define
class AuditoriaRiscoDetectionItemV2:
    """
    Attributes:
        category_label (str): Category label (i18n)
        category_group (str): Category group label (i18n)
        turn (int | None | Unset): Turn number
        interlocutor (None | str | Unset): Speaker
        role (None | str | Unset): Role
        timestamp_start_s (float | None | Unset): Start (s)
        timestamp_end_s (float | None | Unset): End (s)
        timestamp_formatted (None | str | Unset): Formatted timestamp
        term_text (None | str | Unset): Detected term
        suggested_term_for_bank (Any | None | Unset): Suggested term for bank
        category (None | str | Unset): Category code
        category_color (None | str | Unset): Category color
        category_icon (None | str | Unset): Category icon
        criticality (None | str | Unset): Criticality
        category_threshold (float | None | Unset): Category threshold
        category_type (None | str | Unset): Category type
        nature (None | str | Unset): Nature
        llm_confidence (float | None | Unset): LLM confidence
        reason (None | str | Unset): Reason
        is_valid_context (bool | None | Unset): Valid context
        risk_probability (float | None | Unset): Risk probability
        risk_impact (float | None | Unset): Risk impact
        category_weight (float | None | Unset): Category weight
        turn_sentiment (None | str | Unset): Turn sentiment
        intensity (Any | None | Unset): Intensity
        mod_applied (float | None | Unset): Total modifier applied
        mac_applied (float | None | Unset): Audio modifier applied
        mvad_applied (float | None | Unset): Intensity modifier applied
        mod_formula (None | str | Unset): Modifier formula
        mac_details (list[AuditoriaRiscoDetectionItemV2MacDetailsItem] | Unset): MAC details
        calibration_reason (None | str | Unset): Calibration reason
        final_score (float | None | Unset): Final score
        final_score_formula (None | str | Unset): Final score formula
        conversation_limit (Any | None | Unset): Conversation limit
        apply_saturation (bool | None | Unset): Apply saturation
        block_repetition (bool | None | Unset): Block repetition
        status (None | str | Unset): Status
        effective_impact (float | None | Unset): Effective impact
        saturation_factor (float | None | Unset): Saturation factor
        saturation_formula (None | str | Unset): Saturation formula
        threshold_formula (None | str | Unset): Threshold formula
        blocked_formula (None | str | Unset): Blocked formula
        reconciliation_note (None | str | Unset): Reconciliation note
        violated_frameworks (list[Any] | Unset): Violated frameworks
        citation_fidelity (bool | Unset): Citation fidelity Default: True.
        subcategory (None | str | Unset): Subcategory code
        subcategory_label (None | str | Unset): Subcategory label (i18n)
    """

    category_label: str
    category_group: str
    turn: int | None | Unset = UNSET
    interlocutor: None | str | Unset = UNSET
    role: None | str | Unset = UNSET
    timestamp_start_s: float | None | Unset = UNSET
    timestamp_end_s: float | None | Unset = UNSET
    timestamp_formatted: None | str | Unset = UNSET
    term_text: None | str | Unset = UNSET
    suggested_term_for_bank: Any | None | Unset = UNSET
    category: None | str | Unset = UNSET
    category_color: None | str | Unset = UNSET
    category_icon: None | str | Unset = UNSET
    criticality: None | str | Unset = UNSET
    category_threshold: float | None | Unset = UNSET
    category_type: None | str | Unset = UNSET
    nature: None | str | Unset = UNSET
    llm_confidence: float | None | Unset = UNSET
    reason: None | str | Unset = UNSET
    is_valid_context: bool | None | Unset = UNSET
    risk_probability: float | None | Unset = UNSET
    risk_impact: float | None | Unset = UNSET
    category_weight: float | None | Unset = UNSET
    turn_sentiment: None | str | Unset = UNSET
    intensity: Any | None | Unset = UNSET
    mod_applied: float | None | Unset = UNSET
    mac_applied: float | None | Unset = UNSET
    mvad_applied: float | None | Unset = UNSET
    mod_formula: None | str | Unset = UNSET
    mac_details: list[AuditoriaRiscoDetectionItemV2MacDetailsItem] | Unset = UNSET
    calibration_reason: None | str | Unset = UNSET
    final_score: float | None | Unset = UNSET
    final_score_formula: None | str | Unset = UNSET
    conversation_limit: Any | None | Unset = UNSET
    apply_saturation: bool | None | Unset = UNSET
    block_repetition: bool | None | Unset = UNSET
    status: None | str | Unset = UNSET
    effective_impact: float | None | Unset = UNSET
    saturation_factor: float | None | Unset = UNSET
    saturation_formula: None | str | Unset = UNSET
    threshold_formula: None | str | Unset = UNSET
    blocked_formula: None | str | Unset = UNSET
    reconciliation_note: None | str | Unset = UNSET
    violated_frameworks: list[Any] | Unset = UNSET
    citation_fidelity: bool | Unset = True
    subcategory: None | str | Unset = UNSET
    subcategory_label: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        category_label = self.category_label

        category_group = self.category_group

        turn: int | None | Unset
        if isinstance(self.turn, Unset):
            turn = UNSET
        else:
            turn = self.turn

        interlocutor: None | str | Unset
        if isinstance(self.interlocutor, Unset):
            interlocutor = UNSET
        else:
            interlocutor = self.interlocutor

        role: None | str | Unset
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        timestamp_start_s: float | None | Unset
        if isinstance(self.timestamp_start_s, Unset):
            timestamp_start_s = UNSET
        else:
            timestamp_start_s = self.timestamp_start_s

        timestamp_end_s: float | None | Unset
        if isinstance(self.timestamp_end_s, Unset):
            timestamp_end_s = UNSET
        else:
            timestamp_end_s = self.timestamp_end_s

        timestamp_formatted: None | str | Unset
        if isinstance(self.timestamp_formatted, Unset):
            timestamp_formatted = UNSET
        else:
            timestamp_formatted = self.timestamp_formatted

        term_text: None | str | Unset
        if isinstance(self.term_text, Unset):
            term_text = UNSET
        else:
            term_text = self.term_text

        suggested_term_for_bank: Any | None | Unset
        if isinstance(self.suggested_term_for_bank, Unset):
            suggested_term_for_bank = UNSET
        else:
            suggested_term_for_bank = self.suggested_term_for_bank

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        category_color: None | str | Unset
        if isinstance(self.category_color, Unset):
            category_color = UNSET
        else:
            category_color = self.category_color

        category_icon: None | str | Unset
        if isinstance(self.category_icon, Unset):
            category_icon = UNSET
        else:
            category_icon = self.category_icon

        criticality: None | str | Unset
        if isinstance(self.criticality, Unset):
            criticality = UNSET
        else:
            criticality = self.criticality

        category_threshold: float | None | Unset
        if isinstance(self.category_threshold, Unset):
            category_threshold = UNSET
        else:
            category_threshold = self.category_threshold

        category_type: None | str | Unset
        if isinstance(self.category_type, Unset):
            category_type = UNSET
        else:
            category_type = self.category_type

        nature: None | str | Unset
        if isinstance(self.nature, Unset):
            nature = UNSET
        else:
            nature = self.nature

        llm_confidence: float | None | Unset
        if isinstance(self.llm_confidence, Unset):
            llm_confidence = UNSET
        else:
            llm_confidence = self.llm_confidence

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        is_valid_context: bool | None | Unset
        if isinstance(self.is_valid_context, Unset):
            is_valid_context = UNSET
        else:
            is_valid_context = self.is_valid_context

        risk_probability: float | None | Unset
        if isinstance(self.risk_probability, Unset):
            risk_probability = UNSET
        else:
            risk_probability = self.risk_probability

        risk_impact: float | None | Unset
        if isinstance(self.risk_impact, Unset):
            risk_impact = UNSET
        else:
            risk_impact = self.risk_impact

        category_weight: float | None | Unset
        if isinstance(self.category_weight, Unset):
            category_weight = UNSET
        else:
            category_weight = self.category_weight

        turn_sentiment: None | str | Unset
        if isinstance(self.turn_sentiment, Unset):
            turn_sentiment = UNSET
        else:
            turn_sentiment = self.turn_sentiment

        intensity: Any | None | Unset
        if isinstance(self.intensity, Unset):
            intensity = UNSET
        else:
            intensity = self.intensity

        mod_applied: float | None | Unset
        if isinstance(self.mod_applied, Unset):
            mod_applied = UNSET
        else:
            mod_applied = self.mod_applied

        mac_applied: float | None | Unset
        if isinstance(self.mac_applied, Unset):
            mac_applied = UNSET
        else:
            mac_applied = self.mac_applied

        mvad_applied: float | None | Unset
        if isinstance(self.mvad_applied, Unset):
            mvad_applied = UNSET
        else:
            mvad_applied = self.mvad_applied

        mod_formula: None | str | Unset
        if isinstance(self.mod_formula, Unset):
            mod_formula = UNSET
        else:
            mod_formula = self.mod_formula

        mac_details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mac_details, Unset):
            mac_details = []
            for mac_details_item_data in self.mac_details:
                mac_details_item = mac_details_item_data.to_dict()
                mac_details.append(mac_details_item)

        calibration_reason: None | str | Unset
        if isinstance(self.calibration_reason, Unset):
            calibration_reason = UNSET
        else:
            calibration_reason = self.calibration_reason

        final_score: float | None | Unset
        if isinstance(self.final_score, Unset):
            final_score = UNSET
        else:
            final_score = self.final_score

        final_score_formula: None | str | Unset
        if isinstance(self.final_score_formula, Unset):
            final_score_formula = UNSET
        else:
            final_score_formula = self.final_score_formula

        conversation_limit: Any | None | Unset
        if isinstance(self.conversation_limit, Unset):
            conversation_limit = UNSET
        else:
            conversation_limit = self.conversation_limit

        apply_saturation: bool | None | Unset
        if isinstance(self.apply_saturation, Unset):
            apply_saturation = UNSET
        else:
            apply_saturation = self.apply_saturation

        block_repetition: bool | None | Unset
        if isinstance(self.block_repetition, Unset):
            block_repetition = UNSET
        else:
            block_repetition = self.block_repetition

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        effective_impact: float | None | Unset
        if isinstance(self.effective_impact, Unset):
            effective_impact = UNSET
        else:
            effective_impact = self.effective_impact

        saturation_factor: float | None | Unset
        if isinstance(self.saturation_factor, Unset):
            saturation_factor = UNSET
        else:
            saturation_factor = self.saturation_factor

        saturation_formula: None | str | Unset
        if isinstance(self.saturation_formula, Unset):
            saturation_formula = UNSET
        else:
            saturation_formula = self.saturation_formula

        threshold_formula: None | str | Unset
        if isinstance(self.threshold_formula, Unset):
            threshold_formula = UNSET
        else:
            threshold_formula = self.threshold_formula

        blocked_formula: None | str | Unset
        if isinstance(self.blocked_formula, Unset):
            blocked_formula = UNSET
        else:
            blocked_formula = self.blocked_formula

        reconciliation_note: None | str | Unset
        if isinstance(self.reconciliation_note, Unset):
            reconciliation_note = UNSET
        else:
            reconciliation_note = self.reconciliation_note

        violated_frameworks: list[Any] | Unset = UNSET
        if not isinstance(self.violated_frameworks, Unset):
            violated_frameworks = self.violated_frameworks

        citation_fidelity = self.citation_fidelity

        subcategory: None | str | Unset
        if isinstance(self.subcategory, Unset):
            subcategory = UNSET
        else:
            subcategory = self.subcategory

        subcategory_label: None | str | Unset
        if isinstance(self.subcategory_label, Unset):
            subcategory_label = UNSET
        else:
            subcategory_label = self.subcategory_label

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "category_label": category_label,
                "category_group": category_group,
            }
        )
        if turn is not UNSET:
            field_dict["turn"] = turn
        if interlocutor is not UNSET:
            field_dict["interlocutor"] = interlocutor
        if role is not UNSET:
            field_dict["role"] = role
        if timestamp_start_s is not UNSET:
            field_dict["timestamp_start_s"] = timestamp_start_s
        if timestamp_end_s is not UNSET:
            field_dict["timestamp_end_s"] = timestamp_end_s
        if timestamp_formatted is not UNSET:
            field_dict["timestamp_formatted"] = timestamp_formatted
        if term_text is not UNSET:
            field_dict["term_text"] = term_text
        if suggested_term_for_bank is not UNSET:
            field_dict["suggested_term_for_bank"] = suggested_term_for_bank
        if category is not UNSET:
            field_dict["category"] = category
        if category_color is not UNSET:
            field_dict["category_color"] = category_color
        if category_icon is not UNSET:
            field_dict["category_icon"] = category_icon
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if category_threshold is not UNSET:
            field_dict["category_threshold"] = category_threshold
        if category_type is not UNSET:
            field_dict["category_type"] = category_type
        if nature is not UNSET:
            field_dict["nature"] = nature
        if llm_confidence is not UNSET:
            field_dict["llm_confidence"] = llm_confidence
        if reason is not UNSET:
            field_dict["reason"] = reason
        if is_valid_context is not UNSET:
            field_dict["is_valid_context"] = is_valid_context
        if risk_probability is not UNSET:
            field_dict["risk_probability"] = risk_probability
        if risk_impact is not UNSET:
            field_dict["risk_impact"] = risk_impact
        if category_weight is not UNSET:
            field_dict["category_weight"] = category_weight
        if turn_sentiment is not UNSET:
            field_dict["turn_sentiment"] = turn_sentiment
        if intensity is not UNSET:
            field_dict["intensity"] = intensity
        if mod_applied is not UNSET:
            field_dict["mod_applied"] = mod_applied
        if mac_applied is not UNSET:
            field_dict["mac_applied"] = mac_applied
        if mvad_applied is not UNSET:
            field_dict["mvad_applied"] = mvad_applied
        if mod_formula is not UNSET:
            field_dict["mod_formula"] = mod_formula
        if mac_details is not UNSET:
            field_dict["mac_details"] = mac_details
        if calibration_reason is not UNSET:
            field_dict["calibration_reason"] = calibration_reason
        if final_score is not UNSET:
            field_dict["final_score"] = final_score
        if final_score_formula is not UNSET:
            field_dict["final_score_formula"] = final_score_formula
        if conversation_limit is not UNSET:
            field_dict["conversation_limit"] = conversation_limit
        if apply_saturation is not UNSET:
            field_dict["apply_saturation"] = apply_saturation
        if block_repetition is not UNSET:
            field_dict["block_repetition"] = block_repetition
        if status is not UNSET:
            field_dict["status"] = status
        if effective_impact is not UNSET:
            field_dict["effective_impact"] = effective_impact
        if saturation_factor is not UNSET:
            field_dict["saturation_factor"] = saturation_factor
        if saturation_formula is not UNSET:
            field_dict["saturation_formula"] = saturation_formula
        if threshold_formula is not UNSET:
            field_dict["threshold_formula"] = threshold_formula
        if blocked_formula is not UNSET:
            field_dict["blocked_formula"] = blocked_formula
        if reconciliation_note is not UNSET:
            field_dict["reconciliation_note"] = reconciliation_note
        if violated_frameworks is not UNSET:
            field_dict["violated_frameworks"] = violated_frameworks
        if citation_fidelity is not UNSET:
            field_dict["citation_fidelity"] = citation_fidelity
        if subcategory is not UNSET:
            field_dict["subcategory"] = subcategory
        if subcategory_label is not UNSET:
            field_dict["subcategory_label"] = subcategory_label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_detection_item_v2_mac_details_item import (
            AuditoriaRiscoDetectionItemV2MacDetailsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        category_label = d.pop("category_label")

        category_group = d.pop("category_group")

        def _parse_turn(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        turn = _parse_turn(d.pop("turn", UNSET))

        def _parse_interlocutor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interlocutor = _parse_interlocutor(d.pop("interlocutor", UNSET))

        def _parse_role(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_timestamp_start_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        timestamp_start_s = _parse_timestamp_start_s(d.pop("timestamp_start_s", UNSET))

        def _parse_timestamp_end_s(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        timestamp_end_s = _parse_timestamp_end_s(d.pop("timestamp_end_s", UNSET))

        def _parse_timestamp_formatted(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timestamp_formatted = _parse_timestamp_formatted(d.pop("timestamp_formatted", UNSET))

        def _parse_term_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        term_text = _parse_term_text(d.pop("term_text", UNSET))

        def _parse_suggested_term_for_bank(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        suggested_term_for_bank = _parse_suggested_term_for_bank(d.pop("suggested_term_for_bank", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_category_color(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_color = _parse_category_color(d.pop("category_color", UNSET))

        def _parse_category_icon(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_icon = _parse_category_icon(d.pop("category_icon", UNSET))

        def _parse_criticality(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        criticality = _parse_criticality(d.pop("criticality", UNSET))

        def _parse_category_threshold(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        category_threshold = _parse_category_threshold(d.pop("category_threshold", UNSET))

        def _parse_category_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_type = _parse_category_type(d.pop("category_type", UNSET))

        def _parse_nature(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        nature = _parse_nature(d.pop("nature", UNSET))

        def _parse_llm_confidence(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        llm_confidence = _parse_llm_confidence(d.pop("llm_confidence", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_is_valid_context(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_valid_context = _parse_is_valid_context(d.pop("is_valid_context", UNSET))

        def _parse_risk_probability(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        risk_probability = _parse_risk_probability(d.pop("risk_probability", UNSET))

        def _parse_risk_impact(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        risk_impact = _parse_risk_impact(d.pop("risk_impact", UNSET))

        def _parse_category_weight(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        category_weight = _parse_category_weight(d.pop("category_weight", UNSET))

        def _parse_turn_sentiment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        turn_sentiment = _parse_turn_sentiment(d.pop("turn_sentiment", UNSET))

        def _parse_intensity(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        intensity = _parse_intensity(d.pop("intensity", UNSET))

        def _parse_mod_applied(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mod_applied = _parse_mod_applied(d.pop("mod_applied", UNSET))

        def _parse_mac_applied(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mac_applied = _parse_mac_applied(d.pop("mac_applied", UNSET))

        def _parse_mvad_applied(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        mvad_applied = _parse_mvad_applied(d.pop("mvad_applied", UNSET))

        def _parse_mod_formula(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mod_formula = _parse_mod_formula(d.pop("mod_formula", UNSET))

        _mac_details = d.pop("mac_details", UNSET)
        mac_details: list[AuditoriaRiscoDetectionItemV2MacDetailsItem] | Unset = UNSET
        if _mac_details is not UNSET:
            mac_details = []
            for mac_details_item_data in _mac_details:
                mac_details_item = AuditoriaRiscoDetectionItemV2MacDetailsItem.from_dict(mac_details_item_data)

                mac_details.append(mac_details_item)

        def _parse_calibration_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        calibration_reason = _parse_calibration_reason(d.pop("calibration_reason", UNSET))

        def _parse_final_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        final_score = _parse_final_score(d.pop("final_score", UNSET))

        def _parse_final_score_formula(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        final_score_formula = _parse_final_score_formula(d.pop("final_score_formula", UNSET))

        def _parse_conversation_limit(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        conversation_limit = _parse_conversation_limit(d.pop("conversation_limit", UNSET))

        def _parse_apply_saturation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        apply_saturation = _parse_apply_saturation(d.pop("apply_saturation", UNSET))

        def _parse_block_repetition(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        block_repetition = _parse_block_repetition(d.pop("block_repetition", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_effective_impact(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        effective_impact = _parse_effective_impact(d.pop("effective_impact", UNSET))

        def _parse_saturation_factor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        saturation_factor = _parse_saturation_factor(d.pop("saturation_factor", UNSET))

        def _parse_saturation_formula(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        saturation_formula = _parse_saturation_formula(d.pop("saturation_formula", UNSET))

        def _parse_threshold_formula(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        threshold_formula = _parse_threshold_formula(d.pop("threshold_formula", UNSET))

        def _parse_blocked_formula(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        blocked_formula = _parse_blocked_formula(d.pop("blocked_formula", UNSET))

        def _parse_reconciliation_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reconciliation_note = _parse_reconciliation_note(d.pop("reconciliation_note", UNSET))

        violated_frameworks = cast(list[Any], d.pop("violated_frameworks", UNSET))

        citation_fidelity = d.pop("citation_fidelity", UNSET)

        def _parse_subcategory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subcategory = _parse_subcategory(d.pop("subcategory", UNSET))

        def _parse_subcategory_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        subcategory_label = _parse_subcategory_label(d.pop("subcategory_label", UNSET))

        auditoria_risco_detection_item_v2 = cls(
            category_label=category_label,
            category_group=category_group,
            turn=turn,
            interlocutor=interlocutor,
            role=role,
            timestamp_start_s=timestamp_start_s,
            timestamp_end_s=timestamp_end_s,
            timestamp_formatted=timestamp_formatted,
            term_text=term_text,
            suggested_term_for_bank=suggested_term_for_bank,
            category=category,
            category_color=category_color,
            category_icon=category_icon,
            criticality=criticality,
            category_threshold=category_threshold,
            category_type=category_type,
            nature=nature,
            llm_confidence=llm_confidence,
            reason=reason,
            is_valid_context=is_valid_context,
            risk_probability=risk_probability,
            risk_impact=risk_impact,
            category_weight=category_weight,
            turn_sentiment=turn_sentiment,
            intensity=intensity,
            mod_applied=mod_applied,
            mac_applied=mac_applied,
            mvad_applied=mvad_applied,
            mod_formula=mod_formula,
            mac_details=mac_details,
            calibration_reason=calibration_reason,
            final_score=final_score,
            final_score_formula=final_score_formula,
            conversation_limit=conversation_limit,
            apply_saturation=apply_saturation,
            block_repetition=block_repetition,
            status=status,
            effective_impact=effective_impact,
            saturation_factor=saturation_factor,
            saturation_formula=saturation_formula,
            threshold_formula=threshold_formula,
            blocked_formula=blocked_formula,
            reconciliation_note=reconciliation_note,
            violated_frameworks=violated_frameworks,
            citation_fidelity=citation_fidelity,
            subcategory=subcategory,
            subcategory_label=subcategory_label,
        )

        return auditoria_risco_detection_item_v2
