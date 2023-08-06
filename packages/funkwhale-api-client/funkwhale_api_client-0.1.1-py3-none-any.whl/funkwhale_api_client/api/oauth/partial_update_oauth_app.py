from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.application import Application
from ...models.patched_application_request import PatchedApplicationRequest
from ...types import Response


def _get_kwargs(
    client_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedApplicationRequest,
    multipart_data: PatchedApplicationRequest,
    json_body: PatchedApplicationRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/oauth/apps/{client_id}/".format(client.base_url, client_id=client_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Application]:
    if response.status_code == 200:
        response_200 = Application.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Application]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedApplicationRequest,
    multipart_data: PatchedApplicationRequest,
    json_body: PatchedApplicationRequest,
) -> Response[Application]:
    """
    Args:
        client_id (str):
        multipart_data (PatchedApplicationRequest):
        json_body (PatchedApplicationRequest):

    Returns:
        Response[Application]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
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
    client_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedApplicationRequest,
    multipart_data: PatchedApplicationRequest,
    json_body: PatchedApplicationRequest,
) -> Optional[Application]:
    """
    Args:
        client_id (str):
        multipart_data (PatchedApplicationRequest):
        json_body (PatchedApplicationRequest):

    Returns:
        Response[Application]
    """

    return sync_detailed(
        client_id=client_id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    client_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedApplicationRequest,
    multipart_data: PatchedApplicationRequest,
    json_body: PatchedApplicationRequest,
) -> Response[Application]:
    """
    Args:
        client_id (str):
        multipart_data (PatchedApplicationRequest):
        json_body (PatchedApplicationRequest):

    Returns:
        Response[Application]
    """

    kwargs = _get_kwargs(
        client_id=client_id,
        client=client,
        form_data=form_data,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    client_id: str,
    *,
    client: AuthenticatedClient,
    form_data: PatchedApplicationRequest,
    multipart_data: PatchedApplicationRequest,
    json_body: PatchedApplicationRequest,
) -> Optional[Application]:
    """
    Args:
        client_id (str):
        multipart_data (PatchedApplicationRequest):
        json_body (PatchedApplicationRequest):

    Returns:
        Response[Application]
    """

    return (
        await asyncio_detailed(
            client_id=client_id,
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
