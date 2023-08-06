from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.paginated_manage_instance_policy_list import PaginatedManageInstancePolicyList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    block_all: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    reject_media: Union[Unset, None, bool] = UNSET,
    silence_activity: Union[Unset, None, bool] = UNSET,
    silence_notifications: Union[Unset, None, bool] = UNSET,
    target_account_domain: Union[Unset, None, str] = UNSET,
    target_account_username: Union[Unset, None, str] = UNSET,
    target_domain: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/moderation/instance-policies/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["block_all"] = block_all

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["q"] = q

    params["reject_media"] = reject_media

    params["silence_activity"] = silence_activity

    params["silence_notifications"] = silence_notifications

    params["target_account_domain"] = target_account_domain

    params["target_account_username"] = target_account_username

    params["target_domain"] = target_domain

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageInstancePolicyList]:
    if response.status_code == 200:
        response_200 = PaginatedManageInstancePolicyList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageInstancePolicyList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    block_all: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    reject_media: Union[Unset, None, bool] = UNSET,
    silence_activity: Union[Unset, None, bool] = UNSET,
    silence_notifications: Union[Unset, None, bool] = UNSET,
    target_account_domain: Union[Unset, None, str] = UNSET,
    target_account_username: Union[Unset, None, str] = UNSET,
    target_domain: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageInstancePolicyList]:
    """
    Args:
        block_all (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        reject_media (Union[Unset, None, bool]):
        silence_activity (Union[Unset, None, bool]):
        silence_notifications (Union[Unset, None, bool]):
        target_account_domain (Union[Unset, None, str]):
        target_account_username (Union[Unset, None, str]):
        target_domain (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageInstancePolicyList]
    """

    kwargs = _get_kwargs(
        client=client,
        block_all=block_all,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        reject_media=reject_media,
        silence_activity=silence_activity,
        silence_notifications=silence_notifications,
        target_account_domain=target_account_domain,
        target_account_username=target_account_username,
        target_domain=target_domain,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    block_all: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    reject_media: Union[Unset, None, bool] = UNSET,
    silence_activity: Union[Unset, None, bool] = UNSET,
    silence_notifications: Union[Unset, None, bool] = UNSET,
    target_account_domain: Union[Unset, None, str] = UNSET,
    target_account_username: Union[Unset, None, str] = UNSET,
    target_domain: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageInstancePolicyList]:
    """
    Args:
        block_all (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        reject_media (Union[Unset, None, bool]):
        silence_activity (Union[Unset, None, bool]):
        silence_notifications (Union[Unset, None, bool]):
        target_account_domain (Union[Unset, None, str]):
        target_account_username (Union[Unset, None, str]):
        target_domain (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageInstancePolicyList]
    """

    return sync_detailed(
        client=client,
        block_all=block_all,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        reject_media=reject_media,
        silence_activity=silence_activity,
        silence_notifications=silence_notifications,
        target_account_domain=target_account_domain,
        target_account_username=target_account_username,
        target_domain=target_domain,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    block_all: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    reject_media: Union[Unset, None, bool] = UNSET,
    silence_activity: Union[Unset, None, bool] = UNSET,
    silence_notifications: Union[Unset, None, bool] = UNSET,
    target_account_domain: Union[Unset, None, str] = UNSET,
    target_account_username: Union[Unset, None, str] = UNSET,
    target_domain: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageInstancePolicyList]:
    """
    Args:
        block_all (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        reject_media (Union[Unset, None, bool]):
        silence_activity (Union[Unset, None, bool]):
        silence_notifications (Union[Unset, None, bool]):
        target_account_domain (Union[Unset, None, str]):
        target_account_username (Union[Unset, None, str]):
        target_domain (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageInstancePolicyList]
    """

    kwargs = _get_kwargs(
        client=client,
        block_all=block_all,
        ordering=ordering,
        page=page,
        page_size=page_size,
        q=q,
        reject_media=reject_media,
        silence_activity=silence_activity,
        silence_notifications=silence_notifications,
        target_account_domain=target_account_domain,
        target_account_username=target_account_username,
        target_domain=target_domain,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    block_all: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    reject_media: Union[Unset, None, bool] = UNSET,
    silence_activity: Union[Unset, None, bool] = UNSET,
    silence_notifications: Union[Unset, None, bool] = UNSET,
    target_account_domain: Union[Unset, None, str] = UNSET,
    target_account_username: Union[Unset, None, str] = UNSET,
    target_domain: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageInstancePolicyList]:
    """
    Args:
        block_all (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        q (Union[Unset, None, str]):
        reject_media (Union[Unset, None, bool]):
        silence_activity (Union[Unset, None, bool]):
        silence_notifications (Union[Unset, None, bool]):
        target_account_domain (Union[Unset, None, str]):
        target_account_username (Union[Unset, None, str]):
        target_domain (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageInstancePolicyList]
    """

    return (
        await asyncio_detailed(
            client=client,
            block_all=block_all,
            ordering=ordering,
            page=page,
            page_size=page_size,
            q=q,
            reject_media=reject_media,
            silence_activity=silence_activity,
            silence_notifications=silence_notifications,
            target_account_domain=target_account_domain,
            target_account_username=target_account_username,
            target_domain=target_domain,
        )
    ).parsed
