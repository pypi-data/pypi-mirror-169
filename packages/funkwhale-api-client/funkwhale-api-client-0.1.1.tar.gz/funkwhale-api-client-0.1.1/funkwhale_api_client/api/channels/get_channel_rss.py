from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.channel import Channel
from ...types import Response


def _get_kwargs(
    composite: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/channels/{composite}/rss/".format(client.base_url, composite=composite)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Channel]:
    if response.status_code == 200:
        response_200 = Channel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Channel]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    composite: str,
    *,
    client: AuthenticatedClient,
) -> Response[Channel]:
    """
    Args:
        composite (str):

    Returns:
        Response[Channel]
    """

    kwargs = _get_kwargs(
        composite=composite,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    composite: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Channel]:
    """
    Args:
        composite (str):

    Returns:
        Response[Channel]
    """

    return sync_detailed(
        composite=composite,
        client=client,
    ).parsed


async def asyncio_detailed(
    composite: str,
    *,
    client: AuthenticatedClient,
) -> Response[Channel]:
    """
    Args:
        composite (str):

    Returns:
        Response[Channel]
    """

    kwargs = _get_kwargs(
        composite=composite,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    composite: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Channel]:
    """
    Args:
        composite (str):

    Returns:
        Response[Channel]
    """

    return (
        await asyncio_detailed(
            composite=composite,
            client=client,
        )
    ).parsed
