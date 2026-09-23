from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.email_event import EmailEvent

T = TypeVar("T", bound="CreateEmailAlertRequest")


@_attrs_define
class CreateEmailAlertRequest:
    """
    Attributes:
        name (str): Nome identificador Example: Financeiro.
        email (str): Email destino Example: finance@empresa.com.
        events (list[EmailEvent]): Eventos subscritos Example: ['payment.failed', 'subscription.renewed'].
    """

    name: str
    email: str
    events: list[EmailEvent]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        email = self.email

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "email": email,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        email = d.pop("email")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = EmailEvent(events_item_data)

            events.append(events_item)

        create_email_alert_request = cls(
            name=name,
            email=email,
            events=events,
        )

        create_email_alert_request.additional_properties = d
        return create_email_alert_request

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
