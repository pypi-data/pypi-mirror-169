import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.manage_user_simple_request import ManageUserSimpleRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageInvitationRequest")


@attr.s(auto_attribs=True)
class ManageInvitationRequest:
    """
    Attributes:
        owner (Union[Unset, ManageUserSimpleRequest]):
        code (Union[Unset, None, str]):
        users (Union[Unset, List[ManageUserSimpleRequest]]):
    """

    owner: Union[Unset, ManageUserSimpleRequest] = UNSET
    code: Union[Unset, None, str] = UNSET
    users: Union[Unset, List[ManageUserSimpleRequest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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
        field_dict.update({})
        if owner is not UNSET:
            field_dict["owner"] = owner
        if code is not UNSET:
            field_dict["code"] = code
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        owner: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = (None, json.dumps(self.owner.to_dict()).encode(), "application/json")

        code = self.code if isinstance(self.code, Unset) else (None, str(self.code).encode(), "text/plain")
        users: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.users, Unset):
            _temp_users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                _temp_users.append(users_item)
            users = (None, json.dumps(_temp_users).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
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
        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, ManageUserSimpleRequest]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = ManageUserSimpleRequest.from_dict(_owner)

        code = d.pop("code", UNSET)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = ManageUserSimpleRequest.from_dict(users_item_data)

            users.append(users_item)

        manage_invitation_request = cls(
            owner=owner,
            code=code,
            users=users,
        )

        manage_invitation_request.additional_properties = d
        return manage_invitation_request

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
