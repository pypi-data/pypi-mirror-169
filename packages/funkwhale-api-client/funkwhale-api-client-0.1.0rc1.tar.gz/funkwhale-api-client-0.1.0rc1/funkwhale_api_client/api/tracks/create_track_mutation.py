from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.api_mutation import APIMutation
from ...models.track_request import TrackRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: TrackRequest,
    multipart_data: TrackRequest,
    json_body: TrackRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/tracks/{id}/mutations/".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[APIMutation]:
    if response.status_code == 200:
        response_200 = APIMutation.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[APIMutation]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: TrackRequest,
    multipart_data: TrackRequest,
    json_body: TrackRequest,
) -> Response[APIMutation]:
    """A simple ViewSet for viewing and editing accounts.

    Args:
        id (int):
        multipart_data (TrackRequest):
        json_body (TrackRequest):

    Returns:
        Response[APIMutation]
    """

    kwargs = _get_kwargs(
        id=id,
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
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: TrackRequest,
    multipart_data: TrackRequest,
    json_body: TrackRequest,
) -> Optional[APIMutation]:
    """A simple ViewSet for viewing and editing accounts.

    Args:
        id (int):
        multipart_data (TrackRequest):
        json_body (TrackRequest):

    Returns:
        Response[APIMutation]
    """

    return sync_detailed(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: TrackRequest,
    multipart_data: TrackRequest,
    json_body: TrackRequest,
) -> Response[APIMutation]:
    """A simple ViewSet for viewing and editing accounts.

    Args:
        id (int):
        multipart_data (TrackRequest):
        json_body (TrackRequest):

    Returns:
        Response[APIMutation]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: TrackRequest,
    multipart_data: TrackRequest,
    json_body: TrackRequest,
) -> Optional[APIMutation]:
    """A simple ViewSet for viewing and editing accounts.

    Args:
        id (int):
        multipart_data (TrackRequest):
        json_body (TrackRequest):

    Returns:
        Response[APIMutation]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
