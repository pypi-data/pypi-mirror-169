import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.channel_update_request_metadata import ChannelUpdateRequestMetadata
from ..models.content_category_enum import ContentCategoryEnum
from ..models.content_request import ContentRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelUpdateRequest")


@attr.s(auto_attribs=True)
class ChannelUpdateRequest:
    """
    Attributes:
        name (str):
        tags (List[str]):
        content_category (ContentCategoryEnum):
        cover (Union[Unset, None, str]):
        description (Optional[ContentRequest]):
        metadata (Union[Unset, ChannelUpdateRequestMetadata]):
    """

    name: str
    tags: List[str]
    content_category: ContentCategoryEnum
    description: Optional[ContentRequest]
    cover: Union[Unset, None, str] = UNSET
    metadata: Union[Unset, ChannelUpdateRequestMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        tags = self.tags

        content_category = self.content_category.value

        cover = self.cover
        description = self.description.to_dict() if self.description else None

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "tags": tags,
                "content_category": content_category,
                "description": description,
            }
        )
        if cover is not UNSET:
            field_dict["cover"] = cover
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        _temp_tags = self.tags
        tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        content_category = (None, str(self.content_category.value).encode(), "text/plain")

        cover = self.cover if isinstance(self.cover, Unset) else (None, str(self.cover).encode(), "text/plain")
        description = (
            (None, json.dumps(self.description.to_dict()).encode(), "application/json") if self.description else None
        )

        metadata: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = (None, json.dumps(self.metadata.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
                "tags": tags,
                "content_category": content_category,
                "description": description,
            }
        )
        if cover is not UNSET:
            field_dict["cover"] = cover
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        tags = cast(List[str], d.pop("tags"))

        content_category = ContentCategoryEnum(d.pop("content_category"))

        cover = d.pop("cover", UNSET)

        _description = d.pop("description")
        description: Optional[ContentRequest]
        if _description is None:
            description = None
        else:
            description = ContentRequest.from_dict(_description)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ChannelUpdateRequestMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ChannelUpdateRequestMetadata.from_dict(_metadata)

        channel_update_request = cls(
            name=name,
            tags=tags,
            content_category=content_category,
            cover=cover,
            description=description,
            metadata=metadata,
        )

        channel_update_request.additional_properties = d
        return channel_update_request

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
