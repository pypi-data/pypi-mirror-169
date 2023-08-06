from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_manage_album_list import PaginatedManageAlbumList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    artist: Union[Unset, None, int] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/library/albums/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["artist"] = artist

    params["fid"] = fid

    params["mbid"] = mbid

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["q"] = q

    params["title"] = title

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageAlbumList]:
    if response.status_code == 200:
        response_200 = PaginatedManageAlbumList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageAlbumList]:
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
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageAlbumList]:
    """
    Args:
        artist (Union[Unset, None, int]):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageAlbumList]
    """

    kwargs = _get_kwargs(
        client=client,
        artist=artist,
        fid=fid,
        mbid=mbid,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        title=title,
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
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageAlbumList]:
    """
    Args:
        artist (Union[Unset, None, int]):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageAlbumList]
    """

    return sync_detailed(
        client=client,
        artist=artist,
        fid=fid,
        mbid=mbid,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        title=title,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    artist: Union[Unset, None, int] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageAlbumList]:
    """
    Args:
        artist (Union[Unset, None, int]):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageAlbumList]
    """

    kwargs = _get_kwargs(
        client=client,
        artist=artist,
        fid=fid,
        mbid=mbid,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        title=title,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    artist: Union[Unset, None, int] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    title: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageAlbumList]:
    """
    Args:
        artist (Union[Unset, None, int]):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        title (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageAlbumList]
    """

    return (
        await asyncio_detailed(
            client=client,
            artist=artist,
            fid=fid,
            mbid=mbid,
            ordering=ordering,
            page=page,
            page_size=page_size,
            q=q,
            title=title,
        )
    ).parsed
