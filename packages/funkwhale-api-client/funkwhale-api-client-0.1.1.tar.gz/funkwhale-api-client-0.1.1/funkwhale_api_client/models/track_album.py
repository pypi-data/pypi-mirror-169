import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cover_field import CoverField
from ..models.simple_artist import SimpleArtist
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackAlbum")


@attr.s(auto_attribs=True)
class TrackAlbum:
    """
    Attributes:
        id (int):
        title (str):
        artist (SimpleArtist):
        is_local (bool):
        tracks_count (int):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        release_date (Union[Unset, None, datetime.date]):
        cover (Optional[CoverField]):
        creation_date (Union[Unset, datetime.datetime]):
    """

    id: int
    title: str
    artist: SimpleArtist
    is_local: bool
    tracks_count: int
    cover: Optional[CoverField]
    fid: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    release_date: Union[Unset, None, datetime.date] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        artist = self.artist.to_dict()

        is_local = self.is_local
        tracks_count = self.tracks_count
        fid = self.fid
        mbid = self.mbid
        release_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat() if self.release_date else None

        cover = self.cover.to_dict() if self.cover else None

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "artist": artist,
                "is_local": is_local,
                "tracks_count": tracks_count,
                "cover": cover,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        title = d.pop("title")

        artist = SimpleArtist.from_dict(d.pop("artist"))

        is_local = d.pop("is_local")

        tracks_count = d.pop("tracks_count")

        fid = d.pop("fid", UNSET)

        mbid = d.pop("mbid", UNSET)

        _release_date = d.pop("release_date", UNSET)
        release_date: Union[Unset, None, datetime.date]
        if _release_date is None:
            release_date = None
        elif isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        _cover = d.pop("cover")
        cover: Optional[CoverField]
        if _cover is None:
            cover = None
        else:
            cover = CoverField.from_dict(_cover)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        track_album = cls(
            id=id,
            title=title,
            artist=artist,
            is_local=is_local,
            tracks_count=tracks_count,
            fid=fid,
            mbid=mbid,
            release_date=release_date,
            cover=cover,
            creation_date=creation_date,
        )

        track_album.additional_properties = d
        return track_album

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
