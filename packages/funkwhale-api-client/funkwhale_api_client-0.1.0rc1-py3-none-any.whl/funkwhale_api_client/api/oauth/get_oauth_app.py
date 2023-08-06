from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.application import Application
from ...types import Response


def _get_kwargs(
    client_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/oauth/apps/{client_id}/".format(client.base_url, client_id=client_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Application]:
    if response.status_code == 200:
        response_200 = Application.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Application]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Application]:
    """
    Args:
        client_id (str):

    Returns:
        Response[Application]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    client_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Application]:
    """
    Args:
        client_id (str):

    Returns:
        Response[Application]
    """

    return sync_detailed(
        client_id=client_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Application]:
    """
    Args:
        client_id (str):

    Returns:
        Response[Application]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    client_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Application]:
    """
    Args:
        client_id (str):

    Returns:
        Response[Application]
    """

    return (
        await asyncio_detailed(
            client_id=client_id,
            client=client,
        )
    ).parsed
