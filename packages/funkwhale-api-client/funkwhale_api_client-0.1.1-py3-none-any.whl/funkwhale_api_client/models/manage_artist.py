import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.content_category_enum import ContentCategoryEnum
from ..models.cover_field import CoverField
from ..models.manage_base_actor import ManageBaseActor
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageArtist")


@attr.s(auto_attribs=True)
class ManageArtist:
    """
    Attributes:
        id (int):
        name (str):
        domain (str):
        is_local (bool):
        tracks_count (int):
        albums_count (int):
        attributed_to (ManageBaseActor):
        tags (List[str]):
        channel (str):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        cover (Optional[CoverField]):
        content_category (Union[Unset, ContentCategoryEnum]):
    """

    id: int
    name: str
    domain: str
    is_local: bool
    tracks_count: int
    albums_count: int
    attributed_to: ManageBaseActor
    tags: List[str]
    channel: str
    cover: Optional[CoverField]
    fid: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    content_category: Union[Unset, ContentCategoryEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        domain = self.domain
        is_local = self.is_local
        tracks_count = self.tracks_count
        albums_count = self.albums_count
        attributed_to = self.attributed_to.to_dict()

        tags = self.tags

        channel = self.channel
        fid = self.fid
        mbid = self.mbid
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        cover = self.cover.to_dict() if self.cover else None

        content_category: Union[Unset, str] = UNSET
        if not isinstance(self.content_category, Unset):
            content_category = self.content_category.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "domain": domain,
                "is_local": is_local,
                "tracks_count": tracks_count,
                "albums_count": albums_count,
                "attributed_to": attributed_to,
                "tags": tags,
                "channel": channel,
                "cover": cover,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if content_category is not UNSET:
            field_dict["content_category"] = content_category

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        domain = d.pop("domain")

        is_local = d.pop("is_local")

        tracks_count = d.pop("tracks_count")

        albums_count = d.pop("albums_count")

        attributed_to = ManageBaseActor.from_dict(d.pop("attributed_to"))

        tags = cast(List[str], d.pop("tags"))

        channel = d.pop("channel")

        fid = d.pop("fid", UNSET)

        mbid = d.pop("mbid", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _cover = d.pop("cover")
        cover: Optional[CoverField]
        if _cover is None:
            cover = None
        else:
            cover = CoverField.from_dict(_cover)

        _content_category = d.pop("content_category", UNSET)
        content_category: Union[Unset, ContentCategoryEnum]
        if isinstance(_content_category, Unset):
            content_category = UNSET
        else:
            content_category = ContentCategoryEnum(_content_category)

        manage_artist = cls(
            id=id,
            name=name,
            domain=domain,
            is_local=is_local,
            tracks_count=tracks_count,
            albums_count=albums_count,
            attributed_to=attributed_to,
            tags=tags,
            channel=channel,
            fid=fid,
            mbid=mbid,
            creation_date=creation_date,
            cover=cover,
            content_category=content_category,
        )

        manage_artist.additional_properties = d
        return manage_artist

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
