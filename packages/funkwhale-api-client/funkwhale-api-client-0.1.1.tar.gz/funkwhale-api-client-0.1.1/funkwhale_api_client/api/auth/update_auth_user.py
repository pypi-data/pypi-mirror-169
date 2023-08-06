from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.user_details import UserDetails
from ...models.user_details_request import UserDetailsRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: UserDetailsRequest,
    multipart_data: UserDetailsRequest,
    json_body: UserDetailsRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/auth/user/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[UserDetails]:
    if response.status_code == 200:
        response_200 = UserDetails.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UserDetails]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: UserDetailsRequest,
    multipart_data: UserDetailsRequest,
    json_body: UserDetailsRequest,
) -> Response[UserDetails]:
    """Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Default accepted fields: username, first_name, last_name
    Default display fields: pk, username, email, first_name, last_name
    Read-only fields: pk, email

    Returns UserModel fields.

    Args:
        multipart_data (UserDetailsRequest): User model w/o password
        json_body (UserDetailsRequest): User model w/o password

    Returns:
        Response[UserDetails]
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
    form_data: UserDetailsRequest,
    multipart_data: UserDetailsRequest,
    json_body: UserDetailsRequest,
) -> Optional[UserDetails]:
    """Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Default accepted fields: username, first_name, last_name
    Default display fields: pk, username, email, first_name, last_name
    Read-only fields: pk, email

    Returns UserModel fields.

    Args:
        multipart_data (UserDetailsRequest): User model w/o password
        json_body (UserDetailsRequest): User model w/o password

    Returns:
        Response[UserDetails]
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
    form_data: UserDetailsRequest,
    multipart_data: UserDetailsRequest,
    json_body: UserDetailsRequest,
) -> Response[UserDetails]:
    """Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Default accepted fields: username, first_name, last_name
    Default display fields: pk, username, email, first_name, last_name
    Read-only fields: pk, email

    Returns UserModel fields.

    Args:
        multipart_data (UserDetailsRequest): User model w/o password
        json_body (UserDetailsRequest): User model w/o password

    Returns:
        Response[UserDetails]
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
    form_data: UserDetailsRequest,
    multipart_data: UserDetailsRequest,
    json_body: UserDetailsRequest,
) -> Optional[UserDetails]:
    """Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Default accepted fields: username, first_name, last_name
    Default display fields: pk, username, email, first_name, last_name
    Read-only fields: pk, email

    Returns UserModel fields.

    Args:
        multipart_data (UserDetailsRequest): User model w/o password
        json_body (UserDetailsRequest): User model w/o password

    Returns:
        Response[UserDetails]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
