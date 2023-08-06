import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union, cast

import attr

from ..models.content_category_enum import ContentCategoryEnum
from ..models.content_request import ContentRequest
from ..models.patched_channel_update_request_metadata import PatchedChannelUpdateRequestMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedChannelUpdateRequest")


@attr.s(auto_attribs=True)
class PatchedChannelUpdateRequest:
    """
    Attributes:
        cover (Union[Unset, None, str]):
        name (Union[Unset, str]):
        description (Union[Unset, None, ContentRequest]):
        tags (Union[Unset, List[str]]):
        content_category (Union[Unset, ContentCategoryEnum]):
        metadata (Union[Unset, PatchedChannelUpdateRequestMetadata]):
    """

    cover: Union[Unset, None, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, None, ContentRequest] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    content_category: Union[Unset, ContentCategoryEnum] = UNSET
    metadata: Union[Unset, PatchedChannelUpdateRequestMetadata] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cover = self.cover
        name = self.name
        description: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.description, Unset):
            description = self.description.to_dict() if self.description else None

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        content_category: Union[Unset, str] = UNSET
        if not isinstance(self.content_category, Unset):
            content_category = self.content_category.value

        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cover is not UNSET:
            field_dict["cover"] = cover
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if content_category is not UNSET:
            field_dict["content_category"] = content_category
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        cover = self.cover if isinstance(self.cover, Unset) else (None, str(self.cover).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        description: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.description, Unset):
            description = (
                (None, json.dumps(self.description.to_dict()).encode(), "application/json")
                if self.description
                else None
            )

        tags: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tags, Unset):
            _temp_tags = self.tags
            tags = (None, json.dumps(_temp_tags).encode(), "application/json")

        content_category: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.content_category, Unset):
            content_category = (None, str(self.content_category.value).encode(), "text/plain")

        metadata: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = (None, json.dumps(self.metadata.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if cover is not UNSET:
            field_dict["cover"] = cover
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if content_category is not UNSET:
            field_dict["content_category"] = content_category
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cover = d.pop("cover", UNSET)

        name = d.pop("name", UNSET)

        _description = d.pop("description", UNSET)
        description: Union[Unset, None, ContentRequest]
        if _description is None:
            description = None
        elif isinstance(_description, Unset):
            description = UNSET
        else:
            description = ContentRequest.from_dict(_description)

        tags = cast(List[str], d.pop("tags", UNSET))

        _content_category = d.pop("content_category", UNSET)
        content_category: Union[Unset, ContentCategoryEnum]
        if isinstance(_content_category, Unset):
            content_category = UNSET
        else:
            content_category = ContentCategoryEnum(_content_category)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, PatchedChannelUpdateRequestMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PatchedChannelUpdateRequestMetadata.from_dict(_metadata)

        patched_channel_update_request = cls(
            cover=cover,
            name=name,
            description=description,
            tags=tags,
            content_category=content_category,
            metadata=metadata,
        )

        patched_channel_update_request.additional_properties = d
        return patched_channel_update_request

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
