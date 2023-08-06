from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.moderation_target_type_enum import ModerationTargetTypeEnum

T = TypeVar("T", bound="ModerationTarget")


@attr.s(auto_attribs=True)
class ModerationTarget:
    """
    Attributes:
        type (ModerationTargetTypeEnum):
        id (str):
    """

    type: ModerationTargetTypeEnum
    id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ModerationTargetTypeEnum(d.pop("type"))

        id = d.pop("id")

        moderation_target = cls(
            type=type,
            id=id,
        )

        moderation_target.additional_properties = d
        return moderation_target

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
