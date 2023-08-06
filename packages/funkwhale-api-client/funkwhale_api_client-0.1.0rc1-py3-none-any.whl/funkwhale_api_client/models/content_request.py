from typing import Any, Dict, List, Optional, Type, TypeVar

import attr

from ..models.content_type_enum import ContentTypeEnum

T = TypeVar("T", bound="ContentRequest")


@attr.s(auto_attribs=True)
class ContentRequest:
    """
    Attributes:
        content_type (ContentTypeEnum):
        text (Optional[str]):
    """

    content_type: ContentTypeEnum
    text: Optional[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content_type = self.content_type.value

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        content_type = ContentTypeEnum(d.pop("content_type"))

        text = d.pop("text")

        content_request = cls(
            content_type=content_type,
            text=text,
        )

        content_request.additional_properties = d
        return content_request

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
