from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.manage_target_type_enum import ManageTargetTypeEnum

T = TypeVar("T", bound="ManageTargetRequest")


@attr.s(auto_attribs=True)
class ManageTargetRequest:
    """
    Attributes:
        type (ManageTargetTypeEnum):
        id (str):
    """

    type: ManageTargetTypeEnum
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
        type = ManageTargetTypeEnum(d.pop("type"))

        id = d.pop("id")

        manage_target_request = cls(
            type=type,
            id=id,
        )

        manage_target_request.additional_properties = d
        return manage_target_request

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
