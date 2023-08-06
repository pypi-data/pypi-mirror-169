from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_listening_list import PaginatedListeningList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/history/listenings/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["domain"] = domain

    params["hidden"] = hidden

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["scope"] = scope

    params["username"] = username

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedListeningList]:
    if response.status_code == 200:
        response_200 = PaginatedListeningList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedListeningList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedListeningList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        scope (Union[Unset, None, str]):
        username (Union[Unset, None, str]):

    Returns:
        Response[PaginatedListeningList]
    """

    kwargs = _get_kwargs(
        client=client,
        domain=domain,
        hidden=hidden,
        ordering=ordering,
        page=page,
        page_size=page_size,
        scope=scope,
        username=username,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedListeningList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        scope (Union[Unset, None, str]):
        username (Union[Unset, None, str]):

    Returns:
        Response[PaginatedListeningList]
    """

    return sync_detailed(
        client=client,
        domain=domain,
        hidden=hidden,
        ordering=ordering,
        page=page,
        page_size=page_size,
        scope=scope,
        username=username,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedListeningList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        scope (Union[Unset, None, str]):
        username (Union[Unset, None, str]):

    Returns:
        Response[PaginatedListeningList]
    """

    kwargs = _get_kwargs(
        client=client,
        domain=domain,
        hidden=hidden,
        ordering=ordering,
        page=page,
        page_size=page_size,
        scope=scope,
        username=username,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    username: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedListeningList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        scope (Union[Unset, None, str]):
        username (Union[Unset, None, str]):

    Returns:
        Response[PaginatedListeningList]
    """

    return (
        await asyncio_detailed(
            client=client,
            domain=domain,
            hidden=hidden,
            ordering=ordering,
            page=page,
            page_size=page_size,
            scope=scope,
            username=username,
        )
    ).parsed
