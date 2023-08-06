from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.get_artist_libraries_ordering_item import GetArtistLibrariesOrderingItem
from ...models.paginated_library_list import PaginatedLibraryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, str] = UNSET,
    has_albums: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    name_iexact: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetArtistLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/artists/{id}/libraries/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["content_category"] = content_category

    params["has_albums"] = has_albums

    params["hidden"] = hidden

    params["include_channels"] = include_channels

    params["library"] = library

    params["mbid"] = mbid

    params["name"] = name

    params["name__icontains"] = name_icontains

    params["name__iexact"] = name_iexact

    params["name__startswith"] = name_startswith

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedLibraryList]:
    if response.status_code == 200:
        response_200 = PaginatedLibraryList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedLibraryList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, str] = UNSET,
    has_albums: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    name_iexact: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetArtistLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Response[PaginatedLibraryList]:
    """
    Args:
        id (int):
        content_category (Union[Unset, None, str]):
        has_albums (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        name_icontains (Union[Unset, None, str]):
        name_iexact (Union[Unset, None, str]):
        name_startswith (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetArtistLibrariesOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedLibraryList]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        content_category=content_category,
        has_albums=has_albums,
        hidden=hidden,
        include_channels=include_channels,
        library=library,
        mbid=mbid,
        name=name,
        name_icontains=name_icontains,
        name_iexact=name_iexact,
        name_startswith=name_startswith,
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
    id: int,
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, str] = UNSET,
    has_albums: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    name_iexact: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetArtistLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PaginatedLibraryList]:
    """
    Args:
        id (int):
        content_category (Union[Unset, None, str]):
        has_albums (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        name_icontains (Union[Unset, None, str]):
        name_iexact (Union[Unset, None, str]):
        name_startswith (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetArtistLibrariesOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedLibraryList]
    """

    return sync_detailed(
        id=id,
        client=client,
        content_category=content_category,
        has_albums=has_albums,
        hidden=hidden,
        include_channels=include_channels,
        library=library,
        mbid=mbid,
        name=name,
        name_icontains=name_icontains,
        name_iexact=name_iexact,
        name_startswith=name_startswith,
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
    id: int,
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, str] = UNSET,
    has_albums: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    name_iexact: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetArtistLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Response[PaginatedLibraryList]:
    """
    Args:
        id (int):
        content_category (Union[Unset, None, str]):
        has_albums (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        name_icontains (Union[Unset, None, str]):
        name_iexact (Union[Unset, None, str]):
        name_startswith (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetArtistLibrariesOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedLibraryList]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        content_category=content_category,
        has_albums=has_albums,
        hidden=hidden,
        include_channels=include_channels,
        library=library,
        mbid=mbid,
        name=name,
        name_icontains=name_icontains,
        name_iexact=name_iexact,
        name_startswith=name_startswith,
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
    id: int,
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, str] = UNSET,
    has_albums: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    name_iexact: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetArtistLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
) -> Optional[PaginatedLibraryList]:
    """
    Args:
        id (int):
        content_category (Union[Unset, None, str]):
        has_albums (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        name_icontains (Union[Unset, None, str]):
        name_iexact (Union[Unset, None, str]):
        name_startswith (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetArtistLibrariesOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):

    Returns:
        Response[PaginatedLibraryList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            content_category=content_category,
            has_albums=has_albums,
            hidden=hidden,
            include_channels=include_channels,
            library=library,
            mbid=mbid,
            name=name,
            name_icontains=name_icontains,
            name_iexact=name_iexact,
            name_startswith=name_startswith,
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
