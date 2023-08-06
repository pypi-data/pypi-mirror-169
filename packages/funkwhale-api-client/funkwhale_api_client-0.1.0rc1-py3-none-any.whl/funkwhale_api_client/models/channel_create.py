from typing import Any, Dict, List, Optional, Type, TypeVar, Union, cast

import attr

from ..models.channel_create_metadata import ChannelCreateMetadata
from ..models.content import Content
from ..models.content_category_enum import ContentCategoryEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelCreate")


@attr.s(auto_attribs=True)
class ChannelCreate:
    """
    Attributes:
        name (str):
        username (str):
        tags (List[str]):
        content_category (ContentCategoryEnum):
        description (Optional[Content]):
        metadata (Union[Unset, ChannelCreateMetadata]):
    """

    name: str
    username: str
    tags: List[str]
    content_category: ContentCategoryEnum
    description: Optional[Content]
    metadata: Union[Unset, ChannelCreateMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        username = self.username
        tags = self.tags

        content_category = self.content_category.value

        description = self.description.to_dict() if self.description else None

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "username": username,
                "tags": tags,
                "content_category": content_category,
                "description": description,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        username = d.pop("username")

        tags = cast(List[str], d.pop("tags"))

        content_category = ContentCategoryEnum(d.pop("content_category"))

        _description = d.pop("description")
        description: Optional[Content]
        if _description is None:
            description = None
        else:
            description = Content.from_dict(_description)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ChannelCreateMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ChannelCreateMetadata.from_dict(_metadata)

        channel_create = cls(
            name=name,
            username=username,
            tags=tags,
            content_category=content_category,
            description=description,
            metadata=metadata,
        )

        channel_create.additional_properties = d
        return channel_create

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
