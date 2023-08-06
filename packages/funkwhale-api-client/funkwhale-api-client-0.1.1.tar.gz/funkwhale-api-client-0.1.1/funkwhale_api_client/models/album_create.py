import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.content import Content
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlbumCreate")


@attr.s(auto_attribs=True)
class AlbumCreate:
    """
    Attributes:
        title (str):
        artist (str):
        release_date (Union[Unset, None, datetime.date]):
        tags (Union[Unset, List[str]]):
        description (Union[Unset, None, Content]):
    """

    title: str
    artist: str
    release_date: Union[Unset, None, datetime.date] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    description: Union[Unset, None, Content] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        artist = self.artist
        release_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat() if self.release_date else None

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        description: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict() if self.description else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "artist": artist,
            }
        )
        if release_date is not UNSET:
            field_dict["release_date"] = release_date
        if tags is not UNSET:
            field_dict["tags"] = tags
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title")

        artist = d.pop("artist")

        _release_date = d.pop("release_date", UNSET)
        release_date: Union[Unset, None, datetime.date]
        if _release_date is None:
            release_date = None
        elif isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        tags = cast(List[str], d.pop("tags", UNSET))

        _description = d.pop("description", UNSET)
        description: Union[Unset, None, Content]
        if _description is None:
            description = None
        elif isinstance(_description, Unset):
            description = UNSET
        else:
            description = Content.from_dict(_description)

        album_create = cls(
            title=title,
            artist=artist,
            release_date=release_date,
            tags=tags,
            description=description,
        )

        album_create.additional_properties = d
        return album_create

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
