import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.library_privacy_level_enum import LibraryPrivacyLevelEnum
from ..models.manage_base_actor import ManageBaseActor
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageLibrary")


@attr.s(auto_attribs=True)
class ManageLibrary:
    """
    Attributes:
        id (int):
        uuid (str):
        fid (str):
        name (str):
        domain (str):
        is_local (bool):
        creation_date (datetime.datetime):
        uploads_count (int):
        followers_count (int):
        followers_url (str):
        actor (ManageBaseActor):
        url (Optional[str]):
        description (Union[Unset, None, str]):
        privacy_level (Union[Unset, LibraryPrivacyLevelEnum]):
    """

    id: int
    uuid: str
    fid: str
    name: str
    domain: str
    is_local: bool
    creation_date: datetime.datetime
    uploads_count: int
    followers_count: int
    followers_url: str
    actor: ManageBaseActor
    url: Optional[str]
    description: Union[Unset, None, str] = UNSET
    privacy_level: Union[Unset, LibraryPrivacyLevelEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        uuid = self.uuid
        fid = self.fid
        name = self.name
        domain = self.domain
        is_local = self.is_local
        creation_date = self.creation_date.isoformat()

        uploads_count = self.uploads_count
        followers_count = self.followers_count
        followers_url = self.followers_url
        actor = self.actor.to_dict()

        url = self.url
        description = self.description
        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "fid": fid,
                "name": name,
                "domain": domain,
                "is_local": is_local,
                "creation_date": creation_date,
                "uploads_count": uploads_count,
                "followers_count": followers_count,
                "followers_url": followers_url,
                "actor": actor,
                "url": url,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        uuid = d.pop("uuid")

        fid = d.pop("fid")

        name = d.pop("name")

        domain = d.pop("domain")

        is_local = d.pop("is_local")

        creation_date = isoparse(d.pop("creation_date"))

        uploads_count = d.pop("uploads_count")

        followers_count = d.pop("followers_count")

        followers_url = d.pop("followers_url")

        actor = ManageBaseActor.from_dict(d.pop("actor"))

        url = d.pop("url")

        description = d.pop("description", UNSET)

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, LibraryPrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = LibraryPrivacyLevelEnum(_privacy_level)

        manage_library = cls(
            id=id,
            uuid=uuid,
            fid=fid,
            name=name,
            domain=domain,
            is_local=is_local,
            creation_date=creation_date,
            uploads_count=uploads_count,
            followers_count=followers_count,
            followers_url=followers_url,
            actor=actor,
            url=url,
            description=description,
            privacy_level=privacy_level,
        )

        manage_library.additional_properties = d
        return manage_library

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
