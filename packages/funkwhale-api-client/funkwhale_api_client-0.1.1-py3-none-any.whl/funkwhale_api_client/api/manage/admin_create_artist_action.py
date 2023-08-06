from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.manage_artist import ManageArtist
from ...models.manage_artist_request import ManageArtistRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    form_data: ManageArtistRequest,
    multipart_data: ManageArtistRequest,
    json_body: ManageArtistRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/library/artists/action/".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[ManageArtist]:
    if response.status_code == 200:
        response_200 = ManageArtist.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ManageArtist]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    form_data: ManageArtistRequest,
    multipart_data: ManageArtistRequest,
    json_body: ManageArtistRequest,
) -> Response[ManageArtist]:
    """str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

    Args:
        multipart_data (ManageArtistRequest):
        json_body (ManageArtistRequest):

    Returns:
        Response[ManageArtist]
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
    form_data: ManageArtistRequest,
    multipart_data: ManageArtistRequest,
    json_body: ManageArtistRequest,
) -> Optional[ManageArtist]:
    """str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

    Args:
        multipart_data (ManageArtistRequest):
        json_body (ManageArtistRequest):

    Returns:
        Response[ManageArtist]
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
    form_data: ManageArtistRequest,
    multipart_data: ManageArtistRequest,
    json_body: ManageArtistRequest,
) -> Response[ManageArtist]:
    """str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

    Args:
        multipart_data (ManageArtistRequest):
        json_body (ManageArtistRequest):

    Returns:
        Response[ManageArtist]
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
    form_data: ManageArtistRequest,
    multipart_data: ManageArtistRequest,
    json_body: ManageArtistRequest,
) -> Optional[ManageArtist]:
    """str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str

    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.

    Args:
        multipart_data (ManageArtistRequest):
        json_body (ManageArtistRequest):

    Returns:
        Response[ManageArtist]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
