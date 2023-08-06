import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.moderation_target import ModerationTarget

T = TypeVar("T", bound="UserFilter")


@attr.s(auto_attribs=True)
class UserFilter:
    """
    Attributes:
        uuid (str):
        target (ModerationTarget):
        creation_date (datetime.datetime):
    """

    uuid: str
    target: ModerationTarget
    creation_date: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        target = self.target.to_dict()

        creation_date = self.creation_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "target": target,
                "creation_date": creation_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        target = ModerationTarget.from_dict(d.pop("target"))

        creation_date = isoparse(d.pop("creation_date"))

        user_filter = cls(
            uuid=uuid,
            target=target,
            creation_date=creation_date,
        )

        user_filter.additional_properties = d
        return user_filter

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
