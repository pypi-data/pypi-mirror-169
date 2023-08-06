from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="UsersUsage")


@attr.s(auto_attribs=True)
class UsersUsage:
    """
    Attributes:
        total (int):
        active_halfyear (int):
        active_month (int):
    """

    total: int
    active_halfyear: int
    active_month: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        active_halfyear = self.active_halfyear
        active_month = self.active_month

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "activeHalfyear": active_halfyear,
                "activeMonth": active_month,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total = d.pop("total")

        active_halfyear = d.pop("activeHalfyear")

        active_month = d.pop("activeMonth")

        users_usage = cls(
            total=total,
            active_halfyear=active_halfyear,
            active_month=active_month,
        )

        users_usage.additional_properties = d
        return users_usage

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
