from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.manage_user_request import ManageUserRequest
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/moderation/requests/{uuid}/".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ManageUserRequest]:
    if response.status_code == 200:
        response_200 = ManageUserRequest.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ManageUserRequest]:
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
) -> Response[ManageUserRequest]:
    """
    Args:
        uuid (str):

    Returns:
        Response[ManageUserRequest]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
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
) -> Optional[ManageUserRequest]:
    """
    Args:
        uuid (str):

    Returns:
        Response[ManageUserRequest]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[ManageUserRequest]:
    """
    Args:
        uuid (str):

    Returns:
        Response[ManageUserRequest]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Optional[ManageUserRequest]:
    """
    Args:
        uuid (str):

    Returns:
        Response[ManageUserRequest]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
