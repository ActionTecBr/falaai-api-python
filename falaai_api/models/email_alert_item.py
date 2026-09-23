from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmailAlertItem")


@_attrs_define
class EmailAlertItem:
    """
    Attributes:
        id (str): Email alert id
        user_id (str): Owner user id
        name (str): Email alert name
        email (str): Destination email
        events (list[str]): Subscribed events
        active (bool): Is active
        created_at (str): ISO 8601 created
        updated_at (str): ISO 8601 updated
    """

    id: str
    user_id: str
    name: str
    email: str
    events: list[str]
    active: bool
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        name = self.name

        email = self.email

        events = self.events

        active = self.active

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "name": name,
                "email": email,
                "events": events,
                "active": active,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        name = d.pop("name")

        email = d.pop("email")

        events = cast(list[str], d.pop("events"))

        active = d.pop("active")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        email_alert_item = cls(
            id=id,
            user_id=user_id,
            name=name,
            email=email,
            events=events,
            active=active,
            created_at=created_at,
            updated_at=updated_at,
        )

        email_alert_item.additional_properties = d
        return email_alert_item

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
