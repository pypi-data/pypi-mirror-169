import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.cover_field_request import CoverFieldRequest

T = TypeVar("T", bound="ArtistAlbumRequest")


@attr.s(auto_attribs=True)
class ArtistAlbumRequest:
    """
    Attributes:
        is_local (bool):
        id (int):
        fid (str):
        mbid (str):
        title (str):
        release_date (datetime.date):
        creation_date (datetime.datetime):
        cover (Optional[CoverFieldRequest]):
    """

    is_local: bool
    id: int
    fid: str
    mbid: str
    title: str
    release_date: datetime.date
    creation_date: datetime.datetime
    cover: Optional[CoverFieldRequest]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_local = self.is_local
        id = self.id
        fid = self.fid
        mbid = self.mbid
        title = self.title
        release_date = self.release_date.isoformat()
        creation_date = self.creation_date.isoformat()

        cover = self.cover.to_dict() if self.cover else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "is_local": is_local,
                "id": id,
                "fid": fid,
                "mbid": mbid,
                "title": title,
                "release_date": release_date,
                "creation_date": creation_date,
                "cover": cover,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_local = d.pop("is_local")

        id = d.pop("id")

        fid = d.pop("fid")

        mbid = d.pop("mbid")

        title = d.pop("title")

        release_date = isoparse(d.pop("release_date")).date()

        creation_date = isoparse(d.pop("creation_date"))

        _cover = d.pop("cover")
        cover: Optional[CoverFieldRequest]
        if _cover is None:
            cover = None
        else:
            cover = CoverFieldRequest.from_dict(_cover)

        artist_album_request = cls(
            is_local=is_local,
            id=id,
            fid=fid,
            mbid=mbid,
            title=title,
            release_date=release_date,
            creation_date=creation_date,
            cover=cover,
        )

        artist_album_request.additional_properties = d
        return artist_album_request

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
