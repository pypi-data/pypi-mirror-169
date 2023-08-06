from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_playlist_list import PaginatedPlaylistList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/playlists/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["album"] = album

    params["artist"] = artist

    params["name"] = name

    params["name__icontains"] = name_icontains

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["playable"] = playable

    params["q"] = q

    params["scope"] = scope

    params["track"] = track

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedPlaylistList]:
    if response.status_code == 200:
        response_200 = PaginatedPlaylistList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedPlaylistList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedPlaylistList]:
    """
    Args:
        album (Union[Unset, None, int]):
        artist (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        name_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        track (Union[Unset, None, int]):

    Returns:
        Response[PaginatedPlaylistList]
    """

    kwargs = _get_kwargs(
        client=client,
        album=album,
        artist=artist,
        name=name,
        name_icontains=name_icontains,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        scope=scope,
        track=track,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedPlaylistList]:
    """
    Args:
        album (Union[Unset, None, int]):
        artist (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        name_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        track (Union[Unset, None, int]):

    Returns:
        Response[PaginatedPlaylistList]
    """

    return sync_detailed(
        client=client,
        album=album,
        artist=artist,
        name=name,
        name_icontains=name_icontains,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        scope=scope,
        track=track,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedPlaylistList]:
    """
    Args:
        album (Union[Unset, None, int]):
        artist (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        name_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        track (Union[Unset, None, int]):

    Returns:
        Response[PaginatedPlaylistList]
    """

    kwargs = _get_kwargs(
        client=client,
        album=album,
        artist=artist,
        name=name,
        name_icontains=name_icontains,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        scope=scope,
        track=track,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    album: Union[Unset, None, int] = UNSET,
    artist: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    name_icontains: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedPlaylistList]:
    """
    Args:
        album (Union[Unset, None, int]):
        artist (Union[Unset, None, int]):
        name (Union[Unset, None, str]):
        name_icontains (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        track (Union[Unset, None, int]):

    Returns:
        Response[PaginatedPlaylistList]
    """

    return (
        await asyncio_detailed(
            client=client,
            album=album,
            artist=artist,
            name=name,
            name_icontains=name_icontains,
            ordering=ordering,
            page=page,
            page_size=page_size,
            playable=playable,
            q=q,
            scope=scope,
            track=track,
        )
    ).parsed
