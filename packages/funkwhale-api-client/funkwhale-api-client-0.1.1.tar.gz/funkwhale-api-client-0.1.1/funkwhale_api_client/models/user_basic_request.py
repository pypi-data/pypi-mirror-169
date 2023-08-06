import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.attachment_request import AttachmentRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBasicRequest")


@attr.s(auto_attribs=True)
class UserBasicRequest:
    """
    Attributes:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        name (Union[Unset, str]):
        date_joined (Union[Unset, datetime.datetime]):
        avatar (Optional[AttachmentRequest]):
    """

    username: str
    avatar: Optional[AttachmentRequest]
    name: Union[Unset, str] = UNSET
    date_joined: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        name = self.name
        date_joined: Union[Unset, str] = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        avatar = self.avatar.to_dict() if self.avatar else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "avatar": avatar,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        name = d.pop("name", UNSET)

        _date_joined = d.pop("date_joined", UNSET)
        date_joined: Union[Unset, datetime.datetime]
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = isoparse(_date_joined)

        _avatar = d.pop("avatar")
        avatar: Optional[AttachmentRequest]
        if _avatar is None:
            avatar = None
        else:
            avatar = AttachmentRequest.from_dict(_avatar)

        user_basic_request = cls(
            username=username,
            name=name,
            date_joined=date_joined,
            avatar=avatar,
        )

        user_basic_request.additional_properties = d
        return user_basic_request

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
