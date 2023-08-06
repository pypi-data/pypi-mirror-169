from typing import Any, Dict

import httpx

from ...client import AuthenticatedClient
from ...models.library_follow_request import LibraryFollowRequest
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: LibraryFollowRequest,
    multipart_data: LibraryFollowRequest,
    json_body: LibraryFollowRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/federation/follows/library/{uuid}/accept/".format(client.base_url, uuid=uuid)

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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: LibraryFollowRequest,
    multipart_data: LibraryFollowRequest,
    json_body: LibraryFollowRequest,
) -> Response[Any]:
    """
    Args:
        uuid (str):
        multipart_data (LibraryFollowRequest):
        json_body (LibraryFollowRequest):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
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


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: LibraryFollowRequest,
    multipart_data: LibraryFollowRequest,
    json_body: LibraryFollowRequest,
) -> Response[Any]:
    """
    Args:
        uuid (str):
        multipart_data (LibraryFollowRequest):
        json_body (LibraryFollowRequest):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
