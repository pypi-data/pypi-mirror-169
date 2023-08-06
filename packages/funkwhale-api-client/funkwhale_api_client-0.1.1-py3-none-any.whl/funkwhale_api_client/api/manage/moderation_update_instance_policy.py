from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.manage_instance_policy import ManageInstancePolicy
from ...models.manage_instance_policy_request import ManageInstancePolicyRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    form_data: ManageInstancePolicyRequest,
    multipart_data: ManageInstancePolicyRequest,
    json_body: ManageInstancePolicyRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/moderation/instance-policies/{id}/".format(client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[ManageInstancePolicy]:
    if response.status_code == 200:
        response_200 = ManageInstancePolicy.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ManageInstancePolicy]:
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
    form_data: ManageInstancePolicyRequest,
    multipart_data: ManageInstancePolicyRequest,
    json_body: ManageInstancePolicyRequest,
) -> Response[ManageInstancePolicy]:
    """
    Args:
        id (int):
        multipart_data (ManageInstancePolicyRequest):
        json_body (ManageInstancePolicyRequest):

    Returns:
        Response[ManageInstancePolicy]
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
    form_data: ManageInstancePolicyRequest,
    multipart_data: ManageInstancePolicyRequest,
    json_body: ManageInstancePolicyRequest,
) -> Optional[ManageInstancePolicy]:
    """
    Args:
        id (int):
        multipart_data (ManageInstancePolicyRequest):
        json_body (ManageInstancePolicyRequest):

    Returns:
        Response[ManageInstancePolicy]
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
    form_data: ManageInstancePolicyRequest,
    multipart_data: ManageInstancePolicyRequest,
    json_body: ManageInstancePolicyRequest,
) -> Response[ManageInstancePolicy]:
    """
    Args:
        id (int):
        multipart_data (ManageInstancePolicyRequest):
        json_body (ManageInstancePolicyRequest):

    Returns:
        Response[ManageInstancePolicy]
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
    form_data: ManageInstancePolicyRequest,
    multipart_data: ManageInstancePolicyRequest,
    json_body: ManageInstancePolicyRequest,
) -> Optional[ManageInstancePolicy]:
    """
    Args:
        id (int):
        multipart_data (ManageInstancePolicyRequest):
        json_body (ManageInstancePolicyRequest):

    Returns:
        Response[ManageInstancePolicy]
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
