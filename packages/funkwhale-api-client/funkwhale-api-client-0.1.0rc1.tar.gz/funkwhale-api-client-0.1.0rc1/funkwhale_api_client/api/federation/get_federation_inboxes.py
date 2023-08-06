from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_inbox_item_list import PaginatedInboxItemList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    activity_actor: Union[Unset, None, int] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, float] = UNSET,
    is_read: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/federation/inbox/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["activity__actor"] = activity_actor

    params["activity__type"] = activity_type

    params["before"] = before

    params["is_read"] = is_read

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedInboxItemList]:
    if response.status_code == 200:
        response_200 = PaginatedInboxItemList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedInboxItemList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    activity_actor: Union[Unset, None, int] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, float] = UNSET,
    is_read: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedInboxItemList]:
    """
    Args:
        activity_actor (Union[Unset, None, int]):
        activity_type (Union[Unset, None, str]):
        before (Union[Unset, None, float]):
        is_read (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[PaginatedInboxItemList]
    """

    kwargs = _get_kwargs(
        client=client,
        activity_actor=activity_actor,
        activity_type=activity_type,
        before=before,
        is_read=is_read,
        ordering=ordering,
        page=page,
        page_size=page_size,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    activity_actor: Union[Unset, None, int] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, float] = UNSET,
    is_read: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedInboxItemList]:
    """
    Args:
        activity_actor (Union[Unset, None, int]):
        activity_type (Union[Unset, None, str]):
        before (Union[Unset, None, float]):
        is_read (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[PaginatedInboxItemList]
    """

    return sync_detailed(
        client=client,
        activity_actor=activity_actor,
        activity_type=activity_type,
        before=before,
        is_read=is_read,
        ordering=ordering,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    activity_actor: Union[Unset, None, int] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, float] = UNSET,
    is_read: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Response[PaginatedInboxItemList]:
    """
    Args:
        activity_actor (Union[Unset, None, int]):
        activity_type (Union[Unset, None, str]):
        before (Union[Unset, None, float]):
        is_read (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[PaginatedInboxItemList]
    """

    kwargs = _get_kwargs(
        client=client,
        activity_actor=activity_actor,
        activity_type=activity_type,
        before=before,
        is_read=is_read,
        ordering=ordering,
        page=page,
        page_size=page_size,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    activity_actor: Union[Unset, None, int] = UNSET,
    activity_type: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, float] = UNSET,
    is_read: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
) -> Optional[PaginatedInboxItemList]:
    """
    Args:
        activity_actor (Union[Unset, None, int]):
        activity_type (Union[Unset, None, str]):
        before (Union[Unset, None, float]):
        is_read (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):

    Returns:
        Response[PaginatedInboxItemList]
    """

    return (
        await asyncio_detailed(
            client=client,
            activity_actor=activity_actor,
            activity_type=activity_type,
            before=before,
            is_read=is_read,
            ordering=ordering,
            page=page,
            page_size=page_size,
        )
    ).parsed
