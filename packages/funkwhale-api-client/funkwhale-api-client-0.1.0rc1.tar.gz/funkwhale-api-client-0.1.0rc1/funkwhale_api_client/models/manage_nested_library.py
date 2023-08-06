import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.library_privacy_level_enum import LibraryPrivacyLevelEnum
from ..models.manage_base_actor import ManageBaseActor
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageNestedLibrary")


@attr.s(auto_attribs=True)
class ManageNestedLibrary:
    """
    Attributes:
        id (int):
        fid (str):
        name (str):
        domain (str):
        is_local (bool):
        followers_url (str):
        actor (ManageBaseActor):
        uuid (Union[Unset, str]):
        url (Union[Unset, None, str]):
        description (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        privacy_level (Union[Unset, LibraryPrivacyLevelEnum]):
    """

    id: int
    fid: str
    name: str
    domain: str
    is_local: bool
    followers_url: str
    actor: ManageBaseActor
    uuid: Union[Unset, str] = UNSET
    url: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    privacy_level: Union[Unset, LibraryPrivacyLevelEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        fid = self.fid
        name = self.name
        domain = self.domain
        is_local = self.is_local
        followers_url = self.followers_url
        actor = self.actor.to_dict()

        uuid = self.uuid
        url = self.url
        description = self.description
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fid": fid,
                "name": name,
                "domain": domain,
                "is_local": is_local,
                "followers_url": followers_url,
                "actor": actor,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        fid = d.pop("fid")

        name = d.pop("name")

        domain = d.pop("domain")

        is_local = d.pop("is_local")

        followers_url = d.pop("followers_url")

        actor = ManageBaseActor.from_dict(d.pop("actor"))

        uuid = d.pop("uuid", UNSET)

        url = d.pop("url", UNSET)

        description = d.pop("description", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, LibraryPrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = LibraryPrivacyLevelEnum(_privacy_level)

        manage_nested_library = cls(
            id=id,
            fid=fid,
            name=name,
            domain=domain,
            is_local=is_local,
            followers_url=followers_url,
            actor=actor,
            uuid=uuid,
            url=url,
            description=description,
            creation_date=creation_date,
            privacy_level=privacy_level,
        )

        manage_nested_library.additional_properties = d
        return manage_nested_library

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
