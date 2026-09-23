from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auditoria_risco_request import AuditoriaRiscoRequest
from ...models.auditoria_risco_v2_response import AuditoriaRiscoV2Response
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: AuditoriaRiscoRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/analyze/auditoriaRisco",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditoriaRiscoV2Response | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = AuditoriaRiscoV2Response.from_dict(response.json())

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
) -> Response[AuditoriaRiscoV2Response | HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuditoriaRiscoRequest,
) -> Response[AuditoriaRiscoV2Response | HTTPValidationError]:
    """ Compliance Risk Audit — conversation compliance analysis

     Analyzes a call transcript for compliance risks. Returns a score (0-100), classification level,
    violations, positives, and a detailed HTML report.

    **Python:**
    ```python
    import httpx

    response = httpx.post(
        'https://api.fala.ai/v1/analyze/auditoriaRisco',
        headers={'Authorization': 'Bearer fai_xxx'},
        json={
            'dialog': 'Speaker 1: [00:00:00.540 - 00:00:01.139] Hi, Alex.',
            'duration_seconds': 151.0,
            'language': 'pt-BR',
            'response_language': 'en-US'
        }
    )
    print(response.json())
    ```

    **cURL:**
    ```bash
    curl https://api.fala.ai/v1/analyze/auditoriaRisco \\
      -H 'Authorization: Bearer fai_xxx' \\
      -H 'Content-Type: application/json' \\
      -d '{
        "dialog": "Speaker 1: [00:00:00.540 - 00:00:01.139] Hi, Alex.",
        "duration_seconds": 151.0,
        "language": "pt-BR",
        "response_language": "en-US"
      }'
    ```

    Args:
        body (AuditoriaRiscoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditoriaRiscoV2Response | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: AuditoriaRiscoRequest,
) -> AuditoriaRiscoV2Response | HTTPValidationError | None:
    """ Compliance Risk Audit — conversation compliance analysis

     Analyzes a call transcript for compliance risks. Returns a score (0-100), classification level,
    violations, positives, and a detailed HTML report.

    **Python:**
    ```python
    import httpx

    response = httpx.post(
        'https://api.fala.ai/v1/analyze/auditoriaRisco',
        headers={'Authorization': 'Bearer fai_xxx'},
        json={
            'dialog': 'Speaker 1: [00:00:00.540 - 00:00:01.139] Hi, Alex.',
            'duration_seconds': 151.0,
            'language': 'pt-BR',
            'response_language': 'en-US'
        }
    )
    print(response.json())
    ```

    **cURL:**
    ```bash
    curl https://api.fala.ai/v1/analyze/auditoriaRisco \\
      -H 'Authorization: Bearer fai_xxx' \\
      -H 'Content-Type: application/json' \\
      -d '{
        "dialog": "Speaker 1: [00:00:00.540 - 00:00:01.139] Hi, Alex.",
        "duration_seconds": 151.0,
        "language": "pt-BR",
        "response_language": "en-US"
      }'
    ```

    Args:
        body (AuditoriaRiscoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditoriaRiscoV2Response | HTTPValidationError
     """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AuditoriaRiscoRequest,
) -> Response[AuditoriaRiscoV2Response | HTTPValidationError]:
    """ Compliance Risk Audit — conversation compliance analysis

     Analyzes a call transcript for compliance risks. Returns a score (0-100), classification level,
    violations, positives, and a detailed HTML report.

    **Python:**
    ```python
    import httpx

    response = httpx.post(
        'https://api.fala.ai/v1/analyze/auditoriaRisco',
        headers={'Authorization': 'Bearer fai_xxx'},
        json={
            'dialog': 'Speaker 1: [00:00:00.540 - 00:00:01.139] Hi, Alex.',
            'duration_seconds': 151.0,
            'language': 'pt-BR',
            'response_language': 'en-US'
        }
    )
    print(response.json())
    ```

    **cURL:**
    ```bash
    curl https://api.fala.ai/v1/analyze/auditoriaRisco \\
      -H 'Authorization: Bearer fai_xxx' \\
      -H 'Content-Type: application/json' \\
      -d '{
        "dialog": "Speaker 1: [00:00:00.540 - 00:00:01.139] Hi, Alex.",
        "duration_seconds": 151.0,
        "language": "pt-BR",
        "response_language": "en-US"
      }'
    ```

    Args:
        body (AuditoriaRiscoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditoriaRiscoV2Response | HTTPValidationError]
     """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AuditoriaRiscoRequest,
) -> AuditoriaRiscoV2Response | HTTPValidationError | None:
    """ Compliance Risk Audit — conversation compliance analysis

     Analyzes a call transcript for compliance risks. Returns a score (0-100), classification level,
    violations, positives, and a detailed HTML report.

    **Python:**
    ```python
    import httpx

    response = httpx.post(
        'https://api.fala.ai/v1/analyze/auditoriaRisco',
        headers={'Authorization': 'Bearer fai_xxx'},
        json={
            'dialog': 'Speaker 1: [00:00:00.540 - 00:00:01.139] Hi, Alex.',
            'duration_seconds': 151.0,
            'language': 'pt-BR',
            'response_language': 'en-US'
        }
    )
    print(response.json())
    ```

    **cURL:**
    ```bash
    curl https://api.fala.ai/v1/analyze/auditoriaRisco \\
      -H 'Authorization: Bearer fai_xxx' \\
      -H 'Content-Type: application/json' \\
      -d '{
        "dialog": "Speaker 1: [00:00:00.540 - 00:00:01.139] Hi, Alex.",
        "duration_seconds": 151.0,
        "language": "pt-BR",
        "response_language": "en-US"
      }'
    ```

    Args:
        body (AuditoriaRiscoRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditoriaRiscoV2Response | HTTPValidationError
     """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
