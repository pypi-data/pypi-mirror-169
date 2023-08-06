import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.activity_object import ActivityObject
from ..models.activity_payload import ActivityPayload
from ..models.activity_related_object import ActivityRelatedObject
from ..models.activity_target import ActivityTarget
from ..models.api_actor import APIActor
from ..types import UNSET, Unset

T = TypeVar("T", bound="Activity")


@attr.s(auto_attribs=True)
class Activity:
    """
    Attributes:
        actor (APIActor):
        related_object (ActivityRelatedObject):
        uuid (Union[Unset, str]):
        fid (Union[Unset, None, str]):
        payload (Union[Unset, ActivityPayload]):
        object_ (Optional[ActivityObject]):
        target (Optional[ActivityTarget]):
        creation_date (Union[Unset, datetime.datetime]):
        type (Union[Unset, None, str]):
    """

    actor: APIActor
    related_object: ActivityRelatedObject
    object_: Optional[ActivityObject]
    target: Optional[ActivityTarget]
    uuid: Union[Unset, str] = UNSET
    fid: Union[Unset, None, str] = UNSET
    payload: Union[Unset, ActivityPayload] = UNSET
    creation_date: Union[Unset, datetime.datetime] = UNSET
    type: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        actor = self.actor.to_dict()

        related_object = self.related_object.to_dict()

        uuid = self.uuid
        fid = self.fid
        payload: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        object_ = self.object_.to_dict() if self.object_ else None

        target = self.target.to_dict() if self.target else None

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actor": actor,
                "related_object": related_object,
                "object": object_,
                "target": target,
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
        actor = APIActor.from_dict(d.pop("actor"))

        related_object = ActivityRelatedObject.from_dict(d.pop("related_object"))

        uuid = d.pop("uuid", UNSET)

        fid = d.pop("fid", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, ActivityPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = ActivityPayload.from_dict(_payload)

        _object_ = d.pop("object")
        object_: Optional[ActivityObject]
        if _object_ is None:
            object_ = None
        else:
            object_ = ActivityObject.from_dict(_object_)

        _target = d.pop("target")
        target: Optional[ActivityTarget]
        if _target is None:
            target = None
        else:
            target = ActivityTarget.from_dict(_target)

        _creation_date = d.pop("creation_date", UNSET)
        creation_date: Union[Unset, datetime.datetime]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date)

        type = d.pop("type", UNSET)

        activity = cls(
            actor=actor,
            related_object=related_object,
            uuid=uuid,
            fid=fid,
            payload=payload,
            object_=object_,
            target=target,
            creation_date=creation_date,
            type=type,
        )

        activity.additional_properties = d
        return activity

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
