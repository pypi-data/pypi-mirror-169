import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryScanRequest")


@attr.s(auto_attribs=True)
class LibraryScanRequest:
    """
    Attributes:
        total_files (Union[Unset, int]):
        processed_files (Union[Unset, int]):
        errored_files (Union[Unset, int]):
        status (Union[Unset, str]):
        creation_date (Union[Unset, datetime.datetime]):
        modification_date (Union[Unset, None, datetime.datetime]):
    """

    total_files: Union[Unset, int] = UNSET
    processed_files: Union[Unset, int] = UNSET
    errored_files: Union[Unset, int] = UNSET
    status: Union[Unset, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    modification_date: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_files = self.total_files
        processed_files = self.processed_files
        errored_files = self.errored_files
        status = self.status
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        modification_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.modification_date, Unset):
            modification_date = self.modification_date.isoformat() if self.modification_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_files is not UNSET:
            field_dict["total_files"] = total_files
        if processed_files is not UNSET:
            field_dict["processed_files"] = processed_files
        if errored_files is not UNSET:
            field_dict["errored_files"] = errored_files
        if status is not UNSET:
            field_dict["status"] = status
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if modification_date is not UNSET:
            field_dict["modification_date"] = modification_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_files = d.pop("total_files", UNSET)

        processed_files = d.pop("processed_files", UNSET)

        errored_files = d.pop("errored_files", UNSET)

        status = d.pop("status", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _modification_date = d.pop("modification_date", UNSET)
        modification_date: Union[Unset, None, datetime.datetime]
        if _modification_date is None:
            modification_date = None
        elif isinstance(_modification_date, Unset):
            modification_date = UNSET
        else:
            modification_date = isoparse(_modification_date)

        library_scan_request = cls(
            total_files=total_files,
            processed_files=processed_files,
            errored_files=errored_files,
            status=status,
            creation_date=creation_date,
            modification_date=modification_date,
        )

        library_scan_request.additional_properties = d
        return library_scan_request

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
