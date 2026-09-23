from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_timeline_v2_audio_events_item import AuditoriaRiscoTimelineV2AudioEventsItem
    from ..models.auditoria_risco_timeline_v2_audio_groups_found_item import (
        AuditoriaRiscoTimelineV2AudioGroupsFoundItem,
    )
    from ..models.auditoria_risco_timeline_v2_turns_sentiment_item import AuditoriaRiscoTimelineV2TurnsSentimentItem


T = TypeVar("T", bound="AuditoriaRiscoTimelineV2")


@_attrs_define
class AuditoriaRiscoTimelineV2:
    """
    Attributes:
        turns_sentiment (list[AuditoriaRiscoTimelineV2TurnsSentimentItem] | Unset): Per-turn sentiment
        audio_events (list[AuditoriaRiscoTimelineV2AudioEventsItem] | Unset): Audio events (i18n)
        audio_groups_found (list[AuditoriaRiscoTimelineV2AudioGroupsFoundItem] | Unset): Audio groups found
    """

    turns_sentiment: list[AuditoriaRiscoTimelineV2TurnsSentimentItem] | Unset = UNSET
    audio_events: list[AuditoriaRiscoTimelineV2AudioEventsItem] | Unset = UNSET
    audio_groups_found: list[AuditoriaRiscoTimelineV2AudioGroupsFoundItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        turns_sentiment: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.turns_sentiment, Unset):
            turns_sentiment = []
            for turns_sentiment_item_data in self.turns_sentiment:
                turns_sentiment_item = turns_sentiment_item_data.to_dict()
                turns_sentiment.append(turns_sentiment_item)

        audio_events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.audio_events, Unset):
            audio_events = []
            for audio_events_item_data in self.audio_events:
                audio_events_item = audio_events_item_data.to_dict()
                audio_events.append(audio_events_item)

        audio_groups_found: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.audio_groups_found, Unset):
            audio_groups_found = []
            for audio_groups_found_item_data in self.audio_groups_found:
                audio_groups_found_item = audio_groups_found_item_data.to_dict()
                audio_groups_found.append(audio_groups_found_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if turns_sentiment is not UNSET:
            field_dict["turns_sentiment"] = turns_sentiment
        if audio_events is not UNSET:
            field_dict["audio_events"] = audio_events
        if audio_groups_found is not UNSET:
            field_dict["audio_groups_found"] = audio_groups_found

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_timeline_v2_audio_events_item import (
            AuditoriaRiscoTimelineV2AudioEventsItem,  # noqa: PLC0415
        )
        from ..models.auditoria_risco_timeline_v2_audio_groups_found_item import (
            AuditoriaRiscoTimelineV2AudioGroupsFoundItem,  # noqa: PLC0415
        )
        from ..models.auditoria_risco_timeline_v2_turns_sentiment_item import (
            AuditoriaRiscoTimelineV2TurnsSentimentItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _turns_sentiment = d.pop("turns_sentiment", UNSET)
        turns_sentiment: list[AuditoriaRiscoTimelineV2TurnsSentimentItem] | Unset = UNSET
        if _turns_sentiment is not UNSET:
            turns_sentiment = []
            for turns_sentiment_item_data in _turns_sentiment:
                turns_sentiment_item = AuditoriaRiscoTimelineV2TurnsSentimentItem.from_dict(turns_sentiment_item_data)

                turns_sentiment.append(turns_sentiment_item)

        _audio_events = d.pop("audio_events", UNSET)
        audio_events: list[AuditoriaRiscoTimelineV2AudioEventsItem] | Unset = UNSET
        if _audio_events is not UNSET:
            audio_events = []
            for audio_events_item_data in _audio_events:
                audio_events_item = AuditoriaRiscoTimelineV2AudioEventsItem.from_dict(audio_events_item_data)

                audio_events.append(audio_events_item)

        _audio_groups_found = d.pop("audio_groups_found", UNSET)
        audio_groups_found: list[AuditoriaRiscoTimelineV2AudioGroupsFoundItem] | Unset = UNSET
        if _audio_groups_found is not UNSET:
            audio_groups_found = []
            for audio_groups_found_item_data in _audio_groups_found:
                audio_groups_found_item = AuditoriaRiscoTimelineV2AudioGroupsFoundItem.from_dict(
                    audio_groups_found_item_data
                )

                audio_groups_found.append(audio_groups_found_item)

        auditoria_risco_timeline_v2 = cls(
            turns_sentiment=turns_sentiment,
            audio_events=audio_events,
            audio_groups_found=audio_groups_found,
        )

        return auditoria_risco_timeline_v2
