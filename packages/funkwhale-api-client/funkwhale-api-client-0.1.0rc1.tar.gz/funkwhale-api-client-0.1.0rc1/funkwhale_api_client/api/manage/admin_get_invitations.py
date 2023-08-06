from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_manage_invitation_list import PaginatedManageInvitationList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    is_open: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/users/invitations/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["is_open"] = is_open

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageInvitationList]:
    if response.status_code == 200:
        response_200 = PaginatedManageInvitationList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageInvitationList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_open: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageInvitationList]:
    """
    Args:
        is_open (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageInvitationList]
    """

    kwargs = _get_kwargs(
        client=client,
        is_open=is_open,
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
    is_open: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageInvitationList]:
    """
    Args:
        is_open (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageInvitationList]
    """

    return sync_detailed(
        client=client,
        is_open=is_open,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_open: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageInvitationList]:
    """
    Args:
        is_open (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageInvitationList]
    """

    kwargs = _get_kwargs(
        client=client,
        is_open=is_open,
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
    is_open: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageInvitationList]:
    """
    Args:
        is_open (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageInvitationList]
    """

    return (
        await asyncio_detailed(
            client=client,
            is_open=is_open,
            ordering=ordering,
            page=page,
            page_size=page_size,
            q=q,
        )
    ).parsed
