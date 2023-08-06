from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.get_uploads_import_status_item import GetUploadsImportStatusItem
from ...models.paginated_upload_for_owner_list import PaginatedUploadForOwnerList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    album_artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, List[GetUploadsImportStatusItem]] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, str] = UNSET,
    track_artist: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/uploads/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["album_artist"] = album_artist

    params["channel"] = channel

    params["import_reference"] = import_reference

    json_import_status: Union[Unset, None, List[str]] = UNSET
    if not isinstance(import_status, Unset):
        if import_status is None:
            json_import_status = None
        else:
            json_import_status = []
            for import_status_item_data in import_status:
                import_status_item = import_status_item_data.value

                json_import_status.append(import_status_item)

    params["import_status"] = json_import_status

    params["include_channels"] = include_channels

    params["library"] = library

    params["mimetype"] = mimetype

    params["ordering"] = ordering

    params["page"] = page

    params["page_size"] = page_size

    params["playable"] = playable

    params["q"] = q

    params["scope"] = scope

    params["track"] = track

    params["track_artist"] = track_artist

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedUploadForOwnerList]:
    if response.status_code == 200:
        response_200 = PaginatedUploadForOwnerList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedUploadForOwnerList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    album_artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, List[GetUploadsImportStatusItem]] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, str] = UNSET,
    track_artist: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedUploadForOwnerList]:
    """
    Args:
        album_artist (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        import_reference (Union[Unset, None, str]):
        import_status (Union[Unset, None, List[GetUploadsImportStatusItem]]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mimetype (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        track (Union[Unset, None, str]):
        track_artist (Union[Unset, None, str]):

    Returns:
        Response[PaginatedUploadForOwnerList]
    """

    kwargs = _get_kwargs(
        client=client,
        album_artist=album_artist,
        channel=channel,
        import_reference=import_reference,
        import_status=import_status,
        include_channels=include_channels,
        library=library,
        mimetype=mimetype,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        scope=scope,
        track=track,
        track_artist=track_artist,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    album_artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, List[GetUploadsImportStatusItem]] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, str] = UNSET,
    track_artist: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedUploadForOwnerList]:
    """
    Args:
        album_artist (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        import_reference (Union[Unset, None, str]):
        import_status (Union[Unset, None, List[GetUploadsImportStatusItem]]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mimetype (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        track (Union[Unset, None, str]):
        track_artist (Union[Unset, None, str]):

    Returns:
        Response[PaginatedUploadForOwnerList]
    """

    return sync_detailed(
        client=client,
        album_artist=album_artist,
        channel=channel,
        import_reference=import_reference,
        import_status=import_status,
        include_channels=include_channels,
        library=library,
        mimetype=mimetype,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        scope=scope,
        track=track,
        track_artist=track_artist,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    album_artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, List[GetUploadsImportStatusItem]] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, str] = UNSET,
    track_artist: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedUploadForOwnerList]:
    """
    Args:
        album_artist (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        import_reference (Union[Unset, None, str]):
        import_status (Union[Unset, None, List[GetUploadsImportStatusItem]]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mimetype (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        track (Union[Unset, None, str]):
        track_artist (Union[Unset, None, str]):

    Returns:
        Response[PaginatedUploadForOwnerList]
    """

    kwargs = _get_kwargs(
        client=client,
        album_artist=album_artist,
        channel=channel,
        import_reference=import_reference,
        import_status=import_status,
        include_channels=include_channels,
        library=library,
        mimetype=mimetype,
        ordering=ordering,
        page=page,
        page_size=page_size,
        playable=playable,
        q=q,
        scope=scope,
        track=track,
        track_artist=track_artist,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    album_artist: Union[Unset, None, str] = UNSET,
    channel: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, List[GetUploadsImportStatusItem]] = UNSET,
    include_channels: Union[Unset, None, bool] = UNSET,
    library: Union[Unset, None, str] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    playable: Union[Unset, None, bool] = UNSET,
    q: Union[Unset, None, str] = UNSET,
    scope: Union[Unset, None, str] = UNSET,
    track: Union[Unset, None, str] = UNSET,
    track_artist: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedUploadForOwnerList]:
    """
    Args:
        album_artist (Union[Unset, None, str]):
        channel (Union[Unset, None, str]):
        import_reference (Union[Unset, None, str]):
        import_status (Union[Unset, None, List[GetUploadsImportStatusItem]]):
        include_channels (Union[Unset, None, bool]):
        library (Union[Unset, None, str]):
        mimetype (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        playable (Union[Unset, None, bool]):
        q (Union[Unset, None, str]):
        scope (Union[Unset, None, str]):
        track (Union[Unset, None, str]):
        track_artist (Union[Unset, None, str]):

    Returns:
        Response[PaginatedUploadForOwnerList]
    """

    return (
        await asyncio_detailed(
            client=client,
            album_artist=album_artist,
            channel=channel,
            import_reference=import_reference,
            import_status=import_status,
            include_channels=include_channels,
            library=library,
            mimetype=mimetype,
            ordering=ordering,
            page=page,
            page_size=page_size,
            playable=playable,
            q=q,
            scope=scope,
            track=track,
            track_artist=track_artist,
        )
    ).parsed
