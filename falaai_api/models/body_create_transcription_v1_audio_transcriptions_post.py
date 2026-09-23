from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="BodyCreateTranscriptionV1AudioTranscriptionsPost")


@_attrs_define
class BodyCreateTranscriptionV1AudioTranscriptionsPost:
    """
    Attributes:
        file (File):
        model (str | Unset):  Default: 'falaai-transcribe-1'.
        language (str | Unset):  Default: 'pt'.
        client_reference_id (str | Unset): Optional client-supplied ID echoed verbatim in the response. Use to
            correlate/sync with your system. Accepted charset: [A-Za-z0-9._:-]. Not idempotency.
    """

    file: File
    model: str | Unset = "falaai-transcribe-1"
    language: str | Unset = "pt"
    client_reference_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        model = self.model

        language = self.language

        client_reference_id = self.client_reference_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if language is not UNSET:
            field_dict["language"] = language
        if client_reference_id is not UNSET:
            field_dict["client_reference_id"] = client_reference_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.model, Unset):
            files.append(("model", (None, str(self.model).encode(), "text/plain")))

        if not isinstance(self.language, Unset):
            files.append(("language", (None, str(self.language).encode(), "text/plain")))

        if not isinstance(self.client_reference_id, Unset):
            files.append(("client_reference_id", (None, str(self.client_reference_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(payload=BytesIO(d.pop("file")))

        model = d.pop("model", UNSET)

        language = d.pop("language", UNSET)

        client_reference_id = d.pop("client_reference_id", UNSET)

        body_create_transcription_v1_audio_transcriptions_post = cls(
            file=file,
            model=model,
            language=language,
            client_reference_id=client_reference_id,
        )

        body_create_transcription_v1_audio_transcriptions_post.additional_properties = d
        return body_create_transcription_v1_audio_transcriptions_post

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
