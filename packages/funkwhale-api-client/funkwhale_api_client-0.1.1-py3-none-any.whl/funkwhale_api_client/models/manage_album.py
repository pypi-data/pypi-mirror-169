import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.cover_field import CoverField
from ..models.manage_base_actor import ManageBaseActor
from ..models.manage_nested_artist import ManageNestedArtist
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageAlbum")


@attr.s(auto_attribs=True)
class ManageAlbum:
    """
    Attributes:
        id (int):
        title (str):
        cover (CoverField):
        domain (str):
        is_local (bool):
        tracks_count (int):
        artist (ManageNestedArtist):
        attributed_to (ManageBaseActor):
        tags (List[str]):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        release_date (Union[Unset, None, datetime.date]):
    """

    id: int
    title: str
    cover: CoverField
    domain: str
    is_local: bool
    tracks_count: int
    artist: ManageNestedArtist
    attributed_to: ManageBaseActor
    tags: List[str]
    fid: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    release_date: Union[Unset, None, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        title = self.title
        cover = self.cover.to_dict()

        domain = self.domain
        is_local = self.is_local
        tracks_count = self.tracks_count
        artist = self.artist.to_dict()

        attributed_to = self.attributed_to.to_dict()

        tags = self.tags

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
                "id": id,
                "title": title,
                "cover": cover,
                "domain": domain,
                "is_local": is_local,
                "tracks_count": tracks_count,
                "artist": artist,
                "attributed_to": attributed_to,
                "tags": tags,
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
        id = d.pop("id")

        title = d.pop("title")

        cover = CoverField.from_dict(d.pop("cover"))

        domain = d.pop("domain")

        is_local = d.pop("is_local")

        tracks_count = d.pop("tracks_count")

        artist = ManageNestedArtist.from_dict(d.pop("artist"))

        attributed_to = ManageBaseActor.from_dict(d.pop("attributed_to"))

        tags = cast(List[str], d.pop("tags"))

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

        manage_album = cls(
            id=id,
            title=title,
            cover=cover,
            domain=domain,
            is_local=is_local,
            tracks_count=tracks_count,
            artist=artist,
            attributed_to=attributed_to,
            tags=tags,
            fid=fid,
            mbid=mbid,
            creation_date=creation_date,
            release_date=release_date,
        )

        manage_album.additional_properties = d
        return manage_album

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
