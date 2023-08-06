from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.global_preference import GlobalPreference
from ...models.global_preference_request import GlobalPreferenceRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: GlobalPreferenceRequest,
    multipart_data: GlobalPreferenceRequest,
    json_body: GlobalPreferenceRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/instance/admin/settings/bulk/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[GlobalPreference]:
    if response.status_code == 200:
        response_200 = GlobalPreference.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GlobalPreference]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: GlobalPreferenceRequest,
    multipart_data: GlobalPreferenceRequest,
    json_body: GlobalPreferenceRequest,
) -> Response[GlobalPreference]:
    """Update multiple preferences at once

    this is a long method because we ensure everything is valid
    before actually persisting the changes

    Args:
        multipart_data (GlobalPreferenceRequest):
        json_body (GlobalPreferenceRequest):

    Returns:
        Response[GlobalPreference]
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
    form_data: GlobalPreferenceRequest,
    multipart_data: GlobalPreferenceRequest,
    json_body: GlobalPreferenceRequest,
) -> Optional[GlobalPreference]:
    """Update multiple preferences at once

    this is a long method because we ensure everything is valid
    before actually persisting the changes

    Args:
        multipart_data (GlobalPreferenceRequest):
        json_body (GlobalPreferenceRequest):

    Returns:
        Response[GlobalPreference]
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
    form_data: GlobalPreferenceRequest,
    multipart_data: GlobalPreferenceRequest,
    json_body: GlobalPreferenceRequest,
) -> Response[GlobalPreference]:
    """Update multiple preferences at once

    this is a long method because we ensure everything is valid
    before actually persisting the changes

    Args:
        multipart_data (GlobalPreferenceRequest):
        json_body (GlobalPreferenceRequest):

    Returns:
        Response[GlobalPreference]
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
    form_data: GlobalPreferenceRequest,
    multipart_data: GlobalPreferenceRequest,
    json_body: GlobalPreferenceRequest,
) -> Optional[GlobalPreference]:
    """Update multiple preferences at once

    this is a long method because we ensure everything is valid
    before actually persisting the changes

    Args:
        multipart_data (GlobalPreferenceRequest):
        json_body (GlobalPreferenceRequest):

    Returns:
        Response[GlobalPreference]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
