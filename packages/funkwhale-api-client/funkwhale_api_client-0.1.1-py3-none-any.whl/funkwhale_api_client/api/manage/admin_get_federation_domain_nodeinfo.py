from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.manage_domain import ManageDomain
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/federation/domains/{name}/nodeinfo/".format(client.base_url, name=name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ManageDomain]:
    if response.status_code == 200:
        response_200 = ManageDomain.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ManageDomain]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[ManageDomain]:
    """
    Args:
        name (str):

    Returns:
        Response[ManageDomain]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ManageDomain]:
    """
    Args:
        name (str):

    Returns:
        Response[ManageDomain]
    """

    return sync_detailed(
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[ManageDomain]:
    """
    Args:
        name (str):

    Returns:
        Response[ManageDomain]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ManageDomain]:
    """
    Args:
        name (str):

    Returns:
        Response[ManageDomain]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
        )
    ).parsed
