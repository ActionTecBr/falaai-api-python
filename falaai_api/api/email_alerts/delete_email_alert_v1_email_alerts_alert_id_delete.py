from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.email_alert_message_response import EmailAlertMessageResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    alert_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/email-alerts/{alert_id}".format(
            alert_id=quote(str(alert_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EmailAlertMessageResponse | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = EmailAlertMessageResponse.from_dict(response.json())

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
) -> Response[EmailAlertMessageResponse | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EmailAlertMessageResponse | HTTPValidationError]:
    """Remover email de alerta

    Args:
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailAlertMessageResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EmailAlertMessageResponse | HTTPValidationError | None:
    """Remover email de alerta

    Args:
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailAlertMessageResponse | HTTPValidationError
    """

    return sync_detailed(
        alert_id=alert_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[EmailAlertMessageResponse | HTTPValidationError]:
    """Remover email de alerta

    Args:
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmailAlertMessageResponse | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        alert_id=alert_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    alert_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> EmailAlertMessageResponse | HTTPValidationError | None:
    """Remover email de alerta

    Args:
        alert_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmailAlertMessageResponse | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            alert_id=alert_id,
            client=client,
        )
    ).parsed
