from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.patched_upload_for_owner_request import PatchedUploadForOwnerRequest
from ...models.upload_for_owner import UploadForOwner
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedUploadForOwnerRequest,
    multipart_data: PatchedUploadForOwnerRequest,
    json_body: PatchedUploadForOwnerRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/uploads/{uuid}/".format(client.base_url, uuid=uuid)

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


def _parse_response(*, response: httpx.Response) -> Optional[UploadForOwner]:
    if response.status_code == 200:
        response_200 = UploadForOwner.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UploadForOwner]:
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
    form_data: PatchedUploadForOwnerRequest,
    multipart_data: PatchedUploadForOwnerRequest,
    json_body: PatchedUploadForOwnerRequest,
) -> Response[UploadForOwner]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedUploadForOwnerRequest):
        json_body (PatchedUploadForOwnerRequest):

    Returns:
        Response[UploadForOwner]
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
    form_data: PatchedUploadForOwnerRequest,
    multipart_data: PatchedUploadForOwnerRequest,
    json_body: PatchedUploadForOwnerRequest,
) -> Optional[UploadForOwner]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedUploadForOwnerRequest):
        json_body (PatchedUploadForOwnerRequest):

    Returns:
        Response[UploadForOwner]
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
    form_data: PatchedUploadForOwnerRequest,
    multipart_data: PatchedUploadForOwnerRequest,
    json_body: PatchedUploadForOwnerRequest,
) -> Response[UploadForOwner]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedUploadForOwnerRequest):
        json_body (PatchedUploadForOwnerRequest):

    Returns:
        Response[UploadForOwner]
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
    form_data: PatchedUploadForOwnerRequest,
    multipart_data: PatchedUploadForOwnerRequest,
    json_body: PatchedUploadForOwnerRequest,
) -> Optional[UploadForOwner]:
    """
    Args:
        uuid (str):
        multipart_data (PatchedUploadForOwnerRequest):
        json_body (PatchedUploadForOwnerRequest):

    Returns:
        Response[UploadForOwner]
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
