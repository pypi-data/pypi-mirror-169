import json
from io import BytesIO
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.import_status_enum import ImportStatusEnum
from ..models.track_request import TrackRequest
from ..models.upload_for_owner_request_import_metadata import UploadForOwnerRequestImportMetadata
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="UploadForOwnerRequest")


@attr.s(auto_attribs=True)
class UploadForOwnerRequest:
    """
    Attributes:
        audio_file (File):
        filename (Union[Unset, str]):
        track (Union[Unset, None, TrackRequest]):
        library (Union[Unset, str]):
        channel (Union[Unset, str]):
        import_status (Union[Unset, ImportStatusEnum]):  Default: ImportStatusEnum.PENDING.
        import_metadata (Union[Unset, UploadForOwnerRequestImportMetadata]):
        import_reference (Union[Unset, str]):
        source (Union[Unset, None, str]):
    """

    audio_file: File
    filename: Union[Unset, str] = UNSET
    track: Union[Unset, None, TrackRequest] = UNSET
    library: Union[Unset, str] = UNSET
    channel: Union[Unset, str] = UNSET
    import_status: Union[Unset, ImportStatusEnum] = ImportStatusEnum.PENDING
    import_metadata: Union[Unset, UploadForOwnerRequestImportMetadata] = UNSET
    import_reference: Union[Unset, str] = UNSET
    source: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        audio_file = self.audio_file.to_tuple()

        filename = self.filename
        track: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.track, Unset):
            track = self.track.to_dict() if self.track else None

        library = self.library
        channel = self.channel
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
                "audio_file": audio_file,
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

    def to_multipart(self) -> Dict[str, Any]:
        audio_file = self.audio_file.to_tuple()

        filename = (
            self.filename if isinstance(self.filename, Unset) else (None, str(self.filename).encode(), "text/plain")
        )
        track: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.track, Unset):
            track = (None, json.dumps(self.track.to_dict()).encode(), "application/json") if self.track else None

        library = self.library if isinstance(self.library, Unset) else (None, str(self.library).encode(), "text/plain")
        channel = self.channel if isinstance(self.channel, Unset) else (None, str(self.channel).encode(), "text/plain")
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
        source = self.source if isinstance(self.source, Unset) else (None, str(self.source).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "audio_file": audio_file,
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
        audio_file = File(payload=BytesIO(d.pop("audio_file")))

        filename = d.pop("filename", UNSET)

        _track = d.pop("track", UNSET)
        track: Union[Unset, None, TrackRequest]
        if _track is None:
            track = None
        elif isinstance(_track, Unset):
            track = UNSET
        else:
            track = TrackRequest.from_dict(_track)

        library = d.pop("library", UNSET)

        channel = d.pop("channel", UNSET)

        _import_status = d.pop("import_status", UNSET)
        import_status: Union[Unset, ImportStatusEnum]
        if isinstance(_import_status, Unset):
            import_status = UNSET
        else:
            import_status = ImportStatusEnum(_import_status)

        _import_metadata = d.pop("import_metadata", UNSET)
        import_metadata: Union[Unset, UploadForOwnerRequestImportMetadata]
        if isinstance(_import_metadata, Unset):
            import_metadata = UNSET
        else:
            import_metadata = UploadForOwnerRequestImportMetadata.from_dict(_import_metadata)

        import_reference = d.pop("import_reference", UNSET)

        source = d.pop("source", UNSET)

        upload_for_owner_request = cls(
            audio_file=audio_file,
            filename=filename,
            track=track,
            library=library,
            channel=channel,
            import_status=import_status,
            import_metadata=import_metadata,
            import_reference=import_reference,
            source=source,
        )

        upload_for_owner_request.additional_properties = d
        return upload_for_owner_request

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
