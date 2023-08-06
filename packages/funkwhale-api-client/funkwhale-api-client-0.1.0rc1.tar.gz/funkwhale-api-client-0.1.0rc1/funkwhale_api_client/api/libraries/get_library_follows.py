from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.get_library_follows_privacy_level import GetLibraryFollowsPrivacyLevel
from ...models.paginated_library_follow_list import PaginatedLibraryFollowList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, GetLibraryFollowsPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/libraries/{uuid}/follows/".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    json_privacy_level: Union[Unset, None, str] = UNSET
    if not isinstance(privacy_level, Unset):
        json_privacy_level = privacy_level.value if privacy_level else None

    params["privacy_level"] = json_privacy_level

    params["q"] = q

    params["scope"] = scope

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedLibraryFollowList]:
    if response.status_code == 200:
        response_200 = PaginatedLibraryFollowList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedLibraryFollowList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, GetLibraryFollowsPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedLibraryFollowList]:
    """
    Args:
        uuid (str):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, GetLibraryFollowsPrivacyLevel]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):

    Returns:
        Response[PaginatedLibraryFollowList]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        privacy_level=privacy_level,
        q=q,
        scope=scope,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, GetLibraryFollowsPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedLibraryFollowList]:
    """
    Args:
        uuid (str):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, GetLibraryFollowsPrivacyLevel]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):

    Returns:
        Response[PaginatedLibraryFollowList]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        privacy_level=privacy_level,
        q=q,
        scope=scope,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, GetLibraryFollowsPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedLibraryFollowList]:
    """
    Args:
        uuid (str):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, GetLibraryFollowsPrivacyLevel]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):

    Returns:
        Response[PaginatedLibraryFollowList]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        privacy_level=privacy_level,
        q=q,
        scope=scope,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, GetLibraryFollowsPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedLibraryFollowList]:
    """
    Args:
        uuid (str):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, GetLibraryFollowsPrivacyLevel]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):

    Returns:
        Response[PaginatedLibraryFollowList]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            ordering=ordering,
            page=page,
            page_size=page_size,
            privacy_level=privacy_level,
            q=q,
            scope=scope,
        )
    ).parsed
