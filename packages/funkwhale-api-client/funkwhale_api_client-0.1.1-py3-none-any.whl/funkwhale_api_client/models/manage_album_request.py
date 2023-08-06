import datetime
import json
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cover_field_request import CoverFieldRequest
from ..models.manage_base_actor_request import ManageBaseActorRequest
from ..models.manage_nested_artist_request import ManageNestedArtistRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageAlbumRequest")


@attr.s(auto_attribs=True)
class ManageAlbumRequest:
    """
    Attributes:
        title (str):
        cover (CoverFieldRequest):
        domain (str):
        artist (ManageNestedArtistRequest):
        attributed_to (ManageBaseActorRequest):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        release_date (Union[Unset, None, datetime.date]):
    """

    title: str
    cover: CoverFieldRequest
    domain: str
    artist: ManageNestedArtistRequest
    attributed_to: ManageBaseActorRequest
    fid: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    release_date: Union[Unset, None, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        cover = self.cover.to_dict()

        domain = self.domain
        artist = self.artist.to_dict()

        attributed_to = self.attributed_to.to_dict()

        fid = self.fid
        mbid = self.mbid
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        release_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat() if self.release_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "cover": cover,
                "domain": domain,
                "artist": artist,
                "attributed_to": attributed_to,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if release_date is not UNSET:
            field_dict["release_date"] = release_date

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        title = self.title if isinstance(self.title, Unset) else (None, str(self.title).encode(), "text/plain")
        cover = (None, json.dumps(self.cover.to_dict()).encode(), "application/json")

        domain = self.domain if isinstance(self.domain, Unset) else (None, str(self.domain).encode(), "text/plain")
        artist = (None, json.dumps(self.artist.to_dict()).encode(), "application/json")

        attributed_to = (None, json.dumps(self.attributed_to.to_dict()).encode(), "application/json")

        fid = self.fid if isinstance(self.fid, Unset) else (None, str(self.fid).encode(), "text/plain")
        mbid = self.mbid if isinstance(self.mbid, Unset) else (None, str(self.mbid).encode(), "text/plain")
        creation_date: Union[Unset, bytes] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat().encode()

        release_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat().encode() if self.release_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "title": title,
                "cover": cover,
                "domain": domain,
                "artist": artist,
                "attributed_to": attributed_to,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if release_date is not UNSET:
            field_dict["release_date"] = release_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        cover = CoverFieldRequest.from_dict(d.pop("cover"))

        domain = d.pop("domain")

        artist = ManageNestedArtistRequest.from_dict(d.pop("artist"))

        attributed_to = ManageBaseActorRequest.from_dict(d.pop("attributed_to"))

        fid = d.pop("fid", UNSET)

        mbid = d.pop("mbid", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _release_date = d.pop("release_date", UNSET)
        release_date: Union[Unset, None, datetime.date]
        if _release_date is None:
            release_date = None
        elif isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        manage_album_request = cls(
            title=title,
            cover=cover,
            domain=domain,
            artist=artist,
            attributed_to=attributed_to,
            fid=fid,
            mbid=mbid,
            creation_date=creation_date,
            release_date=release_date,
        )

        manage_album_request.additional_properties = d
        return manage_album_request

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
