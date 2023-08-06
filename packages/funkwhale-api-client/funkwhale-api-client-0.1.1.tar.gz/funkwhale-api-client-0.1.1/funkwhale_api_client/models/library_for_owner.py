import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.library_privacy_level_enum import LibraryPrivacyLevelEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryForOwner")


@attr.s(auto_attribs=True)
class LibraryForOwner:
    """
    Attributes:
        uuid (str):
        fid (str):
        name (str):
        uploads_count (int):
        size (int):
        creation_date (datetime.datetime):
        actor (APIActor):
        description (Union[Unset, None, str]):
        privacy_level (Union[Unset, LibraryPrivacyLevelEnum]):
    """

    uuid: str
    fid: str
    name: str
    uploads_count: int
    size: int
    creation_date: datetime.datetime
    actor: APIActor
    description: Union[Unset, None, str] = UNSET
    privacy_level: Union[Unset, LibraryPrivacyLevelEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        fid = self.fid
        name = self.name
        uploads_count = self.uploads_count
        size = self.size
        creation_date = self.creation_date.isoformat()

        actor = self.actor.to_dict()

        description = self.description
        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "fid": fid,
                "name": name,
                "uploads_count": uploads_count,
                "size": size,
                "creation_date": creation_date,
                "actor": actor,
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
        uuid = d.pop("uuid")

        fid = d.pop("fid")

        name = d.pop("name")

        uploads_count = d.pop("uploads_count")

        size = d.pop("size")

        creation_date = isoparse(d.pop("creation_date"))

        actor = APIActor.from_dict(d.pop("actor"))

        description = d.pop("description", UNSET)

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, LibraryPrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = LibraryPrivacyLevelEnum(_privacy_level)

        library_for_owner = cls(
            uuid=uuid,
            fid=fid,
            name=name,
            uploads_count=uploads_count,
            size=size,
            creation_date=creation_date,
            actor=actor,
            description=description,
            privacy_level=privacy_level,
        )

        library_for_owner.additional_properties = d
        return library_for_owner

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
