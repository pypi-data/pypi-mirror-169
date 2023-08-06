import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.manage_user_actor import ManageUserActor
from ..models.privacy_level_enum import PrivacyLevelEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageUser")


@attr.s(auto_attribs=True)
class ManageUser:
    """
    Attributes:
        id (int):
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        actor (ManageUserActor):
        email (str):
        date_joined (datetime.datetime):
        privacy_level (PrivacyLevelEnum):
        full_username (str):
        name (Union[Unset, str]):
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        is_staff (Union[Unset, bool]): Designates whether the user can log into this admin site.
        is_superuser (Union[Unset, bool]): Designates that this user has all permissions without explicitly assigning
            them.
        last_activity (Optional[datetime.datetime]):
        upload_quota (Union[Unset, None, int]):
    """

    id: int
    username: str
    actor: ManageUserActor
    email: str
    date_joined: datetime.datetime
    privacy_level: PrivacyLevelEnum
    full_username: str
    last_activity: Optional[datetime.datetime]
    name: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_staff: Union[Unset, bool] = UNSET
    is_superuser: Union[Unset, bool] = UNSET
    upload_quota: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        username = self.username
        actor = self.actor.to_dict()

        email = self.email
        date_joined = self.date_joined.isoformat()

        privacy_level = self.privacy_level.value

        full_username = self.full_username
        name = self.name
        is_active = self.is_active
        is_staff = self.is_staff
        is_superuser = self.is_superuser
        last_activity = self.last_activity.isoformat() if self.last_activity else None

        upload_quota = self.upload_quota

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
                "actor": actor,
                "email": email,
                "date_joined": date_joined,
                "privacy_level": privacy_level,
                "full_username": full_username,
                "last_activity": last_activity,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if upload_quota is not UNSET:
            field_dict["upload_quota"] = upload_quota

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        username = d.pop("username")

        actor = ManageUserActor.from_dict(d.pop("actor"))

        email = d.pop("email")

        date_joined = isoparse(d.pop("date_joined"))

        privacy_level = PrivacyLevelEnum(d.pop("privacy_level"))

        full_username = d.pop("full_username")

        name = d.pop("name", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        _last_activity = d.pop("last_activity")
        last_activity: Optional[datetime.datetime]
        if _last_activity is None:
            last_activity = None
        else:
            last_activity = isoparse(_last_activity)

        upload_quota = d.pop("upload_quota", UNSET)

        manage_user = cls(
            id=id,
            username=username,
            actor=actor,
            email=email,
            date_joined=date_joined,
            privacy_level=privacy_level,
            full_username=full_username,
            name=name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_activity=last_activity,
            upload_quota=upload_quota,
        )

        manage_user.additional_properties = d
        return manage_user

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
