import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.library_privacy_level_enum import LibraryPrivacyLevelEnum
from ..models.manage_base_actor_request import ManageBaseActorRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageLibraryRequest")


@attr.s(auto_attribs=True)
class ManageLibraryRequest:
    """
    Attributes:
        name (str):
        domain (str):
        followers_url (str):
        actor (ManageBaseActorRequest):
        description (Union[Unset, None, str]):
        privacy_level (Union[Unset, LibraryPrivacyLevelEnum]):
    """

    name: str
    domain: str
    followers_url: str
    actor: ManageBaseActorRequest
    description: Union[Unset, None, str] = UNSET
    privacy_level: Union[Unset, LibraryPrivacyLevelEnum] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        domain = self.domain
        followers_url = self.followers_url
        actor = self.actor.to_dict()

        description = self.description
        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "domain": domain,
                "followers_url": followers_url,
                "actor": actor,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        domain = self.domain if isinstance(self.domain, Unset) else (None, str(self.domain).encode(), "text/plain")
        followers_url = (
            self.followers_url
            if isinstance(self.followers_url, Unset)
            else (None, str(self.followers_url).encode(), "text/plain")
        )
        actor = (None, json.dumps(self.actor.to_dict()).encode(), "application/json")

        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        privacy_level: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = (None, str(self.privacy_level.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
                "domain": domain,
                "followers_url": followers_url,
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
        name = d.pop("name")

        domain = d.pop("domain")

        followers_url = d.pop("followers_url")

        actor = ManageBaseActorRequest.from_dict(d.pop("actor"))

        description = d.pop("description", UNSET)

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, LibraryPrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = LibraryPrivacyLevelEnum(_privacy_level)

        manage_library_request = cls(
            name=name,
            domain=domain,
            followers_url=followers_url,
            actor=actor,
            description=description,
            privacy_level=privacy_level,
        )

        manage_library_request.additional_properties = d
        return manage_library_request

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
