from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.admin_get_accounts_type import AdminGetAccountsType
from ...models.paginated_manage_actor_list import PaginatedManageActorList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    local: Union[Unset, None, bool] = UNSET,
    manually_approves_followers: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AdminGetAccountsType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/accounts/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["domain"] = domain

    params["local"] = local

    params["manually_approves_followers"] = manually_approves_followers

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["q"] = q

    json_type: Union[Unset, None, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value if type else None

    params["type"] = json_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageActorList]:
    if response.status_code == 200:
        response_200 = PaginatedManageActorList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageActorList]:
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
    local: Union[Unset, None, bool] = UNSET,
    manually_approves_followers: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AdminGetAccountsType] = UNSET,
) -> Response[PaginatedManageActorList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        local (Union[Unset, None, bool]):
        manually_approves_followers (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        type (Union[Unset, None, AdminGetAccountsType]):

    Returns:
        Response[PaginatedManageActorList]
    """

    kwargs = _get_kwargs(
        client=client,
        domain=domain,
        local=local,
        manually_approves_followers=manually_approves_followers,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        type=type,
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
    local: Union[Unset, None, bool] = UNSET,
    manually_approves_followers: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AdminGetAccountsType] = UNSET,
) -> Optional[PaginatedManageActorList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        local (Union[Unset, None, bool]):
        manually_approves_followers (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        type (Union[Unset, None, AdminGetAccountsType]):

    Returns:
        Response[PaginatedManageActorList]
    """

    return sync_detailed(
        client=client,
        domain=domain,
        local=local,
        manually_approves_followers=manually_approves_followers,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    local: Union[Unset, None, bool] = UNSET,
    manually_approves_followers: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AdminGetAccountsType] = UNSET,
) -> Response[PaginatedManageActorList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        local (Union[Unset, None, bool]):
        manually_approves_followers (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        type (Union[Unset, None, AdminGetAccountsType]):

    Returns:
        Response[PaginatedManageActorList]
    """

    kwargs = _get_kwargs(
        client=client,
        domain=domain,
        local=local,
        manually_approves_followers=manually_approves_followers,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    local: Union[Unset, None, bool] = UNSET,
    manually_approves_followers: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, AdminGetAccountsType] = UNSET,
) -> Optional[PaginatedManageActorList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        local (Union[Unset, None, bool]):
        manually_approves_followers (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        type (Union[Unset, None, AdminGetAccountsType]):

    Returns:
        Response[PaginatedManageActorList]
    """

    return (
        await asyncio_detailed(
            client=client,
            domain=domain,
            local=local,
            manually_approves_followers=manually_approves_followers,
            ordering=ordering,
            page=page,
            page_size=page_size,
            q=q,
            type=type,
        )
    ).parsed
