from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.fetch import Fetch
from ...models.fetch_request import FetchRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: FetchRequest,
    multipart_data: FetchRequest,
    json_body: FetchRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/federation/fetches/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Fetch]:
    if response.status_code == 201:
        response_201 = Fetch.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[Fetch]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: FetchRequest,
    multipart_data: FetchRequest,
    json_body: FetchRequest,
) -> Response[Fetch]:
    """
    Args:
        multipart_data (FetchRequest):
        json_body (FetchRequest):

    Returns:
        Response[Fetch]
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
    form_data: FetchRequest,
    multipart_data: FetchRequest,
    json_body: FetchRequest,
) -> Optional[Fetch]:
    """
    Args:
        multipart_data (FetchRequest):
        json_body (FetchRequest):

    Returns:
        Response[Fetch]
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
    form_data: FetchRequest,
    multipart_data: FetchRequest,
    json_body: FetchRequest,
) -> Response[Fetch]:
    """
    Args:
        multipart_data (FetchRequest):
        json_body (FetchRequest):

    Returns:
        Response[Fetch]
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
    form_data: FetchRequest,
    multipart_data: FetchRequest,
    json_body: FetchRequest,
) -> Optional[Fetch]:
    """
    Args:
        multipart_data (FetchRequest):
        json_body (FetchRequest):

    Returns:
        Response[Fetch]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
