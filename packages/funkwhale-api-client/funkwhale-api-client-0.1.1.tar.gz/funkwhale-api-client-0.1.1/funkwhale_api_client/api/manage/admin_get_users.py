from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.admin_get_users_privacy_level import AdminGetUsersPrivacyLevel
from ...models.paginated_manage_user_list import PaginatedManageUserList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    is_active: Union[Unset, None, bool] = UNSET,
    is_staff: Union[Unset, None, bool] = UNSET,
    is_superuser: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    permission_library: Union[Unset, None, bool] = UNSET,
    permission_moderation: Union[Unset, None, bool] = UNSET,
    permission_settings: Union[Unset, None, bool] = UNSET,
    privacy_level: Union[Unset, None, AdminGetUsersPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/users/users/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["is_active"] = is_active

    params["is_staff"] = is_staff

    params["is_superuser"] = is_superuser

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["permission_library"] = permission_library

    params["permission_moderation"] = permission_moderation

    params["permission_settings"] = permission_settings

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageUserList]:
    if response.status_code == 200:
        response_200 = PaginatedManageUserList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageUserList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_active: Union[Unset, None, bool] = UNSET,
    is_staff: Union[Unset, None, bool] = UNSET,
    is_superuser: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    permission_library: Union[Unset, None, bool] = UNSET,
    permission_moderation: Union[Unset, None, bool] = UNSET,
    permission_settings: Union[Unset, None, bool] = UNSET,
    privacy_level: Union[Unset, None, AdminGetUsersPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageUserList]:
    """
    Args:
        is_active (Union[Unset, None, bool]):
        is_staff (Union[Unset, None, bool]):
        is_superuser (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        permission_library (Union[Unset, None, bool]):
        permission_moderation (Union[Unset, None, bool]):
        permission_settings (Union[Unset, None, bool]):
        privacy_level (Union[Unset, None, AdminGetUsersPrivacyLevel]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageUserList]
    """

    kwargs = _get_kwargs(
        client=client,
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        ordering=ordering,
        page=page,
        page_size=page_size,
        permission_library=permission_library,
        permission_moderation=permission_moderation,
        permission_settings=permission_settings,
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
    is_active: Union[Unset, None, bool] = UNSET,
    is_staff: Union[Unset, None, bool] = UNSET,
    is_superuser: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    permission_library: Union[Unset, None, bool] = UNSET,
    permission_moderation: Union[Unset, None, bool] = UNSET,
    permission_settings: Union[Unset, None, bool] = UNSET,
    privacy_level: Union[Unset, None, AdminGetUsersPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageUserList]:
    """
    Args:
        is_active (Union[Unset, None, bool]):
        is_staff (Union[Unset, None, bool]):
        is_superuser (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        permission_library (Union[Unset, None, bool]):
        permission_moderation (Union[Unset, None, bool]):
        permission_settings (Union[Unset, None, bool]):
        privacy_level (Union[Unset, None, AdminGetUsersPrivacyLevel]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageUserList]
    """

    return sync_detailed(
        client=client,
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        ordering=ordering,
        page=page,
        page_size=page_size,
        permission_library=permission_library,
        permission_moderation=permission_moderation,
        permission_settings=permission_settings,
        privacy_level=privacy_level,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_active: Union[Unset, None, bool] = UNSET,
    is_staff: Union[Unset, None, bool] = UNSET,
    is_superuser: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    permission_library: Union[Unset, None, bool] = UNSET,
    permission_moderation: Union[Unset, None, bool] = UNSET,
    permission_settings: Union[Unset, None, bool] = UNSET,
    privacy_level: Union[Unset, None, AdminGetUsersPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageUserList]:
    """
    Args:
        is_active (Union[Unset, None, bool]):
        is_staff (Union[Unset, None, bool]):
        is_superuser (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        permission_library (Union[Unset, None, bool]):
        permission_moderation (Union[Unset, None, bool]):
        permission_settings (Union[Unset, None, bool]):
        privacy_level (Union[Unset, None, AdminGetUsersPrivacyLevel]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageUserList]
    """

    kwargs = _get_kwargs(
        client=client,
        is_active=is_active,
        is_staff=is_staff,
        is_superuser=is_superuser,
        ordering=ordering,
        page=page,
        page_size=page_size,
        permission_library=permission_library,
        permission_moderation=permission_moderation,
        permission_settings=permission_settings,
        privacy_level=privacy_level,
        q=q,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_active: Union[Unset, None, bool] = UNSET,
    is_staff: Union[Unset, None, bool] = UNSET,
    is_superuser: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    permission_library: Union[Unset, None, bool] = UNSET,
    permission_moderation: Union[Unset, None, bool] = UNSET,
    permission_settings: Union[Unset, None, bool] = UNSET,
    privacy_level: Union[Unset, None, AdminGetUsersPrivacyLevel] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageUserList]:
    """
    Args:
        is_active (Union[Unset, None, bool]):
        is_staff (Union[Unset, None, bool]):
        is_superuser (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        permission_library (Union[Unset, None, bool]):
        permission_moderation (Union[Unset, None, bool]):
        permission_settings (Union[Unset, None, bool]):
        privacy_level (Union[Unset, None, AdminGetUsersPrivacyLevel]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageUserList]
    """

    return (
        await asyncio_detailed(
            client=client,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            ordering=ordering,
            page=page,
            page_size=page_size,
            permission_library=permission_library,
            permission_moderation=permission_moderation,
            permission_settings=permission_settings,
            privacy_level=privacy_level,
            q=q,
        )
    ).parsed
