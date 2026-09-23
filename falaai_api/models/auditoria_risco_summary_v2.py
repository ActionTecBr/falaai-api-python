from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditoriaRiscoSummaryV2")


@_attrs_define
class AuditoriaRiscoSummaryV2:
    """
    Attributes:
        total_turns (int | None | Unset): Total turns
        total_calibrated (int | None | Unset): Total calibrated detections
        active (int | None | Unset): Active detections
        tolerated (int | None | Unset): Tolerated detections
        blocked (int | None | Unset): Blocked detections
        audio_events_used (int | None | Unset): Audio events used
        audio_events_aggravated (int | None | Unset): Audio events aggravated
        mac_audio_applied (Any | None | Unset): MAC audio applied
        mvad_applied (Any | None | Unset): MVAD applied
        total_participants (int | None | Unset): Total participants
        total_agents (int | None | Unset): Total agents
        total_clients (int | None | Unset): Total clients
        total_bots (int | None | Unset): Total bots
        total_unknown (int | None | Unset): Total unknown
        client_risk_alerts_count (int | None | Unset): Client risk alerts count
        client_behavior_alerts_count (int | None | Unset): Client behavior alerts count
    """

    total_turns: int | None | Unset = UNSET
    total_calibrated: int | None | Unset = UNSET
    active: int | None | Unset = UNSET
    tolerated: int | None | Unset = UNSET
    blocked: int | None | Unset = UNSET
    audio_events_used: int | None | Unset = UNSET
    audio_events_aggravated: int | None | Unset = UNSET
    mac_audio_applied: Any | None | Unset = UNSET
    mvad_applied: Any | None | Unset = UNSET
    total_participants: int | None | Unset = UNSET
    total_agents: int | None | Unset = UNSET
    total_clients: int | None | Unset = UNSET
    total_bots: int | None | Unset = UNSET
    total_unknown: int | None | Unset = UNSET
    client_risk_alerts_count: int | None | Unset = UNSET
    client_behavior_alerts_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_turns: int | None | Unset
        if isinstance(self.total_turns, Unset):
            total_turns = UNSET
        else:
            total_turns = self.total_turns

        total_calibrated: int | None | Unset
        if isinstance(self.total_calibrated, Unset):
            total_calibrated = UNSET
        else:
            total_calibrated = self.total_calibrated

        active: int | None | Unset
        if isinstance(self.active, Unset):
            active = UNSET
        else:
            active = self.active

        tolerated: int | None | Unset
        if isinstance(self.tolerated, Unset):
            tolerated = UNSET
        else:
            tolerated = self.tolerated

        blocked: int | None | Unset
        if isinstance(self.blocked, Unset):
            blocked = UNSET
        else:
            blocked = self.blocked

        audio_events_used: int | None | Unset
        if isinstance(self.audio_events_used, Unset):
            audio_events_used = UNSET
        else:
            audio_events_used = self.audio_events_used

        audio_events_aggravated: int | None | Unset
        if isinstance(self.audio_events_aggravated, Unset):
            audio_events_aggravated = UNSET
        else:
            audio_events_aggravated = self.audio_events_aggravated

        mac_audio_applied: Any | None | Unset
        if isinstance(self.mac_audio_applied, Unset):
            mac_audio_applied = UNSET
        else:
            mac_audio_applied = self.mac_audio_applied

        mvad_applied: Any | None | Unset
        if isinstance(self.mvad_applied, Unset):
            mvad_applied = UNSET
        else:
            mvad_applied = self.mvad_applied

        total_participants: int | None | Unset
        if isinstance(self.total_participants, Unset):
            total_participants = UNSET
        else:
            total_participants = self.total_participants

        total_agents: int | None | Unset
        if isinstance(self.total_agents, Unset):
            total_agents = UNSET
        else:
            total_agents = self.total_agents

        total_clients: int | None | Unset
        if isinstance(self.total_clients, Unset):
            total_clients = UNSET
        else:
            total_clients = self.total_clients

        total_bots: int | None | Unset
        if isinstance(self.total_bots, Unset):
            total_bots = UNSET
        else:
            total_bots = self.total_bots

        total_unknown: int | None | Unset
        if isinstance(self.total_unknown, Unset):
            total_unknown = UNSET
        else:
            total_unknown = self.total_unknown

        client_risk_alerts_count: int | None | Unset
        if isinstance(self.client_risk_alerts_count, Unset):
            client_risk_alerts_count = UNSET
        else:
            client_risk_alerts_count = self.client_risk_alerts_count

        client_behavior_alerts_count: int | None | Unset
        if isinstance(self.client_behavior_alerts_count, Unset):
            client_behavior_alerts_count = UNSET
        else:
            client_behavior_alerts_count = self.client_behavior_alerts_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_turns is not UNSET:
            field_dict["total_turns"] = total_turns
        if total_calibrated is not UNSET:
            field_dict["total_calibrated"] = total_calibrated
        if active is not UNSET:
            field_dict["active"] = active
        if tolerated is not UNSET:
            field_dict["tolerated"] = tolerated
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if audio_events_used is not UNSET:
            field_dict["audio_events_used"] = audio_events_used
        if audio_events_aggravated is not UNSET:
            field_dict["audio_events_aggravated"] = audio_events_aggravated
        if mac_audio_applied is not UNSET:
            field_dict["mac_audio_applied"] = mac_audio_applied
        if mvad_applied is not UNSET:
            field_dict["mvad_applied"] = mvad_applied
        if total_participants is not UNSET:
            field_dict["total_participants"] = total_participants
        if total_agents is not UNSET:
            field_dict["total_agents"] = total_agents
        if total_clients is not UNSET:
            field_dict["total_clients"] = total_clients
        if total_bots is not UNSET:
            field_dict["total_bots"] = total_bots
        if total_unknown is not UNSET:
            field_dict["total_unknown"] = total_unknown
        if client_risk_alerts_count is not UNSET:
            field_dict["client_risk_alerts_count"] = client_risk_alerts_count
        if client_behavior_alerts_count is not UNSET:
            field_dict["client_behavior_alerts_count"] = client_behavior_alerts_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_total_turns(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_turns = _parse_total_turns(d.pop("total_turns", UNSET))

        def _parse_total_calibrated(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_calibrated = _parse_total_calibrated(d.pop("total_calibrated", UNSET))

        def _parse_active(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        active = _parse_active(d.pop("active", UNSET))

        def _parse_tolerated(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tolerated = _parse_tolerated(d.pop("tolerated", UNSET))

        def _parse_blocked(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        blocked = _parse_blocked(d.pop("blocked", UNSET))

        def _parse_audio_events_used(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_events_used = _parse_audio_events_used(d.pop("audio_events_used", UNSET))

        def _parse_audio_events_aggravated(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_events_aggravated = _parse_audio_events_aggravated(d.pop("audio_events_aggravated", UNSET))

        def _parse_mac_audio_applied(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        mac_audio_applied = _parse_mac_audio_applied(d.pop("mac_audio_applied", UNSET))

        def _parse_mvad_applied(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        mvad_applied = _parse_mvad_applied(d.pop("mvad_applied", UNSET))

        def _parse_total_participants(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_participants = _parse_total_participants(d.pop("total_participants", UNSET))

        def _parse_total_agents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_agents = _parse_total_agents(d.pop("total_agents", UNSET))

        def _parse_total_clients(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_clients = _parse_total_clients(d.pop("total_clients", UNSET))

        def _parse_total_bots(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_bots = _parse_total_bots(d.pop("total_bots", UNSET))

        def _parse_total_unknown(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_unknown = _parse_total_unknown(d.pop("total_unknown", UNSET))

        def _parse_client_risk_alerts_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        client_risk_alerts_count = _parse_client_risk_alerts_count(d.pop("client_risk_alerts_count", UNSET))

        def _parse_client_behavior_alerts_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        client_behavior_alerts_count = _parse_client_behavior_alerts_count(d.pop("client_behavior_alerts_count", UNSET))

        auditoria_risco_summary_v2 = cls(
            total_turns=total_turns,
            total_calibrated=total_calibrated,
            active=active,
            tolerated=tolerated,
            blocked=blocked,
            audio_events_used=audio_events_used,
            audio_events_aggravated=audio_events_aggravated,
            mac_audio_applied=mac_audio_applied,
            mvad_applied=mvad_applied,
            total_participants=total_participants,
            total_agents=total_agents,
            total_clients=total_clients,
            total_bots=total_bots,
            total_unknown=total_unknown,
            client_risk_alerts_count=client_risk_alerts_count,
            client_behavior_alerts_count=client_behavior_alerts_count,
        )

        auditoria_risco_summary_v2.additional_properties = d
        return auditoria_risco_summary_v2

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
