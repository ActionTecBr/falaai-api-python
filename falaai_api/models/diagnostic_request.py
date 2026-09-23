from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnostic_audio_event import DiagnosticAudioEvent


T = TypeVar("T", bound="DiagnosticRequest")


@_attrs_define
class DiagnosticRequest:
    """
    Attributes:
        language (str): Transcript language. Required. Accepted: en-US, pt-BR, es-ES, es-MX, fr-FR, de-DE, it-IT, pt-PT,
            zh-CN, ja-JP, ko-KR, ar-SA, hi-IN, ru-RU, id-ID, tr-TR, nl-NL, pl-PL, vi-VN, th-TH, en-GB Example: pt-BR.
        duration_seconds (float): Total audio duration in seconds. Required. Max 3h (10800s).
        model (str | Unset): Analysis model. Always 'falaai-diagnostic-1' Default: 'falaai-diagnostic-1'. Example:
            falaai-diagnostic-1.
        text (str | Unset): Plain transcript (fallback if dialog is empty). At least one of 'dialog' or 'text' required.
            Max 300,000 characters Default: ''.
        dialog (str | Unset): Diarized transcript with speaker turns. PRIMARY source. At least one of 'dialog' or 'text'
            required. Speaker labels accepted (any case): 'Speaker N', 'Interlocutor N', 'Hablante N', 'Locutor N', 'Orador
            N' (space or underscore). Normalized internally to 'Speaker N' in the response. Max 300,000 characters Default:
            ''. Example: Speaker 1: [00:00:00.540 - 00:00:01.139] Hi, Alex..
        audio_events (list[DiagnosticAudioEvent] | Unset): Detected audio events with timestamps (required when using
            dialog)
        client_reference_id (None | str | Unset): Optional client-supplied ID echoed verbatim in the response. Use to
            correlate/sync with your system. Accepted charset: [A-Za-z0-9._:-], max 128 chars. Not idempotency. Example:
            call-2026-08-30-001.
    """

    language: str
    duration_seconds: float
    model: str | Unset = "falaai-diagnostic-1"
    text: str | Unset = ""
    dialog: str | Unset = ""
    audio_events: list[DiagnosticAudioEvent] | Unset = UNSET
    client_reference_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        duration_seconds = self.duration_seconds

        model = self.model

        text = self.text

        dialog = self.dialog

        audio_events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.audio_events, Unset):
            audio_events = []
            for audio_events_item_data in self.audio_events:
                audio_events_item = audio_events_item_data.to_dict()
                audio_events.append(audio_events_item)

        client_reference_id: None | str | Unset
        if isinstance(self.client_reference_id, Unset):
            client_reference_id = UNSET
        else:
            client_reference_id = self.client_reference_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "language": language,
                "duration_seconds": duration_seconds,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if text is not UNSET:
            field_dict["text"] = text
        if dialog is not UNSET:
            field_dict["dialog"] = dialog
        if audio_events is not UNSET:
            field_dict["audio_events"] = audio_events
        if client_reference_id is not UNSET:
            field_dict["client_reference_id"] = client_reference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnostic_audio_event import DiagnosticAudioEvent  # noqa: PLC0415

        d = dict(src_dict)
        language = d.pop("language")

        duration_seconds = d.pop("duration_seconds")

        model = d.pop("model", UNSET)

        text = d.pop("text", UNSET)

        dialog = d.pop("dialog", UNSET)

        _audio_events = d.pop("audio_events", UNSET)
        audio_events: list[DiagnosticAudioEvent] | Unset = UNSET
        if _audio_events is not UNSET:
            audio_events = []
            for audio_events_item_data in _audio_events:
                audio_events_item = DiagnosticAudioEvent.from_dict(audio_events_item_data)

                audio_events.append(audio_events_item)

        def _parse_client_reference_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_reference_id = _parse_client_reference_id(d.pop("client_reference_id", UNSET))

        diagnostic_request = cls(
            language=language,
            duration_seconds=duration_seconds,
            model=model,
            text=text,
            dialog=dialog,
            audio_events=audio_events,
            client_reference_id=client_reference_id,
        )

        return diagnostic_request
