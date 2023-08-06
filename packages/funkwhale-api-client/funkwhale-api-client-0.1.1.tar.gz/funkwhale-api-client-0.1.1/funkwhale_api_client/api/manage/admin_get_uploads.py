from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.admin_get_uploads_import_status import AdminGetUploadsImportStatus
from ...models.admin_get_uploads_ordering_item import AdminGetUploadsOrderingItem
from ...models.paginated_manage_upload_list import PaginatedManageUploadList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, AdminGetUploadsImportStatus] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetUploadsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/manage/library/uploads/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["domain"] = domain

    params["fid"] = fid

    params["import_reference"] = import_reference

    json_import_status: Union[Unset, None, str] = UNSET
    if not isinstance(import_status, Unset):
        json_import_status = import_status.value if import_status else None

    params["import_status"] = json_import_status

    params["mimetype"] = mimetype

    json_ordering: Union[Unset, None, List[str]] = UNSET
    if not isinstance(ordering, Unset):
        if ordering is None:
            json_ordering = None
        else:
            json_ordering = []
            for ordering_item_data in ordering:
                ordering_item = ordering_item_data.value

                json_ordering.append(ordering_item)

    params["ordering"] = json_ordering

    params["page"] = page

    params["page_size"] = page_size

    params["privacy_level"] = privacy_level

    params["q"] = q

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[PaginatedManageUploadList]:
    if response.status_code == 200:
        response_200 = PaginatedManageUploadList.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PaginatedManageUploadList]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, AdminGetUploadsImportStatus] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetUploadsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageUploadList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        fid (Union[Unset, None, str]):
        import_reference (Union[Unset, None, str]):
        import_status (Union[Unset, None, AdminGetUploadsImportStatus]):
        mimetype (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[AdminGetUploadsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, str]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageUploadList]
    """

    kwargs = _get_kwargs(
        client=client,
        domain=domain,
        fid=fid,
        import_reference=import_reference,
        import_status=import_status,
        mimetype=mimetype,
        ordering=ordering,
        page=page,
        page_size=page_size,
        privacy_level=privacy_level,
        q=q,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, AdminGetUploadsImportStatus] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetUploadsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageUploadList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        fid (Union[Unset, None, str]):
        import_reference (Union[Unset, None, str]):
        import_status (Union[Unset, None, AdminGetUploadsImportStatus]):
        mimetype (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[AdminGetUploadsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, str]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageUploadList]
    """

    return sync_detailed(
        client=client,
        domain=domain,
        fid=fid,
        import_reference=import_reference,
        import_status=import_status,
        mimetype=mimetype,
        ordering=ordering,
        page=page,
        page_size=page_size,
        privacy_level=privacy_level,
        q=q,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, AdminGetUploadsImportStatus] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetUploadsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Response[PaginatedManageUploadList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        fid (Union[Unset, None, str]):
        import_reference (Union[Unset, None, str]):
        import_status (Union[Unset, None, AdminGetUploadsImportStatus]):
        mimetype (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[AdminGetUploadsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, str]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageUploadList]
    """

    kwargs = _get_kwargs(
        client=client,
        domain=domain,
        fid=fid,
        import_reference=import_reference,
        import_status=import_status,
        mimetype=mimetype,
        ordering=ordering,
        page=page,
        page_size=page_size,
        privacy_level=privacy_level,
        q=q,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    domain: Union[Unset, None, str] = UNSET,
    fid: Union[Unset, None, str] = UNSET,
    import_reference: Union[Unset, None, str] = UNSET,
    import_status: Union[Unset, None, AdminGetUploadsImportStatus] = UNSET,
    mimetype: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, List[AdminGetUploadsOrderingItem]] = UNSET,
    page: Union[Unset, None, int] = UNSET,
    page_size: Union[Unset, None, int] = UNSET,
    privacy_level: Union[Unset, None, str] = UNSET,
    q: Union[Unset, None, str] = UNSET,
) -> Optional[PaginatedManageUploadList]:
    """
    Args:
        domain (Union[Unset, None, str]):
        fid (Union[Unset, None, str]):
        import_reference (Union[Unset, None, str]):
        import_status (Union[Unset, None, AdminGetUploadsImportStatus]):
        mimetype (Union[Unset, None, str]):
        ordering (Union[Unset, None, List[AdminGetUploadsOrderingItem]]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):
        privacy_level (Union[Unset, None, str]):
        q (Union[Unset, None, str]):

    Returns:
        Response[PaginatedManageUploadList]
    """

    return (
        await asyncio_detailed(
            client=client,
            domain=domain,
            fid=fid,
            import_reference=import_reference,
            import_status=import_status,
            mimetype=mimetype,
            ordering=ordering,
            page=page,
            page_size=page_size,
            privacy_level=privacy_level,
            q=q,
        )
    ).parsed
