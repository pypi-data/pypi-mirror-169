from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.manage_library import ManageLibrary
from ...models.patched_manage_library_request import PatchedManageLibraryRequest
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedManageLibraryRequest,
    multipart_data: PatchedManageLibraryRequest,
    json_body: PatchedManageLibraryRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/library/libraries/{uuid}/".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_data.to_multipart()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[ManageLibrary]:
    if response.status_code == 200:
        response_200 = ManageLibrary.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ManageLibrary]:
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
    form_data: PatchedManageLibraryRequest,
    multipart_data: PatchedManageLibraryRequest,
    json_body: PatchedManageLibraryRequest,
) -> Response[ManageLibrary]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedManageLibraryRequest):
        json_body (PatchedManageLibraryRequest):

    Returns:
        Response[ManageLibrary]
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


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedManageLibraryRequest,
    multipart_data: PatchedManageLibraryRequest,
    json_body: PatchedManageLibraryRequest,
) -> Optional[ManageLibrary]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedManageLibraryRequest):
        json_body (PatchedManageLibraryRequest):

    Returns:
        Response[ManageLibrary]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedManageLibraryRequest,
    multipart_data: PatchedManageLibraryRequest,
    json_body: PatchedManageLibraryRequest,
) -> Response[ManageLibrary]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedManageLibraryRequest):
        json_body (PatchedManageLibraryRequest):

    Returns:
        Response[ManageLibrary]
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


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedManageLibraryRequest,
    multipart_data: PatchedManageLibraryRequest,
    json_body: PatchedManageLibraryRequest,
) -> Optional[ManageLibrary]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedManageLibraryRequest):
        json_body (PatchedManageLibraryRequest):

    Returns:
        Response[ManageLibrary]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
