from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.get_track_mutations_ordering_item import GetTrackMutationsOrderingItem
from ...models.paginated_api_mutation_list import PaginatedAPIMutationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    license_: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTrackMutationsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    title_icontains: Union[Unset, None, str] = UNSET,
    title_iexact: Union[Unset, None, str] = UNSET,
    title_startswith: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/tracks/{id}/mutations/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["album"] = album

    params["artist"] = artist

    params["channel"] = channel

    params["hidden"] = hidden

    params["include_channels"] = include_channels

    params["library"] = library

    params["license"] = license_

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

    params["title"] = title

    params["title__icontains"] = title_icontains

    params["title__iexact"] = title_iexact

    params["title__startswith"] = title_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedAPIMutationList]:
    if response.status_code == 200:
        response_200 = PaginatedAPIMutationList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedAPIMutationList]:
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
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    license_: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTrackMutationsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    title_icontains: Union[Unset, None, str] = UNSET,
    title_iexact: Union[Unset, None, str] = UNSET,
    title_startswith: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedAPIMutationList]:
    """A simple ViewSet for viewing and editing accounts.

    Args:
        id (int):
        album (Union[Unset, None, int]):
        artist (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        license_ (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetTrackMutationsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):
        title (Union[Unset, None, str]):
        title_icontains (Union[Unset, None, str]):
        title_iexact (Union[Unset, None, str]):
        title_startswith (Union[Unset, None, str]):

    Returns:
        Response[PaginatedAPIMutationList]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        album=album,
        artist=artist,
        channel=channel,
        hidden=hidden,
        include_channels=include_channels,
        library=library,
        license_=license_,
        mbid=mbid,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        related=related,
        scope=scope,
        tag=tag,
        title=title,
        title_icontains=title_icontains,
        title_iexact=title_iexact,
        title_startswith=title_startswith,
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
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    license_: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTrackMutationsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    title_icontains: Union[Unset, None, str] = UNSET,
    title_iexact: Union[Unset, None, str] = UNSET,
    title_startswith: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedAPIMutationList]:
    """A simple ViewSet for viewing and editing accounts.

    Args:
        id (int):
        album (Union[Unset, None, int]):
        artist (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        license_ (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetTrackMutationsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):
        title (Union[Unset, None, str]):
        title_icontains (Union[Unset, None, str]):
        title_iexact (Union[Unset, None, str]):
        title_startswith (Union[Unset, None, str]):

    Returns:
        Response[PaginatedAPIMutationList]
    """

    return sync_detailed(
        id=id,
        client=client,
        album=album,
        artist=artist,
        channel=channel,
        hidden=hidden,
        include_channels=include_channels,
        library=library,
        license_=license_,
        mbid=mbid,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        related=related,
        scope=scope,
        tag=tag,
        title=title,
        title_icontains=title_icontains,
        title_iexact=title_iexact,
        title_startswith=title_startswith,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    license_: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTrackMutationsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    title_icontains: Union[Unset, None, str] = UNSET,
    title_iexact: Union[Unset, None, str] = UNSET,
    title_startswith: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedAPIMutationList]:
    """A simple ViewSet for viewing and editing accounts.

    Args:
        id (int):
        album (Union[Unset, None, int]):
        artist (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        license_ (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetTrackMutationsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):
        title (Union[Unset, None, str]):
        title_icontains (Union[Unset, None, str]):
        title_iexact (Union[Unset, None, str]):
        title_startswith (Union[Unset, None, str]):

    Returns:
        Response[PaginatedAPIMutationList]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        album=album,
        artist=artist,
        channel=channel,
        hidden=hidden,
        include_channels=include_channels,
        library=library,
        license_=license_,
        mbid=mbid,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        related=related,
        scope=scope,
        tag=tag,
        title=title,
        title_icontains=title_icontains,
        title_iexact=title_iexact,
        title_startswith=title_startswith,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    license_: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTrackMutationsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    related: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    tag: Union[Unset, None, List[str]] = UNSET,
    title: Union[Unset, None, str] = UNSET,
    title_icontains: Union[Unset, None, str] = UNSET,
    title_iexact: Union[Unset, None, str] = UNSET,
    title_startswith: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedAPIMutationList]:
    """A simple ViewSet for viewing and editing accounts.

    Args:
        id (int):
        album (Union[Unset, None, int]):
        artist (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        hidden (Union[Unset, None, bool]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        license_ (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetTrackMutationsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        related (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        tag (Union[Unset, None, List[str]]):
        title (Union[Unset, None, str]):
        title_icontains (Union[Unset, None, str]):
        title_iexact (Union[Unset, None, str]):
        title_startswith (Union[Unset, None, str]):

    Returns:
        Response[PaginatedAPIMutationList]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            album=album,
            artist=artist,
            channel=channel,
            hidden=hidden,
            include_channels=include_channels,
            library=library,
            license_=license_,
            mbid=mbid,
            ordering=ordering,
            page=page,
            page_size=page_size,
            playable=playable,
            q=q,
            related=related,
            scope=scope,
            tag=tag,
            title=title,
            title_icontains=title_icontains,
            title_iexact=title_iexact,
            title_startswith=title_startswith,
        )
    ).parsed
