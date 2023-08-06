import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.api_actor import APIActor
from ..models.library_privacy_level_enum import LibraryPrivacyLevelEnum
from ..models.library_scan import LibraryScan
from ..models.nested_library_follow import NestedLibraryFollow
from ..types import UNSET, Unset

T = TypeVar("T", bound="Library")


@attr.s(auto_attribs=True)
class Library:
    """
    Attributes:
        fid (str):
        actor (APIActor):
        name (str):
        uploads_count (int):
        uuid (Union[Unset, str]):
        description (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        privacy_level (Union[Unset, LibraryPrivacyLevelEnum]):
        follow (Union[Unset, None, NestedLibraryFollow]):
        latest_scan (Union[Unset, None, LibraryScan]):
    """

    fid: str
    actor: APIActor
    name: str
    uploads_count: int
    uuid: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    privacy_level: Union[Unset, LibraryPrivacyLevelEnum] = UNSET
    follow: Union[Unset, None, NestedLibraryFollow] = UNSET
    latest_scan: Union[Unset, None, LibraryScan] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fid = self.fid
        actor = self.actor.to_dict()

        name = self.name
        uploads_count = self.uploads_count
        uuid = self.uuid
        description = self.description
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        follow: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.follow, Unset):
            follow = self.follow.to_dict() if self.follow else None

        latest_scan: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.latest_scan, Unset):
            latest_scan = self.latest_scan.to_dict() if self.latest_scan else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fid": fid,
                "actor": actor,
                "name": name,
                "uploads_count": uploads_count,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if description is not UNSET:
            field_dict["description"] = description
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level
        if follow is not UNSET:
            field_dict["follow"] = follow
        if latest_scan is not UNSET:
            field_dict["latest_scan"] = latest_scan

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fid = d.pop("fid")

        actor = APIActor.from_dict(d.pop("actor"))

        name = d.pop("name")

        uploads_count = d.pop("uploads_count")

        uuid = d.pop("uuid", UNSET)

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

        _follow = d.pop("follow", UNSET)
        follow: Union[Unset, None, NestedLibraryFollow]
        if _follow is None:
            follow = None
        elif isinstance(_follow, Unset):
            follow = UNSET
        else:
            follow = NestedLibraryFollow.from_dict(_follow)

        _latest_scan = d.pop("latest_scan", UNSET)
        latest_scan: Union[Unset, None, LibraryScan]
        if _latest_scan is None:
            latest_scan = None
        elif isinstance(_latest_scan, Unset):
            latest_scan = UNSET
        else:
            latest_scan = LibraryScan.from_dict(_latest_scan)

        library = cls(
            fid=fid,
            actor=actor,
            name=name,
            uploads_count=uploads_count,
            uuid=uuid,
            description=description,
            creation_date=creation_date,
            privacy_level=privacy_level,
            follow=follow,
            latest_scan=latest_scan,
        )

        library.additional_properties = d
        return library

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
