from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.auditoria_risco_request_call_direction_type_0 import AuditoriaRiscoRequestCallDirectionType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.diagnostic_audio_event import DiagnosticAudioEvent
    from ..models.participant import Participant


T = TypeVar("T", bound="AuditoriaRiscoRequest")


@_attrs_define
class AuditoriaRiscoRequest:
    """
    Attributes:
        duration_seconds (float): Total audio duration in seconds. Required. Max 3h (10800s).
        language (str): Language of the transcript being analyzed. Must match the dialog/text language. Accepted: pt-BR,
            en-US, es-ES. Example: pt-BR.
        response_language (str): Language for analysis results (labels, categories, levels, actions, HTML report). Can
            differ from 'language'. Accepted: pt-BR, en-US, es-ES. Example: en-US.
        model (str | Unset): Analysis model. Always 'falaai-auditoria-risco-1' Default: 'falaai-auditoria-risco-1'.
            Example: falaai-auditoria-risco-1.
        text (str | Unset): Plain transcript (fallback if dialog is empty). At least one of 'dialog' or 'text' required.
            Max 300,000 characters Default: ''.
        dialog (str | Unset): Diarized transcript with speaker turns. PRIMARY source. Speaker labels accepted (any
            case): 'Speaker N', 'Interlocutor N', 'Hablante N', 'Locutor N', 'Orador N' (space or underscore). Normalized
            internally to 'Speaker N' in the response. Max 300,000 characters Default: ''. Example: Speaker 1: [00:00:00.540
            - 00:00:01.139] Hi, Alex..
        audio_events (list[DiagnosticAudioEvent] | Unset): Audio events with timestamps (correlated with turns when
            diarization is present)
        call_direction (AuditoriaRiscoRequestCallDirectionType0 | None | Unset): Who originated the call. inbound=client
            called, outbound=company called. If omitted, LLM infers from context. Example: inbound.
        participants (list[Participant] | None | Unset): Explicit participant roles. If omitted, LLM infers from dialog
            (Lei 17). When provided, used as ground truth — no inference. Example: [{'interlocutor': 'Interlocutor 1',
            'name': 'Antonio', 'role': 'client'}, {'interlocutor': 'Interlocutor 2', 'name': 'Maria', 'role': 'agent'}].
        response_format (str | Unset): Response format version. v1=legacy flat PT-BR, v2=structured EN-US blocks.
            Default: 'v2'. Example: v2.
        client_reference_id (None | str | Unset): Optional client-supplied ID echoed verbatim in the response. Use to
            correlate/sync with your system. Accepted charset: [A-Za-z0-9._:-], max 128 chars. Not idempotency. Example:
            call-2026-08-30-001.
    """

    duration_seconds: float
    language: str
    response_language: str
    model: str | Unset = "falaai-auditoria-risco-1"
    text: str | Unset = ""
    dialog: str | Unset = ""
    audio_events: list[DiagnosticAudioEvent] | Unset = UNSET
    call_direction: AuditoriaRiscoRequestCallDirectionType0 | None | Unset = UNSET
    participants: list[Participant] | None | Unset = UNSET
    response_format: str | Unset = "v2"
    client_reference_id: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        duration_seconds = self.duration_seconds

        language = self.language

        response_language = self.response_language

        model = self.model

        text = self.text

        dialog = self.dialog

        audio_events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.audio_events, Unset):
            audio_events = []
            for audio_events_item_data in self.audio_events:
                audio_events_item = audio_events_item_data.to_dict()
                audio_events.append(audio_events_item)

        call_direction: None | str | Unset
        if isinstance(self.call_direction, Unset):
            call_direction = UNSET
        elif isinstance(self.call_direction, AuditoriaRiscoRequestCallDirectionType0):
            call_direction = self.call_direction.value
        else:
            call_direction = self.call_direction

        participants: list[dict[str, Any]] | None | Unset
        if isinstance(self.participants, Unset):
            participants = UNSET
        elif isinstance(self.participants, list):
            participants = []
            for participants_type_0_item_data in self.participants:
                participants_type_0_item = participants_type_0_item_data.to_dict()
                participants.append(participants_type_0_item)

        else:
            participants = self.participants

        response_format = self.response_format

        client_reference_id: None | str | Unset
        if isinstance(self.client_reference_id, Unset):
            client_reference_id = UNSET
        else:
            client_reference_id = self.client_reference_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "duration_seconds": duration_seconds,
                "language": language,
                "response_language": response_language,
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
        if call_direction is not UNSET:
            field_dict["call_direction"] = call_direction
        if participants is not UNSET:
            field_dict["participants"] = participants
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if client_reference_id is not UNSET:
            field_dict["client_reference_id"] = client_reference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnostic_audio_event import DiagnosticAudioEvent  # noqa: PLC0415
        from ..models.participant import Participant  # noqa: PLC0415

        d = dict(src_dict)
        duration_seconds = d.pop("duration_seconds")

        language = d.pop("language")

        response_language = d.pop("response_language")

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

        def _parse_call_direction(data: object) -> AuditoriaRiscoRequestCallDirectionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                call_direction_type_0 = AuditoriaRiscoRequestCallDirectionType0(data)

                return call_direction_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditoriaRiscoRequestCallDirectionType0 | None | Unset, data)

        call_direction = _parse_call_direction(d.pop("call_direction", UNSET))

        def _parse_participants(data: object) -> list[Participant] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                participants_type_0 = []
                _participants_type_0 = data
                for participants_type_0_item_data in _participants_type_0:
                    participants_type_0_item = Participant.from_dict(participants_type_0_item_data)

                    participants_type_0.append(participants_type_0_item)

                return participants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Participant] | None | Unset, data)

        participants = _parse_participants(d.pop("participants", UNSET))

        response_format = d.pop("response_format", UNSET)

        def _parse_client_reference_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_reference_id = _parse_client_reference_id(d.pop("client_reference_id", UNSET))

        auditoria_risco_request = cls(
            duration_seconds=duration_seconds,
            language=language,
            response_language=response_language,
            model=model,
            text=text,
            dialog=dialog,
            audio_events=audio_events,
            call_direction=call_direction,
            participants=participants,
            response_format=response_format,
            client_reference_id=client_reference_id,
        )

        return auditoria_risco_request
