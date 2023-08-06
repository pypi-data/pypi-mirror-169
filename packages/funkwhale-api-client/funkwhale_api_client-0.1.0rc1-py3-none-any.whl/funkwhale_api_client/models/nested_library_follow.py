import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="NestedLibraryFollow")


@attr.s(auto_attribs=True)
class NestedLibraryFollow:
    """
    Attributes:
        modification_date (datetime.datetime):
        creation_date (Union[Unset, datetime.datetime]):
        uuid (Union[Unset, str]):
        fid (Union[Unset, None, str]):
        approved (Union[Unset, None, bool]):
    """

    modification_date: datetime.datetime
    creation_date: Union[Unset, datetime.datetime] = UNSET
    uuid: Union[Unset, str] = UNSET
    fid: Union[Unset, None, str] = UNSET
    approved: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        modification_date = self.modification_date.isoformat()

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        uuid = self.uuid
        fid = self.fid
        approved = self.approved

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modification_date": modification_date,
            }
        )
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if fid is not UNSET:
            field_dict["fid"] = fid
        if approved is not UNSET:
            field_dict["approved"] = approved

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        modification_date = isoparse(d.pop("modification_date"))

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        uuid = d.pop("uuid", UNSET)

        fid = d.pop("fid", UNSET)

        approved = d.pop("approved", UNSET)

        nested_library_follow = cls(
            modification_date=modification_date,
            creation_date=creation_date,
            uuid=uuid,
            fid=fid,
            approved=approved,
        )

        nested_library_follow.additional_properties = d
        return nested_library_follow

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
