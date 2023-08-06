from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.admin_get_artists_content_category import AdminGetArtistsContentCategory
from ...models.paginated_manage_artist_list import PaginatedManageArtistList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, AdminGetArtistsContentCategory] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/library/artists/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_content_category: Union[Unset, None, str] = UNSET
    if not isinstance(content_category, Unset):
        json_content_category = content_category.value if content_category else None

    params["content_category"] = json_content_category

    params["fid"] = fid

    params["mbid"] = mbid

    params["name"] = name

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageArtistList]:
    if response.status_code == 200:
        response_200 = PaginatedManageArtistList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageArtistList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, AdminGetArtistsContentCategory] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageArtistList]:
    """
    Args:
        content_category (Union[Unset, None, AdminGetArtistsContentCategory]):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageArtistList]
    """

    kwargs = _get_kwargs(
        client=client,
        content_category=content_category,
        fid=fid,
        mbid=mbid,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, AdminGetArtistsContentCategory] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageArtistList]:
    """
    Args:
        content_category (Union[Unset, None, AdminGetArtistsContentCategory]):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageArtistList]
    """

    return sync_detailed(
        client=client,
        content_category=content_category,
        fid=fid,
        mbid=mbid,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, AdminGetArtistsContentCategory] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageArtistList]:
    """
    Args:
        content_category (Union[Unset, None, AdminGetArtistsContentCategory]):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageArtistList]
    """

    kwargs = _get_kwargs(
        client=client,
        content_category=content_category,
        fid=fid,
        mbid=mbid,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    content_category: Union[Unset, None, AdminGetArtistsContentCategory] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    mbid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageArtistList]:
    """
    Args:
        content_category (Union[Unset, None, AdminGetArtistsContentCategory]):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageArtistList]
    """

    return (
        await asyncio_detailed(
            client=client,
            content_category=content_category,
            fid=fid,
            mbid=mbid,
            name=name,
            ordering=ordering,
            page=page,
            page_size=page_size,
            q=q,
        )
    ).parsed
