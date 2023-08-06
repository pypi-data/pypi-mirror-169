from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.radio import Radio
from ...models.radio_request import RadioRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: RadioRequest,
    multipart_data: RadioRequest,
    json_body: RadioRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/radios/radios/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Radio]:
    if response.status_code == 201:
        response_201 = Radio.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[Radio]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: RadioRequest,
    multipart_data: RadioRequest,
    json_body: RadioRequest,
) -> Response[Radio]:
    """
    Args:
        multipart_data (RadioRequest):
        json_body (RadioRequest):

    Returns:
        Response[Radio]
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
    form_data: RadioRequest,
    multipart_data: RadioRequest,
    json_body: RadioRequest,
) -> Optional[Radio]:
    """
    Args:
        multipart_data (RadioRequest):
        json_body (RadioRequest):

    Returns:
        Response[Radio]
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
    form_data: RadioRequest,
    multipart_data: RadioRequest,
    json_body: RadioRequest,
) -> Response[Radio]:
    """
    Args:
        multipart_data (RadioRequest):
        json_body (RadioRequest):

    Returns:
        Response[Radio]
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
    form_data: RadioRequest,
    multipart_data: RadioRequest,
    json_body: RadioRequest,
) -> Optional[Radio]:
    """
    Args:
        multipart_data (RadioRequest):
        json_body (RadioRequest):

    Returns:
        Response[Radio]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
