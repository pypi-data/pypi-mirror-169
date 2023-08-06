import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListeningWriteRequest")


@attr.s(auto_attribs=True)
class ListeningWriteRequest:
    """
    Attributes:
        track (int):
        user (Union[Unset, None, int]):
        creation_date (Union[Unset, None, datetime.datetime]):
    """

    track: int
    user: Union[Unset, None, int] = UNSET
    creation_date: Union[Unset, None, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        track = self.track
        user = self.user
        creation_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat() if self.creation_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "track": track,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        track = self.track if isinstance(self.track, Unset) else (None, str(self.track).encode(), "text/plain")
        user = self.user if isinstance(self.user, Unset) else (None, str(self.user).encode(), "text/plain")
        creation_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat().encode() if self.creation_date else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "track": track,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        track = d.pop("track")

        user = d.pop("user", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, None, datetime.datetime]
        if _creation_date is None:
            creation_date = None
        elif isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        listening_write_request = cls(
            track=track,
            user=user,
            creation_date=creation_date,
        )

        listening_write_request.additional_properties = d
        return listening_write_request

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
