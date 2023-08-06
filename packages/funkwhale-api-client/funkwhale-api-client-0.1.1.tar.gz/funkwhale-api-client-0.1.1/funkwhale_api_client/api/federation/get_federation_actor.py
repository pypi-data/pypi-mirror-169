from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.full_actor import FullActor
from ...types import Response


def _get_kwargs(
    full_username: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/federation/actors/{full_username}/".format(client.base_url, full_username=full_username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[FullActor]:
    if response.status_code == 200:
        response_200 = FullActor.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[FullActor]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    full_username: str,
    *,
    client: AuthenticatedClient,
) -> Response[FullActor]:
    """
    Args:
        full_username (str):

    Returns:
        Response[FullActor]
    """

    kwargs = _get_kwargs(
        full_username=full_username,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    full_username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[FullActor]:
    """
    Args:
        full_username (str):

    Returns:
        Response[FullActor]
    """

    return sync_detailed(
        full_username=full_username,
        client=client,
    ).parsed


async def asyncio_detailed(
    full_username: str,
    *,
    client: AuthenticatedClient,
) -> Response[FullActor]:
    """
    Args:
        full_username (str):

    Returns:
        Response[FullActor]
    """

    kwargs = _get_kwargs(
        full_username=full_username,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    full_username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[FullActor]:
    """
    Args:
        full_username (str):

    Returns:
        Response[FullActor]
    """

    return (
        await asyncio_detailed(
            full_username=full_username,
            client=client,
        )
    ).parsed
