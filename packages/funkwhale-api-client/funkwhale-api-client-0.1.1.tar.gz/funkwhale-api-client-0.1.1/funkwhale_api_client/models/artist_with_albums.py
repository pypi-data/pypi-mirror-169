import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.artist_album import ArtistAlbum
from ..models.artist_with_albums_inline_channel import ArtistWithAlbumsInlineChannel
from ..models.cover_field import CoverField

T = TypeVar("T", bound="ArtistWithAlbums")


@attr.s(auto_attribs=True)
class ArtistWithAlbums:
    """
    Attributes:
        albums (List[ArtistAlbum]):
        tags (List[str]):
        tracks_count (int):
        id (int):
        fid (str):
        mbid (str):
        name (str):
        content_category (str):
        creation_date (datetime.datetime):
        is_local (bool):
        attributed_to (Optional[APIActor]):
        channel (Optional[ArtistWithAlbumsInlineChannel]):
        cover (Optional[CoverField]):
    """

    albums: List[ArtistAlbum]
    tags: List[str]
    tracks_count: int
    id: int
    fid: str
    mbid: str
    name: str
    content_category: str
    creation_date: datetime.datetime
    is_local: bool
    attributed_to: Optional[APIActor]
    channel: Optional[ArtistWithAlbumsInlineChannel]
    cover: Optional[CoverField]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        albums = []
        for albums_item_data in self.albums:
            albums_item = albums_item_data.to_dict()

            albums.append(albums_item)

        tags = self.tags

        tracks_count = self.tracks_count
        id = self.id
        fid = self.fid
        mbid = self.mbid
        name = self.name
        content_category = self.content_category
        creation_date = self.creation_date.isoformat()

        is_local = self.is_local
        attributed_to = self.attributed_to.to_dict() if self.attributed_to else None

        channel = self.channel.to_dict() if self.channel else None

        cover = self.cover.to_dict() if self.cover else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "albums": albums,
                "tags": tags,
                "tracks_count": tracks_count,
                "id": id,
                "fid": fid,
                "mbid": mbid,
                "name": name,
                "content_category": content_category,
                "creation_date": creation_date,
                "is_local": is_local,
                "attributed_to": attributed_to,
                "channel": channel,
                "cover": cover,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        albums = []
        _albums = d.pop("albums")
        for albums_item_data in _albums:
            albums_item = ArtistAlbum.from_dict(albums_item_data)

            albums.append(albums_item)

        tags = cast(List[str], d.pop("tags"))

        tracks_count = d.pop("tracks_count")

        id = d.pop("id")

        fid = d.pop("fid")

        mbid = d.pop("mbid")

        name = d.pop("name")

        content_category = d.pop("content_category")

        creation_date = isoparse(d.pop("creation_date"))

        is_local = d.pop("is_local")

        _attributed_to = d.pop("attributed_to")
        attributed_to: Optional[APIActor]
        if _attributed_to is None:
            attributed_to = None
        else:
            attributed_to = APIActor.from_dict(_attributed_to)

        _channel = d.pop("channel")
        channel: Optional[ArtistWithAlbumsInlineChannel]
        if _channel is None:
            channel = None
        else:
            channel = ArtistWithAlbumsInlineChannel.from_dict(_channel)

        _cover = d.pop("cover")
        cover: Optional[CoverField]
        if _cover is None:
            cover = None
        else:
            cover = CoverField.from_dict(_cover)

        artist_with_albums = cls(
            albums=albums,
            tags=tags,
            tracks_count=tracks_count,
            id=id,
            fid=fid,
            mbid=mbid,
            name=name,
            content_category=content_category,
            creation_date=creation_date,
            is_local=is_local,
            attributed_to=attributed_to,
            channel=channel,
            cover=cover,
        )

        artist_with_albums.additional_properties = d
        return artist_with_albums

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
