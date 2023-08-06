import datetime
import json
from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.import_status_enum import ImportStatusEnum
from ..models.manage_nested_library_request import ManageNestedLibraryRequest
from ..models.manage_nested_track_request import ManageNestedTrackRequest
from ..models.manage_upload_request_import_details import ManageUploadRequestImportDetails
from ..models.manage_upload_request_import_metadata import ManageUploadRequestImportMetadata
from ..models.manage_upload_request_metadata import ManageUploadRequestMetadata
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="ManageUploadRequest")


@attr.s(auto_attribs=True)
class ManageUploadRequest:
    """
    Attributes:
        domain (str):
        audio_file (File):
        track (ManageNestedTrackRequest):
        library (ManageNestedLibraryRequest):
        uuid (Union[Unset, str]):
        fid (Union[Unset, None, str]):
        source (Union[Unset, None, str]):
        mimetype (Union[Unset, None, str]):
        duration (Union[Unset, None, int]):
        bitrate (Union[Unset, None, int]):
        size (Union[Unset, None, int]):
        creation_date (Union[Unset, datetime.datetime]):
        accessed_date (Union[Unset, None, datetime.datetime]):
        modification_date (Union[Unset, None, datetime.datetime]):
        metadata (Union[Unset, ManageUploadRequestMetadata]):
        import_date (Union[Unset, None, datetime.datetime]):
        import_details (Union[Unset, ManageUploadRequestImportDetails]):
        import_status (Union[Unset, ImportStatusEnum]):
        import_metadata (Union[Unset, ManageUploadRequestImportMetadata]):
        import_reference (Union[Unset, str]):
    """

    domain: str
    audio_file: File
    track: ManageNestedTrackRequest
    library: ManageNestedLibraryRequest
    uuid: Union[Unset, str] = UNSET
    fid: Union[Unset, None, str] = UNSET
    source: Union[Unset, None, str] = UNSET
    mimetype: Union[Unset, None, str] = UNSET
    duration: Union[Unset, None, int] = UNSET
    bitrate: Union[Unset, None, int] = UNSET
    size: Union[Unset, None, int] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    accessed_date: Union[Unset, None, datetime.datetime] = UNSET
    modification_date: Union[Unset, None, datetime.datetime] = UNSET
    metadata: Union[Unset, ManageUploadRequestMetadata] = UNSET
    import_date: Union[Unset, None, datetime.datetime] = UNSET
    import_details: Union[Unset, ManageUploadRequestImportDetails] = UNSET
    import_status: Union[Unset, ImportStatusEnum] = UNSET
    import_metadata: Union[Unset, ManageUploadRequestImportMetadata] = UNSET
    import_reference: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        domain = self.domain
        audio_file = self.audio_file.to_tuple()

        track = self.track.to_dict()

        library = self.library.to_dict()

        uuid = self.uuid
        fid = self.fid
        source = self.source
        mimetype = self.mimetype
        duration = self.duration
        bitrate = self.bitrate
        size = self.size
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        accessed_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.accessed_date, Unset):
            accessed_date = self.accessed_date.isoformat() if self.accessed_date else None

        modification_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modification_date, Unset):
            modification_date = self.modification_date.isoformat() if self.modification_date else None

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        import_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.import_date, Unset):
            import_date = self.import_date.isoformat() if self.import_date else None

        import_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.import_details, Unset):
            import_details = self.import_details.to_dict()

        import_status: Union[Unset, str] = UNSET
        if not isinstance(self.import_status, Unset):
            import_status = self.import_status.value

        import_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.import_metadata, Unset):
            import_metadata = self.import_metadata.to_dict()

        import_reference = self.import_reference

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "domain": domain,
                "audio_file": audio_file,
                "track": track,
                "library": library,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if fid is not UNSET:
            field_dict["fid"] = fid
        if source is not UNSET:
            field_dict["source"] = source
        if mimetype is not UNSET:
            field_dict["mimetype"] = mimetype
        if duration is not UNSET:
            field_dict["duration"] = duration
        if bitrate is not UNSET:
            field_dict["bitrate"] = bitrate
        if size is not UNSET:
            field_dict["size"] = size
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if accessed_date is not UNSET:
            field_dict["accessed_date"] = accessed_date
        if modification_date is not UNSET:
            field_dict["modification_date"] = modification_date
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if import_date is not UNSET:
            field_dict["import_date"] = import_date
        if import_details is not UNSET:
            field_dict["import_details"] = import_details
        if import_status is not UNSET:
            field_dict["import_status"] = import_status
        if import_metadata is not UNSET:
            field_dict["import_metadata"] = import_metadata
        if import_reference is not UNSET:
            field_dict["import_reference"] = import_reference

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        domain = self.domain if isinstance(self.domain, Unset) else (None, str(self.domain).encode(), "text/plain")
        audio_file = self.audio_file.to_tuple()

        track = (None, json.dumps(self.track.to_dict()).encode(), "application/json")

        library = (None, json.dumps(self.library.to_dict()).encode(), "application/json")

        uuid = self.uuid if isinstance(self.uuid, Unset) else (None, str(self.uuid).encode(), "text/plain")
        fid = self.fid if isinstance(self.fid, Unset) else (None, str(self.fid).encode(), "text/plain")
        source = self.source if isinstance(self.source, Unset) else (None, str(self.source).encode(), "text/plain")
        mimetype = (
            self.mimetype if isinstance(self.mimetype, Unset) else (None, str(self.mimetype).encode(), "text/plain")
        )
        duration = (
            self.duration if isinstance(self.duration, Unset) else (None, str(self.duration).encode(), "text/plain")
        )
        bitrate = self.bitrate if isinstance(self.bitrate, Unset) else (None, str(self.bitrate).encode(), "text/plain")
        size = self.size if isinstance(self.size, Unset) else (None, str(self.size).encode(), "text/plain")
        creation_date: Union[Unset, bytes] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat().encode()

        accessed_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.accessed_date, Unset):
            accessed_date = self.accessed_date.isoformat().encode() if self.accessed_date else None

        modification_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.modification_date, Unset):
            modification_date = self.modification_date.isoformat().encode() if self.modification_date else None

        metadata: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = (None, json.dumps(self.metadata.to_dict()).encode(), "application/json")

        import_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.import_date, Unset):
            import_date = self.import_date.isoformat().encode() if self.import_date else None

        import_details: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.import_details, Unset):
            import_details = (None, json.dumps(self.import_details.to_dict()).encode(), "application/json")

        import_status: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.import_status, Unset):
            import_status = (None, str(self.import_status.value).encode(), "text/plain")

        import_metadata: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.import_metadata, Unset):
            import_metadata = (None, json.dumps(self.import_metadata.to_dict()).encode(), "application/json")

        import_reference = (
            self.import_reference
            if isinstance(self.import_reference, Unset)
            else (None, str(self.import_reference).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "domain": domain,
                "audio_file": audio_file,
                "track": track,
                "library": library,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if fid is not UNSET:
            field_dict["fid"] = fid
        if source is not UNSET:
            field_dict["source"] = source
        if mimetype is not UNSET:
            field_dict["mimetype"] = mimetype
        if duration is not UNSET:
            field_dict["duration"] = duration
        if bitrate is not UNSET:
            field_dict["bitrate"] = bitrate
        if size is not UNSET:
            field_dict["size"] = size
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if accessed_date is not UNSET:
            field_dict["accessed_date"] = accessed_date
        if modification_date is not UNSET:
            field_dict["modification_date"] = modification_date
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if import_date is not UNSET:
            field_dict["import_date"] = import_date
        if import_details is not UNSET:
            field_dict["import_details"] = import_details
        if import_status is not UNSET:
            field_dict["import_status"] = import_status
        if import_metadata is not UNSET:
            field_dict["import_metadata"] = import_metadata
        if import_reference is not UNSET:
            field_dict["import_reference"] = import_reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain = d.pop("domain")

        audio_file = File(payload=BytesIO(d.pop("audio_file")))

        track = ManageNestedTrackRequest.from_dict(d.pop("track"))

        library = ManageNestedLibraryRequest.from_dict(d.pop("library"))

        uuid = d.pop("uuid", UNSET)

        fid = d.pop("fid", UNSET)

        source = d.pop("source", UNSET)

        mimetype = d.pop("mimetype", UNSET)

        duration = d.pop("duration", UNSET)

        bitrate = d.pop("bitrate", UNSET)

        size = d.pop("size", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _accessed_date = d.pop("accessed_date", UNSET)
        accessed_date: Union[Unset, None, datetime.datetime]
        if _accessed_date is None:
            accessed_date = None
        elif isinstance(_accessed_date, Unset):
            accessed_date = UNSET
        else:
            accessed_date = isoparse(_accessed_date)

        _modification_date = d.pop("modification_date", UNSET)
        modification_date: Union[Unset, None, datetime.datetime]
        if _modification_date is None:
            modification_date = None
        elif isinstance(_modification_date, Unset):
            modification_date = UNSET
        else:
            modification_date = isoparse(_modification_date)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ManageUploadRequestMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ManageUploadRequestMetadata.from_dict(_metadata)

        _import_date = d.pop("import_date", UNSET)
        import_date: Union[Unset, None, datetime.datetime]
        if _import_date is None:
            import_date = None
        elif isinstance(_import_date, Unset):
            import_date = UNSET
        else:
            import_date = isoparse(_import_date)

        _import_details = d.pop("import_details", UNSET)
        import_details: Union[Unset, ManageUploadRequestImportDetails]
        if isinstance(_import_details, Unset):
            import_details = UNSET
        else:
            import_details = ManageUploadRequestImportDetails.from_dict(_import_details)

        _import_status = d.pop("import_status", UNSET)
        import_status: Union[Unset, ImportStatusEnum]
        if isinstance(_import_status, Unset):
            import_status = UNSET
        else:
            import_status = ImportStatusEnum(_import_status)

        _import_metadata = d.pop("import_metadata", UNSET)
        import_metadata: Union[Unset, ManageUploadRequestImportMetadata]
        if isinstance(_import_metadata, Unset):
            import_metadata = UNSET
        else:
            import_metadata = ManageUploadRequestImportMetadata.from_dict(_import_metadata)

        import_reference = d.pop("import_reference", UNSET)

        manage_upload_request = cls(
            domain=domain,
            audio_file=audio_file,
            track=track,
            library=library,
            uuid=uuid,
            fid=fid,
            source=source,
            mimetype=mimetype,
            duration=duration,
            bitrate=bitrate,
            size=size,
            creation_date=creation_date,
            accessed_date=accessed_date,
            modification_date=modification_date,
            metadata=metadata,
            import_date=import_date,
            import_details=import_details,
            import_status=import_status,
            import_metadata=import_metadata,
            import_reference=import_reference,
        )

        manage_upload_request.additional_properties = d
        return manage_upload_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
