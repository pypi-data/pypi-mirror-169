import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.cover_field import CoverField
from ..models.simple_artist import SimpleArtist

T = TypeVar("T", bound="Album")


@attr.s(auto_attribs=True)
class Album:
    """
    Attributes:
        artist (SimpleArtist):
        is_playable (bool):
        tags (List[str]):
        tracks_count (int):
        attributed_to (APIActor):
        id (int):
        fid (str):
        mbid (str):
        title (str):
        release_date (datetime.date):
        creation_date (datetime.datetime):
        is_local (bool):
        duration (int):
        cover (Optional[CoverField]):
    """

    artist: SimpleArtist
    is_playable: bool
    tags: List[str]
    tracks_count: int
    attributed_to: APIActor
    id: int
    fid: str
    mbid: str
    title: str
    release_date: datetime.date
    creation_date: datetime.datetime
    is_local: bool
    duration: int
    cover: Optional[CoverField]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artist = self.artist.to_dict()

        is_playable = self.is_playable
        tags = self.tags

        tracks_count = self.tracks_count
        attributed_to = self.attributed_to.to_dict()

        id = self.id
        fid = self.fid
        mbid = self.mbid
        title = self.title
        release_date = self.release_date.isoformat()
        creation_date = self.creation_date.isoformat()

        is_local = self.is_local
        duration = self.duration
        cover = self.cover.to_dict() if self.cover else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artist": artist,
                "is_playable": is_playable,
                "tags": tags,
                "tracks_count": tracks_count,
                "attributed_to": attributed_to,
                "id": id,
                "fid": fid,
                "mbid": mbid,
                "title": title,
                "release_date": release_date,
                "creation_date": creation_date,
                "is_local": is_local,
                "duration": duration,
                "cover": cover,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        artist = SimpleArtist.from_dict(d.pop("artist"))

        is_playable = d.pop("is_playable")

        tags = cast(List[str], d.pop("tags"))

        tracks_count = d.pop("tracks_count")

        attributed_to = APIActor.from_dict(d.pop("attributed_to"))

        id = d.pop("id")

        fid = d.pop("fid")

        mbid = d.pop("mbid")

        title = d.pop("title")

        release_date = isoparse(d.pop("release_date")).date()

        creation_date = isoparse(d.pop("creation_date"))

        is_local = d.pop("is_local")

        duration = d.pop("duration")

        _cover = d.pop("cover")
        cover: Optional[CoverField]
        if _cover is None:
            cover = None
        else:
            cover = CoverField.from_dict(_cover)

        album = cls(
            artist=artist,
            is_playable=is_playable,
            tags=tags,
            tracks_count=tracks_count,
            attributed_to=attributed_to,
            id=id,
            fid=fid,
            mbid=mbid,
            title=title,
            release_date=release_date,
            creation_date=creation_date,
            is_local=is_local,
            duration=duration,
            cover=cover,
        )

        album.additional_properties = d
        return album

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
