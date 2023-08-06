from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.manage_domain_update import ManageDomainUpdate
from ...models.patched_manage_domain_update_request import PatchedManageDomainUpdateRequest
from ...types import Response


def _get_kwargs(
    name: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedManageDomainUpdateRequest,
    multipart_data: PatchedManageDomainUpdateRequest,
    json_body: PatchedManageDomainUpdateRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/federation/domains/{name}/".format(client.base_url, name=name)

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


def _parse_response(*, response: httpx.Response) -> Optional[ManageDomainUpdate]:
    if response.status_code == 200:
        response_200 = ManageDomainUpdate.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ManageDomainUpdate]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedManageDomainUpdateRequest,
    multipart_data: PatchedManageDomainUpdateRequest,
    json_body: PatchedManageDomainUpdateRequest,
) -> Response[ManageDomainUpdate]:
    """
    Args:
        name (str):
        multipart_data (PatchedManageDomainUpdateRequest):
        json_body (PatchedManageDomainUpdateRequest):

    Returns:
        Response[ManageDomainUpdate]
    """

    kwargs = _get_kwargs(
        name=name,
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
    name: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedManageDomainUpdateRequest,
    multipart_data: PatchedManageDomainUpdateRequest,
    json_body: PatchedManageDomainUpdateRequest,
) -> Optional[ManageDomainUpdate]:
    """
    Args:
        name (str):
        multipart_data (PatchedManageDomainUpdateRequest):
        json_body (PatchedManageDomainUpdateRequest):

    Returns:
        Response[ManageDomainUpdate]
    """

    return sync_detailed(
        name=name,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedManageDomainUpdateRequest,
    multipart_data: PatchedManageDomainUpdateRequest,
    json_body: PatchedManageDomainUpdateRequest,
) -> Response[ManageDomainUpdate]:
    """
    Args:
        name (str):
        multipart_data (PatchedManageDomainUpdateRequest):
        json_body (PatchedManageDomainUpdateRequest):

    Returns:
        Response[ManageDomainUpdate]
    """

    kwargs = _get_kwargs(
        name=name,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedManageDomainUpdateRequest,
    multipart_data: PatchedManageDomainUpdateRequest,
    json_body: PatchedManageDomainUpdateRequest,
) -> Optional[ManageDomainUpdate]:
    """
    Args:
        name (str):
        multipart_data (PatchedManageDomainUpdateRequest):
        json_body (PatchedManageDomainUpdateRequest):

    Returns:
        Response[ManageDomainUpdate]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
