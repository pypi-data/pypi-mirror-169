import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr

from ..models.library_privacy_level_enum import LibraryPrivacyLevelEnum
from ..models.manage_base_actor_request import ManageBaseActorRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchedManageLibraryRequest")


@attr.s(auto_attribs=True)
class PatchedManageLibraryRequest:
    """
    Attributes:
        name (Union[Unset, str]):
        description (Union[Unset, None, str]):
        domain (Union[Unset, str]):
        privacy_level (Union[Unset, LibraryPrivacyLevelEnum]):
        followers_url (Union[Unset, str]):
        actor (Union[Unset, ManageBaseActorRequest]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    domain: Union[Unset, str] = UNSET
    privacy_level: Union[Unset, LibraryPrivacyLevelEnum] = UNSET
    followers_url: Union[Unset, str] = UNSET
    actor: Union[Unset, ManageBaseActorRequest] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        domain = self.domain
        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        followers_url = self.followers_url
        actor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if domain is not UNSET:
            field_dict["domain"] = domain
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level
        if followers_url is not UNSET:
            field_dict["followers_url"] = followers_url
        if actor is not UNSET:
            field_dict["actor"] = actor

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        description = (
            self.description
            if isinstance(self.description, Unset)
            else (None, str(self.description).encode(), "text/plain")
        )
        domain = self.domain if isinstance(self.domain, Unset) else (None, str(self.domain).encode(), "text/plain")
        privacy_level: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = (None, str(self.privacy_level.value).encode(), "text/plain")

        followers_url = (
            self.followers_url
            if isinstance(self.followers_url, Unset)
            else (None, str(self.followers_url).encode(), "text/plain")
        )
        actor: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.actor, Unset):
            actor = (None, json.dumps(self.actor.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if domain is not UNSET:
            field_dict["domain"] = domain
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level
        if followers_url is not UNSET:
            field_dict["followers_url"] = followers_url
        if actor is not UNSET:
            field_dict["actor"] = actor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        domain = d.pop("domain", UNSET)

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, LibraryPrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = LibraryPrivacyLevelEnum(_privacy_level)

        followers_url = d.pop("followers_url", UNSET)

        _actor = d.pop("actor", UNSET)
        actor: Union[Unset, ManageBaseActorRequest]
        if isinstance(_actor, Unset):
            actor = UNSET
        else:
            actor = ManageBaseActorRequest.from_dict(_actor)

        patched_manage_library_request = cls(
            name=name,
            description=description,
            domain=domain,
            privacy_level=privacy_level,
            followers_url=followers_url,
            actor=actor,
        )

        patched_manage_library_request.additional_properties = d
        return patched_manage_library_request

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
