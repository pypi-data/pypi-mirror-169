import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.manage_target import ManageTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageInstancePolicy")


@attr.s(auto_attribs=True)
class ManageInstancePolicy:
    """
    Attributes:
        id (int):
        uuid (str):
        target (ManageTarget):
        creation_date (datetime.datetime):
        actor (str):
        summary (Union[Unset, None, str]):
        is_active (Union[Unset, bool]):
        block_all (Union[Unset, bool]):
        silence_activity (Union[Unset, bool]):
        silence_notifications (Union[Unset, bool]):
        reject_media (Union[Unset, bool]):
    """

    id: int
    uuid: str
    target: ManageTarget
    creation_date: datetime.datetime
    actor: str
    summary: Union[Unset, None, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    block_all: Union[Unset, bool] = UNSET
    silence_activity: Union[Unset, bool] = UNSET
    silence_notifications: Union[Unset, bool] = UNSET
    reject_media: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        uuid = self.uuid
        target = self.target.to_dict()

        creation_date = self.creation_date.isoformat()

        actor = self.actor
        summary = self.summary
        is_active = self.is_active
        block_all = self.block_all
        silence_activity = self.silence_activity
        silence_notifications = self.silence_notifications
        reject_media = self.reject_media

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "target": target,
                "creation_date": creation_date,
                "actor": actor,
            }
        )
        if summary is not UNSET:
            field_dict["summary"] = summary
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if block_all is not UNSET:
            field_dict["block_all"] = block_all
        if silence_activity is not UNSET:
            field_dict["silence_activity"] = silence_activity
        if silence_notifications is not UNSET:
            field_dict["silence_notifications"] = silence_notifications
        if reject_media is not UNSET:
            field_dict["reject_media"] = reject_media

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        uuid = d.pop("uuid")

        target = ManageTarget.from_dict(d.pop("target"))

        creation_date = isoparse(d.pop("creation_date"))

        actor = d.pop("actor")

        summary = d.pop("summary", UNSET)

        is_active = d.pop("is_active", UNSET)

        block_all = d.pop("block_all", UNSET)

        silence_activity = d.pop("silence_activity", UNSET)

        silence_notifications = d.pop("silence_notifications", UNSET)

        reject_media = d.pop("reject_media", UNSET)

        manage_instance_policy = cls(
            id=id,
            uuid=uuid,
            target=target,
            creation_date=creation_date,
            actor=actor,
            summary=summary,
            is_active=is_active,
            block_all=block_all,
            silence_activity=silence_activity,
            silence_notifications=silence_notifications,
            reject_media=reject_media,
        )

        manage_instance_policy.additional_properties = d
        return manage_instance_policy

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
