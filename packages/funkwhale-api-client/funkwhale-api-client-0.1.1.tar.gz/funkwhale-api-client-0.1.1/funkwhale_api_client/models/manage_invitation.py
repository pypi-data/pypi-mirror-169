import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.manage_user_simple import ManageUserSimple
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageInvitation")


@attr.s(auto_attribs=True)
class ManageInvitation:
    """
    Attributes:
        id (int):
        expiration_date (datetime.datetime):
        creation_date (datetime.datetime):
        owner (Union[Unset, ManageUserSimple]):
        code (Union[Unset, None, str]):
        users (Union[Unset, List[ManageUserSimple]]):
    """

    id: int
    expiration_date: datetime.datetime
    creation_date: datetime.datetime
    owner: Union[Unset, ManageUserSimple] = UNSET
    code: Union[Unset, None, str] = UNSET
    users: Union[Unset, List[ManageUserSimple]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        expiration_date = self.expiration_date.isoformat()

        creation_date = self.creation_date.isoformat()

        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        code = self.code
        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "expiration_date": expiration_date,
                "creation_date": creation_date,
            }
        )
        if owner is not UNSET:
            field_dict["owner"] = owner
        if code is not UNSET:
            field_dict["code"] = code
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        expiration_date = isoparse(d.pop("expiration_date"))

        creation_date = isoparse(d.pop("creation_date"))

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, ManageUserSimple]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = ManageUserSimple.from_dict(_owner)

        code = d.pop("code", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = ManageUserSimple.from_dict(users_item_data)

            users.append(users_item)

        manage_invitation = cls(
            id=id,
            expiration_date=expiration_date,
            creation_date=creation_date,
            owner=owner,
            code=code,
            users=users,
        )

        manage_invitation.additional_properties = d
        return manage_invitation

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
