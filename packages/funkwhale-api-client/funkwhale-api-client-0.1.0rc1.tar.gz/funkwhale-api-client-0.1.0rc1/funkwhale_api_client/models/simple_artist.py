import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.content import Content
from ..models.content_category_enum import ContentCategoryEnum
from ..models.cover_field import CoverField
from ..types import UNSET, Unset

T = TypeVar("T", bound="SimpleArtist")


@attr.s(auto_attribs=True)
class SimpleArtist:
    """
    Attributes:
        id (int):
        name (str):
        is_local (bool):
        fid (Union[Unset, None, str]):
        mbid (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        modification_date (Union[Unset, datetime.datetime]):
        content_category (Union[Unset, ContentCategoryEnum]):
        description (Union[Unset, None, Content]):
        attachment_cover (Union[Unset, None, CoverField]):
        channel (Union[Unset, None, str]):
    """

    id: int
    name: str
    is_local: bool
    fid: Union[Unset, None, str] = UNSET
    mbid: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    modification_date: Union[Unset, datetime.datetime] = UNSET
    content_category: Union[Unset, ContentCategoryEnum] = UNSET
    description: Union[Unset, None, Content] = UNSET
    attachment_cover: Union[Unset, None, CoverField] = UNSET
    channel: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        is_local = self.is_local
        fid = self.fid
        mbid = self.mbid
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        modification_date: Union[Unset, str] = UNSET
        if not isinstance(self.modification_date, Unset):
            modification_date = self.modification_date.isoformat()

        content_category: Union[Unset, str] = UNSET
        if not isinstance(self.content_category, Unset):
            content_category = self.content_category.value

        description: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict() if self.description else None

        attachment_cover: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.attachment_cover, Unset):
            attachment_cover = self.attachment_cover.to_dict() if self.attachment_cover else None

        channel = self.channel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "is_local": is_local,
            }
        )
        if fid is not UNSET:
            field_dict["fid"] = fid
        if mbid is not UNSET:
            field_dict["mbid"] = mbid
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if modification_date is not UNSET:
            field_dict["modification_date"] = modification_date
        if content_category is not UNSET:
            field_dict["content_category"] = content_category
        if description is not UNSET:
            field_dict["description"] = description
        if attachment_cover is not UNSET:
            field_dict["attachment_cover"] = attachment_cover
        if channel is not UNSET:
            field_dict["channel"] = channel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        name = d.pop("name")

        is_local = d.pop("is_local")

        fid = d.pop("fid", UNSET)

        mbid = d.pop("mbid", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _modification_date = d.pop("modification_date", UNSET)
        modification_date: Union[Unset, datetime.datetime]
        if isinstance(_modification_date, Unset):
            modification_date = UNSET
        else:
            modification_date = isoparse(_modification_date)

        _content_category = d.pop("content_category", UNSET)
        content_category: Union[Unset, ContentCategoryEnum]
        if isinstance(_content_category, Unset):
            content_category = UNSET
        else:
            content_category = ContentCategoryEnum(_content_category)

        _description = d.pop("description", UNSET)
        description: Union[Unset, None, Content]
        if _description is None:
            description = None
        elif isinstance(_description, Unset):
            description = UNSET
        else:
            description = Content.from_dict(_description)

        _attachment_cover = d.pop("attachment_cover", UNSET)
        attachment_cover: Union[Unset, None, CoverField]
        if _attachment_cover is None:
            attachment_cover = None
        elif isinstance(_attachment_cover, Unset):
            attachment_cover = UNSET
        else:
            attachment_cover = CoverField.from_dict(_attachment_cover)

        channel = d.pop("channel", UNSET)

        simple_artist = cls(
            id=id,
            name=name,
            is_local=is_local,
            fid=fid,
            mbid=mbid,
            creation_date=creation_date,
            modification_date=modification_date,
            content_category=content_category,
            description=description,
            attachment_cover=attachment_cover,
            channel=channel,
        )

        simple_artist.additional_properties = d
        return simple_artist

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
