import datetime
import json
from typing import Any, Dict, List, Tuple, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.content_request import ContentRequest
from ..models.privacy_level_enum import PrivacyLevelEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserWriteRequest")


@attr.s(auto_attribs=True)
class UserWriteRequest:
    """
    Attributes:
        avatar (str):
        name (Union[Unset, str]):
        privacy_level (Union[Unset, PrivacyLevelEnum]):
        instance_support_message_display_date (Union[Unset, None, datetime.datetime]):
        funkwhale_support_message_display_date (Union[Unset, None, datetime.datetime]):
        summary (Union[Unset, None, ContentRequest]):
    """

    avatar: str
    name: Union[Unset, str] = UNSET
    privacy_level: Union[Unset, PrivacyLevelEnum] = UNSET
    instance_support_message_display_date: Union[Unset, None, datetime.datetime] = UNSET
    funkwhale_support_message_display_date: Union[Unset, None, datetime.datetime] = UNSET
    summary: Union[Unset, None, ContentRequest] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        avatar = self.avatar
        name = self.name
        privacy_level: Union[Unset, str] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = self.privacy_level.value

        instance_support_message_display_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.instance_support_message_display_date, Unset):
            instance_support_message_display_date = (
                self.instance_support_message_display_date.isoformat()
                if self.instance_support_message_display_date
                else None
            )

        funkwhale_support_message_display_date: Union[Unset, None, str] = UNSET
        if not isinstance(self.funkwhale_support_message_display_date, Unset):
            funkwhale_support_message_display_date = (
                self.funkwhale_support_message_display_date.isoformat()
                if self.funkwhale_support_message_display_date
                else None
            )

        summary: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict() if self.summary else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "avatar": avatar,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level
        if instance_support_message_display_date is not UNSET:
            field_dict["instance_support_message_display_date"] = instance_support_message_display_date
        if funkwhale_support_message_display_date is not UNSET:
            field_dict["funkwhale_support_message_display_date"] = funkwhale_support_message_display_date
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        avatar = self.avatar if isinstance(self.avatar, Unset) else (None, str(self.avatar).encode(), "text/plain")
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")
        privacy_level: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.privacy_level, Unset):
            privacy_level = (None, str(self.privacy_level.value).encode(), "text/plain")

        instance_support_message_display_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.instance_support_message_display_date, Unset):
            instance_support_message_display_date = (
                self.instance_support_message_display_date.isoformat().encode()
                if self.instance_support_message_display_date
                else None
            )

        funkwhale_support_message_display_date: Union[Unset, None, bytes] = UNSET
        if not isinstance(self.funkwhale_support_message_display_date, Unset):
            funkwhale_support_message_display_date = (
                self.funkwhale_support_message_display_date.isoformat().encode()
                if self.funkwhale_support_message_display_date
                else None
            )

        summary: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = (None, json.dumps(self.summary.to_dict()).encode(), "application/json") if self.summary else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "avatar": avatar,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if privacy_level is not UNSET:
            field_dict["privacy_level"] = privacy_level
        if instance_support_message_display_date is not UNSET:
            field_dict["instance_support_message_display_date"] = instance_support_message_display_date
        if funkwhale_support_message_display_date is not UNSET:
            field_dict["funkwhale_support_message_display_date"] = funkwhale_support_message_display_date
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        avatar = d.pop("avatar")

        name = d.pop("name", UNSET)

        _privacy_level = d.pop("privacy_level", UNSET)
        privacy_level: Union[Unset, PrivacyLevelEnum]
        if isinstance(_privacy_level, Unset):
            privacy_level = UNSET
        else:
            privacy_level = PrivacyLevelEnum(_privacy_level)

        _instance_support_message_display_date = d.pop("instance_support_message_display_date", UNSET)
        instance_support_message_display_date: Union[Unset, None, datetime.datetime]
        if _instance_support_message_display_date is None:
            instance_support_message_display_date = None
        elif isinstance(_instance_support_message_display_date, Unset):
            instance_support_message_display_date = UNSET
        else:
            instance_support_message_display_date = isoparse(_instance_support_message_display_date)

        _funkwhale_support_message_display_date = d.pop("funkwhale_support_message_display_date", UNSET)
        funkwhale_support_message_display_date: Union[Unset, None, datetime.datetime]
        if _funkwhale_support_message_display_date is None:
            funkwhale_support_message_display_date = None
        elif isinstance(_funkwhale_support_message_display_date, Unset):
            funkwhale_support_message_display_date = UNSET
        else:
            funkwhale_support_message_display_date = isoparse(_funkwhale_support_message_display_date)

        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, None, ContentRequest]
        if _summary is None:
            summary = None
        elif isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = ContentRequest.from_dict(_summary)

        user_write_request = cls(
            avatar=avatar,
            name=name,
            privacy_level=privacy_level,
            instance_support_message_display_date=instance_support_message_display_date,
            funkwhale_support_message_display_date=funkwhale_support_message_display_date,
            summary=summary,
        )

        user_write_request.additional_properties = d
        return user_write_request

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
