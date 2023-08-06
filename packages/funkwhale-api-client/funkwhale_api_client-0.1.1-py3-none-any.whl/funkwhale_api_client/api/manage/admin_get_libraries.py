from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.admin_get_libraries_ordering_item import AdminGetLibrariesOrderingItem
from ...models.admin_get_libraries_privacy_level import AdminGetLibrariesPrivacyLevel
from ...models.paginated_manage_library_list import PaginatedManageLibraryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, AdminGetLibrariesPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/library/libraries/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["domain"] = domain

    params["fid"] = fid

    params["name"] = name

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

    json_privacy_level: Union[Unset, None, str] = UNSET
    if not isinstance(privacy_level, Unset):
        json_privacy_level = privacy_level.value if privacy_level else None

    params["privacy_level"] = json_privacy_level

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageLibraryList]:
    if response.status_code == 200:
        response_200 = PaginatedManageLibraryList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageLibraryList]:
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
    fid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, AdminGetLibrariesPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageLibraryList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        fid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[AdminGetLibrariesOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, AdminGetLibrariesPrivacyLevel]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageLibraryList]
    """

    kwargs = _get_kwargs(
        client=client,
        domain=domain,
        fid=fid,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        privacy_level=privacy_level,
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
    domain: Union[Unset, None, str] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, AdminGetLibrariesPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageLibraryList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        fid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[AdminGetLibrariesOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, AdminGetLibrariesPrivacyLevel]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageLibraryList]
    """

    return sync_detailed(
        client=client,
        domain=domain,
        fid=fid,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        privacy_level=privacy_level,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, AdminGetLibrariesPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageLibraryList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        fid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[AdminGetLibrariesOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, AdminGetLibrariesPrivacyLevel]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageLibraryList]
    """

    kwargs = _get_kwargs(
        client=client,
        domain=domain,
        fid=fid,
        name=name,
        ordering=ordering,
        page=page,
        page_size=page_size,
        privacy_level=privacy_level,
        q=q,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetLibrariesOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, AdminGetLibrariesPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageLibraryList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        fid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[AdminGetLibrariesOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, AdminGetLibrariesPrivacyLevel]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageLibraryList]
    """

    return (
        await asyncio_detailed(
            client=client,
            domain=domain,
            fid=fid,
            name=name,
            ordering=ordering,
            page=page,
            page_size=page_size,
            privacy_level=privacy_level,
            q=q,
        )
    ).parsed
