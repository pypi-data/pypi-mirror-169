from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.channel_update import ChannelUpdate
from ...models.channel_update_request import ChannelUpdateRequest
from ...types import Response


def _get_kwargs(
    composite: str,
    *,
    client: AuthenticatedClient,
    form_data: ChannelUpdateRequest,
    multipart_data: ChannelUpdateRequest,
    json_body: ChannelUpdateRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/channels/{composite}/".format(client.base_url, composite=composite)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ChannelUpdate]:
    if response.status_code == 200:
        response_200 = ChannelUpdate.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ChannelUpdate]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    composite: str,
    *,
    client: AuthenticatedClient,
    form_data: ChannelUpdateRequest,
    multipart_data: ChannelUpdateRequest,
    json_body: ChannelUpdateRequest,
) -> Response[ChannelUpdate]:
    """
    Args:
        composite (str):
        multipart_data (ChannelUpdateRequest):
        json_body (ChannelUpdateRequest):

    Returns:
        Response[ChannelUpdate]
    """

    kwargs = _get_kwargs(
        composite=composite,
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
    composite: str,
    *,
    client: AuthenticatedClient,
    form_data: ChannelUpdateRequest,
    multipart_data: ChannelUpdateRequest,
    json_body: ChannelUpdateRequest,
) -> Optional[ChannelUpdate]:
    """
    Args:
        composite (str):
        multipart_data (ChannelUpdateRequest):
        json_body (ChannelUpdateRequest):

    Returns:
        Response[ChannelUpdate]
    """

    return sync_detailed(
        composite=composite,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    composite: str,
    *,
    client: AuthenticatedClient,
    form_data: ChannelUpdateRequest,
    multipart_data: ChannelUpdateRequest,
    json_body: ChannelUpdateRequest,
) -> Response[ChannelUpdate]:
    """
    Args:
        composite (str):
        multipart_data (ChannelUpdateRequest):
        json_body (ChannelUpdateRequest):

    Returns:
        Response[ChannelUpdate]
    """

    kwargs = _get_kwargs(
        composite=composite,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    composite: str,
    *,
    client: AuthenticatedClient,
    form_data: ChannelUpdateRequest,
    multipart_data: ChannelUpdateRequest,
    json_body: ChannelUpdateRequest,
) -> Optional[ChannelUpdate]:
    """
    Args:
        composite (str):
        multipart_data (ChannelUpdateRequest):
        json_body (ChannelUpdateRequest):

    Returns:
        Response[ChannelUpdate]
    """

    return (
        await asyncio_detailed(
            composite=composite,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
