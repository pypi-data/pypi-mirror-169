from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.get_tags_ordering_item import GetTagsOrderingItem
from ...models.paginated_tag_list import PaginatedTagList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTagsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/tags/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params["name__startswith"] = name_startswith

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedTagList]:
    if response.status_code == 200:
        response_200 = PaginatedTagList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedTagList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTagsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedTagList]:
    """
    Args:
        name (Union[Unset, None, str]):
        name_startswith (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetTagsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedTagList]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        name_startswith=name_startswith,
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
    name: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTagsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedTagList]:
    """
    Args:
        name (Union[Unset, None, str]):
        name_startswith (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetTagsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedTagList]
    """

    return sync_detailed(
        client=client,
        name=name,
        name_startswith=name_startswith,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTagsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedTagList]:
    """
    Args:
        name (Union[Unset, None, str]):
        name_startswith (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetTagsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedTagList]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        name_startswith=name_startswith,
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
    name: Union[Unset, None, str] = UNSET,
    name_startswith: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[GetTagsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedTagList]:
    """
    Args:
        name (Union[Unset, None, str]):
        name_startswith (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[GetTagsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedTagList]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            name_startswith=name_startswith,
            ordering=ordering,
            page=page,
            page_size=page_size,
            q=q,
        )
    ).parsed
