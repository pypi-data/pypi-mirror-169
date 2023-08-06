from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.node_info_20 import NodeInfo20
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/v1/instance/nodeinfo/2.0/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[NodeInfo20]:
    if response.status_code == 200:
        response_200 = NodeInfo20.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[NodeInfo20]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[NodeInfo20]:
    """
    Returns:
        Response[NodeInfo20]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[NodeInfo20]:
    """
    Returns:
        Response[NodeInfo20]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[NodeInfo20]:
    """
    Returns:
        Response[NodeInfo20]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[NodeInfo20]:
    """
    Returns:
        Response[NodeInfo20]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
