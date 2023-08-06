import datetime
import json
from typing import Any, Dict, List, Optional, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.api_actor_request import APIActorRequest
from ..models.artist_album_request import ArtistAlbumRequest
from ..models.artist_with_albums_inline_channel_request import ArtistWithAlbumsInlineChannelRequest
from ..models.cover_field_request import CoverFieldRequest
from ..types import Unset

T = TypeVar("T", bound="ArtistWithAlbumsRequest")


@attr.s(auto_attribs=True)
class ArtistWithAlbumsRequest:
    """
    Attributes:
        albums (List[ArtistAlbumRequest]):
        id (int):
        fid (str):
        mbid (str):
        name (str):
        content_category (str):
        creation_date (datetime.datetime):
        is_local (bool):
        attributed_to (Optional[APIActorRequest]):
        channel (Optional[ArtistWithAlbumsInlineChannelRequest]):
        cover (Optional[CoverFieldRequest]):
    """

    albums: List[ArtistAlbumRequest]
    id: int
    fid: str
    mbid: str
    name: str
    content_category: str
    creation_date: datetime.datetime
    is_local: bool
    attributed_to: Optional[APIActorRequest]
    channel: Optional[ArtistWithAlbumsInlineChannelRequest]
    cover: Optional[CoverFieldRequest]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        albums = []
        for albums_item_data in self.albums:
            albums_item = albums_item_data.to_dict()

            albums.append(albums_item)

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

    def to_multipart(self) -> Dict[str, Any]:
        _temp_albums = []
        for albums_item_data in self.albums:
            albums_item = albums_item_data.to_dict()

            _temp_albums.append(albums_item)
        albums = (None, json.dumps(_temp_albums).encode(), "application/json")

        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")
        fid = self.fid if isinstance(self.fid, Unset) else (None, str(self.fid).encode(), "text/plain")
        mbid = self.mbid if isinstance(self.mbid, Unset) else (None, str(self.mbid).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        content_category = (
            self.content_category
            if isinstance(self.content_category, Unset)
            else (None, str(self.content_category).encode(), "text/plain")
        )
        creation_date = self.creation_date.isoformat().encode()

        is_local = (
            self.is_local if isinstance(self.is_local, Unset) else (None, str(self.is_local).encode(), "text/plain")
        )
        attributed_to = (
            (None, json.dumps(self.attributed_to.to_dict()).encode(), "application/json")
            if self.attributed_to
            else None
        )

        channel = (None, json.dumps(self.channel.to_dict()).encode(), "application/json") if self.channel else None

        cover = (None, json.dumps(self.cover.to_dict()).encode(), "application/json") if self.cover else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "albums": albums,
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
            albums_item = ArtistAlbumRequest.from_dict(albums_item_data)

            albums.append(albums_item)

        id = d.pop("id")

        fid = d.pop("fid")

        mbid = d.pop("mbid")

        name = d.pop("name")

        content_category = d.pop("content_category")

        creation_date = isoparse(d.pop("creation_date"))

        is_local = d.pop("is_local")

        _attributed_to = d.pop("attributed_to")
        attributed_to: Optional[APIActorRequest]
        if _attributed_to is None:
            attributed_to = None
        else:
            attributed_to = APIActorRequest.from_dict(_attributed_to)

        _channel = d.pop("channel")
        channel: Optional[ArtistWithAlbumsInlineChannelRequest]
        if _channel is None:
            channel = None
        else:
            channel = ArtistWithAlbumsInlineChannelRequest.from_dict(_channel)

        _cover = d.pop("cover")
        cover: Optional[CoverFieldRequest]
        if _cover is None:
            cover = None
        else:
            cover = CoverFieldRequest.from_dict(_cover)

        artist_with_albums_request = cls(
            albums=albums,
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

        artist_with_albums_request.additional_properties = d
        return artist_with_albums_request

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
