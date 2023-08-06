import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="Subscription")


@attr.s(auto_attribs=True)
class Subscription:
    """
    Attributes:
        approved (bool):
        fid (str):
        uuid (str):
        creation_date (datetime.datetime):
    """

    approved: bool
    fid: str
    uuid: str
    creation_date: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        approved = self.approved
        fid = self.fid
        uuid = self.uuid
        creation_date = self.creation_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "approved": approved,
                "fid": fid,
                "uuid": uuid,
                "creation_date": creation_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        approved = d.pop("approved")

        fid = d.pop("fid")

        uuid = d.pop("uuid")

        creation_date = isoparse(d.pop("creation_date"))

        subscription = cls(
            approved=approved,
            fid=fid,
            uuid=uuid,
            creation_date=creation_date,
        )

        subscription.additional_properties = d
        return subscription

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
