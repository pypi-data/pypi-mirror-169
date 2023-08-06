from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.user_write import UserWrite
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/users/{username}/subsonic-token/".format(client.base_url, username=username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[UserWrite]:
    if response.status_code == 200:
        response_200 = UserWrite.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UserWrite]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[UserWrite]:
    """
    Args:
        username (str):

    Returns:
        Response[UserWrite]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[UserWrite]:
    """
    Args:
        username (str):

    Returns:
        Response[UserWrite]
    """

    return sync_detailed(
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[UserWrite]:
    """
    Args:
        username (str):

    Returns:
        Response[UserWrite]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[UserWrite]:
    """
    Args:
        username (str):

    Returns:
        Response[UserWrite]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
