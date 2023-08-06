from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.radio_session import RadioSession
from ...models.radio_session_request import RadioSessionRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: RadioSessionRequest,
    multipart_data: RadioSessionRequest,
    json_body: RadioSessionRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/radios/sessions/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RadioSession]:
    if response.status_code == 201:
        response_201 = RadioSession.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[RadioSession]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: RadioSessionRequest,
    multipart_data: RadioSessionRequest,
    json_body: RadioSessionRequest,
) -> Response[RadioSession]:
    """
    Args:
        multipart_data (RadioSessionRequest):
        json_body (RadioSessionRequest):

    Returns:
        Response[RadioSession]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    form_data: RadioSessionRequest,
    multipart_data: RadioSessionRequest,
    json_body: RadioSessionRequest,
) -> Optional[RadioSession]:
    """
    Args:
        multipart_data (RadioSessionRequest):
        json_body (RadioSessionRequest):

    Returns:
        Response[RadioSession]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    form_data: RadioSessionRequest,
    multipart_data: RadioSessionRequest,
    json_body: RadioSessionRequest,
) -> Response[RadioSession]:
    """
    Args:
        multipart_data (RadioSessionRequest):
        json_body (RadioSessionRequest):

    Returns:
        Response[RadioSession]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    form_data: RadioSessionRequest,
    multipart_data: RadioSessionRequest,
    json_body: RadioSessionRequest,
) -> Optional[RadioSession]:
    """
    Args:
        multipart_data (RadioSessionRequest):
        json_body (RadioSessionRequest):

    Returns:
        Response[RadioSession]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
