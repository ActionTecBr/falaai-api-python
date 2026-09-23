from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookItem")


@_attrs_define
class WebhookItem:
    """
    Attributes:
        id (str): Webhook id
        user_id (str): Owner user id
        name (str): Webhook name
        url (str): Destination URL
        secret (str): HMAC signing secret
        events (list[str]): Subscribed events
        active (bool): Is active
        retry_enabled (bool): Retry enabled
        created_at (str): ISO 8601 created
        updated_at (str): ISO 8601 updated
        last_delivery_at (None | str | Unset): ISO 8601 of last delivery
        last_status (int | None | Unset): Last HTTP status delivered
        failure_count (int | Unset): Consecutive failures Default: 0.
    """

    id: str
    user_id: str
    name: str
    url: str
    secret: str
    events: list[str]
    active: bool
    retry_enabled: bool
    created_at: str
    updated_at: str
    last_delivery_at: None | str | Unset = UNSET
    last_status: int | None | Unset = UNSET
    failure_count: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        name = self.name

        url = self.url

        secret = self.secret

        events = self.events

        active = self.active

        retry_enabled = self.retry_enabled

        created_at = self.created_at

        updated_at = self.updated_at

        last_delivery_at: None | str | Unset
        if isinstance(self.last_delivery_at, Unset):
            last_delivery_at = UNSET
        else:
            last_delivery_at = self.last_delivery_at

        last_status: int | None | Unset
        if isinstance(self.last_status, Unset):
            last_status = UNSET
        else:
            last_status = self.last_status

        failure_count = self.failure_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "name": name,
                "url": url,
                "secret": secret,
                "events": events,
                "active": active,
                "retry_enabled": retry_enabled,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if last_delivery_at is not UNSET:
            field_dict["last_delivery_at"] = last_delivery_at
        if last_status is not UNSET:
            field_dict["last_status"] = last_status
        if failure_count is not UNSET:
            field_dict["failure_count"] = failure_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        name = d.pop("name")

        url = d.pop("url")

        secret = d.pop("secret")

        events = cast(list[str], d.pop("events"))

        active = d.pop("active")

        retry_enabled = d.pop("retry_enabled")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        def _parse_last_delivery_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_delivery_at = _parse_last_delivery_at(d.pop("last_delivery_at", UNSET))

        def _parse_last_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_status = _parse_last_status(d.pop("last_status", UNSET))

        failure_count = d.pop("failure_count", UNSET)

        webhook_item = cls(
            id=id,
            user_id=user_id,
            name=name,
            url=url,
            secret=secret,
            events=events,
            active=active,
            retry_enabled=retry_enabled,
            created_at=created_at,
            updated_at=updated_at,
            last_delivery_at=last_delivery_at,
            last_status=last_status,
            failure_count=failure_count,
        )

        webhook_item.additional_properties = d
        return webhook_item

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
