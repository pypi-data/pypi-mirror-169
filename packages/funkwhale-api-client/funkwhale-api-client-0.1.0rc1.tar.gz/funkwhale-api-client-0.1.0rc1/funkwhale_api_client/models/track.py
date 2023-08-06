import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.cover_field import CoverField
from ..models.simple_artist import SimpleArtist
from ..models.track_album import TrackAlbum
from ..models.track_uploads_item import TrackUploadsItem

T = TypeVar("T", bound="Track")


@attr.s(auto_attribs=True)
class Track:
    """
    Attributes:
        artist (SimpleArtist):
        album (TrackAlbum):
        uploads (List[TrackUploadsItem]):
        listen_url (str):
        tags (List[str]):
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
        license_ (str):
        is_playable (bool):
        attributed_to (Optional[APIActor]):
        cover (Optional[CoverField]):
    """

    artist: SimpleArtist
    album: TrackAlbum
    uploads: List[TrackUploadsItem]
    listen_url: str
    tags: List[str]
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
    license_: str
    is_playable: bool
    attributed_to: Optional[APIActor]
    cover: Optional[CoverField]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artist = self.artist.to_dict()

        album = self.album.to_dict()

        uploads = []
        for uploads_item_data in self.uploads:
            uploads_item = uploads_item_data.to_dict()

            uploads.append(uploads_item)

        listen_url = self.listen_url
        tags = self.tags

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
        license_ = self.license_
        is_playable = self.is_playable
        attributed_to = self.attributed_to.to_dict() if self.attributed_to else None

        cover = self.cover.to_dict() if self.cover else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "artist": artist,
                "album": album,
                "uploads": uploads,
                "listen_url": listen_url,
                "tags": tags,
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
                "license": license_,
                "is_playable": is_playable,
                "attributed_to": attributed_to,
                "cover": cover,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        artist = SimpleArtist.from_dict(d.pop("artist"))

        album = TrackAlbum.from_dict(d.pop("album"))

        uploads = []
        _uploads = d.pop("uploads")
        for uploads_item_data in _uploads:
            uploads_item = TrackUploadsItem.from_dict(uploads_item_data)

            uploads.append(uploads_item)

        listen_url = d.pop("listen_url")

        tags = cast(List[str], d.pop("tags"))

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

        license_ = d.pop("license")

        is_playable = d.pop("is_playable")

        _attributed_to = d.pop("attributed_to")
        attributed_to: Optional[APIActor]
        if _attributed_to is None:
            attributed_to = None
        else:
            attributed_to = APIActor.from_dict(_attributed_to)

        _cover = d.pop("cover")
        cover: Optional[CoverField]
        if _cover is None:
            cover = None
        else:
            cover = CoverField.from_dict(_cover)

        track = cls(
            artist=artist,
            album=album,
            uploads=uploads,
            listen_url=listen_url,
            tags=tags,
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
            license_=license_,
            is_playable=is_playable,
            attributed_to=attributed_to,
            cover=cover,
        )

        track.additional_properties = d
        return track

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
