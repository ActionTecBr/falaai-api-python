from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audio_event import AudioEvent
    from ..models.audio_input_meta import AudioInputMeta
    from ..models.transcription_usage import TranscriptionUsage


T = TypeVar("T", bound="TranscriptionResponse")


@_attrs_define
class TranscriptionResponse:
    """
    Attributes:
        id (str): Unique transcription identifier. Prefix 'tr-' followed by UUID Example:
            tr-550e8400-e29b-41d4-a716-446655440000.
        object_ (str): Returned object type. Always 'transcription' Example: transcription.
        model (str): Model used for transcription. Ex: 'falaai-transcribe-1' Example: falaai-transcribe-1.
        filename (str): Original audio file name uploaded Example: chamada.mp3.
        processed_at (str): Processing datetime in ISO 8601 UTC format Example: 2026-06-25T01:00:35.399252+00:00.
        usage (TranscriptionUsage):
        language (str): ISO 639-3 language code detected in audio. Ex: 'por' (Portuguese), 'eng' (English), 'spa'
            (Spanish) Example: por.
        duration_seconds (float): Total audio duration in seconds Example: 151.04.
        text (str): Full transcription as plain text, including audio events in brackets Example: Oi, Alex. Oi. O,
            Thais- Oi....
        dialog (str): Turn-by-turn formatted transcript with speaker identification and start/end timestamps Example:
            Speaker 1: [00:00:00.540 - 00:00:01.139] Oi, Alex.
            Speaker 2: [00:00:01.940 - 00:00:02.720] Oi....
        audio_events (list[AudioEvent]): List of detected audio events (laughs, sighs, pauses, etc) with timestamps and
            duration
        event_types (list[str]): Unique audio event types found in transcription, alphabetically sorted Example:
            ['[riso]', '[suspiro]'].
        word_count (int): Total number of recognized words in transcription Example: 773.
        input_ (AudioInputMeta):
        language_confidence (float | None | Unset): Language detection confidence level (0.0 to 1.0). Higher is more
            reliable Example: 1.0.
        client_reference_id (None | str | Unset): Client-supplied ID echoed verbatim (if provided in request) Example:
            call-2026-08-30-001.
    """

    id: str
    object_: str
    model: str
    filename: str
    processed_at: str
    usage: TranscriptionUsage
    language: str
    duration_seconds: float
    text: str
    dialog: str
    audio_events: list[AudioEvent]
    event_types: list[str]
    word_count: int
    input_: AudioInputMeta
    language_confidence: float | None | Unset = UNSET
    client_reference_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        model = self.model

        filename = self.filename

        processed_at = self.processed_at

        usage = self.usage.to_dict()

        language = self.language

        duration_seconds = self.duration_seconds

        text = self.text

        dialog = self.dialog

        audio_events = []
        for audio_events_item_data in self.audio_events:
            audio_events_item = audio_events_item_data.to_dict()
            audio_events.append(audio_events_item)

        event_types = self.event_types

        word_count = self.word_count

        input_ = self.input_.to_dict()

        language_confidence: float | None | Unset
        if isinstance(self.language_confidence, Unset):
            language_confidence = UNSET
        else:
            language_confidence = self.language_confidence

        client_reference_id: None | str | Unset
        if isinstance(self.client_reference_id, Unset):
            client_reference_id = UNSET
        else:
            client_reference_id = self.client_reference_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "model": model,
                "filename": filename,
                "processed_at": processed_at,
                "usage": usage,
                "language": language,
                "duration_seconds": duration_seconds,
                "text": text,
                "dialog": dialog,
                "audio_events": audio_events,
                "event_types": event_types,
                "word_count": word_count,
                "input": input_,
            }
        )
        if language_confidence is not UNSET:
            field_dict["language_confidence"] = language_confidence
        if client_reference_id is not UNSET:
            field_dict["client_reference_id"] = client_reference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audio_event import AudioEvent  # noqa: PLC0415
        from ..models.audio_input_meta import AudioInputMeta  # noqa: PLC0415
        from ..models.transcription_usage import TranscriptionUsage  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        object_ = d.pop("object")

        model = d.pop("model")

        filename = d.pop("filename")

        processed_at = d.pop("processed_at")

        usage = TranscriptionUsage.from_dict(d.pop("usage"))

        language = d.pop("language")

        duration_seconds = d.pop("duration_seconds")

        text = d.pop("text")

        dialog = d.pop("dialog")

        audio_events = []
        _audio_events = d.pop("audio_events")
        for audio_events_item_data in _audio_events:
            audio_events_item = AudioEvent.from_dict(audio_events_item_data)

            audio_events.append(audio_events_item)

        event_types = cast(list[str], d.pop("event_types"))

        word_count = d.pop("word_count")

        input_ = AudioInputMeta.from_dict(d.pop("input"))

        def _parse_language_confidence(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        language_confidence = _parse_language_confidence(d.pop("language_confidence", UNSET))

        def _parse_client_reference_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_reference_id = _parse_client_reference_id(d.pop("client_reference_id", UNSET))

        transcription_response = cls(
            id=id,
            object_=object_,
            model=model,
            filename=filename,
            processed_at=processed_at,
            usage=usage,
            language=language,
            duration_seconds=duration_seconds,
            text=text,
            dialog=dialog,
            audio_events=audio_events,
            event_types=event_types,
            word_count=word_count,
            input_=input_,
            language_confidence=language_confidence,
            client_reference_id=client_reference_id,
        )

        transcription_response.additional_properties = d
        return transcription_response

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
