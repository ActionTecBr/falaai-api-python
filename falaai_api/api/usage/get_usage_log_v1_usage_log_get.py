from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.usage_log_response import UsageLogResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    api_key_id: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_api_key_id: None | str | Unset
    if isinstance(api_key_id, Unset):
        json_api_key_id = UNSET
    else:
        json_api_key_id = api_key_id
    params["api_key_id"] = json_api_key_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage/log",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UsageLogResponse | None:
    if response.status_code == 200:
        response_200 = UsageLogResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UsageLogResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    api_key_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UsageLogResponse]:
    """Get Usage Log

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        api_key_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UsageLogResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        api_key_id=api_key_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    api_key_id: None | str | Unset = UNSET,
) -> HTTPValidationError | UsageLogResponse | None:
    """Get Usage Log

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        api_key_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UsageLogResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        api_key_id=api_key_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    api_key_id: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | UsageLogResponse]:
    """Get Usage Log

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        api_key_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UsageLogResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        api_key_id=api_key_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
    api_key_id: None | str | Unset = UNSET,
) -> HTTPValidationError | UsageLogResponse | None:
    """Get Usage Log

    Args:
        page (int | Unset):  Default: 1.
        limit (int | Unset):  Default: 20.
        api_key_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UsageLogResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            api_key_id=api_key_id,
        )
    ).parsed
