from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.activity import Activity
from ..models.inbox_item_type_enum import InboxItemTypeEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="InboxItem")


@attr.s(auto_attribs=True)
class InboxItem:
    """
    Attributes:
        id (int):
        type (InboxItemTypeEnum):
        activity (Activity):
        is_read (Union[Unset, bool]):
    """

    id: int
    type: InboxItemTypeEnum
    activity: Activity
    is_read: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        activity = self.activity.to_dict()

        is_read = self.is_read

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "activity": activity,
            }
        )
        if is_read is not UNSET:
            field_dict["is_read"] = is_read

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        type = InboxItemTypeEnum(d.pop("type"))

        activity = Activity.from_dict(d.pop("activity"))

        is_read = d.pop("is_read", UNSET)

        inbox_item = cls(
            id=id,
            type=type,
            activity=activity,
            is_read=is_read,
        )

        inbox_item.additional_properties = d
        return inbox_item

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
