from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.manage_invitation import ManageInvitation
from ...models.manage_invitation_request import ManageInvitationRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: ManageInvitationRequest,
    multipart_data: ManageInvitationRequest,
    json_body: ManageInvitationRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/users/invitations/{id}/".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[ManageInvitation]:
    if response.status_code == 200:
        response_200 = ManageInvitation.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ManageInvitation]:
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
    form_data: ManageInvitationRequest,
    multipart_data: ManageInvitationRequest,
    json_body: ManageInvitationRequest,
) -> Response[ManageInvitation]:
    """
    Args:
        id (int):
        multipart_data (ManageInvitationRequest):
        json_body (ManageInvitationRequest):

    Returns:
        Response[ManageInvitation]
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
    form_data: ManageInvitationRequest,
    multipart_data: ManageInvitationRequest,
    json_body: ManageInvitationRequest,
) -> Optional[ManageInvitation]:
    """
    Args:
        id (int):
        multipart_data (ManageInvitationRequest):
        json_body (ManageInvitationRequest):

    Returns:
        Response[ManageInvitation]
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
    form_data: ManageInvitationRequest,
    multipart_data: ManageInvitationRequest,
    json_body: ManageInvitationRequest,
) -> Response[ManageInvitation]:
    """
    Args:
        id (int):
        multipart_data (ManageInvitationRequest):
        json_body (ManageInvitationRequest):

    Returns:
        Response[ManageInvitation]
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
    form_data: ManageInvitationRequest,
    multipart_data: ManageInvitationRequest,
    json_body: ManageInvitationRequest,
) -> Optional[ManageInvitation]:
    """
    Args:
        id (int):
        multipart_data (ManageInvitationRequest):
        json_body (ManageInvitationRequest):

    Returns:
        Response[ManageInvitation]
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
