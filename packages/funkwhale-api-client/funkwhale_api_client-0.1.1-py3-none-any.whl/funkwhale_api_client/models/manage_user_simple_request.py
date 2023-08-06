import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.privacy_level_enum import PrivacyLevelEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageUserSimpleRequest")


@attr.s(auto_attribs=True)
class ManageUserSimpleRequest:
    """
    Attributes:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        email (Union[Unset, str]):
        name (Union[Unset, str]):
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        is_staff (Union[Unset, bool]): Designates whether the user can log into this admin site.
        is_superuser (Union[Unset, bool]): Designates that this user has all permissions without explicitly assigning
            them.
        date_joined (Union[Unset, datetime.datetime]):
        last_activity (Union[Unset, None, datetime.datetime]):
        privacy_level (Union[Unset, PrivacyLevelEnum]):
        upload_quota (Union[Unset, None, int]):
    """

    username: str
    email: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_staff: Union[Unset, bool] = UNSET
    is_superuser: Union[Unset, bool] = UNSET
    date_joined: Union[Unset, datetime.datetime] = UNSET
    last_activity: Union[Unset, None, datetime.datetime] = UNSET
    privacy_level: Union[Unset, PrivacyLevelEnum] = UNSET
    upload_quota: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        email = self.email
        name = self.name
        is_active = self.is_active
        is_staff = self.is_staff
        is_superuser = self.is_superuser
        date_joined: Union[Unset, str] = UNSET
        if not isinstance(self.date_joined, Unset):
            date_joined = self.date_joined.isoformat()

        last_activity: Union[Unset, None, str] = UNSET
        if not isinstance(self.last_activity, Unset):
            last_activity = self.last_activity.isoformat() if self.last_activity else None

        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        upload_quota = self.upload_quota

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
            }
        )
        if email is not UNSET:
            field_dict["email"] = email
        if name is not UNSET:
            field_dict["name"] = name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if date_joined is not UNSET:
            field_dict["date_joined"] = date_joined
        if last_activity is not UNSET:
            field_dict["last_activity"] = last_activity
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level
        if upload_quota is not UNSET:
            field_dict["upload_quota"] = upload_quota

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        email = d.pop("email", UNSET)

        name = d.pop("name", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        _date_joined = d.pop("date_joined", UNSET)
        date_joined: Union[Unset, datetime.datetime]
        if isinstance(_date_joined, Unset):
            date_joined = UNSET
        else:
            date_joined = isoparse(_date_joined)

        _last_activity = d.pop("last_activity", UNSET)
        last_activity: Union[Unset, None, datetime.datetime]
        if _last_activity is None:
            last_activity = None
        elif isinstance(_last_activity, Unset):
            last_activity = UNSET
        else:
            last_activity = isoparse(_last_activity)

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, PrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = PrivacyLevelEnum(_privacy_level)

        upload_quota = d.pop("upload_quota", UNSET)

        manage_user_simple_request = cls(
            username=username,
            email=email,
            name=name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            date_joined=date_joined,
            last_activity=last_activity,
            privacy_level=privacy_level,
            upload_quota=upload_quota,
        )

        manage_user_simple_request.additional_properties = d
        return manage_user_simple_request

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
