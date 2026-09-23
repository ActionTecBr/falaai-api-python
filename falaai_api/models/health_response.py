from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HealthResponse")


@_attrs_define
class HealthResponse:
    """
    Attributes:
        status (str): Overall API status Example: ok.
        version (str): Current API version Example: api_v1.5.2.
        uptime_seconds (int): Uptime in seconds Example: 3600.
        database (bool): Database connection status Example: True.
        phase (str): Development phase Example: development.
        launch_date (str): Expected public launch date Example: 2026-08-01.
    """

    status: str
    version: str
    uptime_seconds: int
    database: bool
    phase: str
    launch_date: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        version = self.version

        uptime_seconds = self.uptime_seconds

        database = self.database

        phase = self.phase

        launch_date = self.launch_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "version": version,
                "uptime_seconds": uptime_seconds,
                "database": database,
                "phase": phase,
                "launch_date": launch_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        version = d.pop("version")

        uptime_seconds = d.pop("uptime_seconds")

        database = d.pop("database")

        phase = d.pop("phase")

        launch_date = d.pop("launch_date")

        health_response = cls(
            status=status,
            version=version,
            uptime_seconds=uptime_seconds,
            database=database,
            phase=phase,
            launch_date=launch_date,
        )

        health_response.additional_properties = d
        return health_response

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
