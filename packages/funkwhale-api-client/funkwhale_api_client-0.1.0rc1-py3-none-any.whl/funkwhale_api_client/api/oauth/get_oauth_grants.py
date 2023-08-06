from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.application import Application
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/oauth/grants/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["ordering"] = ordering

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Application]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Application.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Application]]:
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
) -> Response[List[Application]]:
    """This is a viewset that list applications that have access to the request user
    account, to allow revoking tokens easily.

    Args:
        ordering (Union[Unset, None, str]):

    Returns:
        Response[List[Application]]
    """

    kwargs = _get_kwargs(
        client=client,
        ordering=ordering,
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
) -> Optional[List[Application]]:
    """This is a viewset that list applications that have access to the request user
    account, to allow revoking tokens easily.

    Args:
        ordering (Union[Unset, None, str]):

    Returns:
        Response[List[Application]]
    """

    return sync_detailed(
        client=client,
        ordering=ordering,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
) -> Response[List[Application]]:
    """This is a viewset that list applications that have access to the request user
    account, to allow revoking tokens easily.

    Args:
        ordering (Union[Unset, None, str]):

    Returns:
        Response[List[Application]]
    """

    kwargs = _get_kwargs(
        client=client,
        ordering=ordering,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ordering: Union[Unset, None, str] = UNSET,
) -> Optional[List[Application]]:
    """This is a viewset that list applications that have access to the request user
    account, to allow revoking tokens easily.

    Args:
        ordering (Union[Unset, None, str]):

    Returns:
        Response[List[Application]]
    """

    return (
        await asyncio_detailed(
            client=client,
            ordering=ordering,
        )
    ).parsed
