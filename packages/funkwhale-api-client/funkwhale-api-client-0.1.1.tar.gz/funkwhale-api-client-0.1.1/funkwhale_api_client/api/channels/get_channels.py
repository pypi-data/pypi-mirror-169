from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.get_channels_ordering_item import GetChannelsOrderingItem
from ...models.paginated_channel_list import PaginatedChannelList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    external: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, List[GetChannelsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    subscribed: Union[Unset, None, bool] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/channels/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["external"] = external

    params["hidden"] = hidden

    json_ordering: Union[Unset, None, List[str]] = UNSET
    if not isinstance(ordering, Unset):
        if ordering is None:
            json_ordering = None
        else:
            json_ordering = []
            for ordering_item_data in ordering:
                ordering_item = ordering_item_data.value

                json_ordering.append(ordering_item)

    params["ordering"] = json_ordering

    params["page"] = page

    params["page_size"] = page_size

    params["q"] = q

    params["scope"] = scope

    params["subscribed"] = subscribed

    json_tag: Union[Unset, None, List[str]] = UNSET
    if not isinstance(tag, Unset):
        if tag is None:
            json_tag = None
        else:
            json_tag = tag

    params["tag"] = json_tag

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedChannelList]:
    if response.status_code == 200:
        response_200 = PaginatedChannelList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedChannelList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    external: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, List[GetChannelsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    subscribed: Union[Unset, None, bool] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Response[PaginatedChannelList]:
    """
    Args:
        external (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, List[GetChannelsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        subscribed (Union[Unset, None, bool]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedChannelList]
    """

    kwargs = _get_kwargs(
        client=client,
        external=external,
        hidden=hidden,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        scope=scope,
        subscribed=subscribed,
        tag=tag,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    external: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, List[GetChannelsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    subscribed: Union[Unset, None, bool] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PaginatedChannelList]:
    """
    Args:
        external (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, List[GetChannelsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        subscribed (Union[Unset, None, bool]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedChannelList]
    """

    return sync_detailed(
        client=client,
        external=external,
        hidden=hidden,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        scope=scope,
        subscribed=subscribed,
        tag=tag,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    external: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, List[GetChannelsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    subscribed: Union[Unset, None, bool] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Response[PaginatedChannelList]:
    """
    Args:
        external (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, List[GetChannelsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        subscribed (Union[Unset, None, bool]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedChannelList]
    """

    kwargs = _get_kwargs(
        client=client,
        external=external,
        hidden=hidden,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        scope=scope,
        subscribed=subscribed,
        tag=tag,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    external: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, List[GetChannelsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    subscribed: Union[Unset, None, bool] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PaginatedChannelList]:
    """
    Args:
        external (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, List[GetChannelsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        subscribed (Union[Unset, None, bool]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedChannelList]
    """

    return (
        await asyncio_detailed(
            client=client,
            external=external,
            hidden=hidden,
            ordering=ordering,
            page=page,
            page_size=page_size,
            q=q,
            scope=scope,
            subscribed=subscribed,
            tag=tag,
        )
    ).parsed
