from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.get_albums_ordering_item import GetAlbumsOrderingItem
from ...models.paginated_album_list import PaginatedAlbumList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    artist: Union[Unset, None, int] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    content_category: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetAlbumsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/albums/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["artist"] = artist

    params["channel"] = channel

    params["content_category"] = content_category

    params["hidden"] = hidden

    params["include_channels"] = include_channels

    params["library"] = library

    params["mbid"] = mbid

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

    params["playable"] = playable

    params["q"] = q

    params["related"] = related

    params["scope"] = scope

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedAlbumList]:
    if response.status_code == 200:
        response_200 = PaginatedAlbumList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedAlbumList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    artist: Union[Unset, None, int] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    content_category: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetAlbumsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Response[PaginatedAlbumList]:
    """
    Args:
        artist (Union[Unset, None, int]):
        channel (Union[Unset, None, str]):
        content_category (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetAlbumsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedAlbumList]
    """

    kwargs = _get_kwargs(
        client=client,
        artist=artist,
        channel=channel,
        content_category=content_category,
        hidden=hidden,
        include_channels=include_channels,
        library=library,
        mbid=mbid,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        related=related,
        scope=scope,
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
    artist: Union[Unset, None, int] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    content_category: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetAlbumsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PaginatedAlbumList]:
    """
    Args:
        artist (Union[Unset, None, int]):
        channel (Union[Unset, None, str]):
        content_category (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetAlbumsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedAlbumList]
    """

    return sync_detailed(
        client=client,
        artist=artist,
        channel=channel,
        content_category=content_category,
        hidden=hidden,
        include_channels=include_channels,
        library=library,
        mbid=mbid,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        related=related,
        scope=scope,
        tag=tag,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    artist: Union[Unset, None, int] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    content_category: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetAlbumsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Response[PaginatedAlbumList]:
    """
    Args:
        artist (Union[Unset, None, int]):
        channel (Union[Unset, None, str]):
        content_category (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetAlbumsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedAlbumList]
    """

    kwargs = _get_kwargs(
        client=client,
        artist=artist,
        channel=channel,
        content_category=content_category,
        hidden=hidden,
        include_channels=include_channels,
        library=library,
        mbid=mbid,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        related=related,
        scope=scope,
        tag=tag,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    artist: Union[Unset, None, int] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    content_category: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetAlbumsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PaginatedAlbumList]:
    """
    Args:
        artist (Union[Unset, None, int]):
        channel (Union[Unset, None, str]):
        content_category (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetAlbumsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedAlbumList]
    """

    return (
        await asyncio_detailed(
            client=client,
            artist=artist,
            channel=channel,
            content_category=content_category,
            hidden=hidden,
            include_channels=include_channels,
            library=library,
            mbid=mbid,
            ordering=ordering,
            page=page,
            page_size=page_size,
            playable=playable,
            q=q,
            related=related,
            scope=scope,
            tag=tag,
        )
    ).parsed
