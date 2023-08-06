from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedManageUserRequest")


@attr.s(auto_attribs=True)
class PatchedManageUserRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        is_active (Union[Unset, bool]): Designates whether this user should be treated as active. Unselect this instead
            of deleting accounts.
        is_staff (Union[Unset, bool]): Designates whether the user can log into this admin site.
        is_superuser (Union[Unset, bool]): Designates that this user has all permissions without explicitly assigning
            them.
        upload_quota (Union[Unset, None, int]):
    """

    name: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_staff: Union[Unset, bool] = UNSET
    is_superuser: Union[Unset, bool] = UNSET
    upload_quota: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        is_active = self.is_active
        is_staff = self.is_staff
        is_superuser = self.is_superuser
        upload_quota = self.upload_quota

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )
        is_staff = (
            self.is_staff if isinstance(self.is_staff, Unset) else (None, str(self.is_staff).encode(), "text/plain")
        )
        is_superuser = (
            self.is_superuser
            if isinstance(self.is_superuser, Unset)
            else (None, str(self.is_superuser).encode(), "text/plain")
        )
        upload_quota = (
            self.upload_quota
            if isinstance(self.upload_quota, Unset)
            else (None, str(self.upload_quota).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
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
        name = d.pop("name", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_staff = d.pop("is_staff", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        upload_quota = d.pop("upload_quota", UNSET)

        patched_manage_user_request = cls(
            name=name,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            upload_quota=upload_quota,
        )

        patched_manage_user_request.additional_properties = d
        return patched_manage_user_request

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
