import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.federation_choice_enum import FederationChoiceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="APIActorRequest")


@attr.s(auto_attribs=True)
class APIActorRequest:
    """
    Attributes:
        fid (str):
        domain (str):
        url (Union[Unset, None, str]):
        creation_date (Union[Unset, datetime.datetime]):
        summary (Union[Unset, None, str]):
        preferred_username (Optional[str]):
        name (Union[Unset, None, str]):
        last_fetch_date (Union[Unset, datetime.datetime]):
        type (Union[Unset, FederationChoiceEnum]):
        manually_approves_followers (Union[Unset, None, bool]):
    """

    fid: str
    domain: str
    preferred_username: Optional[str]
    url: Union[Unset, None, str] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    summary: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    last_fetch_date: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, FederationChoiceEnum] = UNSET
    manually_approves_followers: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fid = self.fid
        domain = self.domain
        url = self.url
        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        summary = self.summary
        preferred_username = self.preferred_username
        name = self.name
        last_fetch_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_fetch_date, Unset):
            last_fetch_date = self.last_fetch_date.isoformat()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        manually_approves_followers = self.manually_approves_followers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fid": fid,
                "domain": domain,
                "preferred_username": preferred_username,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if summary is not UNSET:
            field_dict["summary"] = summary
        if name is not UNSET:
            field_dict["name"] = name
        if last_fetch_date is not UNSET:
            field_dict["last_fetch_date"] = last_fetch_date
        if type is not UNSET:
            field_dict["type"] = type
        if manually_approves_followers is not UNSET:
            field_dict["manually_approves_followers"] = manually_approves_followers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fid = d.pop("fid")

        domain = d.pop("domain")

        url = d.pop("url", UNSET)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        summary = d.pop("summary", UNSET)

        preferred_username = d.pop("preferred_username")

        name = d.pop("name", UNSET)

        _last_fetch_date = d.pop("last_fetch_date", UNSET)
        last_fetch_date: Union[Unset, datetime.datetime]
        if isinstance(_last_fetch_date, Unset):
            last_fetch_date = UNSET
        else:
            last_fetch_date = isoparse(_last_fetch_date)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FederationChoiceEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FederationChoiceEnum(_type)

        manually_approves_followers = d.pop("manually_approves_followers", UNSET)

        api_actor_request = cls(
            fid=fid,
            domain=domain,
            url=url,
            creation_date=creation_date,
            summary=summary,
            preferred_username=preferred_username,
            name=name,
            last_fetch_date=last_fetch_date,
            type=type,
            manually_approves_followers=manually_approves_followers,
        )

        api_actor_request.additional_properties = d
        return api_actor_request

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
