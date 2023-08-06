import datetime
import json
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.api_actor_request import APIActorRequest
from ..models.cover_field_request import CoverFieldRequest
from ..models.simple_artist_request import SimpleArtistRequest
from ..types import Unset

T = TypeVar("T", bound="AlbumRequest")


@attr.s(auto_attribs=True)
class AlbumRequest:
    """
    Attributes:
        artist (SimpleArtistRequest):
        attributed_to (APIActorRequest):
        id (int):
        fid (str):
        mbid (str):
        title (str):
        release_date (datetime.date):
        creation_date (datetime.datetime):
        is_local (bool):
        cover (Optional[CoverFieldRequest]):
    """

    artist: SimpleArtistRequest
    attributed_to: APIActorRequest
    id: int
    fid: str
    mbid: str
    title: str
    release_date: datetime.date
    creation_date: datetime.datetime
    is_local: bool
    cover: Optional[CoverFieldRequest]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artist = self.artist.to_dict()

        attributed_to = self.attributed_to.to_dict()

        id = self.id
        fid = self.fid
        mbid = self.mbid
        title = self.title
        release_date = self.release_date.isoformat()
        creation_date = self.creation_date.isoformat()

        is_local = self.is_local
        cover = self.cover.to_dict() if self.cover else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artist": artist,
                "attributed_to": attributed_to,
                "id": id,
                "fid": fid,
                "mbid": mbid,
                "title": title,
                "release_date": release_date,
                "creation_date": creation_date,
                "is_local": is_local,
                "cover": cover,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        artist = (None, json.dumps(self.artist.to_dict()).encode(), "application/json")

        attributed_to = (None, json.dumps(self.attributed_to.to_dict()).encode(), "application/json")

        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        fid = self.fid if isinstance(self.fid, Unset) else (None, str(self.fid).encode(), "text/plain")
        mbid = self.mbid if isinstance(self.mbid, Unset) else (None, str(self.mbid).encode(), "text/plain")
        title = self.title if isinstance(self.title, Unset) else (None, str(self.title).encode(), "text/plain")
        release_date = self.release_date.isoformat().encode()
        creation_date = self.creation_date.isoformat().encode()

        is_local = (
            self.is_local if isinstance(self.is_local, Unset) else (None, str(self.is_local).encode(), "text/plain")
        )
        cover = (None, json.dumps(self.cover.to_dict()).encode(), "application/json") if self.cover else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "artist": artist,
                "attributed_to": attributed_to,
                "id": id,
                "fid": fid,
                "mbid": mbid,
                "title": title,
                "release_date": release_date,
                "creation_date": creation_date,
                "is_local": is_local,
                "cover": cover,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        artist = SimpleArtistRequest.from_dict(d.pop("artist"))

        attributed_to = APIActorRequest.from_dict(d.pop("attributed_to"))

        id = d.pop("id")

        fid = d.pop("fid")

        mbid = d.pop("mbid")

        title = d.pop("title")

        release_date = isoparse(d.pop("release_date")).date()

        creation_date = isoparse(d.pop("creation_date"))

        is_local = d.pop("is_local")

        _cover = d.pop("cover")
        cover: Optional[CoverFieldRequest]
        if _cover is None:
            cover = None
        else:
            cover = CoverFieldRequest.from_dict(_cover)

        album_request = cls(
            artist=artist,
            attributed_to=attributed_to,
            id=id,
            fid=fid,
            mbid=mbid,
            title=title,
            release_date=release_date,
            creation_date=creation_date,
            is_local=is_local,
            cover=cover,
        )

        album_request.additional_properties = d
        return album_request

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
