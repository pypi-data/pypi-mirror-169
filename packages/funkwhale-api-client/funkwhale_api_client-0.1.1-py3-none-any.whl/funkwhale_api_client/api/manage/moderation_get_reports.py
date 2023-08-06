from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.moderation_get_reports_type import ModerationGetReportsType
from ...models.paginated_manage_report_list import PaginatedManageReportList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    is_handled: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    submitter_email: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ModerationGetReportsType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/moderation/reports/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["is_handled"] = is_handled

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["q"] = q

    params["submitter_email"] = submitter_email

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


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageReportList]:
    if response.status_code == 200:
        response_200 = PaginatedManageReportList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageReportList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    is_handled: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    submitter_email: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ModerationGetReportsType] = UNSET,
) -> Response[PaginatedManageReportList]:
    """
    Args:
        is_handled (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        submitter_email (Union[Unset, None, str]):
        type (Union[Unset, None, ModerationGetReportsType]):

    Returns:
        Response[PaginatedManageReportList]
    """

    kwargs = _get_kwargs(
        client=client,
        is_handled=is_handled,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        submitter_email=submitter_email,
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
    is_handled: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    submitter_email: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ModerationGetReportsType] = UNSET,
) -> Optional[PaginatedManageReportList]:
    """
    Args:
        is_handled (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        submitter_email (Union[Unset, None, str]):
        type (Union[Unset, None, ModerationGetReportsType]):

    Returns:
        Response[PaginatedManageReportList]
    """

    return sync_detailed(
        client=client,
        is_handled=is_handled,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        submitter_email=submitter_email,
        type=type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    is_handled: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    submitter_email: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ModerationGetReportsType] = UNSET,
) -> Response[PaginatedManageReportList]:
    """
    Args:
        is_handled (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        submitter_email (Union[Unset, None, str]):
        type (Union[Unset, None, ModerationGetReportsType]):

    Returns:
        Response[PaginatedManageReportList]
    """

    kwargs = _get_kwargs(
        client=client,
        is_handled=is_handled,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        submitter_email=submitter_email,
        type=type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    is_handled: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    submitter_email: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, ModerationGetReportsType] = UNSET,
) -> Optional[PaginatedManageReportList]:
    """
    Args:
        is_handled (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        submitter_email (Union[Unset, None, str]):
        type (Union[Unset, None, ModerationGetReportsType]):

    Returns:
        Response[PaginatedManageReportList]
    """

    return (
        await asyncio_detailed(
            client=client,
            is_handled=is_handled,
            ordering=ordering,
            page=page,
            page_size=page_size,
            q=q,
            submitter_email=submitter_email,
            type=type,
        )
    ).parsed
