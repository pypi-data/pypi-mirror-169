import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.activity_request_payload import ActivityRequestPayload
from ..models.api_actor_request import APIActorRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityRequest")


@attr.s(auto_attribs=True)
class ActivityRequest:
    """
    Attributes:
        actor (APIActorRequest):
        uuid (Union[Unset, str]):
        fid (Union[Unset, None, str]):
        payload (Union[Unset, ActivityRequestPayload]):
        creation_date (Union[Unset, datetime.datetime]):
        type (Union[Unset, None, str]):
    """

    actor: APIActorRequest
    uuid: Union[Unset, str] = UNSET
    fid: Union[Unset, None, str] = UNSET
    payload: Union[Unset, ActivityRequestPayload] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actor = self.actor.to_dict()

        uuid = self.uuid
        fid = self.fid
        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actor": actor,
            }
        )
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if fid is not UNSET:
            field_dict["fid"] = fid
        if payload is not UNSET:
            field_dict["payload"] = payload
        if creation_date is not UNSET:
            field_dict["creation_date"] = creation_date
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        actor = APIActorRequest.from_dict(d.pop("actor"))

        uuid = d.pop("uuid", UNSET)

        fid = d.pop("fid", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, ActivityRequestPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ActivityRequestPayload.from_dict(_payload)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        type = d.pop("type", UNSET)

        activity_request = cls(
            actor=actor,
            uuid=uuid,
            fid=fid,
            payload=payload,
            creation_date=creation_date,
            type=type,
        )

        activity_request.additional_properties = d
        return activity_request

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
