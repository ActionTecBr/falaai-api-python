from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.usage_by_key_item import UsageByKeyItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    key_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_key_id: None | str | Unset
    if isinstance(key_id, Unset):
        json_key_id = UNSET
    else:
        json_key_id = key_id
    params["key_id"] = json_key_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage/by-key",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | list[UsageByKeyItem] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UsageByKeyItem.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | list[UsageByKeyItem]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    key_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[UsageByKeyItem]]:
    """Get Usage By Key

    Args:
        key_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[UsageByKeyItem]]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    key_id: None | str | Unset = UNSET,
) -> HTTPValidationError | list[UsageByKeyItem] | None:
    """Get Usage By Key

    Args:
        key_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[UsageByKeyItem]
    """

    return sync_detailed(
        client=client,
        key_id=key_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    key_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | list[UsageByKeyItem]]:
    """Get Usage By Key

    Args:
        key_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | list[UsageByKeyItem]]
    """

    kwargs = _get_kwargs(
        key_id=key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    key_id: None | str | Unset = UNSET,
) -> HTTPValidationError | list[UsageByKeyItem] | None:
    """Get Usage By Key

    Args:
        key_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | list[UsageByKeyItem]
    """

    return (
        await asyncio_detailed(
            client=client,
            key_id=key_id,
        )
    ).parsed
