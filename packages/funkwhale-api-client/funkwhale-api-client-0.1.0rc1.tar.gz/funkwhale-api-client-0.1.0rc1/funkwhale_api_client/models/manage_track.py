import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.cover_field import CoverField
from ..models.manage_base_actor import ManageBaseActor
from ..models.manage_nested_artist import ManageNestedArtist
from ..models.manage_track_album import ManageTrackAlbum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageTrack")


@attr.s(auto_attribs=True)
class ManageTrack:
    """
    Attributes:
        id (int):
        title (str):
        domain (str):
        is_local (bool):
        artist (ManageNestedArtist):
        uploads_count (int):
        tags (List[str]):
        cover (CoverField):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        position (Union[Unset, None, int]):
        disc_number (Union[Unset, None, int]):
        copyright_ (Union[Unset, None, str]):
        license_ (Union[Unset, None, str]):
        album (Optional[ManageTrackAlbum]):
        attributed_to (Optional[ManageBaseActor]):
    """

    id: int
    title: str
    domain: str
    is_local: bool
    artist: ManageNestedArtist
    uploads_count: int
    tags: List[str]
    cover: CoverField
    album: Optional[ManageTrackAlbum]
    attributed_to: Optional[ManageBaseActor]
    fid: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    position: Union[Unset, None, int] = UNSET
    disc_number: Union[Unset, None, int] = UNSET
    copyright_: Union[Unset, None, str] = UNSET
    license_: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        domain = self.domain
        is_local = self.is_local
        artist = self.artist.to_dict()

        uploads_count = self.uploads_count
        tags = self.tags

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
                "id": id,
                "title": title,
                "domain": domain,
                "is_local": is_local,
                "artist": artist,
                "uploads_count": uploads_count,
                "tags": tags,
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
        id = d.pop("id")

        title = d.pop("title")

        domain = d.pop("domain")

        is_local = d.pop("is_local")

        artist = ManageNestedArtist.from_dict(d.pop("artist"))

        uploads_count = d.pop("uploads_count")

        tags = cast(List[str], d.pop("tags"))

        cover = CoverField.from_dict(d.pop("cover"))

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
        album: Optional[ManageTrackAlbum]
        if _album is None:
            album = None
        else:
            album = ManageTrackAlbum.from_dict(_album)

        _attributed_to = d.pop("attributed_to")
        attributed_to: Optional[ManageBaseActor]
        if _attributed_to is None:
            attributed_to = None
        else:
            attributed_to = ManageBaseActor.from_dict(_attributed_to)

        manage_track = cls(
            id=id,
            title=title,
            domain=domain,
            is_local=is_local,
            artist=artist,
            uploads_count=uploads_count,
            tags=tags,
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

        manage_track.additional_properties = d
        return manage_track

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
