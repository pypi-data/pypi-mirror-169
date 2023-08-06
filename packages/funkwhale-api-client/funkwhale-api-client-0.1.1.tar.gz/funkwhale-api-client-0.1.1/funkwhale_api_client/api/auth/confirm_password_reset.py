from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.password_reset_confirm import PasswordResetConfirm
from ...models.password_reset_confirm_request import PasswordResetConfirmRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: PasswordResetConfirmRequest,
    multipart_data: PasswordResetConfirmRequest,
    json_body: PasswordResetConfirmRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/auth/password/reset/confirm/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[PasswordResetConfirm]:
    if response.status_code == 200:
        response_200 = PasswordResetConfirm.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PasswordResetConfirm]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: PasswordResetConfirmRequest,
    multipart_data: PasswordResetConfirmRequest,
    json_body: PasswordResetConfirmRequest,
) -> Response[PasswordResetConfirm]:
    """Password reset e-mail link is confirmed, therefore
    this resets the user's password.

    Accepts the following POST parameters: token, uid,
        new_password1, new_password2
    Returns the success/fail message.

    Args:
        multipart_data (PasswordResetConfirmRequest): Serializer for requesting a password reset
            e-mail.
        json_body (PasswordResetConfirmRequest): Serializer for requesting a password reset
            e-mail.

    Returns:
        Response[PasswordResetConfirm]
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
    form_data: PasswordResetConfirmRequest,
    multipart_data: PasswordResetConfirmRequest,
    json_body: PasswordResetConfirmRequest,
) -> Optional[PasswordResetConfirm]:
    """Password reset e-mail link is confirmed, therefore
    this resets the user's password.

    Accepts the following POST parameters: token, uid,
        new_password1, new_password2
    Returns the success/fail message.

    Args:
        multipart_data (PasswordResetConfirmRequest): Serializer for requesting a password reset
            e-mail.
        json_body (PasswordResetConfirmRequest): Serializer for requesting a password reset
            e-mail.

    Returns:
        Response[PasswordResetConfirm]
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
    form_data: PasswordResetConfirmRequest,
    multipart_data: PasswordResetConfirmRequest,
    json_body: PasswordResetConfirmRequest,
) -> Response[PasswordResetConfirm]:
    """Password reset e-mail link is confirmed, therefore
    this resets the user's password.

    Accepts the following POST parameters: token, uid,
        new_password1, new_password2
    Returns the success/fail message.

    Args:
        multipart_data (PasswordResetConfirmRequest): Serializer for requesting a password reset
            e-mail.
        json_body (PasswordResetConfirmRequest): Serializer for requesting a password reset
            e-mail.

    Returns:
        Response[PasswordResetConfirm]
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
    form_data: PasswordResetConfirmRequest,
    multipart_data: PasswordResetConfirmRequest,
    json_body: PasswordResetConfirmRequest,
) -> Optional[PasswordResetConfirm]:
    """Password reset e-mail link is confirmed, therefore
    this resets the user's password.

    Accepts the following POST parameters: token, uid,
        new_password1, new_password2
    Returns the success/fail message.

    Args:
        multipart_data (PasswordResetConfirmRequest): Serializer for requesting a password reset
            e-mail.
        json_body (PasswordResetConfirmRequest): Serializer for requesting a password reset
            e-mail.

    Returns:
        Response[PasswordResetConfirm]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
