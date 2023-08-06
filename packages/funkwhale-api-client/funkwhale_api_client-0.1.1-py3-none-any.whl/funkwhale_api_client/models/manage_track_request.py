import datetime
import json
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cover_field_request import CoverFieldRequest
from ..models.manage_base_actor_request import ManageBaseActorRequest
from ..models.manage_nested_artist_request import ManageNestedArtistRequest
from ..models.manage_track_album_request import ManageTrackAlbumRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageTrackRequest")


@attr.s(auto_attribs=True)
class ManageTrackRequest:
    """
    Attributes:
        title (str):
        domain (str):
        artist (ManageNestedArtistRequest):
        cover (CoverFieldRequest):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        position (Union[Unset, None, int]):
        disc_number (Union[Unset, None, int]):
        copyright_ (Union[Unset, None, str]):
        license_ (Union[Unset, None, str]):
        album (Optional[ManageTrackAlbumRequest]):
        attributed_to (Optional[ManageBaseActorRequest]):
    """

    title: str
    domain: str
    artist: ManageNestedArtistRequest
    cover: CoverFieldRequest
    album: Optional[ManageTrackAlbumRequest]
    attributed_to: Optional[ManageBaseActorRequest]
    fid: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    position: Union[Unset, None, int] = UNSET
    disc_number: Union[Unset, None, int] = UNSET
    copyright_: Union[Unset, None, str] = UNSET
    license_: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        domain = self.domain
        artist = self.artist.to_dict()

        cover = self.cover.to_dict()

        fid = self.fid
        mbid = self.mbid
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        position = self.position
        disc_number = self.disc_number
        copyright_ = self.copyright_
        license_ = self.license_
        album = self.album.to_dict() if self.album else None

        attributed_to = self.attributed_to.to_dict() if self.attributed_to else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "domain": domain,
                "artist": artist,
                "cover": cover,
                "album": album,
                "attributed_to": attributed_to,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if position is not UNSET:
            field_dict["position"] = position
        if disc_number is not UNSET:
            field_dict["disc_number"] = disc_number
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if license_ is not UNSET:
            field_dict["license"] = license_

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        title = self.title if isinstance(self.title, Unset) else (None, str(self.title).encode(), "text/plain")
        domain = self.domain if isinstance(self.domain, Unset) else (None, str(self.domain).encode(), "text/plain")
        artist = (None, json.dumps(self.artist.to_dict()).encode(), "application/json")

        cover = (None, json.dumps(self.cover.to_dict()).encode(), "application/json")

        fid = self.fid if isinstance(self.fid, Unset) else (None, str(self.fid).encode(), "text/plain")
        mbid = self.mbid if isinstance(self.mbid, Unset) else (None, str(self.mbid).encode(), "text/plain")
        creation_date: Union[Unset, bytes] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat().encode()

        position = (
            self.position if isinstance(self.position, Unset) else (None, str(self.position).encode(), "text/plain")
        )
        disc_number = (
            self.disc_number
            if isinstance(self.disc_number, Unset)
            else (None, str(self.disc_number).encode(), "text/plain")
        )
        copyright_ = (
            self.copyright_
            if isinstance(self.copyright_, Unset)
            else (None, str(self.copyright_).encode(), "text/plain")
        )
        license_ = (
            self.license_ if isinstance(self.license_, Unset) else (None, str(self.license_).encode(), "text/plain")
        )
        album = (None, json.dumps(self.album.to_dict()).encode(), "application/json") if self.album else None

        attributed_to = (
            (None, json.dumps(self.attributed_to.to_dict()).encode(), "application/json")
            if self.attributed_to
            else None
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "title": title,
                "domain": domain,
                "artist": artist,
                "cover": cover,
                "album": album,
                "attributed_to": attributed_to,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if position is not UNSET:
            field_dict["position"] = position
        if disc_number is not UNSET:
            field_dict["disc_number"] = disc_number
        if copyright_ is not UNSET:
            field_dict["copyright"] = copyright_
        if license_ is not UNSET:
            field_dict["license"] = license_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        domain = d.pop("domain")

        artist = ManageNestedArtistRequest.from_dict(d.pop("artist"))

        cover = CoverFieldRequest.from_dict(d.pop("cover"))

        fid = d.pop("fid", UNSET)

        mbid = d.pop("mbid", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        position = d.pop("position", UNSET)

        disc_number = d.pop("disc_number", UNSET)

        copyright_ = d.pop("copyright", UNSET)

        license_ = d.pop("license", UNSET)

        _album = d.pop("album")
        album: Optional[ManageTrackAlbumRequest]
        if _album is None:
            album = None
        else:
            album = ManageTrackAlbumRequest.from_dict(_album)

        _attributed_to = d.pop("attributed_to")
        attributed_to: Optional[ManageBaseActorRequest]
        if _attributed_to is None:
            attributed_to = None
        else:
            attributed_to = ManageBaseActorRequest.from_dict(_attributed_to)

        manage_track_request = cls(
            title=title,
            domain=domain,
            artist=artist,
            cover=cover,
            fid=fid,
            mbid=mbid,
            creation_date=creation_date,
            position=position,
            disc_number=disc_number,
            copyright_=copyright_,
            license_=license_,
            album=album,
            attributed_to=attributed_to,
        )

        manage_track_request.additional_properties = d
        return manage_track_request

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
