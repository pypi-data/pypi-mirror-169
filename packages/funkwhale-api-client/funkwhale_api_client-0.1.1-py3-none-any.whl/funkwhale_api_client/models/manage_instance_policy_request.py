import json
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.manage_target_request import ManageTargetRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManageInstancePolicyRequest")


@attr.s(auto_attribs=True)
class ManageInstancePolicyRequest:
    """
    Attributes:
        target (ManageTargetRequest):
        summary (Union[Unset, None, str]):
        is_active (Union[Unset, bool]):
        block_all (Union[Unset, bool]):
        silence_activity (Union[Unset, bool]):
        silence_notifications (Union[Unset, bool]):
        reject_media (Union[Unset, bool]):
    """

    target: ManageTargetRequest
    summary: Union[Unset, None, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    block_all: Union[Unset, bool] = UNSET
    silence_activity: Union[Unset, bool] = UNSET
    silence_notifications: Union[Unset, bool] = UNSET
    reject_media: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target = self.target.to_dict()

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
                "target": target,
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

    def to_multipart(self) -> Dict[str, Any]:
        target = (None, json.dumps(self.target.to_dict()).encode(), "application/json")

        summary = self.summary if isinstance(self.summary, Unset) else (None, str(self.summary).encode(), "text/plain")
        is_active = (
            self.is_active if isinstance(self.is_active, Unset) else (None, str(self.is_active).encode(), "text/plain")
        )
        block_all = (
            self.block_all if isinstance(self.block_all, Unset) else (None, str(self.block_all).encode(), "text/plain")
        )
        silence_activity = (
            self.silence_activity
            if isinstance(self.silence_activity, Unset)
            else (None, str(self.silence_activity).encode(), "text/plain")
        )
        silence_notifications = (
            self.silence_notifications
            if isinstance(self.silence_notifications, Unset)
            else (None, str(self.silence_notifications).encode(), "text/plain")
        )
        reject_media = (
            self.reject_media
            if isinstance(self.reject_media, Unset)
            else (None, str(self.reject_media).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "target": target,
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
        target = ManageTargetRequest.from_dict(d.pop("target"))

        summary = d.pop("summary", UNSET)

        is_active = d.pop("is_active", UNSET)

        block_all = d.pop("block_all", UNSET)

        silence_activity = d.pop("silence_activity", UNSET)

        silence_notifications = d.pop("silence_notifications", UNSET)

        reject_media = d.pop("reject_media", UNSET)

        manage_instance_policy_request = cls(
            target=target,
            summary=summary,
            is_active=is_active,
            block_all=block_all,
            silence_activity=silence_activity,
            silence_notifications=silence_notifications,
            reject_media=reject_media,
        )

        manage_instance_policy_request.additional_properties = d
        return manage_instance_policy_request

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
