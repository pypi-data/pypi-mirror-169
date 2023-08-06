import datetime
import json
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.api_actor_request import APIActorRequest
from ..models.cover_field_request import CoverFieldRequest
from ..models.simple_artist_request import SimpleArtistRequest
from ..types import Unset

T = TypeVar("T", bound="TrackRequest")


@attr.s(auto_attribs=True)
class TrackRequest:
    """
    Attributes:
        artist (SimpleArtistRequest):
        id (int):
        fid (str):
        mbid (str):
        title (str):
        creation_date (datetime.datetime):
        is_local (bool):
        position (int):
        disc_number (int):
        downloads_count (int):
        copyright_ (str):
        attributed_to (Optional[APIActorRequest]):
        cover (Optional[CoverFieldRequest]):
    """

    artist: SimpleArtistRequest
    id: int
    fid: str
    mbid: str
    title: str
    creation_date: datetime.datetime
    is_local: bool
    position: int
    disc_number: int
    downloads_count: int
    copyright_: str
    attributed_to: Optional[APIActorRequest]
    cover: Optional[CoverFieldRequest]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artist = self.artist.to_dict()

        id = self.id
        fid = self.fid
        mbid = self.mbid
        title = self.title
        creation_date = self.creation_date.isoformat()

        is_local = self.is_local
        position = self.position
        disc_number = self.disc_number
        downloads_count = self.downloads_count
        copyright_ = self.copyright_
        attributed_to = self.attributed_to.to_dict() if self.attributed_to else None

        cover = self.cover.to_dict() if self.cover else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artist": artist,
                "id": id,
                "fid": fid,
                "mbid": mbid,
                "title": title,
                "creation_date": creation_date,
                "is_local": is_local,
                "position": position,
                "disc_number": disc_number,
                "downloads_count": downloads_count,
                "copyright": copyright_,
                "attributed_to": attributed_to,
                "cover": cover,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        artist = (None, json.dumps(self.artist.to_dict()).encode(), "application/json")

        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        fid = self.fid if isinstance(self.fid, Unset) else (None, str(self.fid).encode(), "text/plain")
        mbid = self.mbid if isinstance(self.mbid, Unset) else (None, str(self.mbid).encode(), "text/plain")
        title = self.title if isinstance(self.title, Unset) else (None, str(self.title).encode(), "text/plain")
        creation_date = self.creation_date.isoformat().encode()

        is_local = (
            self.is_local if isinstance(self.is_local, Unset) else (None, str(self.is_local).encode(), "text/plain")
        )
        position = (
            self.position if isinstance(self.position, Unset) else (None, str(self.position).encode(), "text/plain")
        )
        disc_number = (
            self.disc_number
            if isinstance(self.disc_number, Unset)
            else (None, str(self.disc_number).encode(), "text/plain")
        )
        downloads_count = (
            self.downloads_count
            if isinstance(self.downloads_count, Unset)
            else (None, str(self.downloads_count).encode(), "text/plain")
        )
        copyright_ = (
            self.copyright_
            if isinstance(self.copyright_, Unset)
            else (None, str(self.copyright_).encode(), "text/plain")
        )
        attributed_to = (
            (None, json.dumps(self.attributed_to.to_dict()).encode(), "application/json")
            if self.attributed_to
            else None
        )

        cover = (None, json.dumps(self.cover.to_dict()).encode(), "application/json") if self.cover else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "artist": artist,
                "id": id,
                "fid": fid,
                "mbid": mbid,
                "title": title,
                "creation_date": creation_date,
                "is_local": is_local,
                "position": position,
                "disc_number": disc_number,
                "downloads_count": downloads_count,
                "copyright": copyright_,
                "attributed_to": attributed_to,
                "cover": cover,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        artist = SimpleArtistRequest.from_dict(d.pop("artist"))

        id = d.pop("id")

        fid = d.pop("fid")

        mbid = d.pop("mbid")

        title = d.pop("title")

        creation_date = isoparse(d.pop("creation_date"))

        is_local = d.pop("is_local")

        position = d.pop("position")

        disc_number = d.pop("disc_number")

        downloads_count = d.pop("downloads_count")

        copyright_ = d.pop("copyright")

        _attributed_to = d.pop("attributed_to")
        attributed_to: Optional[APIActorRequest]
        if _attributed_to is None:
            attributed_to = None
        else:
            attributed_to = APIActorRequest.from_dict(_attributed_to)

        _cover = d.pop("cover")
        cover: Optional[CoverFieldRequest]
        if _cover is None:
            cover = None
        else:
            cover = CoverFieldRequest.from_dict(_cover)

        track_request = cls(
            artist=artist,
            id=id,
            fid=fid,
            mbid=mbid,
            title=title,
            creation_date=creation_date,
            is_local=is_local,
            position=position,
            disc_number=disc_number,
            downloads_count=downloads_count,
            copyright_=copyright_,
            attributed_to=attributed_to,
            cover=cover,
        )

        track_request.additional_properties = d
        return track_request

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
