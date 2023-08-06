import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.import_status_enum import ImportStatusEnum
from ..models.track import Track
from ..models.upload_for_owner_import_details import UploadForOwnerImportDetails
from ..models.upload_for_owner_import_metadata import UploadForOwnerImportMetadata
from ..models.upload_for_owner_metadata import UploadForOwnerMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadForOwner")


@attr.s(auto_attribs=True)
class UploadForOwner:
    """
    Attributes:
        uuid (str):
        creation_date (datetime.datetime):
        import_details (UploadForOwnerImportDetails):
        metadata (UploadForOwnerMetadata):
        filename (Union[Unset, str]):
        mimetype (Optional[str]):
        track (Union[Unset, None, Track]):
        library (Union[Unset, str]):
        channel (Union[Unset, str]):
        duration (Optional[int]):
        bitrate (Optional[int]):
        size (Optional[int]):
        import_date (Optional[datetime.datetime]):
        import_status (Union[Unset, ImportStatusEnum]):  Default: ImportStatusEnum.PENDING.
        import_metadata (Union[Unset, UploadForOwnerImportMetadata]):
        import_reference (Union[Unset, str]):
        source (Union[Unset, None, str]):
    """

    uuid: str
    creation_date: datetime.datetime
    import_details: UploadForOwnerImportDetails
    metadata: UploadForOwnerMetadata
    mimetype: Optional[str]
    duration: Optional[int]
    bitrate: Optional[int]
    size: Optional[int]
    import_date: Optional[datetime.datetime]
    filename: Union[Unset, str] = UNSET
    track: Union[Unset, None, Track] = UNSET
    library: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    import_status: Union[Unset, ImportStatusEnum] = ImportStatusEnum.PENDING
    import_metadata: Union[Unset, UploadForOwnerImportMetadata] = UNSET
    import_reference: Union[Unset, str] = UNSET
    source: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        creation_date = self.creation_date.isoformat()

        import_details = self.import_details.to_dict()

        metadata = self.metadata.to_dict()

        filename = self.filename
        mimetype = self.mimetype
        track: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.track, Unset):
            track = self.track.to_dict() if self.track else None

        library = self.library
        channel = self.channel
        duration = self.duration
        bitrate = self.bitrate
        size = self.size
        import_date = self.import_date.isoformat() if self.import_date else None

        import_status: Union[Unset, str] = UNSET
        if not isinstance(self.import_status, Unset):
            import_status = self.import_status.value

        import_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.import_metadata, Unset):
            import_metadata = self.import_metadata.to_dict()

        import_reference = self.import_reference
        source = self.source

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "creation_date": creation_date,
                "import_details": import_details,
                "metadata": metadata,
                "mimetype": mimetype,
                "duration": duration,
                "bitrate": bitrate,
                "size": size,
                "import_date": import_date,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename
        if track is not UNSET:
            field_dict["track"] = track
        if library is not UNSET:
            field_dict["library"] = library
        if channel is not UNSET:
            field_dict["channel"] = channel
        if import_status is not UNSET:
            field_dict["import_status"] = import_status
        if import_metadata is not UNSET:
            field_dict["import_metadata"] = import_metadata
        if import_reference is not UNSET:
            field_dict["import_reference"] = import_reference
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        creation_date = isoparse(d.pop("creation_date"))

        import_details = UploadForOwnerImportDetails.from_dict(d.pop("import_details"))

        metadata = UploadForOwnerMetadata.from_dict(d.pop("metadata"))

        filename = d.pop("filename", UNSET)

        mimetype = d.pop("mimetype")

        _track = d.pop("track", UNSET)
        track: Union[Unset, None, Track]
        if _track is None:
            track = None
        elif isinstance(_track, Unset):
            track = UNSET
        else:
            track = Track.from_dict(_track)

        library = d.pop("library", UNSET)

        channel = d.pop("channel", UNSET)

        duration = d.pop("duration")

        bitrate = d.pop("bitrate")

        size = d.pop("size")

        _import_date = d.pop("import_date")
        import_date: Optional[datetime.datetime]
        if _import_date is None:
            import_date = None
        else:
            import_date = isoparse(_import_date)

        _import_status = d.pop("import_status", UNSET)
        import_status: Union[Unset, ImportStatusEnum]
        if isinstance(_import_status, Unset):
            import_status = UNSET
        else:
            import_status = ImportStatusEnum(_import_status)

        _import_metadata = d.pop("import_metadata", UNSET)
        import_metadata: Union[Unset, UploadForOwnerImportMetadata]
        if isinstance(_import_metadata, Unset):
            import_metadata = UNSET
        else:
            import_metadata = UploadForOwnerImportMetadata.from_dict(_import_metadata)

        import_reference = d.pop("import_reference", UNSET)

        source = d.pop("source", UNSET)

        upload_for_owner = cls(
            uuid=uuid,
            creation_date=creation_date,
            import_details=import_details,
            metadata=metadata,
            filename=filename,
            mimetype=mimetype,
            track=track,
            library=library,
            channel=channel,
            duration=duration,
            bitrate=bitrate,
            size=size,
            import_date=import_date,
            import_status=import_status,
            import_metadata=import_metadata,
            import_reference=import_reference,
            source=source,
        )

        upload_for_owner.additional_properties = d
        return upload_for_owner

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
