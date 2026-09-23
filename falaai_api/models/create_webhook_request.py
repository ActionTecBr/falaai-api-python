from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_event import WebhookEvent
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookRequest")


@_attrs_define
class CreateWebhookRequest:
    """
    Attributes:
        name (str): Nome identificador do webhook Example: Alertas FalaAI.
        url (str): URL HTTPS que recebera POST com HMAC FalaAI-Signature Example:
            https://webhook.site/00000000-0000-0000-0000-000000000000.
        events (list[WebhookEvent]): Eventos subscritos (10 alertas) Example: ['credits.low', 'credits.exhausted',
            'payment.failed'].
        retry_enabled (bool | Unset): Retry exponencial 5 tentativas quando true (false=1 tentativa) Default: False.
            Example: False.
    """

    name: str
    url: str
    events: list[WebhookEvent]
    retry_enabled: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        url = self.url

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        retry_enabled = self.retry_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "url": url,
                "events": events,
            }
        )
        if retry_enabled is not UNSET:
            field_dict["retry_enabled"] = retry_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        url = d.pop("url")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = WebhookEvent(events_item_data)

            events.append(events_item)

        retry_enabled = d.pop("retry_enabled", UNSET)

        create_webhook_request = cls(
            name=name,
            url=url,
            events=events,
            retry_enabled=retry_enabled,
        )

        create_webhook_request.additional_properties = d
        return create_webhook_request

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
