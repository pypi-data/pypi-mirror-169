from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.moderation_get_requests_status import ModerationGetRequestsStatus
from ...models.moderation_get_requests_type import ModerationGetRequestsType
from ...models.paginated_manage_user_request_list import PaginatedManageUserRequestList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, ModerationGetRequestsStatus] = UNSET,
    type: Union[Unset, None, ModerationGetRequestsType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/moderation/requests/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["q"] = q

    json_status: Union[Unset, None, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value if status else None

    params["status"] = json_status

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageUserRequestList]:
    if response.status_code == 200:
        response_200 = PaginatedManageUserRequestList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageUserRequestList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, ModerationGetRequestsStatus] = UNSET,
    type: Union[Unset, None, ModerationGetRequestsType] = UNSET,
) -> Response[PaginatedManageUserRequestList]:
    """
    Args:
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        status (Union[Unset, None, ModerationGetRequestsStatus]):
        type (Union[Unset, None, ModerationGetRequestsType]):

    Returns:
        Response[PaginatedManageUserRequestList]
    """

    kwargs = _get_kwargs(
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        status=status,
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
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, ModerationGetRequestsStatus] = UNSET,
    type: Union[Unset, None, ModerationGetRequestsType] = UNSET,
) -> Optional[PaginatedManageUserRequestList]:
    """
    Args:
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        status (Union[Unset, None, ModerationGetRequestsStatus]):
        type (Union[Unset, None, ModerationGetRequestsType]):

    Returns:
        Response[PaginatedManageUserRequestList]
    """

    return sync_detailed(
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        status=status,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, ModerationGetRequestsStatus] = UNSET,
    type: Union[Unset, None, ModerationGetRequestsType] = UNSET,
) -> Response[PaginatedManageUserRequestList]:
    """
    Args:
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        status (Union[Unset, None, ModerationGetRequestsStatus]):
        type (Union[Unset, None, ModerationGetRequestsType]):

    Returns:
        Response[PaginatedManageUserRequestList]
    """

    kwargs = _get_kwargs(
        client=client,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        status=status,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, ModerationGetRequestsStatus] = UNSET,
    type: Union[Unset, None, ModerationGetRequestsType] = UNSET,
) -> Optional[PaginatedManageUserRequestList]:
    """
    Args:
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        status (Union[Unset, None, ModerationGetRequestsStatus]):
        type (Union[Unset, None, ModerationGetRequestsType]):

    Returns:
        Response[PaginatedManageUserRequestList]
    """

    return (
        await asyncio_detailed(
            client=client,
            ordering=ordering,
            page=page,
            page_size=page_size,
            q=q,
            status=status,
            type=type,
        )
    ).parsed
