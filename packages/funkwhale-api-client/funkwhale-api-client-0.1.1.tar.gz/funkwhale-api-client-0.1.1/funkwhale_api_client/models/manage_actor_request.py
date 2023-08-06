import datetime
import json
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.federation_choice_enum import FederationChoiceEnum
from ..models.manage_user_request import ManageUserRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageActorRequest")


@attr.s(auto_attribs=True)
class ManageActorRequest:
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
        user (Optional[ManageUserRequest]):
    """

    fid: str
    domain: str
    preferred_username: Optional[str]
    user: Optional[ManageUserRequest]
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
        user = self.user.to_dict() if self.user else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fid": fid,
                "domain": domain,
                "preferred_username": preferred_username,
                "user": user,
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

    def to_multipart(self) -> Dict[str, Any]:
        fid = self.fid if isinstance(self.fid, Unset) else (None, str(self.fid).encode(), "text/plain")
        domain = self.domain if isinstance(self.domain, Unset) else (None, str(self.domain).encode(), "text/plain")
        url = self.url if isinstance(self.url, Unset) else (None, str(self.url).encode(), "text/plain")
        preferred_username = (
            self.preferred_username
            if isinstance(self.preferred_username, Unset)
            else (None, str(self.preferred_username).encode(), "text/plain")
        )
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        summary = self.summary if isinstance(self.summary, Unset) else (None, str(self.summary).encode(), "text/plain")
        type: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.type, Unset):
            type = (None, str(self.type.value).encode(), "text/plain")

        last_fetch_date: Union[Unset, bytes] = UNSET
        if not isinstance(self.last_fetch_date, Unset):
            last_fetch_date = self.last_fetch_date.isoformat().encode()

        inbox_url = (
            self.inbox_url if isinstance(self.inbox_url, Unset) else (None, str(self.inbox_url).encode(), "text/plain")
        )
        outbox_url = (
            self.outbox_url
            if isinstance(self.outbox_url, Unset)
            else (None, str(self.outbox_url).encode(), "text/plain")
        )
        shared_inbox_url = (
            self.shared_inbox_url
            if isinstance(self.shared_inbox_url, Unset)
            else (None, str(self.shared_inbox_url).encode(), "text/plain")
        )
        manually_approves_followers = (
            self.manually_approves_followers
            if isinstance(self.manually_approves_followers, Unset)
            else (None, str(self.manually_approves_followers).encode(), "text/plain")
        )
        user = (None, json.dumps(self.user.to_dict()).encode(), "application/json") if self.user else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "fid": fid,
                "domain": domain,
                "preferred_username": preferred_username,
                "user": user,
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

        _user = d.pop("user")
        user: Optional[ManageUserRequest]
        if _user is None:
            user = None
        else:
            user = ManageUserRequest.from_dict(_user)

        manage_actor_request = cls(
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
            user=user,
        )

        manage_actor_request.additional_properties = d
        return manage_actor_request

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
