import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.federation_choice_enum import FederationChoiceEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageBaseActorRequest")


@attr.s(auto_attribs=True)
class ManageBaseActorRequest:
    """
    Attributes:
        fid (str):
        domain (str):
        url (Union[Unset, None, str]):
        preferred_username (Optional[str]):
        name (Union[Unset, None, str]):
        summary (Union[Unset, None, str]):
        type (Union[Unset, FederationChoiceEnum]):
        last_fetch_date (Union[Unset, datetime.datetime]):
        inbox_url (Union[Unset, None, str]):
        outbox_url (Union[Unset, None, str]):
        shared_inbox_url (Union[Unset, None, str]):
        manually_approves_followers (Union[Unset, None, bool]):
    """

    fid: str
    domain: str
    preferred_username: Optional[str]
    url: Union[Unset, None, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    summary: Union[Unset, None, str] = UNSET
    type: Union[Unset, FederationChoiceEnum] = UNSET
    last_fetch_date: Union[Unset, datetime.datetime] = UNSET
    inbox_url: Union[Unset, None, str] = UNSET
    outbox_url: Union[Unset, None, str] = UNSET
    shared_inbox_url: Union[Unset, None, str] = UNSET
    manually_approves_followers: Union[Unset, None, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fid = self.fid
        domain = self.domain
        url = self.url
        preferred_username = self.preferred_username
        name = self.name
        summary = self.summary
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        last_fetch_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_fetch_date, Unset):
            last_fetch_date = self.last_fetch_date.isoformat()

        inbox_url = self.inbox_url
        outbox_url = self.outbox_url
        shared_inbox_url = self.shared_inbox_url
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
        if name is not UNSET:
            field_dict["name"] = name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if type is not UNSET:
            field_dict["type"] = type
        if last_fetch_date is not UNSET:
            field_dict["last_fetch_date"] = last_fetch_date
        if inbox_url is not UNSET:
            field_dict["inbox_url"] = inbox_url
        if outbox_url is not UNSET:
            field_dict["outbox_url"] = outbox_url
        if shared_inbox_url is not UNSET:
            field_dict["shared_inbox_url"] = shared_inbox_url
        if manually_approves_followers is not UNSET:
            field_dict["manually_approves_followers"] = manually_approves_followers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fid = d.pop("fid")

        domain = d.pop("domain")

        url = d.pop("url", UNSET)

        preferred_username = d.pop("preferred_username")

        name = d.pop("name", UNSET)

        summary = d.pop("summary", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, FederationChoiceEnum]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FederationChoiceEnum(_type)

        _last_fetch_date = d.pop("last_fetch_date", UNSET)
        last_fetch_date: Union[Unset, datetime.datetime]
        if isinstance(_last_fetch_date, Unset):
            last_fetch_date = UNSET
        else:
            last_fetch_date = isoparse(_last_fetch_date)

        inbox_url = d.pop("inbox_url", UNSET)

        outbox_url = d.pop("outbox_url", UNSET)

        shared_inbox_url = d.pop("shared_inbox_url", UNSET)

        manually_approves_followers = d.pop("manually_approves_followers", UNSET)

        manage_base_actor_request = cls(
            fid=fid,
            domain=domain,
            url=url,
            preferred_username=preferred_username,
            name=name,
            summary=summary,
            type=type,
            last_fetch_date=last_fetch_date,
            inbox_url=inbox_url,
            outbox_url=outbox_url,
            shared_inbox_url=shared_inbox_url,
            manually_approves_followers=manually_approves_followers,
        )

        manage_base_actor_request.additional_properties = d
        return manage_base_actor_request

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
