from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.webhook_list_response import WebhookListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | WebhookListResponse | None:
    if response.status_code == 200:
        response_200 = WebhookListResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | WebhookListResponse]:
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
) -> Response[HTTPValidationError | WebhookListResponse]:
    """Listar webhooks de alertas

     Lista webhooks do usuario autenticado (10 alertas). Paginado. Inclui o secret da assinatura da URL
    (sempre visivel ao dono).

    Args:
        page (int | Unset): Pagina (1-indexed) Default: 1.
        limit (int | Unset): Itens por pagina (max 100) Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WebhookListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
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
) -> HTTPValidationError | WebhookListResponse | None:
    """Listar webhooks de alertas

     Lista webhooks do usuario autenticado (10 alertas). Paginado. Inclui o secret da assinatura da URL
    (sempre visivel ao dono).

    Args:
        page (int | Unset): Pagina (1-indexed) Default: 1.
        limit (int | Unset): Itens por pagina (max 100) Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WebhookListResponse
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> Response[HTTPValidationError | WebhookListResponse]:
    """Listar webhooks de alertas

     Lista webhooks do usuario autenticado (10 alertas). Paginado. Inclui o secret da assinatura da URL
    (sempre visivel ao dono).

    Args:
        page (int | Unset): Pagina (1-indexed) Default: 1.
        limit (int | Unset): Itens por pagina (max 100) Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | WebhookListResponse]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 1,
    limit: int | Unset = 20,
) -> HTTPValidationError | WebhookListResponse | None:
    """Listar webhooks de alertas

     Lista webhooks do usuario autenticado (10 alertas). Paginado. Inclui o secret da assinatura da URL
    (sempre visivel ao dono).

    Args:
        page (int | Unset): Pagina (1-indexed) Default: 1.
        limit (int | Unset): Itens por pagina (max 100) Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | WebhookListResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
        )
    ).parsed
